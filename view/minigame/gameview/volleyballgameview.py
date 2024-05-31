local var_0_0 = class("VolleyballGameView", import("..BaseMiniGameView"))
local var_0_1 = {
	"maliluosi_2_DOA",
	"suixiang_2_doa",
	"xia_2_DOA",
	"haixiao_2_DOA",
	"zhixiao_2_DOA",
	"nvtiangou_2_DOA",
	"monika_2_DOA"
}
local var_0_2 = {
	10600010,
	10600020,
	10600030,
	10600040,
	10600050,
	10600060,
	10600070
}
local var_0_3 = 1
local var_0_4 = 2
local var_0_5 = -1
local var_0_6 = 0
local var_0_7 = 0.35
local var_0_8 = 0.15
local var_0_9 = 0
local var_0_10 = 1
local var_0_11 = 2
local var_0_12 = 0
local var_0_13 = 1
local var_0_14 = 2
local var_0_15 = 1.5
local var_0_16 = 1
local var_0_17 = 0.5
local var_0_18 = 0.5
local var_0_19 = 0.43
local var_0_20 = 0.5
local var_0_21 = 0.76
local var_0_22 = 0.83
local var_0_23 = -30
local var_0_24 = 50
local var_0_25 = 60
local var_0_26 = 230
local var_0_27 = 60
local var_0_28 = "event./ui/ddldaoshu2"
local var_0_29 = "event./ui/fighterplane_click"
local var_0_30 = "event./ui/jieqiu"
local var_0_31 = "event./ui/kouqiu"
local var_0_32 = 0.8
local var_0_33 = -1000

def var_0_0.getUIName(arg_1_0):
	return "VolleyballGameUI"

def var_0_0.init(arg_2_0):
	arg_2_0.countTimeUI = arg_2_0.findTF("count_time_ui")
	arg_2_0.countTimeImage = arg_2_0.findTF("time", arg_2_0.countTimeUI)
	arg_2_0.countTimeNumImage = arg_2_0.findTF("nums", arg_2_0.countTimeUI)
	arg_2_0.mainUI = arg_2_0.findTF("main_ui")
	arg_2_0.returnBtn = arg_2_0.findTF("return_btn", arg_2_0.mainUI)
	arg_2_0.mainStartBtn = arg_2_0.findTF("start_btn", arg_2_0.mainUI)
	arg_2_0.ruleBtn = arg_2_0.findTF("rule_btn", arg_2_0.mainUI)
	arg_2_0.progressScroll = arg_2_0.findTF("right_panel/scroll_view/", arg_2_0.mainUI)
	arg_2_0.progressContent = arg_2_0.findTF("right_panel/scroll_view/viewport/content", arg_2_0.mainUI)
	arg_2_0.colors = arg_2_0.findTF("right_panel/colors", arg_2_0.mainUI)
	arg_2_0.icons = arg_2_0.findTF("right_panel/icons", arg_2_0.mainUI)
	arg_2_0.gotIcon = arg_2_0.findTF("bg/got", arg_2_0.mainUI)
	arg_2_0.selectUI = arg_2_0.findTF("select_ui")
	arg_2_0.selectBackBtn = arg_2_0.findTF("back_btn", arg_2_0.selectUI)
	arg_2_0.selectStartBtn = arg_2_0.findTF("start_btn", arg_2_0.selectUI)
	arg_2_0.tags = arg_2_0.findTF("select_panel/tags", arg_2_0.selectUI)
	arg_2_0.paints = arg_2_0.findTF("select_panel/paints", arg_2_0.selectUI)
	arg_2_0.freeTitle = arg_2_0.findTF("select_panel/title/free", arg_2_0.selectUI)
	arg_2_0.dayTitle = arg_2_0.findTF("select_panel/title/challenge", arg_2_0.selectUI)
	arg_2_0.titleDayNum = arg_2_0.findTF("select_panel/title/challenge/num", arg_2_0.selectUI)
	arg_2_0.ruleTxt = arg_2_0.findTF("select_panel/rule/rule_txt", arg_2_0.selectUI)
	arg_2_0.select4Chars = arg_2_0.findTF("select_panel/chars", arg_2_0.selectUI)
	arg_2_0.selectWindow = arg_2_0.findTF("select_windows", arg_2_0.selectUI)
	arg_2_0.selectSureBtn = arg_2_0.findTF("windows/sure_btn", arg_2_0.selectWindow)
	arg_2_0.select9Chars = arg_2_0.findTF("windows/char_layout", arg_2_0.selectWindow)
	arg_2_0.selectNum = arg_2_0.findTF("windows/tips/num", arg_2_0.selectWindow)
	arg_2_0.gameUI = arg_2_0.findTF("game_ui")
	arg_2_0.bgEffect = arg_2_0.findTF("bg/shatanpaiqiu_hailang", arg_2_0.gameUI)
	arg_2_0.hitEffect = arg_2_0.findTF("shatanpaiqiu_jida", arg_2_0.gameUI)
	arg_2_0.upEffect = arg_2_0.findTF("shatanpaiqiu_jieqiu", arg_2_0.gameUI)
	arg_2_0.ball = arg_2_0.findTF("ball", arg_2_0.gameUI)
	arg_2_0.ballShadow = arg_2_0.findTF("ball_shadow", arg_2_0.gameUI)
	arg_2_0.pauseBtn = arg_2_0.findTF("pause_btn", arg_2_0.gameUI)
	arg_2_0.backBtn = arg_2_0.findTF("back_btn", arg_2_0.gameUI)
	arg_2_0.qteBtn = arg_2_0.findTF("qte_btn", arg_2_0.gameUI)
	arg_2_0.pos = arg_2_0.findTF("pos", arg_2_0.gameUI)

	arg_2_0.initPos()

	arg_2_0.ourScore = arg_2_0.findTF("score/our", arg_2_0.gameUI)
	arg_2_0.enemyScore = arg_2_0.findTF("score/enemy", arg_2_0.gameUI)
	arg_2_0.qte = arg_2_0.findTF("qte", arg_2_0.gameUI)
	arg_2_0.qteCircles = arg_2_0.findTF("circles", arg_2_0.qte)
	arg_2_0.qteCircle = arg_2_0.findTF("circles/big", arg_2_0.qte)
	arg_2_0.result = arg_2_0.findTF("result", arg_2_0.qte)
	arg_2_0.resultTxt = arg_2_0.findTF("txts", arg_2_0.qte)
	arg_2_0.cutin = arg_2_0.findTF("cutin", arg_2_0.gameUI)
	arg_2_0.cutinPaint = arg_2_0.findTF("cutin/paint", arg_2_0.gameUI)
	arg_2_0.cutinPaints = arg_2_0.findTF("cutin_paints", arg_2_0.gameUI)
	arg_2_0.scoreCutin = arg_2_0.findTF("score_cutin", arg_2_0.gameUI)
	arg_2_0.scoreCutinNums = arg_2_0.findTF("score_cutin/nums", arg_2_0.gameUI)
	arg_2_0.ourScoreCutin = arg_2_0.findTF("score_cutin/our", arg_2_0.gameUI)
	arg_2_0.enemyScoreCutin = arg_2_0.findTF("score_cutin/enemy", arg_2_0.gameUI)
	arg_2_0.charTF = {}
	arg_2_0.charTF.our1 = arg_2_0.findTF("char/our1", arg_2_0.gameUI)
	arg_2_0.charTF.our2 = arg_2_0.findTF("char/our2", arg_2_0.gameUI)
	arg_2_0.charTF.enemy1 = arg_2_0.findTF("char/enemy1", arg_2_0.gameUI)
	arg_2_0.charTF.enemy2 = arg_2_0.findTF("char/enemy2", arg_2_0.gameUI)
	arg_2_0.charModels = {}
	arg_2_0.charactor = {}
	arg_2_0.cutinMask = arg_2_0.findTF("cutin_mask", arg_2_0.gameUI)
	arg_2_0.endUI = arg_2_0.findTF("end_ui")
	arg_2_0.endDayTitle = arg_2_0.findTF("title/race", arg_2_0.endUI)
	arg_2_0.endFreeTitle = arg_2_0.findTF("title/free", arg_2_0.endUI)
	arg_2_0.endTitleDay = arg_2_0.findTF("title/race/num", arg_2_0.endUI)
	arg_2_0.titleDays = arg_2_0.findTF("title_days", arg_2_0.endUI)
	arg_2_0.endOurScore = arg_2_0.findTF("score_panel/score/our", arg_2_0.endUI)
	arg_2_0.endEnemyScore = arg_2_0.findTF("score_panel/score/enemy", arg_2_0.endUI)
	arg_2_0.endScoreNums = arg_2_0.findTF("nums", arg_2_0.endUI)
	arg_2_0.sureBtn = arg_2_0.findTF("sure_btn", arg_2_0.endUI)
	arg_2_0.winTag = arg_2_0.findTF("score_panel/score/win", arg_2_0.endUI)
	arg_2_0.loseTag = arg_2_0.findTF("score_panel/score/lose", arg_2_0.endUI)
	arg_2_0.helpUI = arg_2_0.findTF("help_ui")

