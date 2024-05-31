local var_0_0 = class("CastleGameView", import("..BaseMiniGameView"))

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

def var_0_0.getUIName(arg_1_0):
	return CastleGameVo.game_ui

def var_0_0.didEnter(arg_2_0):
	arg_2_0.initData()
	arg_2_0.initEvent()
	arg_2_0.initUI()
	arg_2_0.initController()

def var_0_0.initData(arg_3_0):
	CastleGameVo.Init(arg_3_0.GetMGData().id, arg_3_0.GetMGHubData().id)

	local var_3_0 = CastleGameVo.frameRate

	if var_3_0 > 60:
		var_3_0 = 60

	arg_3_0.timer = Timer.New(function()
		arg_3_0.onTimer(), 1 / var_3_0, -1)

def var_0_0.initEvent(arg_5_0):
	if not arg_5_0.handle and IsUnityEditor:
		arg_5_0.handle = UpdateBeat.CreateListener(arg_5_0.Update, arg_5_0)

		UpdateBeat.AddListener(arg_5_0.handle)

	arg_5_0.bind(var_0_0.LEVEL_GAME, function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_1:
			arg_5_0.resumeGame()
			arg_5_0.onGameOver()
		else
			arg_5_0.resumeGame())
	arg_5_0.bind(var_0_0.COUNT_DOWN, function(arg_7_0, arg_7_1, arg_7_2)
		arg_5_0.gameStart())
	arg_5_0.bind(var_0_0.OPEN_PAUSE_UI, function(arg_8_0, arg_8_1, arg_8_2)
		arg_5_0.popUI.popPauseUI())
	arg_5_0.bind(var_0_0.OPEN_LEVEL_UI, function(arg_9_0, arg_9_1, arg_9_2)
		arg_5_0.popUI.popLeaveUI())
	arg_5_0.bind(var_0_0.PAUSE_GAME, function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_1:
			arg_5_0.pauseGame()
		else
			arg_5_0.resumeGame())
	arg_5_0.bind(var_0_0.BACK_MENU, function(arg_11_0, arg_11_1, arg_11_2)
		arg_5_0.menuUI.update(arg_5_0.GetMGHubData())
		arg_5_0.menuUI.show(True)
		arg_5_0.gameUI.show(False)
		arg_5_0.gameScene.showContainer(False)

		local var_11_0 = arg_5_0.getBGM()

		if not var_11_0:
			if pg.CriMgr.GetInstance().IsDefaultBGM():
				var_11_0 = pg.voice_bgm.NewMainScene.default_bgm
			else
				var_11_0 = pg.voice_bgm.NewMainScene.bgm

		if arg_5_0.bgm != var_11_0:
			arg_5_0.bgm = var_11_0

			pg.BgmMgr.GetInstance().Push(arg_5_0.__cname, var_11_0))
	arg_5_0.bind(var_0_0.CLOSE_GAME, function(arg_12_0, arg_12_1, arg_12_2)
		arg_5_0.closeView())
	arg_5_0.bind(var_0_0.GAME_OVER, function(arg_13_0, arg_13_1, arg_13_2)
		arg_5_0.onGameOver())
	arg_5_0.bind(var_0_0.SHOW_RULE, function(arg_14_0, arg_14_1, arg_14_2)
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[CastleGameVo.rule_tip].tip
		}))
	arg_5_0.bind(var_0_0.READY_START, function(arg_15_0, arg_15_1, arg_15_2)
		arg_5_0.readyStart())
	arg_5_0.bind(var_0_0.STORE_SERVER, function(arg_16_0, arg_16_1, arg_16_2)
		arg_5_0.StoreDataToServer({
			arg_16_1
		}))
	arg_5_0.bind(var_0_0.SUBMIT_GAME_SUCCESS, function(arg_17_0, arg_17_1, arg_17_2)
		if not arg_5_0.sendSuccessFlag:
			arg_5_0.sendSuccessFlag = True

			arg_5_0.SendSuccess(0))
	arg_5_0.bind(var_0_0.ADD_SCORE, function(arg_18_0, arg_18_1, arg_18_2)
		arg_5_0.addScore(arg_18_1.num)
		arg_5_0.gameUI.addScore(arg_18_1))

def var_0_0.initUI(arg_19_0):
	arg_19_0.clickMask = findTF(arg_19_0._tf, "clickMask")
	arg_19_0.popUI = CastleGamePopUI.New(arg_19_0._tf, arg_19_0)

	arg_19_0.popUI.clearUI()

	arg_19_0.gameUI = CastleGamingUI.New(arg_19_0._tf, arg_19_0)
	arg_19_0.menuUI = CastleGameMenuUI.New(arg_19_0._tf, arg_19_0)

	arg_19_0.menuUI.update(arg_19_0.GetMGHubData())
	arg_19_0.menuUI.show(True)

def var_0_0.initController(arg_20_0):
	arg_20_0.gameScene = CastleGameScene.New(arg_20_0._tf, arg_20_0)

