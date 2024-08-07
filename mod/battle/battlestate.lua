﻿ys = ys or {}

local var_0_0 = ys

var_0_0.Battle = var_0_0.Battle or {}

local var_0_1 = {}

pg.bfConsts = var_0_1
var_0_1.DFT_CRIT_EFFECT = 1.5
var_0_1.DFT_CRIT_RATE = 0.05
var_0_1.SECONDs = 60
var_0_1.PERCENT = 0.01
var_0_1.PERCENT1 = 0.001
var_0_1.PERCENT2 = 0.0001
var_0_1.HUNDRED = 100
var_0_1.SCORE_RATE = {
	0.7,
	0.8,
	0.3
}
var_0_1.CRASH_RATE = {
	0.05,
	0.025
}
var_0_1.SUBMARINE_KAMIKAZE = {
	80,
	3.5,
	1.5,
	1,
	0.5,
	0.5,
	1,
	0.005
}
var_0_1.LEAK_RATE = {
	10,
	2.2,
	0.7,
	0.3,
	1,
	0.005,
	0.5
}
var_0_1.PLANE_LEAK_RATE = {
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
}
var_0_1.METEO_RATE = {
	0.05,
	20,
	0.6,
	0.4
}
var_0_1.NUM1 = 1
var_0_1.NUM0 = 0
var_0_1.NUM10000 = 10000
var_0_1.ACCURACY = {
	0.1,
	2
}
var_0_1.DRATE = {
	25,
	0.02,
	0.0002,
	2000,
	0.1,
	0.8,
	150
}
var_0_1.SPEED_CONST = 0.02
var_0_1.HP_CONST = 1.5

local var_0_2 = singletonClass("BattleState", var_0_0.MVC.Facade)

var_0_0.Battle.BattleState = var_0_2
var_0_2.__name = "BattleState"
var_0_2.BATTLE_STATE_IDLE = "BATTLE_IDLE"
var_0_2.BATTLE_STATE_OPENING = "BATTLE_OPENING"
var_0_2.BATTLE_STATE_FIGHT = "BATTLE_FIGHT"
var_0_2.BATTLE_STATE_REPORT = "BATTLE_REPORT"

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0)
	arg_1_0:ChangeState(var_0_2.BATTLE_STATE_IDLE)
end

function var_0_2.IsAutoBotActive(arg_2_0)
	local var_2_0 = AutoBotCommand.GetAutoBotMark(arg_2_0)

	return PlayerPrefs.GetInt("autoBotIsAcitve" .. var_2_0, 0) == 1 and AutoBotCommand.autoBotSatisfied()
end

function var_0_2.IsAutoSubActive(arg_3_0)
	local var_3_0 = AutoSubCommand.GetAutoSubMark(arg_3_0)

	return PlayerPrefs.GetInt("autoSubIsAcitve" .. var_3_0, 0) == 1
end

function var_0_2.ChatUseable(arg_4_0)
	local var_4_0 = PlayerPrefs.GetInt(HIDE_CHAT_FLAG)
	local var_4_1 = not var_4_0 or var_4_0 ~= 1
	local var_4_2 = arg_4_0:GetBattleType()
	local var_4_3 = arg_4_0.IsAutoBotActive(var_4_2)
	local var_4_4 = var_4_2 == SYSTEM_DUEL
	local var_4_5 = var_4_2 == SYSTEM_CARDPUZZLE

	return var_4_1 and (var_4_4 or var_4_3) and not var_4_5
end

function var_0_2.GetState(arg_5_0)
	return arg_5_0._state
end

function var_0_2.GetBattleType(arg_6_0)
	return arg_6_0._battleType
end

function var_0_2.SetBattleUI(arg_7_0, arg_7_1)
	arg_7_0._baseUI = arg_7_1
end