def var_0_0.initPos(arg_3_0):
	arg_3_0.orgPos = {}
	arg_3_0.orgPos.our_serve = arg_3_0.findTF("our_pos/serve_pos", arg_3_0.pos).anchoredPosition
	arg_3_0.orgPos.our1 = arg_3_0.findTF("our_pos/drop_pos1", arg_3_0.pos).anchoredPosition
	arg_3_0.orgPos.our2 = arg_3_0.findTF("our_pos/drop_pos2", arg_3_0.pos).anchoredPosition
	arg_3_0.orgPos.enemy_serve = arg_3_0.findTF("enemy_pos/serve_pos", arg_3_0.pos).anchoredPosition
	arg_3_0.orgPos.enemy1 = arg_3_0.findTF("enemy_pos/drop_pos1", arg_3_0.pos).anchoredPosition
	arg_3_0.orgPos.enemy2 = arg_3_0.findTF("enemy_pos/drop_pos2", arg_3_0.pos).anchoredPosition

	arg_3_0.resetPos()

def var_0_0.resetPos(arg_4_0):
	arg_4_0.anchoredPos = Clone(arg_4_0.orgPos)
	arg_4_0.anchoredPos.our1 = arg_4_0.getRandomPos("our1")
	arg_4_0.anchoredPos.our2 = arg_4_0.getRandomPos("our2")
	arg_4_0.anchoredPos.enemy1 = arg_4_0.getRandomPos("enemy1")
	arg_4_0.anchoredPos.enemy2 = arg_4_0.getRandomPos("enemy2")

def var_0_0.didEnter(arg_5_0):
	onButton(arg_5_0, arg_5_0.returnBtn, function()
		arg_5_0.emit(var_0_0.ON_BACK), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.ruleBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("venusvolleyball_help")
		}), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.mainStartBtn, function()
		setActive(arg_5_0.selectUI, True)
		pg.UIMgr.GetInstance().BlurPanel(arg_5_0.selectUI)
		arg_5_0.initSelectUI(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.selectBackBtn, function()
		setActive(arg_5_0.selectUI, False)
		pg.UIMgr.GetInstance().UnblurPanel(arg_5_0.selectUI, arg_5_0._tf), SFX_PANEL)

	arg_5_0.canStartGame = False

	onButton(arg_5_0, arg_5_0.selectStartBtn, function()
		if not arg_5_0.canStartGame:
			return

		setActive(arg_5_0.mainUI, False)
		setActive(arg_5_0.selectUI, False)
		pg.UIMgr.GetInstance().UnblurPanel(arg_5_0.selectUI, arg_5_0._tf)
		setActive(arg_5_0.gameUI, True)
		arg_5_0.resetGameData()

		if arg_5_0.isFirstgame == 0:
			arg_5_0.firstShow(function()
				arg_5_0.startCountTimer())
		else
			arg_5_0.startCountTimer(), SFX_PANEL)

	arg_5_0.canSureChar = False

	onButton(arg_5_0, arg_5_0.selectSureBtn, function()
		if not arg_5_0.canSureChar:
			return

		if arg_5_0.selectCharCamp == "enemy":
			arg_5_0.charNames.enemy1 = var_0_1[arg_5_0.selectSDIndex1]
			arg_5_0.charNames.enemy2 = var_0_1[arg_5_0.selectSDIndex2]
		elif arg_5_0.selectCharCamp == "our":
			arg_5_0.charNames.our1 = var_0_1[arg_5_0.selectSDIndex1]
			arg_5_0.charNames.our2 = var_0_1[arg_5_0.selectSDIndex2]

		setActive(arg_5_0.selectWindow, False)
		arg_5_0.refreshSelectUI(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.findTF("mask", arg_5_0.selectWindow), function()
		setActive(arg_5_0.selectWindow, False), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.pauseBtn, function()
		if not arg_5_0.btnAvailable:
			return

		arg_5_0.pauseGame()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			content = i18n("venusvolleyball_suspend_tip"),
			def onNo:()
				arg_5_0.resumeGame(),
			def onYes:()
				arg_5_0.resumeGame()
		}), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.backBtn, function()
		if not arg_5_0.btnAvailable:
			return

		arg_5_0.pauseGame()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("venusvolleyball_return_tip"),
			def onNo:()
				arg_5_0.resumeGame(),
			def onYes:()
				arg_5_0.endGame()
		}), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.qteBtn, function()
		if arg_5_0.qteBtnStatus == var_0_5:
			return

		arg_5_0.qteResult())
	onButton(arg_5_0, arg_5_0.sureBtn, function()
		setActive(arg_5_0.mainUI, True)
		arg_5_0.initMainUI()
		setActive(arg_5_0.gameUI, False)
		setActive(arg_5_0.endUI, False)
		arg_5_0.clearSpineChars()
		pg.UIMgr.GetInstance().UnblurPanel(arg_5_0.endUI, arg_5_0._tf), SFX_PANEL)
	arg_5_0.initMainUI()

def var_0_0.playEffect(arg_22_0, arg_22_1, arg_22_2):
	if arg_22_2:
		arg_22_1.anchoredPosition = arg_22_2
	else
		arg_22_1.anchoredPosition = arg_22_0.ball.anchoredPosition

	setActive(arg_22_1, False)
	setActive(arg_22_1, True)

def var_0_0.getGameData(arg_23_0):
	arg_23_0.mgProxy = getProxy(MiniGameProxy)
	arg_23_0.hubData = arg_23_0.mgProxy.GetHubByHubId(13)
	arg_23_0.curDay = arg_23_0.hubData.ultimate == 0 and arg_23_0.hubData.usedtime + 1 or 8
	arg_23_0.unlockDay = arg_23_0.hubData.usedtime + arg_23_0.hubData.count
	arg_23_0.curDay = arg_23_0.curDay <= arg_23_0.unlockDay and arg_23_0.curDay or arg_23_0.unlockDay
	arg_23_0.mgData = arg_23_0.mgProxy.GetMiniGameData(17)
	arg_23_0.endScore = arg_23_0.mgData.GetSimpleValue("endScore")[arg_23_0.curDay]
	arg_23_0.storylist = arg_23_0.mgData.GetSimpleValue("story")

	local var_23_0 = getProxy(PlayerProxy).getData().id

	arg_23_0.isFirstgame = PlayerPrefs.GetInt("volleyballgame_first_" .. var_23_0)

def var_0_0.getEnemyCharsIndex(arg_24_0):
	return arg_24_0.mgData.GetSimpleValue("mainChar")[arg_24_0.curDay], arg_24_0.mgData.GetSimpleValue("minorChar")[arg_24_0.curDay]

