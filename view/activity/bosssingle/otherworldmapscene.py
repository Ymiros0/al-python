local var_0_0 = class("OtherworldMapScene", import("view.activity.BossSingle.BossSingleSceneTemplate"))
local var_0_1 = "otherworld_scroll_value_x"
local var_0_2 = "otherworld_mode"

var_0_0.MODE_STORY = 1
var_0_0.MODE_BATTLE = 2
var_0_0.NAME2INDEX = {
	xifangjudian = 1,
	mowangcheng = 4,
	julongchaoxue = 5,
	zhongbujudian = 2,
	dongfangjudian = 3
}
var_0_0.TYPE2NAME = {
	[BossSingleEnemyData.TYPE.EAST] = "xifangjudian",
	[BossSingleEnemyData.TYPE.NORMAL] = "zhongbujudian",
	[BossSingleEnemyData.TYPE.HARD] = "dongfangjudian",
	[BossSingleEnemyData.TYPE.SP] = "mowangcheng",
	[BossSingleEnemyData.TYPE.EX] = "julongchaoxue"
}
var_0_0.MAP_AREA_CNT = 5
var_0_0.MAP_AREA_START = 2
var_0_0.FLOAT_LEFT_MIN_Y = -100
var_0_0.FLOAT_ARROW_LIMIT_Y = {
	-50,
	50
}
var_0_0.STORY_TPL_HALF_WIDTH = 235
var_0_0.TERMINAL_DELAY_TIME = 0.5
var_0_0.MAP_ANIM_TIME = 0.8
var_0_0.DEFAULT_SCROLL_VALUE = 0.36

def var_0_0.getUIName(arg_1_0):
	return "OtherworldMapUI"

def var_0_0.SetEventAct(arg_2_0, arg_2_1):
	arg_2_0.eventAct = arg_2_1

def var_0_0.init(arg_3_0):
	var_0_0.super.init(arg_3_0)

	arg_3_0.mapTF = arg_3_0.findTF("map")
	arg_3_0.bgTF = arg_3_0.findTF("bg", arg_3_0.mapTF)
	arg_3_0.mapContent = arg_3_0.findTF("content", arg_3_0.mapTF)
	arg_3_0.storiesTF = arg_3_0.findTF("stories", arg_3_0.mapContent)
	arg_3_0.storyTpl = arg_3_0.findTF("story_node", arg_3_0.storiesTF)

	setActive(arg_3_0.storyTpl, False)

	arg_3_0.strongholdsTF = arg_3_0.findTF("strongholds", arg_3_0.mapContent)
	arg_3_0.locationsTF = arg_3_0.findTF("locations", arg_3_0.mapContent)
	arg_3_0.uiTF = arg_3_0.findTF("ui")
	arg_3_0.focusTF = arg_3_0.findTF("focus", arg_3_0.uiTF)

	setActive(arg_3_0.findTF("tpl", arg_3_0.focusTF), False)

	arg_3_0.topUI = arg_3_0.findTF("top", arg_3_0.uiTF)
	arg_3_0.ptIconTF = arg_3_0.findTF("res_panel/icon", arg_3_0.topUI)
	arg_3_0.ptValueTF = arg_3_0.findTF("res_panel/Text", arg_3_0.topUI)
	arg_3_0.leftUI = arg_3_0.findTF("left", arg_3_0.uiTF)
	arg_3_0.battleBtn = arg_3_0.findTF("battle_btn", arg_3_0.leftUI)
	arg_3_0.storyBtn = arg_3_0.findTF("story_btn", arg_3_0.leftUI)
	arg_3_0.leftArrow = arg_3_0.findTF("arrow", arg_3_0.leftUI)
	arg_3_0.rightArrow = arg_3_0.findTF("right/arrow", arg_3_0.uiTF)
	arg_3_0.playerId = getProxy(PlayerProxy).getRawData().id
	arg_3_0.battleHideLocations = {
		arg_3_0.findTF("2/xifangjudian", arg_3_0.locationsTF),
		arg_3_0.findTF("3/zhongbujudian", arg_3_0.locationsTF),
		arg_3_0.findTF("4/dongfangjudian", arg_3_0.locationsTF),
		arg_3_0.findTF("5/julongchaoxue", arg_3_0.locationsTF),
		arg_3_0.findTF("5/mowangcheng", arg_3_0.locationsTF),
		arg_3_0.findTF("wangdu", arg_3_0.locationsTF)
	}
	arg_3_0.clickMask = arg_3_0.findTF("click_mask", arg_3_0.uiTF)

	setActive(arg_3_0.clickMask, False)