function var_0_2.EnterBattle(arg_8_0, arg_8_1, arg_8_2)
	pg.TimeMgr.GetInstance():ResetCombatTime()
	arg_8_0:Active()
	arg_8_0:ResetTimer()

	arg_8_0._dataProxy = arg_8_0:AddDataProxy(var_0_0.Battle.BattleDataProxy.GetInstance())
	arg_8_0._uiMediator = arg_8_0:AddMediator(var_0_0.Battle.BattleUIMediator.New())

	if arg_8_1.battleType == SYSTEM_DUEL then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleDuelArenaCommand.New())

		arg_8_0._battleCommand:ConfigBattleData(arg_8_1)
	elseif arg_8_1.battleType == SYSTEM_CHALLENGE then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleSingleChallengeCommand.New())

		arg_8_0._battleCommand:ConfigBattleData(arg_8_1)
	elseif arg_8_1.battleType == SYSTEM_DODGEM then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleDodgemCommand.New())
	elseif arg_8_1.battleType == SYSTEM_SUBMARINE_RUN then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleSubmarineRunCommand.New())
	elseif arg_8_1.battleType == SYSTEM_SUB_ROUTINE then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleSubRoutineCommand.New())
	elseif arg_8_1.battleType == SYSTEM_HP_SHARE_ACT_BOSS or arg_8_1.battleType == SYSTEM_BOSS_EXPERIMENT then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleInheritDungeonCommand.New())
	elseif arg_8_1.battleType == SYSTEM_WORLD_BOSS then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleWorldBossCommand.New())
	elseif arg_8_1.battleType == SYSTEM_DEBUG then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleDebugCommand.New())
	elseif arg_8_1.battleType == SYSTEM_AIRFIGHT then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleAirFightCommand.New())
	elseif arg_8_1.battleType == SYSTEM_GUILD then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleGuildBossCommand.New())
	elseif arg_8_1.battleType == SYSTEM_CARDPUZZLE then
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleCardPuzzleCommand.New())
	else
		arg_8_0._battleCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleSingleDungeonCommand.New())
	end

	arg_8_0._battleType = arg_8_1.battleType
	arg_8_0._sceneMediator = arg_8_0:AddMediator(var_0_0.Battle.BattleSceneMediator.New())
	arg_8_0._weaponCommand = arg_8_0:AddCommand(var_0_0.Battle.BattleControllerWeaponCommand.New())

	arg_8_0._dataProxy:InitBattle(arg_8_1)

	if BATTLE_DEFAULT_UNIT_DETAIL then
		arg_8_0:AddMediator(var_0_0.Battle.BattleReferenceBoxMediator.New())
		arg_8_0:GetMediatorByName(var_0_0.Battle.BattleReferenceBoxMediator.__name):ActiveUnitDetail(true)
	end

	if arg_8_2 then
		-- block empty
	else
		arg_8_0:ChangeState(var_0_2.BATTLE_STATE_OPENING)
		UpdateBeat:Add(arg_8_0.Update, arg_8_0)
	end
end

function var_0_2.GetSceneMediator(arg_9_0)
	return arg_9_0._sceneMediator
end

function var_0_2.GetUIMediator(arg_10_0)
	return arg_10_0._uiMediator
end

function var_0_2.ActiveBot(arg_11_0, arg_11_1)
	arg_11_0._weaponCommand:ActiveBot(arg_11_1, true)
	arg_11_0:EnableJoystick(not arg_11_1)
end

function var_0_2.EnableJoystick(arg_12_0, arg_12_1)
	arg_12_0._uiMediator:EnableJoystick(arg_12_1)
end

function var_0_2.IsBotActive(arg_13_0)
	return arg_13_0._weaponCommand:GetWeaponBot():IsActive()
end

function var_0_2.Update(arg_14_0)
	if not arg_14_0._isPause then
		for iter_14_0, iter_14_1 in pairs(arg_14_0._mediatorList) do
			iter_14_1:Update()
		end
	else
		for iter_14_2, iter_14_3 in pairs(arg_14_0._mediatorList) do
			iter_14_3:UpdatePause()
		end
	end
end

function var_0_2.GenerateVertifyData(arg_15_0)
	return
end

function var_0_2.Vertify()
	return true, -1
end

function var_0_2.ChangeState(arg_17_0, arg_17_1)
	arg_17_0._state = arg_17_1

	if arg_17_1 == var_0_2.BATTLE_STATE_OPENING then
		arg_17_0._dataProxy:Start()

		local var_17_0 = arg_17_0._dataProxy._dungeonInfo.beginStoy

		if var_17_0 then
			pg.NewStoryMgr.GetInstance():Play(var_17_0, function()
				arg_17_0._battleCommand:DoPrologue()
			end)
		else
			arg_17_0._battleCommand:DoPrologue()
		end
	elseif arg_17_1 == var_0_2.BATTLE_STATE_FIGHT then
		arg_17_0:ActiveAutoComponentTimer()
	elseif arg_17_1 == var_0_2.BATTLE_STATE_REPORT then
		-- block empty
	end
