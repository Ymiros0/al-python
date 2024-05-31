local var_0_0 = class("ActivityMainScene", import("..base.BaseUI"))

var_0_0.LOCK_ACT_MAIN = "ActivityMainScene.LOCK_ACT_MAIN"
var_0_0.UPDATE_ACTIVITY = "ActivityMainScene.UPDATE_ACTIVITY"
var_0_0.GET_PAGE_BGM = "ActivityMainScene.GET_PAGE_BGM"
var_0_0.FLUSH_TABS = "ActivityMainScene.FLUSH_TABS"

def var_0_0.preload(arg_1_0, arg_1_1):
	arg_1_1()

def var_0_0.getUIName(arg_2_0):
	return "ActivityMainUI"

def var_0_0.PlayBGM(arg_3_0):
	return

def var_0_0.onBackPressed(arg_4_0):
	if arg_4_0.locked:
		return

	for iter_4_0, iter_4_1 in pairs(arg_4_0.windowList):
		if isActive(iter_4_1._tf):
			arg_4_0.HideWindow(iter_4_1.class)

			return

	if arg_4_0.awardWindow and arg_4_0.awardWindow.GetLoaded() and arg_4_0.awardWindow.isShowing():
		arg_4_0.awardWindow.Hide()

		return

	arg_4_0.emit(var_0_0.ON_BACK_PRESSED)

local var_0_1

def var_0_0.init(arg_5_0):
	arg_5_0.btnBack = arg_5_0.findTF("blur_panel/adapt/top/back_btn")
	arg_5_0.pageContainer = arg_5_0.findTF("pages")
	arg_5_0.permanentFinshMask = arg_5_0.findTF("pages_finish")
	arg_5_0.tabs = arg_5_0.findTF("scroll/viewport/content")
	arg_5_0.tab = arg_5_0.findTF("tab", arg_5_0.tabs)
	arg_5_0.entranceList = UIItemList.New(arg_5_0.findTF("enter/viewport/content"), arg_5_0.findTF("enter/viewport/content/btn"))
	arg_5_0.windowList = {}
	arg_5_0.lockAll = arg_5_0.findTF("blur_panel/lock_all")
	arg_5_0.awardWindow = AwardWindow.New(arg_5_0._tf, arg_5_0.event)
	arg_5_0.chargeTipWindow = ChargeTipWindow.New(arg_5_0._tf, arg_5_0.event)

	setActive(arg_5_0.tab, False)
	setActive(arg_5_0.lockAll, False)
	setActive(arg_5_0.permanentFinshMask, False)
	setText(arg_5_0.permanentFinshMask.Find("piece/Text"), i18n("activity_permanent_tips2"))
	onButton(arg_5_0, arg_5_0.permanentFinshMask.Find("piece/arrow/Image"), function()
		arg_5_0.emit(ActivityMediator.FINISH_ACTIVITY_PERMANENT), SFX_PANEL)

	arg_5_0.tabsList = UIItemList.New(arg_5_0.tabs, arg_5_0.tab)

	arg_5_0.tabsList.make(function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_0 == UIItemList.EventUpdate:
			local var_7_0 = arg_5_0.activities[arg_7_1 + 1]

			if arg_5_0.pageDic[var_7_0.id] != None:
				local var_7_1 = var_7_0.getConfig("title_res_tag")

				if var_7_1:
					local var_7_2 = arg_5_0.findTF("red", arg_7_2)
					local var_7_3 = GetSpriteFromAtlas("activityuitable/" .. var_7_1 .. "_text", "") or GetSpriteFromAtlas("activityuitable/activity_text", "")
					local var_7_4 = GetSpriteFromAtlas("activityuitable/" .. var_7_1 .. "_text_selected", "") or GetSpriteFromAtlas("activityuitable/activity_text_selected", "")

					setImageSprite(arg_5_0.findTF("off/text", arg_7_2), var_7_3, True)
					setImageSprite(arg_5_0.findTF("on/text", arg_7_2), var_7_4, True)
					setActive(var_7_2, var_7_0.readyToAchieve())
					onToggle(arg_5_0, arg_7_2, function(arg_8_0)
						if arg_8_0:
							arg_5_0.selectActivity(var_7_0), SFX_PANEL)
				else
					onToggle(arg_5_0, arg_7_2, function(arg_9_0)
						arg_5_0.loadActivityPanel(arg_9_0, var_7_0), SFX_PANEL))