def var_0_0.initMainUI(arg_25_0):
	arg_25_0.isInGame = False

	arg_25_0.getGameData()

	if arg_25_0.hubData.ultimate == 0 and arg_25_0.hubData.usedtime >= arg_25_0.hubData.getConfig("reward_need"):
		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_25_0.hubData.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})

	arg_25_0.isFree = arg_25_0.hubData.ultimate != 0 and True or False

	setActive(arg_25_0.findTF("free_tag", arg_25_0.mainStartBtn), arg_25_0.isFree)
	setActive(arg_25_0.gotIcon, arg_25_0.isFree)
	eachChild(arg_25_0.progressContent, function(arg_26_0)
		local var_26_0 = ""
		local var_26_1 = tonumber(arg_26_0.name)
		local var_26_2 = var_0_1[arg_25_0.mgData.GetSimpleValue("mainChar")[var_26_1]]

		setActive(arg_25_0.findTF("char_bg/mask", arg_26_0), False)
		setActive(arg_25_0.findTF("name_bg/mask", arg_26_0), False)
		setActive(arg_25_0.findTF("pass", arg_26_0), False)

		if var_26_1 == arg_25_0.curDay and arg_25_0.hubData.count > 0:
			var_26_0 = "red"

			setImageSprite(arg_25_0.findTF("char_bg/icon", arg_26_0), arg_25_0.icons.Find(arg_25_0.getCharIndex(var_26_2)).GetComponent(typeof(Image)).sprite, True)
		elif var_26_1 < arg_25_0.curDay or var_26_1 == arg_25_0.curDay and arg_25_0.hubData.count == 0:
			var_26_0 = "grey"

			setImageSprite(arg_25_0.findTF("char_bg/icon", arg_26_0), arg_25_0.icons.Find(arg_25_0.getCharIndex(var_26_2)).GetComponent(typeof(Image)).sprite, True)
			setActive(arg_25_0.findTF("char_bg/mask", arg_26_0), True)
			setActive(arg_25_0.findTF("name_bg/mask", arg_26_0), True)
			setActive(arg_25_0.findTF("pass", arg_26_0), True)
		elif var_26_1 > arg_25_0.curDay and var_26_1 <= arg_25_0.unlockDay:
			var_26_0 = "blue"

			setImageSprite(arg_25_0.findTF("char_bg/icon", arg_26_0), arg_25_0.icons.Find(arg_25_0.getCharIndex(var_26_2)).GetComponent(typeof(Image)).sprite, True)
		else
			var_26_0 = "grey"

			setImageSprite(arg_25_0.findTF("char_bg/icon", arg_26_0), arg_25_0.colors.Find("unkonwn").GetComponent(typeof(Image)).sprite)

		setImageSprite(arg_25_0.findTF("name_bg", arg_26_0), arg_25_0.colors.Find(var_26_0).GetComponent(typeof(Image)).sprite))

	local var_25_0 = 215
	local var_25_1 = math.min(645, (arg_25_0.curDay - 1) * var_25_0)

	arg_25_0.progressContent.anchoredPosition = {
		x = 0,
		y = var_25_1
	}

	onScroll(arg_25_0, arg_25_0.progressScroll, function(arg_27_0)
		setActive(arg_25_0.findTF("right_panel/arraws_up", arg_25_0.mainUI), arg_27_0.y < 1 and True or False)
		setActive(arg_25_0.findTF("right_panel/arraws_down", arg_25_0.mainUI), arg_27_0.y > 0 and True or False))

def var_0_0.initSelectUI(arg_28_0):
	setActive(arg_28_0.freeTitle, arg_28_0.isFree)
	setActive(arg_28_0.dayTitle, not arg_28_0.isFree)
	setText(arg_28_0.titleDayNum, arg_28_0.curDay)
	setText(arg_28_0.ruleTxt, i18n("venusvolleyball_rule_tip", arg_28_0.endScore))

	arg_28_0.charNames = {}
	arg_28_0.lastSelectNames = {}

	eachChild(arg_28_0.select4Chars, function(arg_29_0)
		local var_29_0 = arg_29_0.name

		onButton(arg_28_0, arg_29_0, function()
			if not arg_28_0.isFree and string.find(var_29_0, "enemy"):
				return

			arg_28_0.selectCharCamp = string.find(var_29_0, "enemy") and "enemy" or "our"

			arg_28_0.openSelectWindow()))

	if not arg_28_0.isFree:
		local var_28_0, var_28_1 = arg_28_0.getEnemyCharsIndex()

		arg_28_0.charNames.enemy1, arg_28_0.charNames.enemy2 = var_0_1[var_28_0], var_0_1[var_28_1]

	arg_28_0.refreshSelectUI()

def var_0_0.getCharIndex(arg_31_0, arg_31_1):
	for iter_31_0, iter_31_1 in ipairs(var_0_1):
		if iter_31_1 == arg_31_1:
			return iter_31_0

	return 1

def var_0_0.refreshSelectUI(arg_32_0):
	eachChild(arg_32_0.select4Chars, function(arg_33_0)
		local var_33_0 = arg_33_0.name

		if arg_32_0.charNames[var_33_0]:
			setActive(arg_32_0.findTF("select_btn", arg_33_0), False)
			setActive(arg_32_0.findTF("char", arg_33_0), True)
			setImageSprite(arg_32_0.findTF("char/icon", arg_33_0), arg_32_0.paints.Find(arg_32_0.getCharIndex(arg_32_0.charNames[var_33_0])).GetComponent(typeof(Image)).sprite, True)
			setImageSprite(arg_32_0.findTF("char/tag", arg_33_0), arg_32_0.tags.Find(arg_32_0.getCharIndex(arg_32_0.charNames[var_33_0])).GetComponent(typeof(Image)).sprite, True)
		else
			setActive(arg_32_0.findTF("select_btn", arg_33_0), True)
			setActive(arg_32_0.findTF("char", arg_33_0), False))

	arg_32_0.canStartGame = arg_32_0.charNames.our1 and arg_32_0.charNames.our2 and arg_32_0.charNames.enemy1 and arg_32_0.charNames.enemy2 and True or False

	setGray(arg_32_0.selectStartBtn, not arg_32_0.canStartGame, not arg_32_0.canStartGame)

def var_0_0.isSelected(arg_34_0, arg_34_1, arg_34_2):
	local var_34_0 = False

	for iter_34_0, iter_34_1 in pairs(arg_34_0.charNames):
		if arg_34_1 == iter_34_1:
			var_34_0 = not string.find(iter_34_0, arg_34_2) and True or False

	return var_34_0

def var_0_0.openSelectWindow(arg_35_0):
	setActive(arg_35_0.selectWindow, True)

	arg_35_0.hasSelectNum = 0

	setText(arg_35_0.selectNum, setColorStr(arg_35_0.hasSelectNum, COLOR_GREEN) .. "/2")

	arg_35_0.selectSDIndex1 = None
	arg_35_0.selectSDIndex2 = None

	eachChild(arg_35_0.select9Chars, function(arg_36_0)
		local var_36_0 = tonumber(arg_36_0.name)

		setImageSprite(arg_35_0.findTF("char/frame/icon", arg_36_0), arg_35_0.icons.Find(var_36_0).GetComponent(typeof(Image)).sprite, True)
		onButton(arg_35_0, arg_36_0, function()
			if arg_35_0.isSelected(var_0_1[var_36_0], arg_35_0.selectCharCamp):
				return

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_29)

			if isActive(arg_35_0.findTF("selected", arg_36_0)):
				setActive(arg_35_0.findTF("selected", arg_36_0), False)

				if arg_35_0.selectSDIndex1 and arg_35_0.selectSDIndex1 == var_36_0:
					arg_35_0.selectSDIndex1 = None

				if arg_35_0.selectSDIndex2 and arg_35_0.selectSDIndex2 == var_36_0:
					arg_35_0.selectSDIndex2 = None

				arg_35_0.hasSelectNum = arg_35_0.hasSelectNum - 1
			elif arg_35_0.selectSDIndex1 and arg_35_0.selectSDIndex2:
				-- block empty
			elif arg_35_0.selectSDIndex1:
				arg_35_0.selectSDIndex2 = var_36_0
				arg_35_0.hasSelectNum = arg_35_0.hasSelectNum + 1
			else
				arg_35_0.selectSDIndex1 = var_36_0
				arg_35_0.hasSelectNum = arg_35_0.hasSelectNum + 1

			arg_35_0.refreshSelectWindow()))
	arg_35_0.refreshSelectWindow()

def var_0_0.refreshSelectWindow(arg_38_0):
	eachChild(arg_38_0.select9Chars, function(arg_39_0)
		local var_39_0 = tonumber(arg_39_0.name)

		setActive(arg_38_0.findTF("char/mask", arg_39_0), arg_38_0.isSelected(var_0_1[var_39_0], arg_38_0.selectCharCamp) and True or False)

		if var_39_0 == arg_38_0.selectSDIndex1 or var_39_0 == arg_38_0.selectSDIndex2:
			setActive(arg_38_0.findTF("selected", arg_39_0), True)
		else
			setActive(arg_38_0.findTF("selected", arg_39_0), False))
	setText(arg_38_0.selectNum, setColorStr(arg_38_0.hasSelectNum, COLOR_GREEN) .. "/2")

	arg_38_0.canSureChar = arg_38_0.selectSDIndex1 and arg_38_0.selectSDIndex2 and True or False

	setGray(arg_38_0.selectSureBtn, not arg_38_0.canSureChar, not arg_38_0.canSureChar)

