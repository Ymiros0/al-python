local var_0_0 = class("LevelScene", import("..base.BaseUI"))
local var_0_1 = 0.5
local var_0_2 = 1
local var_0_3 = 2
local var_0_4 = 3

def var_0_0.forceGC(arg_1_0):
	return True

def var_0_0.getUIName(arg_2_0):
	return "LevelMainScene"

def var_0_0.ResUISettings(arg_3_0):
	return {
		showType = PlayerResUI.TYPE_ALL,
		groupName = LayerWeightConst.GROUP_LEVELUI
	}

def var_0_0.getBGM(arg_4_0):
	local function var_4_0()
		return checkExist(arg_4_0.contextData.chapterVO, {
			"getConfig",
			{
				"bgm"
			}
		}) or ""

	local function var_4_1()
		if not arg_4_0.contextData.map:
			return

		local var_6_0 = arg_4_0.contextData.map.getConfig("ani_controller")

		if var_6_0 and #var_6_0 > 0:
			for iter_6_0, iter_6_1 in ipairs(var_6_0):
				local var_6_1 = _.rest(iter_6_1[2], 2)

				for iter_6_2, iter_6_3 in ipairs(var_6_1):
					if string.find(iter_6_3, "^bgm_") and iter_6_1[1] == var_0_3:
						local var_6_2 = iter_6_1[2][1]
						local var_6_3 = getProxy(ChapterProxy).GetChapterItemById(var_6_2)

						if var_6_3 and not var_6_3.isClear():
							return string.sub(iter_6_3, 5)

		return checkExist(arg_4_0.contextData.map, {
			"getConfig",
			{
				"bgm"
			}
		}) or ""

	for iter_4_0, iter_4_1 in ipairs({
		var_4_0(),
		var_4_1()
	}):
		if iter_4_1 != "":
			return iter_4_1

	return var_0_0.super.getBGM(arg_4_0)

var_0_0.optionsPath = {
	"top/top_chapter/option"
}

def var_0_0.preload(arg_7_0, arg_7_1):
	local var_7_0 = getProxy(ChapterProxy)

	if arg_7_0.contextData.mapIdx and arg_7_0.contextData.chapterId:
		local var_7_1 = var_7_0.getChapterById(arg_7_0.contextData.chapterId)

		if var_7_1.getConfig("map") == arg_7_0.contextData.mapIdx:
			arg_7_0.contextData.chapterVO = var_7_1

			if var_7_1.active:
				assert(not arg_7_0.contextData.openChapterId or arg_7_0.contextData.openChapterId == arg_7_0.contextData.chapterId)

				arg_7_0.contextData.openChapterId = None

	local var_7_2, var_7_3 = arg_7_0.GetInitializeMap()

	if arg_7_0.contextData.entranceStatus == None:
		arg_7_0.contextData.entranceStatus = not var_7_3

	if not arg_7_0.contextData.entranceStatus:
		arg_7_0.PreloadLevelMainUI(var_7_2, arg_7_1)
	else
		arg_7_1()

def var_0_0.GetInitializeMap(arg_8_0):
	local var_8_0 = (function()
		local var_9_0 = arg_8_0.contextData.chapterVO

		if var_9_0 and var_9_0.active:
			return var_9_0.getConfig("map")

		local var_9_1 = arg_8_0.contextData.mapIdx

		if var_9_1:
			return var_9_1

		local var_9_2

		if arg_8_0.contextData.targetChapter and arg_8_0.contextData.targetMap:
			arg_8_0.contextData.openChapterId = arg_8_0.contextData.targetChapter
			var_9_2 = arg_8_0.contextData.targetMap.id
			arg_8_0.contextData.targetChapter = None
			arg_8_0.contextData.targetMap = None
		elif arg_8_0.contextData.eliteDefault:
			local var_9_3 = getProxy(ChapterProxy).getUseableMaxEliteMap()

			var_9_2 = var_9_3 and var_9_3.id or None
			arg_8_0.contextData.eliteDefault = None

		return var_9_2)()
	local var_8_1 = var_8_0 and getProxy(ChapterProxy).getMapById(var_8_0)

	if var_8_1:
		local var_8_2, var_8_3 = var_8_1.isUnlock()

		if not var_8_2:
			pg.TipsMgr.GetInstance().ShowTips(var_8_3)

			var_8_0 = getProxy(ChapterProxy).getLastUnlockMap().id
			arg_8_0.contextData.mapIdx = var_8_0
	else
		var_8_0 = None

	return var_8_0 or arg_8_0.selectMap(), tobool(var_8_0)

def var_0_0.init(arg_10_0):
	arg_10_0.initData()
	arg_10_0.initUI()
	arg_10_0.initEvents()
	arg_10_0.updateClouds()

def var_0_0.initData(arg_11_0):
	arg_11_0.tweens = {}
	arg_11_0.mapWidth = 1920
	arg_11_0.mapHeight = 1440
	arg_11_0.levelCamIndices = 1
	arg_11_0.frozenCount = 0
	arg_11_0.currentBG = None
	arg_11_0.mapBuilder = None
	arg_11_0.mbDict = {}
	arg_11_0.mapGroup = {}

	if not arg_11_0.contextData.huntingRangeVisibility:
		arg_11_0.contextData.huntingRangeVisibility = 2

def var_0_0.initUI(arg_12_0):
	arg_12_0.topPanel = arg_12_0.findTF("top")
	arg_12_0.canvasGroup = arg_12_0.topPanel.GetComponent("CanvasGroup")
	arg_12_0.canvasGroup.blocksRaycasts = not arg_12_0.canvasGroup.blocksRaycasts
	arg_12_0.canvasGroup.blocksRaycasts = not arg_12_0.canvasGroup.blocksRaycasts
	arg_12_0.entranceLayer = arg_12_0.findTF("entrance")
	arg_12_0.ptBonus = EventPtBonus.New(arg_12_0.entranceLayer.Find("btns/btn_task/bonusPt"))
	arg_12_0.entranceBg = arg_12_0.findTF("entrance_bg")
	arg_12_0.topChapter = arg_12_0.findTF("top_chapter", arg_12_0.topPanel)

	setActive(arg_12_0.topChapter.Find("title_chapter"), False)
	setActive(arg_12_0.topChapter.Find("type_chapter"), False)
	setActive(arg_12_0.topChapter.Find("type_escort"), False)
	setActive(arg_12_0.topChapter.Find("type_skirmish"), False)

	arg_12_0.chapterName = arg_12_0.findTF("title_chapter/name", arg_12_0.topChapter)
	arg_12_0.chapterNoTitle = arg_12_0.findTF("title_chapter/chapter", arg_12_0.topChapter)
	arg_12_0.resChapter = arg_12_0.findTF("resources", arg_12_0.topChapter)

	setActive(arg_12_0.topChapter, True)

	arg_12_0._voteBookBtn = arg_12_0.topChapter.Find("vote_book")
	arg_12_0.leftChapter = arg_12_0.findTF("main/left_chapter")

	setActive(arg_12_0.leftChapter, True)

	arg_12_0.leftCanvasGroup = arg_12_0.leftChapter.GetComponent(typeof(CanvasGroup))
	arg_12_0.btnPrev = arg_12_0.findTF("btn_prev", arg_12_0.leftChapter)
	arg_12_0.btnPrevCol = arg_12_0.findTF("btn_prev/prev_image", arg_12_0.leftChapter)
	arg_12_0.eliteBtn = arg_12_0.findTF("buttons/btn_elite", arg_12_0.leftChapter)
	arg_12_0.normalBtn = arg_12_0.findTF("buttons/btn_normal", arg_12_0.leftChapter)
	arg_12_0.actNormalBtn = arg_12_0.findTF("buttons/btn_act_normal", arg_12_0.leftChapter)

	setActive(arg_12_0.actNormalBtn, False)

	arg_12_0.actEliteBtn = arg_12_0.findTF("buttons/btn_act_elite", arg_12_0.leftChapter)

	setActive(arg_12_0.actEliteBtn, False)

	arg_12_0.actExtraBtn = arg_12_0.findTF("buttons/btn_act_extra", arg_12_0.leftChapter)
	arg_12_0.actExtraBtnAnim = arg_12_0.findTF("usm", arg_12_0.actExtraBtn)
	arg_12_0.remasterBtn = arg_12_0.findTF("buttons/btn_remaster", arg_12_0.leftChapter)
	arg_12_0.escortBar = arg_12_0.findTF("escort_bar", arg_12_0.leftChapter)

	setActive(arg_12_0.escortBar, False)

	arg_12_0.eliteQuota = arg_12_0.findTF("elite_quota", arg_12_0.leftChapter)

	setActive(arg_12_0.eliteQuota, False)

	arg_12_0.skirmishBar = arg_12_0.findTF("left_times", arg_12_0.leftChapter)
	arg_12_0.mainLayer = arg_12_0.findTF("main")

	setActive(arg_12_0.mainLayer.Find("title_chapter_lines"), False)

	arg_12_0.rightChapter = arg_12_0.findTF("main/right_chapter")
	arg_12_0.rightCanvasGroup = arg_12_0.rightChapter.GetComponent(typeof(CanvasGroup))
	arg_12_0.eventContainer = arg_12_0.findTF("event_btns/event_container", arg_12_0.rightChapter)
	arg_12_0.btnSpecial = arg_12_0.findTF("btn_task", arg_12_0.eventContainer)
	arg_12_0.challengeBtn = arg_12_0.findTF("btn_challenge", arg_12_0.eventContainer)
	arg_12_0.dailyBtn = arg_12_0.findTF("btn_daily", arg_12_0.eventContainer)
	arg_12_0.militaryExerciseBtn = arg_12_0.findTF("btn_pvp", arg_12_0.eventContainer)
	arg_12_0.activityBtn = arg_12_0.findTF("event_btns/activity_btn", arg_12_0.rightChapter)
	arg_12_0.ptTotal = arg_12_0.findTF("event_btns/pt_text", arg_12_0.rightChapter)
	arg_12_0.ticketTxt = arg_12_0.findTF("event_btns/tickets/Text", arg_12_0.rightChapter)
	arg_12_0.remasterAwardBtn = arg_12_0.findTF("btn_remaster_award", arg_12_0.rightChapter)
	arg_12_0.btnNext = arg_12_0.findTF("btn_next", arg_12_0.rightChapter)
	arg_12_0.btnNextCol = arg_12_0.findTF("btn_next/next_image", arg_12_0.rightChapter)
	arg_12_0.countDown = arg_12_0.findTF("event_btns/count_down", arg_12_0.rightChapter)

	setActive(arg_12_0.findTF("event_btns/BottomList", arg_12_0.rightChapter), True)

	arg_12_0.actExchangeShopBtn = arg_12_0.findTF("event_btns/BottomList/btn_exchange", arg_12_0.rightChapter)
	arg_12_0.actAtelierBuffBtn = arg_12_0.findTF("event_btns/BottomList/btn_control_center", arg_12_0.rightChapter)
	arg_12_0.actExtraRank = arg_12_0.findTF("event_btns/BottomList/act_extra_rank", arg_12_0.rightChapter)

	setActive(arg_12_0.rightChapter, True)
	setActive(arg_12_0.remasterAwardBtn, False)

	arg_12_0.damageTextTemplate = go(arg_12_0.findTF("damage", arg_12_0.topPanel))

	setActive(arg_12_0.damageTextTemplate, False)

	arg_12_0.damageTextPool = {
		arg_12_0.damageTextTemplate
	}
	arg_12_0.damageTextActive = {}
	arg_12_0.mapHelpBtn = arg_12_0.findTF("help_button", arg_12_0.topPanel)

	setActive(arg_12_0.mapHelpBtn, False)

	arg_12_0.avoidText = arg_12_0.findTF("text_avoid", arg_12_0.topPanel)
	arg_12_0.commanderTinkle = arg_12_0.findTF("neko_tinkle", arg_12_0.topPanel)

	setActive(arg_12_0.commanderTinkle, False)

	arg_12_0.spResult = arg_12_0.findTF("sp_result", arg_12_0.topPanel)

	setActive(arg_12_0.spResult, False)

	arg_12_0.helpPage = arg_12_0.findTF("help_page", arg_12_0.topPanel)
	arg_12_0.helpImage = arg_12_0.findTF("icon", arg_12_0.helpPage)

	setActive(arg_12_0.helpPage, False)

	arg_12_0.curtain = arg_12_0.findTF("curtain", arg_12_0.topPanel)

	setActive(arg_12_0.curtain, False)

	arg_12_0.map = arg_12_0.findTF("maps")
	arg_12_0.mapTFs = {
		arg_12_0.findTF("maps/map1"),
		arg_12_0.findTF("maps/map2")
	}

	for iter_12_0, iter_12_1 in ipairs(arg_12_0.mapTFs):
		iter_12_1.GetComponent(typeof(Image)).enabled = False

	local var_12_0 = arg_12_0.map.GetComponent(typeof(AspectRatioFitter))

	var_12_0.aspectRatio, var_12_0.aspectRatio = var_12_0.aspectRatio, 1
	arg_12_0.UIFXList = arg_12_0.findTF("maps/UI_FX_list")

	local var_12_1 = arg_12_0.UIFXList.GetComponentsInChildren(typeof(Renderer))

	for iter_12_2 = 0, var_12_1.Length - 1:
		var_12_1[iter_12_2].sortingOrder = -1

	local var_12_2 = pg.UIMgr.GetInstance()

	arg_12_0.levelCam = var_12_2.levelCamera.GetComponent(typeof(Camera))
	arg_12_0.uiMain = var_12_2.LevelMain

	setActive(arg_12_0.uiMain, False)

	arg_12_0.uiCam = var_12_2.uiCamera.GetComponent(typeof(Camera))
	arg_12_0.levelGrid = arg_12_0.uiMain.Find("LevelGrid")

	setActive(arg_12_0.levelGrid, True)

	arg_12_0.dragLayer = arg_12_0.levelGrid.Find("DragLayer")
	arg_12_0.float = arg_12_0.findTF("float")
	arg_12_0.clouds = arg_12_0.findTF("clouds", arg_12_0.float)

	setActive(arg_12_0.clouds, True)
	setActive(arg_12_0.float.Find("levels"), False)

	arg_12_0.resources = arg_12_0.findTF("resources").GetComponent("ItemList")
	arg_12_0.arrowTarget = arg_12_0.resources.prefabItem[0]
	arg_12_0.destinationMarkTpl = arg_12_0.resources.prefabItem[1]
	arg_12_0.championTpl = arg_12_0.resources.prefabItem[3]
	arg_12_0.deadTpl = arg_12_0.resources.prefabItem[4]
	arg_12_0.enemyTpl = Instantiate(arg_12_0.resources.prefabItem[5])
	arg_12_0.oniTpl = arg_12_0.resources.prefabItem[6]
	arg_12_0.shipTpl = arg_12_0.resources.prefabItem[8]
	arg_12_0.subTpl = arg_12_0.resources.prefabItem[9]
	arg_12_0.transportTpl = arg_12_0.resources.prefabItem[11]

	setText(arg_12_0.findTF("fighting/Text", arg_12_0.enemyTpl), i18n("ui_word_levelui2_inevent"))
	setAnchoredPosition(arg_12_0.topChapter, {
		y = 0
	})
	setAnchoredPosition(arg_12_0.leftChapter, {
		x = 0
	})
	setAnchoredPosition(arg_12_0.rightChapter, {
		x = 0
	})

	arg_12_0.bubbleMsgBoxes = {}
	arg_12_0.loader = AutoLoader.New()
	arg_12_0.levelFleetView = LevelFleetView.New(arg_12_0.topPanel, arg_12_0.event, arg_12_0.contextData)
	arg_12_0.levelInfoView = LevelInfoView.New(arg_12_0.topPanel, arg_12_0.event, arg_12_0.contextData)

	arg_12_0.buildCommanderPanel()

	arg_12_0.levelRemasterView = LevelRemasterView.New(arg_12_0.topPanel, arg_12_0.event, arg_12_0.contextData)

