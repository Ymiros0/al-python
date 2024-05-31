local var_0_0 = class("GameRoomMatch3View", import("..BaseMiniGameView"))
local var_0_1 = 6
local var_0_2 = 7
local var_0_3 = -405
local var_0_4 = -275
local var_0_5 = 135
local var_0_6 = 110
local var_0_7 = False
local var_0_8 = 0.1
local var_0_9 = 0
local var_0_10 = 0.3
local var_0_11 = 0.5
local var_0_12 = 100
local var_0_13 = 0.2
local var_0_14 = 0.4
local var_0_15 = 180
local var_0_16 = 60
local var_0_17 = 3
local var_0_18 = 2
local var_0_19 = 0.3
local var_0_20 = 0.3
local var_0_21 = 2.5
local var_0_22 = "event./ui/ddldaoshu2"
local var_0_23 = "event./ui/boat_drag"
local var_0_24 = "event./ui/break_out_full"
local var_0_25 = "event./ui/sx-good"
local var_0_26 = "event./ui/sx-perfect"
local var_0_27 = "event./ui/sx-jishu"
local var_0_28 = "event./ui/furniTrue_save"

def var_0_0.getUIName(arg_1_0):
	return "GameRoomMatch3UI"

def var_0_0.getBGM(arg_2_0):
	return "backyard"

def var_0_0.init(arg_3_0):
	arg_3_0.matchEffect = arg_3_0.findTF("effects/sanxiaoxiaoshi")
	arg_3_0.goodEffect = arg_3_0.findTF("effects/sanxiaoGood")
	arg_3_0.greatEffect = arg_3_0.findTF("effects/sanxiaoGreat")
	arg_3_0.perfectEffect = arg_3_0.findTF("effects/sanxiaoPerfect")
	arg_3_0.hintEffect = arg_3_0.findTF("effects/hint")
	arg_3_0.selectedEffect = arg_3_0.findTF("effects/selected")
	arg_3_0.whitenMat = arg_3_0.findTF("effects/whiten").GetComponent("Image").material
	arg_3_0.backBtn = arg_3_0.findTF("button/back")
	arg_3_0.mainPage = arg_3_0.findTF("main")
	arg_3_0.startBtn = arg_3_0.findTF("main/start")
	arg_3_0.helpBtn = arg_3_0.findTF("main/rule")
	arg_3_0.countdownPage = arg_3_0.findTF("countdown")
	arg_3_0.countdownAnim = arg_3_0.findTF("countdown")
	arg_3_0.gamePage = arg_3_0.findTF("game")
	arg_3_0.gameMask = arg_3_0.findTF("game/mask")
	arg_3_0.warning = arg_3_0.findTF("game/warning")
	arg_3_0.countdownTf = arg_3_0.findTF("game/countdown")
	arg_3_0.countdownText = arg_3_0.findTF("game/countdown/Text")
	arg_3_0.inf = arg_3_0.findTF("game/countdown/inf")
	arg_3_0.scoreText = arg_3_0.findTF("game/score/Text")
	arg_3_0.floatText = arg_3_0.findTF("game/floatText")
	arg_3_0.floatChar = {}
	arg_3_0.pausePage = arg_3_0.findTF("game/pause")
	arg_3_0.pauseYes = arg_3_0.findTF("game/pause/yes")
	arg_3_0.pauseNo = arg_3_0.findTF("game/pause/no")

	for iter_3_0 = 0, 9:
		arg_3_0.floatChar[iter_3_0] = arg_3_0.findTF("game/floatText/" .. iter_3_0)

	arg_3_0.tilesRoot = arg_3_0.findTF("game/tiles")
	arg_3_0.gameListener = arg_3_0.tilesRoot.GetComponent("EventTriggerListener")
	arg_3_0.longPressListener = arg_3_0.tilesRoot.GetComponent("UILongPressTrigger")
	arg_3_0.endPage = arg_3_0.findTF("end")
	arg_3_0.endBtn = arg_3_0.findTF("end/end_btn")
	arg_3_0.endScore = arg_3_0.findTF("end/score/Text")
	arg_3_0.newSign = arg_3_0.findTF("end/score/Text/new")
	arg_3_0.bestScore = arg_3_0.findTF("end/highest/Text")
	arg_3_0.tiles = {
		arg_3_0.findTF("tiles/Akashi"),
		arg_3_0.findTF("tiles/Ayanami"),
		arg_3_0.findTF("tiles/Javelin"),
		arg_3_0.findTF("tiles/Laffey"),
		arg_3_0.findTF("tiles/Z23")
	}

def var_0_0.onBackPressed(arg_4_0):
	if isActive(arg_4_0.mainPage):
		arg_4_0.emit(var_0_0.ON_BACK)
	elif isActive(arg_4_0.pausePage):
		triggerButton(arg_4_0.pauseNo)
	elif isActive(arg_4_0.gamePage):
		arg_4_0.pause()
	elif isActive(arg_4_0.endPage) and arg_4_0.endBtn.GetComponent("Button").enabled:
		triggerButton(arg_4_0.endBtn)