def var_0_0.firstShow(arg_40_0, arg_40_1):
	setActive(arg_40_0.helpUI, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_40_0.helpUI)
	onButton(arg_40_0, arg_40_0.helpUI, function()
		local var_41_0 = getProxy(PlayerProxy).getData().id

		PlayerPrefs.SetInt("volleyballgame_first_" .. var_41_0, 1)
		setActive(arg_40_0.helpUI, False)
		pg.UIMgr.GetInstance().UnblurPanel(arg_40_0.helpUI, arg_40_0._tf)

		if arg_40_1:
			arg_40_1(), SFX_PANEL)

def var_0_0.startCountTimer(arg_42_0):
	arg_42_0.setBtnAvailable(False)
	setActive(arg_42_0.countTimeUI, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_42_0.countTimeUI)

	arg_42_0.countTime = 3

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_28)
	setImageSprite(arg_42_0.countTimeImage, arg_42_0.countTimeNumImage.Find(arg_42_0.countTime).GetComponent(typeof(Image)).sprite)

	local function var_42_0()
		arg_42_0.countTime = arg_42_0.countTime - 1

		if arg_42_0.countTime <= 0:
			setActive(arg_42_0.countTimeUI, False)
			pg.UIMgr.GetInstance().UnblurPanel(arg_42_0.countTimeUI, arg_42_0._tf)
			arg_42_0.resetGameAni()
			arg_42_0.startGame()
		else
			setImageSprite(arg_42_0.countTimeImage, arg_42_0.countTimeNumImage.Find(arg_42_0.countTime).GetComponent(typeof(Image)).sprite)

	if arg_42_0.countTimer:
		arg_42_0.countTimer.Reset(var_42_0, 1, -1)
	else
		arg_42_0.countTimer = Timer.New(var_42_0, 1, -1)

	arg_42_0.countTimer.Start()

def var_0_0.setBtnAvailable(arg_44_0, arg_44_1):
	arg_44_0.btnAvailable = arg_44_1

	setGray(arg_44_0.backBtn, not arg_44_1, not arg_44_1)
	setGray(arg_44_0.pauseBtn, not arg_44_1, not arg_44_1)

def var_0_0.startGame(arg_45_0):
	arg_45_0.isInGame = True

	arg_45_0.setBtnAvailable(True)
	setActive(arg_45_0.bgEffect, False)
	setActive(arg_45_0.bgEffect, True)

	if arg_45_0.beginTeam == var_0_3:
		arg_45_0.ourServe(function()
			arg_45_0.enemyUp2Up(function()
				arg_45_0.enemyUp2Hit(function()
					arg_45_0.enemyThrow(function()
						arg_45_0.enterLoop()))))
	else
		arg_45_0.enemyServe(function()
			arg_45_0.enterLoop())

def var_0_0.enterLoop(arg_51_0):
	arg_51_0.ourUp2Up(function()
		arg_51_0.ourUp2Hit(function()
			arg_51_0.ourThrow(function()
				arg_51_0.enemyUp2Up(function()
					arg_51_0.enemyUp2Hit(function()
						arg_51_0.enemyThrow(function()
							arg_51_0.enterLoop()))))))

def var_0_0.ourServe(arg_58_0, arg_58_1):
	arg_58_0.ballPosTag = "our_serve"

	setActive(arg_58_0.ball, True)
	arg_58_0.charServeBall()
	arg_58_0.managedTween(LeanTween.delayedCall, function()
		local var_59_0 = "enemy" .. math.random(2)

		arg_58_0.ballPosTag = var_59_0
		arg_58_0.anchoredPos[arg_58_0.ballPosTag] = arg_58_0.getRandomPos(arg_58_0.ballPosTag)

		arg_58_0.ballServe(arg_58_0.ball, var_0_15, arg_58_0.anchoredPos[var_59_0], function()
			if arg_58_1:
				arg_58_1())
		arg_58_0.managedTween(LeanTween.delayedCall, function()
			arg_58_0.charUpBall(), var_0_15 - var_0_21, None), var_0_20 + 0.5, None)

def var_0_0.enemyServe(arg_62_0, arg_62_1):
	arg_62_0.ballPosTag = "enemy_serve"

	setActive(arg_62_0.ball, True)
	arg_62_0.charServeBall()
	arg_62_0.managedTween(LeanTween.delayedCall, function()
		local var_63_0 = "our" .. math.random(2)

		arg_62_0.ballPosTag = var_63_0
		arg_62_0.anchoredPos[arg_62_0.ballPosTag] = arg_62_0.getRandomPos(arg_62_0.ballPosTag)

		arg_62_0.ballServe(arg_62_0.ball, var_0_15, arg_62_0.anchoredPos[var_63_0], function()
			if arg_62_1:
				arg_62_1())
		arg_62_0.managedTween(LeanTween.delayedCall, function()
			arg_62_0.charUpBall(), var_0_15 - var_0_21, None), var_0_20 + 0.5, None)

def var_0_0.ourUp2Up(arg_66_0, arg_66_1):
	if arg_66_0.qteStatus == var_0_11 and arg_66_0.qteType == var_0_13:
		arg_66_0.ourFly()

		return

	arg_66_0.ballPosTag = arg_66_0.ballPosTag == "our1" and "our2" or "our1"

	arg_66_0.ballUp2Up(arg_66_0.ball, var_0_16, arg_66_0.anchoredPos[arg_66_0.ballPosTag], function()
		if arg_66_1:
			arg_66_1())
	arg_66_0.managedTween(LeanTween.delayedCall, function()
		arg_66_0.charUpBall(), 0.3, None)

def var_0_0.ourUp2Hit(arg_69_0, arg_69_1):
	local var_69_0 = {}

	arg_69_0.ballPosTag = arg_69_0.ballPosTag == "our1" and "our2" or "our1"
	arg_69_0.anchoredPos[arg_69_0.ballPosTag] = arg_69_0.getRandomPos(arg_69_0.ballPosTag)
	arg_69_0.qteType = var_0_14

	arg_69_0.charHitBall()

	local var_69_1 = False

	local function var_69_2(arg_70_0)
		if var_69_1:
			arg_70_0()
		else
			var_69_1 = True

	table.insert(var_69_0, function(arg_71_0)
		local function var_71_0()
			if arg_69_0.isCutin:
				arg_69_0.showcutin(function()
					arg_69_0.isCutin = False

					arg_71_0())
			else
				arg_71_0()

		arg_69_0.managedTween(LeanTween.delayedCall, function()
			var_69_2(var_71_0), var_0_16 - 0.2, None)
		arg_69_0.managedTween(LeanTween.delayedCall, function()
			arg_69_0.startQTE(var_0_32, 200, arg_69_0.anchoredPos[arg_69_0.ballPosTag], function()
				var_69_2(var_71_0)), var_0_16 - var_0_32 - 0.2, None))
	table.insert(var_69_0, function(arg_77_0)
		arg_69_0.ballUp2Hit(arg_69_0.ball, var_0_16, arg_69_0.anchoredPos[arg_69_0.ballPosTag], arg_77_0))
	parallelAsync(var_69_0, function()
		if arg_69_1:
			arg_69_1())

def var_0_0.ourThrow(arg_79_0, arg_79_1):
	local var_79_0 = "enemy" .. math.random(2)

	arg_79_0.ballPosTag = var_79_0
	arg_79_0.anchoredPos[arg_79_0.ballPosTag] = arg_79_0.getRandomPos(arg_79_0.ballPosTag)

	arg_79_0.ballHit(arg_79_0.ball, var_0_17, arg_79_0.anchoredPos[var_79_0], function()
		if arg_79_1:
			arg_79_1())
	arg_79_0.charUpBall()

def var_0_0.enemyUp2Up(arg_81_0, arg_81_1):
	if arg_81_0.qteStatus == var_0_10 and arg_81_0.qteType == var_0_14:
		arg_81_0.enemyFly()

		return

	arg_81_0.ballPosTag = arg_81_0.ballPosTag == "enemy1" and "enemy2" or "enemy1"

	arg_81_0.ballUp2Up(arg_81_0.ball, var_0_16, arg_81_0.anchoredPos[arg_81_0.ballPosTag], function()
		if arg_81_1:
			arg_81_1())
	arg_81_0.managedTween(LeanTween.delayedCall, function()
		arg_81_0.charUpBall(), 0.3, None)