def var_0_0.initEvents(arg_13_0):
	arg_13_0.bind(LevelUIConst.OPEN_COMMANDER_PANEL, function(arg_14_0, arg_14_1, arg_14_2, arg_14_3)
		arg_13_0.openCommanderPanel(arg_14_1, arg_14_2, arg_14_3))
	arg_13_0.bind(LevelUIConst.HANDLE_SHOW_MSG_BOX, function(arg_15_0, arg_15_1)
		arg_13_0.HandleShowMsgBox(arg_15_1))
	arg_13_0.bind(LevelUIConst.DO_AMBUSH_WARNING, function(arg_16_0, arg_16_1)
		arg_13_0.doAmbushWarning(arg_16_1))
	arg_13_0.bind(LevelUIConst.DISPLAY_AMBUSH_INFO, function(arg_17_0, arg_17_1)
		arg_13_0.displayAmbushInfo(arg_17_1))
	arg_13_0.bind(LevelUIConst.DISPLAY_STRATEGY_INFO, function(arg_18_0, arg_18_1)
		arg_13_0.displayStrategyInfo(arg_18_1))
	arg_13_0.bind(LevelUIConst.FROZEN, function(arg_19_0)
		arg_13_0.frozen())
	arg_13_0.bind(LevelUIConst.UN_FROZEN, function(arg_20_0)
		arg_13_0.unfrozen())
	arg_13_0.bind(LevelUIConst.DO_TRACKING, function(arg_21_0, arg_21_1)
		arg_13_0.doTracking(arg_21_1))
	arg_13_0.bind(LevelUIConst.SWITCH_TO_MAP, function()
		if arg_13_0.isfrozen():
			return

		arg_13_0.switchToMap())
	arg_13_0.bind(LevelUIConst.DISPLAY_REPAIR_WINDOW, function(arg_23_0, arg_23_1)
		arg_13_0.displayRepairWindow(arg_23_1))
	arg_13_0.bind(LevelUIConst.DO_PLAY_ANIM, function(arg_24_0, arg_24_1)
		arg_13_0.doPlayAnim(arg_24_1.name, arg_24_1.callback, arg_24_1.onStart))
	arg_13_0.bind(LevelUIConst.HIDE_FLEET_SELECT, function()
		arg_13_0.hideFleetSelect())
	arg_13_0.bind(LevelUIConst.HIDE_FLEET_EDIT, function(arg_26_0)
		arg_13_0.hideFleetEdit())
	arg_13_0.bind(LevelUIConst.ADD_MSG_QUEUE, function(arg_27_0, arg_27_1)
		arg_13_0.addbubbleMsgBox(arg_27_1))
	arg_13_0.bind(LevelUIConst.SET_MAP, function(arg_28_0, arg_28_1)
		arg_13_0.setMap(arg_28_1))

def var_0_0.addbubbleMsgBox(arg_29_0, arg_29_1):
	table.insert(arg_29_0.bubbleMsgBoxes, arg_29_1)

	if #arg_29_0.bubbleMsgBoxes > 1:
		return

	local var_29_0

	local function var_29_1()
		local var_30_0 = arg_29_0.bubbleMsgBoxes[1]

		if var_30_0:
			var_30_0(function()
				table.remove(arg_29_0.bubbleMsgBoxes, 1)
				var_29_1())

	var_29_1()

def var_0_0.CleanBubbleMsgbox(arg_32_0):
	table.clean(arg_32_0.bubbleMsgBoxes)

def var_0_0.updatePtActivity(arg_33_0, arg_33_1):
	arg_33_0.ptActivity = arg_33_1

	arg_33_0.updateActivityRes()

def var_0_0.updateActivityRes(arg_34_0):
	local var_34_0 = findTF(arg_34_0.ptTotal, "Text")
	local var_34_1 = findTF(arg_34_0.ptTotal, "icon/Image")

	if var_34_0 and var_34_1 and arg_34_0.ptActivity:
		setText(var_34_0, "x" .. arg_34_0.ptActivity.data1)
		GetImageSpriteFromAtlasAsync(Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = tonumber(arg_34_0.ptActivity.getConfig("config_id"))
		}).getIcon(), "", var_34_1, True)

def var_0_0.setCommanderPrefabs(arg_35_0, arg_35_1):
	arg_35_0.commanderPrefabs = arg_35_1

def var_0_0.didEnter(arg_36_0):
	arg_36_0.openedCommanerSystem = not LOCK_COMMANDER and pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_36_0.player.level, "CommanderCatMediator")

	onButton(arg_36_0, arg_36_0.findTF("back_button", arg_36_0.topChapter), function()
		if arg_36_0.isfrozen():
			return

		local var_37_0 = arg_36_0.contextData.map

		if var_37_0 and (var_37_0.isActivity() or var_37_0.isEscort()):
			arg_36_0.emit(LevelMediator2.ON_SWITCH_NORMAL_MAP)

			return
		elif var_37_0 and var_37_0.isSkirmish():
			arg_36_0.emit(var_0_0.ON_BACK)
		elif not arg_36_0.contextData.entranceStatus:
			arg_36_0.ShowEntranceUI(True)
		else
			arg_36_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_36_0, arg_36_0.btnSpecial, function()
		if arg_36_0.isfrozen():
			return

		arg_36_0.emit(LevelMediator2.ON_OPEN_EVENT_SCENE), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.dailyBtn, function()
		if arg_36_0.isfrozen():
			return

		DailyLevelProxy.dailyLevelId = None

		arg_36_0.updatDailyBtnTip()
		arg_36_0.emit(LevelMediator2.ON_DAILY_LEVEL), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.challengeBtn, function()
		if arg_36_0.isfrozen():
			return

		local var_40_0, var_40_1 = arg_36_0.checkChallengeOpen()

		if var_40_0 == False:
			pg.TipsMgr.GetInstance().ShowTips(var_40_1)
		else
			arg_36_0.emit(LevelMediator2.CLICK_CHALLENGE_BTN), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.militaryExerciseBtn, function()
		if arg_36_0.isfrozen():
			return

		arg_36_0.emit(LevelMediator2.ON_OPEN_MILITARYEXERCISE), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.normalBtn, function()
		if arg_36_0.isfrozen():
			return

		arg_36_0.setMap(arg_36_0.contextData.map.getBindMapId()), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.eliteBtn, function()
		if arg_36_0.isfrozen():
			return

		if arg_36_0.contextData.map.getBindMapId() == 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("elite_disable_unusable"))

			local var_43_0 = getProxy(ChapterProxy).getUseableMaxEliteMap()

			if var_43_0:
				arg_36_0.setMap(var_43_0.configId)
				pg.TipsMgr.GetInstance().ShowTips(i18n("elite_warp_to_latest_map"))
		elif arg_36_0.contextData.map.isEliteEnabled():
			arg_36_0.setMap(arg_36_0.contextData.map.getBindMapId())
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("elite_disable_unsatisfied")), SFX_UI_WEIGHANCHOR_HARD)
	onButton(arg_36_0, arg_36_0.remasterBtn, function()
		if arg_36_0.isfrozen():
			return

		arg_36_0.displayRemasterPanel()
		getProxy(ChapterProxy).setRemasterTip(False)
		arg_36_0.updateRemasterBtnTip(), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.entranceLayer.Find("enters/enter_main"), function()
		if arg_36_0.isfrozen():
			return

		arg_36_0.ShowSelectedMap(arg_36_0.GetInitializeMap()), SFX_PANEL)
	setText(arg_36_0.entranceLayer.Find("enters/enter_main/Text"), getProxy(ChapterProxy).getLastUnlockMap().getLastUnlockChapterName())
	onButton(arg_36_0, arg_36_0.entranceLayer.Find("enters/enter_world/enter"), function()
		if arg_36_0.isfrozen():
			return

		arg_36_0.emit(LevelMediator2.ENTER_WORLD), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.entranceLayer.Find("enters/enter_ready/activity"), function()
		if arg_36_0.isfrozen():
			return

		local var_47_0 = getProxy(ActivityProxy).getEnterReadyActivity()

		switch(var_47_0.getConfig("type"), {
			[ActivityConst.ACTIVITY_TYPE_ZPROJECT] = function()
				arg_36_0.emit(LevelMediator2.ON_ACTIVITY_MAP),
			[ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2] = function()
				arg_36_0.emit(LevelMediator2.ON_OPEN_ACT_BOSS_BATTLE),
			[ActivityConst.ACTIVITY_TYPE_BOSSRUSH] = function()
				arg_36_0.emit(LevelMediator2.ON_BOSSRUSH_MAP),
			[ActivityConst.ACTIVITY_TYPE_BOSSSINGLE] = function()
				arg_36_0.emit(LevelMediator2.ON_BOSSSINGLE_MAP, {
					mode = OtherworldMapScene.MODE_BATTLE
				})
		}), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.entranceLayer.Find("btns/btn_remaster"), function()
		if arg_36_0.isfrozen():
			return

		arg_36_0.displayRemasterPanel()
		getProxy(ChapterProxy).setRemasterTip(False)
		arg_36_0.updateRemasterBtnTip(), SFX_PANEL)
	setActive(arg_36_0.entranceLayer.Find("btns/btn_remaster"), OPEN_REMASTER)
	onButton(arg_36_0, arg_36_0.entranceLayer.Find("btns/btn_challenge"), function()
		if arg_36_0.isfrozen():
			return

		local var_53_0, var_53_1 = arg_36_0.checkChallengeOpen()

		if var_53_0 == False:
			pg.TipsMgr.GetInstance().ShowTips(var_53_1)
		else
			arg_36_0.emit(LevelMediator2.CLICK_CHALLENGE_BTN), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.entranceLayer.Find("btns/btn_pvp"), function()
		if arg_36_0.isfrozen():
			return

		arg_36_0.emit(LevelMediator2.ON_OPEN_MILITARYEXERCISE), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.entranceLayer.Find("btns/btn_daily"), function()
		if arg_36_0.isfrozen():
			return

		DailyLevelProxy.dailyLevelId = None

		arg_36_0.updatDailyBtnTip()
		arg_36_0.emit(LevelMediator2.ON_DAILY_LEVEL), SFX_PANEL)
	onButton(arg_36_0, arg_36_0.entranceLayer.Find("btns/btn_task"), function()
		if arg_36_0.isfrozen():
			return

		arg_36_0.emit(LevelMediator2.ON_OPEN_EVENT_SCENE), SFX_PANEL)
	setActive(arg_36_0.entranceLayer.Find("enters/enter_world/enter"), not WORLD_ENTER_LOCK)
	setActive(arg_36_0.entranceLayer.Find("enters/enter_world/nothing"), WORLD_ENTER_LOCK)

	local var_36_0 = getProxy(ActivityProxy).getEnterReadyActivity()

	setActive(arg_36_0.entranceLayer.Find("enters/enter_ready/nothing"), not tobool(var_36_0))
	setActive(arg_36_0.entranceLayer.Find("enters/enter_ready/activity"), tobool(var_36_0))

	if tobool(var_36_0):
		local var_36_1 = var_36_0.getConfig("config_client").entrance_bg

		if var_36_1:
			GetImageSpriteFromAtlasAsync(var_36_1, "", arg_36_0.entranceLayer.Find("enters/enter_ready/activity"), True)

	local var_36_2 = pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_36_0.player.level, "EventMediator")

	setActive(arg_36_0.btnSpecial.Find("lock"), not var_36_2)
	setActive(arg_36_0.entranceLayer.Find("btns/btn_task/lock"), not var_36_2)

	local var_36_3 = pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_36_0.player.level, "DailyLevelMediator")

	setActive(arg_36_0.dailyBtn.Find("lock"), not var_36_3)
	setActive(arg_36_0.entranceLayer.Find("btns/btn_daily/lock"), not var_36_3)

	local var_36_4 = pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_36_0.player.level, "MilitaryExerciseMediator")

	setActive(arg_36_0.militaryExerciseBtn.Find("lock"), not var_36_4)
	setActive(arg_36_0.entranceLayer.Find("btns/btn_pvp/lock"), not var_36_4)

	local var_36_5 = LimitChallengeConst.IsOpen()

	setActive(arg_36_0.challengeBtn.Find("lock"), not var_36_5)
	setActive(arg_36_0.entranceLayer.Find("btns/btn_challenge/lock"), not var_36_5)

	local var_36_6 = LimitChallengeConst.IsInAct()

	setActive(arg_36_0.challengeBtn, var_36_6)
	setActive(arg_36_0.entranceLayer.Find("btns/btn_challenge"), var_36_6)

	local var_36_7 = LimitChallengeConst.IsShowRedPoint()

	setActive(arg_36_0.entranceLayer.Find("btns/btn_challenge/tip"), var_36_7)
	arg_36_0.initMapBtn(arg_36_0.btnPrev, -1)
	arg_36_0.initMapBtn(arg_36_0.btnNext, 1)

	if arg_36_0.contextData.editEliteChapter:
		local var_36_8 = getProxy(ChapterProxy).getChapterById(arg_36_0.contextData.editEliteChapter)

		arg_36_0.displayFleetEdit(var_36_8)

		arg_36_0.contextData.editEliteChapter = None
	elif arg_36_0.contextData.selectedChapterVO:
		arg_36_0.displayFleetSelect(arg_36_0.contextData.selectedChapterVO)

		arg_36_0.contextData.selectedChapterVO = None

	local var_36_9 = arg_36_0.contextData.chapterVO

	if not var_36_9 or not var_36_9.active:
		arg_36_0.tryPlaySubGuide()

	arg_36_0.updateRemasterBtnTip()
	arg_36_0.updatDailyBtnTip()

	if arg_36_0.contextData.open_remaster:
		arg_36_0.displayRemasterPanel(arg_36_0.contextData.isSP)

		arg_36_0.contextData.open_remaster = None

	arg_36_0.ShowEntranceUI(arg_36_0.contextData.entranceStatus)

	if not arg_36_0.contextData.entranceStatus:
		arg_36_0.emit(LevelMediator2.ON_ENTER_MAINLEVEL, arg_36_0.GetInitializeMap())

	arg_36_0.emit(LevelMediator2.ON_DIDENTER)

def var_0_0.checkChallengeOpen(arg_57_0):
	local var_57_0 = getProxy(PlayerProxy).getRawData().level

	return pg.SystemOpenMgr.GetInstance().isOpenSystem(var_57_0, "ChallengeMainMediator")

def var_0_0.tryPlaySubGuide(arg_58_0):
	if arg_58_0.contextData.map and arg_58_0.contextData.map.isSkirmish():
		return

	pg.SystemGuideMgr.GetInstance().Play(arg_58_0)

def var_0_0.onBackPressed(arg_59_0):
	if arg_59_0.isfrozen():
		return

	if arg_59_0.levelAmbushView:
		return

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	if arg_59_0.levelInfoView.isShowing():
		arg_59_0.hideChapterPanel()

		return

	if arg_59_0.levelFleetView.isShowing():
		arg_59_0.hideFleetEdit()

		return

	if arg_59_0.levelStrategyView:
		arg_59_0.hideStrategyInfo()

		return

	if arg_59_0.levelRepairView:
		arg_59_0.hideRepairWindow()

		return

	if arg_59_0.levelRemasterView.isShowing():
		arg_59_0.hideRemasterPanel()

		return

	if isActive(arg_59_0.helpPage):
		setActive(arg_59_0.helpPage, False)

		return

	local var_59_0 = arg_59_0.contextData.chapterVO
	local var_59_1 = getProxy(ChapterProxy).getActiveChapter()

	if var_59_0 and var_59_1:
		arg_59_0.switchToMap()

		return

	triggerButton(arg_59_0.findTF("back_button", arg_59_0.topChapter))

def var_0_0.ShowEntranceUI(arg_60_0, arg_60_1):
	setActive(arg_60_0.entranceLayer, arg_60_1)
	setActive(arg_60_0.entranceBg, arg_60_1)
	setActive(arg_60_0.map, not arg_60_1)
	setActive(arg_60_0.float, not arg_60_1)
	setActive(arg_60_0.mainLayer, not arg_60_1)
	setActive(arg_60_0.topChapter.Find("type_entrance"), arg_60_1)

	arg_60_0.contextData.entranceStatus = tobool(arg_60_1)

	if arg_60_1:
		setActive(arg_60_0.topChapter.Find("title_chapter"), False)
		setActive(arg_60_0.topChapter.Find("type_chapter"), False)
		setActive(arg_60_0.topChapter.Find("type_escort"), False)
		setActive(arg_60_0.topChapter.Find("type_skirmish"), False)

		if arg_60_0.newChapterCDTimer:
			arg_60_0.newChapterCDTimer.Stop()

			arg_60_0.newChapterCDTimer = None

		arg_60_0.RecordLastMapOnExit()

		arg_60_0.contextData.mapIdx = None
		arg_60_0.contextData.map = None

	arg_60_0.PlayBGM()

def var_0_0.PreloadLevelMainUI(arg_61_0, arg_61_1, arg_61_2):
	if arg_61_0.preloadLevelDone:
		existCall(arg_61_2)

		return

	local var_61_0

	local function var_61_1()
		if not arg_61_0.exited:
			arg_61_0.preloadLevelDone = True

			existCall(arg_61_2)

	local var_61_2 = getProxy(ChapterProxy).getMapById(arg_61_1)
	local var_61_3 = arg_61_0.GetMapBG(var_61_2)

	table.ParallelIpairsAsync(var_61_3, function(arg_63_0, arg_63_1, arg_63_2)
		GetSpriteFromAtlasAsync("levelmap/" .. arg_63_1.BG, "", arg_63_2), var_61_1)

