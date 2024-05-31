local var_0_0 = class("BuildShipScene", import("...base.BaseUI"))

var_0_0.PAGE_BUILD = 1
var_0_0.PAGE_QUEUE = 2
var_0_0.PAGE_SUPPORT = 3
var_0_0.PAGE_UNSEAM = 4
var_0_0.PAGE_PRAY = 5
var_0_0.PAGE_NEWSERVER = 6
var_0_0.PROJECTS = {
	SPECIAL = "special",
	ACTIVITY = "new",
	HEAVY = "heavy",
	LIGHT = "light"
}

def var_0_0.getUIName(arg_1_0):
	return "BuildShipUI"

def var_0_0.ResUISettings(arg_2_0):
	return True

def var_0_0.setPools(arg_3_0, arg_3_1):
	arg_3_0.pools = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_1):
		table.insert(arg_3_0.pools, iter_3_1)

def var_0_0.setPlayer(arg_4_0, arg_4_1):
	arg_4_0.contextData.player = arg_4_1

def var_0_0.setUseItem(arg_5_0, arg_5_1):
	arg_5_0.contextData.itemVO = arg_5_1 or Item.New({
		count = 0,
		id = pg.ship_data_create_material[1].use_item
	})

	if arg_5_0.poolsPage and arg_5_0.poolsPage.GetLoaded():
		arg_5_0.poolsPage.UpdateItem(arg_5_0.contextData.itemVO.count)

def var_0_0.setStartCount(arg_6_0, arg_6_1):
	arg_6_0.contextData.startCount = arg_6_1

def var_0_0.setFlagShip(arg_7_0, arg_7_1):
	arg_7_0.contextData.falgShip = arg_7_1

def var_0_0.RefreshActivityBuildPool(arg_8_0, arg_8_1):
	arg_8_0.poolsPage.RefreshActivityBuildPool(arg_8_1)

def var_0_0.RefreshFreeBuildActivity(arg_9_0):
	arg_9_0.poolsPage.RefreshFreeBuildActivity()
	arg_9_0.poolsPage.UpdateTicket()

def var_0_0.RefreshRegularExchangeCount(arg_10_0):
	arg_10_0.poolsPage.RefreshRegularExchangeCount()

def var_0_0.init(arg_11_0):
	Input.multiTouchEnabled = False
	arg_11_0.blurPanel = arg_11_0.findTF("blur_panel")
	arg_11_0.topPanel = arg_11_0.findTF("adapt/top", arg_11_0.blurPanel)
	arg_11_0.backBtn = arg_11_0.findTF("back_btn", arg_11_0.topPanel)
	arg_11_0.toggles = {
		arg_11_0.findTF("adapt/left_length/frame/tagRoot/build_btn", arg_11_0.blurPanel),
		arg_11_0.findTF("adapt/left_length/frame/tagRoot/queue_btn", arg_11_0.blurPanel),
		arg_11_0.findTF("adapt/left_length/frame/tagRoot/support_btn", arg_11_0.blurPanel),
		arg_11_0.findTF("adapt/left_length/frame/tagRoot/unseam_btn", arg_11_0.blurPanel),
		arg_11_0.findTF("adapt/left_length/frame/tagRoot/pray_btn", arg_11_0.blurPanel),
		arg_11_0.findTF("adapt/left_length/frame/tagRoot/other_build_btn", arg_11_0.blurPanel)
	}
	arg_11_0.tip = arg_11_0.toggles[2].Find("tip")
	arg_11_0.contextData.msgbox = BuildShipMsgBox.New(arg_11_0._tf, arg_11_0.event)
	arg_11_0.contextData.helpWindow = BuildShipHelpWindow.New(arg_11_0._tf, arg_11_0.event)
	arg_11_0.poolsPage = BuildShipPoolsPage.New(arg_11_0._tf, arg_11_0.event, arg_11_0.contextData)
	arg_11_0.supportShipPoolPage = SupportShipPoolPage.New(arg_11_0._tf, arg_11_0.event, arg_11_0.contextData)

def var_0_0.didEnter(arg_12_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_12_0.blurPanel, {
		groupName = LayerWeightConst.GROUP_BUILDSHIPSCENE
	})
	onButton(arg_12_0, arg_12_0.backBtn, function()
		arg_12_0.emit(var_0_0.ON_BACK), SFX_CANCEL)

	local var_12_0 = arg_12_0.findTF("adapt/left_length/stamp", arg_12_0.blurPanel)

	setActive(var_12_0, getProxy(TaskProxy).mingshiTouchFlagEnabled())
	onButton(arg_12_0, var_12_0, function()
		getProxy(TaskProxy).dealMingshiTouchFlag(11), SFX_CONFIRM)

	for iter_12_0, iter_12_1 in ipairs(arg_12_0.toggles):
		onToggle(arg_12_0, iter_12_1, function(arg_15_0)
			arg_12_0.switchPage(iter_12_0, arg_15_0), SFX_PANEL)

	local var_12_1 = getProxy(ActivityProxy)
	local var_12_2 = var_12_1.getActivityById(ActivityConst.ACTIVITY_PRAY_POOL)

	if var_12_2 and not var_12_2.isEnd():
		setActive(arg_12_0.toggles[var_0_0.PAGE_PRAY], True)
	else
		setActive(arg_12_0.toggles[var_0_0.PAGE_PRAY], False)

	if underscore.any(arg_12_0.pools, function(arg_16_0)
		return checkExist(var_12_1.getBuildPoolActivity(arg_16_0), {
			"getConfig",
			{
				"type"
			}
		}) == ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD):
		setActive(arg_12_0.toggles[var_0_0.PAGE_NEWSERVER], True)
	else
		setActive(arg_12_0.toggles[var_0_0.PAGE_NEWSERVER], False)

	local var_12_3 = arg_12_0.contextData.page or pg.SeriesGuideMgr.GetInstance().isRunning() and var_0_0.PAGE_BUILD or var_0_0.PAGE_NEWSERVER

	if not isActive(arg_12_0.toggles[var_12_3]):
		var_12_3 = var_0_0.PAGE_BUILD

	triggerToggle(arg_12_0.toggles[var_12_3], True)
	PoolMgr.GetInstance().GetUI("al_bg01", True, function(arg_17_0)
		arg_17_0.SetActive(True)
		setParent(arg_17_0, arg_12_0._tf)
		arg_17_0.transform.SetAsFirstSibling())
	TagTipHelper.SetFreeBuildMark()

	arg_12_0.bulinTip = AprilFoolBulinSubView.ShowAprilFoolBulin(arg_12_0, arg_12_0.blurPanel)

