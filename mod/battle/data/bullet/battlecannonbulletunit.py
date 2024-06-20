import BattleBulletUnit
class BattleCannonBulletUnit(BattleBulletUnit):
	__name = "BattleCannonBulletUnit"

	def __init__(arg_1_0, arg_1_1, arg_1_2):
		super().__init__(arg_1_0, arg_1_1, arg_1_2)

	def Hit(arg_2_0, arg_2_1, arg_2_2):
		super().Hit(arg_2_0, arg_2_1, arg_2_2)

		arg_2_0._pierceCount = arg_2_0._pierceCount - 1