def var_0_0.selectMap(arg_64_0):
	local var_64_0 = arg_64_0.contextData.mapIdx

	if not var_64_0:
		local var_64_1 = getProxy(ChapterProxy)
		local var_64_2 = Map.lastMap and var_64_1.getMapById(Map.lastMap)

		if var_64_2 and var_64_2.isUnlock():
			var_64_0 = Map.lastMap
		else
			var_64_0 = var_64_1.getLastUnlockMap().id

	return var_64_0

def var_0_0.setShips(arg_65_0, arg_65_1):
	arg_65_0.shipVOs = arg_65_1

def var_0_0.updateRes(arg_66_0, arg_66_1):
	if arg_66_0.levelStageView:
		arg_66_0.levelStageView.ActionInvoke("SetPlayer", arg_66_1)

	arg_66_0.player = arg_66_1

def var_0_0.setEliteQuota(arg_67_0, arg_67_1, arg_67_2):
	local var_67_0 = arg_67_2 - arg_67_1
	local var_67_1 = arg_67_0.findTF("bg/Text", arg_67_0.eliteQuota).GetComponent(typeof(Text))

	if arg_67_1 == arg_67_2:
		var_67_1.color = Color.red
	else
		var_67_1.color = Color.New(0.47, 0.89, 0.27)

	var_67_1.text = var_67_0 .. "/" .. arg_67_2

def var_0_0.updateEvent(arg_68_0, arg_68_1):
	local var_68_0 = arg_68_1.hasFinishState()

	setActive(arg_68_0.btnSpecial.Find("tip"), var_68_0)
	setActive(arg_68_0.entranceLayer.Find("btns/btn_task/tip"), var_68_0)

def var_0_0.updateFleet(arg_69_0, arg_69_1):
	arg_69_0.fleets = arg_69_1

def var_0_0.updateChapterVO(arg_70_0, arg_70_1, arg_70_2):
	local var_70_0 = arg_70_1.getConfig("map")

	if not arg_70_0.contextData.chapterVO and arg_70_0.contextData.mapIdx == var_70_0 and bit.band(arg_70_2, ChapterConst.DirtyMapItems) > 0:
		arg_70_0.updateMapItems()

	if arg_70_0.contextData.chapterVO and arg_70_0.contextData.chapterVO.id == arg_70_1.id and arg_70_1.active:
		arg_70_0.setChapter(arg_70_1)

	if arg_70_0.contextData.chapterVO and arg_70_0.contextData.chapterVO.id == arg_70_1.id and arg_70_1.active and arg_70_0.levelStageView and arg_70_0.grid:
		local var_70_1 = False
		local var_70_2 = False
		local var_70_3 = False

		if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyFleet) > 0:
			arg_70_0.levelStageView.updateStageFleet()
			arg_70_0.levelStageView.updateAmbushRate(arg_70_1.fleet.line, True)

			var_70_3 = True

			if arg_70_0.grid:
				arg_70_0.grid.RefreshFleetCells()
				arg_70_0.grid.UpdateFloor()

				var_70_1 = True

		if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyChampion) > 0:
			var_70_3 = True

			if arg_70_0.grid:
				arg_70_0.grid.UpdateFleets()
				arg_70_0.grid.clearChampions()
				arg_70_0.grid.initChampions()

				var_70_2 = True
		elif bit.band(arg_70_2, ChapterConst.DirtyChampionPosition) > 0:
			var_70_3 = True

			if arg_70_0.grid:
				arg_70_0.grid.UpdateFleets()
				arg_70_0.grid.updateChampions()

				var_70_2 = True

		if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyAchieve) > 0:
			arg_70_0.levelStageView.updateStageAchieve()

		if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyAttachment) > 0:
			arg_70_0.levelStageView.updateAmbushRate(arg_70_1.fleet.line, True)

			if arg_70_0.grid:
				if not (arg_70_2 < 0) and not (bit.band(arg_70_2, ChapterConst.DirtyFleet) > 0):
					arg_70_0.grid.updateFleet(arg_70_1.fleets[arg_70_1.findex].id)

				arg_70_0.grid.updateAttachments()

				if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyAutoAction) > 0:
					arg_70_0.grid.updateQuadCells(ChapterConst.QuadStateNormal)
				else
					var_70_1 = True

		if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyStrategy) > 0:
			arg_70_0.levelStageView.updateStageStrategy()

			var_70_3 = True

			arg_70_0.levelStageView.updateStageBarrier()
			arg_70_0.levelStageView.UpdateAutoFightPanel()

		if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyAutoAction) > 0:
			-- block empty
		elif var_70_1:
			arg_70_0.grid.updateQuadCells(ChapterConst.QuadStateNormal)
		elif var_70_2:
			arg_70_0.grid.updateQuadCells(ChapterConst.QuadStateFrozen)

		if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyCellFlag) > 0:
			arg_70_0.grid.UpdateFloor()

		if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyBase) > 0:
			arg_70_0.levelStageView.UpdateDefenseStatus()

		if arg_70_2 < 0 or bit.band(arg_70_2, ChapterConst.DirtyFloatItems) > 0:
			arg_70_0.grid.UpdateItemCells()

		if var_70_3:
			arg_70_0.levelStageView.updateFleetBuff()

def var_0_0.updateClouds(arg_71_0):
	arg_71_0.cloudRTFs = {}
	arg_71_0.cloudRects = {}
	arg_71_0.cloudTimer = {}

	for iter_71_0 = 1, 6:
		local var_71_0 = arg_71_0.findTF("cloud_" .. iter_71_0, arg_71_0.clouds)
		local var_71_1 = rtf(var_71_0)

		table.insert(arg_71_0.cloudRTFs, var_71_1)
		table.insert(arg_71_0.cloudRects, var_71_1.rect.width)

	arg_71_0.initCloudsPos()

	for iter_71_1, iter_71_2 in ipairs(arg_71_0.cloudRTFs):
		local var_71_2 = arg_71_0.cloudRects[iter_71_1]
		local var_71_3 = arg_71_0.initPositions[iter_71_1] or Vector2(0, 0)
		local var_71_4 = 30 - var_71_3.y / 20
		local var_71_5 = (arg_71_0.mapWidth + var_71_2) / var_71_4
		local var_71_6

		var_71_6 = LeanTween.moveX(iter_71_2, arg_71_0.mapWidth, var_71_5).setRepeat(-1).setOnCompleteOnRepeat(True).setOnComplete(System.Action(function()
			var_71_2 = arg_71_0.cloudRects[iter_71_1]
			iter_71_2.anchoredPosition = Vector2(-var_71_2, var_71_3.y)

			var_71_6.setFrom(-var_71_2).setTime((arg_71_0.mapWidth + var_71_2) / var_71_4)))
		var_71_6.passed = math.random() * var_71_5
		arg_71_0.cloudTimer[iter_71_1] = var_71_6.uniqueId

def var_0_0.RefreshMapBG(arg_73_0):
	arg_73_0.PlayBGM()
	arg_73_0.SwitchMapBG(arg_73_0.contextData.map, arg_73_0.lastMapIdx, True)

def var_0_0.updateCouldAnimator(arg_74_0, arg_74_1, arg_74_2):
	if arg_74_1:
		local var_74_0 = arg_74_0.contextData.map.getConfig("ani_controller")

		local function var_74_1(arg_75_0)
			arg_75_0 = tf(arg_75_0)

			local var_75_0 = Vector3.one

			if arg_75_0.rect.width > 0 and arg_75_0.rect.height > 0:
				var_75_0.x = arg_75_0.parent.rect.width / arg_75_0.rect.width
				var_75_0.y = arg_75_0.parent.rect.height / arg_75_0.rect.height

			arg_75_0.localScale = var_75_0

			if var_74_0 and #var_74_0 > 0:
				(function()
					for iter_76_0, iter_76_1 in ipairs(var_74_0):
						if iter_76_1[1] == var_0_2:
							local var_76_0 = iter_76_1[2][1]
							local var_76_1 = _.rest(iter_76_1[2], 2)

							for iter_76_2, iter_76_3 in ipairs(var_76_1):
								local var_76_2 = arg_75_0.Find(iter_76_3)

								if not IsNil(var_76_2):
									local var_76_3 = getProxy(ChapterProxy).GetChapterItemById(var_76_0)

									if var_76_3 and not var_76_3.isClear():
										setActive(var_76_2, False)
						elif iter_76_1[1] == var_0_3:
							local var_76_4 = iter_76_1[2][1]
							local var_76_5 = _.rest(iter_76_1[2], 2)

							for iter_76_4, iter_76_5 in ipairs(var_76_5):
								local var_76_6 = arg_75_0.Find(iter_76_5)

								if not IsNil(var_76_6):
									local var_76_7 = getProxy(ChapterProxy).GetChapterItemById(var_76_4)

									if var_76_7 and not var_76_7.isClear():
										setActive(var_76_6, True)

										return
						elif iter_76_1[1] == var_0_4:
							local var_76_8 = iter_76_1[2][1]
							local var_76_9 = _.rest(iter_76_1[2], 2)

							for iter_76_6, iter_76_7 in ipairs(var_76_9):
								local var_76_10 = arg_75_0.Find(iter_76_7)

								if not IsNil(var_76_10):
									local var_76_11 = getProxy(ChapterProxy).GetChapterItemById(var_76_8)

									if var_76_11 and not var_76_11.isClear():
										setActive(var_76_10, True))()

		local var_74_2 = arg_74_0.loader.GetPrefab("ui/" .. arg_74_1, arg_74_1, function(arg_77_0)
			arg_77_0.SetActive(True)

			local var_77_0 = arg_74_0.mapTFs[arg_74_2]

			setParent(arg_77_0, var_77_0)
			pg.ViewUtils.SetSortingOrder(arg_77_0, ChapterConst.LayerWeightMap + arg_74_2 * 2 - 1)
			var_74_1(arg_77_0))

		table.insert(arg_74_0.mapGroup, var_74_2)

def var_0_0.updateMapItems(arg_78_0):
	local var_78_0 = arg_78_0.contextData.map
	local var_78_1 = var_78_0.getConfig("cloud_suffix")

	if var_78_1 == "":
		setActive(arg_78_0.clouds, False)
	else
		setActive(arg_78_0.clouds, True)

		for iter_78_0, iter_78_1 in ipairs(var_78_0.getConfig("clouds_pos")):
			local var_78_2 = arg_78_0.cloudRTFs[iter_78_0]
			local var_78_3 = var_78_2.GetComponent(typeof(Image))

			var_78_3.enabled = False

			GetSpriteFromAtlasAsync("clouds/cloud_" .. iter_78_0 .. "_" .. var_78_1, "", function(arg_79_0)
				if not arg_78_0.exited and not IsNil(var_78_3) and var_78_0 == arg_78_0.contextData.map:
					var_78_3.enabled = True
					var_78_3.sprite = arg_79_0

					var_78_3.SetNativeSize()

					arg_78_0.cloudRects[iter_78_0] = var_78_2.rect.width)

	arg_78_0.mapBuilder.buffer.UpdateMapItems(var_78_0)

def var_0_0.updateDifficultyBtns(arg_80_0):
	local var_80_0 = arg_80_0.contextData.map.getConfig("type")

	setActive(arg_80_0.normalBtn, var_80_0 == Map.ELITE)
	setActive(arg_80_0.eliteQuota, var_80_0 == Map.ELITE)
	setActive(arg_80_0.eliteBtn, var_80_0 == Map.SCENARIO)

	local var_80_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.ELITE_AWARD_ACTIVITY_ID)

	setActive(arg_80_0.eliteBtn.Find("pic_activity"), var_80_1 and not var_80_1.isEnd())

def var_0_0.updateActivityBtns(arg_81_0):
	local var_81_0, var_81_1 = arg_81_0.contextData.map.isActivity()
	local var_81_2 = arg_81_0.contextData.map.isRemaster()
	local var_81_3 = arg_81_0.contextData.map.isSkirmish()
	local var_81_4 = arg_81_0.contextData.map.isEscort()
	local var_81_5 = arg_81_0.contextData.map.getConfig("type")
	local var_81_6 = getProxy(ActivityProxy).GetEarliestActByType(ActivityConst.ACTIVITY_TYPE_ZPROJECT)
	local var_81_7 = var_81_6 and not var_81_6.isEnd() and not var_81_0 and not var_81_3 and not var_81_4

	if var_81_7:
		local var_81_8 = setmetatable({}, MainActMapBtn)

		var_81_8.image = arg_81_0.activityBtn.Find("Image").GetComponent(typeof(Image))
		var_81_8.subImage = arg_81_0.activityBtn.Find("sub_Image").GetComponent(typeof(Image))
		var_81_8.tipTr = arg_81_0.activityBtn.Find("Tip").GetComponent(typeof(Image))
		var_81_8.tipTxt = arg_81_0.activityBtn.Find("Tip/Text").GetComponent(typeof(Text))
		var_81_7 = var_81_8.InShowTime()

		if var_81_7:
			var_81_8.InitTipImage()
			var_81_8.InitSubImage()
			var_81_8.InitImage(function()
				return)
			var_81_8.OnInit()

	setActive(arg_81_0.activityBtn, var_81_7)
	arg_81_0.updateRemasterInfo()

	if var_81_0 and var_81_1:
		local var_81_9 = getProxy(ChapterProxy).getMapsByActivities()
		local var_81_10 = underscore.any(var_81_9, function(arg_83_0)
			return arg_83_0.isActExtra())

		setActive(arg_81_0.actExtraBtn, var_81_10 and not var_81_2 and var_81_5 != Map.ACT_EXTRA)

		if isActive(arg_81_0.actExtraBtn):
			if underscore.all(underscore.filter(var_81_9, function(arg_84_0)
				local var_84_0 = arg_84_0.getMapType()

				return var_84_0 == Map.ACTIVITY_EASY or var_84_0 == Map.ACTIVITY_HARD), function(arg_85_0)
				return arg_85_0.isAllChaptersClear()):
				setActive(arg_81_0.actExtraBtnAnim, True)
			else
				setActive(arg_81_0.actExtraBtnAnim, False)

			setActive(arg_81_0.actExtraBtn.Find("Tip"), getProxy(ChapterProxy).IsActivitySPChapterActive() and SettingsProxy.IsShowActivityMapSPTip())

		local var_81_11 = checkExist(arg_81_0.contextData.map.getBindMap(), {
			"isHardMap"
		})

		setActive(arg_81_0.actEliteBtn, var_81_11 and var_81_5 != Map.ACTIVITY_HARD)
		setActive(arg_81_0.actNormalBtn, var_81_5 != Map.ACTIVITY_EASY)
		setActive(arg_81_0.actExtraRank, var_81_5 == Map.ACT_EXTRA)
		setActive(arg_81_0.actExchangeShopBtn, not var_81_2 and var_81_1 and not ActivityConst.HIDE_PT_PANELS)
		setActive(arg_81_0.ptTotal, not var_81_2 and var_81_1 and not ActivityConst.HIDE_PT_PANELS and arg_81_0.ptActivity and not arg_81_0.ptActivity.isEnd())
		arg_81_0.updateActivityRes()
	else
		setActive(arg_81_0.actExtraBtn, False)
		setActive(arg_81_0.actEliteBtn, False)
		setActive(arg_81_0.actNormalBtn, False)
		setActive(arg_81_0.actExtraRank, False)
		setActive(arg_81_0.actExchangeShopBtn, False)
		setActive(arg_81_0.actAtelierBuffBtn, False)
		setActive(arg_81_0.ptTotal, False)

	setActive(arg_81_0.eventContainer, (not var_81_0 or not var_81_1) and not var_81_4)
	setActive(arg_81_0.remasterBtn, OPEN_REMASTER and (var_81_2 or not var_81_0 and not var_81_4 and not var_81_3))
	setActive(arg_81_0.ticketTxt.parent, var_81_2)
	arg_81_0.updateRemasterTicket()
	arg_81_0.updateCountDown()
	arg_81_0.registerActBtn()

	if var_81_0 and var_81_5 != Map.ACT_EXTRA:
		Map.lastMapForActivity = arg_81_0.contextData.mapIdx

def var_0_0.updateRemasterTicket(arg_86_0):
	setText(arg_86_0.ticketTxt, getProxy(ChapterProxy).remasterTickets .. " / " .. pg.gameset.reactivity_ticket_max.key_value)
	arg_86_0.emit(LevelUIConst.FLUSH_REMASTER_TICKET)

def var_0_0.updateRemasterBtnTip(arg_87_0):
	local var_87_0 = getProxy(ChapterProxy)
	local var_87_1 = var_87_0.ifShowRemasterTip() or var_87_0.anyRemasterAwardCanReceive()

	SetActive(arg_87_0.remasterBtn.Find("tip"), var_87_1)
	SetActive(arg_87_0.entranceLayer.Find("btns/btn_remaster/tip"), var_87_1)

