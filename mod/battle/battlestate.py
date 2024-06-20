from Framework.base.mvc.Facade import Facade
import ys





class bfConsts:
	DFT_CRIT_EFFECT = 1.5
	DFT_CRIT_RATE = 0.05
	SECONDs = 60
	PERCENT = 0.01
	PERCENT1 = 0.001
	PERCENT2 = 0.0001
	HUNDRED = 100
	SCORE_RATE = [
		0.7,
		0.8,
		0.3
	]
	CRASH_RATE = [
		0.05,
		0.025
	]
	SUBMARINE_KAMIKAZE = [
		80,
		3.5,
		1.5,
		1,
		0.5,
		0.5,
		1,
		0.005
	]
	LEAK_RATE = [
		10,
		2.2,
		0.7,
		0.3,
		1,
		0.005,
		0.5
	]
	PLANE_LEAK_RATE = [
		1,
		1,
		0.01,
		0.5,
		0.7,
		0.3,
		1,
		0.005,
		150,
		150,
		1,
		1
	]
	METEO_RATE = [
		0.05,
		20,
		0.6,
		0.4
	]
	NUM1 = 1
	NUM0 = 0
	NUM10000 = 10000
	ACCURACY = [
		0.1,
		2
	]
	DRATE = [
		25,
		0.02,
		0.0002,
		2000,
		0.1,
		0.8,
		150
	]
	SPEED_CONST = 0.02
	HP_CONST = 1.5


