﻿local var_0_0 = class("LaunchBallGameView", import("..BaseMiniGameView"))

var_0_0.LEVEL_GAME = "leavel game"
var_0_0.PAUSE_GAME = "pause game "
var_0_0.OPEN_PAUSE_UI = "open pause ui"
var_0_0.OPEN_LEVEL_UI = "open leave ui"
var_0_0.BACK_MENU = "back menu"
var_0_0.CLOSE_GAME = "close game"
var_0_0.SHOW_RULE = "show rule"
var_0_0.READY_START = "ready start"
var_0_0.COUNT_DOWN = "count down"
var_0_0.STORE_SERVER = "store server"
var_0_0.SUBMIT_GAME_SUCCESS = "submit game success"
var_0_0.ADD_SCORE = "add score"
var_0_0.GAME_OVER = "game over"
var_0_0.JOYSTICK_ACTIVE_CHANGE = "joy stick active change"
var_0_0.PRESS_SKILL = "press skill"

local var_0_1 = true

function var_0_0.getUIName(arg_1_0)
	return LaunchBallGameVo.game_ui
end

function var_0_0.getBGM(arg_2_0)
	return LaunchBallGameVo.game_bgm
end

function var_0_0.didEnter(arg_3_0)
	if not LaunchBallGameVo.gameRoundData then
		LaunchBallGameVo.initRoundData(3, 1)
	end

	arg_3_0:initData()
	arg_3_0:initEvent()
	arg_3_0:initUI()
	arg_3_0:initController()

	if LaunchBallGameVo.gameRoundData.type == LaunchBallGameConst.round_type_zhuanshu then
		LaunchBallGameVo.SetPlayer(LaunchBallGameVo.gameRoundData.player_id)
		arg_3_0:readyStart()
	end
end

function var_0_0.initData(arg_4_0)
	LaunchBallGameVo.Init(arg_4_0:GetMGData().id, arg_4_0:GetMGHubData().id)

	local var_4_0 = LaunchBallGameVo.frameRate

	if var_4_0 > 60 then
		var_4_0 = 60
	end

	arg_4_0.timer = Timer.New(function()
		arg_4_0:onTimer()
	end, 1 / var_4_0, -1)
end

function var_0_0.initEvent(arg_6_0)
	if not arg_6_0.handle and IsUnityEditor then
		arg_6_0.handle = UpdateBeat:CreateListener(arg_6_0.Update, arg_6_0)

		UpdateBeat:AddListener(arg_6_0.handle)
	end

	arg_6_0:bind(var_0_0.LEVEL_GAME, function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_1 then
			arg_6_0:resumeGame()
			arg_6_0:onGameOver()
		else
			arg_6_0:resumeGame()
		end
	end)
	arg_6_0:bind(var_0_0.COUNT_DOWN, function(arg_8_0, arg_8_1, arg_8_2)
		arg_6_0:gameStart()
	end)
	arg_6_0:bind(var_0_0.OPEN_PAUSE_UI, function(arg_9_0, arg_9_1, arg_9_2)
		arg_6_0.popUI:popPauseUI()
	end)
	arg_6_0:bind(var_0_0.OPEN_LEVEL_UI, function(arg_10_0, arg_10_1, arg_10_2)
		arg_6_0.popUI:popLeaveUI()
	end)
	arg_6_0:bind(var_0_0.PAUSE_GAME, function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_1 then
			arg_6_0:pauseGame()
		else
			arg_6_0:resumeGame()
		end
	end)
	arg_6_0:bind(var_0_0.BACK_MENU, function(arg_12_0, arg_12_1, arg_12_2)
		if LaunchBallGameVo.gameRoundData.type ~= LaunchBallGameConst.round_type_wuxian then
			arg_6_0:closeView()

			return
		end

		arg_6_0.menuUI:update(arg_6_0:GetMGHubData())
		arg_6_0.menuUI:show(true)
		arg_6_0.gameUI:show(false)
		arg_6_0.gameScene:showContainer(false)

		local var_12_0 = arg_6_0:getBGM()

		if not var_12_0 then
			if pg.CriMgr.GetInstance():IsDefaultBGM() then
				var_12_0 = pg.voice_bgm.NewMainScene.default_bgm
			else
				var_12_0 = pg.voice_bgm.NewMainScene.bgm
			end
		end

		if arg_6_0.bgm ~= var_12_0 then
			arg_6_0.bgm = var_12_0

			pg.BgmMgr.GetInstance():Push(arg_6_0.__cname, var_12_0)
		end
	end)
	arg_6_0:bind(var_0_0.CLOSE_GAME, function(arg_13_0, arg_13_1, arg_13_2)
		arg_6_0:closeView()
	end)
	arg_6_0:bind(var_0_0.GAME_OVER, function(arg_14_0, arg_14_1, arg_14_2)
		arg_6_0:onGameOver()
	end)
	arg_6_0:bind(var_0_0.SHOW_RULE, function(arg_15_0, arg_15_1, arg_15_2)
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[LaunchBallGameVo.rule_tip].tip
		})
	end)
	arg_6_0:bind(var_0_0.READY_START, function(arg_16_0, arg_16_1, arg_16_2)
		arg_6_0:readyStart()
	end)
	arg_6_0:bind(var_0_0.STORE_SERVER, function(arg_17_0, arg_17_1, arg_17_2)
		arg_6_0:StoreDataToServer({
			arg_17_1
		})
	end)
	arg_6_0:bind(var_0_0.SUBMIT_GAME_SUCCESS, function(arg_18_0, arg_18_1, arg_18_2)
		local var_18_0 = LaunchBallGameVo.gameRoundData.type
		local var_18_1 = LaunchBallGameVo.gameRoundData.type_index
		local var_18_2 = LaunchBallGameVo.scoreNum

		LaunchBallGameVo.UpdateGameResultData(LaunchBallGameVo.result_player, LaunchBallGameVo.selectPlayer)
		LaunchBallGameVo.UpdateGameResultData(LaunchBallGameVo.result_round, LaunchBallGameVo.gameRoundData.id)
		LaunchBallActivityMgr.GetGameAward(ActivityConst.MINIGAME_ZUMA, var_18_0, var_18_1, var_18_2)
		LaunchBallTaskMgr.CheckTaskUpdate(LaunchBallGameVo.gameResultData)
	end)
	arg_6_0:bind(var_0_0.ADD_SCORE, function(arg_19_0, arg_19_1, arg_19_2)
		arg_6_0:addScore(arg_19_1.num)
		arg_6_0.gameUI:addScore(arg_19_1)
	end)
	arg_6_0:bind(var_0_0.JOYSTICK_ACTIVE_CHANGE, function(arg_20_0, arg_20_1, arg_20_2)
		if arg_6_0.gameStartFlag then
			arg_6_0.gameScene:joystickActive(arg_20_1)
		end
	end)
	arg_6_0:bind(var_0_0.PRESS_SKILL, function(arg_21_0, arg_21_1, arg_21_2)
		arg_6_0.gameScene:useSkill()
	end)