def var_0_0.updatDailyBtnTip(arg_88_0):
	local var_88_0 = getProxy(DailyLevelProxy).ifShowDailyTip()

	SetActive(arg_88_0.dailyBtn.Find("tip"), var_88_0)
	SetActive(arg_88_0.entranceLayer.Find("btns/btn_daily/tip"), var_88_0)

def var_0_0.updateRemasterInfo(arg_89_0):
	arg_89_0.emit(LevelUIConst.FLUSH_REMASTER_INFO)

	if not arg_89_0.contextData.map:
		return

	local var_89_0 = getProxy(ChapterProxy)
	local var_89_1
	local var_89_2 = arg_89_0.contextData.map.getRemaster()

	if var_89_2 and #pg.re_map_template[var_89_2].drop_gain > 0:
		for iter_89_0, iter_89_1 in ipairs(pg.re_map_template[var_89_2].drop_gain):
			if #iter_89_1 > 0 and var_89_0.remasterInfo[iter_89_1[1]][iter_89_0].receive == False:
				var_89_1 = {
					iter_89_0,
					iter_89_1
				}

				break

	setActive(arg_89_0.remasterAwardBtn, var_89_1)

	if var_89_1:
		local var_89_3 = var_89_1[1]
		local var_89_4, var_89_5, var_89_6, var_89_7 = unpack(var_89_1[2])
		local var_89_8 = var_89_0.remasterInfo[var_89_4][var_89_3]

		setText(arg_89_0.remasterAwardBtn.Find("Text"), var_89_8.count .. "/" .. var_89_7)
		updateDrop(arg_89_0.remasterAwardBtn.Find("IconTpl"), {
			type = var_89_5,
			id = var_89_6
		})
		setActive(arg_89_0.remasterAwardBtn.Find("tip"), var_89_7 <= var_89_8.count)
		onButton(arg_89_0, arg_89_0.remasterAwardBtn, function()
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideYes = True,
				hideNo = True,
				type = MSGBOX_TYPE_SINGLE_ITEM,
				drop = {
					type = var_89_5,
					id = var_89_6
				},
				weight = LayerWeightConst.TOP_LAYER,
				remaster = {
					word = i18n("level_remaster_tip4", pg.chapter_template[var_89_4].chapter_name),
					number = var_89_8.count .. "/" .. var_89_7,
					btn_text = i18n(var_89_8.count < var_89_7 and "level_remaster_tip2" or "level_remaster_tip3"),
					def btn_call:()
						if var_89_8.count < var_89_7:
							local var_91_0 = pg.chapter_template[var_89_4].map
							local var_91_1, var_91_2 = var_89_0.getMapById(var_91_0).isUnlock()

							if not var_91_1:
								pg.TipsMgr.GetInstance().ShowTips(var_91_2)
							else
								arg_89_0.ShowSelectedMap(var_91_0)
						else
							arg_89_0.emit(LevelMediator2.ON_CHAPTER_REMASTER_AWARD, var_89_4, var_89_3)
				}
			}), SFX_PANEL)

def var_0_0.updateCountDown(arg_92_0):
	local var_92_0 = getProxy(ChapterProxy)

	if arg_92_0.newChapterCDTimer:
		arg_92_0.newChapterCDTimer.Stop()

		arg_92_0.newChapterCDTimer = None

	local var_92_1 = 0

	if arg_92_0.contextData.map.isActivity() and not arg_92_0.contextData.map.isRemaster():
		local var_92_2 = var_92_0.getMapsByActivities()

		_.each(var_92_2, function(arg_93_0)
			local var_93_0 = arg_93_0.getChapterTimeLimit()

			if var_92_1 == 0:
				var_92_1 = var_93_0
			else
				var_92_1 = math.min(var_92_1, var_93_0))
		setActive(arg_92_0.countDown, var_92_1 > 0)
		setText(arg_92_0.countDown.Find("title"), i18n("levelScene_new_chapter_coming"))
	else
		setActive(arg_92_0.countDown, False)

	if var_92_1 > 0:
		setText(arg_92_0.countDown.Find("time"), pg.TimeMgr.GetInstance().DescCDTime(var_92_1))

		arg_92_0.newChapterCDTimer = Timer.New(function()
			var_92_1 = var_92_1 - 1

			if var_92_1 <= 0:
				arg_92_0.updateCountDown()

				if not arg_92_0.contextData.chapterVO:
					arg_92_0.setMap(arg_92_0.contextData.mapIdx)
			else
				setText(arg_92_0.countDown.Find("time"), pg.TimeMgr.GetInstance().DescCDTime(var_92_1)), 1, -1)

		arg_92_0.newChapterCDTimer.Start()
	else
		setText(arg_92_0.countDown.Find("time"), "")

def var_0_0.registerActBtn(arg_95_0):
	if arg_95_0.isRegisterBtn:
		return

	arg_95_0.isRegisterBtn = True

	onButton(arg_95_0, arg_95_0.actExtraRank, function()
		if arg_95_0.isfrozen():
			return

		arg_95_0.emit(LevelMediator2.ON_EXTRA_RANK), SFX_PANEL)
	onButton(arg_95_0, arg_95_0.activityBtn, function()
		if arg_95_0.isfrozen():
			return

		arg_95_0.emit(LevelMediator2.ON_ACTIVITY_MAP), SFX_UI_CLICK)
	onButton(arg_95_0, arg_95_0.actExchangeShopBtn, function()
		if arg_95_0.isfrozen():
			return

		arg_95_0.emit(LevelMediator2.GO_ACT_SHOP), SFX_UI_CLICK)
	onButton(arg_95_0, arg_95_0.actAtelierBuffBtn, function()
		if arg_95_0.isfrozen():
			return

		arg_95_0.emit(LevelMediator2.SHOW_ATELIER_BUFF), SFX_UI_CLICK)

	local var_95_0 = getProxy(ChapterProxy)

	local function var_95_1(arg_100_0, arg_100_1, arg_100_2)
		local var_100_0

		if arg_100_0.isRemaster():
			var_100_0 = var_95_0.getRemasterMaps(arg_100_0.remasterId)
		else
			var_100_0 = var_95_0.getMapsByActivities()

		local var_100_1 = _.select(var_100_0, function(arg_101_0)
			return arg_101_0.getMapType() == arg_100_1)

		table.sort(var_100_1, function(arg_102_0, arg_102_1)
			return arg_102_0.id < arg_102_1.id)

		local var_100_2 = table.indexof(underscore.map(var_100_1, function(arg_103_0)
			return arg_103_0.id), arg_100_2) or #var_100_1

		while not var_100_1[var_100_2].isUnlock():
			if var_100_2 > 1:
				var_100_2 = var_100_2 - 1
			else
				break

		return var_100_1[var_100_2]

	local function var_95_2()
		if arg_95_0.isfrozen():
			return

		local var_104_0 = arg_95_0.contextData.map.getBindMapId()
		local var_104_1 = var_95_1(arg_95_0.contextData.map, Map.ACTIVITY_HARD, var_104_0)
		local var_104_2, var_104_3 = var_104_1.isUnlock()

		if var_104_2:
			arg_95_0.setMap(var_104_1.id)
		else
			pg.TipsMgr.GetInstance().ShowTips(var_104_3)

	onButton(arg_95_0, arg_95_0.actEliteBtn, var_95_2, SFX_PANEL)
	arg_95_0.bind(LevelUIConst.SWITCH_CHALLENGE_MAP, var_95_2)
	onButton(arg_95_0, arg_95_0.actNormalBtn, function()
		if arg_95_0.isfrozen():
			return

		local var_105_0 = arg_95_0.contextData.map.getBindMapId()
		local var_105_1 = var_95_1(arg_95_0.contextData.map, Map.ACTIVITY_EASY, var_105_0)
		local var_105_2, var_105_3 = var_105_1.isUnlock()

		if var_105_2:
			arg_95_0.setMap(var_105_1.id)
		else
			pg.TipsMgr.GetInstance().ShowTips(var_105_3), SFX_PANEL)
	onButton(arg_95_0, arg_95_0.actExtraBtn, function()
		if arg_95_0.isfrozen():
			return

		local var_106_0 = PlayerPrefs.HasKey("ex_mapId") and PlayerPrefs.GetInt("ex_mapId", 0) or 0
		local var_106_1 = var_95_1(arg_95_0.contextData.map, Map.ACT_EXTRA, var_106_0)
		local var_106_2, var_106_3 = var_106_1.isUnlock()

		if var_106_2:
			arg_95_0.setMap(var_106_1.id)
		else
			pg.TipsMgr.GetInstance().ShowTips(var_106_3), SFX_PANEL)

def var_0_0.initCloudsPos(arg_107_0, arg_107_1):
	arg_107_0.initPositions = {}

	local var_107_0 = arg_107_1 or 1
	local var_107_1 = pg.expedition_data_by_map[var_107_0].clouds_pos

	for iter_107_0, iter_107_1 in ipairs(arg_107_0.cloudRTFs):
		local var_107_2 = var_107_1[iter_107_0]

		if var_107_2:
			iter_107_1.anchoredPosition = Vector2(var_107_2[1], var_107_2[2])

			table.insert(arg_107_0.initPositions, iter_107_1.anchoredPosition)
		else
			setActive(iter_107_1, False)

def var_0_0.initMapBtn(arg_108_0, arg_108_1, arg_108_2):
	onButton(arg_108_0, arg_108_1, function()
		if arg_108_0.isfrozen():
			return

		local var_109_0 = arg_108_0.contextData.mapIdx + arg_108_2
		local var_109_1 = getProxy(ChapterProxy).getMapById(var_109_0)

		if not var_109_1:
			return

		if var_109_1.getMapType() == Map.ELITE and not var_109_1.isEliteEnabled():
			var_109_1 = var_109_1.getBindMap()
			var_109_0 = var_109_1.id

			pg.TipsMgr.GetInstance().ShowTips(i18n("elite_disable_unusable"))

		local var_109_2, var_109_3 = var_109_1.isUnlock()

		if arg_108_2 > 0 and not var_109_2:
			pg.TipsMgr.GetInstance().ShowTips(var_109_3)

			return

		arg_108_0.setMap(var_109_0), SFX_PANEL)

def var_0_0.ShowSelectedMap(arg_110_0, arg_110_1, arg_110_2):
	seriesAsync({
		function(arg_111_0)
			if arg_110_0.contextData.entranceStatus:
				arg_110_0.frozen()

				arg_110_0.nextPreloadMap = arg_110_1

				arg_110_0.PreloadLevelMainUI(arg_110_1, function()
					arg_110_0.unfrozen()

					if arg_110_0.nextPreloadMap != arg_110_1:
						return

					arg_110_0.emit(LevelMediator2.ON_ENTER_MAINLEVEL, arg_110_1)
					arg_110_0.ShowEntranceUI(False)
					arg_111_0())
			else
				arg_110_0.setMap(arg_110_1)
				arg_111_0()
	}, arg_110_2)

def var_0_0.setMap(arg_113_0, arg_113_1):
	arg_113_0.lastMapIdx = arg_113_0.contextData.mapIdx
	arg_113_0.contextData.mapIdx = arg_113_1
	arg_113_0.contextData.map = getProxy(ChapterProxy).getMapById(arg_113_1)

	assert(arg_113_0.contextData.map, "map cannot be None " .. arg_113_1)

	if arg_113_0.contextData.map.getMapType() == Map.ACT_EXTRA:
		PlayerPrefs.SetInt("ex_mapId", arg_113_0.contextData.map.id)
		PlayerPrefs.Save()
	elif arg_113_0.contextData.map.isRemaster():
		PlayerPrefs.SetInt("remaster_lastmap_" .. arg_113_0.contextData.map.remasterId, arg_113_1)
		PlayerPrefs.Save()

	arg_113_0.updateMap()
	arg_113_0.tryPlayMapStory()

local var_0_5 = import("view.level.MapBuilder.MapBuilder")
local var_0_6 = {
	default = "MapBuilderNormal",
	[var_0_5.TYPENORMAL] = "MapBuilderNormal",
	[var_0_5.TYPEESCORT] = "MapBuilderEscort",
	[var_0_5.TYPESHINANO] = "MapBuilderShinano",
	[var_0_5.TYPESKIRMISH] = "MapBuilderSkirmish",
	[var_0_5.TYPEBISMARCK] = "MapBuilderBismarck",
	[var_0_5.TYPESSSS] = "MapBuilderSSSS",
	[var_0_5.TYPEATELIER] = "MapBuilderAtelier",
	[var_0_5.TYPESENRANKAGURA] = "MapBuilderSenrankagura"
}

def var_0_0.SwitchMapBuilder(arg_114_0, arg_114_1):
	if arg_114_0.mapBuilder and arg_114_0.mapBuilder.GetType() != arg_114_1:
		arg_114_0.mapBuilder.buffer.Hide()

	local var_114_0 = arg_114_0.GetMapBuilderInBuffer(arg_114_1)

	arg_114_0.mapBuilder = var_114_0

	var_114_0.buffer.Show()
	var_114_0.buffer.ShowButtons()

def var_0_0.GetMapBuilderInBuffer(arg_115_0, arg_115_1):
	if not arg_115_0.mbDict[arg_115_1]:
		local var_115_0 = _G[var_0_6[arg_115_1] or var_0_6.default]

		arg_115_0.mbDict[arg_115_1] = var_115_0.New(arg_115_0._tf, arg_115_0)
		arg_115_0.mbDict[arg_115_1].isFrozen = arg_115_0.isfrozen()

		arg_115_0.mbDict[arg_115_1].Load()

	return arg_115_0.mbDict[arg_115_1]

def var_0_0.JudgeMapBuilderType(arg_116_0):
	return (arg_116_0.contextData.map.getConfig("ui_type"))

def var_0_0.updateMap(arg_117_0):
	local var_117_0 = arg_117_0.contextData.map

	arg_117_0.SwitchMapBG(var_117_0, arg_117_0.lastMapIdx)

	arg_117_0.lastMapIdx = None

	local var_117_1 = var_117_0.getConfig("anchor")
	local var_117_2

	if var_117_1 == "":
		var_117_2 = Vector2.zero
	else
		var_117_2 = Vector2(unpack(var_117_1))

	arg_117_0.map.pivot = var_117_2

	local var_117_3 = var_117_0.getConfig("uifx")

	for iter_117_0 = 1, arg_117_0.UIFXList.childCount:
		local var_117_4 = arg_117_0.UIFXList.GetChild(iter_117_0 - 1)

		setActive(var_117_4, var_117_4.name == var_117_3)

	arg_117_0.PlayBGM()

	local var_117_5 = arg_117_0.JudgeMapBuilderType()

	arg_117_0.SwitchMapBuilder(var_117_5)
	arg_117_0.mapBuilder.buffer.Update(var_117_0)
	arg_117_0.UpdateSwitchMapButton()
	arg_117_0.updateMapItems()
	arg_117_0.mapBuilder.buffer.UpdateButtons()
	arg_117_0.mapBuilder.buffer.PostUpdateMap(var_117_0)

	if arg_117_0.contextData.openChapterId:
		arg_117_0.mapBuilder.buffer.TryOpenChapter(arg_117_0.contextData.openChapterId)

		arg_117_0.contextData.openChapterId = None

def var_0_0.UpdateSwitchMapButton(arg_118_0):
	local var_118_0 = arg_118_0.contextData.map
	local var_118_1 = getProxy(ChapterProxy)
	local var_118_2 = var_118_1.getMapById(var_118_0.id - 1)
	local var_118_3 = var_118_1.getMapById(var_118_0.id + 1)

	setActive(arg_118_0.btnPrev, tobool(var_118_2))
	setActive(arg_118_0.btnNext, tobool(var_118_3))

	local var_118_4 = Color.New(0.5, 0.5, 0.5, 1)

	setImageColor(arg_118_0.btnPrevCol, var_118_2 and Color.white or var_118_4)
	setImageColor(arg_118_0.btnNextCol, var_118_3 and var_118_3.isUnlock() and Color.white or var_118_4)

def var_0_0.TrySwitchChapter(arg_119_0, arg_119_1):
	local var_119_0 = getProxy(ChapterProxy).getActiveChapter()

	if var_119_0:
		if var_119_0.id == arg_119_1.id:
			arg_119_0.switchToChapter(var_119_0)
		else
			local var_119_1 = i18n("levelScene_chapter_strategying", var_119_0.getConfig("chapter_name"))

			pg.TipsMgr.GetInstance().ShowTips(var_119_1)
	else
		arg_119_0.displayChapterPanel(arg_119_1)

def var_0_0.updateChapterTF(arg_120_0, arg_120_1):
	if not arg_120_0.mapBuilder.UpdateChapterTF:
		return

	arg_120_0.mapBuilder.buffer.UpdateChapterTF(arg_120_1)

