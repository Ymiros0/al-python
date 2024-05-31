local var_0_0 = class("LaunchBallGameView", import("..BaseMiniGameView"))

var_0_0.LEVEL_GAME = "leavel game"
var_0_0.PAUSE_GAME = "pause game "
var_0_0.OPEN_PAUSE_UI = "open pause ui"
var_0_0.OPEN_LEVEL_UI = "open leave ui"
var_0_0.BACK_MENU = "back menu"
var_0_0.CLOSE_GAME = "close game"
var_0_0.SHOW_RULE = "show rule"
var_0_0.READY_START = "ready start"
var_0_0.COUNT_DOWN = "count:wn"
var_0_0.STORE_SERVER = "store server"
var_0_0.SUBMIT_GAME_SUCCESS = "submit game success"
var_0_0.ADD_SCORE = "add score"
var_0_0.GAME_OVER = "game over"
var_0_0.JOYSTICK_ACTIVE_CHANGE = "joy stick active change"
var_0_0.PRESS_SKILL = "press skill"

local var_0_1 = True

def var_0_0.getUIName(arg_1_0):
	return LaunchBallGameVo.game_ui

def var_0_0.getBGM(arg_2_0):
	return LaunchBallGameVo.game_bgm

def var_0_0.didEnter(arg_3_0):
	if not LaunchBallGameVo.gameRoundData:
		LaunchBallGameVo.initRoundData(3, 1)

	arg_3_0.initData()
	arg_3_0.initEvent()
	arg_3_0.initUI()
	arg_3_0.initController()

	if LaunchBallGameVo.gameRoundData.type == LaunchBallGameConst.round_type_zhuanshu:
		LaunchBallGameVo.SetPlayer(LaunchBallGameVo.gameRoundData.player_id)
		arg_3_0.readyStart()

def var_0_0.initData(arg_4_0):
	LaunchBallGameVo.Init(arg_4_0.GetMGData().id, arg_4_0.GetMGHubData().id)

	local var_4_0 = LaunchBallGameVo.frameRate

	if var_4_0 > 60:
		var_4_0 = 60

	arg_4_0.timer = Timer.New(function()
		arg_4_0.onTimer(), 1 / var_4_0, -1)