def var_0_0.enemyUp2Hit(arg_84_0, arg_84_1):
	arg_84_0.ballPosTag = arg_84_0.ballPosTag == "enemy1" and "enemy2" or "enemy1"
	arg_84_0.anchoredPos[arg_84_0.ballPosTag] = arg_84_0.getRandomPos(arg_84_0.ballPosTag)
	arg_84_0.randomQtePos = "our" .. math.random(2)
	arg_84_0.anchoredPos[arg_84_0.randomQtePos] = arg_84_0.getRandomPos(arg_84_0.randomQtePos)
	arg_84_0.qteType = var_0_13

	arg_84_0.managedTween(LeanTween.delayedCall, function()
		arg_84_0.startQTE(var_0_32, 0, arg_84_0.anchoredPos[arg_84_0.randomQtePos]), var_0_16 - var_0_32, None)
	arg_84_0.ballUp2Hit(arg_84_0.ball, var_0_16, arg_84_0.anchoredPos[arg_84_0.ballPosTag], function()
		if arg_84_1:
			arg_84_1())
	arg_84_0.charHitBall()

def var_0_0.enemyThrow(arg_87_0, arg_87_1):
	arg_87_0.ballPosTag = arg_87_0.randomQtePos

	arg_87_0.ballHit(arg_87_0.ball, var_0_17, arg_87_0.anchoredPos[arg_87_0.ballPosTag], function()
		if arg_87_1:
			arg_87_1())
	arg_87_0.charUpBall()

def var_0_0.ourFly(arg_89_0):
	arg_89_0.ballPosTag = "out"

	local var_89_0 = math.random(1000, 1100)
	local var_89_1 = math.random(0, 200)

	arg_89_0.hitFly(arg_89_0.ball, var_0_18, {
		x = -var_89_0,
		y = var_89_1 - 100
	}, function()
		arg_89_0.qteStatus = var_0_9

		setGray(arg_89_0.qteBtn, True, True)

		arg_89_0.enemyScoreNum = arg_89_0.enemyScoreNum + 1

		arg_89_0.updateScore())

def var_0_0.enemyFly(arg_91_0):
	arg_91_0.ballPosTag = "out"

	local var_91_0 = math.random(1000, 1100)
	local var_91_1 = math.random(0, 200)

	arg_91_0.hitFly(arg_91_0.ball, var_0_18, {
		x = var_91_0,
		y = var_91_1 - 100
	}, function()
		arg_91_0.qteStatus = var_0_9

		setGray(arg_91_0.qteBtn, True, True)

		arg_91_0.ourScoreNum = arg_91_0.ourScoreNum + 1

		arg_91_0.updateScore())

def var_0_0.qteSuccess(arg_93_0):
	arg_93_0.qteStatus = var_0_10
	arg_93_0.beginTeam = var_0_3

	arg_93_0.changeQTEBtnStatus(var_0_5)

def var_0_0.qteFail(arg_94_0):
	arg_94_0.qteStatus = var_0_11
	arg_94_0.beginTeam = var_0_4

	arg_94_0.changeQTEBtnStatus(var_0_5)

def var_0_0.GetBeziersPoints(arg_95_0, arg_95_1, arg_95_2, arg_95_3, arg_95_4):
	local function var_95_0(arg_96_0)
		local var_96_0 = arg_95_1.Clone().Mul((1 - arg_96_0) * (1 - arg_96_0))
		local var_96_1 = arg_95_2.Clone().Mul(2 * arg_96_0 * (1 - arg_96_0))
		local var_96_2 = arg_95_3.Clone().Mul(arg_96_0 * arg_96_0)

		return var_96_0.Clone().Add(var_96_1).Add(var_96_2)

	local var_95_1 = {}

	table.insert(var_95_1, Vector3(0, 0, 0))
	table.insert(var_95_1, var_95_0(0))

	for iter_95_0 = 1, arg_95_4:
		local var_95_2 = iter_95_0 / arg_95_4

		table.insert(var_95_1, var_95_0(var_95_2))

	table.insert(var_95_1, Vector3(0, 0, 0))

	return var_95_1

def var_0_0.ballParabolaMove(arg_97_0, arg_97_1, arg_97_2, arg_97_3, arg_97_4, arg_97_5, arg_97_6):
	local var_97_0 = Vector2(arg_97_1.anchoredPosition.x, arg_97_1.anchoredPosition.y - arg_97_5)
	local var_97_1 = Vector2(arg_97_3.x, arg_97_3.y)
	local var_97_2 = var_97_1.x - var_97_0.x
	local var_97_3 = var_97_1.y - var_97_0.y
	local var_97_4 = math.abs(arg_97_6 - arg_97_5)
	local var_97_5 = DOAParabolaCalc(arg_97_2, math.abs(var_0_33), var_97_4)
	local var_97_6
	local var_97_7

	if arg_97_5 < arg_97_6:
		var_97_6 = var_97_5 + var_97_4

		local var_97_8 = var_97_5
	else
		var_97_6 = var_97_5

		local var_97_9 = var_97_5 + var_97_4

	local var_97_10 = math.sqrt(2 * math.abs(var_0_33) * var_97_6)

	arg_97_0.managedTween(LeanTween.value, function()
		if arg_97_4:
			arg_97_4(), go(arg_97_1), 0, arg_97_2, arg_97_2).setOnUpdate(System.Action_float(function(arg_99_0)
		local var_99_0 = var_97_2 * arg_99_0 / arg_97_2
		local var_99_1 = var_97_3 * arg_99_0 / arg_97_2
		local var_99_2 = var_97_10 * arg_99_0 + 0.5 * var_0_33 * arg_99_0 * arg_99_0

		arg_97_1.anchoredPosition = Vector2(var_97_0.x + var_99_0, var_97_0.y + var_99_1 + arg_97_5 + var_99_2)))

def var_0_0.ballServe(arg_100_0, arg_100_1, arg_100_2, arg_100_3, arg_100_4):
	arg_100_0.ballParabolaMove(arg_100_1, arg_100_2, arg_100_3, function()
		if arg_100_4:
			arg_100_4(), var_0_24, var_0_25)
	arg_100_0.managedTween(LeanTween.move, None, arg_100_0.ballShadow, Vector3(arg_100_3.x, arg_100_3.y + var_0_23), arg_100_2).setEase(LeanTweenType.linear)

def var_0_0.ballUp2Up(arg_102_0, arg_102_1, arg_102_2, arg_102_3, arg_102_4):
	arg_102_0.ballParabolaMove(arg_102_1, arg_102_2, arg_102_3, function()
		if arg_102_4:
			arg_102_4(), var_0_25, var_0_25)
	arg_102_0.managedTween(LeanTween.move, None, arg_102_0.ballShadow, Vector3(arg_102_3.x, arg_102_3.y + var_0_23), arg_102_2).setEase(LeanTweenType.linear)

def var_0_0.ballUp2Hit(arg_104_0, arg_104_1, arg_104_2, arg_104_3, arg_104_4):
	local var_104_0 = {
		x = arg_104_3.x,
		y = arg_104_3.y
	}

	arg_104_0.ballParabolaMove(arg_104_1, arg_104_2, var_104_0, function()
		if arg_104_4:
			arg_104_4(), var_0_25, var_0_26)
	arg_104_0.managedTween(LeanTween.move, None, arg_104_0.ballShadow, Vector3(arg_104_3.x, arg_104_3.y + var_0_23), arg_104_2).setEase(LeanTweenType.linear)

def var_0_0.ballHit(arg_106_0, arg_106_1, arg_106_2, arg_106_3, arg_106_4):
	arg_106_3 = Vector2(arg_106_3.x, arg_106_3.y + var_0_25)

	arg_106_0.managedTween(LeanTween.moveX, function()
		if arg_106_4:
			arg_106_4(), arg_106_1, arg_106_3.x, arg_106_2).setEase(LeanTweenType.linear)
	arg_106_0.managedTween(LeanTween.moveY, None, arg_106_1, arg_106_3.y, arg_106_2).setEase(LeanTweenType.linear)
	arg_106_0.managedTween(LeanTween.move, None, arg_106_0.ballShadow, Vector3(arg_106_3.x, arg_106_3.y + var_0_23), arg_106_2).setEase(LeanTweenType.linear)