def var_0_0.tryPlayMapStory(arg_121_0):
	if IsUnityEditor and not ENABLE_GUIDE:
		return

	seriesAsync({
		function(arg_122_0)
			local var_122_0 = arg_121_0.contextData.map.getConfig("enter_story")

			if var_122_0 and var_122_0 != "" and not pg.NewStoryMgr.GetInstance().IsPlayed(var_122_0) and not arg_121_0.contextData.map.isRemaster() and not pg.SystemOpenMgr.GetInstance().active:
				local var_122_1 = tonumber(var_122_0)

				if var_122_1 and var_122_1 > 0:
					arg_121_0.emit(LevelMediator2.ON_PERFORM_COMBAT, var_122_1)
				else
					pg.NewStoryMgr.GetInstance().Play(var_122_0, arg_122_0)

				return

			arg_122_0(),
		function(arg_123_0)
			local var_123_0 = arg_121_0.contextData.map.getConfig("guide_id")

			if var_123_0 and var_123_0 != "":
				pg.SystemGuideMgr.GetInstance().PlayByGuideId(var_123_0, None, arg_123_0)

				return

			arg_123_0(),
		function(arg_124_0)
			if isActive(arg_121_0.actAtelierBuffBtn) and getProxy(ActivityProxy).AtelierActivityAllSlotIsEmpty() and getProxy(ActivityProxy).OwnAtelierActivityItemCnt(34, 1):
				local var_124_0 = PlayerPrefs.GetInt("first_enter_ryza_buff_" .. getProxy(PlayerProxy).getRawData().id, 0) == 0
				local var_124_1

				if var_124_0:
					var_124_1 = {
						1,
						2
					}
				else
					var_124_1 = {
						1
					}

				pg.SystemGuideMgr.GetInstance().PlayByGuideId("NG0034", var_124_1)
			else
				arg_124_0(),
		function(arg_125_0)
			if arg_121_0.exited:
				return

			pg.SystemOpenMgr.GetInstance().notification(arg_121_0.player.level)

			if pg.SystemOpenMgr.GetInstance().active:
				getProxy(ChapterProxy).StopAutoFight()
	})

def var_0_0.DisplaySPAnim(arg_126_0, arg_126_1, arg_126_2, arg_126_3):
	arg_126_0.uiAnims = arg_126_0.uiAnims or {}

	local var_126_0 = arg_126_0.uiAnims[arg_126_1]

	local function var_126_1()
		arg_126_0.playing = True

		arg_126_0.frozen()
		var_126_0.SetActive(True)

		local var_127_0 = tf(var_126_0)

		pg.UIMgr.GetInstance().OverlayPanel(var_127_0, {
			groupName = LayerWeightConst.GROUP_LEVELUI
		})

		if arg_126_3:
			arg_126_3(var_126_0)

		var_127_0.GetComponent("DftAniEvent").SetEndEvent(function(arg_128_0)
			arg_126_0.playing = False

			if arg_126_2:
				arg_126_2(var_126_0)

			arg_126_0.unfrozen())
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WARNING)

	if not var_126_0:
		PoolMgr.GetInstance().GetUI(arg_126_1, True, function(arg_129_0)
			arg_129_0.SetActive(True)

			arg_126_0.uiAnims[arg_126_1] = arg_129_0
			var_126_0 = arg_126_0.uiAnims[arg_126_1]

			var_126_1())
	else
		var_126_1()

def var_0_0.displaySpResult(arg_130_0, arg_130_1, arg_130_2):
	setActive(arg_130_0.spResult, True)
	arg_130_0.DisplaySPAnim(arg_130_1 == 1 and "SpUnitWin" or "SpUnitLose", function(arg_131_0)
		onButton(arg_130_0, arg_131_0, function()
			removeOnButton(arg_131_0)
			setActive(arg_131_0, False)
			pg.UIMgr.GetInstance().UnOverlayPanel(arg_131_0, arg_130_0._tf)
			arg_130_0.hideSpResult()
			arg_130_2(), SFX_PANEL))

def var_0_0.hideSpResult(arg_133_0):
	setActive(arg_133_0.spResult, False)

def var_0_0.displayBombResult(arg_134_0, arg_134_1):
	setActive(arg_134_0.spResult, True)
	arg_134_0.DisplaySPAnim("SpBombRet", function(arg_135_0)
		onButton(arg_134_0, arg_135_0, function()
			removeOnButton(arg_135_0)
			setActive(arg_135_0, False)
			pg.UIMgr.GetInstance().UnOverlayPanel(arg_135_0, arg_134_0._tf)
			arg_134_0.hideSpResult()
			arg_134_1(), SFX_PANEL), function(arg_137_0)
		setText(arg_137_0.transform.Find("right/name_bg/en"), arg_134_0.contextData.chapterVO.modelCount))

def var_0_0.displayChapterPanel(arg_138_0, arg_138_1, arg_138_2):
	local function var_138_0(arg_139_0)
		if getProxy(BayProxy).getShipCount() >= arg_138_0.player.getMaxShipBag():
			NoPosMsgBox(i18n("switch_to_shop_tip_noDockyard"), openDockyardClear, gotoChargeScene, openDockyardIntensify)

			return

		arg_138_0.hideChapterPanel()

		local var_139_0 = arg_138_1.getConfig("type")

		arg_138_0.contextData.chapterLoopFlag = arg_139_0

		if var_139_0 == Chapter.CustomFleet:
			arg_138_0.displayFleetEdit(arg_138_1)
		elif #arg_138_1.getNpcShipByType(1) > 0:
			arg_138_0.emit(LevelMediator2.ON_TRACKING, arg_138_1.id)

			return
		else
			arg_138_0.displayFleetSelect(arg_138_1)

	local function var_138_1()
		arg_138_0.hideChapterPanel()

	if getProxy(ChapterProxy).getMapById(arg_138_1.getConfig("map")).isSkirmish() and #arg_138_1.getNpcShipByType(1) > 0:
		var_138_0(False)

		return

	arg_138_0.levelInfoView.Load()
	arg_138_0.levelInfoView.ActionInvoke("set", arg_138_1, arg_138_2)
	arg_138_0.levelInfoView.ActionInvoke("setCBFunc", var_138_0, var_138_1)
	arg_138_0.levelInfoView.ActionInvoke("Show")

def var_0_0.hideChapterPanel(arg_141_0):
	if arg_141_0.levelInfoView.isShowing():
		arg_141_0.levelInfoView.ActionInvoke("Hide")

def var_0_0.destroyChapterPanel(arg_142_0):
	arg_142_0.levelInfoView.Destroy()

	arg_142_0.levelInfoView = None

def var_0_0.displayFleetSelect(arg_143_0, arg_143_1):
	local var_143_0 = arg_143_0.contextData.selectedFleetIDs or arg_143_1.GetDefaultFleetIndex()

	arg_143_1 = Clone(arg_143_1)
	arg_143_1.loopFlag = arg_143_0.contextData.chapterLoopFlag

	arg_143_0.levelFleetView.updateSpecialOperationTickets(arg_143_0.spTickets)
	arg_143_0.levelFleetView.Load()
	arg_143_0.levelFleetView.ActionInvoke("setHardShipVOs", arg_143_0.shipVOs)
	arg_143_0.levelFleetView.ActionInvoke("setOpenCommanderTag", arg_143_0.openedCommanerSystem)
	arg_143_0.levelFleetView.ActionInvoke("set", arg_143_1, arg_143_0.fleets, var_143_0)
	arg_143_0.levelFleetView.ActionInvoke("Show")

def var_0_0.hideFleetSelect(arg_144_0):
	if arg_144_0.levelCMDFormationView.isShowing():
		arg_144_0.levelCMDFormationView.Hide()

	if arg_144_0.levelFleetView:
		arg_144_0.levelFleetView.Hide()

def var_0_0.buildCommanderPanel(arg_145_0):
	arg_145_0.levelCMDFormationView = LevelCMDFormationView.New(arg_145_0.topPanel, arg_145_0.event, arg_145_0.contextData)

def var_0_0.destroyFleetSelect(arg_146_0):
	if not arg_146_0.levelFleetView:
		return

	arg_146_0.levelFleetView.Destroy()

	arg_146_0.levelFleetView = None

def var_0_0.displayFleetEdit(arg_147_0, arg_147_1):
	arg_147_1 = Clone(arg_147_1)
	arg_147_1.loopFlag = arg_147_0.contextData.chapterLoopFlag

	arg_147_0.levelFleetView.updateSpecialOperationTickets(arg_147_0.spTickets)
	arg_147_0.levelFleetView.Load()
	arg_147_0.levelFleetView.ActionInvoke("setOpenCommanderTag", arg_147_0.openedCommanerSystem)
	arg_147_0.levelFleetView.ActionInvoke("setHardShipVOs", arg_147_0.shipVOs)
	arg_147_0.levelFleetView.ActionInvoke("setOnHard", arg_147_1)
	arg_147_0.levelFleetView.ActionInvoke("Show")

def var_0_0.hideFleetEdit(arg_148_0):
	arg_148_0.hideFleetSelect()

def var_0_0.destroyFleetEdit(arg_149_0):
	arg_149_0.destroyFleetSelect()

def var_0_0.RefreshFleetSelectView(arg_150_0, arg_150_1):
	if not arg_150_0.levelFleetView:
		return

	assert(arg_150_0.levelFleetView.GetLoaded())

	local var_150_0 = arg_150_0.levelFleetView.IsSelectMode()
	local var_150_1

	if var_150_0:
		arg_150_0.levelFleetView.ActionInvoke("set", arg_150_1 or arg_150_0.levelFleetView.chapter, arg_150_0.fleets, arg_150_0.levelFleetView.getSelectIds())

		if arg_150_0.levelCMDFormationView.isShowing():
			local var_150_2 = arg_150_0.levelCMDFormationView.fleet.id

			var_150_1 = arg_150_0.fleets[var_150_2]
	else
		arg_150_0.levelFleetView.ActionInvoke("setOnHard", arg_150_1 or arg_150_0.levelFleetView.chapter)

		if arg_150_0.levelCMDFormationView.isShowing():
			local var_150_3 = arg_150_0.levelCMDFormationView.fleet.id

			var_150_1 = arg_150_1.wrapEliteFleet(var_150_3)

	if var_150_1:
		arg_150_0.levelCMDFormationView.ActionInvoke("updateFleet", var_150_1)

def var_0_0.setChapter(arg_151_0, arg_151_1):
	local var_151_0

	if arg_151_1:
		var_151_0 = arg_151_1.id

	arg_151_0.contextData.chapterId = var_151_0
	arg_151_0.contextData.chapterVO = arg_151_1

def var_0_0.switchToChapter(arg_152_0, arg_152_1):
	if arg_152_0.contextData.mapIdx != arg_152_1.getConfig("map"):
		arg_152_0.setMap(arg_152_1.getConfig("map"))

	arg_152_0.setChapter(arg_152_1)
	setActive(arg_152_0.clouds, False)
	arg_152_0.mapBuilder.buffer.Hide()

	arg_152_0.leftCanvasGroup.blocksRaycasts = False
	arg_152_0.rightCanvasGroup.blocksRaycasts = False

	assert(not arg_152_0.levelStageView, "LevelStageView Exists On SwitchToChapter")
	arg_152_0.DestroyLevelStageView()

	if not arg_152_0.levelStageView:
		arg_152_0.levelStageView = LevelStageView.New(arg_152_0.topPanel, arg_152_0.event, arg_152_0.contextData)

		arg_152_0.levelStageView.Load()

		arg_152_0.levelStageView.isFrozen = arg_152_0.isfrozen()

	arg_152_0.frozen()

	local function var_152_0()
		seriesAsync({
			function(arg_154_0)
				pg.UIMgr.GetInstance().BlurPanel(arg_152_0.topPanel, False, {
					blurCamList = {
						pg.UIMgr.CameraUI
					},
					groupName = LayerWeightConst.GROUP_LEVELUI
				})
				pg.playerResUI.SetActive({
					active = True,
					groupName = LayerWeightConst.GROUP_LEVELUI,
					showType = PlayerResUI.TYPE_ALL
				})
				arg_152_0.levelStageView.updateStageInfo()
				arg_152_0.levelStageView.updateAmbushRate(arg_152_1.fleet.line, True)
				arg_152_0.levelStageView.updateStageAchieve()
				arg_152_0.levelStageView.updateStageBarrier()
				arg_152_0.levelStageView.updateBombPanel()
				arg_152_0.levelStageView.UpdateDefenseStatus()
				onNextTick(arg_154_0),
			function(arg_155_0)
				if arg_152_0.exited:
					return

				arg_152_0.levelStageView.updateStageStrategy()

				arg_152_0.canvasGroup.blocksRaycasts = arg_152_0.frozenCount == 0

				onNextTick(arg_155_0),
			function(arg_156_0)
				if arg_152_0.exited:
					return

				arg_152_0.levelStageView.updateStageFleet()
				arg_152_0.levelStageView.updateSupportFleet()
				arg_152_0.levelStageView.updateFleetBuff()
				onNextTick(arg_156_0),
			function(arg_157_0)
				if arg_152_0.exited:
					return

				parallelAsync({
					function(arg_158_0)
						local var_158_0 = arg_152_1.getConfig("scale")
						local var_158_1 = LeanTween.value(go(arg_152_0.map), arg_152_0.map.localScale, Vector3.New(var_158_0[3], var_158_0[3], 1), var_0_1).setOnUpdateVector3(function(arg_159_0)
							arg_152_0.map.localScale = arg_159_0
							arg_152_0.float.localScale = arg_159_0).setOnComplete(System.Action(arg_158_0)).setEase(LeanTweenType.easeOutSine)

						arg_152_0.RecordTween("mapScale", var_158_1.uniqueId)

						local var_158_2 = LeanTween.value(go(arg_152_0.map), arg_152_0.map.pivot, Vector2.New(math.clamp(var_158_0[1] - 0.5, 0, 1), math.clamp(var_158_0[2] - 0.5, 0, 1)), var_0_1)

						var_158_2.setOnUpdateVector2(function(arg_160_0)
							arg_152_0.map.pivot = arg_160_0
							arg_152_0.float.pivot = arg_160_0).setEase(LeanTweenType.easeOutSine)
						arg_152_0.RecordTween("mapPivot", var_158_2.uniqueId)
						shiftPanel(arg_152_0.leftChapter, -arg_152_0.leftChapter.rect.width - 200, 0, 0.3, 0, True, None, LeanTweenType.easeOutSine)
						shiftPanel(arg_152_0.rightChapter, arg_152_0.rightChapter.rect.width + 200, 0, 0.3, 0, True, None, LeanTweenType.easeOutSine)
						shiftPanel(arg_152_0.topChapter, 0, arg_152_0.topChapter.rect.height, 0.3, 0, True, None, LeanTweenType.easeOutSine)
						arg_152_0.levelStageView.ShiftStagePanelIn(),
					function(arg_161_0)
						arg_152_0.PlayBGM()

						local var_161_0 = {}
						local var_161_1 = arg_152_1.getConfig("bg")

						if var_161_1 and #var_161_1 > 0:
							var_161_0[1] = {
								BG = var_161_1
							}

						arg_152_0.SwitchBG(var_161_0, arg_161_0)
				}, function()
					onNextTick(arg_157_0)
					arg_152_0.mapBuilder.buffer.HideButtons()),
			function(arg_163_0)
				if arg_152_0.exited:
					return

				setActive(arg_152_0.topChapter, False)
				setActive(arg_152_0.leftChapter, False)
				setActive(arg_152_0.rightChapter, False)

				arg_152_0.leftCanvasGroup.blocksRaycasts = True
				arg_152_0.rightCanvasGroup.blocksRaycasts = True

				arg_152_0.initGrid(arg_163_0),
			function(arg_164_0)
				if arg_152_0.exited:
					return

				arg_152_0.levelStageView.SetGrid(arg_152_0.grid)

				arg_152_0.contextData.huntingRangeVisibility = arg_152_0.contextData.huntingRangeVisibility - 1

				arg_152_0.grid.toggleHuntingRange()

				local var_164_0 = arg_152_1.getConfig("pop_pic")

				if var_164_0 and #var_164_0 > 0 and arg_152_0.FirstEnterChapter == arg_152_1.id:
					arg_152_0.doPlayAnim(var_164_0, function(arg_165_0)
						setActive(arg_165_0, False)

						if arg_152_0.exited:
							return

						arg_164_0())
				else
					arg_164_0(),
			function(arg_166_0)
				arg_152_0.levelStageView.tryAutoAction(arg_166_0),
			function(arg_167_0)
				if arg_152_0.exited:
					return

				arg_152_0.unfrozen()

				if arg_152_0.FirstEnterChapter:
					arg_152_0.emit(LevelMediator2.ON_RESUME_SUBSTATE, arg_152_1.subAutoAttack)

				arg_152_0.FirstEnterChapter = None

				arg_152_0.levelStageView.tryAutoTrigger(True)
		})

	arg_152_0.levelStageView.ActionInvoke("SetSeriesOperation", var_152_0)
	arg_152_0.levelStageView.ActionInvoke("SetPlayer", arg_152_0.player)
	arg_152_0.levelStageView.ActionInvoke("SwitchToChapter", arg_152_1)