def var_0_0.initEvent(arg_6_0):
	if not arg_6_0.handle and IsUnityEditor:
		arg_6_0.handle = UpdateBeat.CreateListener(arg_6_0.Update, arg_6_0)

		UpdateBeat.AddListener(arg_6_0.handle)

	arg_6_0.bind(var_0_0.LEVEL_GAME, function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_1:
			arg_6_0.resumeGame()
			arg_6_0.onGameOver()
		else
			arg_6_0.resumeGame())
	arg_6_0.bind(var_0_0.COUNT_DOWN, function(arg_8_0, arg_8_1, arg_8_2)
		arg_6_0.gameStart())
	arg_6_0.bind(var_0_0.OPEN_PAUSE_UI, function(arg_9_0, arg_9_1, arg_9_2)
		arg_6_0.popUI.popPauseUI())
	arg_6_0.bind(var_0_0.OPEN_LEVEL_UI, function(arg_10_0, arg_10_1, arg_10_2)
		arg_6_0.popUI.popLeaveUI())
	arg_6_0.bind(var_0_0.PAUSE_GAME, function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_1:
			arg_6_0.pauseGame()
		else
			arg_6_0.resumeGame())
	arg_6_0.bind(var_0_0.BACK_MENU, function(arg_12_0, arg_12_1, arg_12_2)
		if LaunchBallGameVo.gameRoundData.type != LaunchBallGameConst.round_type_wuxian:
			arg_6_0.closeView()

			return

		arg_6_0.menuUI.update(arg_6_0.GetMGHubData())
		arg_6_0.menuUI.show(True)
		arg_6_0.gameUI.show(False)
		arg_6_0.gameScene.showContainer(False)

		local var_12_0 = arg_6_0.getBGM()

		if not var_12_0:
			if pg.CriMgr.GetInstance().IsDefaultBGM():
				var_12_0 = pg.voice_bgm.NewMainScene.default_bgm
			else
				var_12_0 = pg.voice_bgm.NewMainScene.bgm

		if arg_6_0.bgm != var_12_0:
			arg_6_0.bgm = var_12_0

			pg.BgmMgr.GetInstance().Push(arg_6_0.__cname, var_12_0))
	arg_6_0.bind(var_0_0.CLOSE_GAME, function(arg_13_0, arg_13_1, arg_13_2)
		arg_6_0.closeView())
	arg_6_0.bind(var_0_0.GAME_OVER, function(arg_14_0, arg_14_1, arg_14_2)
		arg_6_0.onGameOver())
	arg_6_0.bind(var_0_0.SHOW_RULE, function(arg_15_0, arg_15_1, arg_15_2)
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[LaunchBallGameVo.rule_tip].tip
		}))
	arg_6_0.bind(var_0_0.READY_START, function(arg_16_0, arg_16_1, arg_16_2)
		arg_6_0.readyStart())
	arg_6_0.bind(var_0_0.STORE_SERVER, function(arg_17_0, arg_17_1, arg_17_2)
		arg_6_0.StoreDataToServer({
			arg_17_1
		}))
	arg_6_0.bind(var_0_0.SUBMIT_GAME_SUCCESS, function(arg_18_0, arg_18_1, arg_18_2)
		local var_18_0 = LaunchBallGameVo.gameRoundData.type
		local var_18_1 = LaunchBallGameVo.gameRoundData.type_index
		local var_18_2 = LaunchBallGameVo.scoreNum

		LaunchBallGameVo.UpdateGameResultData(LaunchBallGameVo.result_player, LaunchBallGameVo.selectPlayer)
		LaunchBallGameVo.UpdateGameResultData(LaunchBallGameVo.result_round, LaunchBallGameVo.gameRoundData.id)
		LaunchBallActivityMgr.GetGameAward(ActivityConst.MINIGAME_ZUMA, var_18_0, var_18_1, var_18_2)
		LaunchBallTaskMgr.CheckTaskUpdate(LaunchBallGameVo.gameResultData))
	arg_6_0.bind(var_0_0.ADD_SCORE, function(arg_19_0, arg_19_1, arg_19_2)
		arg_6_0.addScore(arg_19_1.num)
		arg_6_0.gameUI.addScore(arg_19_1))
	arg_6_0.bind(var_0_0.JOYSTICK_ACTIVE_CHANGE, function(arg_20_0, arg_20_1, arg_20_2)
		if arg_6_0.gameStartFlag:
			arg_6_0.gameScene.joystickActive(arg_20_1))
	arg_6_0.bind(var_0_0.PRESS_SKILL, function(arg_21_0, arg_21_1, arg_21_2)
		arg_6_0.gameScene.useSkill())

def var_0_0.initUI(arg_22_0):
	arg_22_0.clickMask = findTF(arg_22_0._tf, "clickMask")
	arg_22_0.popUI = LaunchBallGamePopUI.New(arg_22_0._tf, arg_22_0)

	arg_22_0.popUI.clearUI()

	arg_22_0.gameUI = LaunchBallGamingUI.New(arg_22_0._tf, arg_22_0)

	arg_22_0.gameUI.show(False)

	arg_22_0.menuUI = LaunchBallGameMenuUI.New(arg_22_0._tf, arg_22_0)

	arg_22_0.menuUI.update(arg_22_0.GetMGHubData())
	arg_22_0.menuUI.show(True)

def var_0_0.initController(arg_23_0):
	arg_23_0.gameScene = LaunchBallGameScene.New(arg_23_0._tf, arg_23_0)

def var_0_0.Update(arg_24_0):
	if arg_24_0.gameStop or arg_24_0.settlementFlag:
		return

	if IsUnityEditor:
		if Input.GetKeyDown(KeyCode.S) and arg_24_0.timer:
			arg_24_0.timerStop()

		if Input.GetKeyUp(KeyCode.S):
			arg_24_0.gameUI.press(KeyCode.S, False)

		if Input.GetKeyDown(KeyCode.W) and arg_24_0.timer:
			arg_24_0.timerStart()

		if Input.GetKeyUp(KeyCode.W):
			arg_24_0.gameUI.press(KeyCode.W, False)

		if Input.GetKeyDown(KeyCode.A):
			arg_24_0.gameUI.press(KeyCode.A, True)

		if Input.GetKeyUp(KeyCode.A):
			arg_24_0.gameUI.press(KeyCode.A, False)

		if Input.GetKeyDown(KeyCode.D):
			arg_24_0.gameUI.press(KeyCode.D, True)

		if Input.GetKeyUp(KeyCode.D):
			arg_24_0.gameUI.press(KeyCode.D, False)

		if Input.GetKeyDown(KeyCode.J):
			arg_24_0.onTimer()

