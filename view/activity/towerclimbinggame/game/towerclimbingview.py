local var_0_0 = class("TowerClimbingView")

local function var_0_1(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = GetOrAddComponent(arg_1_0, "EventTriggerListener")

	var_1_0.AddPointDownFunc(function(arg_2_0, arg_2_1)
		if arg_1_1:
			arg_1_1())
	var_1_0.AddPointUpFunc(function(arg_3_0, arg_3_1)
		if arg_1_2:
			arg_1_2())

local function var_0_2(arg_4_0)
	local var_4_0 = GetOrAddComponent(arg_4_0, "EventTriggerListener")

	var_4_0.RemovePointDownFunc()
	var_4_0.RemovePointUpFunc()

def var_0_0.Ctor(arg_5_0, arg_5_1):
	pg.DelegateInfo.New(arg_5_0)

	arg_5_0.controller = arg_5_1

def var_0_0.SetUI(arg_6_0, arg_6_1):
	arg_6_0._go = arg_6_1
	arg_6_0._tf = arg_6_1.transform
	arg_6_0.overView = findTF(arg_6_0._tf, "overview")
	arg_6_0.gameView = findTF(arg_6_0._tf, "AD")
	arg_6_0.maps = {
		findTF(arg_6_0._tf, "overview/maps/1"),
		findTF(arg_6_0._tf, "overview/maps/2"),
		findTF(arg_6_0._tf, "overview/maps/3")
	}
	arg_6_0.exitGameBtn = findTF(arg_6_0.gameView, "back")
	arg_6_0.jumpBtn = findTF(arg_6_0.gameView, "prints/right_btn_layout/up")
	arg_6_0.leftLayout = findTF(arg_6_0.gameView, "prints/left_btn_layout")
	arg_6_0.moveBtn = findTF(arg_6_0.leftLayout, "move_btn")
	arg_6_0.quitPanel = findTF(arg_6_0._tf, "quit_panel")
	arg_6_0.quitPanelCancelBtn = arg_6_0.quitPanel.Find("frame/cancel")
	arg_6_0.quitPanelCconfirmBtn = arg_6_0.quitPanel.Find("frame/confirm")
	arg_6_0.resultPanel = findTF(arg_6_0._tf, "result_panel")
	arg_6_0.resultPanelScoreTxt = arg_6_0.resultPanel.Find("frame/curr/Text").GetComponent(typeof(Text))
	arg_6_0.resultPanelHScoreTxt = arg_6_0.resultPanel.Find("frame/higtest/Text").GetComponent(typeof(Text))
	arg_6_0.resultPanelEndBtn = arg_6_0.resultPanel.Find("frame/cancel")
	arg_6_0.helpBtn = arg_6_0._tf.Find("overview/logo/help")
	arg_6_0.enterPanel = arg_6_0._tf.Find("enter_panel")
	arg_6_0.enterPanelTxt = arg_6_0.enterPanel.Find("Text").GetComponent(typeof(Text))

	arg_6_0.ResetParams()

def var_0_0.OnEnter(arg_7_0, arg_7_1):
	setActive(arg_7_0.overView, True)
	setActive(arg_7_0.gameView, False)
	onButton(arg_7_0, arg_7_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.towerclimbing_gametip.tip
		}), SFX_PANEL)
	onButton(arg_7_0, arg_7_0.exitGameBtn, function()
		arg_7_0.ShowQuitPanel(), SFX_PANEL)

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.maps):
		onButton(arg_7_0, iter_7_1, function()
			arg_7_0.controller.StartGame(iter_7_0), SFX_PANEL)

def var_0_0.DoEnter(arg_11_0, arg_11_1):
	setActive(arg_11_0.overView, False)
	setActive(arg_11_0.gameView, True)

	arg_11_0.inDownCnt = True

	arg_11_0.ActivePanel(arg_11_0.enterPanel, True)

	local var_11_0 = 4

	arg_11_0.timer = Timer.New(function()
		var_11_0 = var_11_0 - 1

		if var_11_0 == 3:
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_STEP_PILE_COUNTDOWN)

		arg_11_0.enterPanelTxt.text = var_11_0

		if var_11_0 == 0:
			arg_11_1()
			arg_11_0.ActivePanel(arg_11_0.enterPanel, False)
			arg_11_0.timer.Stop()

			arg_11_0.timer = None
			arg_11_0.inDownCnt = None, 1, -1)

	arg_11_0.timer.Start()
	arg_11_0.timer.func()

def var_0_0.OnStartGame(arg_13_0):
	var_0_1(arg_13_0.jumpBtn, function()
		arg_13_0.controller.PlayerJump()
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL))
	arg_13_0.OnSlip(arg_13_0.moveBtn, function()
		arg_13_0.rightOffse = 0.06
		arg_13_0.leftOffse = 0, function()
		arg_13_0.rightOffse = 0
		arg_13_0.leftOffse = -0.06, function()
		arg_13_0.rightOffse = 0
		arg_13_0.leftOffse = 0, function()
		arg_13_0.rightOffse = 0
		arg_13_0.leftOffse = 0)