def var_0_0.checkPage(arg_18_0):
	if arg_18_0.contextData.msgbox and arg_18_0.contextData.msgbox.GetLoaded() and arg_18_0.contextData.msgbox.isShowing():
		arg_18_0.contextData.msgbox.Hide()

	if arg_18_0.contextData.helpWindow and arg_18_0.contextData.helpWindow.GetLoaded() and arg_18_0.contextData.helpWindow.isShowing():
		arg_18_0.contextData.helpWindow.Hide()

	local var_18_0 = getProxy(ActivityProxy)

	if underscore.any(arg_18_0.pools, function(arg_19_0)
		return checkExist(var_18_0.getBuildPoolActivity(arg_19_0), {
			"getConfig",
			{
				"type"
			}
		}) == ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD):
		setActive(arg_18_0.toggles[var_0_0.PAGE_NEWSERVER], True)
	else
		setActive(arg_18_0.toggles[var_0_0.PAGE_NEWSERVER], False)

	if not isActive(arg_18_0.toggles[var_0_0.PAGE_NEWSERVER]) and arg_18_0.contextData.page == var_0_0.PAGE_NEWSERVER:
		triggerToggle(arg_18_0.toggles[var_0_0.PAGE_BUILD], True)
	else
		arg_18_0.poolsPage.Flush(arg_18_0.pools)

def var_0_0.switchPage(arg_20_0, arg_20_1, arg_20_2):
	if arg_20_2:
		arg_20_0.contextData.page = arg_20_1 == var_0_0.PAGE_UNSEAM and var_0_0.PAGE_BUILD or arg_20_1

	if arg_20_1 == var_0_0.PAGE_UNSEAM:
		if arg_20_2:
			arg_20_0.emit(BuildShipMediator.OPEN_DESTROY)
	elif arg_20_1 == var_0_0.PAGE_QUEUE:
		if arg_20_2:
			arg_20_0.emit(BuildShipMediator.OPEN_PROJECT_LIST)
		else
			arg_20_0.emit(BuildShipMediator.REMOVE_PROJECT_LIST)
	elif arg_20_1 == var_0_0.PAGE_SUPPORT:
		arg_20_0.supportShipPoolPage.ExecuteAction("ShowOrHide", arg_20_2)

		if arg_20_2:
			arg_20_0.supportShipPoolPage.ExecuteAction("Flush")
	elif arg_20_1 == var_0_0.PAGE_BUILD:
		arg_20_0.poolsPage.ExecuteAction("ShowOrHide", arg_20_2)

		if arg_20_2:
			arg_20_0.poolsPage.ExecuteAction("Flush", arg_20_0.pools, False)
	elif arg_20_1 == var_0_0.PAGE_NEWSERVER:
		arg_20_0.poolsPage.ExecuteAction("ShowOrHide", arg_20_2)

		if arg_20_2:
			arg_20_0.poolsPage.ExecuteAction("Flush", arg_20_0.pools, True)
	elif arg_20_1 == var_0_0.PAGE_PRAY:
		if arg_20_2:
			arg_20_0.emit(BuildShipMediator.OPEN_PRAY_PAGE)
		else
			arg_20_0.emit(BuildShipMediator.CLOSE_PRAY_PAGE)

def var_0_0.updateQueueTip(arg_21_0, arg_21_1):
	setActive(arg_21_0.tip, arg_21_1 > 0)

def var_0_0.onBackPressed(arg_22_0):
	if arg_22_0.contextData.helpWindow.GetLoaded() and arg_22_0.contextData.helpWindow.isShowing():
		arg_22_0.contextData.helpWindow.Hide()

		return

	if arg_22_0.contextData.msgbox.GetLoaded() and arg_22_0.contextData.msgbox.isShowing():
		arg_22_0.contextData.msgbox.Hide()

		return

	arg_22_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.willExit(arg_23_0):
	Input.multiTouchEnabled = True

	arg_23_0.contextData.msgbox.Destroy()
	arg_23_0.contextData.helpWindow.Destroy()
	arg_23_0.poolsPage.Destroy()
	arg_23_0.supportShipPoolPage.Destroy()
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_23_0.blurPanel, arg_23_0._tf)

return var_0_0