def var_0_0.didEnter(arg_4_0):
	var_0_0.super.didEnter(arg_4_0)
	arg_4_0.SetNativeSizes()
	onButton(arg_4_0, arg_4_0.findTF("return_btn", arg_4_0.topUI), function()
		arg_4_0.onBackPressed(), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.findTF("home_btn", arg_4_0.topUI), function()
		arg_4_0.quickExitFunc(), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.findTF("help_btn", arg_4_0.topUI), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.otherworld_map_help.tip
		}), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.battleBtn, function()
		arg_4_0.PlaySwithAnim(function()
			arg_4_0.ShowBattleMode()), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.storyBtn, function()
		if not arg_4_0.eventAct:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

			return

		arg_4_0.PlaySwithAnim(function()
			arg_4_0.ShowStoryMode()), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.findTF("terminal_btn", arg_4_0.leftUI), function()
		arg_4_0.OpenTerminal(), SFX_CANCEL)
	onScroll(arg_4_0, arg_4_0.mapTF, function(arg_13_0)
		setActive(arg_4_0.leftArrow, arg_13_0.x > 0.1)
		setActive(arg_4_0.rightArrow, arg_13_0.x < 0.85)

		arg_4_0.scrollValueX = arg_13_0.x

		arg_4_0.onDragFunction())
	GetImageSpriteFromAtlasAsync(Drop.New({
		type = DROP_TYPE_RESOURCE,
		id = arg_4_0.contextData.resId
	}).getIcon(), "", arg_4_0.ptIconTF)
	arg_4_0.InitStrongholds()
	arg_4_0.InitStoryNodes()

	arg_4_0.bgScale = arg_4_0._tf.rect.height / 1440

	setLocalScale(arg_4_0.mapTF, {
		x = arg_4_0.bgScale,
		y = arg_4_0.bgScale,
		z = arg_4_0.bgScale
	})

	local var_4_0, var_4_1, var_4_2 = getSizeRate()

	arg_4_0.delta = Vector2(var_4_1 - 100, var_4_2 - 100) / 2
	arg_4_0.extendLimit = Vector2(arg_4_0.mapTF.rect.width * arg_4_0.bgScale - arg_4_0._tf.rect.width, arg_4_0.mapTF.rect.height * arg_4_0.bgScale - arg_4_0._tf.rect.height) / 2

	if not arg_4_0.contextData.mode:
		local var_4_3 = PlayerPrefs.GetInt(var_0_2 .. arg_4_0.playerId, 0)

		if var_4_3 == 0:
			arg_4_0.contextData.mode = var_0_0.MODE_BATTLE
		else
			arg_4_0.contextData.mode = var_4_3

	local var_4_4 = arg_4_0.eventAct and arg_4_0.eventAct.getConfig("config_client").open_story

	if var_4_4 and var_4_4 != "" and not pg.NewStoryMgr.GetInstance().IsPlayed(var_4_4) or not pg.NewStoryMgr.GetInstance().IsPlayed("NG0044"):
		arg_4_0.contextData.mode = var_0_0.MODE_BATTLE

	if arg_4_0.contextData.mode == var_0_0.MODE_BATTLE:
		arg_4_0.ShowBattleMode()
	elif arg_4_0.eventAct:
		arg_4_0.ShowStoryMode()
	else
		arg_4_0.ShowBattleMode()

	arg_4_0.UpdateView()
	seriesAsync({
		function(arg_14_0)
			local var_14_0 = PlayerPrefs.GetFloat(var_0_1 .. arg_4_0.playerId, 0)

			if not PlayerPrefs.HasKey(var_0_1 .. arg_4_0.playerId):
				var_14_0 = var_0_0.DEFAULT_SCROLL_VALUE

			scrollTo(arg_4_0.mapTF, var_14_0, 0)
			arg_14_0(),
		function(arg_15_0)
			local var_15_0 = arg_4_0.eventAct and arg_4_0.eventAct.getConfig("config_client").open_story

			if var_15_0 and var_15_0 != "":
				pg.NewStoryMgr.GetInstance().Play(var_15_0, arg_15_0)
			else
				arg_15_0(),
		function(arg_16_0)
			pg.SystemGuideMgr.GetInstance().PlayByGuideId("NG0044", None, arg_16_0),
		function(arg_17_0)
			if arg_4_0.contextData.openTerminal:
				arg_4_0.OpenTerminal({
					page = arg_4_0.contextData.terminalPage,
					onExit = arg_17_0
				})

				arg_4_0.contextData.openTerminal = None
				arg_4_0.contextData.terminalPage = None
			else
				arg_17_0()
	}, function()
		if arg_4_0.eventAct and arg_4_0.contextData.eventTriggerId:
			arg_4_0.managedTween(LeanTween.delayedCall, function()
				arg_4_0.emit(OtherworldMapMediator.ON_EVENT_TRIGGER, {
					actId = arg_4_0.eventAct.id,
					eventId = arg_4_0.contextData.eventTriggerId
				})

				arg_4_0.contextData.eventTriggerId = None, 0.02, None))

