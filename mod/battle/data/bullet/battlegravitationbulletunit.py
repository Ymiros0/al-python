import BattleBulletUnit
from mgr import TimeMgr
class BattleGravitationBulletUnit(BattleBulletUnit):
	__name = "BattleGravitationBulletUnit"

	def __init__(arg_1_0, arg_1_1, arg_1_2):
		super().__init__(arg_1_0, arg_1_1, arg_1_2)

	def Update(arg_2_0, arg_2_1):
		if arg_2_0._pierceCount > 0:
			super().Update(arg_2_0, arg_2_1)

	def SetTemplateData(arg_3_0, arg_3_1):
		super().SetTemplateData(arg_3_0, arg_3_1)

		arg_3_0._hitInterval = arg_3_1.hit_type.interval or 0.2

	def GetExplodePostion(arg_4_0):
		return arg_4_0._explodePos

	def SetExplodePosition(arg_5_0, arg_5_1):
		arg_5_0._explodePos = arg_5_1

	def DealDamage(arg_6_0):
		arg_6_0._nextDamageTime = TimeMgr.GetInstance().GetCombatTime() + arg_6_0._hitInterval

	def CanDealDamage(arg_7_0):
		if not arg_7_0._nextDamageTime:
			arg_7_0._nextDamageTime = TimeMgr.GetInstance().GetCombatTime() + arg_7_0._tempData.extra_param.alert_duration

			return False
		else:
			return arg_7_0._nextDamageTime < TimeMgr.GetInstance().GetCombatTime()

	def Hit(arg_8_0, arg_8_1, arg_8_2):
		super().Hit(arg_8_0, arg_8_1, arg_8_2)

		arg_8_0._pierceCount = arg_8_0._pierceCount - 1
		arg_8_0._position.y = 100
