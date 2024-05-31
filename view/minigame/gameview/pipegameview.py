local var_0_0 = class("PipeGameView", import("..BaseMiniGameView"))
local var_0_1 = import("view.miniGame.gameView.PipeGame.PipeGameVo")

def var_0_0.getUIName(arg_1_0):
	return var_0_1.game_ui

def var_0_0.getBGM(arg_2_0):
	return var_0_1.menu_bgm

def var_0_0.didEnter(arg_3_0):
	arg_3_0.initData()
	arg_3_0.initEvent()
	arg_3_0.initUI()

def var_0_0.initData(arg_4_0):
	var_0_1.Init(arg_4_0.GetMGData().id, arg_4_0.GetMGHubData().id)
	var_0_1.SetGameTpl(findTF(arg_4_0._tf, "tpl"))

	local var_4_0 = var_0_1.frameRate

	if var_4_0 > 60:
		var_4_0 = 60

	arg_4_0.timer = Timer.New(function()
		arg_4_0.onTimer(), 1 / var_4_0, -1)

def var_0_0.initEvent(arg_6_0):
	if not arg_6_0.handle and IsUnityEditor:
		arg_6_0.handle = UpdateBeat.CreateListener(arg_6_0.UpdateBeat, arg_6_0)

		UpdateBeat.AddListener(arg_6_0.handle)

	arg_6_0.bind(PipeGameEvent.LEVEL_GAME, function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_1:
			arg_6_0.resumeGame()
			arg_6_0.gameScene.setGameOver()
		else
			arg_6_0.resumeGame())
	arg_6_0.bind(PipeGameEvent.COUNT_DOWN, function(arg_8_0, arg_8_1, arg_8_2)
		arg_6_0.gameStart())
	arg_6_0.bind(PipeGameEvent.ON_HOME, function(arg_9_0, arg_9_1, arg_9_2)
		arg_6_0.emit(BaseUI.ON_HOME))
	arg_6_0.bind(PipeGameEvent.OPEN_PAUSE_UI, function(arg_10_0, arg_10_1, arg_10_2)
		arg_6_0.popUI.popPauseUI())
	arg_6_0.bind(PipeGameEvent.OPEN_LEVEL_UI, function(arg_11_0, arg_11_1, arg_11_2)
		arg_6_0.popUI.popLeaveUI())
	arg_6_0.bind(PipeGameEvent.PAUSE_GAME, function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_1:
			arg_6_0.pauseGame()
		else
			arg_6_0.resumeGame())
	arg_6_0.bind(PipeGameEvent.BACK_MENU, function(arg_13_0, arg_13_1, arg_13_2)
		arg_6_0.menuUI.update(arg_6_0.GetMGHubData())
		arg_6_0.menuUI.show(True)
		arg_6_0.gameUI.show(False)
		arg_6_0.gameScene.showContainer(False)
		arg_6_0.changeBgm(PipeGameConst.bgm_type_default))
	arg_6_0.bind(PipeGameEvent.CLOSE_GAME, function(arg_14_0, arg_14_1, arg_14_2)
		arg_6_0.closeView())
	arg_6_0.bind(PipeGameEvent.GAME_OVER, function(arg_15_0, arg_15_1, arg_15_2)
		arg_6_0.onGameOver())
	arg_6_0.bind(PipeGameEvent.SHOW_RULE, function(arg_16_0, arg_16_1, arg_16_2)
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[var_0_1.rule_tip].tip
		}))
	arg_6_0.bind(PipeGameEvent.SHOW_RANK, function(arg_17_0, arg_17_1, arg_17_2)
		arg_6_0.popUI.showRank(True))
	arg_6_0.bind(PipeGameEvent.READY_START, function(arg_18_0, arg_18_1, arg_18_2)
		arg_6_0.readyStart())
	arg_6_0.bind(PipeGameEvent.STORE_SERVER, function(arg_19_0, arg_19_1, arg_19_2)
		getProxy(MiniGameProxy).UpdataHighScore(var_0_1.game_id, arg_19_1))
	arg_6_0.bind(PipeGameEvent.SUBMIT_GAME_SUCCESS, function(arg_20_0, arg_20_1, arg_20_2)
		if not arg_6_0.sendSuccessFlag:
			arg_6_0.sendSuccessFlag = True

			arg_6_0.SendSuccess(0))
	arg_6_0.bind(PipeGameEvent.ADD_SCORE, function(arg_21_0, arg_21_1, arg_21_2)
		arg_6_0.addScore(arg_21_1.num)
		arg_6_0.gameUI.addScore(arg_21_1))