def var_0_0.SetNativeSizes(arg_20_0):
	eachChild(arg_20_0.bgTF, function(arg_21_0)
		eachChild(arg_21_0, function(arg_22_0)
			local var_22_0 = arg_22_0.GetComponent(typeof(Image))

			if var_22_0:
				var_22_0.SetNativeSize()))
	eachChild(arg_20_0.locationsTF, function(arg_23_0)
		if arg_23_0.childCount > 0:
			eachChild(arg_23_0, function(arg_24_0)
				local var_24_0 = arg_24_0.GetComponent(typeof(Image))

				if var_24_0:
					var_24_0.SetNativeSize())
		else
			local var_23_0 = arg_23_0.GetComponent(typeof(Image))

			if var_23_0:
				var_23_0.SetNativeSize())
	eachChild(arg_20_0.strongholdsTF, function(arg_25_0)
		local var_25_0 = arg_25_0.Find("name/Image")
		local var_25_1 = var_25_0 and var_25_0.GetComponent(typeof(Image))

		if var_25_1:
			var_25_1.SetNativeSize())

def var_0_0.BindStronghold(arg_26_0, arg_26_1, arg_26_2):
	onButton(arg_26_0, arg_26_0.findTF(arg_26_1 .. "/icon", arg_26_0.strongholdsTF), arg_26_2, SFX_PANEL)
	onButton(arg_26_0, arg_26_0.findTF(arg_26_1 .. "/name", arg_26_0.strongholdsTF), arg_26_2, SFX_PANEL)

def var_0_0.InitStrongholds(arg_27_0, arg_27_1, arg_27_2):
	arg_27_0.BindStronghold("wangdu", function()
		pg.SceneAnimMgr.GetInstance().OtherWorldCoverGoScene(SCENE.OTHERWORLD_BACKHILL))

	for iter_27_0, iter_27_1 in pairs(var_0_0.NAME2INDEX):
		arg_27_0.BindStronghold(iter_27_0, function()
			local var_29_0, var_29_1 = arg_27_0.contextData.bossActivity.CheckEntranceByIdx(iter_27_1)

			if var_29_0:
				arg_27_0.ShowNormalFleet(iter_27_1)
			else
				pg.TipsMgr.GetInstance().ShowTips(var_29_1))

def var_0_0.InitStoryNodes(arg_30_0):
	arg_30_0.eventIds = {}
	arg_30_0.nodeItemList = UIItemList.New(arg_30_0.storiesTF, arg_30_0.storyTpl)

	arg_30_0.nodeItemList.make(function(arg_31_0, arg_31_1, arg_31_2)
		if arg_31_0 == UIItemList.EventUpdate:
			local var_31_0 = arg_31_1 + 1
			local var_31_1 = arg_30_0.eventIds[var_31_0]
			local var_31_2 = arg_30_0.eventAct.GetEventById(var_31_1)

			arg_31_2.name = var_31_2.id

			arg_31_2.GetComponent(typeof(Animation)).Stop()

			if not arg_30_0.playInAnimId or arg_30_0.playInAnimId != var_31_2.id:
				setLocalScale(arg_31_2, Vector3.one)

				GetOrAddComponent(arg_31_2, typeof(CanvasGroup)).alpha = 1

			local var_31_3, var_31_4 = unpack(var_31_2.GetPos())

			setAnchoredPosition(arg_31_2, {
				x = var_31_3,
				y = var_31_4
			})
			setImageSprite(arg_31_2.Find("type"), GetSpriteFromAtlas("ui/otherworldmapui_atlas", var_31_2.GetIconName()))
			setText(arg_31_2.Find("title"), var_31_2.GetName())
			onButton(arg_30_0, arg_31_2, function()
				if arg_30_0.eventAct.CheckTrigger(var_31_1):
					arg_30_0.TriggerEvent(var_31_1), SFX_CONFIRM))

	arg_30_0.floatItemList = UIItemList.New(arg_30_0.focusTF, arg_30_0.focusTF.Find("tpl"))

	arg_30_0.floatItemList.make(function(arg_33_0, arg_33_1, arg_33_2)
		arg_33_1 = arg_33_1 + 1

		if arg_33_0 == UIItemList.EventUpdate:
			local var_33_0 = arg_30_0.eventIds[arg_33_1]
			local var_33_1 = arg_30_0.eventAct.GetEventById(var_33_0)

			arg_33_2.name = var_33_0

			setImageSprite(arg_33_2.Find("type"), GetSpriteFromAtlas("ui/otherworldmapui_atlas", var_33_1.GetIconName()))
			onButton(arg_30_0, arg_33_2, function()
				arg_30_0.FocusNode(arg_30_0.eventIds[arg_33_1]), SFX_PANEL))