def var_0_0.charMove(arg_108_0, arg_108_1, arg_108_2, arg_108_3, arg_108_4):
	arg_108_0.managedTween(LeanTween.moveX, None, arg_108_1, arg_108_3.x, arg_108_2).setEase(LeanTweenType.easeOutQuad)
	arg_108_0.managedTween(LeanTween.moveY, function()
		if arg_108_4:
			arg_108_4(), arg_108_1, arg_108_3.y, arg_108_2).setEase(LeanTweenType.linear)

def var_0_0.hitFly(arg_110_0, arg_110_1, arg_110_2, arg_110_3, arg_110_4):
	arg_110_0.ballParabolaMove(arg_110_1, arg_110_2, arg_110_3, function()
		if arg_110_4:
			arg_110_4(), var_0_27, var_0_26)
	arg_110_0.managedTween(LeanTween.move, None, arg_110_0.ballShadow, Vector3(arg_110_3.x, arg_110_3.y + var_0_23), arg_110_2).setEase(LeanTweenType.linear)

def var_0_0.startQTE(arg_112_0, arg_112_1, arg_112_2, arg_112_3, arg_112_4):
	arg_112_0.changeQTEBtnStatus(var_0_6)

	arg_112_0.qte.anchoredPosition = {
		x = arg_112_3.x,
		y = arg_112_3.y + arg_112_2
	}

	setActive(arg_112_0.qte, True)
	setActive(arg_112_0.qteCircles, True)
	setActive(arg_112_0.result, False)
	setLocalScale(arg_112_0.qteCircle, Vector3(1, 1, 1))
	arg_112_0.result.GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_113_0)
		setActive(arg_112_0.result, False))

	arg_112_0.qteCallback = arg_112_4
	arg_112_0.qteTween = LeanTween.scale(arg_112_0.qteCircle, Vector3(0, 0, 1), arg_112_1).setOnComplete(System.Action(function()
		arg_112_0.changeQTEBtnStatus(var_0_5)
		setImageSprite(arg_112_0.result, arg_112_0.resultTxt.Find("miss").GetComponent(typeof(Image)).sprite, True)
		setActive(arg_112_0.result, True)
		arg_112_0.qteFail()

		arg_112_0.isCutin = False

		setActive(arg_112_0.qteCircles, False)
		existCall(arg_112_0.qteCallback)

		arg_112_0.qteCallback = None)).uniqueId

def var_0_0.qteResult(arg_115_0):
	if LeanTween.isTweening(arg_115_0.qteTween):
		LeanTween.cancel(arg_115_0.qteTween, False)

	local var_115_0 = math.abs(arg_115_0.qteCircle.localScale.x)

	setActive(arg_115_0.result, True)

	arg_115_0.isCutin = False

	if var_115_0 <= 0 or var_115_0 > var_0_7:
		setImageSprite(arg_115_0.result, arg_115_0.resultTxt.Find("miss").GetComponent(typeof(Image)).sprite, True)
		arg_115_0.qteFail()
	elif var_115_0 > var_0_8:
		setImageSprite(arg_115_0.result, arg_115_0.resultTxt.Find("good").GetComponent(typeof(Image)).sprite, True)
		arg_115_0.qteSuccess()
	else
		setImageSprite(arg_115_0.result, arg_115_0.resultTxt.Find("perfect").GetComponent(typeof(Image)).sprite, True)
		arg_115_0.qteSuccess()

		if arg_115_0.qteType == var_0_14:
			arg_115_0.isCutin = True
		else
			arg_115_0.isCutin = False

	setActive(arg_115_0.qteCircles, False)
	existCall(arg_115_0.qteCallback)

	arg_115_0.qteCallback = None

local function var_0_34(arg_116_0, arg_116_1, arg_116_2, arg_116_3, arg_116_4)
	local var_116_0 = {
		_tf = arg_116_1,
		spineAnim = arg_116_2,
		skele = arg_116_3,
		posTag = arg_116_4
	}

	function var_116_0.ctor(arg_117_0)
		var_116_0._tf.anchoredPosition = arg_116_0.anchoredPos[arg_116_4]

	function var_116_0.setPosTag(arg_118_0, arg_118_1)
		var_116_0._tf.anchoredPosition = arg_116_0.anchoredPos[arg_118_1]
		var_116_0.posTag = arg_118_1

	function var_116_0.getPosTag(arg_119_0)
		return var_116_0.posTag

	function var_116_0.pauseSpine(arg_120_0)
		var_116_0.skele.timeScale = 0

	function var_116_0.resumeSpine(arg_121_0)
		var_116_0.skele.timeScale = 1

	function var_116_0.setActionOnce(arg_122_0, arg_122_1, arg_122_2)
		var_116_0.spineAnim.SetActionCallBack(function(arg_123_0)
			if arg_123_0 == "action":
				if arg_122_1 == "chuanqiu" or arg_122_1 == "dianqiu":
					arg_116_0.playEffect(arg_116_0.upEffect, Vector2(var_116_0._tf.anchoredPosition.x, var_116_0._tf.anchoredPosition.y + var_0_25))
					pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_30)
				elif arg_122_1 == "kouqiu":
					arg_116_0.playEffect(arg_116_0.hitEffect, Vector2(var_116_0._tf.anchoredPosition.x, var_116_0._tf.anchoredPosition.y + var_0_25 + var_0_26))
					pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_31)
				elif arg_122_1 == "faqiu":
					pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_30)
					arg_116_0.playEffect(arg_116_0.upEffect, Vector2(var_116_0._tf.anchoredPosition.x, var_116_0._tf.anchoredPosition.y + var_0_24))

			if arg_123_0 == "finish":
				var_116_0.spineAnim.SetActionCallBack(None)

				if arg_122_2:
					arg_122_2()
				else
					var_116_0.spineAnim.SetAction("normal2", 0))
		var_116_0.spineAnim.SetAction(arg_122_1, 0)

	function var_116_0.move(arg_124_0, arg_124_1, arg_124_2, arg_124_3, arg_124_4)
		local function var_124_0()
			var_116_0.spineAnim.SetAction("run", 0)

			var_116_0.posTag = arg_124_2

			arg_116_0.charMove(var_116_0._tf, arg_124_1, arg_116_0.anchoredPos[arg_124_2], function()
				if arg_124_4:
					arg_124_4()
				else
					var_116_0.spineAnim.SetAction("normal2", 0))

		if arg_124_3:
			var_116_0.setActionOnce(arg_124_3, function()
				var_124_0())
		else
			var_124_0()

	var_116_0.ctor()

	return var_116_0

def var_0_0.getRandomPos(arg_128_0, arg_128_1):
	local var_128_0 = math.random(0, 300)
	local var_128_1 = math.random(0, 50)
	local var_128_2 = arg_128_0.orgPos[arg_128_1]
	local var_128_3 = var_128_2

	if string.find(arg_128_1, "our"):
		var_128_3 = {
			x = var_128_2.x + var_128_0 - 50,
			y = var_128_2.y + var_128_1 - 25
		}
	else
		var_128_3 = {
			x = var_128_2.x + var_128_0 - 250,
			y = var_128_2.y + var_128_1 - 25
		}

	return var_128_3

def var_0_0.loadSpineChars(arg_129_0):
	arg_129_0.clearSpineChars()

	arg_129_0.beginTeam = math.random(2)

	if arg_129_0.beginTeam == var_0_3:
		arg_129_0.serveChar = "our" .. math.random(2)
	else
		arg_129_0.serveChar = "enemy" .. math.random(2)

	arg_129_0.setBallPos()

	for iter_129_0, iter_129_1 in pairs(arg_129_0.charNames):
		arg_129_0.loadOneSpineChar(iter_129_0, arg_129_0.serveChar)