def var_0_0.didEnter(arg_5_0):
	onButton(arg_5_0, arg_5_0.backBtn, function()
		arg_5_0.onBackPressed(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.startBtn, function()
		arg_5_0.openCoinLayer(False)

		if var_0_7:
			setActive(arg_5_0.mainPage, False)
			setActive(arg_5_0.gamePage, True)
			arg_5_0.startGame()
		else
			arg_5_0.mainPage.GetComponent("CanvasGroup").blocksRaycasts = False

			arg_5_0.managedTween(LeanTween.value, function()
				arg_5_0.mainPage.GetComponent("CanvasGroup").alpha = 1
				arg_5_0.mainPage.GetComponent("CanvasGroup").blocksRaycasts = True

				setActive(arg_5_0.mainPage, False)
				setActive(arg_5_0.countdownPage, True)
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_22), go(arg_5_0.mainPage), 1, 0, var_0_20).setOnUpdate(System.Action_float(function(arg_9_0)
				arg_5_0.mainPage.GetComponent("CanvasGroup").alpha = arg_9_0)))

	if arg_5_0.getGameRoomData():
		arg_5_0.gameHelpTip = arg_5_0.getGameRoomData().game_help

	onButton(arg_5_0, arg_5_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = arg_5_0.gameHelpTip
		}), SFX_PANEL)
	arg_5_0.countdownAnim.GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_11_0)
		setActive(arg_5_0.countdownPage, False)
		setActive(arg_5_0.gamePage, True)
		arg_5_0.startGame())
	onButton(arg_5_0, arg_5_0.endBtn, function()
		arg_5_0.mainPage.GetComponent("CanvasGroup").blocksRaycasts = False

		arg_5_0.managedTween(LeanTween.value, function()
			arg_5_0.mainPage.GetComponent("CanvasGroup").alpha = 1
			arg_5_0.mainPage.GetComponent("CanvasGroup").blocksRaycasts = True, go(arg_5_0.endPage), 0, 1, var_0_20).setOnUpdate(System.Action_float(function(arg_14_0)
			arg_5_0.mainPage.GetComponent("CanvasGroup").alpha = arg_14_0))
		setActive(arg_5_0.mainPage, True)
		setActive(arg_5_0.countdownPage, False)
		setActive(arg_5_0.gamePage, False)
		setActive(arg_5_0.endPage, False)
		arg_5_0.openCoinLayer(True))
	onButton(arg_5_0, arg_5_0.pauseYes, function()
		arg_5_0.stopGame())
	onButton(arg_5_0, arg_5_0.pauseNo, function()
		setActive(arg_5_0.pausePage, False)
		arg_5_0.resumeGame())

	local var_5_0 = False

	arg_5_0.gameListener.AddPointClickFunc(function(arg_17_0, arg_17_1)
		if var_5_0:
			var_5_0 = False

			return

		if arg_5_0.updating:
			return

		if not arg_5_0.inGame:
			return

		local var_17_0 = LuaHelper.ScreenToLocal(arg_5_0.tilesRoot, arg_17_1.position, GameObject.Find("UICamera").GetComponent(typeof(Camera)))
		local var_17_1, var_17_2 = arg_5_0.pos2index(var_17_0)

		if arg_5_0.selected:
			if arg_5_0.selected == arg_5_0.tileTfs[var_17_1][var_17_2]:
				arg_5_0.unselect()
			elif math.abs(var_17_1 - arg_5_0.selectedIndex.i) + math.abs(var_17_2 - arg_5_0.selectedIndex.j) == 1:
				arg_5_0.tryMoveTo({
					i = var_17_1,
					j = var_17_2
				})
			else
				arg_5_0.select(var_17_1, var_17_2)
		else
			arg_5_0.select(var_17_1, var_17_2))
	arg_5_0.longPressListener.onLongPressed.AddListener(function()
		if arg_5_0.updating:
			return

		if not arg_5_0.inGame:
			return

		local var_18_0 = LuaHelper.ScreenToLocal(arg_5_0.tilesRoot, Input.mousePosition, GameObject.Find("UICamera").GetComponent(typeof(Camera)))
		local var_18_1, var_18_2 = arg_5_0.pos2index(var_18_0)

		arg_5_0.unselect()
		arg_5_0.animate(var_18_1, var_18_2, True))
	arg_5_0.gameListener.AddBeginDragFunc(function(arg_19_0, arg_19_1)
		if arg_5_0.updating:
			return

		if not arg_5_0.inGame:
			return

		var_5_0 = True

		local var_19_0 = arg_19_1.delta
		local var_19_1 = LuaHelper.ScreenToLocal(arg_5_0.tilesRoot, arg_19_1.position, GameObject.Find("UICamera").GetComponent(typeof(Camera)))
		local var_19_2, var_19_3 = arg_5_0.pos2index(var_19_1)

		arg_5_0.animate(var_19_2, var_19_3, False)
		arg_5_0.unselect()

		arg_5_0.selected = arg_5_0.tileTfs[var_19_2][var_19_3]
		arg_5_0.selectedIndex = {
			i = var_19_2,
			j = var_19_3
		}

		if math.abs(var_19_0.x) > math.abs(var_19_0.y):
			var_19_2 = 0
			var_19_3 = var_19_0.x > 0 and 1 or -1
		else
			var_19_2 = var_19_0.y > 0 and 1 or -1
			var_19_3 = 0

		arg_5_0.tryMoveTo({
			i = arg_5_0.selectedIndex.i + var_19_2,
			j = arg_5_0.selectedIndex.j + var_19_3
		}))
	setActive(arg_5_0.mainPage, True)
	arg_5_0.updateData()

