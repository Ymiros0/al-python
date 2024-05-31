local var_0_0 = class("NewServerCarnivalScene", import("...base.BaseUI"))

var_0_0.TASK_PAGE = 1
var_0_0.SHOP_PAGE = 2
var_0_0.GIFT_PAGE = 3

def var_0_0.getUIName(arg_1_0):
	return "NewServerCarnivalUI"

def var_0_0.preload(arg_2_0, arg_2_1):
	local var_2_0 = {}

	table.insert(var_2_0, function(arg_3_0)
		pg.m02.sendNotification(GAME.GET_NEW_SERVER_SHOP, {
			def callback:(arg_4_0)
				arg_2_0.SetNewServerShop(arg_4_0)
				arg_3_0()
		}))
	parallelAsync(var_2_0, arg_2_1)

def var_0_0.SetNewServerShop(arg_5_0, arg_5_1):
	arg_5_0.newServerShop = arg_5_1

def var_0_0.setData(arg_6_0):
	local var_6_0 = getProxy(ActivityProxy)
	local var_6_1 = var_6_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_TASK)
	local var_6_2 = var_6_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_SHOP)
	local var_6_3 = var_6_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_GIFT)

	if var_6_1 and not var_6_1.isEnd():
		arg_6_0.taskActivity = var_6_1
	else
		arg_6_0.taskActivity = None

	if var_6_2 and not var_6_2.isEnd():
		arg_6_0.shopActivity = var_6_2
	else
		arg_6_0.shopActivity = None

	if var_6_3 and not var_6_3.isEnd():
		arg_6_0.giftActivity = var_6_3
	else
		arg_6_0.giftActivity = None

	arg_6_0.player = getProxy(PlayerProxy).getData()

def var_0_0.init(arg_7_0):
	arg_7_0.blurPanel = arg_7_0.findTF("blur_panel")
	arg_7_0.top = arg_7_0.findTF("adapt/top", arg_7_0.blurPanel)
	arg_7_0.resPanel = arg_7_0.findTF("res", arg_7_0.top)
	arg_7_0.backBtn = arg_7_0.findTF("back_btn", arg_7_0.top)
	arg_7_0.helpBtn = arg_7_0.findTF("help_btn", arg_7_0.top)
	arg_7_0.leftPanel = arg_7_0.findTF("left")
	arg_7_0.timeTF = arg_7_0.findTF("time", arg_7_0.leftPanel)
	arg_7_0.toggles = {
		arg_7_0.findTF("frame/toggle_group/task", arg_7_0.leftPanel),
		arg_7_0.findTF("frame/toggle_group/shop", arg_7_0.leftPanel),
		arg_7_0.findTF("frame/toggle_group/gift", arg_7_0.leftPanel)
	}
	arg_7_0.main = arg_7_0.findTF("main")
	arg_7_0.pages = {
		arg_7_0.findTF("task_container", arg_7_0.main),
		arg_7_0.findTF("shop_container", arg_7_0.main),
		arg_7_0.findTF("gift_container", arg_7_0.main)
	}

def var_0_0.didEnter(arg_8_0):
	onButton(arg_8_0, arg_8_0.backBtn, function()
		arg_8_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.newserver_activity_tip.tip
		}), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.findTF("gem/add_btn", arg_8_0.resPanel), function()
		local function var_11_0()
			if not pg.m02.hasMediator(ChargeMediator.__cname):
				pg.m02.sendNotification(GAME.GO_SCENE, SCENE.CHARGE, {
					wrap = ChargeScene.TYPE_DIAMOND
				})
			else
				pg.m02.sendNotification(var_0_0.GO_MALL)

		if PLATFORM_CODE == PLATFORM_JP:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				fontSize = 23,
				yesText = "text_buy",
				content = i18n("word_diamond_tip", arg_8_0.player.getFreeGem(), arg_8_0.player.getChargeGem(), arg_8_0.player.getTotalGem()),
				onYes = var_11_0,
				alignment = TextAnchor.UpperLeft,
				weight = LayerWeightConst.TOP_LAYER
			})
		else
			var_11_0(), SFX_PANEL)
	arg_8_0.updatePages()
	arg_8_0.updateTime()
	setText(arg_8_0.findTF("gem/gem_value", arg_8_0.resPanel), arg_8_0.player.getTotalGem())

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.toggles):
		onToggle(arg_8_0, iter_8_1, function(arg_13_0)
			setActive(arg_8_0.pages[iter_8_0], arg_13_0)
			arg_8_0.updateLocalRedDotData(iter_8_0)
			arg_8_0.updatePages()
			setActive(arg_8_0.resPanel, arg_13_0 and iter_8_0 == var_0_0.GIFT_PAGE))

	setActive(arg_8_0.toggles[var_0_0.TASK_PAGE], arg_8_0.taskActivity)
	setActive(arg_8_0.toggles[var_0_0.SHOP_PAGE], arg_8_0.shopActivity)
	setActive(arg_8_0.toggles[var_0_0.GIFT_PAGE], arg_8_0.giftActivity)

	arg_8_0.page = arg_8_0.taskActivity and var_0_0.TASK_PAGE or var_0_0.SHOP_PAGE
	arg_8_0.page = arg_8_0.contextData.page and arg_8_0.contextData.page or arg_8_0.page

	triggerToggle(arg_8_0.toggles[arg_8_0.page], True)