end

function var_0_0.initUI(arg_22_0)
	arg_22_0.clickMask = findTF(arg_22_0._tf, "clickMask")
	arg_22_0.popUI = LaunchBallGamePopUI.New(arg_22_0._tf, arg_22_0)

	arg_22_0.popUI:clearUI()

	arg_22_0.gameUI = LaunchBallGamingUI.New(arg_22_0._tf, arg_22_0)

	arg_22_0.gameUI:show(false)

	arg_22_0.menuUI = LaunchBallGameMenuUI.New(arg_22_0._tf, arg_22_0)

	arg_22_0.menuUI:update(arg_22_0:GetMGHubData())
	arg_22_0.menuUI:show(true)
end

function var_0_0.initController(arg_23_0)
	arg_23_0.gameScene = LaunchBallGameScene.New(arg_23_0._tf, arg_23_0)
end

function var_0_0.Update(arg_24_0)
	if arg_24_0.gameStop or arg_24_0.settlementFlag then
		return
	end

	if IsUnityEditor then
		if Input.GetKeyDown(KeyCode.S) and arg_24_0.timer then
			arg_24_0:timerStop()
		end

		if Input.GetKeyUp(KeyCode.S) then
			arg_24_0.gameUI:press(KeyCode.S, false)
		end

		if Input.GetKeyDown(KeyCode.W) and arg_24_0.timer then
			arg_24_0:timerStart()
		end

		if Input.GetKeyUp(KeyCode.W) then
			arg_24_0.gameUI:press(KeyCode.W, false)
		end

		if Input.GetKeyDown(KeyCode.A) then
			arg_24_0.gameUI:press(KeyCode.A, true)
		end

		if Input.GetKeyUp(KeyCode.A) then
			arg_24_0.gameUI:press(KeyCode.A, false)
		end

		if Input.GetKeyDown(KeyCode.D) then
			arg_24_0.gameUI:press(KeyCode.D, true)
		end

		if Input.GetKeyUp(KeyCode.D) then
			arg_24_0.gameUI:press(KeyCode.D, false)
		end

		if Input.GetKeyDown(KeyCode.J) then
			arg_24_0:onTimer()
		end
	end
end

function var_0_0.readyStart(arg_25_0)
	arg_25_0.readyStartFlag = true

	LaunchBallGameVo.Prepare()
	arg_25_0.popUI:readyStart()
	arg_25_0.menuUI:show(false)
	arg_25_0.gameUI:show(false)