def var_0_0.updateData(arg_20_0):
	arg_20_0.infinite = arg_20_0.GetMGHubData().count == 0

	local var_20_0 = arg_20_0.GetMGData().GetRuntimeData("elements")

	arg_20_0.best = var_20_0 and var_20_0[1] or 0

def var_0_0.index2pos(arg_21_0, arg_21_1, arg_21_2):
	return Vector3.New(var_0_3 + (arg_21_2 - 1) * var_0_5, var_0_4 + (arg_21_1 - 1) * var_0_6)

def var_0_0.pos2index(arg_22_0, arg_22_1):
	local var_22_0 = var_0_3 - var_0_5 / 2
	local var_22_1 = var_0_4 - var_0_6 / 2

	return math.ceil((arg_22_1.y - var_22_1) / var_0_6), math.ceil((arg_22_1.x - var_22_0) / var_0_5)

def var_0_0.dropTime(arg_23_0):
	return math.max(arg_23_0 * var_0_8, var_0_9)

def var_0_0.cancelHint(arg_24_0):
	if arg_24_0.hint:
		Destroy(arg_24_0.hint)
		arg_24_0.hint1.GetComponent("Animator").SetBool("selected", False)
		arg_24_0.hint2.GetComponent("Animator").SetBool("selected", False)

		arg_24_0.hint = None
		arg_24_0.hint1 = None
		arg_24_0.hint2 = None

local var_0_29 = {
	{
		0,
		1
	},
	{
		0,
		-1
	},
	{
		-1,
		0
	},
	{
		1,
		0
	}
}

def var_0_0.unselect(arg_25_0):
	if arg_25_0.selectedEffectTf:
		Destroy(arg_25_0.selectedEffectTf)

		arg_25_0.selectedEffectTf = None

	if arg_25_0.selected:
		arg_25_0.animate(arg_25_0.selectedIndex.i, arg_25_0.selectedIndex.j, False)

		arg_25_0.selected = None
		arg_25_0.selectedIndex = None

		arg_25_0.reorderTiles()

def var_0_0.select(arg_26_0, arg_26_1, arg_26_2):
	arg_26_0.unselect()

	arg_26_0.selected = arg_26_0.tileTfs[arg_26_1][arg_26_2]
	arg_26_0.selectedIndex = {
		i = arg_26_1,
		j = arg_26_2
	}
	arg_26_0.selectedEffectTf = rtf(cloneTplTo(arg_26_0.selectedEffect, arg_26_0.tilesRoot))
	arg_26_0.selectedEffectTf.anchoredPosition = arg_26_0.selected.anchoredPosition

	arg_26_0.selected.SetAsLastSibling()
	arg_26_0.animate(arg_26_1, arg_26_2, True)

def var_0_0.animate(arg_27_0, arg_27_1, arg_27_2, arg_27_3):
	if not arg_27_0.tileTfs[arg_27_1][arg_27_2]:
		warning("bad position", arg_27_1, arg_27_2)

	arg_27_0.tileTfs[arg_27_1][arg_27_2].GetComponent("Animator").SetBool("selected", arg_27_3)

	for iter_27_0, iter_27_1 in pairs(var_0_29):
		local var_27_0 = arg_27_0.tileTfs[arg_27_1 + iter_27_1[1]][arg_27_2 + iter_27_1[2]]

		if var_27_0:
			var_27_0.GetComponent("Animator").SetBool("selected", arg_27_3)

	if arg_27_0.hint:
		arg_27_0.hint1.GetComponent("Animator").SetBool("selected", True)
		arg_27_0.hint2.GetComponent("Animator").SetBool("selected", True)

def var_0_0.tryMoveTo(arg_28_0, arg_28_1):
	if arg_28_0.selectedIndex == None:
		return

	if arg_28_0.hintTimer:
		arg_28_0.hintTimer.Pause()

	if not arg_28_0.tileIndicies[arg_28_1.i][arg_28_1.j]:
		return

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_23)

	if arg_28_0.moveValid(arg_28_0.selectedIndex, arg_28_1):
		local var_28_0 = arg_28_0.selectedIndex

		arg_28_0.unselect()

		arg_28_0.updating = True

		arg_28_0.swap(var_28_0, arg_28_1)
		arg_28_0.managedTween(LeanTween.delayedCall, function()
			if not arg_28_0.inGame:
				return

			arg_28_0.combo = 0

			arg_28_0.update(), var_0_13, None)
	else
		local var_28_1 = arg_28_0.tileTfs[arg_28_0.selectedIndex.i][arg_28_0.selectedIndex.j]
		local var_28_2 = arg_28_0.tileTfs[arg_28_1.i][arg_28_1.j]
		local var_28_3 = arg_28_0.index2pos(arg_28_0.selectedIndex.i, arg_28_0.selectedIndex.j)
		local var_28_4 = arg_28_0.index2pos(arg_28_1.i, arg_28_1.j)

		arg_28_0.managedTween(LeanTween.move, None, var_28_1, var_28_4, var_0_13).setLoopPingPong(1)
		arg_28_0.managedTween(LeanTween.move, None, var_28_2, var_28_3, var_0_13).setLoopPingPong(1)

		arg_28_0.updating = True

		arg_28_0.managedTween(LeanTween.delayedCall, function()
			arg_28_0.updating = False

			arg_28_0.hintTimer.Resume(), var_0_13 * 2 + 0.1, None)
		arg_28_0.unselect()