def var_0_0.updateShopDedDot(arg_14_0):
	setActive(arg_14_0.findTF("tip", arg_14_0.toggles[var_0_0.SHOP_PAGE]), arg_14_0.newServerShopPage.isTip())

def var_0_0.updatePages(arg_15_0):
	if arg_15_0.taskActivity:
		if not arg_15_0.newServerTaskPage:
			arg_15_0.newServerTaskPage = NewServerTaskPage.New(arg_15_0.pages[var_0_0.TASK_PAGE], arg_15_0.event, arg_15_0.contextData)

			arg_15_0.newServerTaskPage.Reset()
			arg_15_0.newServerTaskPage.Load()

		setActive(arg_15_0.findTF("tip", arg_15_0.toggles[var_0_0.TASK_PAGE]), arg_15_0.newServerTaskPage.isTip())

	if arg_15_0.shopActivity:
		if not arg_15_0.newServerShopPage:
			arg_15_0.newServerShopPage = NewServerShopPage.New(arg_15_0.pages[var_0_0.SHOP_PAGE], arg_15_0.event, arg_15_0.contextData)

			arg_15_0.newServerShopPage.Reset()
			arg_15_0.newServerShopPage.SetShop(arg_15_0.newServerShop)
			arg_15_0.newServerShopPage.Load()

		setActive(arg_15_0.findTF("tip", arg_15_0.toggles[var_0_0.SHOP_PAGE]), arg_15_0.newServerShopPage.isTip())

	if arg_15_0.giftActivity:
		if not arg_15_0.newServerGiftPage:
			arg_15_0.newServerGiftPage = NewServerGiftPage.New(arg_15_0.pages[var_0_0.GIFT_PAGE], arg_15_0.event, arg_15_0.contextData)

			arg_15_0.newServerGiftPage.Reset()
			arg_15_0.newServerGiftPage.Load()

		setActive(arg_15_0.findTF("tip", arg_15_0.toggles[var_0_0.GIFT_PAGE]), arg_15_0.newServerGiftPage.isTip())

def var_0_0.updateLocalRedDotData(arg_16_0, arg_16_1):
	if arg_16_1 == var_0_0.SHOP_PAGE:
		if arg_16_0.newServerShopPage.isTip() and PlayerPrefs.GetInt("newserver_shop_first_" .. arg_16_0.player.id) == 0:
			PlayerPrefs.SetInt("newserver_shop_first_" .. arg_16_0.player.id, 1)
	elif arg_16_1 == var_0_0.GIFT_PAGE and arg_16_0.newServerGiftPage.isTip():
		PlayerPrefs.SetInt("newserver_gift_first_" .. arg_16_0.player.id, 1)

def var_0_0.updateTime(arg_17_0):
	local var_17_0 = pg.TimeMgr.GetInstance()
	local var_17_1 = (arg_17_0.taskActivity and arg_17_0.taskActivity.stopTime or arg_17_0.shopActivity.stopTime) - var_17_0.GetServerTime()
	local var_17_2 = math.floor(var_17_1 / 86400)
	local var_17_3 = math.floor((var_17_1 - var_17_2 * 86400) / 3600)

	setText(arg_17_0.timeTF, i18n("newserver_time", var_17_2, var_17_3))
	setActive(arg_17_0.findTF("title_activity", arg_17_0.timeTF), arg_17_0.taskActivity)
	setActive(arg_17_0.findTF("title_shop", arg_17_0.timeTF), not arg_17_0.taskActivity)

def var_0_0.onUpdateTask(arg_18_0):
	if arg_18_0.newServerTaskPage:
		arg_18_0.newServerTaskPage.onUpdateTask()

	if arg_18_0.newServerShopPage:
		arg_18_0.newServerShopPage.UpdateRes()

	arg_18_0.updatePages()

def var_0_0.onUpdatePlayer(arg_19_0, arg_19_1):
	arg_19_0.player = arg_19_1

	setText(arg_19_0.findTF("gem/gem_value", arg_19_0.resPanel), arg_19_0.player.getTotalGem())

	if arg_19_0.newServerGiftPage:
		arg_19_0.newServerGiftPage.onUpdatePlayer(arg_19_1)

def var_0_0.onUpdateGift(arg_20_0):
	if arg_20_0.newServerGiftPage:
		arg_20_0.newServerGiftPage.onUpdateGift()

	arg_20_0.updatePages()

def var_0_0.willExit(arg_21_0):
	return

def var_0_0.isShow():
	local var_22_0 = getProxy(ActivityProxy)
	local var_22_1 = var_22_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_TASK)
	local var_22_2 = var_22_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_SHOP)
	local var_22_3 = var_22_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_GIFT)

	return var_22_1 and not var_22_1.isEnd() or var_22_2 and not var_22_2.isEnd() or var_22_3 and not var_22_3.isEnd()

def var_0_0.isTip():
	local var_23_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_TASK)

	if var_23_0 and not var_23_0.isEnd():
		local var_23_1 = getProxy(TaskProxy)
		local var_23_2 = var_23_0.getConfig("config_data")

		for iter_23_0, iter_23_1 in ipairs(var_23_2):
			for iter_23_2, iter_23_3 in ipairs(iter_23_1):
				assert(var_23_1.getTaskVO(iter_23_3), "without this task." .. iter_23_3)

				if var_23_1.getTaskVO(iter_23_3).getTaskStatus() == 1:
					return True

	return False

return var_0_0