def var_0_0.switchToMap(arg_168_0, arg_168_1):
	arg_168_0.frozen()
	arg_168_0.destroyGrid()
	LeanTween.cancel(go(arg_168_0.map))

	local var_168_0 = LeanTween.value(go(arg_168_0.map), arg_168_0.map.localScale, Vector3.one, var_0_1).setOnUpdateVector3(function(arg_169_0)
		arg_168_0.map.localScale = arg_169_0
		arg_168_0.float.localScale = arg_169_0).setOnComplete(System.Action(function()
		arg_168_0.mapBuilder.buffer.Show()
		arg_168_0.mapBuilder.buffer.Update(arg_168_0.contextData.map)
		arg_168_0.UpdateSwitchMapButton()
		arg_168_0.updateMapItems()
		arg_168_0.mapBuilder.buffer.UpdateButtons()
		arg_168_0.mapBuilder.buffer.PostUpdateMap(arg_168_0.contextData.map)
		arg_168_0.unfrozen()
		existCall(arg_168_1))).setEase(LeanTweenType.easeOutSine)

	arg_168_0.RecordTween("mapScale", var_168_0.uniqueId)

	local var_168_1 = arg_168_0.contextData.map.getConfig("anchor")
	local var_168_2

	if var_168_1 == "":
		var_168_2 = Vector2.zero
	else
		var_168_2 = Vector2(unpack(var_168_1))

	local var_168_3 = LeanTween.value(go(arg_168_0.map), arg_168_0.map.pivot, var_168_2, var_0_1)

	var_168_3.setOnUpdateVector2(function(arg_171_0)
		arg_168_0.map.pivot = arg_171_0
		arg_168_0.float.pivot = arg_171_0).setEase(LeanTweenType.easeOutSine)
	arg_168_0.RecordTween("mapPivot", var_168_3.uniqueId)
	setActive(arg_168_0.topChapter, True)
	setActive(arg_168_0.leftChapter, True)
	setActive(arg_168_0.rightChapter, True)
	shiftPanel(arg_168_0.leftChapter, 0, 0, 0.3, 0, True, None, LeanTweenType.easeOutSine)
	shiftPanel(arg_168_0.rightChapter, 0, 0, 0.3, 0, True, None, LeanTweenType.easeOutSine)
	shiftPanel(arg_168_0.topChapter, 0, 0, 0.3, 0, True, None, LeanTweenType.easeOutSine)
	assert(arg_168_0.levelStageView, "LevelStageView Doesnt Exist On SwitchToMap")

	if arg_168_0.levelStageView:
		arg_168_0.levelStageView.ActionInvoke("ShiftStagePanelOut", function()
			arg_168_0.DestroyLevelStageView())
		arg_168_0.levelStageView.ActionInvoke("SwitchToMap")

	arg_168_0.SwitchMapBG(arg_168_0.contextData.map)
	arg_168_0.mapBuilder.buffer.ShowButtons()
	arg_168_0.setChapter(None)
	arg_168_0.PlayBGM()
	pg.UIMgr.GetInstance().UnblurPanel(arg_168_0.topPanel, arg_168_0._tf)
	pg.playerResUI.SetActive({
		active = False
	})

	arg_168_0.canvasGroup.blocksRaycasts = arg_168_0.frozenCount == 0
	arg_168_0.canvasGroup.interactable = True

	if arg_168_0.ambushWarning and arg_168_0.ambushWarning.activeSelf:
		arg_168_0.ambushWarning.SetActive(False)
		arg_168_0.unfrozen()

def var_0_0.SwitchBG(arg_173_0, arg_173_1, arg_173_2, arg_173_3):
	if not arg_173_1 or #arg_173_1 <= 0:
		existCall(arg_173_2)

		return
	elif arg_173_3:
		-- block empty
	elif table.equal(arg_173_0.currentBG, arg_173_1):
		return

	arg_173_0.currentBG = arg_173_1

	for iter_173_0, iter_173_1 in ipairs(arg_173_0.mapGroup):
		arg_173_0.loader.ClearRequest(iter_173_1)

	table.clear(arg_173_0.mapGroup)

	local var_173_0 = {}

	table.ParallelIpairsAsync(arg_173_1, function(arg_174_0, arg_174_1, arg_174_2)
		local var_174_0 = arg_173_0.mapTFs[arg_174_0]
		local var_174_1 = arg_173_0.loader.GetSpriteDirect("levelmap/" .. arg_174_1.BG, "", function(arg_175_0)
			var_173_0[arg_174_0] = arg_175_0

			arg_174_2(), var_174_0)

		table.insert(arg_173_0.mapGroup, var_174_1)
		arg_173_0.updateCouldAnimator(arg_174_1.Animator, arg_174_0), function()
		for iter_176_0, iter_176_1 in ipairs(arg_173_0.mapTFs):
			setImageSprite(iter_176_1, var_173_0[iter_176_0])
			setActive(iter_176_1, arg_173_1[iter_176_0])
			SetCompomentEnabled(iter_176_1, typeof(Image), True)

		existCall(arg_173_2))

local var_0_7 = {
	1520001,
	1520002,
	1520011,
	1520012
}
local var_0_8 = {
	{
		1420008,
		"map_1420008",
		1420021,
		"map_1420001"
	},
	{
		1420018,
		"map_1420018",
		1420031,
		"map_1420011"
	}
}
local var_0_9 = {
	1420001,
	1420011
}

def var_0_0.ClearMapTransitions(arg_177_0):
	if not arg_177_0.mapTransitions:
		return

	for iter_177_0, iter_177_1 in pairs(arg_177_0.mapTransitions):
		if iter_177_1:
			PoolMgr.GetInstance().ReturnPrefab("ui/" .. iter_177_0, iter_177_0, iter_177_1, True)
		else
			PoolMgr.GetInstance().DestroyPrefab("ui/" .. iter_177_0, iter_177_0)

	arg_177_0.mapTransitions = None

def var_0_0.SwitchMapBG(arg_178_0, arg_178_1, arg_178_2, arg_178_3):
	local var_178_0, var_178_1, var_178_2 = arg_178_0.GetMapBG(arg_178_1, arg_178_2)

	if not var_178_1:
		arg_178_0.SwitchBG(var_178_0, arg_178_3)

		return

	arg_178_0.PlayMapTransition("LevelMapTransition_" .. var_178_1, var_178_2, function()
		arg_178_0.SwitchBG(var_178_0, arg_178_3))

def var_0_0.GetMapBG(arg_180_0, arg_180_1, arg_180_2):
	if not table.contains(var_0_7, arg_180_1.id):
		return {
			arg_180_0.GetMapElement(arg_180_1)
		}

	local var_180_0 = arg_180_1.id
	local var_180_1 = table.indexof(var_0_7, var_180_0) - 1
	local var_180_2 = bit.lshift(bit.rshift(var_180_1, 1), 1) + 1
	local var_180_3 = {
		var_0_7[var_180_2],
		var_0_7[var_180_2 + 1]
	}
	local var_180_4 = _.map(var_180_3, function(arg_181_0)
		return getProxy(ChapterProxy).getMapById(arg_181_0))

	if _.all(var_180_4, function(arg_182_0)
		return arg_182_0.isAllChaptersClear()):
		local var_180_5 = {
			arg_180_0.GetMapElement(arg_180_1)
		}

		if not arg_180_2 or math.abs(var_180_0 - arg_180_2) != 1:
			return var_180_5

		local var_180_6 = var_0_9[bit.rshift(var_180_2 - 1, 1) + 1]
		local var_180_7 = bit.band(var_180_1, 1) == 1

		return var_180_5, var_180_6, var_180_7
	else
		local var_180_8 = 0

		;(function()
			local var_183_0 = var_180_4[1].getChapters()

			for iter_183_0, iter_183_1 in ipairs(var_183_0):
				if not iter_183_1.isClear():
					return

				var_180_8 = var_180_8 + 1

			if not var_180_4[2].isAnyChapterUnlocked(True):
				return

			var_180_8 = var_180_8 + 1

			local var_183_1 = var_180_4[2].getChapters()

			for iter_183_2, iter_183_3 in ipairs(var_183_1):
				if not iter_183_3.isClear():
					return

				var_180_8 = var_180_8 + 1)()

		local var_180_9

		if var_180_8 > 0:
			local var_180_10 = var_0_8[bit.rshift(var_180_2 - 1, 1) + 1]

			var_180_9 = {
				{
					BG = "map_" .. var_180_10[1],
					Animator = var_180_10[2]
				},
				{
					BG = "map_" .. var_180_10[3] + var_180_8,
					Animator = var_180_10[4]
				}
			}
		else
			var_180_9 = {
				arg_180_0.GetMapElement(arg_180_1)
			}

		return var_180_9

def var_0_0.GetMapElement(arg_184_0, arg_184_1):
	local var_184_0 = arg_184_1.getConfig("bg")
	local var_184_1 = arg_184_1.getConfig("ani_controller")

	if var_184_1 and #var_184_1 > 0:
		(function()
			for iter_185_0, iter_185_1 in ipairs(var_184_1):
				local var_185_0 = _.rest(iter_185_1[2], 2)

				for iter_185_2, iter_185_3 in ipairs(var_185_0):
					if string.find(iter_185_3, "^map_") and iter_185_1[1] == var_0_3:
						local var_185_1 = iter_185_1[2][1]
						local var_185_2 = getProxy(ChapterProxy).GetChapterItemById(var_185_1)

						if var_185_2 and not var_185_2.isClear():
							var_184_0 = iter_185_3

							return)()

	local var_184_2 = {
		BG = var_184_0
	}

	var_184_2.Animator, var_184_2.AnimatorController = arg_184_0.GetMapAnimator(arg_184_1)

	return var_184_2

def var_0_0.GetMapAnimator(arg_186_0, arg_186_1):
	local var_186_0 = arg_186_1.getConfig("ani_name")

	if arg_186_1.getConfig("animtor") == 1 and var_186_0 and #var_186_0 > 0:
		local var_186_1 = arg_186_1.getConfig("ani_controller")

		if var_186_1 and #var_186_1 > 0:
			(function()
				for iter_187_0, iter_187_1 in ipairs(var_186_1):
					local var_187_0 = _.rest(iter_187_1[2], 2)

					for iter_187_2, iter_187_3 in ipairs(var_187_0):
						if string.find(iter_187_3, "^effect_") and iter_187_1[1] == var_0_3:
							local var_187_1 = iter_187_1[2][1]
							local var_187_2 = getProxy(ChapterProxy).GetChapterItemById(var_187_1)

							if var_187_2 and not var_187_2.isClear():
								var_186_0 = "map_" .. string.sub(iter_187_3, 8)

								return)()

		return var_186_0, var_186_1

def var_0_0.PlayMapTransition(arg_188_0, arg_188_1, arg_188_2, arg_188_3, arg_188_4):
	arg_188_0.mapTransitions = arg_188_0.mapTransitions or {}

	local var_188_0

	local function var_188_1()
		arg_188_0.frozen()
		existCall(arg_188_3, var_188_0)
		var_188_0.SetActive(True)

		local var_189_0 = tf(var_188_0)

		pg.UIMgr.GetInstance().OverlayPanel(var_189_0, {
			groupName = LayerWeightConst.GROUP_LEVELUI
		})
		var_188_0.GetComponent(typeof(Animator)).Play(arg_188_2 and "Sequence" or "Inverted", -1, 0)
		var_189_0.GetComponent("DftAniEvent").SetEndEvent(function(arg_190_0)
			pg.UIMgr.GetInstance().UnOverlayPanel(var_189_0, arg_188_0._tf)
			existCall(arg_188_4, var_188_0)
			PoolMgr.GetInstance().ReturnPrefab("ui/" .. arg_188_1, arg_188_1, var_188_0)

			arg_188_0.mapTransitions[arg_188_1] = False

			arg_188_0.unfrozen())

	PoolMgr.GetInstance().GetPrefab("ui/" .. arg_188_1, arg_188_1, True, function(arg_191_0)
		var_188_0 = arg_191_0
		arg_188_0.mapTransitions[arg_188_1] = arg_191_0

		var_188_1())

def var_0_0.DestroyLevelStageView(arg_192_0):
	if arg_192_0.levelStageView:
		arg_192_0.levelStageView.Destroy()

		arg_192_0.levelStageView = None

def var_0_0.displayAmbushInfo(arg_193_0, arg_193_1):
	arg_193_0.levelAmbushView = LevelAmbushView.New(arg_193_0.topPanel, arg_193_0.event, arg_193_0.contextData)

	arg_193_0.levelAmbushView.Load()
	arg_193_0.levelAmbushView.ActionInvoke("SetFuncOnComplete", arg_193_1)

def var_0_0.hideAmbushInfo(arg_194_0):
	if arg_194_0.levelAmbushView:
		arg_194_0.levelAmbushView.Destroy()

		arg_194_0.levelAmbushView = None

def var_0_0.doAmbushWarning(arg_195_0, arg_195_1):
	arg_195_0.frozen()

	local function var_195_0()
		arg_195_0.ambushWarning.SetActive(True)

		local var_196_0 = tf(arg_195_0.ambushWarning)

		var_196_0.SetParent(pg.UIMgr.GetInstance().OverlayMain.transform, False)
		var_196_0.SetSiblingIndex(1)

		local var_196_1 = var_196_0.GetComponent("DftAniEvent")

		var_196_1.SetTriggerEvent(function(arg_197_0)
			arg_195_1())
		var_196_1.SetEndEvent(function(arg_198_0)
			arg_195_0.ambushWarning.SetActive(False)
			arg_195_0.unfrozen())
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WARNING)
		Timer.New(function()
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WARNING), 1, 1).Start()

	if not arg_195_0.ambushWarning:
		PoolMgr.GetInstance().GetUI("ambushwarnui", True, function(arg_200_0)
			arg_200_0.SetActive(True)

			arg_195_0.ambushWarning = arg_200_0

			var_195_0())
	else
		var_195_0()

def var_0_0.destroyAmbushWarn(arg_201_0):
	if arg_201_0.ambushWarning:
		PoolMgr.GetInstance().ReturnUI("ambushwarnui", arg_201_0.ambushWarning)

		arg_201_0.ambushWarning = None

def var_0_0.displayStrategyInfo(arg_202_0, arg_202_1):
	arg_202_0.levelStrategyView = LevelStrategyView.New(arg_202_0.topPanel, arg_202_0.event, arg_202_0.contextData)

	arg_202_0.levelStrategyView.Load()
	arg_202_0.levelStrategyView.ActionInvoke("set", arg_202_1)

	local function var_202_0()
		local var_203_0 = arg_202_0.contextData.chapterVO.fleet
		local var_203_1 = pg.strategy_data_template[arg_202_1.id]

		if not var_203_0.canUseStrategy(arg_202_1):
			return

		local var_203_2 = var_203_0.getNextStgUser(arg_202_1.id)

		if var_203_1.type == ChapterConst.StgTypeForm:
			arg_202_0.emit(LevelMediator2.ON_OP, {
				type = ChapterConst.OpStrategy,
				id = var_203_2,
				arg1 = arg_202_1.id
			})
		elif var_203_1.type == ChapterConst.StgTypeConsume:
			arg_202_0.emit(LevelMediator2.ON_OP, {
				type = ChapterConst.OpStrategy,
				id = var_203_2,
				arg1 = arg_202_1.id
			})

		arg_202_0.hideStrategyInfo()

	local function var_202_1()
		arg_202_0.hideStrategyInfo()

	arg_202_0.levelStrategyView.ActionInvoke("setCBFunc", var_202_0, var_202_1)

def var_0_0.hideStrategyInfo(arg_205_0):
	if arg_205_0.levelStrategyView:
		arg_205_0.levelStrategyView.Destroy()

		arg_205_0.levelStrategyView = None