def var_0_0.readyStart(arg_25_0):
	arg_25_0.readyStartFlag = True

	LaunchBallGameVo.Prepare()
	arg_25_0.popUI.readyStart()
	arg_25_0.menuUI.show(False)
	arg_25_0.gameUI.show(False)

def var_0_0.gameStart(arg_26_0):
	local var_26_0 = LaunchBallGameConst.map_data[LaunchBallGameVo.gameRoundData.map].bgm

	pg.BgmMgr.GetInstance().Push(arg_26_0.__cname, var_26_0)

	arg_26_0.bgm = var_26_0
	arg_26_0.readyStartFlag = False
	arg_26_0.gameStartFlag = True
	arg_26_0.sendSuccessFlag = False

	arg_26_0.popUI.popCountUI(False)
	arg_26_0.gameUI.start()
	arg_26_0.gameUI.show(True)
	arg_26_0.gameScene.start()
	arg_26_0.timerStart()

def var_0_0.changeSpeed(arg_27_0, arg_27_1):
	return

def var_0_0.onTimer(arg_28_0):
	arg_28_0.gameStep()

def var_0_0.gameStep(arg_29_0):
	arg_29_0.stepRunTimeData()
	arg_29_0.gameScene.step()
	arg_29_0.gameUI.step()

	if LaunchBallGameVo.gameTime <= 0:
		arg_29_0.onGameOver()

def var_0_0.timerStart(arg_30_0):
	if not arg_30_0.timer.running:
		arg_30_0.timer.Start()

def var_0_0.timerResume(arg_31_0):
	if not arg_31_0.timer.running:
		arg_31_0.timer.Start()

	arg_31_0.gameScene.resume()

def var_0_0.timerStop(arg_32_0):
	if arg_32_0.timer.running:
		arg_32_0.timer.Stop()

	arg_32_0.gameScene.stop()

def var_0_0.stepRunTimeData(arg_33_0):
	local var_33_0 = Time.deltaTime

	if var_33_0 > 0.016:
		var_33_0 = 0.016

	LaunchBallGameVo.gameTime = LaunchBallGameVo.gameTime - var_33_0
	LaunchBallGameVo.gameStepTime = LaunchBallGameVo.gameStepTime + var_33_0
	LaunchBallGameVo.deltaTime = var_33_0

def var_0_0.addScore(arg_34_0, arg_34_1):
	LaunchBallGameVo.scoreNum = LaunchBallGameVo.scoreNum + arg_34_1

def var_0_0.onGameOver(arg_35_0):
	if arg_35_0.settlementFlag:
		return

	arg_35_0.timerStop()
	arg_35_0.clearController()

	arg_35_0.settlementFlag = True

	setActive(arg_35_0.clickMask, True)
	LeanTween.delayedCall(go(arg_35_0._tf), 0.1, System.Action(function()
		arg_35_0.settlementFlag = False
		arg_35_0.gameStartFlag = False

		setActive(arg_35_0.clickMask, False)
		arg_35_0.popUI.updateSettlementUI()
		arg_35_0.popUI.popSettlementUI(True)))

def var_0_0.OnApplicationPaused(arg_37_0):
	if not arg_37_0.gameStartFlag:
		return

	if arg_37_0.readyStartFlag:
		return

	if arg_37_0.settlementFlag:
		return

	arg_37_0.pauseGame()
	arg_37_0.popUI.popPauseUI()

def var_0_0.clearController(arg_38_0):
	arg_38_0.gameScene.clear()

def var_0_0.pauseGame(arg_39_0):
	arg_39_0.gameStop = True

	arg_39_0.changeSpeed(0)
	arg_39_0.timerStop()

def var_0_0.resumeGame(arg_40_0):
	arg_40_0.gameStop = False

	arg_40_0.changeSpeed(1)
	arg_40_0.timerStart()

def var_0_0.onBackPressed(arg_41_0):
	if arg_41_0.readyStartFlag:
		return

	if not arg_41_0.gameStartFlag:
		arg_41_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_41_0.settlementFlag:
			return

		arg_41_0.popUI.backPressed()

def var_0_0.OnSendMiniGameOPDone(arg_42_0, arg_42_1):
	return

def var_0_0.willExit(arg_43_0):
	if arg_43_0.handle:
		UpdateBeat.RemoveListener(arg_43_0.handle)

	if arg_43_0._tf and LeanTween.isTweening(go(arg_43_0._tf)):
		LeanTween.cancel(go(arg_43_0._tf))

	if arg_43_0.timer and arg_43_0.timer.running:
		arg_43_0.timer.Stop()

	Time.timeScale = 1
	arg_43_0.timer = None

return var_0_0
