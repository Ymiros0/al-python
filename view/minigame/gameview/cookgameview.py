local var_0_0 = class("CookGameView", import("..BaseMiniGameView"))
local var_0_1 = "bar-soft"
local var_0_2 = "event./ui/ddldaoshu2"
local var_0_3 = "event./ui/break_out_full"
local var_0_4 = 60
local var_0_5 = "cookgameui_atlas"
local var_0_6 = 0.1
local var_0_7 = 8
local var_0_8 = {
	time_up = 0.5,
	cake_num = 5,
	extend_time = 10,
	char_path = "ui/minigameui/cookgameassets",
	speed_num = 3,
	path = "ui/minigameui/" .. var_0_5
}

var_0_0.CLICK_JUDGE_EVENT = "click judge event"
var_0_0.AC_CAKE_EVENT = "ac cake event"
var_0_0.SERVE_EVENT = "serve event"
var_0_0.EXTEND_EVENT = "extend event"

def var_0_0.getUIName(arg_1_0):
	return "CookGameUI"

def var_0_0.didEnter(arg_2_0):
	arg_2_0.initEvent()
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.initGameUI()
	arg_2_0.initController()
	arg_2_0.updateMenuUI()
	arg_2_0.openMenuUI()

def var_0_0.initEvent(arg_3_0):
	if not arg_3_0.uiCam:
		arg_3_0.uiCam = GameObject.Find("UICamera").GetComponent("Camera")

	arg_3_0.bind(CookGameView.CLICK_JUDGE_EVENT, function(arg_4_0, arg_4_1, arg_4_2)
		if arg_3_0.charController:
			arg_3_0.charController.setJudgeAction(arg_4_1, None, arg_4_2))
	arg_3_0.bind(CookGameView.AC_CAKE_EVENT, function(arg_5_0, arg_5_1, arg_5_2)
		if arg_3_0.charController:
			arg_3_0.charController.createAcCake(arg_5_1, arg_5_2))
	arg_3_0.bind(CookGameView.SERVE_EVENT, function(arg_6_0, arg_6_1, arg_6_2)
		local var_6_0 = arg_6_1.serveData.battleData.id
		local var_6_1 = arg_6_1.right
		local var_6_2 = arg_6_1.pos
		local var_6_3 = arg_6_1.rate
		local var_6_4 = arg_6_1.weight
		local var_6_5 = var_6_1 and 1 or -1
		local var_6_6 = var_6_1 and 1 or 0
		local var_6_7 = arg_6_1.serveData.parameter.right_index
		local var_6_8
		local var_6_9 = var_6_0 != var_0_8.playerChar and var_6_0 != var_0_8.partnerChar and var_6_0 != var_0_8.partnerPet

		if not arg_6_1.serveData.battleData.weight:
			local var_6_10 = 0

		if var_6_1 and arg_6_1.serveData.battleData.cake_allow:
			var_6_6 = 3

		if var_6_1 and arg_6_1.serveData.battleData.score_added:
			var_6_5 = var_6_5 + arg_6_1.serveData.parameter.series_right_index - 1

		if arg_6_1.serveData.battleData.random_score:
			var_6_5 = var_6_5 * math.random(1, CookGameConst.random_score)

		local var_6_11 = var_6_5 * var_6_3

		arg_3_0.addScore(var_6_11, var_6_9)
		arg_3_0.showScore(var_6_11, var_6_2, var_6_6)

		if arg_6_1.serveData.battleData.double_score == 8:
			if var_6_1 and var_6_7 and var_6_7 % 2 == 0:
				arg_3_0.addScore(var_6_11, var_6_9)
				LeanTween.delayedCall(go(arg_3_0._tf), 0.5, System.Action(function()
					arg_3_0.showScore(var_6_11, var_6_2, 2)))
		elif arg_6_1.serveData.battleData.half_double and var_6_1 and math.random() > 0.5:
			arg_3_0.addScore(var_6_11, var_6_9)
			LeanTween.delayedCall(go(arg_3_0._tf), 0.5, System.Action(function()
				arg_3_0.showScore(var_6_11, var_6_2, 2))))
	arg_3_0.bind(CookGameView.EXTEND_EVENT, function(arg_9_0, arg_9_1, arg_9_2)
		if arg_3_0.judgesController:
			arg_3_0.judgesController.extend()

		arg_3_0.waitingExtendTime = False
		arg_3_0.extendTime = var_0_8.extend_time
		arg_3_0.gameTime = 0)