def var_0_0.displayRepairWindow(arg_206_0, arg_206_1):
	local var_206_0 = arg_206_0.contextData.chapterVO
	local var_206_1 = getProxy(ChapterProxy)
	local var_206_2
	local var_206_3
	local var_206_4
	local var_206_5
	local var_206_6 = var_206_1.repairTimes
	local var_206_7, var_206_8, var_206_9 = ChapterConst.GetRepairParams()

	arg_206_0.levelRepairView = LevelRepairView.New(arg_206_0.topPanel, arg_206_0.event, arg_206_0.contextData)

	arg_206_0.levelRepairView.Load()
	arg_206_0.levelRepairView.ActionInvoke("set", var_206_6, var_206_7, var_206_8, var_206_9)

	local function var_206_10()
		if var_206_7 - math.min(var_206_6, var_206_7) == 0 and arg_206_0.player.getTotalGem() < var_206_9:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_rmb"))

			return

		arg_206_0.emit(LevelMediator2.ON_OP, {
			type = ChapterConst.OpRepair,
			id = var_206_0.fleet.id,
			arg1 = arg_206_1.id
		})
		arg_206_0.hideRepairWindow()

	local function var_206_11()
		arg_206_0.hideRepairWindow()

	arg_206_0.levelRepairView.ActionInvoke("setCBFunc", var_206_10, var_206_11)

def var_0_0.hideRepairWindow(arg_209_0):
	if arg_209_0.levelRepairView:
		arg_209_0.levelRepairView.Destroy()

		arg_209_0.levelRepairView = None

def var_0_0.displayRemasterPanel(arg_210_0, arg_210_1):
	arg_210_0.levelRemasterView.Load()

	local function var_210_0(arg_211_0)
		arg_210_0.ShowSelectedMap(arg_211_0)

	arg_210_0.levelRemasterView.ActionInvoke("Show")
	arg_210_0.levelRemasterView.ActionInvoke("set", var_210_0, arg_210_1)

def var_0_0.hideRemasterPanel(arg_212_0):
	if arg_212_0.levelRemasterView.isShowing():
		arg_212_0.levelRemasterView.ActionInvoke("Hide")

def var_0_0.initGrid(arg_213_0, arg_213_1):
	local var_213_0 = arg_213_0.contextData.chapterVO

	if not var_213_0:
		return

	arg_213_0.enableLevelCamera()
	setActive(arg_213_0.uiMain, True)

	arg_213_0.levelGrid.localEulerAngles = Vector3(var_213_0.theme.angle, 0, 0)
	arg_213_0.grid = LevelGrid.New(arg_213_0.dragLayer)

	arg_213_0.grid.attach(arg_213_0)
	arg_213_0.grid.ExtendItem("shipTpl", arg_213_0.shipTpl)
	arg_213_0.grid.ExtendItem("subTpl", arg_213_0.subTpl)
	arg_213_0.grid.ExtendItem("transportTpl", arg_213_0.transportTpl)
	arg_213_0.grid.ExtendItem("enemyTpl", arg_213_0.enemyTpl)
	arg_213_0.grid.ExtendItem("championTpl", arg_213_0.championTpl)
	arg_213_0.grid.ExtendItem("oniTpl", arg_213_0.oniTpl)
	arg_213_0.grid.ExtendItem("arrowTpl", arg_213_0.arrowTarget)
	arg_213_0.grid.ExtendItem("destinationMarkTpl", arg_213_0.destinationMarkTpl)

	function arg_213_0.grid.onShipStepChange(arg_214_0)
		arg_213_0.levelStageView.updateAmbushRate(arg_214_0)

	arg_213_0.grid.initAll(arg_213_1)

def var_0_0.destroyGrid(arg_215_0):
	if arg_215_0.grid:
		arg_215_0.grid.detach()

		arg_215_0.grid = None

		arg_215_0.disableLevelCamera()
		setActive(arg_215_0.dragLayer, True)
		setActive(arg_215_0.uiMain, False)

def var_0_0.doTracking(arg_216_0, arg_216_1):
	arg_216_0.frozen()

	local function var_216_0()
		arg_216_0.radar.SetActive(True)

		local var_217_0 = tf(arg_216_0.radar)

		var_217_0.SetParent(arg_216_0.topPanel, False)
		var_217_0.SetSiblingIndex(1)
		var_217_0.GetComponent("DftAniEvent").SetEndEvent(function(arg_218_0)
			arg_216_0.radar.SetActive(False)
			arg_216_0.unfrozen()
			arg_216_1())
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_SEARCH)

	if not arg_216_0.radar:
		PoolMgr.GetInstance().GetUI("RadarEffectUI", True, function(arg_219_0)
			arg_219_0.SetActive(True)

			arg_216_0.radar = arg_219_0

			var_216_0())
	else
		var_216_0()

def var_0_0.destroyTracking(arg_220_0):
	if arg_220_0.radar:
		PoolMgr.GetInstance().ReturnUI("RadarEffectUI", arg_220_0.radar)

		arg_220_0.radar = None

def var_0_0.doPlayAirStrike(arg_221_0, arg_221_1, arg_221_2, arg_221_3):
	local function var_221_0()
		arg_221_0.playing = True

		arg_221_0.frozen()
		arg_221_0.airStrike.SetActive(True)

		local var_222_0 = tf(arg_221_0.airStrike)

		var_222_0.SetParent(pg.UIMgr.GetInstance().OverlayMain.transform, False)
		var_222_0.SetAsLastSibling()
		setActive(var_222_0.Find("words/be_striked"), arg_221_1 == ChapterConst.SubjectChampion)
		setActive(var_222_0.Find("words/strike_enemy"), arg_221_1 == ChapterConst.SubjectPlayer)

		local function var_222_1()
			arg_221_0.playing = False

			SetActive(arg_221_0.airStrike, False)

			if arg_221_3:
				arg_221_3()

			arg_221_0.unfrozen()

		var_222_0.GetComponent("DftAniEvent").SetEndEvent(var_222_1)

		if arg_221_2:
			onButton(arg_221_0, var_222_0, var_222_1, SFX_PANEL)
		else
			removeOnButton(var_222_0)

		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WARNING)

	if not arg_221_0.airStrike:
		PoolMgr.GetInstance().GetUI("AirStrike", True, function(arg_224_0)
			arg_224_0.SetActive(True)

			arg_221_0.airStrike = arg_224_0

			var_221_0())
	else
		var_221_0()

def var_0_0.destroyAirStrike(arg_225_0):
	if arg_225_0.airStrike:
		arg_225_0.airStrike.GetComponent("DftAniEvent").SetEndEvent(None)
		PoolMgr.GetInstance().ReturnUI("AirStrike", arg_225_0.airStrike)

		arg_225_0.airStrike = None

def var_0_0.doPlayAnim(arg_226_0, arg_226_1, arg_226_2, arg_226_3):
	arg_226_0.uiAnims = arg_226_0.uiAnims or {}

	local var_226_0 = arg_226_0.uiAnims[arg_226_1]

	local function var_226_1()
		arg_226_0.playing = True

		arg_226_0.frozen()
		var_226_0.SetActive(True)

		local var_227_0 = tf(var_226_0)

		pg.UIMgr.GetInstance().OverlayPanel(var_227_0, {
			groupName = LayerWeightConst.GROUP_LEVELUI
		})

		if arg_226_3:
			arg_226_3(var_226_0)

		var_227_0.GetComponent("DftAniEvent").SetEndEvent(function(arg_228_0)
			arg_226_0.playing = False

			pg.UIMgr.GetInstance().UnOverlayPanel(var_227_0, arg_226_0._tf)

			if arg_226_2:
				arg_226_2(var_226_0)

			arg_226_0.unfrozen())
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WARNING)

	if not var_226_0:
		PoolMgr.GetInstance().GetUI(arg_226_1, True, function(arg_229_0)
			arg_229_0.SetActive(True)

			arg_226_0.uiAnims[arg_226_1] = arg_229_0
			var_226_0 = arg_226_0.uiAnims[arg_226_1]

			var_226_1())
	else
		var_226_1()

def var_0_0.destroyUIAnims(arg_230_0):
	if arg_230_0.uiAnims:
		for iter_230_0, iter_230_1 in pairs(arg_230_0.uiAnims):
			pg.UIMgr.GetInstance().UnOverlayPanel(tf(iter_230_1), arg_230_0._tf)
			iter_230_1.GetComponent("DftAniEvent").SetEndEvent(None)
			PoolMgr.GetInstance().ReturnUI(iter_230_0, iter_230_1)

		arg_230_0.uiAnims = None

def var_0_0.doPlayTorpedo(arg_231_0, arg_231_1):
	local function var_231_0()
		arg_231_0.playing = True

		arg_231_0.frozen()
		arg_231_0.torpetoAni.SetActive(True)

		local var_232_0 = tf(arg_231_0.torpetoAni)

		var_232_0.SetParent(arg_231_0.topPanel, False)
		var_232_0.SetAsLastSibling()
		var_232_0.GetComponent("DftAniEvent").SetEndEvent(function(arg_233_0)
			arg_231_0.playing = False

			SetActive(arg_231_0.torpetoAni, False)

			if arg_231_1:
				arg_231_1()

			arg_231_0.unfrozen())
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WARNING)

	if not arg_231_0.torpetoAni:
		PoolMgr.GetInstance().GetUI("Torpeto", True, function(arg_234_0)
			arg_234_0.SetActive(True)

			arg_231_0.torpetoAni = arg_234_0

			var_231_0())
	else
		var_231_0()

def var_0_0.destroyTorpedo(arg_235_0):
	if arg_235_0.torpetoAni:
		arg_235_0.torpetoAni.GetComponent("DftAniEvent").SetEndEvent(None)
		PoolMgr.GetInstance().ReturnUI("Torpeto", arg_235_0.torpetoAni)

		arg_235_0.torpetoAni = None

def var_0_0.doPlayStrikeAnim(arg_236_0, arg_236_1, arg_236_2, arg_236_3):
	arg_236_0.strikeAnims = arg_236_0.strikeAnims or {}

	local var_236_0
	local var_236_1
	local var_236_2

	local function var_236_3()
		if coroutine.status(var_236_2) == "suspended":
			local var_237_0, var_237_1 = coroutine.resume(var_236_2)

			assert(var_237_0, debug.traceback(var_236_2, var_237_1))

	var_236_2 = coroutine.create(function()
		arg_236_0.playing = True

		arg_236_0.frozen()

		local var_238_0 = arg_236_0.strikeAnims[arg_236_2]

		setActive(var_238_0, True)

		local var_238_1 = tf(var_238_0)
		local var_238_2 = findTF(var_238_1, "torpedo")
		local var_238_3 = findTF(var_238_1, "mask/painting")
		local var_238_4 = findTF(var_238_1, "ship")

		setParent(var_236_0, var_238_3.Find("fitter"), False)
		setParent(var_236_1, var_238_4, False)
		setActive(var_238_4, False)
		setActive(var_238_2, False)
		var_238_1.SetParent(pg.UIMgr.GetInstance().OverlayMain.transform, False)
		var_238_1.SetAsLastSibling()

		local var_238_5 = var_238_1.GetComponent("DftAniEvent")
		local var_238_6 = var_236_1.GetComponent("SpineAnimUI")
		local var_238_7 = var_238_6.GetComponent("SkeletonGraphic")

		var_238_5.SetStartEvent(function(arg_239_0)
			var_238_6.SetAction("attack", 0)

			var_238_7.freeze = True)
		var_238_5.SetTriggerEvent(function(arg_240_0)
			var_238_7.freeze = False

			var_238_6.SetActionCallBack(function(arg_241_0)
				if arg_241_0 == "action":
					-- block empty
				elif arg_241_0 == "finish":
					var_238_7.freeze = True))
		var_238_5.SetEndEvent(function(arg_242_0)
			var_238_7.freeze = False

			var_236_3())
		onButton(arg_236_0, var_238_1, var_236_3, SFX_CANCEL)
		coroutine.yield()
		retPaintingPrefab(var_238_3, arg_236_1.getPainting())
		var_238_6.SetActionCallBack(None)

		var_238_7.freeze = False

		PoolMgr.GetInstance().ReturnSpineChar(arg_236_1.getPrefab(), var_236_1)
		setActive(var_238_0, False)

		arg_236_0.playing = False

		arg_236_0.unfrozen()

		if arg_236_3:
			arg_236_3())

	local function var_236_4()
		if arg_236_0.strikeAnims[arg_236_2] and var_236_0 and var_236_1:
			var_236_3()

	PoolMgr.GetInstance().GetPainting(arg_236_1.getPainting(), True, function(arg_244_0)
		var_236_0 = arg_244_0

		ShipExpressionHelper.SetExpression(var_236_0, arg_236_1.getPainting())
		var_236_4())
	PoolMgr.GetInstance().GetSpineChar(arg_236_1.getPrefab(), True, function(arg_245_0)
		var_236_1 = arg_245_0
		var_236_1.transform.localScale = Vector3.one

		var_236_4())

	if not arg_236_0.strikeAnims[arg_236_2]:
		PoolMgr.GetInstance().GetUI(arg_236_2, True, function(arg_246_0)
			arg_236_0.strikeAnims[arg_236_2] = arg_246_0

			var_236_4())

def var_0_0.destroyStrikeAnim(arg_247_0):
	if arg_247_0.strikeAnims:
		for iter_247_0, iter_247_1 in pairs(arg_247_0.strikeAnims):
			iter_247_1.GetComponent("DftAniEvent").SetEndEvent(None)
			PoolMgr.GetInstance().ReturnUI(iter_247_0, iter_247_1)

		arg_247_0.strikeAnims = None

def var_0_0.doPlayEnemyAnim(arg_248_0, arg_248_1, arg_248_2, arg_248_3):
	arg_248_0.strikeAnims = arg_248_0.strikeAnims or {}

	local var_248_0
	local var_248_1

	local function var_248_2()
		if coroutine.status(var_248_1) == "suspended":
			local var_249_0, var_249_1 = coroutine.resume(var_248_1)

			assert(var_249_0, debug.traceback(var_248_1, var_249_1))

	var_248_1 = coroutine.create(function()
		arg_248_0.playing = True

		arg_248_0.frozen()

		local var_250_0 = arg_248_0.strikeAnims[arg_248_2]

		setActive(var_250_0, True)

		local var_250_1 = tf(var_250_0)
		local var_250_2 = findTF(var_250_1, "torpedo")
		local var_250_3 = findTF(var_250_1, "ship")

		setParent(var_248_0, var_250_3, False)
		setActive(var_250_3, False)
		setActive(var_250_2, False)
		var_250_1.SetParent(pg.UIMgr.GetInstance().OverlayMain.transform, False)
		var_250_1.SetAsLastSibling()

		local var_250_4 = var_250_1.GetComponent("DftAniEvent")
		local var_250_5 = var_248_0.GetComponent("SpineAnimUI")
		local var_250_6 = var_250_5.GetComponent("SkeletonGraphic")

		var_250_4.SetStartEvent(function(arg_251_0)
			var_250_5.SetAction("attack", 0)

			var_250_6.freeze = True)
		var_250_4.SetTriggerEvent(function(arg_252_0)
			var_250_6.freeze = False

			var_250_5.SetActionCallBack(function(arg_253_0)
				if arg_253_0 == "action":
					-- block empty
				elif arg_253_0 == "finish":
					var_250_6.freeze = True))
		var_250_4.SetEndEvent(function(arg_254_0)
			var_250_6.freeze = False

			var_248_2())
		onButton(arg_248_0, var_250_1, var_248_2, SFX_CANCEL)
		coroutine.yield()
		var_250_5.SetActionCallBack(None)

		var_250_6.freeze = False

		PoolMgr.GetInstance().ReturnSpineChar(arg_248_1.getPrefab(), var_248_0)
		setActive(var_250_0, False)

		arg_248_0.playing = False

		arg_248_0.unfrozen()

		if arg_248_3:
			arg_248_3())

	local function var_248_3()
		if arg_248_0.strikeAnims[arg_248_2] and var_248_0:
			var_248_2()

	PoolMgr.GetInstance().GetSpineChar(arg_248_1.getPrefab(), True, function(arg_256_0)
		var_248_0 = arg_256_0
		var_248_0.transform.localScale = Vector3.one

		var_248_3())

	if not arg_248_0.strikeAnims[arg_248_2]:
		PoolMgr.GetInstance().GetUI(arg_248_2, True, function(arg_257_0)
			arg_248_0.strikeAnims[arg_248_2] = arg_257_0

			var_248_3())

def var_0_0.doSignalSearch(arg_258_0, arg_258_1):
	arg_258_0.frozen()

	local function var_258_0()
		arg_258_0.playing = True

		arg_258_0.signalAni.SetActive(True)

		local var_259_0 = tf(arg_258_0.signalAni)

		var_259_0.SetParent(arg_258_0.topPanel, False)
		var_259_0.SetAsLastSibling()
		var_259_0.GetComponent("DftAniEvent").SetEndEvent(function(arg_260_0)
			arg_258_0.playing = False

			SetActive(arg_258_0.signalAni, False)

			if arg_258_1:
				arg_258_1()

			arg_258_0.unfrozen())
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WARNING)

	if not arg_258_0.signalAni:
		PoolMgr.GetInstance().GetUI("SignalUI", True, function(arg_261_0)
			arg_261_0.SetActive(True)

			arg_258_0.signalAni = arg_261_0

			var_258_0())
	else
		var_258_0()