def var_0_0.loadOneSpineChar(arg_130_0, arg_130_1, arg_130_2):
	if not arg_130_0.charNames[arg_130_1]:
		arg_130_0.charNames[arg_130_1] = False

		return

	pg.UIMgr.GetInstance().LoadingOn()
	PoolMgr.GetInstance().GetSpineChar(arg_130_0.charNames[arg_130_1], True, function(arg_131_0)
		pg.UIMgr.GetInstance().LoadingOff()

		local var_131_0 = ""
		local var_131_1

		if string.find(arg_130_1, "our"):
			tf(arg_131_0).localScale = Vector3(0.6, 0.6, 1)
			tf(arg_131_0).localPosition = Vector3(-20, 0, 0)

			if string.find(arg_130_1, "1"):
				var_131_1 = "our1"
			else
				var_131_1 = "our2"
		else
			tf(arg_131_0).localScale = Vector3(-0.6, 0.6, 1)
			tf(arg_131_0).localPosition = Vector3(20, 0, 0)
			var_131_1 = string.find(arg_130_1, "1") and "enemy1" or "enemy2"

		arg_130_0.charModels[arg_130_1] = arg_131_0

		local var_131_2 = arg_131_0.GetComponent("SpineAnimUI")
		local var_131_3 = arg_131_0.GetComponent("SkeletonGraphic")

		var_131_2.SetAction("normal2", 0)

		var_131_3.timeScale = 1

		local var_131_4 = arg_130_0._tf.Find("game_ui/char/" .. arg_130_1)

		setParent(arg_131_0, var_131_4)

		arg_130_0.charactor[arg_130_1] = var_0_34(arg_130_0, var_131_4, var_131_2, var_131_3, var_131_1)

		if arg_130_1 == arg_130_2:
			if arg_130_0.beginTeam == var_0_3:
				arg_130_0.charactor[arg_130_1].setPosTag("our_serve")
			else
				arg_130_0.charactor[arg_130_1].setPosTag("enemy_serve"))

def var_0_0.clearSpineChars(arg_132_0):
	for iter_132_0, iter_132_1 in pairs(arg_132_0.charModels):
		if arg_132_0.charModels[iter_132_0] and arg_132_0.charNames[iter_132_0]:
			PoolMgr.GetInstance().ReturnSpineChar(arg_132_0.charNames[iter_132_0], arg_132_0.charModels[iter_132_0])

	arg_132_0.charModels = {}

def var_0_0.getCharWithTag(arg_133_0, arg_133_1):
	for iter_133_0, iter_133_1 in pairs(arg_133_0.charactor):
		if iter_133_1.getPosTag() == arg_133_1:
			return iter_133_0, iter_133_1

	return None

def var_0_0.getAnotherChar(arg_134_0, arg_134_1):
	local var_134_0 = ""

	if string.find(arg_134_1, "our"):
		var_134_0 = arg_134_1 == "our1" and "our2" or "our1"
	elif string.find(arg_134_1, "enemy"):
		var_134_0 = arg_134_1 == "enemy1" and "enemy2" or "enemy1"

	return var_134_0, arg_134_0.charactor[var_134_0]

def var_0_0.setBallPos(arg_135_0):
	setActive(arg_135_0.ball, True)

	local var_135_0 = string.find(arg_135_0.serveChar, "our") and "our_serve" or "enemy_serve"

	arg_135_0.ball.anchoredPosition = {
		x = arg_135_0.orgPos[var_135_0].x,
		y = arg_135_0.orgPos[var_135_0].y + 300
	}
	arg_135_0.ballShadow.anchoredPosition = Vector3(arg_135_0.orgPos[var_135_0].x, arg_135_0.orgPos[var_135_0].y, 0)

	arg_135_0.managedTween(LeanTween.rotate, None, arg_135_0.ball, 360, 0.5).setLoopClamp()

def var_0_0.resetChar(arg_136_0):
	arg_136_0.resetPos()

	for iter_136_0, iter_136_1 in pairs(arg_136_0.charactor):
		if LeanTween.isTweening(go(iter_136_1._tf)):
			LeanTween.cancel(go(iter_136_1._tf))

	arg_136_0.charactor.our1.setPosTag("our1")
	arg_136_0.charactor.our2.setPosTag("our2")
	arg_136_0.charactor.enemy1.setPosTag("enemy1")
	arg_136_0.charactor.enemy2.setPosTag("enemy2")

	if arg_136_0.beginTeam == var_0_3:
		arg_136_0.serveChar = "our" .. math.random(2)

		arg_136_0.charactor[arg_136_0.serveChar].setPosTag("our_serve")
	else
		arg_136_0.serveChar = "enemy" .. math.random(2)

		arg_136_0.charactor[arg_136_0.serveChar].setPosTag("enemy_serve")

	arg_136_0.setBallPos()

def var_0_0.charServeBall(arg_137_0):
	arg_137_0.managedTween(LeanTween.rotate, None, arg_137_0.ball, 360, 0.5).setLoopClamp()

	local var_137_0 = string.find(arg_137_0.serveChar, "our") and "our_serve" or "enemy_serve"

	arg_137_0.managedTween(LeanTween.delayedCall, function()
		arg_137_0.managedTween(LeanTween.moveY, None, arg_137_0.ball, arg_137_0.orgPos[var_137_0].y + var_0_24, 0.5).setEase(LeanTweenType.linear)
		arg_137_0.charactor[arg_137_0.serveChar].setActionOnce("faqiu", function()
			arg_137_0.managedTween(LeanTween.delayedCall, function()
				arg_137_0.charactor[arg_137_0.serveChar].move(1, arg_137_0.serveChar), 0.2, None)), 0.5, None)

def var_0_0.charUpBall(arg_141_0, arg_141_1):
	local var_141_0, var_141_1 = arg_141_0.getCharWithTag(arg_141_0.ballPosTag)

	if not var_141_1:
		return

	arg_141_0.upChar = var_141_0
	arg_141_0.hitChar = arg_141_0.getAnotherChar(arg_141_0.upChar)

	var_141_1.move(0.45, arg_141_0.ballPosTag, None, function()
		var_141_1.setActionOnce("chuanqiu"))

def var_0_0.charHitBall(arg_143_0):
	local var_143_0 = arg_143_0.charactor[arg_143_0.hitChar]

	var_143_0.move(0.5, arg_143_0.ballPosTag, None, function()
		var_143_0.setActionOnce("kouqiu"))

def var_0_0.showcutin(arg_145_0, arg_145_1):
	arg_145_0.setBtnAvailable(False)
	arg_145_0.pauseGame()
	setActive(arg_145_0.cutin, True)

	local var_145_0 = ""

	for iter_145_0, iter_145_1 in pairs(arg_145_0.charNames):
		if iter_145_0 == arg_145_0.hitChar:
			var_145_0 = iter_145_1

	local var_145_1, var_145_2, var_145_3 = ShipWordHelper.GetWordAndCV(var_0_2[arg_145_0.getCharIndex(var_145_0)], "skill")

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_145_2)
	setActive(arg_145_0.findTF("line", arg_145_0.gameUI), True)
	setActive(arg_145_0.findTF("shatanpaiqiu_cutin", arg_145_0.cutin), False)
	setActive(arg_145_0.findTF("shatanpaiqiu_cutin", arg_145_0.cutin), True)
	setImageSprite(arg_145_0.cutinPaint, arg_145_0.cutinPaints.Find(arg_145_0.getCharIndex(var_145_0)).GetComponent(typeof(Image)).sprite, True)
	LeanTween.moveX(arg_145_0.cutin, 0, 0.3).setOnComplete(System.Action(function()
		LeanTween.delayedCall(1, System.Action(function()
			setActive(arg_145_0.findTF("line", arg_145_0.gameUI), False)
			LeanTween.moveX(arg_145_0.cutin, -567, 0.3).setOnComplete(System.Action(function()
				setActive(arg_145_0.cutin, False)
				arg_145_0.setBtnAvailable(True)
				arg_145_0.resumeGame()

				if arg_145_1:
					arg_145_1()))))))

def var_0_0.showScoreCutin(arg_149_0, arg_149_1):
	arg_149_0.setBtnAvailable(False)
	arg_149_0.pauseGame()
	setImageSprite(arg_149_0.ourScoreCutin, arg_149_0.scoreCutinNums.Find(arg_149_0.ourScoreNum).GetComponent(typeof(Image)).sprite, True)
	setImageSprite(arg_149_0.enemyScoreCutin, arg_149_0.scoreCutinNums.Find(arg_149_0.enemyScoreNum).GetComponent(typeof(Image)).sprite, True)
	setActive(arg_149_0.scoreCutin, True)
	setLocalScale(arg_149_0.scoreCutin, Vector3(1, 0, 1))
	LeanTween.scale(arg_149_0.scoreCutin, Vector3(1, 1, 1), 0.2).setOnComplete(System.Action(function()
		arg_149_0.resetChar()
		LeanTween.delayedCall(0.6, System.Action(function()
			LeanTween.scale(arg_149_0.scoreCutin, Vector3(1, 0, 1), 0.2).setOnComplete(System.Action(function()
				setActive(arg_149_0.scoreCutin, False)
				arg_149_0.setBtnAvailable(True)
				arg_149_0.resumeGame()

				if arg_149_1:
					arg_149_1()))))))