def var_0_0.onDragFunction(arg_35_0):
	if not var_0_0.screenPoints:
		var_0_0.screenPoints = {
			Vector2(-arg_35_0.delta.x, arg_35_0.delta.y),
			Vector2(arg_35_0.delta.x, arg_35_0.delta.y),
			Vector2(arg_35_0.delta.x, -arg_35_0.delta.y),
			Vector2(-arg_35_0.delta.x, -arg_35_0.delta.y)
		}

	for iter_35_0, iter_35_1 in ipairs(arg_35_0.eventIds):
		local var_35_0 = arg_35_0.nodeItemList.container.Find(tostring(iter_35_1))

		if var_35_0:
			local var_35_1 = arg_35_0._tf.InverseTransformPoint(var_35_0.position)
			local var_35_2

			for iter_35_2, iter_35_3 in ipairs(var_0_0.screenPoints):
				local var_35_3 = var_0_0.screenPoints[iter_35_2 % 4 + 1]
				local var_35_4 = Vector2(var_35_1.x, var_35_1.y)

				if iter_35_3.x < 0:
					var_35_4.x = var_35_4.x + var_0_0.STORY_TPL_HALF_WIDTH

				if iter_35_3.x > 0:
					var_35_4.x = var_35_4.x - var_0_0.STORY_TPL_HALF_WIDTH

				local var_35_5, var_35_6, var_35_7 = LineLine(Vector2.zero, var_35_4, iter_35_3, var_35_3)

				if var_35_5:
					var_35_2 = var_35_4 * var_35_6

					break

			local var_35_8 = arg_35_0.floatItemList.container.Find(tostring(iter_35_1))
			local var_35_9 = var_35_8.GetComponent(typeof(CanvasGroup))

			var_35_9.interactable = tobool(var_35_2)
			var_35_9.blocksRaycasts = tobool(var_35_2)
			var_35_9.alpha = tobool(var_35_2) and 1 or 0

			if var_35_2:
				local var_35_10 = var_35_2 * (1 - 50 / var_35_2.Magnitude())

				if var_35_10.x < 0 and var_35_10.y < var_0_0.FLOAT_LEFT_MIN_Y:
					var_35_10.y = var_0_0.FLOAT_LEFT_MIN_Y

				if var_35_10.y >= var_0_0.FLOAT_ARROW_LIMIT_Y[1] and var_35_10.y <= var_0_0.FLOAT_ARROW_LIMIT_Y[2]:
					if var_35_10.x < 0:
						setActive(arg_35_0.leftArrow, False)

					if var_35_10.x > 0:
						setActive(arg_35_0.rightArrow, False)

				setAnchoredPosition(var_35_8, var_35_10)

				local var_35_11 = math.rad2Deg * math.atan2(var_35_2.y, var_35_2.x)

				setLocalEulerAngles(var_35_8.Find("arrow"), {
					z = var_35_11
				})

	if arg_35_0.contextData.mode == var_0_0.MODE_BATTLE:
		local var_35_12
		local var_35_13 = arg_35_0._tf.InverseTransformPoint(arg_35_0.findTF("wangdu", arg_35_0.strongholdsTF).position)

		var_35_13.x = var_35_13.x + 150

		for iter_35_4, iter_35_5 in ipairs(var_0_0.screenPoints):
			local var_35_14 = var_0_0.screenPoints[iter_35_4 % 4 + 1]
			local var_35_15, var_35_16, var_35_17 = LineLine(Vector2.zero, var_35_13, iter_35_5, var_35_14)

			if var_35_15:
				var_35_12 = var_35_13 * var_35_16

				break

		setActive(arg_35_0.findTF("tip", arg_35_0.leftArrow), arg_35_0.isShowWangduTip and var_35_12)

		local var_35_18
		local var_35_19 = arg_35_0._tf.InverseTransformPoint(arg_35_0.findTF("mowangcheng", arg_35_0.strongholdsTF).position)

		var_35_19.x = var_35_19.x + 100

		for iter_35_6, iter_35_7 in ipairs(var_0_0.screenPoints):
			local var_35_20 = var_0_0.screenPoints[iter_35_6 % 4 + 1]
			local var_35_21, var_35_22, var_35_23 = LineLine(Vector2.zero, var_35_19, iter_35_7, var_35_20)

			if var_35_21:
				var_35_18 = var_35_19 * var_35_22

				break

		setActive(arg_35_0.findTF("tip", arg_35_0.rightArrow), arg_35_0.isShowSpTip and var_35_18)