def var_0_0.destroySignalSearch(arg_262_0):
	if arg_262_0.signalAni:
		arg_262_0.signalAni.GetComponent("DftAniEvent").SetEndEvent(None)
		PoolMgr.GetInstance().ReturnUI("SignalUI", arg_262_0.signalAni)

		arg_262_0.signalAni = None

def var_0_0.doPlayCommander(arg_263_0, arg_263_1, arg_263_2):
	arg_263_0.frozen()
	setActive(arg_263_0.commanderTinkle, True)

	local var_263_0 = arg_263_1.getSkills()

	setText(arg_263_0.commanderTinkle.Find("name"), #var_263_0 > 0 and var_263_0[1].getConfig("name") or "")
	setImageSprite(arg_263_0.commanderTinkle.Find("icon"), GetSpriteFromAtlas("commanderhrz/" .. arg_263_1.getConfig("painting"), ""))

	local var_263_1 = arg_263_0.commanderTinkle.GetComponent(typeof(CanvasGroup))

	var_263_1.alpha = 0

	local var_263_2 = Vector2(248, 237)

	LeanTween.value(go(arg_263_0.commanderTinkle), 0, 1, 0.5).setOnUpdate(System.Action_float(function(arg_264_0)
		local var_264_0 = arg_263_0.commanderTinkle.localPosition

		var_264_0.x = var_263_2.x + -100 * (1 - arg_264_0)
		arg_263_0.commanderTinkle.localPosition = var_264_0
		var_263_1.alpha = arg_264_0)).setEase(LeanTweenType.easeOutSine)
	LeanTween.value(go(arg_263_0.commanderTinkle), 0, 1, 0.3).setDelay(0.7).setOnUpdate(System.Action_float(function(arg_265_0)
		local var_265_0 = arg_263_0.commanderTinkle.localPosition

		var_265_0.x = var_263_2.x + 100 * arg_265_0
		arg_263_0.commanderTinkle.localPosition = var_265_0
		var_263_1.alpha = 1 - arg_265_0)).setOnComplete(System.Action(function()
		if arg_263_2:
			arg_263_2()

		arg_263_0.unfrozen()))

def var_0_0.strikeEnemy(arg_267_0, arg_267_1, arg_267_2, arg_267_3):
	local var_267_0 = arg_267_0.grid.shakeCell(arg_267_1)

	if not var_267_0:
		arg_267_3()

		return

	arg_267_0.easeDamage(var_267_0, arg_267_2, function()
		arg_267_3())

def var_0_0.easeDamage(arg_269_0, arg_269_1, arg_269_2, arg_269_3):
	arg_269_0.frozen()

	local var_269_0 = arg_269_0.levelCam.WorldToScreenPoint(arg_269_1.position)
	local var_269_1 = tf(arg_269_0.GetDamageText())

	var_269_1.position = arg_269_0.uiCam.ScreenToWorldPoint(var_269_0)

	local var_269_2 = var_269_1.localPosition

	var_269_2.y = var_269_2.y + 40
	var_269_2.z = 0

	setText(var_269_1, arg_269_2)

	var_269_1.localPosition = var_269_2

	LeanTween.value(go(var_269_1), 0, 1, 1).setOnUpdate(System.Action_float(function(arg_270_0)
		local var_270_0 = var_269_1.localPosition

		var_270_0.y = var_269_2.y + 60 * arg_270_0
		var_269_1.localPosition = var_270_0

		setTextAlpha(var_269_1, 1 - arg_270_0))).setOnComplete(System.Action(function()
		arg_269_0.ReturnDamageText(var_269_1)
		arg_269_0.unfrozen()

		if arg_269_3:
			arg_269_3()))

def var_0_0.easeAvoid(arg_272_0, arg_272_1, arg_272_2):
	arg_272_0.frozen()

	local var_272_0 = arg_272_0.levelCam.WorldToScreenPoint(arg_272_1)

	arg_272_0.avoidText.position = arg_272_0.uiCam.ScreenToWorldPoint(var_272_0)

	local var_272_1 = arg_272_0.avoidText.localPosition

	var_272_1.z = 0
	arg_272_0.avoidText.localPosition = var_272_1

	setActive(arg_272_0.avoidText, True)

	local var_272_2 = arg_272_0.avoidText.Find("avoid")

	LeanTween.value(go(arg_272_0.avoidText), 0, 1, 1).setOnUpdate(System.Action_float(function(arg_273_0)
		local var_273_0 = arg_272_0.avoidText.localPosition

		var_273_0.y = var_272_1.y + 100 * arg_273_0
		arg_272_0.avoidText.localPosition = var_273_0

		setImageAlpha(arg_272_0.avoidText, 1 - arg_273_0)
		setImageAlpha(var_272_2, 1 - arg_273_0))).setOnComplete(System.Action(function()
		setActive(arg_272_0.avoidText, False)
		arg_272_0.unfrozen()

		if arg_272_2:
			arg_272_2()))

def var_0_0.GetDamageText(arg_275_0):
	local var_275_0 = table.remove(arg_275_0.damageTextPool)

	if not var_275_0:
		var_275_0 = Instantiate(arg_275_0.damageTextTemplate)

		local var_275_1 = tf(arg_275_0.damageTextTemplate).GetSiblingIndex()

		setParent(var_275_0, tf(arg_275_0.damageTextTemplate).parent)
		tf(var_275_0).SetSiblingIndex(var_275_1 + 1)

	table.insert(arg_275_0.damageTextActive, var_275_0)
	setActive(var_275_0, True)

	return var_275_0

def var_0_0.ReturnDamageText(arg_276_0, arg_276_1):
	assert(arg_276_1)

	if not arg_276_1:
		return

	arg_276_1 = go(arg_276_1)

	table.removebyvalue(arg_276_0.damageTextActive, arg_276_1)
	table.insert(arg_276_0.damageTextPool, arg_276_1)
	setActive(arg_276_1, False)

def var_0_0.resetLevelGrid(arg_277_0):
	arg_277_0.dragLayer.localPosition = Vector3.zero

def var_0_0.ShowCurtains(arg_278_0, arg_278_1):
	setActive(arg_278_0.curtain, arg_278_1)

def var_0_0.frozen(arg_279_0):
	local var_279_0 = arg_279_0.frozenCount

	arg_279_0.frozenCount = arg_279_0.frozenCount + 1
	arg_279_0.canvasGroup.blocksRaycasts = arg_279_0.frozenCount == 0

	if var_279_0 == 0 and arg_279_0.frozenCount != 0:
		arg_279_0.emit(LevelUIConst.ON_FROZEN)

def var_0_0.unfrozen(arg_280_0, arg_280_1):
	if arg_280_0.exited:
		return

	local var_280_0 = arg_280_0.frozenCount
	local var_280_1 = arg_280_1 == -1 and arg_280_0.frozenCount or arg_280_1 or 1

	arg_280_0.frozenCount = arg_280_0.frozenCount - var_280_1
	arg_280_0.canvasGroup.blocksRaycasts = arg_280_0.frozenCount == 0

	if var_280_0 != 0 and arg_280_0.frozenCount == 0:
		arg_280_0.emit(LevelUIConst.ON_UNFROZEN)

def var_0_0.isfrozen(arg_281_0):
	return arg_281_0.frozenCount > 0

def var_0_0.enableLevelCamera(arg_282_0):
	arg_282_0.levelCamIndices = math.max(arg_282_0.levelCamIndices - 1, 0)

	if arg_282_0.levelCamIndices == 0:
		arg_282_0.levelCam.enabled = True

		pg.LayerWeightMgr.GetInstance().switchOriginParent()

def var_0_0.disableLevelCamera(arg_283_0):
	arg_283_0.levelCamIndices = arg_283_0.levelCamIndices + 1

	if arg_283_0.levelCamIndices > 0:
		arg_283_0.levelCam.enabled = False

		pg.LayerWeightMgr.GetInstance().switchOriginParent()

def var_0_0.RecordTween(arg_284_0, arg_284_1, arg_284_2):
	arg_284_0.tweens[arg_284_1] = arg_284_2

def var_0_0.DeleteTween(arg_285_0, arg_285_1):
	local var_285_0 = arg_285_0.tweens[arg_285_1]

	if var_285_0:
		LeanTween.cancel(var_285_0)

		arg_285_0.tweens[arg_285_1] = None

def var_0_0.openCommanderPanel(arg_286_0, arg_286_1, arg_286_2, arg_286_3):
	local var_286_0 = arg_286_2.id

	arg_286_0.levelCMDFormationView.setCallback(function(arg_287_0)
		if not arg_286_3:
			if arg_287_0.type == LevelUIConst.COMMANDER_OP_SHOW_SKILL:
				arg_286_0.emit(LevelMediator2.ON_COMMANDER_SKILL, arg_287_0.skill)
			elif arg_287_0.type == LevelUIConst.COMMANDER_OP_ADD:
				arg_286_0.contextData.commanderSelected = {
					chapterId = var_286_0,
					fleetId = arg_286_1.id
				}

				arg_286_0.emit(LevelMediator2.ON_SELECT_COMMANDER, arg_287_0.pos, arg_286_1.id, arg_286_2)
				arg_286_0.closeCommanderPanel()
			else
				arg_286_0.emit(LevelMediator2.ON_COMMANDER_OP, {
					FleetType = LevelUIConst.FLEET_TYPE_SELECT,
					data = arg_287_0,
					fleetId = arg_286_1.id,
					chapterId = var_286_0
				}, arg_286_2)
		elif arg_287_0.type == LevelUIConst.COMMANDER_OP_SHOW_SKILL:
			arg_286_0.emit(LevelMediator2.ON_COMMANDER_SKILL, arg_287_0.skill)
		elif arg_287_0.type == LevelUIConst.COMMANDER_OP_ADD:
			arg_286_0.contextData.eliteCommanderSelected = {
				index = arg_286_3,
				pos = arg_287_0.pos,
				chapterId = var_286_0
			}

			arg_286_0.emit(LevelMediator2.ON_SELECT_ELITE_COMMANDER, arg_286_3, arg_287_0.pos, arg_286_2)
			arg_286_0.closeCommanderPanel()
		else
			arg_286_0.emit(LevelMediator2.ON_COMMANDER_OP, {
				FleetType = LevelUIConst.FLEET_TYPE_EDIT,
				data = arg_287_0,
				index = arg_286_3,
				chapterId = var_286_0
			}, arg_286_2))
	arg_286_0.levelCMDFormationView.Load()
	arg_286_0.levelCMDFormationView.ActionInvoke("update", arg_286_1, arg_286_0.commanderPrefabs)
	arg_286_0.levelCMDFormationView.ActionInvoke("Show")

def var_0_0.updateCommanderPrefab(arg_288_0):
	if arg_288_0.levelCMDFormationView.isShowing():
		arg_288_0.levelCMDFormationView.ActionInvoke("updatePrefabs", arg_288_0.commanderPrefabs)

def var_0_0.closeCommanderPanel(arg_289_0):
	arg_289_0.levelCMDFormationView.ActionInvoke("Hide")

def var_0_0.destroyCommanderPanel(arg_290_0):
	arg_290_0.levelCMDFormationView.Destroy()

	arg_290_0.levelCMDFormationView = None

def var_0_0.setSpecialOperationTickets(arg_291_0, arg_291_1):
	arg_291_0.spTickets = arg_291_1

def var_0_0.HandleShowMsgBox(arg_292_0, arg_292_1):
	pg.MsgboxMgr.GetInstance().ShowMsgBox(arg_292_1)

def var_0_0.updatePoisonAreaTip(arg_293_0):
	local var_293_0 = arg_293_0.contextData.chapterVO
	local var_293_1 = (function(arg_294_0)
		local var_294_0 = {}
		local var_294_1 = pg.map_event_list[var_293_0.id] or {}
		local var_294_2

		if var_293_0.isLoop():
			var_294_2 = var_294_1.event_list_loop or {}
		else
			var_294_2 = var_294_1.event_list or {}

		for iter_294_0, iter_294_1 in ipairs(var_294_2):
			local var_294_3 = pg.map_event_template[iter_294_1]

			if var_294_3.c_type == arg_294_0:
				table.insert(var_294_0, var_294_3)

		return var_294_0)(ChapterConst.EvtType_Poison)

	if var_293_1:
		for iter_293_0, iter_293_1 in ipairs(var_293_1):
			local var_293_2 = iter_293_1.round_gametip

			if var_293_2 != None and var_293_2 != "" and var_293_0.getRoundNum() == var_293_2[1]:
				pg.TipsMgr.GetInstance().ShowTips(i18n(var_293_2[2]))

def var_0_0.updateVoteBookBtn(arg_295_0):
	setActive(arg_295_0._voteBookBtn, False)

def var_0_0.RecordLastMapOnExit(arg_296_0):
	local var_296_0 = getProxy(ChapterProxy)

	if var_296_0 and not arg_296_0.contextData.noRecord:
		local var_296_1 = arg_296_0.contextData.map

		if not var_296_1:
			return

		if var_296_1 and var_296_1.NeedRecordMap():
			var_296_0.recordLastMap(ChapterProxy.LAST_MAP, var_296_1.id)

		if Map.lastMapForActivity:
			var_296_0.recordLastMap(ChapterProxy.LAST_MAP_FOR_ACTIVITY, Map.lastMapForActivity)

def var_0_0.willExit(arg_297_0):
	arg_297_0.ClearMapTransitions()
	arg_297_0.loader.Clear()

	if arg_297_0.contextData.chapterVO:
		pg.UIMgr.GetInstance().UnblurPanel(arg_297_0.topPanel, arg_297_0._tf)
		pg.playerResUI.SetActive({
			active = False
		})

	if arg_297_0.levelFleetView and arg_297_0.levelFleetView.selectIds:
		arg_297_0.contextData.selectedFleetIDs = {}

		for iter_297_0, iter_297_1 in pairs(arg_297_0.levelFleetView.selectIds):
			for iter_297_2, iter_297_3 in pairs(iter_297_1):
				arg_297_0.contextData.selectedFleetIDs[#arg_297_0.contextData.selectedFleetIDs + 1] = iter_297_3

	arg_297_0.destroyChapterPanel()
	arg_297_0.destroyFleetEdit()
	arg_297_0.destroyCommanderPanel()
	arg_297_0.DestroyLevelStageView()
	arg_297_0.hideRepairWindow()
	arg_297_0.hideStrategyInfo()
	arg_297_0.hideRemasterPanel()
	arg_297_0.hideSpResult()
	arg_297_0.destroyGrid()
	arg_297_0.destroyAmbushWarn()
	arg_297_0.destroyAirStrike()
	arg_297_0.destroyTorpedo()
	arg_297_0.destroyStrikeAnim()
	arg_297_0.destroyTracking()
	arg_297_0.destroyUIAnims()
	PoolMgr.GetInstance().DestroyPrefab("chapter/cell_quad_mark", "")
	PoolMgr.GetInstance().DestroyPrefab("chapter/cell_quad", "")
	PoolMgr.GetInstance().DestroyPrefab("chapter/cell", "")
	PoolMgr.GetInstance().DestroyPrefab("chapter/plane", "")

	for iter_297_4, iter_297_5 in pairs(arg_297_0.mbDict):
		iter_297_5.Destroy()

	arg_297_0.mbDict = None

	for iter_297_6, iter_297_7 in pairs(arg_297_0.tweens):
		LeanTween.cancel(iter_297_7)

	arg_297_0.tweens = None

	if arg_297_0.cloudTimer:
		_.each(arg_297_0.cloudTimer, function(arg_298_0)
			LeanTween.cancel(arg_298_0))

		arg_297_0.cloudTimer = None

	if arg_297_0.newChapterCDTimer:
		arg_297_0.newChapterCDTimer.Stop()

		arg_297_0.newChapterCDTimer = None

	for iter_297_8, iter_297_9 in ipairs(arg_297_0.damageTextActive):
		LeanTween.cancel(iter_297_9)

	LeanTween.cancel(go(arg_297_0.avoidText))

	arg_297_0.map.localScale = Vector3.one
	arg_297_0.map.pivot = Vector2(0.5, 0.5)
	arg_297_0.float.localScale = Vector3.one
	arg_297_0.float.pivot = Vector2(0.5, 0.5)

	for iter_297_10, iter_297_11 in ipairs(arg_297_0.mapTFs):
		clearImageSprite(iter_297_11)

	_.each(arg_297_0.cloudRTFs, function(arg_299_0)
		clearImageSprite(arg_299_0))
	PoolMgr.GetInstance().DestroyAllSprite()
	Destroy(arg_297_0.enemyTpl)
	arg_297_0.RecordLastMapOnExit()
	arg_297_0.levelRemasterView.Destroy()

return var_0_0
