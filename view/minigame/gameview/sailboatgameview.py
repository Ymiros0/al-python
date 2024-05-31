local var_0_0 = class("SailBoatGameView", import("..BaseMiniGameView"))

var_0_0.LEVEL_GAME = "leavel game"
var_0_0.PAUSE_GAME = "pause game "
var_0_0.OPEN_PAUSE_UI = "open pause ui"
var_0_0.OPEN_LEVEL_UI = "open leave ui"
var_0_0.BACK_MENU = "back menu"
var_0_0.OPEN_EQUIP_UI = "open equip ui"
var_0_0.CLOSE_GAME = "close game"
var_0_0.SHOW_RULE = "show rule"
var_0_0.READY_START = "ready start"
var_0_0.COUNT_DOWN = "count:wn"
var_0_0.STORE_SERVER = "store server"
var_0_0.SUBMIT_GAME_SUCCESS = "submit game success"
var_0_0.ADD_SCORE = "add score"
var_0_0.GAME_OVER = "game over"
var_0_0.USE_SKILL = "use skill"
var_0_0.JOYSTICK_ACTIVE_CHANGE = "joy stick active change"

local var_0_1 = import("view.miniGame.gameView.SailBoatGame.SailBoatGameVo")

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
		arg_6_0.handle = UpdateBeat.CreateListener(arg_6_0.Update, arg_6_0)

		UpdateBeat.AddListener(arg_6_0.handle)

	arg_6_0.bind(var_0_0.LEVEL_GAME, function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_1:
			arg_6_0.resumeGame()
			arg_6_0.onGameOver()
		else
			arg_6_0.resumeGame())
	arg_6_0.bind(var_0_0.USE_SKILL, function(arg_8_0, arg_8_1, arg_8_2)
		arg_6_0.gameScene.useSkill())
	arg_6_0.bind(var_0_0.COUNT_DOWN, function(arg_9_0, arg_9_1, arg_9_2)
		arg_6_0.gameStart())
	arg_6_0.bind(var_0_0.OPEN_EQUIP_UI, function(arg_10_0, arg_10_1, arg_10_2)
		arg_6_0.equipUI.show(True)
		arg_6_0.menuUI.show(False))
	arg_6_0.bind(var_0_0.OPEN_PAUSE_UI, function(arg_11_0, arg_11_1, arg_11_2)
		arg_6_0.popUI.popPauseUI())
	arg_6_0.bind(var_0_0.OPEN_LEVEL_UI, function(arg_12_0, arg_12_1, arg_12_2)
		arg_6_0.popUI.popLeaveUI())
	arg_6_0.bind(var_0_0.PAUSE_GAME, function(arg_13_0, arg_13_1, arg_13_2)
		if arg_13_1:
			arg_6_0.pauseGame()
		else
			arg_6_0.resumeGame())
	arg_6_0.bind(var_0_0.BACK_MENU, function(arg_14_0, arg_14_1, arg_14_2)
		arg_6_0.menuUI.update(arg_6_0.GetMGHubData())
		arg_6_0.menuUI.show(True)
		arg_6_0.gameUI.show(False)
		arg_6_0.gameScene.showContainer(False)

		local var_14_0 = arg_6_0.getBGM()

		if not var_14_0:
			if pg.CriMgr.GetInstance().IsDefaultBGM():
				var_14_0 = pg.voice_bgm.NewMainScene.default_bgm
			else
				var_14_0 = pg.voice_bgm.NewMainScene.bgm

		if arg_6_0.bgm != var_14_0:
			arg_6_0.bgm = var_14_0

			pg.BgmMgr.GetInstance().Push(arg_6_0.__cname, var_14_0)

		arg_6_0.initBgAnimation())
	arg_6_0.bind(var_0_0.CLOSE_GAME, function(arg_15_0, arg_15_1, arg_15_2)
		arg_6_0.closeView())
	arg_6_0.bind(var_0_0.GAME_OVER, function(arg_16_0, arg_16_1, arg_16_2)
		arg_6_0.onGameOver())
	arg_6_0.bind(var_0_0.SHOW_RULE, function(arg_17_0, arg_17_1, arg_17_2)
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[var_0_1.rule_tip].tip
		}))
	arg_6_0.bind(var_0_0.READY_START, function(arg_18_0, arg_18_1, arg_18_2)
		arg_6_0.readyStart())
	arg_6_0.bind(var_0_0.STORE_SERVER, function(arg_19_0, arg_19_1, arg_19_2)
		arg_6_0.StoreDataToServer({
			arg_19_1
		}))
	arg_6_0.bind(var_0_0.SUBMIT_GAME_SUCCESS, function(arg_20_0, arg_20_1, arg_20_2)
		if not arg_6_0.sendSuccessFlag:
			arg_6_0.sendSuccessFlag = True

			arg_6_0.SendSuccess(0))
	arg_6_0.bind(var_0_0.ADD_SCORE, function(arg_21_0, arg_21_1, arg_21_2)
		arg_6_0.addScore(arg_21_1.num)
		arg_6_0.gameUI.addScore(arg_21_1))
	arg_6_0.bind(var_0_0.JOYSTICK_ACTIVE_CHANGE, function(arg_22_0, arg_22_1, arg_22_2)
		if arg_6_0.gameStartFlag:
			arg_6_0.gameScene.joystickActive(arg_22_1))