local var_0_30 = {
	{
		{
			0,
			-2
		},
		{
			0,
			-1
		}
	},
	{
		{
			0,
			-1
		},
		{
			0,
			1
		}
	},
	{
		{
			0,
			1
		},
		{
			0,
			2
		}
	}
}

def var_0_0.isConnected(arg_31_0, arg_31_1):
	for iter_31_0, iter_31_1 in pairs(var_0_30):
		local var_31_0
		local var_31_1
		local var_31_2
		local var_31_3 = arg_31_0.tileIndicies[arg_31_1.i][arg_31_1.j]
		local var_31_4 = arg_31_0.tileIndicies[arg_31_1.i + iter_31_1[1][1]][arg_31_1.j + iter_31_1[1][2]]
		local var_31_5 = arg_31_0.tileIndicies[arg_31_1.i + iter_31_1[2][1]][arg_31_1.j + iter_31_1[2][2]]

		if var_31_3 == var_31_4 and var_31_3 == var_31_5:
			return True

		local var_31_6 = arg_31_0.tileIndicies[arg_31_1.i + iter_31_1[1][2]][arg_31_1.j + iter_31_1[1][1]]
		local var_31_7 = arg_31_0.tileIndicies[arg_31_1.i + iter_31_1[2][2]][arg_31_1.j + iter_31_1[2][1]]

		if var_31_3 == var_31_6 and var_31_3 == var_31_7:
			return True

	return False

def var_0_0.moveValid(arg_32_0, arg_32_1, arg_32_2):
	arg_32_0.tileIndicies[arg_32_1.i][arg_32_1.j], arg_32_0.tileIndicies[arg_32_2.i][arg_32_2.j] = arg_32_0.tileIndicies[arg_32_2.i][arg_32_2.j], arg_32_0.tileIndicies[arg_32_1.i][arg_32_1.j]

	local var_32_0 = arg_32_0.isConnected(arg_32_1) or arg_32_0.isConnected(arg_32_2)

	arg_32_0.tileIndicies[arg_32_1.i][arg_32_1.j], arg_32_0.tileIndicies[arg_32_2.i][arg_32_2.j] = arg_32_0.tileIndicies[arg_32_2.i][arg_32_2.j], arg_32_0.tileIndicies[arg_32_1.i][arg_32_1.j]

	return var_32_0

def var_0_0.moveTile(arg_33_0, arg_33_1, arg_33_2, arg_33_3):
	local var_33_0 = arg_33_0.index2pos(arg_33_2.i, arg_33_2.j)

	arg_33_0.managedTween(LeanTween.move, None, arg_33_1, var_33_0, arg_33_3 or 0).setEase(LeanTweenType.easeInQuad)

def var_0_0.swap(arg_34_0, arg_34_1, arg_34_2):
	local var_34_0 = arg_34_0.tileTfs[arg_34_1.i][arg_34_1.j]
	local var_34_1 = arg_34_0.tileTfs[arg_34_2.i][arg_34_2.j]

	arg_34_0.moveTile(var_34_0, arg_34_2, var_0_13)
	arg_34_0.moveTile(var_34_1, arg_34_1, var_0_13)

	arg_34_0.tileTfs[arg_34_1.i][arg_34_1.j], arg_34_0.tileTfs[arg_34_2.i][arg_34_2.j] = arg_34_0.tileTfs[arg_34_2.i][arg_34_2.j], arg_34_0.tileTfs[arg_34_1.i][arg_34_1.j]
	arg_34_0.tileIndicies[arg_34_1.i][arg_34_1.j], arg_34_0.tileIndicies[arg_34_2.i][arg_34_2.j] = arg_34_0.tileIndicies[arg_34_2.i][arg_34_2.j], arg_34_0.tileIndicies[arg_34_1.i][arg_34_1.j]

def var_0_0.formatTime(arg_35_0, arg_35_1):
	local var_35_0 = math.floor(arg_35_1 / 60)

	arg_35_1 = arg_35_1 - var_35_0 * 60

	local var_35_1 = math.floor(arg_35_1)

	return var_35_0 .. "." .. var_35_1

def dir2Angle(arg_36_0):
	if arg_36_0[1] == 1:
		return -90
	elif arg_36_0[1] == -1:
		return 90
	elif arg_36_0[2] == 1:
		return 180
	elif arg_36_0[2] == -1:
		return 0