def var_0_0.initUI(arg_22_0):
	if IsUnityEditor:
		setActive(findTF(arg_22_0._tf, "tpl"), False)

	arg_22_0.clickMask = findTF(arg_22_0._tf, "clickMask")
	arg_22_0.popUI = PipeGamePopUI.New(arg_22_0._tf, arg_22_0)

	arg_22_0.popUI.clearUI()

	arg_22_0.gameUI = PipeGamingUI.New(arg_22_0._tf, arg_22_0)

	arg_22_0.gameUI.show(False)

	arg_22_0.menuUI = PipeGameMenuUI.New(arg_22_0._tf, arg_22_0)

	arg_22_0.menuUI.update(arg_22_0.GetMGHubData())
	arg_22_0.menuUI.show(True)

	arg_22_0.gameScene = PipeGameScene.New(arg_22_0._tf, arg_22_0)

def var_0_0.changeBgm(arg_23_0, arg_23_1):
	local var_23_0

	if arg_23_1 == PipeGameConst.bgm_type_default:
		var_23_0 = arg_23_0.getBGM()

		if not var_23_0:
			if pg.CriMgr.GetInstance().IsDefaultBGM():
				var_23_0 = pg.voice_bgm.NewMainScene.default_bgm
			else
				var_23_0 = pg.voice_bgm.NewMainScene.bgm
	elif arg_23_1 == PipeGameConst.bgm_type_menu:
		var_23_0 = var_0_1.menu_bgm
	elif arg_23_1 == PipeGameConst.bgm_type_game:
		var_23_0 = var_0_1.game_bgm

	if arg_23_0.bgm != var_23_0:
		arg_23_0.bgm = var_23_0

		pg.BgmMgr.GetInstance().Push(arg_23_0.__cname, var_23_0)

def var_0_0.UpdateBeat(arg_24_0):
	if arg_24_0.gameStop or arg_24_0.settlementFlag:
		return

def var_0_0.readyStart(arg_25_0):
	arg_25_0.readyStartFlag = True

	var_0_1.Prepare()
	arg_25_0.popUI.readyStart()
	arg_25_0.menuUI.show(False)
	arg_25_0.gameUI.show(False)

def var_0_0.gameStart(arg_26_0):
	arg_26_0.readyStartFlag = False
	arg_26_0.gameStartFlag = True
	arg_26_0.sendSuccessFlag = False

	arg_26_0.popUI.popCountUI(False)
	arg_26_0.gameUI.start()
	arg_26_0.gameUI.show(True)
	arg_26_0.gameScene.start()
	arg_26_0.timerStart()
	arg_26_0.changeBgm(PipeGameConst.bgm_type_game)

def var_0_0.changeSpeed(arg_27_0, arg_27_1):
	return

def var_0_0.onTimer(arg_28_0):
	arg_28_0.gameStep()

def var_0_0.gameStep(arg_29_0):
	arg_29_0.stepRunTimeData()
	arg_29_0.gameScene.step(var_0_1.deltaTime)
	arg_29_0.gameUI.step(var_0_1.deltaTime)

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

	var_0_1.gameTime = var_0_1.gameTime - var_33_0

	if not var_0_1.startSettlement:
		var_0_1.gameDragTime = var_0_1.gameDragTime - var_33_0

		if var_0_1.gameDragTime < 0:
			var_0_1.gameDragTime = 0

	var_0_1.gameStepTime = var_0_1.gameStepTime + var_33_0
	var_0_1.deltaTime = var_33_0

def var_0_0.addScore(arg_34_0, arg_34_1):
	var_0_1.scoreNum = var_0_1.scoreNum + arg_34_1

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
		return
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

	var_0_1.Clear()

return var_0_0