def var_0_0.FocusNode(arg_36_0, arg_36_1, arg_36_2):
	local var_36_0 = arg_36_0.nodeItemList.container.Find(arg_36_1).anchoredPosition * -1

	var_36_0.x = math.clamp(var_36_0.x, -arg_36_0.extendLimit.x, arg_36_0.extendLimit.x)
	var_36_0.y = math.clamp(var_36_0.y, -arg_36_0.extendLimit.y, arg_36_0.extendLimit.y)

	if arg_36_0.twFocusId:
		LeanTween.cancel(arg_36_0.twFocusId)

		arg_36_0.twFocusId = None

	local var_36_1 = {}

	table.insert(var_36_1, function(arg_37_0)
		SetCompomentEnabled(arg_36_0.mapTF, typeof(ScrollRect), False)

		local var_37_0 = (arg_36_0.mapTF.anchoredPosition - var_36_0).magnitude
		local var_37_1 = var_37_0 > 0 and var_37_0 / (40 * math.sqrt(var_37_0)) or 0

		arg_36_0.twFocusId = LeanTween.move(arg_36_0.mapTF, Vector3(var_36_0.x, var_36_0.y), var_37_1).setEase(LeanTweenType.easeInOutSine).setOnUpdate(System.Action_float(function(arg_38_0)
			arg_36_0.onDragFunction())).setOnComplete(System.Action(arg_37_0)).uniqueId)
	seriesAsync(var_36_1, function()
		SetCompomentEnabled(arg_36_0.mapTF, typeof(ScrollRect), True)

		if arg_36_2:
			arg_36_2())

def var_0_0.FocusPoint(arg_40_0, arg_40_1, arg_40_2):
	arg_40_1.x = math.clamp(arg_40_1.x, -arg_40_0.extendLimit.x, arg_40_0.extendLimit.x)
	arg_40_1.y = math.clamp(arg_40_1.y, -arg_40_0.extendLimit.y, arg_40_0.extendLimit.y)

	if arg_40_0.twFocusId:
		LeanTween.cancel(arg_40_0.twFocusId)

		arg_40_0.twFocusId = None

	local var_40_0 = {}

	table.insert(var_40_0, function(arg_41_0)
		SetCompomentEnabled(arg_40_0.mapTF, typeof(ScrollRect), False)

		local var_41_0 = (arg_40_0.mapTF.anchoredPosition - arg_40_1).magnitude
		local var_41_1 = var_41_0 > 0 and var_41_0 / (40 * math.sqrt(var_41_0)) or 0

		arg_40_0.twFocusId = LeanTween.move(arg_40_0.mapTF, Vector3(arg_40_1.x, arg_40_1.y), var_41_1).setEase(LeanTweenType.easeInOutSine).setOnUpdate(System.Action_float(function(arg_42_0)
			arg_40_0.onDragFunction())).setOnComplete(System.Action(arg_41_0)).uniqueId)
	seriesAsync(var_40_0, function()
		SetCompomentEnabled(arg_40_0.mapTF, typeof(ScrollRect), True)

		if arg_40_2:
			arg_40_2())

def var_0_0.TriggerEvent(arg_44_0, arg_44_1, arg_44_2):
	local var_44_0 = arg_44_0.eventAct.GetEventById(arg_44_1)

	switch(var_44_0.GetStoryType(), {
		[SingleEvent.STORY_TYPE.STORY] = function()
			seriesAsync({
				function(arg_46_0)
					local var_46_0 = var_44_0.GetStory()

					if var_46_0 and var_46_0 != "":
						pg.NewStoryMgr.GetInstance().Play(var_46_0, arg_46_0, True)
			}, function()
				arg_44_0.emit(OtherworldMapMediator.ON_EVENT_TRIGGER, {
					actId = arg_44_0.eventAct.id,
					eventId = arg_44_1
				})),
		[SingleEvent.STORY_TYPE.BATTLE] = function()
			seriesAsync({
				function(arg_49_0)
					local var_49_0 = tonumber(var_44_0.GetStory())

					if var_49_0 and var_49_0 > 0:
						arg_44_0.emit(OtherworldMapMediator.ON_PERFORM_COMBAT, var_49_0)

					arg_44_0.contextData.eventTriggerId = arg_44_1
			}, function()
				existCall(arg_44_2))
	}, function()
		pg.TipsMgr.GetInstance().ShowTips("trigger unkonw story_type. " .. var_44_0.GetStoryType()))

def var_0_0.UpdateToggleTip(arg_52_0):
	if not arg_52_0.eventAct:
		setActive(arg_52_0.findTF("new", arg_52_0.storyBtn), False)
		setActive(arg_52_0.findTF("new", arg_52_0.battleBtn), False)

		return

	local var_52_0 = arg_52_0.eventAct.GetAllEventIds()
	local var_52_1 = underscore.any(var_52_0, function(arg_53_0)
		local var_53_0 = arg_52_0.eventAct.GetEventById(arg_53_0)

		return var_53_0 and arg_52_0.eventAct.CheckTrigger(var_53_0.id) and var_53_0.GetMode() == SingleEvent.MODE_TYPE.STORY)
	local var_52_2 = underscore.any(var_52_0, function(arg_54_0)
		local var_54_0 = arg_52_0.eventAct.GetEventById(arg_54_0)

		return var_54_0 and arg_52_0.eventAct.CheckTrigger(var_54_0.id) and var_54_0.GetMode() == SingleEvent.MODE_TYPE.BATTLE)

	setActive(arg_52_0.findTF("new", arg_52_0.storyBtn), var_52_1)
	setActive(arg_52_0.findTF("new", arg_52_0.battleBtn), var_52_2)