def var_0_0.startGame(arg_37_0):
	arg_37_0.updateData()

	local var_37_0 = Timer.New(function()
		arg_37_0.managedTween(LeanTween.value, function()
			arg_37_0.gamePage.GetComponent("CanvasGroup").alpha = 1

			arg_37_0.stopGame(), go(arg_37_0.gamePage), 1, 0, var_0_10).setOnUpdate(System.Action_float(function(arg_40_0)
			arg_37_0.gamePage.GetComponent("CanvasGroup").alpha = arg_40_0))
		UpdateBeat.RemoveListener(arg_37_0.handle), arg_37_0.infinite and var_0_15 or var_0_16)

	arg_37_0.handle = UpdateBeat.CreateListener(function()
		setText(arg_37_0.countdownText, math.floor(var_37_0.time))

		if var_37_0.time <= var_0_17 and not isActive(arg_37_0.warning):
			setActive(arg_37_0.warning, True), arg_37_0)

	var_37_0.Start()
	UpdateBeat.AddListener(arg_37_0.handle)

	arg_37_0.timer = var_37_0

	setActive(arg_37_0.inf, False)
	setActive(arg_37_0.countdownText, True)

	arg_37_0.tileIndicies = {}

	for iter_37_0 = -1, var_0_1 + 2:
		arg_37_0.tileIndicies[iter_37_0] = {}

	arg_37_0.tileTfs = {}

	for iter_37_1 = -1, var_0_1 + 2:
		arg_37_0.tileTfs[iter_37_1] = {}

	arg_37_0.fillTileIndicies()
	arg_37_0.fillTiles(True)

	arg_37_0.selected = None
	arg_37_0.updating = False
	arg_37_0.score = 0
	arg_37_0.combo = 0
	arg_37_0.inGame = True

	setText(arg_37_0.scoreText, arg_37_0.score)

	function arg_37_0.hintFunc()
		if arg_37_0.hint:
			return

		local var_42_0, var_42_1, var_42_2 = arg_37_0.findMove()
		local var_42_3

		var_42_3.anchoredPosition, var_42_3 = (arg_37_0.index2pos(var_42_0, var_42_1) + arg_37_0.index2pos(var_42_0 + var_42_2[1], var_42_1 + var_42_2[2])) / 2, rtf(cloneTplTo(arg_37_0.hintEffect, arg_37_0.tilesRoot))
		var_42_3.localEulerAngles = Vector3.New(0, 0, dir2Angle(var_42_2))
		arg_37_0.hint = var_42_3
		arg_37_0.hint1 = arg_37_0.tileTfs[var_42_0][var_42_1]
		arg_37_0.hint2 = arg_37_0.tileTfs[var_42_0 + var_42_2[1]][var_42_1 + var_42_2[2]]

		arg_37_0.hint1.GetComponent("Animator").SetBool("selected", True)
		arg_37_0.hint2.GetComponent("Animator").SetBool("selected", True)

	arg_37_0.hintTimer = Timer.New(arg_37_0.hintFunc, var_0_21)

	arg_37_0.hintTimer.Start()

def var_0_0.pauseGame(arg_43_0):
	if arg_43_0.timer:
		arg_43_0.timer.Pause()

	if arg_43_0.hintTimer:
		arg_43_0.hintTimer.Pause()

	if arg_43_0.warning:
		arg_43_0.warning.GetComponent("Animator").enabled = False

	arg_43_0.pauseManagedTween()

def var_0_0.pause(arg_44_0):
	setActive(arg_44_0.pausePage, True)
	arg_44_0.pauseGame()

def var_0_0.resumeGame(arg_45_0):
	if arg_45_0.timer:
		arg_45_0.timer.Resume()

	if arg_45_0.hintTimer:
		arg_45_0.hintTimer.Resume()

	if arg_45_0.warning:
		arg_45_0.warning.GetComponent("Animator").enabled = True

	arg_45_0.resumeManagedTween()