def var_0_0.initUI(arg_23_0):
	if IsUnityEditor:
		setActive(findTF(arg_23_0._tf, "tpl"), False)

	arg_23_0.clickMask = findTF(arg_23_0._tf, "clickMask")
	arg_23_0.popUI = SailBoatGamePopUI.New(arg_23_0._tf, arg_23_0)

	arg_23_0.popUI.clearUI()

	arg_23_0.gameUI = SailBoatGamingUI.New(arg_23_0._tf, arg_23_0)

	arg_23_0.gameUI.show(False)

	arg_23_0.menuUI = SailBoatGameMenuUI.New(arg_23_0._tf, arg_23_0)

	arg_23_0.menuUI.update(arg_23_0.GetMGHubData())
	arg_23_0.menuUI.show(True)

	arg_23_0.equipUI = SailBoatEquipUI.New(arg_23_0._tf, arg_23_0)

	arg_23_0.equipUI.show(False)

	arg_23_0.gameScene = SailBoatGameScene.New(arg_23_0._tf, arg_23_0)

	arg_23_0.initBgAnimation()

def var_0_0.initBgAnimation(arg_24_0):
	local var_24_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.BOAT_QIAN_SHAO_ZHAN)
	local var_24_1 = getProxy(TaskProxy)
	local var_24_2 = {
		"Phase_00",
		"Phase_01",
		"Phase_02",
		"Phase_03",
		"Phase_04",
		"Phase_05",
		"Phase_06",
		"Phase_07"
	}
	local var_24_3 = var_24_0.getConfig("config_data")
	local var_24_4 = var_24_0.data3

	if var_24_1.getFinishTaskById(var_24_3[var_24_4][1]) != None and var_24_1.getFinishTaskById(var_24_3[var_24_4][2]) != None:
		var_24_4 = var_24_4 + 1

	GetComponent(findTF(arg_24_0._tf, "sceneBg/1"), typeof(Animator)).Play(var_24_2[var_24_4])

def var_0_0.Update(arg_25_0):
	if arg_25_0.gameStop or arg_25_0.settlementFlag:
		return

	if IsUnityEditor:
		if Input.GetKeyDown(KeyCode.S):
			arg_25_0.gameUI.press(KeyCode.S, True)

		if Input.GetKeyUp(KeyCode.S):
			arg_25_0.gameUI.press(KeyCode.S, False)

		if Input.GetKeyDown(KeyCode.W):
			arg_25_0.gameUI.press(KeyCode.W, True)

		if Input.GetKeyUp(KeyCode.W):
			arg_25_0.gameUI.press(KeyCode.W, False)

		if Input.GetKeyDown(KeyCode.A):
			arg_25_0.gameUI.press(KeyCode.A, True)

		if Input.GetKeyUp(KeyCode.A):
			arg_25_0.gameUI.press(KeyCode.A, False)

		if Input.GetKeyDown(KeyCode.D):
			arg_25_0.gameUI.press(KeyCode.D, True)

		if Input.GetKeyUp(KeyCode.D):
			arg_25_0.gameUI.press(KeyCode.D, False)

		if Input.GetKeyDown(KeyCode.J):
			arg_25_0.gameScene.press(KeyCode.J, True)

def var_0_0.readyStart(arg_26_0):
	arg_26_0.readyStartFlag = True

	var_0_1.Prepare()
	arg_26_0.popUI.readyStart()
	arg_26_0.menuUI.show(False)
	arg_26_0.gameUI.show(False)
	arg_26_0.equipUI.show(False)
	setActive(findTF(arg_26_0._tf, "sceneBg"), False)

