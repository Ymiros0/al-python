import math
from Vector3 import Vector3
import BattleBulletUnit
import BattleFormulas
import BattleAttr
class BattleTorpedoBulletUnit(BattleBulletUnit):

	__name = "BattleTorpedoBulletUnit"

	def calcSpeed(self):
		var_2_0 = 1 + BattleAttr.GetCurrent(self, "bulletSpeedRatio")
		var_2_1 = max(0, self._velocity + BattleAttr.GetCurrent(self, "torpedoSpeedExtra")) * var_2_0
		var_2_2 = BattleFormulas.ConvertBulletSpeed(var_2_1)
		var_2_3 = math.deg2Rad * self._yAngle

		self._speed = Vector3(var_2_2 * math.cos(var_2_3), 0, var_2_2 * math.sin(var_2_3))

	def GetExplodePostion(self):
		return self._explodePos

	def SetExplodePosition(arg_4_0, arg_4_1):
		arg_4_0._explodePos = arg_4_1

	def InitCldComponent(self):
		super().InitCldComponent(self)
		self.ResetCldSurface()

	def Hit(self, arg_6_1, arg_6_2):
		super().Hit(self, arg_6_1, arg_6_2)

		self._pierceCount = self._pierceCount - 1