def var_0_0.fillTileIndicies(arg_46_0):
	local var_46_0 = {}

	for iter_46_0 = -1, var_0_1 + 2:
		var_46_0[iter_46_0] = {}

		for iter_46_1 = 1, var_0_2:
			var_46_0[iter_46_0][iter_46_1] = arg_46_0.tileIndicies[iter_46_0][iter_46_1]

	repeat
		arg_46_0.tileIndicies = {}

		for iter_46_2 = -1, var_0_1 + 2:
			arg_46_0.tileIndicies[iter_46_2] = {}

			for iter_46_3 = 1, var_0_2:
				arg_46_0.tileIndicies[iter_46_2][iter_46_3] = var_46_0[iter_46_2][iter_46_3]

		for iter_46_4 = 1, var_0_1:
			for iter_46_5 = 1, var_0_2:
				if not arg_46_0.tileIndicies[iter_46_4][iter_46_5]:
					local var_46_1
					local var_46_2

					if arg_46_0.tileIndicies[iter_46_4 - 1][iter_46_5] and arg_46_0.tileIndicies[iter_46_4 - 1][iter_46_5] == arg_46_0.tileIndicies[iter_46_4 - 2][iter_46_5]:
						var_46_1 = arg_46_0.tileIndicies[iter_46_4 - 1][iter_46_5]

					if arg_46_0.tileIndicies[iter_46_4][iter_46_5 - 1] and arg_46_0.tileIndicies[iter_46_4][iter_46_5 - 1] == arg_46_0.tileIndicies[iter_46_4][iter_46_5 - 2]:
						var_46_2 = arg_46_0.tileIndicies[iter_46_4][iter_46_5 - 2]

					local var_46_3 = math.random(1, #arg_46_0.tiles)

					while var_46_3 == var_46_1 or var_46_3 == var_46_2:
						var_46_3 = math.random(1, #arg_46_0.tiles)

					arg_46_0.tileIndicies[iter_46_4][iter_46_5] = var_46_3
	until arg_46_0.findMove()

def var_0_0.reorderTiles(arg_47_0):
	for iter_47_0 = 1, var_0_1:
		for iter_47_1 = 1, var_0_2:
			if arg_47_0.tileTfs[iter_47_0][iter_47_1]:
				arg_47_0.tileTfs[iter_47_0][iter_47_1].SetAsFirstSibling()

def var_0_0.fillTiles(arg_48_0, arg_48_1):
	local var_48_0 = 0

	for iter_48_0 = 1, var_0_2:
		local var_48_1 = 0

		for iter_48_1 = var_0_1, 1, -1:
			if not arg_48_0.tileTfs[iter_48_1][iter_48_0]:
				var_48_1 = var_48_1 + 1

		var_48_0 = math.max(var_48_1, var_48_0)

		for iter_48_2 = 1, var_0_1:
			if not arg_48_0.tileTfs[iter_48_2][iter_48_0]:
				local var_48_2 = rtf(cloneTplTo(arg_48_0.tiles[arg_48_0.tileIndicies[iter_48_2][iter_48_0]], arg_48_0.tilesRoot))

				if arg_48_1:
					var_48_2.anchoredPosition = arg_48_0.index2pos(iter_48_2, iter_48_0)
				else
					var_48_2.anchoredPosition = arg_48_0.index2pos(iter_48_2 + var_48_1, iter_48_0)

					arg_48_0.moveTile(var_48_2, {
						i = iter_48_2,
						j = iter_48_0
					}, arg_48_0.dropTime(var_48_1))

				arg_48_0.tileTfs[iter_48_2][iter_48_0] = var_48_2

	arg_48_0.reorderTiles()

	return var_48_0

local var_0_31 = {
	{
		{
			-1,
			-2
		},
		{
			-1,
			-1
		}
	},
	{
		{
			-1,
			-1
		},
		{
			-1,
			1
		}
	},
	{
		{
			-1,
			1
		},
		{
			-1,
			2
		}
	}
}

def var_0_0.findMove(arg_49_0):
	for iter_49_0 = 1, var_0_1:
		for iter_49_1 = 1, var_0_2:
			local var_49_0 = arg_49_0.tileIndicies[iter_49_0][iter_49_1]
			local var_49_1
			local var_49_2

			for iter_49_2, iter_49_3 in pairs(var_0_31):
				local var_49_3 = arg_49_0.tileIndicies[iter_49_0 + iter_49_3[1][1]][iter_49_1 + iter_49_3[1][2]]
				local var_49_4 = arg_49_0.tileIndicies[iter_49_0 + iter_49_3[2][1]][iter_49_1 + iter_49_3[2][2]]

				if var_49_0 == var_49_3 and var_49_0 == var_49_4:
					return iter_49_0, iter_49_1, {
						-1,
						0
					}

				local var_49_5 = arg_49_0.tileIndicies[iter_49_0 - iter_49_3[1][1]][iter_49_1 - iter_49_3[1][2]]
				local var_49_6 = arg_49_0.tileIndicies[iter_49_0 - iter_49_3[2][1]][iter_49_1 - iter_49_3[2][2]]

				if var_49_0 == var_49_5 and var_49_0 == var_49_6:
					return iter_49_0, iter_49_1, {
						1,
						0
					}

				local var_49_7 = arg_49_0.tileIndicies[iter_49_0 - iter_49_3[1][2]][iter_49_1 + iter_49_3[1][1]]
				local var_49_8 = arg_49_0.tileIndicies[iter_49_0 - iter_49_3[2][2]][iter_49_1 + iter_49_3[2][1]]

				if var_49_0 == var_49_7 and var_49_0 == var_49_8:
					return iter_49_0, iter_49_1, {
						0,
						-1
					}

				local var_49_9 = arg_49_0.tileIndicies[iter_49_0 + iter_49_3[1][2]][iter_49_1 - iter_49_3[1][1]]
				local var_49_10 = arg_49_0.tileIndicies[iter_49_0 + iter_49_3[2][2]][iter_49_1 - iter_49_3[2][1]]

				if var_49_0 == var_49_9 and var_49_0 == var_49_10:
					return iter_49_0, iter_49_1, {
						0,
						1
					}

def var_0_0.stopGame(arg_50_0):
	arg_50_0.inGame = False

	setActive(arg_50_0.warning, False)
	arg_50_0.hintTimer.Reset(arg_50_0.hintFunc, 5)
	arg_50_0.hintTimer.Stop()
	arg_50_0.cleanManagedTween(True)
	arg_50_0.cancelHint()

	if arg_50_0.timer:
		arg_50_0.timer.Pause()

	if arg_50_0.handle:
		UpdateBeat.RemoveListener(arg_50_0.handle)

	for iter_50_0 = 1, var_0_1:
		for iter_50_1 = 1, var_0_2:
			if arg_50_0.tileTfs[iter_50_0][iter_50_1]:
				Destroy(arg_50_0.tileTfs[iter_50_0][iter_50_1])

	if arg_50_0.selectedEffectTf:
		Destroy(arg_50_0.selectedEffectTf)

		arg_50_0.selectedEffectTf = None

	setText(arg_50_0.bestScore, math.max(arg_50_0.best, arg_50_0.score))
	setActive(arg_50_0.gamePage, False)
	setActive(arg_50_0.pausePage, False)
	setActive(arg_50_0.endBtn, False)
	setActive(arg_50_0.endPage, True)

	if arg_50_0.score > 0:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_27)

	setActive(arg_50_0.newSign, False)
	setText(arg_50_0.endScore, 0)
	arg_50_0.managedTween(LeanTween.value, function()
		setActive(arg_50_0.newSign, arg_50_0.best < arg_50_0.score)
		setActive(arg_50_0.endBtn, True)
		setImageAlpha(arg_50_0.endBtn, 0)

		arg_50_0.endBtn.GetComponent("Button").enabled = False

		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_28)
		arg_50_0.managedTween(LeanTween.value, function()
			arg_50_0.endBtn.GetComponent("Button").enabled = True
			arg_50_0.timer = None

			arg_50_0.SendSuccess(arg_50_0.score), go(arg_50_0.endBtn), 0, 1, var_0_19).setOnUpdate(System.Action_float(function(arg_53_0)
			setImageAlpha(arg_50_0.endBtn, arg_53_0))), go(arg_50_0.endScore), 0, arg_50_0.score, arg_50_0.score > 0 and var_0_18 or 0).setOnUpdate(System.Action_float(function(arg_54_0)
		setText(arg_50_0.endScore, math.floor(arg_54_0))))