def var_0_0.Update(arg_21_0):
	if arg_21_0.gameStop or arg_21_0.settlementFlag:
		return

	if IsUnityEditor:
		if Input.GetKeyDown(KeyCode.S):
			arg_21_0.gameUI.press(KeyCode.S, True)

		if Input.GetKeyUp(KeyCode.S):
			arg_21_0.gameUI.press(KeyCode.S, False)

		if Input.GetKeyDown(KeyCode.W):
			arg_21_0.gameUI.press(KeyCode.W, True)

		if Input.GetKeyUp(KeyCode.W):
			arg_21_0.gameUI.press(KeyCode.W, False)

		if Input.GetKeyDown(KeyCode.A):
			arg_21_0.gameUI.press(KeyCode.A, True)

		if Input.GetKeyUp(KeyCode.A):
			arg_21_0.gameUI.press(KeyCode.A, False)

		if Input.GetKeyDown(KeyCode.D):
			arg_21_0.gameUI.press(KeyCode.D, True)

		if Input.GetKeyUp(KeyCode.D):
			arg_21_0.gameUI.press(KeyCode.D, False)

def var_0_0.readyStart(arg_22_0):
	arg_22_0.readyStartFlag = True

	CastleGameVo.Prepare()
	arg_22_0.popUI.readyStart()
	arg_22_0.menuUI.show(False)
	arg_22_0.gameUI.show(False)

def var_0_0.gameStart(arg_23_0):
	arg_23_0.readyStartFlag = False
	arg_23_0.gameStartFlag = True
	arg_23_0.sendSuccessFlag = False

	arg_23_0.popUI.popCountUI(False)
	arg_23_0.gameUI.start()
	arg_23_0.gameUI.show(True)
	arg_23_0.gameScene.start()
	arg_23_0.timerStart()

def var_0_0.changeSpeed(arg_24_0, arg_24_1):
	return

def var_0_0.onTimer(arg_25_0):
	arg_25_0.gameStep()

def var_0_0.gameStep(arg_26_0):
	arg_26_0.stepRunTimeData()
	arg_26_0.gameScene.step()
	arg_26_0.gameUI.step()

	if CastleGameVo.gameTime <= 0:
		arg_26_0.onGameOver()

def var_0_0.timerStart(arg_27_0):
	if not arg_27_0.timer.running:
		arg_27_0.timer.Start()

def var_0_0.timerResume(arg_28_0):
	if not arg_28_0.timer.running:
		arg_28_0.timer.Start()

	arg_28_0.gameScene.resume()

def var_0_0.timerStop(arg_29_0):
	if arg_29_0.timer.running:
		arg_29_0.timer.Stop()

	arg_29_0.gameScene.stop()

def var_0_0.stepRunTimeData(arg_30_0):
	local var_30_0 = Time.deltaTime

	if var_30_0 > 0.016:
		var_30_0 = 0.016

	CastleGameVo.gameTime = CastleGameVo.gameTime - var_30_0
	CastleGameVo.gameStepTime = CastleGameVo.gameStepTime + var_30_0
	CastleGameVo.deltaTime = var_30_0

def var_0_0.addScore(arg_31_0, arg_31_1):
	CastleGameVo.scoreNum = CastleGameVo.scoreNum + arg_31_1

def var_0_0.onGameOver(arg_32_0):
	if arg_32_0.settlementFlag:
		return

	arg_32_0.timerStop()
	arg_32_0.clearController()

	arg_32_0.settlementFlag = True

	setActive(arg_32_0.clickMask, True)
	LeanTween.delayedCall(go(arg_32_0._tf), 0.1, System.Action(function()
		arg_32_0.settlementFlag = False
		arg_32_0.gameStartFlag = False

		setActive(arg_32_0.clickMask, False)
		arg_32_0.popUI.updateSettlementUI()
		arg_32_0.popUI.popSettlementUI(True)))

def var_0_0.OnApplicationPaused(arg_34_0):
	if not arg_34_0.gameStartFlag:
		return

	if arg_34_0.readyStartFlag:
		return

	if arg_34_0.settlementFlag:
		return

	arg_34_0.pauseGame()
	arg_34_0.popUI.popPauseUI()

def var_0_0.clearController(arg_35_0):
	arg_35_0.gameScene.clear()

def var_0_0.pauseGame(arg_36_0):
	arg_36_0.gameStop = True

	arg_36_0.changeSpeed(0)
	arg_36_0.timerStop()

def var_0_0.resumeGame(arg_37_0):
	arg_37_0.gameStop = False

	arg_37_0.changeSpeed(1)
	arg_37_0.timerStart()

def var_0_0.onBackPressed(arg_38_0):
	if arg_38_0.readyStartFlag:
		return

	if not arg_38_0.gameStartFlag:
		arg_38_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_38_0.settlementFlag:
			return

		arg_38_0.popUI.backPressed()

def var_0_0.OnSendMiniGameOPDone(arg_39_0, arg_39_1):
	return

def var_0_0.willExit(arg_40_0):
	if arg_40_0.handle:
		UpdateBeat.RemoveListener(arg_40_0.handle)

	if arg_40_0._tf and LeanTween.isTweening(go(arg_40_0._tf)):
		LeanTween.cancel(go(arg_40_0._tf))

	if arg_40_0.timer and arg_40_0.timer.running:
		arg_40_0.timer.Stop()

	Time.timeScale = 1
	arg_40_0.timer = None

return var_0_0
