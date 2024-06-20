from luatable import table
from Vector3 import Vector3, quaternion as Quaternion
import math
import BattleBulletEvent
import BattleConfig
import BattleBulletUnit
from Framework.event import Event
from support.utils import Tool
import TimeMgr

class BattleBombBulletUnit(BattleBulletUnit):
	__name = "BattleBombBulletUnit"

	def __init__(self, arg_1_1, arg_1_2):
		super.__init__(self, arg_1_1, arg_1_2)

		self._randomOffset = Vector3.zero

	def InitSpeed(self):
		if self._barrageLowPriority:
			self._yAngle = self._baseAngle + self._barrageAngle
		else:
			self._yAngle = math.rad2Deg * math.atan2(self._explodePos.z - self._spawnPos.z, self._explodePos.x - self._spawnPos.x)

		self.calcSpeed()

		self.updateSpeed = self.doNothing

	def Update(self):
		if self._exist:
			super.Update(self)

	def GetPierceCount(self):
		return 1

	def IsOutRange(self, arg_5_1):
		if not self._exist:
			return False

		if self._explodeTime and arg_5_1 >= self._explodeTime:
			return True

		if self._reachDestFlag and not self._explodeTime:
			return True
		else:
			return False

	def OutRange(self):
		var_6_0 = table(
			UID = self.unitUniqueID
		)

		self.DispatchEvent(Event(BattleBulletEvent.EXPLODE, var_6_0))
		super.OutRange(self)

	def SetSpawnPosition(arg_7_0, arg_7_1):
		super.SetSpawnPosition(arg_7_0, arg_7_1)

		if arg_7_0._barragePriority:
			arg_7_0._explodePos = arg_7_0._explodePos + Vector3(arg_7_0._offsetX, 0, arg_7_0._offsetZ)

			var_7_0 = Quaternion.Euler(0, arg_7_0._barrageAngle, 0)
			var_7_1 = Tool.FilterY(arg_7_0._spawnPos)

			arg_7_0._explodePos = var_7_0 * (arg_7_0._explodePos - var_7_1) + var_7_1

		if arg_7_0._fixToRange and Vector3.BattleDistance(arg_7_0._explodePos, arg_7_0._spawnPos) > arg_7_0._range:
			var_7_2 = Tool.FilterY(arg_7_0._explodePos - arg_7_0._spawnPos)

			arg_7_0._explodePos = Vector3.Normalize(var_7_2) * arg_7_0._range + arg_7_0._spawnPos

		if arg_7_0._convertedVelocity != 0:
			var_7_3 = Tool.FilterY(arg_7_0._spawnPos)
			var_7_4 = Vector3.Distance(var_7_3, arg_7_0._explodePos) / arg_7_0._convertedVelocity
			var_7_5 = arg_7_0._explodePos.y - arg_7_0._spawnPos.y

			arg_7_0._verticalSpeed = arg_7_0.GetTemplate().extra_param.launchVrtSpeed or var_7_5 / var_7_4 - 0.5 * arg_7_0._gravity * var_7_4

	def SetExplodePosition(arg_8_0, arg_8_1):
		var_8_0 = arg_8_0.GetTemplate().extra_param

		if var_8_0.targetFixX and var_8_0.targetFixZ:
			arg_8_0._explodePos = Vector3(var_8_0.targetFixX, 0, var_8_0.targetFixZ)
		else:
			arg_8_0._explodePos = arg_8_1.Clone()

		if not arg_8_0._barragePriority:
			arg_8_0._explodePos = arg_8_0._explodePos + arg_8_0._randomOffset

		arg_8_0._explodePos.y = BattleConfig.BombDetonateHeight
		
	def SetTemplateData(arg_9_0, arg_9_1):
		super().SetTemplateData(arg_9_0, arg_9_1)

		var_9_0 = arg_9_0.GetTemplate().extra_param

		arg_9_0._barragePriority = var_9_0.barragePriority
		arg_9_0._barrageLowPriority = var_9_0.barrageLowPriority
		arg_9_0._fixToRange = var_9_0.fixToRange

		if var_9_0.barragePriority:
			arg_9_0._randomOffset = Vector3.zero
		else:
			var_9_1 = var_9_0.accuracy
			var_9_2 = 0

			if var_9_1:
				var_9_2 = arg_9_0.GetAttrByName(var_9_1)

			var_9_3 = var_9_0.randomOffsetX or 0
			var_9_4 = var_9_0.randomOffsetZ or 0
			var_9_5 = math.max(0, var_9_3 - var_9_2)
			var_9_6 = math.max(0, var_9_4 - var_9_2)
			var_9_7 = var_9_0.offsetX or 0
			var_9_8 = var_9_0.offsetZ or 0

			if var_9_5 != 0:
				var_9_5 = var_9_5 * (math.random() - 0.5) + var_9_7

			if var_9_6 != 0:
				var_9_6 = var_9_6 * (math.random() - 0.5) + var_9_8

			var_9_9 = var_9_0.targetOffsetX or 0
			var_9_10 = var_9_0.targetOffsetZ or 0

			arg_9_0._randomOffset = Vector3(var_9_5 + var_9_9, 0, var_9_6 + var_9_10)

		if var_9_0.timeToExplode:
			arg_9_0._explodeTime = TimeMgr.GetInstance().GetCombatTime() + var_9_0.timeToExplode

		arg_9_0._gravity = var_9_0.gravity or BattleConfig.GRAVITY
		arg_9_0._hitInterval = arg_9_1.hit_type.interval or 0.2

	def DealDamage(arg_10_0):
		arg_10_0._nextDamageTime = TimeMgr.GetInstance().GetCombatTime() + arg_10_0._hitInterval

	def CanDealDamage(arg_11_0):
		if not arg_11_0._nextDamageTime:
			arg_11_0._nextDamageTime = TimeMgr.GetInstance().GetCombatTime() + arg_11_0._tempData.extra_param.alert_duration

			return False
		else:
			return arg_11_0._nextDamageTime < TimeMgr.GetInstance().GetCombatTime()

	def HideBullet(arg_12_0):
		arg_12_0._position.x = 0
		arg_12_0._position.y = 100
		arg_12_0._position.z = 0

	def GetExplodePostion(arg_13_0):
		return arg_13_0._explodePos
