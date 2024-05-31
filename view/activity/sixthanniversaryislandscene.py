local var_0_0 = class("SixthAnniversaryIslandScene", import("..base.BaseUI"))

var_0_0.optionsPath = {
	"top/btn_home"
}
var_0_0.SHOP = "SixthAnniversaryIslandScene.SHOP"

def var_0_0.getUIName(arg_1_0):
	return "SixthAnniversaryIslandUI"

def var_0_0.setActivity(arg_2_0, arg_2_1):
	arg_2_0.activity = arg_2_1

def var_0_0.setNodeIds(arg_3_0, arg_3_1):
	arg_3_0.ids = arg_3_1

def var_0_0.setPlayer(arg_4_0, arg_4_1):
	arg_4_0.player = arg_4_1

	setText(arg_4_0.rtResPanel.Find("tpl/Text"), arg_4_0.player.getResById(350) or 0)

def var_0_0.setResDrop(arg_5_0, arg_5_1, arg_5_2):
	arg_5_0.resDrop = arg_5_1
	arg_5_0.resDailyNumber = arg_5_2

	setText(arg_5_0.rtResPanel.Find("tpl_2/Text"), arg_5_1.count or 0)

def var_0_0.init(arg_6_0):
	arg_6_0.rtTop = arg_6_0._tf.Find("top")

	pg.UIMgr.GetInstance().OverlayPanel(arg_6_0.rtTop)

	arg_6_0.effectObjs = {}
	arg_6_0.proxy = getProxy(IslandProxy)

	local var_6_0 = pg.TimeMgr.GetInstance()
	local var_6_1 = arg_6_0._tf.Find("map/content")

	arg_6_0.nodeItemList = UIItemList.New(var_6_1, var_6_1.Find("node"))

	arg_6_0.nodeItemList.make(function(arg_7_0, arg_7_1, arg_7_2)
		arg_7_1 = arg_7_1 + 1

		if arg_7_0 == UIItemList.EventUpdate:
			local var_7_0 = arg_6_0.ids[arg_7_1]
			local var_7_1 = arg_6_0.proxy.GetNode(var_7_0)

			arg_7_2.name = var_7_1.id

			local var_7_2, var_7_3 = unpack(var_7_1.getConfig("address"))

			setAnchoredPosition(arg_7_2, {
				x = var_7_2,
				y = var_7_3
			})

			local var_7_4 = var_7_1.getConfig("type")

			eachChild(arg_7_2.Find("main/type"), function(arg_8_0)
				setActive(arg_8_0, arg_8_0.name == tostring(var_7_4)))
			setLocalScale(arg_7_2, Vector3(0, 0, 1))
			setActive(arg_7_2.Find("name"), var_7_1.getConfig("icon_name") != "")
			onToggle(arg_6_0, arg_7_2, function(arg_9_0)
				if arg_9_0:
					arg_6_0.selectId = var_7_0
					arg_6_0.contextData.lastNodeId = var_7_0)
			setActive(arg_7_2.Find("click"), True)
			onButton(arg_6_0, arg_7_2.Find("click"), function()
				local var_10_0 = arg_6_0.proxy.GetNode(var_7_0)

				triggerToggle(arg_7_2, var_10_0.CanToggleOn())

				if var_10_0.CanTrigger():
					arg_6_0.isAutoPlayStory = False

					arg_6_0.triggerNode(var_7_0)
				elif var_10_0.IsRefresh() and var_10_0.IsCompleted():
					local var_10_1 = var_6_0.GetNextTime(0, 0, 0) - var_6_0.GetServerTime()
					local var_10_2 = 3
					local var_10_3

					var_10_3 = Timer.New(function()
						if arg_6_0.exited:
							var_10_3.Stop()

							var_10_3 = None

						if var_10_2 == 0:
							setActive(arg_7_2.Find("main/time"), False)
						else
							setText(arg_7_2.Find("main/time/Text"), i18n("islandnode_tips1") .. var_6_0.DescCDTime(var_10_1))

							var_10_1 = var_10_1 - 1
							var_10_2 = var_10_2 - 1, 1, 3)

					var_10_3.func()
					var_10_3.Start()
					setActive(arg_7_2.Find("main/time"), True), SFX_CONFIRM)
			arg_6_0.refreshNode(var_7_0))

	local var_6_2 = arg_6_0.rtTop.Find("panel/content/mask/scroll_rect")

	arg_6_0.panelItemList = UIItemList.New(var_6_2, var_6_2.Find("tpl"))

	arg_6_0.panelItemList.make(function(arg_12_0, arg_12_1, arg_12_2)
		arg_12_1 = arg_12_1 + 1

		if arg_12_0 == UIItemList.EventUpdate:
			local var_12_0 = arg_6_0.proxy.GetNode(arg_6_0.dailyIds[arg_12_1])

			arg_12_2.name = var_12_0.id

			GetImageSpriteFromAtlasAsync("ui/sixthanniversaryislandui_atlas", var_12_0.getConfig("icon"), arg_12_2.Find("Image"))
			setActive(arg_12_2.Find("mask"), not var_12_0.RedDotHint())
			onButton(arg_6_0, arg_12_2, function()
				arg_6_0.focus(var_12_0.id, LeanTweenType.easeInOutSine), SFX_PANEL))
	triggerToggle(arg_6_0.rtTop.Find("panel/toggle"), False)

	local var_6_3 = arg_6_0._tf.Find("top/focus")

	arg_6_0.floatItemList = UIItemList.New(var_6_3, var_6_3.Find("main_mark"))

	arg_6_0.floatItemList.make(function(arg_14_0, arg_14_1, arg_14_2)
		arg_14_1 = arg_14_1 + 1

		if arg_14_0 == UIItemList.EventUpdate:
			arg_14_2.name = arg_6_0.mainIds[arg_14_1]

			onButton(arg_6_0, arg_14_2, function()
				arg_6_0.focus(arg_6_0.mainIds[arg_14_1], LeanTweenType.easeInOutSine), SFX_PANEL))

	arg_6_0.rtResPanel = arg_6_0.rtTop.Find("res")
	arg_6_0.rtMap = arg_6_0._tf.Find("map")

	arg_6_0.rtMap.GetComponent(typeof(ScrollRect)).onValueChanged.AddListener(function()
		arg_6_0.onDragFunction())

	local var_6_4, var_6_5, var_6_6 = getSizeRate()

	arg_6_0.delta = Vector2(var_6_5 - 100, var_6_6 - 100) / 2
	arg_6_0.extendLimit = Vector2(arg_6_0.rtMap.rect.width - arg_6_0._tf.rect.width, arg_6_0.rtMap.rect.height - arg_6_0._tf.rect.height) / 2
	arg_6_0.displayDic = {}

	onButton(arg_6_0, arg_6_0.rtTop.Find("btn_back"), function()
		arg_6_0.closeView(), SFX_CANCEL)
	setActive(arg_6_0.rtTop.Find("btn_now"), False)
	onButton(arg_6_0, arg_6_0.rtTop.Find("btns/btn_shop"), function()
		arg_6_0.emit(SixthAnniversaryIslandMediator.GO_SHOP), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.rtTop.Find("btns/btn_note"), function()
		arg_6_0.emit(SixthAnniversaryIslandMediator.OPEN_NOTE), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.rtTop.Find("btns/btn_help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("island_help")
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.rtResPanel.Find("tpl"), function()
		arg_6_0.emit(SixthAnniversaryIslandMediator.OPEN_RES, {
			id = 350,
			type = 1
		}, ""), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.rtResPanel.Find("tpl_2"), function()
		arg_6_0.emit(SixthAnniversaryIslandMediator.OPEN_RES, Clone(arg_6_0.resDrop), i18n("island_game_limit_help", arg_6_0.resDailyNumber)), SFX_PANEL)

def var_0_0.onDragFunction(arg_23_0):
	if not var_0_0.screenPoints:
		var_0_0.screenPoints = {
			Vector2(-arg_23_0.delta.x, arg_23_0.delta.y),
			Vector2(arg_23_0.delta.x, arg_23_0.delta.y),
			Vector2(arg_23_0.delta.x, -arg_23_0.delta.y),
			Vector2(-arg_23_0.delta.x, -arg_23_0.delta.y)
		}

	for iter_23_0, iter_23_1 in ipairs(arg_23_0.mainIds):
		local var_23_0 = arg_23_0.nodeItemList.container.Find(iter_23_1)
		local var_23_1 = arg_23_0._tf.InverseTransformPoint(var_23_0.position)
		local var_23_2

		for iter_23_2, iter_23_3 in ipairs(var_0_0.screenPoints):
			local var_23_3 = var_0_0.screenPoints[iter_23_2 % 4 + 1]
			local var_23_4, var_23_5, var_23_6 = LineLine(Vector2.zero, Vector2(var_23_1.x, var_23_1.y), iter_23_3, var_23_3)

			if var_23_4:
				var_23_2 = var_23_1 * var_23_5

				break

		local var_23_7 = arg_23_0.floatItemList.container.Find(iter_23_1)
		local var_23_8 = var_23_7.GetComponent(typeof(CanvasGroup))

		var_23_8.interactable = tobool(var_23_2)
		var_23_8.blocksRaycasts = tobool(var_23_2)
		var_23_8.alpha = tobool(var_23_2) and 1 or 0

		if var_23_2:
			setAnchoredPosition(var_23_7, var_23_2 * (1 - 50 / var_23_2.Magnitude()))

			local var_23_9 = math.rad2Deg * math.atan2(var_23_2.y, var_23_2.x) - 45

			setLocalEulerAngles(var_23_7.Find("arrow"), {
				z = var_23_9
			})
			setLocalEulerAngles(var_23_7.Find("arrow_shadow"), {
				z = var_23_9
			})

def var_0_0.focus(arg_24_0, arg_24_1, arg_24_2, arg_24_3):
	local var_24_0 = arg_24_0.nodeItemList.container.Find(arg_24_1)

	if not arg_24_3:
		triggerToggle(var_24_0, arg_24_0.proxy.GetNode(arg_24_1).CanToggleOn())

	local var_24_1 = var_24_0.anchoredPosition * -1

	var_24_1.x = math.clamp(var_24_1.x, -arg_24_0.extendLimit.x, arg_24_0.extendLimit.x)
	var_24_1.y = math.clamp(var_24_1.y, -arg_24_0.extendLimit.y, arg_24_0.extendLimit.y)

	if arg_24_0.twFocusId:
		LeanTween.cancel(arg_24_0.twFocusId)

		arg_24_0.twFocusId = None

	if arg_24_2:
		local var_24_2 = {}

		table.insert(var_24_2, function(arg_25_0)
			SetCompomentEnabled(arg_24_0.rtMap, typeof(ScrollRect), False)

			local var_25_0 = (arg_24_0.rtMap.anchoredPosition - var_24_1).magnitude
			local var_25_1 = var_25_0 > 0 and var_25_0 / (40 * math.sqrt(var_25_0)) or 0

			arg_24_0.twFocusId = LeanTween.move(arg_24_0.rtMap, Vector3(var_24_1.x, var_24_1.y), var_25_1).setEase(arg_24_2).setOnUpdate(System.Action_float(function(arg_26_0)
				arg_24_0.onDragFunction())).setOnComplete(System.Action(arg_25_0)).uniqueId)
		seriesAsync(var_24_2, function()
			SetCompomentEnabled(arg_24_0.rtMap, typeof(ScrollRect), True))
	else
		arg_24_0.rtMap.anchoredPosition = var_24_1

		arg_24_0.onDragFunction()

def var_0_0.triggerNode(arg_28_0, arg_28_1):
	local var_28_0 = getProxy(IslandProxy).GetNode(arg_28_1)

	if var_28_0.IsNew():
		arg_28_0.emit(SixthAnniversaryIslandMediator.MARK_NODE_AFTER_NEW, arg_28_1)

	if var_28_0.IsCompleted():
		if var_28_0.getConfig("type") == 5:
			arg_28_0.emit(SixthAnniversaryIslandMediator.INTO_ENTRANCE, var_28_0.getConfig("params")[1])
	else
		arg_28_0.triggerEvent(var_28_0)

def var_0_0.triggerEvent(arg_29_0, arg_29_1):
	assert(arg_29_1.eventId and arg_29_1.eventId != 0)

	local var_29_0 = IslandEvent.New({
		id = arg_29_1.eventId
	})

	switch(var_29_0.getConfig("type"), {
		[3] = function()
			local var_30_0 = {}
			local var_30_1 = var_29_0.getConfig("story")

			if var_30_1 and var_30_1 != "":
				table.insert(var_30_0, function(arg_31_0)
					if arg_29_0.isAutoPlayStory:
						pg.NewStoryMgr.GetInstance().ForceAutoPlay(var_30_1, arg_31_0)
					else
						pg.NewStoryMgr.GetInstance().ForceManualPlay(var_30_1, arg_31_0))
				table.insert(var_30_0, function(arg_32_0, arg_32_1, arg_32_2, arg_32_3)
					arg_29_0.isAutoPlayStory = arg_32_3

					arg_32_0(arg_32_2))

			seriesAsync(var_30_0, function(arg_33_0)
				arg_29_0.emit(SixthAnniversaryIslandMediator.OPEN_QTE_GAME, var_29_0.getConfig("params")[1], function(arg_34_0)
					arg_29_0.emit(SixthAnniversaryIslandMediator.TRIGGER_NODE_EVENT, arg_29_1.id, arg_34_0 or 0)))
	}, function()
		local var_35_0 = {}
		local var_35_1 = var_29_0.getConfig("story")

		if var_35_1 and var_35_1 != "":
			table.insert(var_35_0, function(arg_36_0)
				if arg_29_0.isAutoPlayStory:
					pg.NewStoryMgr.GetInstance().ForceAutoPlay(var_35_1, arg_36_0, True)
				else
					pg.NewStoryMgr.GetInstance().ForceManualPlay(var_35_1, arg_36_0, True))
			table.insert(var_35_0, function(arg_37_0, arg_37_1, arg_37_2, arg_37_3)
				arg_29_0.isAutoPlayStory = arg_37_3

				arg_37_0(arg_37_2))

		seriesAsync(var_35_0, function(arg_38_0)
			arg_29_0.emit(SixthAnniversaryIslandMediator.TRIGGER_NODE_EVENT, arg_29_1.id, arg_38_0 or 0)))

def var_0_0.afterTriggerEvent(arg_39_0, arg_39_1):
	local var_39_0 = arg_39_0.proxy.GetNode(arg_39_1)

	if var_39_0.IsCompleted():
		underscore.each(arg_39_0.ids, function(arg_40_0)
			arg_39_0.refreshNode(arg_40_0))
		arg_39_0.refreshDailyPanel()
	else
		arg_39_0.refreshNode(arg_39_1)

	if var_39_0.CanTrigger():
		triggerToggle(arg_39_0.nodeItemList.container.Find(arg_39_1), var_39_0.CanToggleOn())
		arg_39_0.triggerNode(arg_39_1)

def var_0_0.refreshNode(arg_41_0, arg_41_1):
	local var_41_0 = arg_41_0.nodeItemList.container.Find(arg_41_1)
	local var_41_1 = getProxy(IslandProxy).GetNode(arg_41_1)
	local var_41_2 = var_41_1.IsVisual()

	setActive(var_41_0.Find("click"), var_41_2)

	local var_41_3 = var_41_2 and var_41_1.GetScale() or 0
	local var_41_4 = Vector3(var_41_3, var_41_3, 1)

	if var_41_0.localScale != var_41_4:
		LeanTween.cancel(var_41_0)
		LeanTween.scale(var_41_0, var_41_4, 0.3).setEase(LeanTweenType.easeInOutSine)

	if var_41_2 and not arg_41_0.displayDic[arg_41_1]:
		arg_41_0.displayDic[arg_41_1] = True

		local var_41_5 = var_41_1.getConfig("icon")

		if var_41_5 == "":
			SetCompomentEnabled(var_41_0.Find("main"), typeof(Image), False)
			SetCompomentEnabled(var_41_0.Find("selected_back/light"), typeof(Image), False)
		else
			GetSpriteFromAtlasAsync("ui/sixthanniversaryislandui_atlas", var_41_5, function(arg_42_0)
				setImageSprite(var_41_0.Find("main"), arg_42_0)
				setImageSprite(var_41_0.Find("main/mask"), arg_42_0))
			GetImageSpriteFromAtlasAsync("ui/sixthanniversaryislandui_atlas", var_41_5 .. "_light", var_41_0.Find("selected_back/light"))

		if var_41_1.getConfig("icon_name") != "":
			GetImageSpriteFromAtlasAsync("ui/sixthanniversaryislandui_atlas", var_41_1.getConfig("icon_name"), var_41_0.Find("name/Image"), True)

		local var_41_6 = var_41_1.GetEffectName()

		if var_41_6 != "":
			pg.PoolMgr.GetInstance().GetUI(var_41_6, True, function(arg_43_0)
				table.insert(arg_41_0.effectObjs, {
					name = var_41_6,
					go = arg_43_0
				})
				setParent(arg_43_0, var_41_0.Find("click"), False))

	setActive(var_41_0.Find("main/type"), var_41_1.RedDotHint())

	local var_41_7 = var_41_1.IsRefresh() and var_41_1.IsCompleted()

	setActive(var_41_0.Find("name"), not var_41_7 and not var_41_1.IsTreasure())
	setActive(var_41_0.Find("main/mask"), var_41_7)
	setActive(var_41_0.Find("main/time"), False)
	setActive(var_41_0.Find("main/new"), var_41_1.IsNew())

	local var_41_8 = GetOrAddComponent(var_41_0.Find("main"), typeof("LOutLine"))

	ReflectionHelp.RefSetField(typeof("LOutLine"), "OutlineWidth", var_41_8, var_41_7 and 0 or 3)
	ReflectionHelp.RefCallMethod(typeof("LOutLine"), "_Refresh", var_41_8)
	triggerToggle(var_41_0, arg_41_0.selectId == arg_41_1 and var_41_1.CanToggleOn())

def var_0_0.refreshDailyPanel(arg_44_0):
	arg_44_0.dailyIds = underscore.select(arg_44_0.ids, function(arg_45_0)
		local var_45_0 = arg_44_0.proxy.GetNode(arg_45_0)

		return (var_45_0.IsRefresh() or var_45_0.IsFlowerField()) and var_45_0.IsVisual())

	arg_44_0.panelItemList.align(#arg_44_0.dailyIds)

	arg_44_0.mainIds = underscore.select(arg_44_0.ids, function(arg_46_0)
		local var_46_0 = arg_44_0.proxy.GetNode(arg_46_0)

		return var_46_0.IsMain() and var_46_0.IsVisual())

	arg_44_0.floatItemList.align(#arg_44_0.mainIds)
	arg_44_0.onDragFunction()

def var_0_0.focusList(arg_47_0, arg_47_1, arg_47_2, arg_47_3):
	for iter_47_0, iter_47_1 in ipairs(arg_47_1):
		if arg_47_0.proxy.GetNode(iter_47_1).IsVisual():
			arg_47_0.focus(iter_47_1, arg_47_2, arg_47_3)

			return True

	return False

def var_0_0.didEnter(arg_48_0):
	arg_48_0.nodeItemList.align(#arg_48_0.ids)
	arg_48_0.refreshDailyPanel()
	arg_48_0.updateTaskTip()

	local var_48_0 = {}

	if arg_48_0.contextData.nodeIds and #arg_48_0.contextData.nodeIds > 0:
		table.insert(var_48_0, function(arg_49_0)
			if not arg_48_0.focusList(arg_48_0.contextData.nodeIds):
				pg.TipsMgr.GetInstance().ShowTips(i18n("islandnode_tips8"))
				arg_49_0()

			arg_48_0.contextData.nodeIds = None)
	elif arg_48_0.contextData.checkMain:
		table.insert(var_48_0, function(arg_50_0)
			local var_50_0 = getProxy(IslandProxy)
			local var_50_1 = underscore.filter(underscore.map(arg_48_0.ids, function(arg_51_0)
				return var_50_0.GetNode(arg_51_0)), function(arg_52_0)
				return arg_52_0.IsMain() and not arg_52_0.IsCompleted())
			local var_50_2 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2).GetTotalBuildingLevel()

			if #var_50_1 > 0 and underscore.all(var_50_1, function(arg_53_0)
				return not arg_53_0.IsUnlock() and arg_53_0.getConfig("open_need")[1] > var_50_2):
				pg.TipsMgr.GetInstance().ShowTips(i18n("islandnode_tips9"))

			arg_50_0())

	arg_48_0.contextData.checkMain = None

	local var_48_1 = {
		1001,
		1002,
		1003,
		1004,
		1005
	}

	if arg_48_0.contextData.lastNodeId:
		table.insert(var_48_1, 1, arg_48_0.contextData.lastNodeId)

	table.insert(var_48_0, function(arg_54_0)
		if not arg_48_0.focusList(var_48_1):
			arg_54_0())
	seriesAsync(var_48_0, function()
		arg_48_0.focusList({
			1050,
			1051,
			1052,
			1053
		}, None, True))

	local var_48_2 = "HAIDAORICHANG2"

	pg.NewStoryMgr.GetInstance().Play(var_48_2, function()
		if arg_48_0.contextData.wraps:
			switch(arg_48_0.contextData.wraps, {
				[var_0_0.SHOP] = function()
					arg_48_0.emit(SixthAnniversaryIslandMediator.GO_SHOP)
			})

			arg_48_0.contextData.wraps = None)

def var_0_0.updateTaskTip(arg_58_0):
	setActive(arg_58_0.rtTop.Find("btns/btn_note/tip"), getProxy(ActivityTaskProxy).getActTaskTip(ActivityConst.ISLAND_TASK_ID))

def var_0_0.willExit(arg_59_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_59_0.rtTop, arg_59_0._tf)
	arg_59_0.rtMap.GetComponent(typeof(ScrollRect)).onValueChanged.RemoveAllListeners()

	local var_59_0 = pg.PoolMgr.GetInstance()

	for iter_59_0, iter_59_1 in ipairs(arg_59_0.effectObjs):
		var_59_0.ReturnUI(iter_59_1.name, iter_59_1.go)

return var_0_0