def var_0_0.UpdateMapArea(arg_55_0):
	if not arg_55_0.eventAct:
		return

	local var_55_0 = arg_55_0.contextData.mode == var_0_0.MODE_STORY
	local var_55_1 = arg_55_0.eventAct.GetUnlockMapAreas()

	for iter_55_0 = var_0_0.MAP_AREA_START, var_0_0.MAP_AREA_CNT:
		local var_55_2 = table.contains(var_55_1, iter_55_0)

		setActive(arg_55_0.findTF(tostring(iter_55_0), arg_55_0.locationsTF), not var_55_0 or not var_55_2)
		setActive(arg_55_0.findTF(tostring(iter_55_0), arg_55_0.bgTF), var_55_2 and var_55_0)

def var_0_0.PlayMapAnim(arg_56_0, arg_56_1, arg_56_2):
	local var_56_0 = arg_56_0.eventAct.GetEventById(arg_56_1).GetMapOptions()
	local var_56_1 = arg_56_0.findTF(var_56_0, arg_56_0.bgTF)
	local var_56_2 = arg_56_0.findTF(var_56_0, arg_56_0.locationsTF)

	if var_56_1 and var_56_2:
		setActive(var_56_1, True)

		GetOrAddComponent(var_56_1, typeof(CanvasGroup)).alpha = 0

		arg_56_0.managedTween(LeanTween.value, None, go(var_56_1), 0, 1, var_0_0.MAP_ANIM_TIME).setOnUpdate(System.Action_float(function(arg_57_0)
			GetOrAddComponent(var_56_1, typeof(CanvasGroup)).alpha = arg_57_0)).setOnComplete(System.Action(function()
			arg_56_2()))

		GetOrAddComponent(var_56_2, typeof(CanvasGroup)).alpha = 1

		arg_56_0.managedTween(LeanTween.value, None, go(var_56_1), 1, 0, var_0_0.MAP_ANIM_TIME).setOnUpdate(System.Action_float(function(arg_59_0)
			GetOrAddComponent(var_56_2, typeof(CanvasGroup)).alpha = arg_59_0)).setOnComplete(System.Action(function()
			setActive(var_56_2, False)))
	else
		arg_56_2()

def var_0_0.UpdateWangduBtn(arg_61_0):
	arg_61_0.isShowWangduTip = OtherworldBackHillScene.IsShowTip()

	setActive(arg_61_0.findTF("wangdu/name/tip", arg_61_0.strongholdsTF), arg_61_0.isShowWangduTip)
	setActive(arg_61_0.findTF("tip", arg_61_0.leftArrow), arg_61_0.isShowWangduTip and arg_61_0.contextData.mode == var_0_0.MODE_BATTLE)

def var_0_0.UpdateEntrances(arg_62_0):
	local var_62_0 = arg_62_0.contextData.bossActivity

	for iter_62_0, iter_62_1 in pairs(var_62_0.GetEnemyDatas()):
		local var_62_1 = var_62_0.IsUnlockByEnemyId(iter_62_1.id)
		local var_62_2 = iter_62_1.GetType()
		local var_62_3 = arg_62_0.findTF(var_0_0.TYPE2NAME[var_62_2], arg_62_0.strongholdsTF)
		local var_62_4 = arg_62_0.findTF("lock", var_62_3)

		if var_62_4:
			setActive(var_62_4, not var_62_1)

		if var_62_2 == BossSingleEnemyData.TYPE.SP:
			setActive(arg_62_0.findTF("count", var_62_3), var_62_1 and iter_62_1.InTime())

			local var_62_5, var_62_6 = var_62_0.GetCounts(iter_62_1.id)

			setText(arg_62_0.findTF("count/Text", var_62_3), i18n("levelScene_chapter_count_tip") .. var_62_5 .. "/" .. var_62_6)

			local var_62_7 = var_62_1 and var_62_5 > 0 and iter_62_1.InTime()

			setActive(arg_62_0.findTF("name/tip", var_62_3), var_62_7)
			setActive(arg_62_0.findTF("tip", arg_62_0.rightArrow), var_62_7 and arg_62_0.contextData.mode == var_0_0.MODE_BATTLE)