class BattleState(Facade):
	__name = "BattleState"
	BATTLE_STATE_IDLE = "BATTLE_IDLE"
	BATTLE_STATE_OPENING = "BATTLE_OPENING"
	BATTLE_STATE_FIGHT = "BATTLE_FIGHT"
	BATTLE_STATE_REPORT = "BATTLE_REPORT"

	def __init__(self):
		super().__new__(self)
		self.ChangeState(self.BATTLE_STATE_IDLE)

	def IsAutoBotActive(arg_2_0):
		var_2_0 = AutoBotCommand.GetAutoBotMark(arg_2_0)

		return PlayerPrefs.GetInt("autoBotIsAcitve" .. var_2_0, 0) == 1 and AutoBotCommand.autoBotSatisfied()

	def IsAutoSubActive(arg_3_0):
		local var_3_0 = AutoSubCommand.GetAutoSubMark(arg_3_0)

		return PlayerPrefs.GetInt("autoSubIsAcitve" .. var_3_0, 0) == 1

	def ChatUseable(arg_4_0):
		local var_4_0 = PlayerPrefs.GetInt(HIDE_CHAT_FLAG)
		local var_4_1 = not var_4_0 or var_4_0 != 1
		local var_4_2 = arg_4_0.GetBattleType()
		local var_4_3 = arg_4_0.IsAutoBotActive(var_4_2)
		local var_4_4 = var_4_2 == SYSTEM_DUEL
		local var_4_5 = var_4_2 == SYSTEM_CARDPUZZLE

		return var_4_1 and (var_4_4 or var_4_3) and not var_4_5

	def GetState(arg_5_0):
		return arg_5_0._state

	def GetBattleType(arg_6_0):
		return arg_6_0._battleType

	def SetBattleUI(arg_7_0, arg_7_1):
		arg_7_0._baseUI = arg_7_1

	def EnterBattle(arg_8_0, arg_8_1, arg_8_2):
		pg.TimeMgr.GetInstance().ResetCombatTime()
		arg_8_0.Active()
		arg_8_0.ResetTimer()

		arg_8_0._dataProxy = arg_8_0.AddDataProxy(var_0_0.Battle.BattleDataProxy.GetInstance())
		arg_8_0._uiMediator = arg_8_0.AddMediator(var_0_0.Battle.BattleUIMediator.New())

		if arg_8_1.battleType == SYSTEM_DUEL:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleDuelArenaCommand.New())

			arg_8_0._battleCommand.ConfigBattleData(arg_8_1)
		elif arg_8_1.battleType == SYSTEM_CHALLENGE:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleSingleChallengeCommand.New())

			arg_8_0._battleCommand.ConfigBattleData(arg_8_1)
		elif arg_8_1.battleType == SYSTEM_DODGEM:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleDodgemCommand.New())
		elif arg_8_1.battleType == SYSTEM_SUBMARINE_RUN:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleSubmarineRunCommand.New())
		elif arg_8_1.battleType == SYSTEM_SUB_ROUTINE:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleSubRoutineCommand.New())
		elif arg_8_1.battleType == SYSTEM_HP_SHARE_ACT_BOSS or arg_8_1.battleType == SYSTEM_BOSS_EXPERIMENT:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleInheritDungeonCommand.New())
		elif arg_8_1.battleType == SYSTEM_WORLD_BOSS:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleWorldBossCommand.New())
		elif arg_8_1.battleType == SYSTEM_DEBUG:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleDebugCommand.New())
		elif arg_8_1.battleType == SYSTEM_AIRFIGHT:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleAirFightCommand.New())
		elif arg_8_1.battleType == SYSTEM_GUILD:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleGuildBossCommand.New())
		elif arg_8_1.battleType == SYSTEM_CARDPUZZLE:
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleCardPuzzleCommand.New())
		else
			arg_8_0._battleCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleSingleDungeonCommand.New())

		arg_8_0._battleType = arg_8_1.battleType
		arg_8_0._sceneMediator = arg_8_0.AddMediator(var_0_0.Battle.BattleSceneMediator.New())
		arg_8_0._weaponCommand = arg_8_0.AddCommand(var_0_0.Battle.BattleControllerWeaponCommand.New())

		arg_8_0._dataProxy.InitBattle(arg_8_1)

		if BATTLE_DEFAULT_UNIT_DETAIL:
			arg_8_0.AddMediator(var_0_0.Battle.BattleReferenceBoxMediator.New())
			arg_8_0.GetMediatorByName(var_0_0.Battle.BattleReferenceBoxMediator.__name).ActiveUnitDetail(True)

		if arg_8_2:
			-- block empty
		else
			arg_8_0.ChangeState(BATTLE_STATE_OPENING)
			UpdateBeat.Add(arg_8_0.Update, arg_8_0)

	def GetSceneMediator(arg_9_0):
		return arg_9_0._sceneMediator

	def GetUIMediator(arg_10_0):
		return arg_10_0._uiMediator

	def ActiveBot(arg_11_0, arg_11_1):
		arg_11_0._weaponCommand.ActiveBot(arg_11_1, True)
		arg_11_0.EnableJoystick(not arg_11_1)

	def EnableJoystick(arg_12_0, arg_12_1):
		arg_12_0._uiMediator.EnableJoystick(arg_12_1)

	def IsBotActive(arg_13_0):
		return arg_13_0._weaponCommand.GetWeaponBot().IsActive()

	def Update(arg_14_0):
		if not arg_14_0._isPause:
			for iter_14_0, iter_14_1 in pairs(arg_14_0._mediatorList):
				iter_14_1.Update()
		else
			for iter_14_2, iter_14_3 in pairs(arg_14_0._mediatorList):
				iter_14_3.UpdatePause()

	def GenerateVertifyData(arg_15_0):
		return

	def Vertify():
		return True, -1

	def ChangeState(arg_17_0, arg_17_1):
		arg_17_0._state = arg_17_1

		if arg_17_1 == BATTLE_STATE_OPENING:
			arg_17_0._dataProxy.Start()

			local var_17_0 = arg_17_0._dataProxy._dungeonInfo.beginStoy

			if var_17_0:
				pg.NewStoryMgr.GetInstance().Play(var_17_0, function()
					arg_17_0._battleCommand.DoPrologue())
			else
				arg_17_0._battleCommand.DoPrologue()
		elif arg_17_1 == BATTLE_STATE_FIGHT:
			arg_17_0.ActiveAutoComponentTimer()
		elif arg_17_1 == BATTLE_STATE_REPORT:
			-- block empty

	def GetUI(arg_19_0):
		return arg_19_0._baseUI

	def ConfigBattleEndFunc(arg_20_0, arg_20_1):
		arg_20_0._endFunc = arg_20_1

	def BattleEnd(arg_21_0):
		arg_21_0.disableCommon()

		if arg_21_0._dataProxy.GetStatistics()._battleScore >= var_0_0.Battle.BattleConst.BattleScore.B:
			arg_21_0._dataProxy.CelebrateVictory(arg_21_0._dataProxy.GetFriendlyCode())
			arg_21_0.reportDelayTimer(function()
				arg_21_0.DoResult(), var_0_0.Battle.BattleConfig.CelebrateDuration)
		else
			arg_21_0.DoResult()

	def BattleTimeUp(arg_23_0):
		arg_23_0.disableCommon()
		arg_23_0.ActiveEscape()
		arg_23_0.reportDelayTimer(function()
			arg_23_0.DeactiveEscape()
			arg_23_0.DoResult(), var_0_0.Battle.BattleConfig.EscapeDuration)

	def DoResult(arg_25_0):
		arg_25_0._sceneMediator.PauseCharacterAction(True)
		arg_25_0._dataProxy.BotPercentage(arg_25_0._weaponCommand.GetBotActiveDuration())
		arg_25_0._dataProxy.HPRatioStatistics()
		arg_25_0._endFunc(arg_25_0._dataProxy.GetStatistics())

	def ExitBattle(arg_26_0):
		var_0_0.Battle.BattleCameraUtil.GetInstance().Clear()

		for iter_26_0, iter_26_1 in pairs(arg_26_0._mediatorList):
			arg_26_0.RemoveMediator(iter_26_1)

		for iter_26_2, iter_26_3 in pairs(arg_26_0._commandList):
			arg_26_0.RemoveCommand(iter_26_3)

		for iter_26_4, iter_26_5 in pairs(arg_26_0._proxyList):
			arg_26_0.RemoveProxy(iter_26_5)

		var_0_0.Battle.BattleConfig.BASIC_TIME_SCALE = 1

		arg_26_0.RemoveAllTimer()
		var_0_0.Battle.BattleResourceManager.GetInstance().Clear()

		arg_26_0._takeoverProcess = None

		arg_26_0.ChangeState(BATTLE_STATE_IDLE)

		arg_26_0._baseUI = None
		arg_26_0._endFunc = None
		arg_26_0._uiMediator = None
		arg_26_0._sceneMediator = None
		arg_26_0._battleCommand = None
		arg_26_0._weaponCommand = None

		removeSingletonInstance(var_0_0.Battle.BattleDataProxy)

		arg_26_0._dataProxy = None

		var_0_0.Battle.BattleVariable.Clear()
		var_0_0.Battle.BattleBulletFactory.DestroyFactory()
		UpdateBeat.Remove(arg_26_0.Update, arg_26_0)
		pg.EffectMgr.GetInstance().ClearBattleEffectMap()

		arg_26_0._timeScale = None
		arg_26_0._timescalerCache = None

		gcAll(True)

	def Stop(arg_27_0, arg_27_1):
		arg_27_0.disableCommon()
		arg_27_0._baseUI.exitBattle(arg_27_1)

	def disableCommon(arg_28_0):
		arg_28_0._weaponCommand.ActiveBot(False)
		arg_28_0.ScaleTimer()
		var_0_0.Battle.BattleCameraUtil.GetInstance().ResetFocus()
		arg_28_0.ChangeState(BATTLE_STATE_REPORT)
		arg_28_0._dataProxy.ClearAirFighterTimer()
		arg_28_0._dataProxy.KillAllAircraft()
		arg_28_0._sceneMediator.AllBulletNeutralize()
		var_0_0.Battle.BattleCameraUtil.GetInstance().StopShake()
		var_0_0.Battle.BattleCameraUtil.GetInstance().Deactive()
		arg_28_0._uiMediator.DisableComponent()
		arg_28_0.Deactive()

	def reportDelayTimer(arg_29_0, arg_29_1, arg_29_2):
		local var_29_0

		local function var_29_1()
			pg.TimeMgr.GetInstance().RemoveBattleTimer(var_29_0)

			var_29_0 = None

			arg_29_1()

		arg_29_0.RemoveAllTimer()
		pg.TimeMgr.GetInstance().ResumeBattleTimer()

		var_29_0 = pg.TimeMgr.GetInstance().AddBattleTimer("", -1, arg_29_2, var_29_1)

	def SetTakeoverProcess(arg_31_0, arg_31_1):
		assert(arg_31_0._takeoverProcess == None, "已经有接管的战斗过程，暂时没有定义这种逻辑")
		assert(arg_31_1.Pause != None and type(arg_31_1.Pause) == "function", "SetTakeoverProcess附加过程，必须要有Pause函数")
		assert(arg_31_1.Pause != None and type(arg_31_1.Resume) == "function", "SetTakeoverProcess附加过程，必须要有Pause函数")

		arg_31_0._takeoverProcess = arg_31_1

		arg_31_0._pause()

	def ClearTakeoverProcess(arg_32_0):
		assert(arg_32_0._takeoverProcess, "没有接管的战斗过程，暂时没有定义这种逻辑")

		arg_32_0._takeoverProcess = None

		arg_32_0._resume()

	def IsPause(arg_33_0):
		return arg_33_0._isPause

	def Pause(arg_34_0):
		local var_34_0 = arg_34_0._takeoverProcess

		if var_34_0:
			var_34_0.Pause()
		else
			arg_34_0._pause()

	def _pause(arg_35_0):
		arg_35_0.Deactive()
		arg_35_0._dataProxy.PausePuzzleComponent()
		arg_35_0._sceneMediator.Pause()

		if arg_35_0._timeScale != 1:
			arg_35_0.CacheTimescaler(arg_35_0._timeScale)
			arg_35_0.ScaleTimer(1)

		var_0_0.Battle.BattleCameraUtil.GetInstance().PauseCameraTween()

	def Resume(arg_36_0):
		if arg_36_0._state == BATTLE_STATE_IDLE:
			arg_36_0.ChangeState(BATTLE_STATE_OPENING)
			UpdateBeat.Add(arg_36_0.Update, arg_36_0)
		elif arg_36_0._state == BATTLE_STATE_REPORT:
			return

		local var_36_0 = arg_36_0._takeoverProcess

		if var_36_0:
			var_36_0.Resume()
		else
			arg_36_0._resume()

	def _resume(arg_37_0):
		arg_37_0._sceneMediator.Resume()
		arg_37_0.Active()
		arg_37_0._dataProxy.ResumePuzzleComponent()

		if arg_37_0._timescalerCache:
			arg_37_0.ScaleTimer(arg_37_0._timescalerCache)
			arg_37_0.CacheTimescaler()

		var_0_0.Battle.BattleCameraUtil.GetInstance().ResumeCameraTween()

	def ScaleTimer(arg_38_0, arg_38_1):
		arg_38_1 = arg_38_1 or var_0_0.Battle.BattleConfig.BASIC_TIME_SCALE

		pg.TimeMgr.GetInstance().ScaleBattleTimer(arg_38_1)

		arg_38_0._timeScale = arg_38_1

	def GetTimeScaleRate(arg_39_0):
		return arg_39_0._timeScale or 1

	def CacheTimescaler(arg_40_0, arg_40_1):
		arg_40_0._timescalerCache = arg_40_1

	def var_0_0.Battle.PlayBattleSFX(arg_41_0):
		if arg_41_0 != "":
			pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./" .. arg_41_0)

	def OpenConsole(arg_42_0):
		arg_42_0._uiMediator.InitDebugConsole()
		arg_42_0._uiMediator.ActiveDebugConsole()

	def ActiveReference(arg_43_0):
		arg_43_0._controllerCommand = arg_43_0.AddCommand(var_0_0.Battle.BattleControllerCommand.New())
