import BattleBulletUnit
class BattleStrayBulletUnit(BattleBulletUnit):
	__name = "BattleStrayBulletUnit"

	def SetExplodePosition(self, arg_2_1):
		self._explodePos = arg_2_1

	def GetExplodePostion(self):
		return self._explodePos