def var_0_0.didEnter(arg_10_0):
	onButton(arg_10_0, arg_10_0.btnBack, function()
		arg_10_0.emit(var_0_0.ON_BACK), SOUND_BACK)
	arg_10_0.updateEntrances()
	arg_10_0.emit(ActivityMediator.SHOW_NEXT_ACTIVITY)
	arg_10_0.bind(var_0_0.LOCK_ACT_MAIN, function(arg_12_0, arg_12_1)
		arg_10_0.locked = arg_12_1

		setActive(arg_10_0.lockAll, arg_12_1))
	arg_10_0.bind(var_0_0.UPDATE_ACTIVITY, function(arg_13_0, arg_13_1)
		arg_10_0.updateActivity(arg_13_1))
	arg_10_0.bind(var_0_0.GET_PAGE_BGM, function(arg_14_0, arg_14_1, arg_14_2)
		arg_14_2.bgm = arg_10_0.getBGM(arg_14_1) or arg_10_0.getBGM())
	arg_10_0.bind(var_0_0.FLUSH_TABS, function()
		arg_10_0.flushTabs())

def var_0_0.setPlayer(arg_16_0, arg_16_1):
	arg_16_0.shareData.SetPlayer(arg_16_1)

def var_0_0.setFlagShip(arg_17_0, arg_17_1):
	arg_17_0.shareData.SetFlagShip(arg_17_1)

def var_0_0.updateTaskLayers(arg_18_0):
	if not arg_18_0.activity:
		return

	arg_18_0.updateActivity(arg_18_0.activity)

