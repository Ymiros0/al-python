from luatable import ipairs

from buff import BattleBuffUnit
import BattleBulletUnit
from support.utils import Tool
class BattleEffectBulletUnit(BattleBulletUnit):
		
	__name = "BattleEffectBulletUnit"

	def __init__(self, arg_1_1, arg_1_2):
		super().__init__(self, arg_1_1, arg_1_2)

	def Update(self, arg_2_1):
		super().Update(self, arg_2_1)

		if self._flare:
			self._flare.SetPosition(Tool.FilterY(self.GetPosition().Clone()))

	def IsFlare(self):
		return self.GetTemplate().attach_buff[1].flare

	def OutRange(self):
		super().OutRange(self)

		if self._flare:
			self._flare.SetActiveFlag(False)

			self._flare = None

	def spawnArea(self, arg_5_1):
		var_5_0 = self.GetTemplate()
		var_5_1 = var_5_0.hit_type
		var_5_2 = var_5_0.attach_buff[1]
		var_5_3 = var_5_2.buff_id
		var_5_4 = var_5_2.buff_level or 1

		def var_5_5(a):
			for iter_6_0, iter_6_1 in ipairs(a):
				if iter_6_1.Active:
					var_6_0 = a._battleProxy.GetUnitList()[iter_6_1.UID]
					var_6_1 = BattleBuffUnit.New(var_5_3, var_5_4)

					var_6_0.AddBuff(var_6_1, True)

		def var_5_6(a):
			if a.Active:
				a._battleProxy.GetUnitList()[a.UID].RemoveBuff(var_5_3, True)

		time = var_5_1.time

		var_5_7 = self._battleProxy.SpawnLastingColumnArea(self.GetEffectField(), self.GetIFF(), Tool.FilterY(self.GetPosition().Clone()), var_5_1.range, time, var_5_5, var_5_6, var_5_2.friendly, var_5_2.effect_id)

		if arg_5_1:
			self._flare = var_5_7

		return var_5_7

	def GetExplodePostion(self):
		return self._explodePos

	def SetExplodePosition(self, arg_9_1):
		self._explodePos = arg_9_1