end

function var_0_0.gameStart(arg_26_0)
	local var_26_0 = LaunchBallGameConst.map_data[LaunchBallGameVo.gameRoundData.map].bgm

	pg.BgmMgr.GetInstance():Push(arg_26_0.__cname, var_26_0)

	arg_26_0.bgm = var_26_0
	arg_26_0.readyStartFlag = false
	arg_26_0.gameStartFlag = true
	arg_26_0.sendSuccessFlag = false

	arg_26_0.popUI:popCountUI(false)
	arg_26_0.gameUI:start()
	arg_26_0.gameUI:show(true)
	arg_26_0.gameScene:start()
	arg_26_0:timerStart()
end

function var_0_0.changeSpeed(arg_27_0, arg_27_1)
	return
end

function var_0_0.onTimer(arg_28_0)
	arg_28_0:gameStep()
end

function var_0_0.gameStep(arg_29_0)
	arg_29_0:stepRunTimeData()
	arg_29_0.gameScene:step()
	arg_29_0.gameUI:step()

	if LaunchBallGameVo.gameTime <= 0 then
		arg_29_0:onGameOver()
	end
end

function var_0_0.timerStart(arg_30_0)
	if not arg_30_0.timer.running then
		arg_30_0.timer:Start()
	end
end

function var_0_0.timerResume(arg_31_0)
	if not arg_31_0.timer.running then
		arg_31_0.timer:Start()
	end

	arg_31_0.gameScene:resume()
end

function var_0_0.timerStop(arg_32_0)
	if arg_32_0.timer.running then
		arg_32_0.timer:Stop()
	end

	arg_32_0.gameScene:stop()
end

function var_0_0.stepRunTimeData(arg_33_0)
	local var_33_0 = Time.deltaTime

	if var_33_0 > 0.016 then
		var_33_0 = 0.016
	end

	LaunchBallGameVo.gameTime = LaunchBallGameVo.gameTime - var_33_0
	LaunchBallGameVo.gameStepTime = LaunchBallGameVo.gameStepTime + var_33_0
	LaunchBallGameVo.deltaTime = var_33_0
end

function var_0_0.addScore(arg_34_0, arg_34_1)
	LaunchBallGameVo.scoreNum = LaunchBallGameVo.scoreNum + arg_34_1
end

function var_0_0.onGameOver(arg_35_0)
	if arg_35_0.settlementFlag then
		return
	end

	arg_35_0:timerStop()
	arg_35_0:clearController()

	arg_35_0.settlementFlag = true

	setActive(arg_35_0.clickMask, true)
	LeanTween.delayedCall(go(arg_35_0._tf), 0.1, System.Action(function()
		arg_35_0.settlementFlag = false
		arg_35_0.gameStartFlag = false

		setActive(arg_35_0.clickMask, false)
		arg_35_0.popUI:updateSettlementUI()
		arg_35_0.popUI:popSettlementUI(true)
	end))
end

function var_0_0.OnApplicationPaused(arg_37_0)
	if not arg_37_0.gameStartFlag then
		return
	end

	if arg_37_0.readyStartFlag then
		return
	end

	if arg_37_0.settlementFlag then
		return
	end

	arg_37_0:pauseGame()
	arg_37_0.popUI:popPauseUI()
end

function var_0_0.clearController(arg_38_0)
	arg_38_0.gameScene:clear()
end

function var_0_0.pauseGame(arg_39_0)
	arg_39_0.gameStop = true

	arg_39_0:changeSpeed(0)
	arg_39_0:timerStop()
end

function var_0_0.resumeGame(arg_40_0)
	arg_40_0.gameStop = false

	arg_40_0:changeSpeed(1)
	arg_40_0:timerStart()
end

function var_0_0.onBackPressed(arg_41_0)
	if arg_41_0.readyStartFlag then
		return
	end

	if not arg_41_0.gameStartFlag then
		arg_41_0:emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_41_0.settlementFlag then
			return
		end

		arg_41_0.popUI:backPressed()
	end
end

function var_0_0.OnSendMiniGameOPDone(arg_42_0, arg_42_1)
	return
end

function var_0_0.willExit(arg_43_0)
	if arg_43_0.handle then
		UpdateBeat:RemoveListener(arg_43_0.handle)
	end

	if arg_43_0._tf and LeanTween.isTweening(go(arg_43_0._tf)) then
		LeanTween.cancel(go(arg_43_0._tf))
	end

	if arg_43_0.timer and arg_43_0.timer.running then
		arg_43_0.timer:Stop()
	end

	Time.timeScale = 1
	arg_43_0.timer = nil
end

return var_0_0
