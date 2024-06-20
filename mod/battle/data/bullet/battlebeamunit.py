from Vector3 import Vector3
from alsupport import math
import BattleDataFunction
import BattleVariable
import BattleConfig
import TimeMgr

class BattleBeamUnit:
	__name = "BattleBeamUnit"
	BEAM_STATE_READY = "ready"
	BEAM_STATE_ATTACK = "attack"
	BEAM_STATE_FINISH = "finish"

	def __init__(self, arg_1_1, arg_1_2):
		self._bulletID = arg_1_1
		self._beamInfoID = arg_1_2
		self._cldList = {}
		self._beamState = self.BEAM_STATE_READY

	def IsBeamActive(self):
		return self._aoe.GetActiveFlag()

	def ClearBeam(self):
		self._beamState = self.BEAM_STATE_FINISH
		self._aoe = None
		self._cldList = {}
		self._nextDamageTime = None

	def SetAoeData(arg_4_0, arg_4_1):
		arg_4_0._aoe = arg_4_1
		arg_4_0._beamTemp = BattleDataFunction.GetBarrageTmpDataFromID(arg_4_0._beamInfoID)
		arg_4_0._bulletTemp = BattleDataFunction.GetBulletTmpDataFromID(arg_4_0._bulletID)
		arg_4_0._angle = arg_4_0._beamTemp.angle

		arg_4_0._aoe.SetAngle(arg_4_0._angle + arg_4_0._aimAngle)

		var_4_0 = arg_4_0._bulletTemp.extra_param.diveFilter

		if var_4_0:
			arg_4_0._aoe.SetDiveFilter(var_4_0)

	def SetAimAngle(arg_5_0, arg_5_1):
		arg_5_0._aimAngle = arg_5_1 or 0

	def SetAimPosition(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
		if arg_6_3 == BattleConfig.FOE_CODE:
			arg_6_0._aimAngle = math.rad2Deg * math.atan2(arg_6_2.z - arg_6_1.z, arg_6_2.x - arg_6_1.x)
		elif arg_6_3 == BattleConfig.FRIENDLY_CODE:
			arg_6_0._aimAngle = math.rad2Deg * math.atan2(arg_6_1.z - arg_6_2.z, arg_6_1.x - arg_6_2.x)

	def getAngleRatio(arg_7_0):
		return BattleVariable.GetSpeedRatio(arg_7_0._aoe.GetTimeRationExemptKey(), arg_7_0._aoe.GetIFF())

	def GetAoeData(arg_8_0):
		return arg_8_0._aoe

	def UpdateBeamPos(arg_9_0, arg_9_1):
		arg_9_0._aoe.SetPosition(Vector3(arg_9_1.x + arg_9_0._beamTemp.offset_x, 0, arg_9_1.z + arg_9_0._beamTemp.offset_z))

	def UpdateBeamAngle(arg_10_0):
		arg_10_0._angle = arg_10_0._angle + arg_10_0._beamTemp.delta_angle * arg_10_0.getAngleRatio()

		arg_10_0._aoe.SetAngle(arg_10_0._angle + arg_10_0._aimAngle)

	def AddCldUnit(arg_11_0, arg_11_1):
		var_11_0 = arg_11_1.GetUniqueID()

		arg_11_0._cldList[var_11_0] = arg_11_1

	def RemoveCldUnit(arg_12_0, arg_12_1):
		var_12_0 = arg_12_1.GetUniqueID()

		arg_12_0._cldList[var_12_0] = None

	def ChangeBeamState(arg_13_0, arg_13_1):
		arg_13_0._beamState = arg_13_1

	def GetBeamState(arg_14_0):
		return arg_14_0._beamState

	def GetCldUnitList(arg_15_0):
		return arg_15_0._cldList

	def BeginFocus(arg_16_0):
		arg_16_0._nextDamageTime = TimeMgr.GetInstance().GetCombatTime() + arg_16_0._beamTemp.senior_delay

	def DealDamage(arg_17_0):
		arg_17_0._nextDamageTime = TimeMgr.GetInstance().GetCombatTime() + arg_17_0._beamTemp.delta_delay

	def CanDealDamage(arg_18_0):
		return arg_18_0._nextDamageTime < TimeMgr.GetInstance().GetCombatTime()

	def GetFXID(arg_19_0):
		return arg_19_0._bulletTemp.hit_fx

	def GetSFXID(arg_20_0):
		return arg_20_0._bulletTemp.hit_sfx

	def GetBulletID(arg_21_0):
		return arg_21_0._bulletID

	def GetBeamInfoID(arg_22_0):
		return arg_22_0._beamInfoID

	def GetBeamExtraParam(arg_23_0):
		return arg_23_0._bulletTemp.extra_param