end

function var_0_2.GetUI(arg_19_0)
	return arg_19_0._baseUI
end

function var_0_2.ConfigBattleEndFunc(arg_20_0, arg_20_1)
	arg_20_0._endFunc = arg_20_1
end

function var_0_2.BattleEnd(arg_21_0)
	arg_21_0:disableCommon()

	if arg_21_0._dataProxy:GetStatistics()._battleScore >= var_0_0.Battle.BattleConst.BattleScore.B then
		arg_21_0._dataProxy:CelebrateVictory(arg_21_0._dataProxy:GetFriendlyCode())
		arg_21_0:reportDelayTimer(function()
			arg_21_0:DoResult()
		end, var_0_0.Battle.BattleConfig.CelebrateDuration)
	else
		arg_21_0:DoResult()
	end
end

function var_0_2.BattleTimeUp(arg_23_0)
	arg_23_0:disableCommon()
	arg_23_0:ActiveEscape()
	arg_23_0:reportDelayTimer(function()
		arg_23_0:DeactiveEscape()
		arg_23_0:DoResult()
	end, var_0_0.Battle.BattleConfig.EscapeDuration)
end

function var_0_2.DoResult(arg_25_0)
	arg_25_0._sceneMediator:PauseCharacterAction(true)
	arg_25_0._dataProxy:BotPercentage(arg_25_0._weaponCommand:GetBotActiveDuration())
	arg_25_0._dataProxy:HPRatioStatistics()
	arg_25_0._endFunc(arg_25_0._dataProxy:GetStatistics())
end

function var_0_2.ExitBattle(arg_26_0)
	var_0_0.Battle.BattleCameraUtil.GetInstance():Clear()

	for iter_26_0, iter_26_1 in pairs(arg_26_0._mediatorList) do
		arg_26_0:RemoveMediator(iter_26_1)
	end

	for iter_26_2, iter_26_3 in pairs(arg_26_0._commandList) do
		arg_26_0:RemoveCommand(iter_26_3)
	end

	for iter_26_4, iter_26_5 in pairs(arg_26_0._proxyList) do
		arg_26_0:RemoveProxy(iter_26_5)
	end

	var_0_0.Battle.BattleConfig.BASIC_TIME_SCALE = 1

	arg_26_0:RemoveAllTimer()
	var_0_0.Battle.BattleResourceManager.GetInstance():Clear()

	arg_26_0._takeoverProcess = nil

	arg_26_0:ChangeState(var_0_2.BATTLE_STATE_IDLE)

	arg_26_0._baseUI = nil
	arg_26_0._endFunc = nil
	arg_26_0._uiMediator = nil
	arg_26_0._sceneMediator = nil
	arg_26_0._battleCommand = nil
	arg_26_0._weaponCommand = nil

	removeSingletonInstance(var_0_0.Battle.BattleDataProxy)

	arg_26_0._dataProxy = nil

	var_0_0.Battle.BattleVariable.Clear()
	var_0_0.Battle.BattleBulletFactory.DestroyFactory()
	UpdateBeat:Remove(arg_26_0.Update, arg_26_0)
	pg.EffectMgr.GetInstance():ClearBattleEffectMap()

	arg_26_0._timeScale = nil
	arg_26_0._timescalerCache = nil

	gcAll(true)
end

function var_0_2.Stop(arg_27_0, arg_27_1)
	arg_27_0:disableCommon()
	arg_27_0._baseUI:exitBattle(arg_27_1)
end

function var_0_2.disableCommon(arg_28_0)
	arg_28_0._weaponCommand:ActiveBot(false)
	arg_28_0:ScaleTimer()
	var_0_0.Battle.BattleCameraUtil.GetInstance():ResetFocus()
	arg_28_0:ChangeState(var_0_2.BATTLE_STATE_REPORT)
	arg_28_0._dataProxy:ClearAirFighterTimer()
	arg_28_0._dataProxy:KillAllAircraft()
	arg_28_0._sceneMediator:AllBulletNeutralize()
	var_0_0.Battle.BattleCameraUtil.GetInstance():StopShake()
	var_0_0.Battle.BattleCameraUtil.GetInstance():Deactive()
	arg_28_0._uiMediator:DisableComponent()
	arg_28_0:Deactive()
end

