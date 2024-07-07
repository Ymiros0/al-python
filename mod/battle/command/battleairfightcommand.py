from packages.luatable import table, ipairs

import BattleSingleDungeonCommand
import BattleUnitEvent
import BattleEvent
from mod.battle.data import BattleConfig, BattleConst, BattleFormulas
from mod.battle.data.manager.BattleWaveUpdater import BattleWaveUpdater #!
from mod.battle.BattleState import BattleState
from mod.battle.view.scene.BattlePopNumManager import BattlePopNumManager #!
from mod.battle.view.characterfactory.BattleHPBarManager import BattleHPBarManager #!
import controller.const.game as GAME
from const import SYSTEM_AIRFIGHT
from mgr.UIMgr import UIMgr #!
from model.const import ShipType
from support.helpers import M02

class BattleAirFightCommand(BattleSingleDungeonCommand):
	__name = "BattleAirFightCommand"

	def AddEvent(self, *args):
		super().AddEvent(self, *args)
		self._dataProxy.RegisterEventListener(self, BattleEvent.COMMON_DATA_INIT_FINISH, self.onBattleDataInitFinished)

	def RemoveEvent(self, *args):
		self._dataProxy.UnregisterEventListener(self, BattleEvent.COMMON_DATA_INIT_FINISH)
		super().RemoveEvent(self, *args)

	def DoPrologue(self):
		UIMgr().Marching()

		def _function():
			def _function2():
				self._dataProxy.SetupCalculateDamage(BattleFormulas.FriendInvincibleDamage)
				self._dataProxy.SetupDamageKamikazeShip(BattleFormulas.CalcDamageLockS2M)
				self._dataProxy.SetupDamageCrush(BattleFormulas.FriendInvincibleCrashDamage)
				self._uiMediator.ShowTimer()
				self._state.ChangeState(BattleState.BATTLE_STATE_FIGHT)
				self._waveUpdater.Start(), SYSTEM_AIRFIGHT
			self._uiMediator.OpeningEffect(_function2)
			self._dataProxy.InitAllFleetUnitsWeaponCD()

		self._uiMediator.SeaSurfaceShift(1, 15, None, _function)

		var_4_1 = self._state.GetSceneMediator()

		var_4_1.InitPopScorePool()
		var_4_1.EnablePopContainer(BattlePopNumManager.CONTAINER_HP, False)
		var_4_1.EnablePopContainer(BattlePopNumManager.CONTAINER_SCORE, False)
		var_4_1.EnablePopContainer(BattleHPBarManager.ROOT_NAME, False)
		self._uiMediator.ShowAirFightScoreBar()

	def initWaveModule(self):
		def var_7_0(arg_8_0, arg_8_1, arg_8_2):
			self._dataProxy.SpawnMonster(arg_8_0, arg_8_1, arg_8_2, BattleConfig.FOE_CODE)

		def var_7_1():
			if self._vertifyFail:
				M02.sendNotification(GAME.CHEATER_MARK, table(
					reason = self._vertifyFail
				))

				return

			self._dataProxy.CalcAirFightScore()
			self._state.BattleEnd()

		self._waveUpdater = BattleWaveUpdater.New(var_7_0, None, var_7_1, None)

	def onBattleDataInitFinished(self):
		self._dataProxy.AirFightInit()

		var_10_0 = self._userFleet.GetScoutList()

		for iter_10_0, iter_10_1 in ipairs(var_10_0):
			iter_10_1.HideWaveFx()

	def RegisterUnitEvent(self, arg_11_1, *args):
		super().RegisterUnitEvent(self, arg_11_1, *args)

		if arg_11_1.GetUnitType() == BattleConst.UnitType.PLAYER_UNIT:
			arg_11_1.RegisterEventListener(self, BattleUnitEvent.UPDATE_HP, self.onPlayerHPUpdate)

	def UnregisterUnitEvent(self, arg_12_1, *args):
		if arg_12_1.GetUnitType() == BattleConst.UnitType.PLAYER_UNIT:
			arg_12_1.UnregisterEventListener(self, BattleUnitEvent.UPDATE_HP)

		super().UnregisterUnitEvent(self, arg_12_1, *args)

	ShipType2Point = table({
		ShipType.YuLeiTing: 200,
		ShipType.JinBi: 300,
		ShipType.ZiBao: 3000
	})
	BeenHitDecreasePoint = 10

	def onWillDie(self, arg_13_1):
		var_13_0 = arg_13_1.Dispatcher
		var_13_1 = var_13_0.GetDeathReason()
		var_13_2 = var_13_0.GetTemplate().type

		if var_13_1 == BattleConst.UnitDeathReason.CRUSH or var_13_1 == BattleConst.UnitDeathReason.KILLED:
			var_13_3 = self.ShipType2Point[var_13_2]

			if var_13_3 and var_13_3 > 0:
				self._dataProxy.AddAirFightScore(var_13_3)

	def onPlayerHPUpdate(self, arg_14_1):
		if arg_14_1.Data.dHP <= 0:
			self._dataProxy.DecreaseAirFightScore(self.BeenHitDecreasePoint * -arg_14_1.Data.dHP)