def var_0_0.instanceActivityPage(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_1.getConfig("page_info")

	if var_19_0.class_name and not arg_19_0.pageDic[arg_19_1.id] and not arg_19_1.isEnd():
		local var_19_1 = import("view.activity.subPages." .. var_19_0.class_name).New(arg_19_0.pageContainer, arg_19_0.event, arg_19_0.contextData)

		if var_19_1.UseSecondPage(arg_19_1):
			var_19_1.SetUIName(var_19_0.ui_name2)
		else
			var_19_1.SetUIName(var_19_0.ui_name)

		var_19_1.SetShareData(arg_19_0.shareData)

		arg_19_0.pageDic[arg_19_1.id] = var_19_1

def var_0_0.setActivities(arg_20_0, arg_20_1):
	arg_20_0.activities = arg_20_1 or {}
	arg_20_0.shareData = arg_20_0.shareData or ActivityShareData.New()
	arg_20_0.pageDic = arg_20_0.pageDic or {}

	for iter_20_0, iter_20_1 in ipairs(arg_20_1):
		arg_20_0.instanceActivityPage(iter_20_1)

	arg_20_0.activity = None

	table.sort(arg_20_0.activities, function(arg_21_0, arg_21_1)
		local var_21_0 = arg_21_0.getShowPriority()
		local var_21_1 = arg_21_1.getShowPriority()

		if var_21_0 == var_21_1:
			return arg_21_0.id > arg_21_1.id

		return var_21_1 < var_21_0)
	arg_20_0.flushTabs()

def var_0_0.getActivityIndex(arg_22_0, arg_22_1):
	for iter_22_0, iter_22_1 in ipairs(arg_22_0.activities):
		if iter_22_1.id == arg_22_1:
			return iter_22_0

	return None

def var_0_0.updateActivity(arg_23_0, arg_23_1):
	if ActivityConst.PageIdLink[arg_23_1.id]:
		arg_23_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.PageIdLink[arg_23_1.id])

	if arg_23_1.isShow() and not arg_23_1.isEnd():
		arg_23_0.activities[arg_23_0.getActivityIndex(arg_23_1.id) or #arg_23_0.activities + 1] = arg_23_1

		table.sort(arg_23_0.activities, function(arg_24_0, arg_24_1)
			local var_24_0 = arg_24_0.getShowPriority()
			local var_24_1 = arg_24_1.getShowPriority()

			if var_24_0 == var_24_1:
				return arg_24_0.id > arg_24_1.id

			return var_24_1 < var_24_0)

		if not arg_23_0.pageDic[arg_23_1.id]:
			arg_23_0.instanceActivityPage(arg_23_1)

		arg_23_0.flushTabs()

		if arg_23_0.activity and arg_23_0.activity.id == arg_23_1.id:
			arg_23_0.activity = arg_23_1

			arg_23_0.pageDic[arg_23_1.id].ActionInvoke("Flush", arg_23_1)
			setActive(arg_23_0.permanentFinshMask, pg.activity_task_permanent[arg_23_1.id] and arg_23_1.canPermanentFinish())

def var_0_0.removeActivity(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_0.getActivityIndex(arg_25_1)

	if var_25_0:
		table.remove(arg_25_0.activities, var_25_0)
		arg_25_0.pageDic[arg_25_1].Destroy()

		arg_25_0.pageDic[arg_25_1] = None

		arg_25_0.flushTabs()

		if arg_25_0.activity and arg_25_0.activity.id == arg_25_1:
			arg_25_0.activity = None

			arg_25_0.verifyTabs()

def var_0_0.loadLayers(arg_26_0):
	local var_26_0 = arg_26_0.pageDic[arg_26_0.activity.id]

	if var_26_0 and var_26_0.OnLoadLayers:
		var_26_0.OnLoadLayers()

def var_0_0.removeLayers(arg_27_0):
	local var_27_0 = arg_27_0.pageDic[arg_27_0.activity.id]

	if var_27_0 and var_27_0.OnRemoveLayers:
		var_27_0.OnRemoveLayers()

def var_0_0.GetOnShowEntranceData():
	var_0_1 = var_0_1 or require("GameCfg.activity.EntranceData")

	assert(var_0_1, "Missing EntranceData.lua!")

	var_0_1 = var_0_1 or {}

	return (_.select(var_0_1, function(arg_29_0)
		return arg_29_0.isShow and arg_29_0.isShow()))

def var_0_0.updateEntrances(arg_30_0):
	local var_30_0 = var_0_0.GetOnShowEntranceData()
	local var_30_1 = math.max(#var_30_0, 5)

	arg_30_0.entranceList.make(function(arg_31_0, arg_31_1, arg_31_2)
		if arg_31_0 == UIItemList.EventUpdate:
			local var_31_0 = var_30_0[arg_31_1 + 1]
			local var_31_1 = "empty"

			removeOnButton(arg_31_2)

			local var_31_2 = False

			if var_31_0 and table.getCount(var_31_0) != 0 and var_31_0.isShow():
				onButton(arg_30_0, arg_31_2, function()
					arg_30_0.emit(var_31_0.event, var_31_0.data[1], var_31_0.data[2]), SFX_PANEL)

				var_31_1 = var_31_0.banner

				if var_31_0.isTip:
					var_31_2 = var_31_0.isTip()

			setActive(arg_31_2.Find("tip"), var_31_2)
			LoadImageSpriteAsync("activitybanner/" .. var_31_1, arg_31_2))
	arg_30_0.entranceList.align(var_30_1)

def var_0_0.flushTabs(arg_33_0):
	arg_33_0.tabsList.align(#arg_33_0.activities)

def var_0_0.selectActivity(arg_34_0, arg_34_1):
	if arg_34_1 and (not arg_34_0.activity or arg_34_0.activity.id != arg_34_1.id):
		local var_34_0 = arg_34_0.pageDic[arg_34_1.id]

		assert(var_34_0, "找不到id." .. arg_34_1.id .. "的活动页，请检查")
		var_34_0.Load()
		var_34_0.ActionInvoke("Flush", arg_34_1)
		var_34_0.ActionInvoke("ShowOrHide", True)

		if arg_34_0.activity and arg_34_0.activity.id != arg_34_1.id:
			arg_34_0.pageDic[arg_34_0.activity.id].ActionInvoke("ShowOrHide", False)

		arg_34_0.activity = arg_34_1
		arg_34_0.contextData.id = arg_34_1.id

		setActive(arg_34_0.permanentFinshMask, pg.activity_task_permanent[arg_34_1.id] and arg_34_1.canPermanentFinish())

def var_0_0.verifyTabs(arg_35_0, arg_35_1):
	local var_35_0 = arg_35_0.getActivityIndex(arg_35_1) or 1
	local var_35_1 = arg_35_0.tabs.GetChild(var_35_0 - 1)

	triggerToggle(var_35_1, True)

def var_0_0.loadActivityPanel(arg_36_0, arg_36_1, arg_36_2):
	local var_36_0 = arg_36_2.getConfig("type")
	local var_36_1

	if var_36_1 and arg_36_1:
		arg_36_0.emit(ActivityMediator.OPEN_LAYER, var_36_1)
	elif var_36_1 and not arg_36_1:
		arg_36_0.emit(ActivityMediator.CLOSE_LAYER, var_36_1.mediator)
	else
		originalPrint("------活动id为" .. arg_36_2.id .. "类型为" .. arg_36_2.getConfig("type") .. "的页面不存在")

def var_0_0.getBonusWindow(arg_37_0, arg_37_1, arg_37_2):
	local var_37_0 = arg_37_0.findTF(arg_37_1)

	if not var_37_0:
		PoolMgr.GetInstance().GetUI("ActivitybonusWindow", True, function(arg_38_0)
			SetParent(arg_38_0, arg_37_0._tf, False)

			arg_38_0.name = arg_37_1

			arg_37_2(arg_38_0))
	else
		arg_37_2(var_37_0)

def var_0_0.ShowWindow(arg_39_0, arg_39_1, arg_39_2):
	local var_39_0 = arg_39_1.__cname

	if not arg_39_0.windowList[var_39_0]:
		arg_39_0.getBonusWindow(var_39_0, function(arg_40_0)
			arg_39_0.windowList[var_39_0] = arg_39_1.New(tf(arg_40_0), arg_39_0)

			arg_39_0.windowList[var_39_0].Show(arg_39_2))
	else
		arg_39_0.windowList[var_39_0].Show(arg_39_2)

def var_0_0.HideWindow(arg_41_0, arg_41_1):
	local var_41_0 = arg_41_1.__cname

	if not arg_41_0.windowList[var_41_0]:
		return

	arg_41_0.windowList[var_41_0].Hide()

def var_0_0.ShowAwardWindow(arg_42_0, arg_42_1, arg_42_2, arg_42_3):
	arg_42_0.awardWindow.ExecuteAction("Flush", arg_42_1, arg_42_2, arg_42_3)

def var_0_0.OnChargeSuccess(arg_43_0, arg_43_1):
	arg_43_0.chargeTipWindow.ExecuteAction("Show", arg_43_1)

def var_0_0.willExit(arg_44_0):
	arg_44_0.shareData = None

	for iter_44_0, iter_44_1 in pairs(arg_44_0.pageDic):
		iter_44_1.Destroy()

	for iter_44_2, iter_44_3 in pairs(arg_44_0.windowList):
		iter_44_3.Dispose()

	if arg_44_0.awardWindow:
		arg_44_0.awardWindow.Destroy()

		arg_44_0.awardWindow = None

	if arg_44_0.chargeTipWindow:
		arg_44_0.chargeTipWindow.Destroy()

		arg_44_0.chargeTipWindow = None

return var_0_0