function var_0_2.reportDelayTimer(arg_29_0, arg_29_1, arg_29_2)
	local var_29_0

	local function var_29_1()
		pg.TimeMgr.GetInstance():RemoveBattleTimer(var_29_0)

		var_29_0 = nil

		arg_29_1()
	end

	arg_29_0:RemoveAllTimer()
	pg.TimeMgr.GetInstance():ResumeBattleTimer()

	var_29_0 = pg.TimeMgr.GetInstance():AddBattleTimer("", -1, arg_29_2, var_29_1)
end

function var_0_2.SetTakeoverProcess(arg_31_0, arg_31_1)
	assert(arg_31_0._takeoverProcess == nil, "已经有接管的战斗过程，暂时没有定义这种逻辑")
	assert(arg_31_1.Pause ~= nil and type(arg_31_1.Pause) == "function", "SetTakeoverProcess附加过程，必须要有Pause函数")
	assert(arg_31_1.Pause ~= nil and type(arg_31_1.Resume) == "function", "SetTakeoverProcess附加过程，必须要有Pause函数")

	arg_31_0._takeoverProcess = arg_31_1

	arg_31_0:_pause()
end

function var_0_2.ClearTakeoverProcess(arg_32_0)
	assert(arg_32_0._takeoverProcess, "没有接管的战斗过程，暂时没有定义这种逻辑")

	arg_32_0._takeoverProcess = nil

	arg_32_0:_resume()
end

function var_0_2.IsPause(arg_33_0)
	return arg_33_0._isPause
end

function var_0_2.Pause(arg_34_0)
	local var_34_0 = arg_34_0._takeoverProcess

	if var_34_0 then
		var_34_0.Pause()
	else
		arg_34_0:_pause()
	end
end

function var_0_2._pause(arg_35_0)
	arg_35_0:Deactive()
	arg_35_0._dataProxy:PausePuzzleComponent()
	arg_35_0._sceneMediator:Pause()

	if arg_35_0._timeScale ~= 1 then
		arg_35_0:CacheTimescaler(arg_35_0._timeScale)
		arg_35_0:ScaleTimer(1)
	end

	var_0_0.Battle.BattleCameraUtil.GetInstance():PauseCameraTween()
end

function var_0_2.Resume(arg_36_0)
	if arg_36_0._state == var_0_2.BATTLE_STATE_IDLE then
		arg_36_0:ChangeState(var_0_2.BATTLE_STATE_OPENING)
		UpdateBeat:Add(arg_36_0.Update, arg_36_0)
	elseif arg_36_0._state == var_0_2.BATTLE_STATE_REPORT then
		return
	end

	local var_36_0 = arg_36_0._takeoverProcess

	if var_36_0 then
		var_36_0.Resume()
	else
		arg_36_0:_resume()
	end
end

function var_0_2._resume(arg_37_0)
	arg_37_0._sceneMediator:Resume()
	arg_37_0:Active()
	arg_37_0._dataProxy:ResumePuzzleComponent()

	if arg_37_0._timescalerCache then
		arg_37_0:ScaleTimer(arg_37_0._timescalerCache)
		arg_37_0:CacheTimescaler()
	end

	var_0_0.Battle.BattleCameraUtil.GetInstance():ResumeCameraTween()
end

function var_0_2.ScaleTimer(arg_38_0, arg_38_1)
	arg_38_1 = arg_38_1 or var_0_0.Battle.BattleConfig.BASIC_TIME_SCALE

	pg.TimeMgr.GetInstance():ScaleBattleTimer(arg_38_1)

	arg_38_0._timeScale = arg_38_1
end

function var_0_2.GetTimeScaleRate(arg_39_0)
	return arg_39_0._timeScale or 1
end

function var_0_2.CacheTimescaler(arg_40_0, arg_40_1)
	arg_40_0._timescalerCache = arg_40_1
end

function var_0_0.Battle.PlayBattleSFX(arg_41_0)
	if arg_41_0 ~= "" then
		pg.CriMgr.GetInstance():PlaySoundEffect_V3("event:/" .. arg_41_0)
	end
end

function var_0_2.OpenConsole(arg_42_0)
	arg_42_0._uiMediator:InitDebugConsole()
	arg_42_0._uiMediator:ActiveDebugConsole()
end

function var_0_2.ActiveReference(arg_43_0)
	arg_43_0._controllerCommand = arg_43_0:AddCommand(var_0_0.Battle.BattleControllerCommand.New())
end
