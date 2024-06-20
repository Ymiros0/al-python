from luatable import table, setmetatable, Clone, ipairs
from Vector3 import Vector3
import math

from support.utils import Tool

import BattleAttr
import BattleBulletEvent
import BattleDataProxy
import BattleFormulas
up = Vector3.up
import BattleVariable
import BattleConfig
import BattleTargetChoise
viewFPS = 1 / BattleConfig.viewFPS
import BattleConst
from Framework.event import EventDispatcher, Event
from component import BattleCubeCldComponent

class BattleBulletUnit:
	__name = "BattleBulletUnit"

	ACC_INTERVAL = BattleConfig.calcInterval
	TRACKER_ANGLE = math.cos(math.deg2Rad * 10)
	MIRROR_RES = "_mirror"

	def doAccelerate(self, arg_1_1):
		var_1_0, var_1_1 = self.GetAcceleration(arg_1_1)

		if var_1_0 == 0 and var_1_1 == 0:
			return

		if var_1_0 < 0 and self._speedLength + var_1_0 < 0:
			self.reverseAcceleration()

		self._speed.Set(self._speed.x + self._speedNormal.x * var_1_0 + self._speedCross.x * var_1_1, self._speed.y + self._speedNormal.y * var_1_0 + self._speedCross.y * var_1_1, self._speed.z + self._speedNormal.z * var_1_0 + self._speedCross.z * var_1_1)

		self._speedLength = self._speed.Magnitude()

		if self._speedLength != 0:
			self._speedNormal.Copy(self._speed).Div(self._speedLength)

		self._speedCross.Copy(self._speedNormal).Cross2(up)

	def doTrack(self):
		if self.getTrackingTarget() == None:
			var_2_0 = BattleTargetChoise.TargetHarmNearest(self)[1]

			if var_2_0 != None and self.GetDistance(var_2_0) <= self._trackRange:
				self.setTrackingTarget(var_2_0)

		var_2_1 = self.getTrackingTarget()

		if var_2_1 == None or var_2_1 == -1:
			return
		elif not var_2_1.IsAlive():
			self.setTrackingTarget(-1)

			return
		elif self.GetDistance(var_2_1) > self._trackRange:
			self.setTrackingTarget(-1)

			return

		var_2_2 = var_2_1.GetBeenAimedPosition()

		if not var_2_2:
			return

		var_2_3 = var_2_2 - self.GetPosition()

		var_2_3.SetNormalize()

		var_2_4 = Vector3.Normalize(self._speed)
		var_2_5 = Vector3.Dot(var_2_4, var_2_3)
		var_2_6 = var_2_4.z * var_2_3.x - var_2_4.x * var_2_3.z

		if var_2_5 >= self.TRACKER_ANGLE:
			return

		var_2_7 = self.GetSpeedRatio()
		var_2_8 = math.cos(self._cosAngularSpeed * var_2_7)
		var_2_9 = math.sin(self._sinAngularSpeed * var_2_7)
		var_2_10 = var_2_5
		var_2_11 = var_2_6

		if var_2_5 < var_2_8:
			var_2_10 = var_2_8
			var_2_11 = var_2_9 * (var_2_11 >= 0 and 1 or -1)

		var_2_12 = self._speed.x * var_2_10 + self._speed.z * var_2_11
		var_2_13 = self._speed.z * var_2_10 - self._speed.x * var_2_11

		self._speed.Set(var_2_12, 0, var_2_13)

	def doOrbit(self):
		var_3_0 = Tool.FilterY(self._weapon.GetPosition())
		var_3_1 = Tool.FilterY(self.GetPosition())
		var_3_2 = (var_3_1 - var_3_0).magnitude
		var_3_3 = (var_3_0 - var_3_1).normalized
		var_3_4

		if var_3_2 > 10:
			var_3_4 = (var_3_3 + self._speed.normalized).normalized
		else:
			var_3_4 = (Vector3(-var_3_3.z, 0, var_3_3.x) + self._speed.normalized).normalized

		self._speed = var_3_4

	def RotateY(self, arg_4_1):
		var_4_0 = math.cos(arg_4_1)
		var_4_1 = math.sin(arg_4_1)

		return Vector3(self.x * var_4_0 + self.z * var_4_1, self.y, self.z * var_4_0 - self.x * var_4_1)

	def doCircle(self):
		if not self._originPos:
			return

		var_5_0 = self.GetSpeedRatio() * (1 + BattleAttr.GetCurrent(self, "bulletSpeedRatio"))
		var_5_1 = Tool.FilterY(self._position - self._originPos)
		var_5_2 = self._convertedVelocity
		var_5_3 = var_5_1.Magnitude()
		var_5_4 = var_5_3 - self._centripetalSpeed * var_5_0 * self._inverseFlag

		self._inverseFlag = var_5_4 < 0 and -self._inverseFlag or self._inverseFlag

		if var_5_3 <= 1e-05:
			return

		var_5_5 = self._circleAntiClockwise
		var_5_6 = var_5_2 / var_5_3 * (var_5_5 and 1 or -1) * var_5_0

		self._speed = self.RotateY(var_5_1, var_5_6).Mul(var_5_4 / var_5_3).Sub(var_5_1)

	def doNothing(self):
		if self._gravity != 0:
			self._verticalSpeed = self._verticalSpeed + self._gravity * self.GetSpeedRatio()

	def Ctor(self, arg_7_1, arg_7_2):
		EventDispatcher.AttachEventDispatcher(self)

		self._battleProxy = BattleDataProxy.GetInstance()
		self._uniqueID = arg_7_1
		self._speedExemptKey = "bullet_" + arg_7_1
		self._IFF = arg_7_2
		self._collidedList = {}
		self._speed = Vector3.zero
		self._exist = True
		self._timeStamp = 0
		self._dmgEnhanceRate = 1
		self._frame = 0
		self._reachDestFlag = False
		self._verticalSpeed = 0
		self._damageList = {}

	def Update(self, arg_8_1):
		var_8_0 = self.GetSpeedRatio()

		self.updateSpeed(arg_8_1)
		self.updateBarrageTransform(arg_8_1)
		self._position.Set(self._position.x + self._speed.x * var_8_0, self._position.y + self._speed.y * var_8_0, self._position.z + self._speed.z * var_8_0)

		self._position.y = self._position.y + self._verticalSpeed * var_8_0

		if self._gravity == 0:
			self._reachDestFlag = Vector3.SqrDistance(self._spawnPos, self._position) > self._sqrRange
		else:
			if self._fieldSwitchHeight != 0 and self._position.y <= self._fieldSwitchHeight:
				self._field = BattleConst.BulletField.SURFACE

			self._reachDestFlag = self._position.y <= BattleConfig.BombDetonateHeight

	def ActiveCldBox(self):
		self._cldComponent.SetActive(True)

	def DeactiveCldBox(self):
		self._cldComponent.SetActive(False)

	def SetStartTimeStamp(self, arg_11_1):
		self._timeStamp = arg_11_1

	def Hit(self, arg_12_1, arg_12_2):
		self._collidedList[arg_12_1] = True

		var_12_0 = table(
			UID = arg_12_1,
			type = arg_12_2
		)

		self.DispatchEvent(Event.New(BattleBulletEvent.HIT, var_12_0))

	def Intercepted(self):
		self.DispatchEvent(Event.New(BattleBulletEvent.INTERCEPTED, {}))

	def Reflected(self):
		self._speed.x = -self._speed.x

	def ResetVelocity(self, arg_15_1):
		var_15_0 = self._tempData
		var_15_1 = self.GetTemplate().extra_param

		if not arg_15_1:
			arg_15_1 = var_15_0.velocity

			if var_15_1.velocity_offset:
				arg_15_1 = math.random(arg_15_1 - var_15_1.velocity_offset, arg_15_1 + var_15_1.velocity_offset)
			elif var_15_1.velocity_offsetF:
				arg_15_1 = arg_15_1 + math.random() * 2 * var_15_1.velocity_offsetF - var_15_1.velocity_offsetF

		self._velocity = arg_15_1
		self._convertedVelocity = BattleFormulas.ConvertBulletSpeed(self._velocity)

	def SetTemplateData(self, arg_16_1):
		self._tempData = setmetatable({}, table(
			__index = arg_16_1
		))

		var_16_0 = self.GetTemplate().extra_param

		self.SetModleID(arg_16_1.modle_ID, self.ORIGNAL_RES)
		self.SetSFXID(self._tempData.hit_sfx, self._tempData.miss_sfx)
		self.ResetVelocity()

		self._pierceCount = arg_16_1.pierce_count

		self.FixRange()
		self.InitCldComponent()

		self._accTable = Clone(self._tempData.acceleration)

		def _sort(a,b):
			return a.t < b.t
		table.sort(self._accTable, _sort)

		self._field = arg_16_1.effect_type
		self._gravity = var_16_0.gravity or 0
		self._fieldSwitchHeight = var_16_0.effectSwitchHeight or 0
		self._ignoreShield = self._tempData.extra_param.ignoreShield == True
		self._autoRotate = self._tempData.extra_param.dontRotate != True

		self.SetDiverFilter()

	def GetModleID(self):
		var_18_0 = self.GetTemplate().extra_param
		var_18_1

		if self._IFF == BattleConfig.FOE_CODE:
			if self._mirrorSkin == self.MIRROR_SKIN_RES:
				var_18_1 = self._modleID + self.MIRROR_RES
			elif self._mirrorSkin == self.ORIGNAL_RES and var_18_0.mirror == True:
				var_18_1 = self._modleID + self.MIRROR_RES
			else:
				var_18_1 = self._modleID
		else:
			var_18_1 = self._modleID

		return var_18_1

	ORIGNAL_RES = -1
	SKIN_RES = 0
	MIRROR_SKIN_RES = 1

	def SetModleID(self, arg_19_1, arg_19_2, arg_19_3):
		self._modleID = arg_19_1
		self._mirrorSkin = arg_19_2

		if arg_19_3 and arg_19_3 != "":
			self._tempData.hit_fx = arg_19_3

	def SetSFXID(self, arg_20_1, arg_20_2):
		if arg_20_1:
			self._hitSFX = arg_20_1

		if arg_20_2:
			self._missSFX = arg_20_2

	def SetShiftInfo(self, arg_21_1, arg_21_2):
		var_21_0 = 0
		var_21_1 = 0
		var_21_2 = self.GetTemplate().extra_param

		if var_21_2.randomLaunchOffsetX:
			var_21_0 = math.random() * var_21_2.randomLaunchOffsetX * 2 - var_21_2.randomLaunchOffsetX

		if var_21_2.randomLaunchOffsetZ:
			var_21_1 = math.random() * var_21_2.randomLaunchOffsetZ * 2 - var_21_2.randomLaunchOffsetZ

		self._offsetX = arg_21_1 + var_21_0
		self._offsetZ = arg_21_2 + var_21_1

	def SetRotateInfo(self, arg_22_1, arg_22_2, arg_22_3):
		self._targetPos = arg_22_1
		self._baseAngle = arg_22_2
		self._barrageAngle = arg_22_3

		var_22_0 = self._barrageAngle % 360

		if var_22_0 > 0 and var_22_0 < 180:
			for iter_22_0, iter_22_1 in ipairs(self._accTable):
				if iter_22_1.flip:
					iter_22_1.v = iter_22_1.v * -1

	def SetBarrageTransformTempate(self, arg_23_1):
		if len(arg_23_1) > 0:
			self._barrageTransData = arg_23_1

	def SetAttr(self, arg_24_1):
		BattleAttr.SetAttr(self, arg_24_1)

	def GetAttr(self):
		return BattleAttr.GetAttr(self)

	def SetStandHostAttr(self, arg_26_1):
		self._standUnit = {}

		BattleAttr.SetAttr(self._standUnit, arg_26_1)

	def GetWeaponHostAttr(self):
		if self._standUnit:
			return BattleAttr.GetAttr(self._standUnit)
		else:
			return self.GetAttr()

	def GetWeaponAtkAttr(self):
		var_28_0 = self.GetWeaponHostAttr()
		var_28_1
		var_28_2 = self._weapon.GetAtkAttrTrasnform(var_28_0)

		if var_28_2:
			var_28_1 = var_28_2
		else:
			var_28_3 = self.GetWeaponTempData().attack_attribute

			var_28_1 = BattleAttr.GetAtkAttrByType(var_28_0, var_28_3)

		return var_28_1

	def GetWeaponCardPuzzleEnhance(self):
		return self._weapon.GetCardPuzzleDamageEnhance()

	def SetDamageEnhance(self, arg_30_1):
		self._dmgEnhanceRate = arg_30_1

	def GetDamageEnhance(self):
		return self._dmgEnhanceRate

	def GetAttrByName(self, arg_32_1):
		return BattleAttr.GetCurrent(self, arg_32_1)

	def GetVerticalSpeed(self):
		return self._verticalSpeed

	def IsGravitate(self):
		return self._gravity != 0

	def SetBuffTrigger(self, arg_35_1):
		self._host = arg_35_1
		self._buffTriggerFun = {}

	def SetBuffFun(self, arg_36_1, arg_36_2):
		var_36_0 = self._buffTriggerFun[arg_36_1] or {}

		var_36_0.append(arg_36_2)
		self._buffTriggerFun[arg_36_1] = var_36_0

	def BuffTrigger(self, arg_37_1, arg_37_2):
		var_37_0 = self._host

		if var_37_0 and var_37_0.IsAlive():
			self._host.TriggerBuff(arg_37_1, arg_37_2)

			var_37_1 = self._buffTriggerFun[arg_37_1]

			if var_37_1:
				for iter_37_0, iter_37_1 in ipairs(var_37_1):
					iter_37_1(self._host, arg_37_2)

	def SetIsCld(self, arg_38_1):
		self._needCld = arg_38_1

	def GetIsCld(self):
		return self._needCld

	def IsIngoreCld(self):
		return self._tempData.extra_param.ingoreCld

	def IsFragile(self):
		return self._tempData.extra_param.fragile

	def IsIndiscriminate(self):
		return self._tempData.extra_param.indiscriminate

	def GetExtraTag(self):
		return self._tempData.extra_param.tag

	def AppendDamageUnit(self, arg_44_1):
		self._damageList.append(arg_44_1)

	def DamageUnitListWriteback(self):
		self._weapon.UpdateCombo(self._damageList)

	def HasAcceleration(self):
		return len(self._accTable) != 0

	def IsTracker(self):
		return self._accTable.tracker

	def IsOrbit(self):
		return self._accTable.orbit

	def IsCircle(self):
		return self._accTable.circle

	def GetAcceleration(self, arg_50_1):
		self._lastAccTime = self._lastAccTime or self._timeStamp

		var_50_0 = math.modf((arg_50_1 - self._lastAccTime) / self.ACC_INTERVAL)

		self._lastAccTime = self._lastAccTime + self.ACC_INTERVAL * var_50_0

		var_50_1 = arg_50_1 - self._timeStamp
		var_50_2 = len(self._accTable)

		while var_50_2 > 0:
			var_50_3 = self._accTable[var_50_2]

			if var_50_1 + self.ACC_INTERVAL < var_50_3.t:
				var_50_2 = var_50_2 - 1
			else:
				return var_50_3.u * var_50_0, var_50_3.v * var_50_0

		return 0, 0

	def reverseAcceleration(self):
		for iter_51_0, iter_51_1 in ipairs(self._accTable):
			iter_51_1.u = iter_51_1.u * -1

	def GetDistance(self, arg_52_1):
		var_52_0 = self._battleProxy.FrameIndex

		if self._frame != var_52_0:
			self._distanceBackup = {}
			self._frame = var_52_0

		var_52_1 = self._distanceBackup[arg_52_1]

		if var_52_1 == None:
			var_52_1 = Vector3.Distance(self.GetPosition(), arg_52_1.GetPosition())
			self._distanceBackup[arg_52_1] = var_52_1

			arg_52_1.backupDistance(self, var_52_1)

		return var_52_1

	def backupDistance(self, arg_53_1, arg_53_2):
		var_53_0 = self._battleProxy.FrameIndex

		if self._frame != var_53_0:
			self._distanceBackup = {}
			self._frame = var_53_0

		self._distanceBackup[arg_53_1] = arg_53_2

	def getTrackingTarget(self):
		return self._tarckingTarget

	def setTrackingTarget(self, arg_55_1):
		self._tarckingTarget = arg_55_1

	def SetWeapon(self, arg_56_1):
		self._weapon = arg_56_1

		if arg_56_1:
			self._correctedDMG = self._weapon.GetCorrectedDMG()

	def GetWeapon(self):
		return self._weapon

	def GetCorrectedDMG(self):
		return self._correctedDMG

	def OverrideCorrectedDMG(self, arg_59_1):
		self._correctedDMG = BattleFormulas.WeaponDamagePreCorrection(self._weapon, arg_59_1)

	def GetWeaponTempData(self):
		return self._weapon.GetTemplateData()

	def GetPosition(self):
		return self._position or Vector3.zero

	def SetSpawnPosition(self, arg_62_1):
		self._spawnPos = arg_62_1
		self._position = arg_62_1.Clone()

		if self._gravity != 0:
			var_62_0 = math.atan2(self._speed.x, self._speed.z)

			if var_62_0 == 0:
				self._verticalSpeed = 0
			else:
				var_62_1 = Vector3(math.cos(var_62_0) * 60, math.sin(var_62_0) * 60)
				var_62_2 = 60 / self._convertedVelocity

				self._verticalSpeed = -0.5 * self._gravity * var_62_2

	def GetSpawnPosition(self):
		return self._spawnPos

	def GetTemplate(self):
		return self._tempData

	def GetType(self):
		return self._tempData.type

	def GetHitSFX(self):
		return self._hitSFX

	def GetMissSFX(self):
		return self._missSFX

	def GetOutBound(self):
		return self._tempData.out_bound

	def GetUniqueID(self):
		return self._uniqueID

	def GetOffset(self):
		return self._offsetX, self._offsetZ, self._isOffsetPriority

	def GetRotateInfo(self):
		return self._targetPos, self._baseAngle, self._barrageAngle

	def IsOutRange(self):
		return self._reachDestFlag

	def SetYAngle(self, arg_73_1):
		self._yAngle = arg_73_1

	def SetOffsetPriority(self, arg_74_1):
		self._isOffsetPriority = arg_74_1 or False

	def GetOffsetPriority(self):
		return self._isOffsetPriority

	def GetYAngle(self):
		return self._yAngle

	def GetCurrentYAngle(self):
		var_77_0 = Vector3.Normalize(self._speed)
		var_77_1 = math.acos(var_77_0.x) / math.deg2Rad

		if var_77_0.z < 0:
			var_77_1 = 360 - var_77_1

		return var_77_1

	def GetIFF(self):
		return self._IFF

	def GetHost(self):
		return self._host

	def GetPierceCount(self):
		return self._pierceCount

	def AppendAttachBuff(self, arg_81_1):
		self._attachBuffList = self._attachBuffList or self.generateAttachBuffList()

		table.insert(self._attachBuffList, arg_81_1)

	def GetAttachBuff(self):
		self._attachBuffList = self._attachBuffList or self.generateAttachBuffList()

		return self._attachBuffList

	def generateAttachBuffList(self):
		var_83_0 = {}

		if not self.GetTemplate().attach_buff:
			var_83_1 = {}

		for iter_83_0, iter_83_1 in ipairs(self.GetTemplate().attach_buff):
			var_83_2 = table(
				buff_id = iter_83_1.buff_id,
				level = iter_83_1.buff_level,
				rant = iter_83_1.rant
			)

			table.insert(var_83_0, var_83_2)

		return var_83_0

	def GetEffectField(self):
		return self._field

	def SetDiverFilter(self, arg_85_1):
		if arg_85_1 == None:
			self._diveFilter = self._tempData.extra_param.diveFilter or {
				2
			}
		else:
			self._diveFilter = arg_85_1

	def GetDiveFilter(self):
		return self._diveFilter

	def GetVelocity(self):
		return self._velocity

	def GetConvertedVelocity(self):
		return self._convertedVelocity

	def GetSpeedExemptKey(self):
		return self._speedExemptKey

	def IsCollided(self, arg_90_1):
		return self._collidedList[arg_90_1]

	def GetExist(self):
		return self._exist

	def SetExist(self, arg_92_1):
		self._exist = arg_92_1

	def GetIgnoreShield(self):
		return self._ignoreShield

	def SetIgnoreShield(self, arg_94_1):
		self._ignoreShield = arg_94_1

	def IsAutoRotate(self):
		return self._autoRotate

	def Dispose(self):
		self._dataProxy = None

		EventDispatcher.DetachEventDispatcher(self)

	def InitCldComponent(self):
		var_97_0 = self.GetTemplate().cld_box
		var_97_1 = self.GetTemplate().cld_offset
		var_97_2 = var_97_1[1]

		if self.GetIFF() == BattleConfig.FOE_CODE:
			var_97_2 = var_97_2 * -1

		self._cldComponent = BattleCubeCldComponent.New(var_97_0[1], var_97_0[2], var_97_0[3], var_97_2, var_97_1[3])

		var_97_3 = table(
			type = BattleConst.CldType.BULLET,
			IFF = self.GetIFF(),
			UID = self.GetUniqueID()
		)

		self._cldComponent.SetCldData(var_97_3)

	def ResetCldSurface(self):
		var_98_0 = self.GetDiveFilter()

		if var_98_0 and len(var_98_0) == 0:
			self.GetCldData().Surface = BattleConst.OXY_STATE.DIVE
		else:
			self.GetCldData().Surface = BattleConst.OXY_STATE.FLOAT

	def GetBoxSize(self):
		return self._cldComponent.GetCldBoxSize()

	def GetCldBox(self):
		return self._cldComponent.GetCldBox(self.GetPosition())

	def GetCldData(self):
		return self._cldComponent.GetCldData()

	def GetSpeed(self):
		return self._speed

	def GetSpeedRatio(self):
		return BattleVariable.GetSpeedRatio(self._speedExemptKey, self._IFF)

	def InitSpeed(self, arg_104_1):
		if self._yAngle == None:
			self._yAngle = (arg_104_1 or self._baseAngle) + self._barrageAngle

		self.calcSpeed()

		if self.HasAcceleration():
			self._speedLength = self._speed.Magnitude()

			var_104_0 = math.deg2Rad * self._yAngle

			self._speedNormal = Vector3(math.cos(var_104_0), 0, math.sin(var_104_0))
			self._speedCross = Vector3.Cross(self._speedNormal, up)
			self.updateSpeed = self.doAccelerate
		elif self.IsTracker():
			var_104_1 = self._accTable.tracker

			self._trackRange = var_104_1.range
			self._cosAngularSpeed = math.deg2Rad * var_104_1.angular
			self._sinAngularSpeed = math.deg2Rad * var_104_1.angular
			self._negativeCosAngularSpeed = math.deg2Rad * var_104_1.angular * -1
			self._negativeSinAngularSpeed = math.deg2Rad * var_104_1.angular * -1
			self.updateSpeed = self.doTrack
		elif self.IsCircle():
			var_104_2 = self._accTable.circle

			self._originPos = var_104_2.center or self._targetPos
			self._circleAntiClockwise = bool(var_104_2.antiClockWise)
			self._centripetalSpeed = (var_104_2.centripetalSpeed or 0) * viewFPS
			self._inverseFlag = 1
			self.updateSpeed = self.doCircle
		else:
			self.updateSpeed = self.doNothing

	def calcSpeed(self):
		var_105_0 = 1 + BattleAttr.GetCurrent(self, "bulletSpeedRatio")
		var_105_1 = self._velocity * var_105_0
		var_105_2 = BattleFormulas.ConvertBulletSpeed(var_105_1)
		var_105_3 = math.deg2Rad * self._yAngle

		self._speed = Vector3(var_105_2 * math.cos(var_105_3), 0, var_105_2 * math.sin(var_105_3))

	def updateBarrageTransform(self, arg_106_1):
		if not self._barrageTransData or len(self._barrageTransData) == 0:
			return

		var_106_0 = arg_106_1 - self._timeStamp
		var_106_1 = self._barrageTransData[1]

		if var_106_0 >= var_106_1.transStartDelay:
			if var_106_1.transAimAngle:
				self._yAngle = var_106_1.transAimAngle
			else:
				self._yAngle = math.rad2Deg * math.atan2(var_106_1.transAimPosZ - self._position.z, var_106_1.transAimPosX - self._position.x)

			self.calcSpeed()
			table.remove(self._barrageTransData, 1)

			var_106_2 = self._barrageTransData[1]

			if var_106_2:
				var_106_2.transStartDelay = var_106_2.transStartDelay + var_106_1.transStartDelay

	def GetCurrentDistance(self):
		return Vector3.Distance(self._spawnPos, self._position)

	def SetOutRangeCallback(self, arg_108_1):
		self._outRangeFunc = arg_108_1

	def OutRange(self):
		self.DispatchEvent(Event(BattleBulletEvent.OUT_RANGE, {}))
		self._outRangeFunc(self)

	def FixRange(self, arg_110_1, arg_110_2):
		arg_110_1 = arg_110_1 or self._tempData.range
		arg_110_2 = arg_110_2 or 0

		var_110_0 = self._tempData.range_offset

		if var_110_0 == 0:
			self._range = arg_110_1
		else:
			self._range = arg_110_1 + var_110_0 * (math.random() - 0.5)

		self._range = math.max(0, self._range + arg_110_2)
		self._sqrRange = self._range * self._range

	def ImmuneBombCLS(self):
		return self.GetTemplate().extra_param.ignoreB

	def ImmuneCLS(self):
		return self._immuneCLS

	def SetImmuneCLS(self, arg_113_1):
		self._immuneCLS = arg_113_1