def var_0_0.formatScore(arg_55_0, arg_55_1, arg_55_2):
	local var_55_0 = {}

	while arg_55_2 > 0:
		table.insert(var_55_0, math.fmod(arg_55_2, 10))

		arg_55_2 = math.floor(arg_55_2 / 10)

	for iter_55_0 = #var_55_0, 1, -1:
		cloneTplTo(arg_55_0.floatChar[var_55_0[iter_55_0]], arg_55_1)

def var_0_0.update(arg_56_0):
	arg_56_0.hintTimer.Stop()

	local var_56_0 = True

	arg_56_0.updating = True

	local var_56_1 = arg_56_0.tryMatch()

	if next(var_56_1) != None:
		arg_56_0.cancelHint()

		var_56_0 = False
		arg_56_0.combo = arg_56_0.combo + 1

		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_24)

		local var_56_2

		for iter_56_0, iter_56_1 in pairs(var_56_1):
			if #iter_56_1 == 3:
				var_56_2 = 30 * arg_56_0.combo
			elif #iter_56_1 == 4:
				var_56_2 = 60 * arg_56_0.combo
			else
				var_56_2 = 20 * #iter_56_1 * arg_56_0.combo

			arg_56_0.score = arg_56_0.score + var_56_2

			setText(arg_56_0.scoreText, arg_56_0.score)

			local var_56_3 = Vector2.zero

			_.each(iter_56_1, function(arg_57_0)
				arg_56_0.tileIndicies[arg_57_0[1]][arg_57_0[2]] = None

				if arg_56_0.tileTfs[arg_57_0[1]][arg_57_0[2]]:
					local var_57_0 = arg_56_0.tileTfs[arg_57_0[1]][arg_57_0[2]]

					var_56_3 = var_56_3 + var_57_0.anchoredPosition
					var_57_0.GetComponent("Image").material = arg_56_0.whitenMat

					local var_57_1 = var_57_0.localPosition

					var_57_1.z = -50

					local var_57_2 = cloneTplTo(arg_56_0.matchEffect, arg_56_0.tilesRoot)

					var_57_2.localPosition = var_57_1

					arg_56_0.managedTween(LeanTween.value, function()
						Destroy(var_57_0)
						Destroy(var_57_2), go(var_57_0), 1, 0, var_0_10).setOnUpdate(System.Action_float(function(arg_59_0)
						setImageAlpha(var_57_0, arg_59_0)
						setLocalScale(var_57_0, Vector3.one * arg_59_0 * 2.7)))

				arg_56_0.tileTfs[arg_57_0[1]][arg_57_0[2]] = None)

			var_56_3 = var_56_3 / #iter_56_1

			local var_56_4 = rtf(cloneTplTo(arg_56_0.floatText, arg_56_0.tilesRoot))

			var_56_4.anchoredPosition = var_56_3

			arg_56_0.formatScore(var_56_4, var_56_2)
			arg_56_0.managedTween(LeanTween.moveY, function()
				Destroy(var_56_4), var_56_4, var_56_3.y + var_0_12, var_0_11)

		arg_56_0.managedTween(LeanTween.delayedCall, function()
			if not arg_56_0.inGame:
				return

			local var_61_0 = 0

			for iter_61_0 = 1, var_0_1:
				for iter_61_1 = 1, var_0_2:
					if arg_56_0.tileIndicies[iter_61_0][iter_61_1]:
						local var_61_1 = iter_61_0

						for iter_61_2 = iter_61_0, 1, -1:
							if arg_56_0.tileIndicies[iter_61_2 - 1][iter_61_1] or iter_61_2 == 1:
								var_61_1 = iter_61_2

								break

						if var_61_1 != iter_61_0:
							local var_61_2 = iter_61_0 - var_61_1

							var_61_0 = math.max(var_61_2, var_61_0)

							arg_56_0.moveTile(arg_56_0.tileTfs[iter_61_0][iter_61_1], {
								i = var_61_1,
								j = iter_61_1
							}, arg_56_0.dropTime(var_61_2))

							arg_56_0.tileTfs[var_61_1][iter_61_1] = arg_56_0.tileTfs[iter_61_0][iter_61_1]
							arg_56_0.tileIndicies[var_61_1][iter_61_1] = arg_56_0.tileIndicies[iter_61_0][iter_61_1]
							arg_56_0.tileTfs[iter_61_0][iter_61_1] = None
							arg_56_0.tileIndicies[iter_61_0][iter_61_1] = None

			arg_56_0.fillTileIndicies()

			local var_61_3 = arg_56_0.tryMatch()

			if arg_56_0.combo > 1 and next(var_61_3) == None:
				local var_61_4
				local var_61_5 = Vector3.New(0, 0, -50)

				if arg_56_0.combo == 2:
					var_61_4 = cloneTplTo(arg_56_0.goodEffect, arg_56_0.tilesRoot)

					pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_25)
				elif arg_56_0.combo == 3:
					var_61_4 = cloneTplTo(arg_56_0.greatEffect, arg_56_0.tilesRoot)

					pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_25)
				else
					var_61_4 = cloneTplTo(arg_56_0.perfectEffect, arg_56_0.tilesRoot)

					pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_26)

				var_61_4.localPosition = var_61_5

				arg_56_0.managedTween(LeanTween.delayedCall, function()
					Destroy(var_61_4), var_0_14, None)

			local var_61_6 = math.max(arg_56_0.fillTiles(), var_61_0)

			arg_56_0.managedTween(LeanTween.delayedCall, function()
				if not arg_56_0.inGame:
					return

				arg_56_0.update(), math.max(var_0_14, arg_56_0.dropTime(var_61_6)), None), var_0_10, None)

	if arg_56_0.inGame:
		arg_56_0.hintTimer.Reset(arg_56_0.hintFunc, var_0_21)
		arg_56_0.hintTimer.Start()

	arg_56_0.updating = not var_56_0

