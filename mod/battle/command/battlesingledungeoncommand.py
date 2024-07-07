from packages.luatable import table, pairs, ipairs

from Framework.base.mvc.Command import Command
from Framework.event.Event import Event
import BattleUnitEvent
import BattleEvent
from BattleControllerWeaponCommand import BattleControllerWeaponCommand
from mod.battle.BattleState import BattleState
from mod.battle.data import BattleConfig, BattleConst
from mod.battle.data.BattleDataProxy import BattleDataProxy
from mod.battle.data.manager.BattleWaveUpdater import BattleWaveUpdater
import controller.const.game as GAME
from const import SYSTEM_PERFORM, SYSTEM_PROLOGUE
from mgr.UIMgr import UIMgr #!
from support.helpers import M02

class BattleSingleDungeonCommand(Command):
	__name = "BattleSingleDungeonCommand"

	def Initialize(self):
		super().Initialize(self)

		self._dataProxy = self._state.GetProxyByName(BattleDataProxy.__name)
		self._uiMediator = self._state.GetUIMediator()

		self.Init()
		self.InitProtocol()
		self.AddEvent()

		self._count = 0

	def DoPrologue(arg_3_0):
		UIMgr.GetInstance().Marching()

		def var_3_0():
			def _function():
				arg_3_0._uiMediator.ShowAutoBtn()
				arg_3_0._uiMediator.ShowTimer()
				arg_3_0._state.GetCommandByName(BattleControllerWeaponCommand.__name).TryAutoSub()
				arg_3_0._state.ChangeState(BattleState.BATTLE_STATE_FIGHT)
				arg_3_0._waveUpdater.Start()

				if arg_3_0._dataProxy.GetInitData().hideAllButtons:
					arg_3_0._dataProxy.DispatchEvent(Event.New(BattleEvent.HIDE_INTERACTABLE_BUTTONS, table(
						isActive = False
					)))
			arg_3_0._uiMediator.OpeningEffect(_function)
			arg_3_0._dataProxy.GetFleetByIFF(BattleConfig.FRIENDLY_CODE).FleetWarcry()
			arg_3_0._dataProxy.InitAllFleetUnitsWeaponCD()
			arg_3_0._dataProxy.TirggerBattleStartBuffs()

		arg_3_0._uiMediator.SeaSurfaceShift(45, 0, None, var_3_0)

	def Init(arg_6_0):
		arg_6_0._unitDataList = table()

		arg_6_0.initWaveModule()

	def Clear(arg_7_0):
		for iter_7_0, iter_7_1 in pairs(arg_7_0._unitDataList):
			arg_7_0.UnregisterUnitEvent(iter_7_1)

			arg_7_0._unitDataList[iter_7_0] = None

		arg_7_0._waveUpdater.Clear()

	def Reinitialize(arg_8_0):
		arg_8_0._state.Deactive()
		arg_8_0.Clear()
		arg_8_0.Init()

	def Dispose(arg_9_0):
		arg_9_0.Clear()
		arg_9_0.RemoveEvent()
		super().Dispose(arg_9_0)

	def SetVertifyFail(arg_10_0, arg_10_1):
		if not arg_10_0._vertifyFail:
			arg_10_0._vertifyFail = arg_10_1

	def onInitBattle(arg_11_0):
		arg_11_0._userFleet = arg_11_0._dataProxy.GetFleetByIFF(BattleConfig.FRIENDLY_CODE)

		arg_11_0._waveUpdater.SetWavesData(arg_11_0._dataProxy.GetStageInfo())

	def initWaveModule(arg_12_0):
		def var_12_0(arg_13_0, arg_13_1, arg_13_2):
			arg_12_0._dataProxy.SpawnMonster(arg_13_0, arg_13_1, arg_13_2, BattleConfig.FOE_CODE)

		def var_12_1(arg_14_0):
			arg_12_0._dataProxy.SpawnAirFighter(arg_14_0)

		def var_12_2():
			if arg_12_0._vertifyFail:
				M02.sendNotification(GAME.CHEATER_MARK, table(
					reason = arg_12_0._vertifyFail
				))

				return

			arg_12_0.CalcStatistic()
			arg_12_0._state.BattleEnd()

		def var_12_3(arg_16_0, arg_16_1, arg_16_2, arg_16_3, arg_16_4):
			arg_12_0._dataProxy.SpawnCubeArea(BattleConst.AOEField.SURFACE, -1, arg_16_0, arg_16_1, arg_16_2, arg_16_3, arg_16_4)

		arg_12_0._waveUpdater = BattleWaveUpdater.New(var_12_0, var_12_1, var_12_2, var_12_3)

	def InitProtocol(arg_17_0):
		return

	def AddEvent(arg_18_0):
		arg_18_0._dataProxy.RegisterEventListener(arg_18_0, BattleEvent.ADD_UNIT, arg_18_0.onAddUnit)
		arg_18_0._dataProxy.RegisterEventListener(arg_18_0, BattleEvent.REMOVE_UNIT, arg_18_0.onRemoveUnit)
		arg_18_0._dataProxy.RegisterEventListener(arg_18_0, BattleEvent.STAGE_DATA_INIT_FINISH, arg_18_0.onInitBattle)
		arg_18_0._dataProxy.RegisterEventListener(arg_18_0, BattleEvent.SHUT_DOWN_PLAYER, arg_18_0.onPlayerShutDown)
		arg_18_0._dataProxy.RegisterEventListener(arg_18_0, BattleEvent.UPDATE_COUNT_DOWN, arg_18_0.onUpdateCountDown)

	def RemoveEvent(arg_19_0):
		arg_19_0._dataProxy.UnregisterEventListener(arg_19_0, BattleEvent.ADD_UNIT)
		arg_19_0._dataProxy.UnregisterEventListener(arg_19_0, BattleEvent.REMOVE_UNIT)
		arg_19_0._dataProxy.UnregisterEventListener(arg_19_0, BattleEvent.STAGE_DATA_INIT_FINISH)
		arg_19_0._dataProxy.UnregisterEventListener(arg_19_0, BattleEvent.SHUT_DOWN_PLAYER)
		arg_19_0._dataProxy.UnregisterEventListener(arg_19_0, BattleEvent.UPDATE_COUNT_DOWN)

	def onAddUnit(arg_20_0, arg_20_1):
		var_20_0 = arg_20_1.Data.type
		var_20_1 = arg_20_1.Data.unit

		arg_20_0.RegisterUnitEvent(var_20_1)

		arg_20_0._unitDataList[var_20_1.GetUniqueID()] = var_20_1

		if var_20_0 == BattleConst.UnitType.ENEMY_UNIT or var_20_0 == BattleConst.UnitType.BOSS_UNIT:
			arg_20_0._waveUpdater.AddMonster(var_20_1)

	def RegisterUnitEvent(arg_21_0, arg_21_1):
		var_21_0 = arg_21_1.GetUnitType()

		if var_21_0 != BattleConst.UnitType.MINION_UNIT:
			arg_21_1.RegisterEventListener(arg_21_0, BattleUnitEvent.WILL_DIE, arg_21_0.onWillDie)

		arg_21_1.RegisterEventListener(arg_21_0, BattleUnitEvent.DYING, arg_21_0.onUnitDying)

		if var_21_0 == BattleConst.UnitType.PLAYER_UNIT:
			arg_21_1.RegisterEventListener(arg_21_0, BattleUnitEvent.SHUT_DOWN_PLAYER, arg_21_0.onShutDownPlayer)

	def UnregisterUnitEvent(arg_22_0, arg_22_1):
		arg_22_1.UnregisterEventListener(arg_22_0, BattleUnitEvent.WILL_DIE)
		arg_22_1.UnregisterEventListener(arg_22_0, BattleUnitEvent.DYING)

		if arg_22_1.GetUnitType() == BattleConst.UnitType.PLAYER_UNIT:
			arg_22_1.UnregisterEventListener(arg_22_0, BattleUnitEvent.SHUT_DOWN_PLAYER)

	def onRemoveUnit(arg_23_0, arg_23_1):
		var_23_0 = arg_23_1.Data.UID

		arg_23_0._waveUpdater.RemoveMonster(var_23_0)

		var_23_1 = arg_23_0._unitDataList[var_23_0]

		if var_23_1 == None:
			return

		arg_23_0.UnregisterUnitEvent(var_23_1)

		arg_23_0._unitDataList[var_23_0] = None

	def onPlayerShutDown(arg_24_0, arg_24_1):
		if arg_24_0._state.GetState() != arg_24_0._state.BATTLE_STATE_FIGHT:
			return

		if arg_24_1.Data.unit == arg_24_0._userFleet.GetFlagShip() and arg_24_0._dataProxy.GetInitData().battleType != SYSTEM_PROLOGUE and arg_24_0._dataProxy.GetInitData().battleType != SYSTEM_PERFORM:
			arg_24_0.CalcStatistic()
			arg_24_0._state.BattleEnd()

			return

		if len(arg_24_0._userFleet.GetScoutList()) == 0:
			arg_24_0.CalcStatistic()
			arg_24_0._state.BattleEnd()

	def onUpdateCountDown(arg_25_0, arg_25_1):
		if arg_25_0._dataProxy.GetCountDown() <= 0:
			arg_25_0._dataProxy.EnemyEscape()
			arg_25_0.CalcStatistic()
			arg_25_0._state.BattleTimeUp()

	def onUnitDying(arg_26_0, arg_26_1):
		var_26_0 = arg_26_1.Dispatcher.GetUniqueID()

		arg_26_0._dataProxy.KillUnit(var_26_0)

	def onWillDie(arg_27_0, arg_27_1):
		var_27_0 = arg_27_1.Dispatcher
		var_27_1 = BattleConst.UnitDeathReason
		var_27_2 = var_27_0.GetDeathReason()

		if var_27_2 == var_27_1.LEAVE:
			if var_27_0.GetIFF() == BattleConfig.FRIENDLY_CODE:
				arg_27_0._dataProxy.CalcBPWhenPlayerLeave(var_27_0)
		elif var_27_2 == var_27_1.DESTRUCT:
			arg_27_0._dataProxy.CalcBattleScoreWhenDead(var_27_0)

			if var_27_0.IsBoss():
				arg_27_0._dataProxy.AddScoreWhenBossDestruct()
		else:
			arg_27_0._dataProxy.CalcBattleScoreWhenDead(var_27_0)

		var_27_3 = arg_27_0._dataProxy.IsThereBoss()

		if var_27_0.IsBoss() and not var_27_3:
			arg_27_0._dataProxy.KillAllEnemy()

	def onShutDownPlayer(arg_28_0, arg_28_1):
		var_28_0 = arg_28_1.Dispatcher.GetUniqueID()

		arg_28_0._dataProxy.ShutdownPlayerUnit(var_28_0)

	def GetMaxRestHPRateBossRate(arg_29_0):
		var_29_0 = arg_29_0._waveUpdater.GetAllBossWave()

		for iter_29_0, iter_29_1 in ipairs(var_29_0):
			if iter_29_1.GetState() == iter_29_1.STATE_DEACTIVE:
				return 10000

		var_29_1 = 0

		for iter_29_2, iter_29_3 in pairs(arg_29_0._dataProxy.GetUnitList()):
			if iter_29_3.IsBoss() and iter_29_3.IsAlive():
				var_29_1 = max(var_29_1, iter_29_3.GetHPRate())

		return var_29_1 * 10000

	def CalcStatistic(arg_30_0):
		arg_30_0._dataProxy.CalcSingleDungeonScoreAtEnd(arg_30_0._userFleet)

		var_30_0 = arg_30_0.GetMaxRestHPRateBossRate()

		arg_30_0._dataProxy.CalcMaxRestHPRateBossRate(var_30_0)