def var_0_0.updateScore(arg_153_0):
	setText(arg_153_0.ourScore, arg_153_0.ourScoreNum)
	setText(arg_153_0.enemyScore, arg_153_0.enemyScoreNum)
	setActive(arg_153_0.qte, False)

	if arg_153_0.ourScoreNum >= arg_153_0.endScore or arg_153_0.enemyScoreNum >= arg_153_0.endScore:
		arg_153_0.endGame()
	else
		arg_153_0.showScoreCutin(function()
			arg_153_0.startGame())

def var_0_0.endGame(arg_155_0):
	setActive(arg_155_0.winTag, arg_155_0.ourScoreNum != arg_155_0.enemyScoreNum)
	setActive(arg_155_0.loseTag, arg_155_0.ourScoreNum != arg_155_0.enemyScoreNum)
	arg_155_0.setBtnAvailable(False)

	arg_155_0.isInGame = False

	pg.UIMgr.GetInstance().BlurPanel(arg_155_0.endUI)
	setActive(arg_155_0.endUI, True)
	setActive(arg_155_0.endFreeTitle, arg_155_0.isFree)
	setActive(arg_155_0.endDayTitle, not arg_155_0.isFree)
	setImageSprite(arg_155_0.endTitleDay, arg_155_0.titleDays.Find(arg_155_0.curDay).GetComponent(typeof(Image)).sprite, True)
	setImageSprite(arg_155_0.endOurScore, arg_155_0.endScoreNums.Find(arg_155_0.ourScoreNum).GetComponent(typeof(Image)).sprite, True)
	setImageSprite(arg_155_0.endEnemyScore, arg_155_0.endScoreNums.Find(arg_155_0.enemyScoreNum).GetComponent(typeof(Image)).sprite, True)

	local var_155_0 = -20
	local var_155_1

	if arg_155_0.ourScoreNum > arg_155_0.enemyScoreNum:
		arg_155_0.winTag.anchoredPosition = Vector3(-170, 200, 0)
		arg_155_0.loseTag.anchoredPosition = Vector3(180, 200, 0)
		var_155_1 = -20
	else
		arg_155_0.winTag.anchoredPosition = Vector3(170, 200, 0)
		arg_155_0.loseTag.anchoredPosition = Vector3(-180, 200, 0)
		var_155_1 = 20

	setActive(arg_155_0.winTag.GetChild(0), False)
	setActive(arg_155_0.winTag.GetChild(0), True)
	setLocalRotation(arg_155_0.loseTag, Vector3(0, 0, 0))
	LeanTween.rotateZ(go(arg_155_0.loseTag), var_155_1, 0.2).setOnComplete(System.Action(function()
		if arg_155_0.GetMGHubData().count > 0:
			arg_155_0.emit(BaseMiniGameMediator.MINI_GAME_SUCCESS, 0)))

def var_0_0.OnGetAwardDone(arg_157_0, arg_157_1):
	if arg_157_1.cmd == MiniGameOPCommand.CMD_COMPLETE:
		local var_157_0 = arg_157_0.GetMGHubData()
		local var_157_1 = var_157_0.ultimate
		local var_157_2 = var_157_0.usedtime
		local var_157_3 = var_157_0.getConfig("reward_need")
		local var_157_4 = arg_157_0.GetMGHubData().count
		local var_157_5 = pg.NewStoryMgr.GetInstance()
		local var_157_6 = arg_157_0.storylist[arg_157_0.GetMGHubData().usedtime] and arg_157_0.storylist[arg_157_0.GetMGHubData().usedtime][1] or None

		if var_157_2 != 7 and var_157_6 and not var_157_5.IsPlayed(var_157_6):
			var_157_5.Play(var_157_6)

		if var_157_1 == 0 and var_157_3 <= var_157_2:
			pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
				hubid = var_157_0.id,
				cmd = MiniGameOPCommand.CMD_ULTIMATE,
				args1 = {}
			})
	elif arg_157_1.cmd == MiniGameOPCommand.CMD_ULTIMATE:
		local var_157_7 = arg_157_0.storylist[7][1] and arg_157_0.storylist[7][1] or None
		local var_157_8 = pg.NewStoryMgr.GetInstance()

		if var_157_7 and not var_157_8.IsPlayed(var_157_7):
			var_157_8.Play(var_157_7)

def var_0_0.pauseGame(arg_158_0):
	arg_158_0.pauseManagedTween()

	if arg_158_0.qteTimer:
		arg_158_0.qteTimer.Pause()

	if arg_158_0.qteTween and LeanTween.isTweening(arg_158_0.qteTween):
		LeanTween.pause(arg_158_0.qteTween)

	for iter_158_0, iter_158_1 in pairs(arg_158_0.charactor):
		iter_158_1.pauseSpine()

def var_0_0.resumeGame(arg_159_0):
	arg_159_0.resumeManagedTween()

	if arg_159_0.qteTimer:
		arg_159_0.qteTimer.Resume()

	if arg_159_0.qteTween and LeanTween.isTweening(arg_159_0.qteTween):
		LeanTween.resume(arg_159_0.qteTween)

	for iter_159_0, iter_159_1 in pairs(arg_159_0.charactor):
		iter_159_1.resumeSpine()

def var_0_0.clearTimer(arg_160_0):
	if arg_160_0.qteTimer:
		arg_160_0.qteTimer.Stop()

		arg_160_0.qteTimer = None

	if arg_160_0.countTimer:
		arg_160_0.countTimer.Stop()

		arg_160_0.countTimer = None

def var_0_0.changeQTEBtnStatus(arg_161_0, arg_161_1):
	arg_161_0.qteBtnStatus = arg_161_1

def var_0_0.resetGameData(arg_162_0):
	arg_162_0.qteStatus = var_0_9
	arg_162_0.qteType = var_0_12

	arg_162_0.changeQTEBtnStatus(var_0_5)

	arg_162_0.ballPosTag = ""
	arg_162_0.isCutin = False
	arg_162_0.cutin.anchoredPosition = {
		x = -567,
		y = 582
	}
	arg_162_0.isScoreCutin = False

	setActive(arg_162_0.scoreCutin, False)

	arg_162_0.ourScoreNum = 0
	arg_162_0.enemyScoreNum = 0

	setText(arg_162_0.ourScore, arg_162_0.ourScoreNum)
	setText(arg_162_0.enemyScore, arg_162_0.enemyScoreNum)
	setActive(arg_162_0.qte, False)
	arg_162_0.loadSpineChars()

def var_0_0.exitGame(arg_163_0):
	arg_163_0.isInGame = False

	arg_163_0.setBtnAvailable(True)
	arg_163_0.resetGameAni()

def var_0_0.resetGameAni(arg_164_0):
	arg_164_0.cleanManagedTween()

	if arg_164_0.qteTween and LeanTween.isTweening(arg_164_0.qteTween):
		LeanTween.cancel(arg_164_0.qteTween, False)

	arg_164_0.clearTimer()

def var_0_0.willExit(arg_165_0):
	arg_165_0.clearSpineChars()
	pg.UIMgr.GetInstance().UnblurPanel(arg_165_0.selectUI, arg_165_0._tf)
	pg.UIMgr.GetInstance().UnblurPanel(arg_165_0.endUI, arg_165_0._tf)
	pg.UIMgr.GetInstance().UnblurPanel(arg_165_0.countTimeUI, arg_165_0._tf)

def var_0_0.onBackPressed(arg_166_0):
	if arg_166_0.isInGame:
		triggerButton(arg_166_0.backBtn)
	elif isActive(arg_166_0.selectUI):
		triggerButton(arg_166_0.selectBackBtn)
	elif isActive(arg_166_0.mainUI):
		triggerButton(arg_166_0.returnBtn)

return var_0_0