def var_0_0.showScore(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	if arg_10_1 == 0:
		return

	local var_10_0

	if #arg_10_0.showScoresPool > 0:
		var_10_0 = table.remove(arg_10_0.showScoresPool, 1)
	else
		var_10_0 = tf(Instantiate(arg_10_0.showScoreTpl))

		setParent(var_10_0, arg_10_0.sceneFrontContainer)
		GetComponent(findTF(var_10_0, "anim"), typeof(DftAniEvent)).SetEndEvent(function()
			for iter_11_0 = #arg_10_0.showScores, 1, -1:
				if var_10_0 == arg_10_0.showScores[iter_11_0]:
					setActive(var_10_0, False)
					table.insert(arg_10_0.showScoresPool, table.remove(arg_10_0.showScores, iter_11_0)))

	var_10_0.anchoredPosition = arg_10_0.sceneFrontContainer.InverseTransformPoint(arg_10_2)

	setText(findTF(var_10_0, "anim/text_sub"), "" .. tostring(arg_10_1))
	setText(findTF(var_10_0, "anim/text_add"), "+" .. tostring(arg_10_1))

	if arg_10_1 > 0:
		setActive(findTF(var_10_0, "anim/text_sub"), False)
		setActive(findTF(var_10_0, "anim/text_add"), True)
	else
		setActive(findTF(var_10_0, "anim/text_sub"), True)
		setActive(findTF(var_10_0, "anim/text_add"), False)

	setActive(var_10_0, False)
	setActive(var_10_0, True)
	table.insert(arg_10_0.showScores, var_10_0)

def var_0_0.onEventHandle(arg_12_0, arg_12_1):
	return

def var_0_0.initData(arg_13_0):
	local var_13_0 = Application.targetFrameRate or 60

	if var_13_0 > 60:
		var_13_0 = 60

	arg_13_0.timer = Timer.New(function()
		arg_13_0.onTimer(), 1 / var_13_0, -1)
	arg_13_0.showScores = {}
	arg_13_0.showScoresPool = {}
	arg_13_0.dropData = pg.mini_game[arg_13_0.GetMGData().id].simple_config_data.drop_ids
	var_0_8.playerChar = None
	var_0_8.partnerChar = None
	var_0_8.partnerPet = None
	var_0_8.enemy1Char = None
	var_0_8.enemy2Char = None
	var_0_8.enemyPet = None
	arg_13_0.selectPlayer = True
	arg_13_0.selectPartner = False

def var_0_0.initUI(arg_15_0):
	arg_15_0.backSceneTf = findTF(arg_15_0._tf, "scene_background")
	arg_15_0.sceneContainer = findTF(arg_15_0._tf, "sceneMask/sceneContainer")
	arg_15_0.sceneFrontContainer = findTF(arg_15_0._tf, "sceneMask/sceneContainer/scene_front")
	arg_15_0.clickMask = findTF(arg_15_0._tf, "clickMask")
	arg_15_0.bg = findTF(arg_15_0._tf, "bg")
	arg_15_0.countUI = findTF(arg_15_0._tf, "pop/CountUI")
	arg_15_0.countAnimator = GetComponent(findTF(arg_15_0.countUI, "count"), typeof(Animator))
	arg_15_0.countDft = GetOrAddComponent(findTF(arg_15_0.countUI, "count"), typeof(DftAniEvent))

	arg_15_0.countDft.SetTriggerEvent(function()
		return)
	arg_15_0.countDft.SetEndEvent(function()
		setActive(arg_15_0.countUI, False)
		arg_15_0.gameStart())

	arg_15_0.leaveUI = findTF(arg_15_0._tf, "pop/LeaveUI")

	onButton(arg_15_0, findTF(arg_15_0.leaveUI, "ad/btnOk"), function()
		arg_15_0.resumeGame()
		arg_15_0.onGameOver(), SFX_CANCEL)
	onButton(arg_15_0, findTF(arg_15_0.leaveUI, "ad/btnCancel"), function()
		arg_15_0.resumeGame(), SFX_CANCEL)
	setActive(arg_15_0.leaveUI, False)

	arg_15_0.pauseUI = findTF(arg_15_0._tf, "pop/pauseUI")

	onButton(arg_15_0, findTF(arg_15_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_15_0.pauseUI, False)
		arg_15_0.resumeGame(), SFX_CANCEL)

	arg_15_0.settlementUI = findTF(arg_15_0._tf, "pop/SettleMentUI")

	onButton(arg_15_0, findTF(arg_15_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_15_0.settlementUI, False)
		arg_15_0.openMenuUI(), SFX_CANCEL)
	setActive(arg_15_0.settlementUI, False)

	arg_15_0.menuUI = findTF(arg_15_0._tf, "pop/menuUI")
	arg_15_0.battleScrollRect = GetComponent(findTF(arg_15_0.menuUI, "battList"), typeof(ScrollRect))
	arg_15_0.totalTimes = arg_15_0.getGameTotalTime()

	local var_15_0 = arg_15_0.getGameUsedTimes() - 4 < 0 and 0 or arg_15_0.getGameUsedTimes() - 4

	scrollTo(arg_15_0.battleScrollRect, 0, 1 - var_15_0 / (arg_15_0.totalTimes - 4))
	onButton(arg_15_0, findTF(arg_15_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_22_0 = arg_15_0.battleScrollRect.normalizedPosition.y + 1 / (arg_15_0.totalTimes - 4)

		if var_22_0 > 1:
			var_22_0 = 1

		scrollTo(arg_15_0.battleScrollRect, 0, var_22_0), SFX_CANCEL)
	onButton(arg_15_0, findTF(arg_15_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_23_0 = arg_15_0.battleScrollRect.normalizedPosition.y - 1 / (arg_15_0.totalTimes - 4)

		if var_23_0 < 0:
			var_23_0 = 0

		scrollTo(arg_15_0.battleScrollRect, 0, var_23_0), SFX_CANCEL)
	onButton(arg_15_0, findTF(arg_15_0.menuUI, "adButton/btnBack"), function()
		arg_15_0.closeView(), SFX_CANCEL)
	onButton(arg_15_0, findTF(arg_15_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.mini_cookgametip.tip
		}), SFX_CANCEL)
	onButton(arg_15_0, findTF(arg_15_0.menuUI, "btnStart"), function()
		setActive(arg_15_0.menuUI, False)
		arg_15_0.openSelectUI(), SFX_CANCEL)

	local var_15_1 = findTF(arg_15_0.menuUI, "tplBattleItem")

	arg_15_0.battleItems = {}
	arg_15_0.dropItems = {}

	for iter_15_0 = 1, 7:
		local var_15_2 = tf(instantiate(var_15_1))

		var_15_2.name = "battleItem_" .. iter_15_0

		setParent(var_15_2, findTF(arg_15_0.menuUI, "battList/Viewport/Content"))

		local var_15_3 = iter_15_0

		GetSpriteFromAtlasAsync("ui/minigameui/" .. var_0_5, "battleDesc" .. var_15_3, function(arg_27_0)
			if arg_27_0:
				setImageSprite(findTF(var_15_2, "state_open/desc"), arg_27_0, True)
				setImageSprite(findTF(var_15_2, "state_clear/desc"), arg_27_0, True)
				setImageSprite(findTF(var_15_2, "state_current/desc"), arg_27_0, True)
				setImageSprite(findTF(var_15_2, "state_closed/desc"), arg_27_0, True))

		local var_15_4 = findTF(var_15_2, "icon")
		local var_15_5 = {
			type = arg_15_0.dropData[iter_15_0][1],
			id = arg_15_0.dropData[iter_15_0][2],
			amount = arg_15_0.dropData[iter_15_0][3]
		}

		updateDrop(var_15_4, var_15_5)
		onButton(arg_15_0, var_15_4, function()
			arg_15_0.emit(BaseUI.ON_DROP, var_15_5), SFX_PANEL)
		table.insert(arg_15_0.dropItems, var_15_4)
		setActive(var_15_2, True)
		table.insert(arg_15_0.battleItems, var_15_2)

	arg_15_0.selectUI = findTF(arg_15_0._tf, "pop/selectUI")
	arg_15_0.selectCharTpl = findTF(arg_15_0.selectUI, "ad/charTpl")

	setActive(arg_15_0.selectCharTpl, False)

	arg_15_0.selectCharsContainer = findTF(arg_15_0.selectUI, "ad/chars/Viewport/Content")
	arg_15_0.selectCharId = None
	arg_15_0.selectChars = {}

	local var_15_6 = #CookGameConst.char_ids
	local var_15_7 = findTF(arg_15_0.selectUI, "ad/charDetail")

	arg_15_0.detailDescPositons = {}

	for iter_15_1 = 1, var_15_6:
		local var_15_8 = CookGameConst.char_ids[iter_15_1]
		local var_15_9 = arg_15_0.getCharDataById(var_15_8)
		local var_15_10 = tf(instantiate(arg_15_0.selectCharTpl))

		setParent(var_15_10, arg_15_0.selectCharsContainer)

		if var_15_9:
			local var_15_11 = var_15_9.icon
			local var_15_12 = var_15_9.pos
			local var_15_13 = pg.gametip[var_15_9.desc].tip
			local var_15_14 = pg.ship_data_statistics[var_15_9.ship_id].name

			setScrollText(findTF(var_15_10, "name/text"), var_15_14)
			setActive(findTF(var_15_10, "desc"), False)
			setActive(findTF(var_15_10, "desc_en"), False)

			if PLATFORM_CODE == PLATFORM_US:
				setActive(findTF(var_15_10, "desc_en"), True)
				setText(findTF(var_15_10, "desc_en"), var_15_13)
			else
				setActive(findTF(var_15_10, "desc"), True)
				setText(findTF(var_15_10, "desc"), var_15_13)

			local var_15_15 = findTF(var_15_10, "detailDesc")

			setActive(var_15_15, False)

			if var_15_9.detail_name:
				arg_15_0.detailDescPositons[var_15_9.detail_name] = var_15_15.anchoredPosition

				setText(findTF(var_15_15, "name"), i18n(var_15_9.detail_name))
				setText(findTF(var_15_15, "desc"), i18n(var_15_9.detail_desc))
				setActive(findTF(var_15_10, "clickDesc"), True)
				onButton(arg_15_0, findTF(var_15_10, "clickDesc"), function()
					local var_29_0 = isActive(var_15_15)
					local var_29_1

					if not var_29_0:
						var_29_1 = var_15_7.InverseTransformPoint(var_15_15.position)

						setParent(var_15_15, var_15_7)

						arg_15_0.detailDescTf = var_15_15
						arg_15_0.detailDescContent = var_15_10
						arg_15_0.detailDescName = var_15_9.detail_name
					else
						var_29_1 = arg_15_0.detailDescPositons[var_15_9.detail_name]

						setParent(var_15_15, var_15_10)

						arg_15_0.detailDescTf = None
						arg_15_0.detailDescContent = None
						arg_15_0.detailDescName = None

					var_15_15.anchoredPosition = var_29_1

					setActive(var_15_15, not var_29_0))

			GetSpriteFromAtlasAsync("ui/minigameui/" .. var_0_5, var_15_11, function(arg_30_0)
				local var_30_0 = findTF(var_15_10, "icon/img")

				setActive(var_30_0, True)

				var_30_0.anchoredPosition = var_15_12

				setImageSprite(var_30_0, arg_30_0, True))
			setActive(findTF(var_15_10, "selected"), False)
			onButton(arg_15_0, findTF(var_15_10, "click"), function()
				arg_15_0.selectChar(var_15_9.id), SFX_PANEL)
		else
			GetComponent(var_15_10, typeof(CanvasGroup)).alpha = 0

		setActive(var_15_10, True)
		table.insert(arg_15_0.selectChars, {
			data = var_15_9,
			tf = var_15_10
		})

	arg_15_0.playerTf = findTF(arg_15_0.selectUI, "ad/player")
	arg_15_0.partnerTf = findTF(arg_15_0.selectUI, "ad/partner")
	arg_15_0.selectClickTf = findTF(arg_15_0.selectUI, "ad/click")

	setActive(arg_15_0.selectClickTf, False)
	onButton(arg_15_0, findTF(arg_15_0.selectUI, "ad/btnStart"), function()
		if var_0_8.playerChar and var_0_8.partnerChar:
			arg_15_0.randomAIShip()
			setActive(arg_15_0.selectUI, False)
			arg_15_0.readyStart(), SFX_PANEL)
	onButton(arg_15_0, findTF(arg_15_0.selectUI, "ad/player"), function()
		arg_15_0.selectPlayer = True
		arg_15_0.selectPartner = False

		arg_15_0.updateSelectUI(), SFX_PANEL)
	onButton(arg_15_0, findTF(arg_15_0.selectUI, "ad/partner"), function()
		arg_15_0.selectPlayer = False
		arg_15_0.selectPartner = True

		arg_15_0.updateSelectUI(), SFX_PANEL)
	onButton(arg_15_0, findTF(arg_15_0.selectUI, "ad/back"), function()
		setActive(arg_15_0.selectUI, False)
		arg_15_0.openMenuUI(), SFX_PANEL)

	arg_15_0.pageMax = math.ceil(var_15_6 / var_0_7) - 1
	arg_15_0.curPageIndex = 0
	arg_15_0.scrollNum = 1 / arg_15_0.pageMax
	arg_15_0.scrollRect = GetComponent(findTF(arg_15_0.selectUI, "ad/chars"), typeof(ScrollRect))
	arg_15_0.scrollRect.normalizedPosition = Vector2(0, 0)

	arg_15_0.scrollRect.onValueChanged.Invoke(Vector2(0, 0))

	arg_15_0.scrollRect.normalizedPosition = Vector2(0, 0)

	arg_15_0.scrollRect.onValueChanged.Invoke(Vector2(0, 0))
	GetOrAddComponent(findTF(arg_15_0.selectUI, "ad/chars"), typeof(EventTriggerListener)).AddPointDownFunc(function(arg_36_0, arg_36_1)
		return)
	arg_15_0.scrollRect.onValueChanged.AddListener(function(arg_37_0, arg_37_1, arg_37_2)
		if arg_15_0.detailDescTf:
			setActive(arg_15_0.detailDescTf, False)
			setParent(arg_15_0.detailDescTf, arg_15_0.detailDescContent)

			arg_15_0.detailDescTf.anchoredPosition = arg_15_0.detailDescPositons[arg_15_0.detailDescName]
			arg_15_0.detailDescTf = None
			arg_15_0.detailDescContent = None
			arg_15_0.detailDescName = None)
	onButton(arg_15_0, findTF(arg_15_0.selectUI, "ad/next"), function()
		arg_15_0.curPageIndex = arg_15_0.curPageIndex + arg_15_0.scrollNum

		if arg_15_0.curPageIndex > 1:
			arg_15_0.curPageIndex = 1

		arg_15_0.scrollRect.normalizedPosition = Vector2(arg_15_0.curPageIndex, 0)

		arg_15_0.scrollRect.onValueChanged.Invoke(Vector2(arg_15_0.curPageIndex, 0)), SFX_PANEL)
	onButton(arg_15_0, findTF(arg_15_0.selectUI, "ad/pre"), function()
		arg_15_0.curPageIndex = arg_15_0.curPageIndex - arg_15_0.scrollNum

		if arg_15_0.curPageIndex < 0:
			arg_15_0.curPageIndex = 0

		arg_15_0.scrollRect.normalizedPosition = Vector2(arg_15_0.curPageIndex, 0)

		arg_15_0.scrollRect.onValueChanged.Invoke(Vector2(arg_15_0.curPageIndex, 0)), SFX_PANEL)
	setActive(arg_15_0.selectUI, False)

	if not arg_15_0.handle and IsUnityEditor:
		arg_15_0.handle = UpdateBeat.CreateListener(arg_15_0.Update, arg_15_0)

		UpdateBeat.AddListener(arg_15_0.handle)

	GetComponent(findTF(arg_15_0.selectUI, "ad/playerDesc"), typeof(Image)).SetNativeSize()
	GetComponent(findTF(arg_15_0.selectUI, "ad/partnerDesc"), typeof(Image)).SetNativeSize()
	GetComponent(findTF(arg_15_0.pauseUI, "ad/desc"), typeof(Image)).SetNativeSize()
	GetComponent(findTF(arg_15_0.leaveUI, "ad/desc"), typeof(Image)).SetNativeSize()

def var_0_0.initGameUI(arg_40_0):
	arg_40_0.gameUI = findTF(arg_40_0._tf, "ui/gameUI")
	arg_40_0.showScoreTpl = findTF(arg_40_0.sceneFrontContainer, "score")

	setActive(arg_40_0.showScoreTpl, False)
	onButton(arg_40_0, findTF(arg_40_0.gameUI, "topRight/btnStop"), function()
		arg_40_0.stopGame()
		setActive(arg_40_0.pauseUI, True))
	onButton(arg_40_0, findTF(arg_40_0.gameUI, "btnLeave"), function()
		arg_40_0.stopGame()
		setActive(arg_40_0.leaveUI, True))

	arg_40_0.gameTimeS = findTF(arg_40_0.gameUI, "top/time/s")
	arg_40_0.scoreTf = findTF(arg_40_0.gameUI, "top/score")
	arg_40_0.otherScoreTf = findTF(arg_40_0.gameUI, "top/otherScore")

def var_0_0.initController(arg_43_0):
	arg_43_0.judgesController = CookGameJudgesController.New(arg_43_0.sceneContainer, var_0_8, arg_43_0)

	local var_43_0 = findTF(arg_43_0.sceneContainer, "scene_background/charTpl")

	setActive(var_43_0, False)

	arg_43_0.charController = CookGameCharController.New(arg_43_0.sceneContainer, var_0_8, arg_43_0)

def var_0_0.Update(arg_44_0):
	arg_44_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_45_0):
	if arg_45_0.gameStop or arg_45_0.settlementFlag:
		return

	if IsUnityEditor and Input.GetKeyDown(KeyCode.S):
		-- block empty

def var_0_0.updateMenuUI(arg_46_0):
	local var_46_0 = arg_46_0.getGameUsedTimes()
	local var_46_1 = arg_46_0.getGameTimes()

	for iter_46_0 = 1, #arg_46_0.battleItems:
		setActive(findTF(arg_46_0.battleItems[iter_46_0], "state_open"), False)
		setActive(findTF(arg_46_0.battleItems[iter_46_0], "state_closed"), False)
		setActive(findTF(arg_46_0.battleItems[iter_46_0], "state_clear"), False)
		setActive(findTF(arg_46_0.battleItems[iter_46_0], "state_current"), False)

		if iter_46_0 <= var_46_0:
			SetParent(arg_46_0.dropItems[iter_46_0], findTF(arg_46_0.battleItems[iter_46_0], "state_clear/icon"))
			setActive(arg_46_0.dropItems[iter_46_0], True)
			setActive(findTF(arg_46_0.battleItems[iter_46_0], "state_clear"), True)
		elif iter_46_0 == var_46_0 + 1 and var_46_1 >= 1:
			setActive(findTF(arg_46_0.battleItems[iter_46_0], "state_current"), True)
			SetParent(arg_46_0.dropItems[iter_46_0], findTF(arg_46_0.battleItems[iter_46_0], "state_current/icon"))
			setActive(arg_46_0.dropItems[iter_46_0], True)
		elif var_46_0 < iter_46_0 and iter_46_0 <= var_46_0 + var_46_1:
			setActive(findTF(arg_46_0.battleItems[iter_46_0], "state_open"), True)
			SetParent(arg_46_0.dropItems[iter_46_0], findTF(arg_46_0.battleItems[iter_46_0], "state_open/icon"))
			setActive(arg_46_0.dropItems[iter_46_0], True)
		else
			setActive(findTF(arg_46_0.battleItems[iter_46_0], "state_closed"), True)
			SetParent(arg_46_0.dropItems[iter_46_0], findTF(arg_46_0.battleItems[iter_46_0], "state_closed/icon"))
			setActive(arg_46_0.dropItems[iter_46_0], True)

	arg_46_0.totalTimes = arg_46_0.getGameTotalTime()

	local var_46_2 = 1 - (arg_46_0.getGameUsedTimes() - 3 < 0 and 0 or arg_46_0.getGameUsedTimes() - 3) / (arg_46_0.totalTimes - 4)

	if var_46_2 > 1:
		var_46_2 = 1

	scrollTo(arg_46_0.battleScrollRect, 0, var_46_2)
	setActive(findTF(arg_46_0.menuUI, "btnStart/tip"), var_46_1 > 0)
	arg_46_0.CheckGet()

def var_0_0.CheckGet(arg_47_0):
	setActive(findTF(arg_47_0.menuUI, "got"), False)

	if arg_47_0.getUltimate() and arg_47_0.getUltimate() != 0:
		setActive(findTF(arg_47_0.menuUI, "got"), True)

	if arg_47_0.getUltimate() == 0:
		if arg_47_0.getGameTotalTime() > arg_47_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_47_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_47_0.menuUI, "got"), True)