def var_0_0.gameStart(arg_27_0):
	arg_27_0.readyStartFlag = False
	arg_27_0.gameStartFlag = True
	arg_27_0.sendSuccessFlag = False

	arg_27_0.popUI.popCountUI(False)
	arg_27_0.gameUI.start()
	arg_27_0.gameUI.show(True)

	if arg_27_0.bgm != var_0_1.game_bgm:
		arg_27_0.bgm = var_0_1.game_bgm

		pg.BgmMgr.GetInstance().Push(arg_27_0.__cname, var_0_1.game_bgm)

	arg_27_0.gameScene.start()
	arg_27_0.timerStart()

def var_0_0.changeSpeed(arg_28_0, arg_28_1):
	return

def var_0_0.onTimer(arg_29_0):
	arg_29_0.gameStep()

def var_0_0.gameStep(arg_30_0):
	arg_30_0.stepRunTimeData()
	arg_30_0.gameScene.step(var_0_1.deltaTime)
	arg_30_0.gameUI.step(var_0_1.deltaTime)

	if var_0_1.gameTime <= 0:
		arg_30_0.onGameOver()

def var_0_0.timerStart(arg_31_0):
	if not arg_31_0.timer.running:
		arg_31_0.timer.Start()

def var_0_0.timerResume(arg_32_0):
	if not arg_32_0.timer.running:
		arg_32_0.timer.Start()

	arg_32_0.gameScene.resume()

def var_0_0.timerStop(arg_33_0):
	if arg_33_0.timer.running:
		arg_33_0.timer.Stop()

	arg_33_0.gameScene.stop()

def var_0_0.stepRunTimeData(arg_34_0):
	local var_34_0 = Time.deltaTime

	if var_34_0 > 0.016:
		var_34_0 = 0.016

	var_0_1.gameTime = var_0_1.gameTime - var_34_0
	var_0_1.gameStepTime = var_0_1.gameStepTime + var_34_0
	var_0_1.deltaTime = var_34_0

	local var_34_1 = var_0_1.GetSceneSpeed()

	var_34_1.x = var_0_1.moveAmount.x * var_34_0
	var_34_1.y = var_0_1.moveAmount.y * var_34_0

	var_0_1.SetSceneSpeed(var_34_1)

def var_0_0.addScore(arg_35_0, arg_35_1):
	var_0_1.scoreNum = var_0_1.scoreNum + arg_35_1

def var_0_0.onGameOver(arg_36_0):
	if arg_36_0.settlementFlag:
		return

	arg_36_0.timerStop()
	arg_36_0.clearController()

	arg_36_0.settlementFlag = True

	setActive(arg_36_0.clickMask, True)
	LeanTween.delayedCall(go(arg_36_0._tf), 0.1, System.Action(function()
		arg_36_0.settlementFlag = False
		arg_36_0.gameStartFlag = False

		setActive(arg_36_0.clickMask, False)
		arg_36_0.popUI.updateSettlementUI()
		arg_36_0.popUI.popSettlementUI(True)))
	setActive(findTF(arg_36_0._tf, "sceneBg"), True)

def var_0_0.OnApplicationPaused(arg_38_0):
	if not arg_38_0.gameStartFlag:
		return

	if arg_38_0.readyStartFlag:
		return

	if arg_38_0.settlementFlag:
		return

	arg_38_0.pauseGame()
	arg_38_0.popUI.popPauseUI()

def var_0_0.clearController(arg_39_0):
	arg_39_0.gameScene.clear()

def var_0_0.pauseGame(arg_40_0):
	arg_40_0.gameStop = True

	arg_40_0.changeSpeed(0)
	arg_40_0.timerStop()

def var_0_0.resumeGame(arg_41_0):
	arg_41_0.gameStop = False

	arg_41_0.changeSpeed(1)
	arg_41_0.timerStart()

def var_0_0.onBackPressed(arg_42_0):
	if arg_42_0.readyStartFlag:
		return

	if not arg_42_0.gameStartFlag:
		arg_42_0.emit(var_0_0.ON_BACK_PRESSED)

		return
	else
		if arg_42_0.settlementFlag:
			return

		arg_42_0.popUI.backPressed()

def var_0_0.OnSendMiniGameOPDone(arg_43_0, arg_43_1):
	return

def var_0_0.willExit(arg_44_0):
	if arg_44_0.handle:
		UpdateBeat.RemoveListener(arg_44_0.handle)

	if arg_44_0._tf and LeanTween.isTweening(go(arg_44_0._tf)):
		LeanTween.cancel(go(arg_44_0._tf))

	if arg_44_0.timer and arg_44_0.timer.running:
		arg_44_0.timer.Stop()

	Time.timeScale = 1
	arg_44_0.timer = None

	var_0_1.Clear()

return var_0_0