def var_0_0.OnSlip(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4, arg_19_5):
	local var_19_0 = GetOrAddComponent(arg_19_1, "EventTriggerListener")
	local var_19_1 = GameObject.Find("UICamera").GetComponent("Camera").WorldToScreenPoint(arg_19_0.leftLayout.position)
	local var_19_2 = 0
	local var_19_3 = 10

	local function var_19_4(arg_20_0, arg_20_1)
		var_19_2 = arg_20_1.position.x - var_19_1.x

		if var_19_2 < -var_19_3:
			if arg_19_3:
				arg_19_3()
		elif var_19_2 > var_19_3:
			if arg_19_2:
				arg_19_2()
		elif arg_19_5:
			arg_19_5()

	var_19_0.AddPointDownFunc(function(arg_21_0, arg_21_1)
		var_19_2 = 0

		var_19_4(arg_21_0, arg_21_1))
	var_19_0.AddDragFunc(var_19_4)
	var_19_0.AddPointUpFunc(function(arg_22_0, arg_22_1)
		var_19_2 = 0

		if arg_19_4:
			arg_19_4())

def var_0_0.ClearSlip(arg_23_0, arg_23_1):
	local var_23_0 = GetOrAddComponent(arg_23_1, "EventTriggerListener")

	var_23_0.RemovePointDownFunc()
	var_23_0.RemovePointUpFunc()
	var_23_0.RemoveDragFunc()

def var_0_0.Update(arg_24_0):
	arg_24_0.AddDebugInput()

	arg_24_0.hrzOffse = arg_24_0.leftOffse + arg_24_0.rightOffse

	arg_24_0.controller.OnStickChange(arg_24_0.hrzOffse)

def var_0_0.AddDebugInput(arg_25_0):
	if IsUnityEditor:
		if Input.GetKeyDown(KeyCode.A):
			arg_25_0.leftOffse = -0.06

		if Input.GetKeyUp(KeyCode.A):
			arg_25_0.leftOffse = 0

		if Input.GetKeyDown(KeyCode.D):
			arg_25_0.rightOffse = 0.06

		if Input.GetKeyUp(KeyCode.D):
			arg_25_0.rightOffse = 0

		if Input.GetKeyDown(KeyCode.Space):
			arg_25_0.controller.PlayerJump()
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL)

def var_0_0.OnCreateMap(arg_26_0, arg_26_1, arg_26_2):
	arg_26_0.map = TowerClimbingMap.New(arg_26_0, arg_26_1)

	arg_26_0.map.Init(arg_26_2)

def var_0_0.ResetParams(arg_27_0):
	arg_27_0.leftOffse = 0
	arg_27_0.rightOffse = 0
	arg_27_0.hrzOffse = 0

def var_0_0.OnEndGame(arg_28_0, arg_28_1, arg_28_2, arg_28_3):
	arg_28_0.ResetParams()
	removeOnButton(arg_28_0.jumpBtn)
	arg_28_0.ShowResultPanel(arg_28_1, arg_28_2, arg_28_3)

def var_0_0.OnExitGame(arg_29_0):
	setActive(arg_29_0.overView, True)
	setActive(arg_29_0.gameView, False)

	if arg_29_0.map:
		arg_29_0.map.Dispose()

def var_0_0.ShowQuitPanel(arg_30_0):
	arg_30_0.ActivePanel(arg_30_0.quitPanel, True)
	onButton(arg_30_0, arg_30_0.quitPanelCconfirmBtn, function()
		arg_30_0.ActivePanel(arg_30_0.quitPanel, False)
		arg_30_0.controller.EndGame(), SFX_PANEL)
	onButton(arg_30_0, arg_30_0.quitPanelCancelBtn, function()
		arg_30_0.ActivePanel(arg_30_0.quitPanel, False), SFX_PANEL)

def var_0_0.ShowResultPanel(arg_33_0, arg_33_1, arg_33_2, arg_33_3):
	arg_33_0.ActivePanel(arg_33_0.resultPanel, True)

	arg_33_0.resultPanelScoreTxt.text = arg_33_1

	if arg_33_0.highScores and arg_33_3 <= #arg_33_0.highScores:
		arg_33_0.resultPanelHScoreTxt.text = arg_33_0.highScores[arg_33_3]
	else
		arg_33_0.resultPanelHScoreTxt.text = arg_33_2

	onButton(arg_33_0, arg_33_0.resultPanelEndBtn, function()
		arg_33_0.ActivePanel(arg_33_0.resultPanel, False)
		arg_33_0.controller.ExitGame(), SFX_PANEL)

def var_0_0.SetHighScore(arg_35_0, arg_35_1):
	arg_35_0.highScores = arg_35_1

def var_0_0.ActivePanel(arg_36_0, arg_36_1, arg_36_2):
	if arg_36_2:
		pg.UIMgr.GetInstance().BlurPanel(arg_36_1)
	else
		pg.UIMgr.GetInstance().UnblurPanel(arg_36_1, arg_36_0._tf)

	setActive(arg_36_1, arg_36_2)

def var_0_0.onBackPressed(arg_37_0):
	if arg_37_0.inDownCnt:
		return True

	if arg_37_0.controller.IsStarting:
		arg_37_0.ShowQuitPanel()

		return True

	if isActive(arg_37_0.resultPanel):
		arg_37_0.ActivePanel(arg_37_0.resultPanel, False)
		arg_37_0.controller.ExitGame()

		return True

	return False

def var_0_0.Dispose(arg_38_0):
	if arg_38_0.timer:
		arg_38_0.timer.Stop()

		arg_38_0.timer = None

	var_0_2(arg_38_0.jumpBtn)
	arg_38_0.ClearSlip(arg_38_0.moveBtn)
	pg.DelegateInfo.Dispose(arg_38_0)

	if arg_38_0.map:
		arg_38_0.map.Dispose()

return var_0_0