def var_0_0.openSelectUI(arg_48_0):
	setActive(arg_48_0.selectUI, True)

	arg_48_0.selectPlayer = True
	arg_48_0.selectPartner = False

	arg_48_0.updateSelectUI()

def var_0_0.updateSelectUI(arg_49_0):
	local var_49_0 = var_0_8.playerChar

	if var_49_0:
		local var_49_1 = findTF(arg_49_0.selectUI, "ad/player/icon/img")
		local var_49_2 = arg_49_0.getCharData(var_49_0, "icon")
		local var_49_3 = arg_49_0.getCharData(var_49_0, "pos")

		GetSpriteFromAtlasAsync("ui/minigameui/" .. var_0_5, var_49_2, function(arg_50_0)
			var_49_1.anchoredPosition = var_49_3

			setActive(var_49_1, True)
			setImageSprite(var_49_1, arg_50_0, True))
	else
		setActive(findTF(arg_49_0.selectUI, "ad/player/icon/img"), False)

	local var_49_4 = var_0_8.partnerChar

	if var_49_4:
		local var_49_5 = findTF(arg_49_0.selectUI, "ad/partner/icon/img")
		local var_49_6 = arg_49_0.getCharData(var_49_4, "icon")
		local var_49_7 = arg_49_0.getCharData(var_49_4, "pos")

		GetSpriteFromAtlasAsync("ui/minigameui/" .. var_0_5, var_49_6, function(arg_51_0)
			var_49_5.anchoredPosition = var_49_7

			setActive(var_49_5, True)
			setImageSprite(var_49_5, arg_51_0, True))
	else
		setActive(findTF(arg_49_0.selectUI, "ad/partner/icon/img"), False)

	if arg_49_0.selectPlayer:
		setActive(findTF(arg_49_0.selectUI, "ad/player/selected"), True)
		setActive(findTF(arg_49_0.selectUI, "ad/partner/selected"), False)
	elif arg_49_0.selectPartner:
		setActive(findTF(arg_49_0.selectUI, "ad/player/selected"), False)
		setActive(findTF(arg_49_0.selectUI, "ad/partner/selected"), True)