def var_0_0.tryMatch(arg_64_0):
	local var_64_0 = {}

	for iter_64_0 = 1, var_0_1:
		var_64_0[iter_64_0] = {}

	return arg_64_0.bfs(var_64_0)

def var_0_0.bfs(arg_65_0, arg_65_1):
	local var_65_0 = {}

	for iter_65_0 = 1, var_0_1:
		for iter_65_1 = 1, var_0_2:
			if not arg_65_1[iter_65_0][iter_65_1]:
				if not arg_65_0.isConnected({
					i = iter_65_0,
					j = iter_65_1
				}):
					arg_65_1[iter_65_0][iter_65_1] = True
				else
					local var_65_1 = {
						{
							iter_65_0,
							iter_65_1
						}
					}
					local var_65_2 = {
						{
							iter_65_0,
							iter_65_1
						}
					}
					local var_65_3 = arg_65_0.tileIndicies[iter_65_0][iter_65_1]

					while next(var_65_1) != None:
						local var_65_4, var_65_5 = unpack(table.remove(var_65_1))

						arg_65_1[var_65_4][var_65_5] = True

						for iter_65_2, iter_65_3 in pairs(var_0_29):
							local var_65_6 = var_65_4 + iter_65_3[1]
							local var_65_7 = var_65_5 + iter_65_3[2]

							if arg_65_0.tileIndicies[var_65_6][var_65_7] and not arg_65_1[var_65_6][var_65_7] and arg_65_0.tileIndicies[var_65_6][var_65_7] == var_65_3 and arg_65_0.isConnected({
								i = var_65_6,
								j = var_65_7
							}):
								table.insert(var_65_1, {
									var_65_6,
									var_65_7
								})
								table.insert(var_65_2, {
									var_65_6,
									var_65_7
								})

					if #var_65_2 >= 3:
						table.insert(var_65_0, var_65_2)

	return var_65_0

return var_0_0
