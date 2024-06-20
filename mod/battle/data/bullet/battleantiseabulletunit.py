import BattleBulletUnit
class BattleAntiSeaBulletUnit(BattleBulletUnit):
	__name = "BattleAntiSeaBulletUnit"


	def __init__(arg_1_0, arg_1_1, arg_1_2):
		super().__init__(arg_1_0, arg_1_1, arg_1_2)

	def Update(arg_2_0, arg_2_1):
		return

	def IsOutRange(arg_3_0):
		return False

	def SetDirectHitUnit(arg_4_0, arg_4_1):
		arg_4_0._directHitUnit = arg_4_1

	def GetDirectHitUnit(arg_5_0):
		return arg_5_0._directHitUnit

	def Dispose(arg_6_0):
		arg_6_0._directHitUnit = None

		super().Dispose(arg_6_0)