def var_0_0.selectChar(arg_52_0, arg_52_1):
	arg_52_0.selectCharId = arg_52_1

	for iter_52_0 = 1, #arg_52_0.selectChars:
		local var_52_0 = arg_52_0.selectChars[iter_52_0].data

		if var_52_0:
			local var_52_1 = arg_52_0.selectChars[iter_52_0].tf

			if var_52_0.id == arg_52_1:
				setActive(findTF(var_52_1, "selected"), True)
			else
				setActive(findTF(var_52_1, "selected"), False)

	if arg_52_0.selectPlayer:
		if var_0_8.partnerChar and var_0_8.partnerChar == arg_52_1:
			var_0_8.partnerChar = var_0_8.playerChar or None

		var_0_8.playerChar = arg_52_1

		if not var_0_8.partnerChar:
			arg_52_0.selectPlayer = False
			arg_52_0.selectPartner = True
	elif arg_52_0.selectPartner:
		if var_0_8.playerChar and var_0_8.playerChar == arg_52_1:
			var_0_8.playerChar = var_0_8.partnerChar

		var_0_8.partnerChar = arg_52_1

		if not var_0_8.playerChar:
			arg_52_0.selectPlayer = True
			arg_52_0.selectPartner = False

	if var_0_8.playerChar and CookGameConst.char_battle_data[var_0_8.playerChar].pet:
		var_0_8.partnerPet = CookGameConst.char_battle_data[var_0_8.playerChar].pet
	elif var_0_8.partnerChar and CookGameConst.char_battle_data[var_0_8.partnerChar].pet:
		var_0_8.partnerPet = CookGameConst.char_battle_data[var_0_8.partnerChar].pet
	else
		var_0_8.partnerPet = None

	arg_52_0.updateSelectUI()