def var_0_0.OpenTerminal(arg_63_0, arg_63_1):
	arg_63_0.emit(OtherworldMapMediator.GO_SUBLAYER, Context.New({
		mediator = OtherworldTerminalMediator,
		viewComponent = OtherworldTerminalLayer,
		data = arg_63_1
	}))

def var_0_0.UpdateEvents(arg_64_0, arg_64_1):
	if not arg_64_0.eventAct:
		return

	local var_64_0 = arg_64_0.contextData.mode == var_0_0.MODE_STORY and SingleEvent.MODE_TYPE.STORY or SingleEvent.MODE_TYPE.BATTLE

	arg_64_0.eventIds = underscore.select(arg_64_0.eventAct.GetAllEventIds(), function(arg_65_0)
		local var_65_0 = arg_64_0.eventAct.GetEventById(arg_65_0)

		return var_65_0 and arg_64_0.eventAct.CheckTrigger(var_65_0.id) and var_65_0.GetMode() == var_64_0)

	local var_64_1 = {}

	if arg_64_1:
		local var_64_2 = arg_64_0.nodeItemList.container.Find(tostring(arg_64_1)).anchoredPosition * -1
		local var_64_3 = arg_64_0.contextData.mode == var_0_0.MODE_STORY and #arg_64_0.eventIds > 0

		if #arg_64_0.eventAct.GetEventById(arg_64_1).GetOptions() > 0:
			table.insert(var_64_1, function(arg_66_0)
				arg_64_0.OpenTerminal({
					upgrade = True,
					onExit = arg_66_0
				}))

		if var_64_3:
			local var_64_4, var_64_5 = unpack(arg_64_0.eventAct.GetEventById(arg_64_0.eventIds[1]).GetPos())
			local var_64_6 = Vector2(var_64_4, var_64_5) * -1

			table.insert(var_64_1, function(arg_67_0)
				arg_64_0.FocusPoint({
					x = (var_64_2.x + var_64_6.x) / 2,
					y = (var_64_2.y + var_64_6.y) / 2
				}, arg_67_0))

		table.insert(var_64_1, function(arg_68_0)
			local var_68_0 = arg_64_0.nodeItemList.container.Find(tostring(arg_64_1))
			local var_68_1 = var_68_0.GetComponent(typeof(Animation))
			local var_68_2 = var_68_0.GetComponent(typeof(DftAniEvent))

			var_68_2.SetEndEvent(function()
				arg_68_0()
				var_68_2.SetEndEvent(None))
			var_68_1.Play("story_node_out"))
		table.insert(var_64_1, function(arg_70_0)
			if var_64_3:
				arg_64_0.playInAnimId = arg_64_0.eventIds[1]

			arg_64_0.nodeItemList.align(#arg_64_0.eventIds)
			arg_64_0.floatItemList.align(#arg_64_0.eventIds)
			arg_64_0.UpdateToggleTip()
			arg_64_0.managedTween(LeanTween.delayedCall, function()
				arg_70_0(), 0.02, None))

		if arg_64_0.eventAct.IsShowMapAnim(arg_64_1):
			table.insert(var_64_1, function(arg_72_0)
				arg_64_0.PlayMapAnim(arg_64_1, arg_72_0))

		if var_64_3:
			table.insert(var_64_1, function(arg_73_0)
				local var_73_0 = arg_64_0.nodeItemList.container.Find(tostring(arg_64_0.eventIds[1]))
				local var_73_1 = var_73_0.GetComponent(typeof(Animation))
				local var_73_2 = var_73_0.GetComponent(typeof(DftAniEvent))

				var_73_2.SetEndEvent(function()
					arg_73_0()
					var_73_2.SetEndEvent(None)

					arg_64_0.playInAnimId = None)

				GetOrAddComponent(var_73_0, typeof(CanvasGroup)).alpha = 0

				var_73_1.Play("story_node_in"))
	else
		table.insert(var_64_1, function(arg_75_0)
			arg_64_0.nodeItemList.align(#arg_64_0.eventIds)

			if not arg_64_0.first:
				eachChild(arg_64_0.nodeItemList.container, function(arg_76_0)
					if isActive(arg_76_0):
						onNextTick(function()
							arg_76_0.GetComponent(typeof(Animation)).Play("story_node_in")))

				arg_64_0.first = True

			arg_64_0.floatItemList.align(#arg_64_0.eventIds)
			arg_64_0.UpdateToggleTip()
			arg_75_0())

	setActive(arg_64_0.clickMask, True)
	seriesAsync(var_64_1, function()
		arg_64_0.onDragFunction()
		setActive(arg_64_0.clickMask, False))

def var_0_0.UpdateRes(arg_79_0):
	setText(arg_79_0.ptValueTF, getProxy(PlayerProxy).getData().getResource(arg_79_0.contextData.resId))

def var_0_0.UpdateTerminalTip(arg_80_0):
	setActive(arg_80_0.findTF("terminal_btn/tip", arg_80_0.leftUI), TerminalAdventurePage.IsTip())

def var_0_0.ShowBattleMode(arg_81_0):
	arg_81_0.contextData.mode = var_0_0.MODE_BATTLE

	setActive(arg_81_0.battleBtn, False)
	setActive(arg_81_0.storyBtn, True)
	setActive(arg_81_0.strongholdsTF, True)

	for iter_81_0, iter_81_1 in ipairs(arg_81_0.battleHideLocations):
		setActive(iter_81_1, False)

	arg_81_0.UpdateEvents()
	arg_81_0.UpdateMapArea()

	local var_81_0 = arg_81_0.contextData.bossActivity
	local var_81_1 = var_81_0.GetEnemyDataByType(BossSingleEnemyData.TYPE.SP)

	if not var_81_0.IsUnlockByEnemyId(var_81_1.id) or not var_81_1.InTime():
		arg_81_0.isShowSpTip = False
	else
		local var_81_2, var_81_3 = var_81_0.GetCounts(var_81_1.id)

		arg_81_0.isShowSpTip = var_81_2 > 0

	setActive(arg_81_0.findTF("tip", arg_81_0.rightArrow), arg_81_0.isShowSpTip)
	setActive(arg_81_0.findTF("tip", arg_81_0.leftArrow), arg_81_0.isShowWangduTip)
	PlayerPrefs.SetInt(var_0_2 .. arg_81_0.playerId, arg_81_0.contextData.mode)
	PlayerPrefs.Save()

def var_0_0.ShowStoryMode(arg_82_0):
	arg_82_0.contextData.mode = var_0_0.MODE_STORY

	setActive(arg_82_0.battleBtn, True)
	setActive(arg_82_0.storyBtn, False)
	setActive(arg_82_0.strongholdsTF, False)

	for iter_82_0, iter_82_1 in ipairs(arg_82_0.battleHideLocations):
		setActive(iter_82_1, True)

	arg_82_0.UpdateEvents()
	arg_82_0.UpdateMapArea()
	setActive(arg_82_0.findTF("tip", arg_82_0.rightArrow), False)
	setActive(arg_82_0.findTF("tip", arg_82_0.leftArrow), False)
	PlayerPrefs.SetInt(var_0_2 .. arg_82_0.playerId, arg_82_0.contextData.mode)
	PlayerPrefs.Save()

def var_0_0.PlaySwithAnim(arg_83_0, arg_83_1):
	seriesAsync({
		function(arg_84_0)
			if not arg_83_0.swithAnimTF:
				PoolMgr.GetInstance().GetUI("OtherworldCoverUI", True, function(arg_85_0)
					arg_83_0.swithAnimTF = arg_85_0.transform

					setParent(arg_83_0.swithAnimTF, arg_83_0._tf, False)
					setActive(arg_83_0.swithAnimTF, False)
					arg_84_0())
			else
				arg_84_0(),
		function(arg_86_0)
			setActive(arg_83_0.swithAnimTF, True)

			local var_86_0 = arg_83_0.swithAnimTF.Find("yuncaizhuanchang").GetComponent(typeof(SpineAnimUI))

			var_86_0.SetActionCallBack(function(arg_87_0)
				if arg_87_0 == "finish":
					setActive(arg_83_0.swithAnimTF, False)
				elif arg_87_0 == "action" and arg_83_1:
					arg_83_1())
			var_86_0.SetAction("action", 0)
	}, function()
		return)

def var_0_0.UpdateView(arg_89_0):
	arg_89_0.UpdateWangduBtn()
	arg_89_0.UpdateRes()
	arg_89_0.UpdateEntrances()
	arg_89_0.UpdateEvents()
	arg_89_0.UpdateMapArea()
	arg_89_0.UpdateTerminalTip()
	arg_89_0.UpdateToggleTip()

def var_0_0.willExit(arg_90_0):
	var_0_0.super.willExit(arg_90_0)
	arg_90_0.cleanManagedTween()
	PlayerPrefs.SetFloat(var_0_1 .. arg_90_0.playerId, arg_90_0.scrollValueX or 0)
	PlayerPrefs.Save()

def var_0_0.IsShowTip():
	local function var_91_0()
		local var_92_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.OTHER_WORLD_TERMINAL_BATTLE_ID)

		if not var_92_0 or var_92_0.isEnd():
			return False

		local var_92_1 = var_92_0.GetEnemyDataByType(BossSingleEnemyData.TYPE.SP)

		if not var_92_0.IsUnlockByEnemyId(var_92_1.id) or not var_92_1.InTime():
			return False

		local var_92_2, var_92_3 = var_92_0.GetCounts(var_92_1.id)

		return var_92_2 > 0

	return TerminalAdventurePage.IsTip() or var_91_0()

var_0_0.personalRandomData = None

return var_0_0