def var_0_0.getCharDataById(arg_53_0, arg_53_1):
	for iter_53_0, iter_53_1 in pairs(CookGameConst.char_data):
		if iter_53_1.id == arg_53_1:
			return Clone(iter_53_1)

	return None

def var_0_0.getCharData(arg_54_0, arg_54_1, arg_54_2):
	for iter_54_0 = 1, #CookGameConst.char_data:
		local var_54_0 = CookGameConst.char_data[iter_54_0]

		if var_54_0.id == arg_54_1:
			if not arg_54_2:
				return Clone(var_54_0)
			else
				return Clone(var_54_0[arg_54_2])

	return None

def var_0_0.randomAIShip(arg_55_0):
	local var_55_0 = {}

	for iter_55_0, iter_55_1 in pairs(CookGameConst.char_battle_data):
		if iter_55_1.extend:
			table.insert(var_55_0, iter_55_1.id)

	if var_0_8.playerChar:
		table.insert(var_55_0, var_0_8.playerChar)

	if var_0_8.partnerChar:
		table.insert(var_55_0, var_0_8.partnerChar)

	local var_55_1 = Clone(CookGameConst.random_ids)

	for iter_55_2 = #var_55_1, 1, -1:
		if table.contains(var_55_0, var_55_1[iter_55_2]):
			table.remove(var_55_1, iter_55_2)

	var_0_8.enemy1Char = table.remove(var_55_1, math.random(1, #var_55_1))
	var_0_8.enemy2Char = table.remove(var_55_1, math.random(1, #var_55_1))
	var_0_8.enemyPet = CookGameConst.char_battle_data[var_0_8.enemy1Char].pet or CookGameConst.char_battle_data[var_0_8.enemy2Char].pet or None

def var_0_0.openMenuUI(arg_56_0):
	setActive(findTF(arg_56_0.sceneContainer, "scene_front"), False)
	setActive(findTF(arg_56_0.sceneContainer, "scene_background"), False)
	setActive(findTF(arg_56_0.sceneContainer, "scene"), False)
	setActive(arg_56_0.gameUI, False)
	setActive(arg_56_0.menuUI, True)
	setActive(arg_56_0.bg, True)
	arg_56_0.updateMenuUI()

def var_0_0.clearUI(arg_57_0):
	setActive(arg_57_0.sceneContainer, False)
	setActive(arg_57_0.settlementUI, False)
	setActive(arg_57_0.countUI, False)
	setActive(arg_57_0.menuUI, False)
	setActive(arg_57_0.gameUI, False)
	setActive(arg_57_0.selectUI, False)

def var_0_0.readyStart(arg_58_0):
	arg_58_0.readyStartFlag = True

	arg_58_0.controllerReady()
	setActive(arg_58_0.countUI, True)
	arg_58_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_2)

	arg_58_0.readyStartFlag = False

def var_0_0.gameStart(arg_59_0):
	setActive(findTF(arg_59_0.sceneContainer, "scene_front"), True)
	setActive(findTF(arg_59_0.sceneContainer, "scene_background"), True)
	setActive(findTF(arg_59_0.sceneContainer, "scene"), True)

	GetComponent(findTF(arg_59_0.sceneContainer, "scene"), typeof(CanvasGroup)).alpha = 1

	setActive(arg_59_0.bg, False)

	arg_59_0.sceneContainer.anchoredPosition = Vector2(0, 0)
	arg_59_0.offsetPosition = Vector2(0, 0)

	setActive(arg_59_0.gameUI, True)

	arg_59_0.gameStartFlag = True
	arg_59_0.scoreNum = 0
	arg_59_0.otherScoreNum = 0
	arg_59_0.gameStepTime = 0
	arg_59_0.gameTime = var_0_4
	arg_59_0.extendTime = None
	arg_59_0.waitingExtendTime = False

	if var_0_8.playerChar == 6 or var_0_8.partnerChar == 6:
		arg_59_0.waitingExtendTime = True

	for iter_59_0 = #arg_59_0.showScores, 1, -1:
		if not table.contains(arg_59_0.showScoresPool, arg_59_0.showScores[iter_59_0]):
			local var_59_0 = table.remove(arg_59_0.showScores, iter_59_0)

			table.insert(arg_59_0.showScoresPool, var_59_0)

	for iter_59_1 = #arg_59_0.showScoresPool, 1, -1:
		setActive(arg_59_0.showScoresPool[iter_59_1], False)

	local function var_59_1(arg_60_0, arg_60_1)
		local var_60_0 = arg_59_0.getCharData(arg_60_0, "icon")
		local var_60_1 = arg_59_0.getCharData(arg_60_0, "pos")

		GetSpriteFromAtlasAsync("ui/minigameui/" .. var_0_5, var_60_0, function(arg_61_0)
			setActive(arg_60_1, True)
			setImageSprite(arg_60_1, arg_61_0, True))

	var_59_1(var_0_8.playerChar, findTF(arg_59_0.gameUI, "top/leftCharPos/player/img"))
	var_59_1(var_0_8.partnerChar, findTF(arg_59_0.gameUI, "top/leftCharPos/partner/img"))
	var_59_1(var_0_8.enemy1Char, findTF(arg_59_0.gameUI, "top/rightCharPos/enemy1/img"))
	var_59_1(var_0_8.enemy2Char, findTF(arg_59_0.gameUI, "top/rightCharPos/enemy2/img"))
	arg_59_0.updateGameUI()
	arg_59_0.timerStart()
	arg_59_0.controllerStart()

def var_0_0.controllerReady(arg_62_0):
	GetComponent(findTF(arg_62_0.sceneContainer, "scene"), typeof(CanvasGroup)).alpha = 0

	setActive(findTF(arg_62_0.sceneContainer, "scene"), True)
	arg_62_0.charController.readyStart()

def var_0_0.controllerStart(arg_63_0):
	arg_63_0.judgesController.start()
	arg_63_0.charController.start()

def var_0_0.getGameTimes(arg_64_0):
	return arg_64_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_65_0):
	return arg_65_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_66_0):
	return arg_66_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_67_0):
	return (arg_67_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.changeSpeed(arg_68_0, arg_68_1):
	if arg_68_0.judgesController:
		arg_68_0.judgesController.changeSpeed(arg_68_1)

	if arg_68_0.charController:
		arg_68_0.charController.changeSpeed(arg_68_1)

def var_0_0.onTimer(arg_69_0):
	arg_69_0.gameStep()

def var_0_0.gameStep(arg_70_0):
	if arg_70_0.gameTime and arg_70_0.gameTime > 3 and arg_70_0.gameTime - Time.deltaTime < 3 and var_0_8.playerChar != 6 and var_0_8.playerChar != 6:
		arg_70_0.judgesController.timeUp()

	if arg_70_0.extendTime and arg_70_0.extendTime > 3 and arg_70_0.extendTime - Time.deltaTime < 3:
		arg_70_0.judgesController.timeUp()

	arg_70_0.gameTime = arg_70_0.gameTime - Time.deltaTime

	if arg_70_0.gameTime < 0:
		arg_70_0.gameTime = 0

	var_0_8.gameTime = arg_70_0.gameTime

	if arg_70_0.extendTime and arg_70_0.extendTime > 0:
		arg_70_0.extendTime = arg_70_0.extendTime - Time.deltaTime

		if arg_70_0.extendTime < 0:
			arg_70_0.extendTime = 0

	arg_70_0.gameStepTime = arg_70_0.gameStepTime + Time.deltaTime

	arg_70_0.controllerStep(Time.deltaTime)
	arg_70_0.updateGameUI()

	if not arg_70_0.waitingExtendTime and arg_70_0.gameTime <= 0:
		if arg_70_0.extendTime:
			if arg_70_0.extendTime <= 0:
				arg_70_0.onGameOver()
		else
			arg_70_0.onGameOver()

		return

def var_0_0.controllerStep(arg_71_0, arg_71_1):
	arg_71_0.judgesController.step(arg_71_1)
	arg_71_0.charController.step(arg_71_1)

def var_0_0.timerStart(arg_72_0):
	if not arg_72_0.timer.running:
		arg_72_0.timer.Start()

def var_0_0.timerStop(arg_73_0):
	if arg_73_0.timer.running:
		arg_73_0.timer.Stop()

def var_0_0.updateGameUI(arg_74_0):
	setText(arg_74_0.scoreTf, arg_74_0.scoreNum)
	setText(arg_74_0.otherScoreTf, arg_74_0.otherScoreNum)

	if arg_74_0.extendTime and arg_74_0.extendTime > 0:
		setText(arg_74_0.gameTimeS, math.ceil(arg_74_0.extendTime))
	else
		setText(arg_74_0.gameTimeS, math.ceil(arg_74_0.gameTime))

def var_0_0.addScore(arg_75_0, arg_75_1, arg_75_2):
	if arg_75_2:
		arg_75_0.otherScoreNum = arg_75_0.otherScoreNum + arg_75_1

		if arg_75_0.otherScoreNum < 0:
			arg_75_0.otherScoreNum = 0
	else
		arg_75_0.scoreNum = arg_75_0.scoreNum + arg_75_1

		if arg_75_0.scoreNum < 0:
			arg_75_0.scoreNum = 0

def var_0_0.onGameOver(arg_76_0):
	if arg_76_0.settlementFlag:
		return

	arg_76_0.timerStop()
	arg_76_0.controllerClear()

	arg_76_0.settlementFlag = True

	setActive(arg_76_0.clickMask, True)
	LeanTween.delayedCall(go(arg_76_0._tf), 0.1, System.Action(function()
		arg_76_0.settlementFlag = False
		arg_76_0.gameStartFlag = False

		setActive(arg_76_0.clickMask, False)
		arg_76_0.showSettlement()))

def var_0_0.showSettlement(arg_78_0):
	setActive(arg_78_0.settlementUI, True)
	GetComponent(findTF(arg_78_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_78_0 = arg_78_0.GetMGData().GetRuntimeData("elements")
	local var_78_1 = arg_78_0.scoreNum
	local var_78_2 = var_78_0 and #var_78_0 > 0 and var_78_0[1] or 0
	local var_78_3 = arg_78_0.otherScoreNum or 0

	setActive(findTF(arg_78_0.settlementUI, "ad/new"), var_78_2 < var_78_1)

	if var_78_2 <= var_78_1:
		var_78_2 = var_78_1

		arg_78_0.StoreDataToServer({
			var_78_2
		})

	local var_78_4 = findTF(arg_78_0.settlementUI, "ad/highText")
	local var_78_5 = findTF(arg_78_0.settlementUI, "ad/currentText")
	local var_78_6 = findTF(arg_78_0.settlementUI, "ad/otherText")

	setText(var_78_4, var_78_2)
	setText(var_78_5, var_78_1)
	setText(var_78_6, var_78_3)

	if arg_78_0.getGameTimes() and arg_78_0.getGameTimes() > 0:
		arg_78_0.sendSuccessFlag = True

		arg_78_0.SendSuccess(0)

	if var_78_3 < var_78_1:
		setActive(findTF(arg_78_0.settlementUI, "ad/win"), True)
		setActive(findTF(arg_78_0.settlementUI, "ad/defeat"), False)
	elif var_78_1 < var_78_3:
		setActive(findTF(arg_78_0.settlementUI, "ad/win"), False)
		setActive(findTF(arg_78_0.settlementUI, "ad/defeat"), True)
	else
		setActive(findTF(arg_78_0.settlementUI, "ad/win"), False)
		setActive(findTF(arg_78_0.settlementUI, "ad/defeat"), False)

	local var_78_7 = {}

	table.insert(var_78_7, {
		name = "player",
		char_id = var_0_8.playerChar
	})
	table.insert(var_78_7, {
		name = "partner",
		char_id = var_0_8.partnerChar
	})
	table.insert(var_78_7, {
		name = "enemy1",
		char_id = var_0_8.enemy1Char
	})
	table.insert(var_78_7, {
		name = "enemy2",
		char_id = var_0_8.enemy2Char
	})

	for iter_78_0 = 1, #var_78_7:
		local var_78_8 = var_78_7[iter_78_0].char_id
		local var_78_9 = findTF(arg_78_0.settlementUI, "ad/" .. var_78_7[iter_78_0].name)
		local var_78_10 = arg_78_0.getCharData(var_78_8, "icon")
		local var_78_11 = arg_78_0.getCharData(var_78_8, "pos")

		GetSpriteFromAtlasAsync("ui/minigameui/" .. var_0_5, var_78_10, function(arg_79_0)
			local var_79_0 = findTF(var_78_9, "mask/img")

			setActive(var_79_0, True)

			var_79_0.anchoredPosition = var_78_11

			setImageSprite(var_79_0, arg_79_0, True))

def var_0_0.OnApplicationPaused(arg_80_0):
	if not arg_80_0.gameStartFlag:
		return

	if arg_80_0.readyStartFlag:
		return

	if arg_80_0.settlementFlag:
		return

	if isActive(arg_80_0.pauseUI) or isActive(arg_80_0.leaveUI):
		return

	if not isActive(arg_80_0.pauseUI):
		setActive(arg_80_0.pauseUI, True)

	arg_80_0.stopGame()

def var_0_0.controllerClear(arg_81_0):
	arg_81_0.judgesController.clear()
	arg_81_0.charController.clear()

def var_0_0.resumeGame(arg_82_0):
	arg_82_0.gameStop = False

	setActive(arg_82_0.leaveUI, False)
	arg_82_0.changeSpeed(1)
	arg_82_0.timerStart()

def var_0_0.stopGame(arg_83_0):
	arg_83_0.gameStop = True

	arg_83_0.timerStop()
	arg_83_0.changeSpeed(0)

def var_0_0.onBackPressed(arg_84_0):
	if arg_84_0.readyStartFlag:
		return

	if not arg_84_0.gameStartFlag:
		arg_84_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_84_0.settlementFlag:
			return

		if isActive(arg_84_0.pauseUI):
			setActive(arg_84_0.pauseUI, False)

		arg_84_0.stopGame()
		setActive(arg_84_0.leaveUI, True)

def var_0_0.willExit(arg_85_0):
	if arg_85_0.handle:
		UpdateBeat.RemoveListener(arg_85_0.handle)

	if arg_85_0._tf and LeanTween.isTweening(go(arg_85_0._tf)):
		LeanTween.cancel(go(arg_85_0._tf))

	arg_85_0.destroyController()

	if arg_85_0.timer and arg_85_0.timer.running:
		arg_85_0.timer.Stop()

	arg_85_0.scrollRect.onValueChanged.RemoveAllListeners()

	Time.timeScale = 1
	arg_85_0.timer = None

def var_0_0.destroyController(arg_86_0):
	return

return var_0_0
