local var_0_0 = class("WorldPortLayer", import("..base.BaseUI"))

var_0_0.Listeners = {
	onUpdateGoods = "OnUpdateGoods",
	onUpdateMoneyCount = "OnUpdateMoneyCount",
	onUpdateTasks = "OnUpdateTasks",
	onUpdateNGoods = "OnUpdateNGoods"
}
var_0_0.TitleName = {
	"text_gangkou",
	"text_operation",
	"text_supply"
}
var_0_0.PageMain = 0
var_0_0.PageTask = 1
var_0_0.PageShop = 2
var_0_0.PageDockyard = 3
var_0_0.PageNShop = 4
var_0_0.BlurPages = {
	[var_0_0.PageTask] = True,
	[var_0_0.PageShop] = True,
	[var_0_0.PageNShop] = True
}
var_0_0.optionsPath = {
	"blur_panel/adapt/top/title/option"
}

def var_0_0.getUIName(arg_1_0):
	return "WorldPortUI"

def var_0_0.init(arg_2_0):
	for iter_2_0, iter_2_1 in pairs(var_0_0.Listeners):
		arg_2_0[iter_2_0] = function(...)
			var_0_0[iter_2_1](arg_2_0, ...)

	arg_2_0.rtBg = arg_2_0.findTF("bg")
	arg_2_0.rtEnterIcon = arg_2_0.rtBg.Find("enter_icon")
	arg_2_0.rtBgNShop = arg_2_0._tf.Find("bg_2")
	arg_2_0.rtBlurPanel = arg_2_0.findTF("blur_panel")
	arg_2_0.rtTasks = arg_2_0.rtBlurPanel.Find("adapt/tasks")
	arg_2_0.rtShop = arg_2_0.rtBlurPanel.Find("adapt/shop")
	arg_2_0.rtPainting = arg_2_0.rtShop.Find("paint")
	arg_2_0.btnPainting = arg_2_0.rtShop.Find("paint_touch")

	setActive(arg_2_0.btnPainting, False)

	arg_2_0.rtChat = arg_2_0.rtShop.Find("chat")

	setActive(arg_2_0.rtChat, False)

	arg_2_0.rtNShop = arg_2_0.rtBlurPanel.Find("adapt/new_shop")
	arg_2_0.containerPort = arg_2_0.rtNShop.Find("frame/content/left")
	arg_2_0.tplPort = arg_2_0.containerPort.Find("port_tpl")
	arg_2_0.poolTplPort = {
		arg_2_0.tplPort
	}
	arg_2_0.rtNGoodsContainer = arg_2_0.rtNShop.Find("frame/content/right/page/view/content")
	arg_2_0.rtNShopRes = arg_2_0.rtNShop.Find("frame/content/right/page/title/res")

	local var_2_0 = Drop.New({
		type = DROP_TYPE_WORLD_ITEM,
		id = WorldItem.PortMoneyId
	})

	GetImageSpriteFromAtlasAsync(var_2_0.getIcon(), "", arg_2_0.rtNShopRes.Find("icon/Image"), False)
	setText(arg_2_0.rtNShopRes.Find("icon/name"), var_2_0.getName())

	arg_2_0.rtTop = arg_2_0.rtBlurPanel.Find("adapt/top")
	arg_2_0.btnBack = arg_2_0.rtTop.Find("title/back_button")
	arg_2_0.rtTopTitle = arg_2_0.rtTop.Find("title")
	arg_2_0.rtImageTitle = arg_2_0.rtTopTitle.Find("print/title")
	arg_2_0.rtImageTitleTask = arg_2_0.rtTopTitle.Find("print/title_task")
	arg_2_0.rtImageTitleShop = arg_2_0.rtTopTitle.Find("print/title_shop")
	arg_2_0.rtTopLeft = arg_2_0.rtTop.Find("left_stage")
	arg_2_0.rtTopRight = arg_2_0.rtTop.Find("right_stage")
	arg_2_0.wsWorldInfo = WSWorldInfo.New()
	arg_2_0.wsWorldInfo.transform = arg_2_0.rtTopRight.Find("display_panel/world_info")

	arg_2_0.wsWorldInfo.Setup()
	setText(arg_2_0.rtTopRight.Find("display_panel/title/title"), i18n("world_map_title_tips"))
	setText(arg_2_0.rtTopRight.Find("display_panel/title/title_en"), i18n("world_map_title_tips_en"))
	setText(arg_2_0.wsWorldInfo.transform.Find("power/bg/Word"), i18n("world_total_power"))
	setText(arg_2_0.wsWorldInfo.transform.Find("explore/mileage/Text"), i18n("world_mileage"))
	setText(arg_2_0.wsWorldInfo.transform.Find("explore/pressing/Text"), i18n("world_pressing"))

	arg_2_0.rtTopBottom = arg_2_0.rtTop.Find("bottom_stage")
	arg_2_0.btnOperation = arg_2_0.rtTopBottom.Find("btn/operation")
	arg_2_0.btnSupply = arg_2_0.rtTopBottom.Find("btn/supply")
	arg_2_0.btnDockyard = arg_2_0.rtTopBottom.Find("btn/dockyard")
	arg_2_0.resPanel = WorldResource.New()

	arg_2_0.resPanel._tf.SetParent(arg_2_0.rtTop.Find("title/resources"), False)

	arg_2_0.rtTaskWindow = arg_2_0.findTF("task_window")
	arg_2_0.wsTasks = {}
	arg_2_0.wsGoods = {}
	arg_2_0.page = -1
	arg_2_0.dirtyFlags = {}
	arg_2_0.cdTF = arg_2_0.rtShop.Find("timer_bg")
	arg_2_0.emptyTF = arg_2_0.rtShop.Find("frame/scrollview/empty")
	arg_2_0.refreshBtn = arg_2_0.rtShop.Find("refresh_btn")

	setActive(arg_2_0.refreshBtn, False)

	arg_2_0.glitchArtMaterial = arg_2_0.findTF("resource/material1").GetComponent(typeof(Image)).material
	arg_2_0.singleWindow = OriginShopSingleWindow.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.multiWindow = OriginShopMultiWindow.New(arg_2_0._tf, arg_2_0.event)

def var_0_0.didEnter(arg_4_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_4_0._tf, {
		groupName = arg_4_0.getGroupNameFromData()
	})
	onButton(arg_4_0, arg_4_0.btnBack, function()
		if arg_4_0.isTweening:
			return

		if arg_4_0.port.IsTempPort() or arg_4_0.page == var_0_0.PageMain:
			arg_4_0.EaseOutUI(function()
				arg_4_0.closeView())
		else
			arg_4_0.SetPage(var_0_0.PageMain), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.btnOperation, function()
		arg_4_0.SetPage(var_0_0.PageTask), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.btnSupply, function()
		if nowWorld().UsePortNShop():
			arg_4_0.SetPage(var_0_0.PageNShop)
		else
			arg_4_0.SetPage(var_0_0.PageShop), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.btnDockyard, function()
		arg_4_0.emit(WorldPortMediator.OnOpenBay), SFX_PANEL)
	arg_4_0.UpdatePainting(arg_4_0.GetPaintingInfo())
	arg_4_0.UpdateTaskTip()
	arg_4_0.UpdateCDTip()
	arg_4_0.UpdateNShopTip()

	if arg_4_0.port.IsTempPort():
		arg_4_0.contextData.page = WorldPortLayer.PageShop
	elif arg_4_0.contextData.page == WorldPortLayer.PageDockyard:
		arg_4_0.contextData.page = None

	arg_4_0.SetPage(arg_4_0.contextData.page or WorldPortLayer.PageMain)
	arg_4_0.EaseInUI()

def var_0_0.onBackPressed(arg_10_0):
	triggerButton(arg_10_0.btnBack)

def var_0_0.willExit(arg_11_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_11_0._tf)
	arg_11_0.RecyclePainting(arg_11_0.rtPainting)
	arg_11_0.singleWindow.Destroy()
	arg_11_0.multiWindow.Destroy()

	arg_11_0.contextData.isEnter = True

	if var_0_0.BlurPages[arg_11_0.page]:
		pg.UIMgr.GetInstance().UnblurPanel(arg_11_0.rtBlurPanel, arg_11_0._tf)

	arg_11_0.CancelUITween()
	arg_11_0.DisposeTopUI()
	arg_11_0.DisposeTasks()
	arg_11_0.DisposeGoods()
	arg_11_0.atlas.RemoveListener(WorldAtlas.EventUpdateNGoodsCount, arg_11_0.onUpdateNGoods)

	arg_11_0.atlas = None

	arg_11_0.port.RemoveListener(WorldMapPort.EventUpdateTaskIds, arg_11_0.onUpdateTasks)
	arg_11_0.port.RemoveListener(WorldMapPort.EventUpdateGoods, arg_11_0.onUpdateGoods)

	arg_11_0.port = None

	arg_11_0.resPanel.exit()

	arg_11_0.resPanel = None

	arg_11_0.refreshTimer.Stop()

	arg_11_0.refreshTimer = None

	arg_11_0.inventory.RemoveListener(WorldInventoryProxy.EventUpdateItem, arg_11_0.onUpdateMoneyCount)

	arg_11_0.inventory = None

	arg_11_0.taskProxy.RemoveListener(WorldTaskProxy.EventUpdateTask, arg_11_0.onUpdateTasks)

	arg_11_0.taskProxy = None

	arg_11_0.wsWorldInfo.Dispose()

	arg_11_0.wsWorldInfo = None

def var_0_0.GetPaintingInfo(arg_12_0):
	if arg_12_0.port.IsTempPort():
		return "mingshi", False
	else
		return "tbniang", True

def var_0_0.UpdatePainting(arg_13_0, arg_13_1, arg_13_2):
	arg_13_0.paintingName = arg_13_1

	setPaintingPrefab(arg_13_0.rtPainting, arg_13_1, "chuanwu")

	if arg_13_2:
		arg_13_0.AddGlitchArtEffectForPating(arg_13_0.rtPainting)

def var_0_0.AddGlitchArtEffectForPating(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_1.GetComponentsInChildren(typeof(Image))

	for iter_14_0 = 0, var_14_0.Length - 1:
		var_14_0[iter_14_0].material = arg_14_0.glitchArtMaterial

def var_0_0.RecyclePainting(arg_15_0, arg_15_1):
	if arg_15_1.Find("fitter").childCount > 0:
		local var_15_0 = arg_15_1.GetComponentsInChildren(typeof(Image))

		for iter_15_0 = 0, var_15_0.Length - 1:
			local var_15_1 = var_15_0[iter_15_0]
			local var_15_2 = Color.white

			if var_15_1.material != var_15_1.defaultGraphicMaterial:
				var_15_1.material = var_15_1.defaultGraphicMaterial

				var_15_1.material.SetColor("_Color", var_15_2)

		setGray(arg_15_1, False, True)

		local var_15_3 = arg_15_1.Find("fitter").GetChild(0)

		retPaintingPrefab(arg_15_1, var_15_3.name)

		local var_15_4 = var_15_3.Find("temp_mask")

		if var_15_4:
			Destroy(var_15_4)

def var_0_0.DisplayTopUI(arg_16_0, arg_16_1):
	setActive(arg_16_0.rtImageTitle, arg_16_1 == var_0_0.PageMain)
	setActive(arg_16_0.rtImageTitleTask, arg_16_1 == var_0_0.PageTask)
	setActive(arg_16_0.rtImageTitleShop, arg_16_1 == var_0_0.PageShop or arg_16_1 == var_0_0.PageNShop)
	setActive(arg_16_0.rtTopLeft, arg_16_1 != var_0_0.PageNShop)
	setActive(arg_16_0.rtTopRight, arg_16_1 == var_0_0.PageMain)
	setActive(arg_16_0.rtTopBottom, arg_16_1 == var_0_0.PageMain)
	setActive(arg_16_0.rtBg, arg_16_1 != var_0_0.PageNShop)
	setActive(arg_16_0.rtBgNShop, arg_16_1 == var_0_0.PageNShop)

def var_0_0.DisposeTopUI(arg_17_0):
	arg_17_0.wsPortLeft.Dispose()

def var_0_0.NewPortLeft(arg_18_0):
	local var_18_0 = WSPortLeft.New()

	var_18_0.transform = arg_18_0.rtTopLeft

	var_18_0.Setup()
	var_18_0.UpdateMap(nowWorld().GetActiveMap())

	return var_18_0

def var_0_0.EnterPortAnim(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_0.rtEnterIcon.GetComponent(typeof(DftAniEvent))

	if var_19_0:
		var_19_0.SetTriggerEvent(function(arg_20_0)
			arg_19_1())
		var_19_0.SetEndEvent(function(arg_21_0)
			setActive(arg_19_0.rtEnterIcon, False))

	setActive(arg_19_0.rtEnterIcon, True)

def var_0_0.EaseInUI(arg_22_0, arg_22_1):
	arg_22_0.isTweening = True

	local var_22_0 = {}

	arg_22_0.CancelUITween()

	if #arg_22_0.enterIcon > 0 and not arg_22_0.contextData.isEnter:
		table.insert(var_22_0, function(arg_23_0)
			setActive(arg_22_0.rtTop, False)
			arg_22_0.EnterPortAnim(function()
				setActive(arg_22_0.rtTop, True)

				return arg_23_0()))
	else
		setActive(arg_22_0.rtEnterIcon, False)

	seriesAsync(var_22_0, function()
		setAnchoredPosition(arg_22_0.rtTopLeft, {
			x = -arg_22_0.rtTopLeft.rect.width
		})
		setAnchoredPosition(arg_22_0.rtTopRight, {
			x = arg_22_0.rtTopRight.rect.width
		})
		setAnchoredPosition(arg_22_0.rtTopTitle, {
			y = arg_22_0.rtTopTitle.rect.height
		})
		setAnchoredPosition(arg_22_0.rtTopBottom, {
			y = -arg_22_0.rtTopRight.rect.height
		})
		LeanTween.moveX(arg_22_0.rtTopLeft, 0, WorldConst.UIEaseDuration).setEase(LeanTweenType.easeOutSine)
		LeanTween.moveX(arg_22_0.rtTopRight, 0, WorldConst.UIEaseDuration).setEase(LeanTweenType.easeOutSine)
		LeanTween.moveY(arg_22_0.rtTopTitle, 0, WorldConst.UIEaseDuration).setEase(LeanTweenType.easeOutSine)
		LeanTween.moveY(arg_22_0.rtTopBottom, 0, WorldConst.UIEaseDuration).setEase(LeanTweenType.easeOutSine).setOnComplete(System.Action(function()
			arg_22_0.isTweening = False

			return existCall(arg_22_1))))

def var_0_0.EaseOutUI(arg_27_0, arg_27_1):
	arg_27_0.CancelUITween()
	LeanTween.moveX(arg_27_0.rtTopLeft, -arg_27_0.rtTopLeft.rect.width, WorldConst.UIEaseDuration).setEase(LeanTweenType.easeOutSine)
	LeanTween.moveX(arg_27_0.rtTopRight, arg_27_0.rtTopRight.rect.width, WorldConst.UIEaseDuration).setEase(LeanTweenType.easeOutSine)
	LeanTween.moveY(arg_27_0.rtTopTitle, arg_27_0.rtTopTitle.rect.height, WorldConst.UIEaseDuration).setEase(LeanTweenType.easeOutSine)
	LeanTween.moveY(arg_27_0.rtTopBottom, -arg_27_0.rtTopRight.rect.height, WorldConst.UIEaseDuration).setEase(LeanTweenType.easeOutSine).setOnComplete(System.Action(function()
		arg_27_0.isTweening = False

		return existCall(arg_27_1)))

def var_0_0.CancelUITween(arg_29_0):
	LeanTween.cancel(go(arg_29_0.rtTopTitle))
	LeanTween.cancel(go(arg_29_0.rtTopLeft))
	LeanTween.cancel(go(arg_29_0.rtTopRight))
	LeanTween.cancel(go(arg_29_0.rtTopBottom))

def var_0_0.SetPlayer(arg_30_0, arg_30_1):
	arg_30_0.player = arg_30_1

	arg_30_0.resPanel.setPlayer(arg_30_1)

def var_0_0.SetAtlas(arg_31_0, arg_31_1):
	arg_31_0.atlas = arg_31_1

	arg_31_0.atlas.AddListener(WorldAtlas.EventUpdateNGoodsCount, arg_31_0.onUpdateNGoods)

	arg_31_0.nGoodsDic = {}
	arg_31_0.nGoodsPortDic = {}

	for iter_31_0, iter_31_1 in pairs(arg_31_1.nShopGoodsDic):
		arg_31_0.nGoodsDic[iter_31_0] = Goods.Create({
			id = iter_31_0,
			count = iter_31_1
		}, Goods.TYPE_WORLD_NSHOP)

		local var_31_0 = arg_31_0.nGoodsDic[iter_31_0].getConfig("port_id")

		arg_31_0.nGoodsPortDic[var_31_0] = arg_31_0.nGoodsPortDic[var_31_0] or {}

		table.insert(arg_31_0.nGoodsPortDic[var_31_0], arg_31_0.nGoodsDic[iter_31_0])

	for iter_31_2, iter_31_3 in pairs(arg_31_0.nGoodsPortDic):
		table.sort(iter_31_3, CompareFuncs({
			function(arg_32_0)
				return -arg_32_0.getConfig("priority"),
			function(arg_33_0)
				return arg_33_0.id
		}))

def var_0_0.SetPort(arg_34_0, arg_34_1):
	local var_34_0 = nowWorld()

	arg_34_0.port = arg_34_1

	arg_34_0.port.AddListener(WorldMapPort.EventUpdateTaskIds, arg_34_0.onUpdateTasks)
	arg_34_0.port.AddListener(WorldMapPort.EventUpdateGoods, arg_34_0.onUpdateGoods)
	arg_34_0.SetBg(arg_34_0.port.id)

	arg_34_0.refreshTimer = Timer.New(function()
		if arg_34_0.port.IsValid():
			arg_34_0.UpdateRefreshTime(arg_34_0.port.expiredTime - pg.TimeMgr.GetInstance().GetServerTime())
		else
			arg_34_0.emit(WorldPortMediator.OnReqPort, var_34_0.GetActiveMap().id), 1, -1)

	arg_34_0.refreshTimer.Start()
	arg_34_0.refreshTimer.func()

	local var_34_1 = var_34_0.GetActiveMap().GetFleet()

	arg_34_0.wsPortLeft = arg_34_0.NewPortLeft()

	local var_34_2 = arg_34_0.port.GetRealm()

	setActive(arg_34_0.btnOperation, var_34_2 == 0 or var_34_2 == var_34_0.GetRealm())
	setActive(arg_34_0.btnDockyard, var_34_2 == 0 or var_34_2 == var_34_0.GetRealm())
	setActive(arg_34_0.btnSupply, arg_34_0.nGoodsPortDic[arg_34_1.id])
	setActive(arg_34_0.resPanel._tf, var_34_0.IsSystemOpen(WorldConst.SystemResource))

	arg_34_0.inventory = var_34_0.GetInventoryProxy()

	arg_34_0.inventory.AddListener(WorldInventoryProxy.EventUpdateItem, arg_34_0.onUpdateMoneyCount)
	arg_34_0.OnUpdateMoneyCount()

	arg_34_0.taskProxy = var_34_0.GetTaskProxy()

	arg_34_0.taskProxy.AddListener(WorldTaskProxy.EventUpdateTask, arg_34_0.onUpdateTasks)

def var_0_0.SetBg(arg_36_0, arg_36_1):
	arg_36_0.portBg = pg.world_port_data[arg_36_1].port_bg

	setImageAlpha(arg_36_0.rtBg, #arg_36_0.portBg > 0 and 1 or 0)

	if #arg_36_0.portBg > 0:
		GetImageSpriteFromAtlasAsync("world/port/" .. arg_36_0.portBg, "", arg_36_0.rtBg)

	arg_36_0.enterIcon = pg.world_port_data[arg_36_1].port_entrance_icon

	setActive(arg_36_0.rtEnterIcon, #arg_36_0.enterIcon > 0)

	if #arg_36_0.enterIcon > 0:
		GetImageSpriteFromAtlasAsync("world/porttitle/" .. arg_36_0.enterIcon, "", arg_36_0.rtEnterIcon, False)

	GetImageSpriteFromAtlasAsync("world/portword/" .. arg_36_0.portBg, "", arg_36_0.rtImageTitle, True)
	GetImageSpriteFromAtlasAsync("world/portword/" .. arg_36_0.portBg .. "_en", "", arg_36_0.rtImageTitle.Find("Image"), True)

def var_0_0.OnUpdateTasks(arg_37_0):
	arg_37_0.UpdateTaskTip()
	arg_37_0.SetPageDirty(var_0_0.PageTask)

	if arg_37_0.page == var_0_0.PageTask:
		arg_37_0.UpdateTasks()

def var_0_0.OnUpdateGoods(arg_38_0):
	arg_38_0.UpdateCDTip()
	arg_38_0.SetPageDirty(var_0_0.PageShop)

	if arg_38_0.page == var_0_0.PageShop:
		arg_38_0.UpdateGoods()

def var_0_0.OnUpdateNGoods(arg_39_0, arg_39_1, arg_39_2, arg_39_3, arg_39_4):
	if arg_39_0.page == var_0_0.PageNShop:
		local var_39_0 = arg_39_0.nGoodsDic[arg_39_3]

		var_39_0.buyCount = arg_39_4

		local var_39_1 = arg_39_0.rtNGoodsDic[arg_39_3]

		setText(var_39_1.Find("count_contain/count"), var_39_0.GetPurchasableCnt() .. "/" .. var_39_0.GetLimitGoodCount())
		setActive(var_39_1.Find("mask"), not var_39_0.canPurchase())
		setActive(var_39_1.Find("new"), False)
	else
		arg_39_0.SetPageDirty(var_0_0.PageNShop)

def var_0_0.SetPage(arg_40_0, arg_40_1):
	if arg_40_0.page != arg_40_1:
		if var_0_0.BlurPages[arg_40_0.page or 0] != var_0_0.BlurPages[arg_40_1]:
			if var_0_0.BlurPages[arg_40_1]:
				pg.UIMgr.GetInstance().BlurPanel(arg_40_0.rtBlurPanel, False)
			else
				pg.UIMgr.GetInstance().UnblurPanel(arg_40_0.rtBlurPanel, arg_40_0._tf)

		if arg_40_1 == var_0_0.PageShop and arg_40_0.paintingName == "buzhihuo_shop":
			arg_40_0.showRandomShipWord(pg.navalacademy_shoppingstreet_template[1].words_enter, True, "enter")

		arg_40_0.page = arg_40_1

		arg_40_0.UpdatePage()

		arg_40_0.contextData.page = arg_40_1

def var_0_0.SetPageDirty(arg_41_0, arg_41_1):
	arg_41_0.dirtyFlags[arg_41_1] = True

def var_0_0.IsPageDirty(arg_42_0, arg_42_1):
	return arg_42_0.dirtyFlags[arg_42_1] == True or arg_42_0.dirtyFlags[arg_42_1] == None

def var_0_0.UpdatePage(arg_43_0):
	local var_43_0 = arg_43_0.page

	arg_43_0.DisplayTopUI(var_43_0)
	setActive(arg_43_0.rtTasks, var_43_0 == var_0_0.PageTask)
	setActive(arg_43_0.rtShop, var_43_0 == var_0_0.PageShop)
	setActive(arg_43_0.rtNShop, var_43_0 == var_0_0.PageNShop)

	if arg_43_0.IsPageDirty(var_43_0):
		if var_43_0 == var_0_0.PageTask:
			arg_43_0.UpdateTasks()
		elif var_43_0 == var_0_0.PageShop:
			arg_43_0.UpdateGoods()
		elif var_43_0 == var_0_0.PageNShop:
			arg_43_0.UpdateNShopPorts()

def var_0_0.UpdateTasks(arg_44_0):
	arg_44_0.dirtyFlags[var_0_0.PageTask] = False

	local var_44_0 = arg_44_0.rtTasks.Find("frame/viewport/content")
	local var_44_1 = var_44_0.GetChild(0)
	local var_44_2 = _.map(arg_44_0.port.taskIds, function(arg_45_0)
		return WorldTask.New({
			id = arg_45_0
		}))

	table.sort(var_44_2, CompareFuncs(WorldTask.sortDic))
	UIItemList.StaticAlign(var_44_0, var_44_1, #var_44_2, function(arg_46_0, arg_46_1, arg_46_2)
		local var_46_0 = arg_46_1 + 1

		if arg_46_0 == UIItemList.EventUpdate:
			local var_46_1 = var_44_2[var_46_0]

			arg_44_0.wsTasks[var_46_0] = arg_44_0.wsTasks[var_46_0] or WSPortTask.New(arg_46_2)

			local var_46_2 = arg_44_0.wsTasks[var_46_0]

			var_46_2.Setup(var_46_1)
			onButton(arg_44_0, var_46_2.btnInactive, function()
				arg_44_0.emit(WorldPortMediator.OnAccepetTask, var_46_1, arg_44_0.port.id), SFX_PANEL)
			onButton(arg_44_0, var_46_2.btnOnGoing, function()
				arg_44_0.showTaskWindow(var_46_1), SFX_PANEL)
			onButton(arg_44_0, var_46_2.btnFinished, function()
				arg_44_0.emit(WorldPortMediator.OnSubmitTask, var_46_1), SFX_PANEL)

			function var_46_2.onDrop(arg_50_0)
				arg_44_0.emit(var_0_0.ON_DROP, arg_50_0))

	local var_44_3 = arg_44_0.rtTasks.Find("frame/empty")

	setActive(var_44_3, #var_44_2 == 0)

def var_0_0.DisposeTasks(arg_51_0):
	_.each(arg_51_0.wsTasks, function(arg_52_0)
		arg_52_0.Dispose())

	arg_51_0.wsTasks = {}

def var_0_0.UpdateGoods(arg_53_0):
	arg_53_0.dirtyFlags[var_0_0.PageShop] = False

	local var_53_0 = arg_53_0.rtShop.Find("frame/scrollview/view")
	local var_53_1 = var_53_0.GetChild(0)
	local var_53_2 = underscore.rest(arg_53_0.port.goods, 1)

	table.sort(var_53_2, CompareFuncs({
		function(arg_54_0)
			return -arg_54_0.config.priority,
		function(arg_55_0)
			return arg_55_0.id
	}))
	UIItemList.StaticAlign(var_53_0, var_53_1, #var_53_2, function(arg_56_0, arg_56_1, arg_56_2)
		arg_56_1 = arg_56_1 + 1

		if arg_56_0 == UIItemList.EventUpdate:
			local var_56_0 = var_53_2[arg_56_1]

			arg_53_0.wsGoods[arg_56_1] = arg_53_0.wsGoods[arg_56_1] or WSPortGoods.New(arg_56_2)

			local var_56_1 = arg_53_0.wsGoods[arg_56_1]

			var_56_1.Setup(var_56_0)
			onButton(arg_53_0, var_56_1.transform, function()
				if var_56_0.count > 0:
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						yesText = "text_buy",
						type = MSGBOX_TYPE_SINGLE_ITEM,
						drop = var_56_0.item,
						def onYes:()
							arg_53_0.emit(WorldPortMediator.OnBuyGoods, var_56_0)
					}), SFX_PANEL))

def var_0_0.DisposeGoods(arg_59_0):
	_.each(arg_59_0.wsGoods, function(arg_60_0)
		arg_60_0.Dispose())

	arg_59_0.wsGoods = {}

def var_0_0.UpdateNShopPorts(arg_61_0):
	arg_61_0.dirtyFlags[var_0_0.PageNShop] = False

	local var_61_0 = underscore.keys(arg_61_0.nGoodsPortDic)

	table.sort(var_61_0)

	for iter_61_0, iter_61_1 in ipairs(var_61_0):
		if not arg_61_0.poolTplPort[iter_61_0]:
			table.insert(arg_61_0.poolTplPort, cloneTplTo(arg_61_0.tplPort, arg_61_0.containerPort))

		local var_61_1 = arg_61_0.poolTplPort[iter_61_0]

		setText(var_61_1.Find("Text"), pg.world_port_data[iter_61_1].name)
		setActive(var_61_1.Find("tip"), arg_61_0.atlas.markPortDic.newGoods[iter_61_1])
		onToggle(arg_61_0, var_61_1, function(arg_62_0)
			if arg_62_0:
				if arg_61_0.nShopPortId == iter_61_1:
					return

				setActive(var_61_1.Find("tip"), False)
				arg_61_0.atlas.UpdatePortMarkNShop(iter_61_1, False)
				arg_61_0.UpdateNShopTip()
				arg_61_0.UpdateNShopGoods(iter_61_1), SFX_PANEL)
		triggerToggle(var_61_1, iter_61_1 == arg_61_0.port.id)

def var_0_0.UpdateNShopGoods(arg_63_0, arg_63_1):
	arg_63_0.nShopPortId = arg_63_1

	local var_63_0 = arg_63_0.atlas.GetPressingUnlockCount()
	local var_63_1 = arg_63_0.atlas.GetPressingUnlockRecordCount(arg_63_1)
	local var_63_2 = {}

	for iter_63_0, iter_63_1 in ipairs(arg_63_0.nGoodsPortDic[arg_63_1]):
		local var_63_3 = iter_63_1.getConfig("unlock_num")

		var_63_2[var_63_3] = var_63_2[var_63_3] or {}

		table.insert(var_63_2[var_63_3], iter_63_1)

	arg_63_0.rtNGoodsDic = {}

	local var_63_4 = underscore.keys(var_63_2)

	table.sort(var_63_4)
	UIItemList.StaticAlign(arg_63_0.rtNGoodsContainer, arg_63_0.rtNGoodsContainer.Find("group"), #var_63_4, function(arg_64_0, arg_64_1, arg_64_2)
		arg_64_1 = arg_64_1 + 1

		if arg_64_0 == UIItemList.EventUpdate:
			local var_64_0 = var_63_4[arg_64_1]

			setActive(arg_64_2.Find("title"), arg_64_1 > 1)
			setText(arg_64_2.Find("title/other/Text"), i18n("world_instruction_port_goods_locked"))
			setText(arg_64_2.Find("title/other/progress"), math.min(var_63_0, var_64_0) .. "/" .. var_64_0)

			local var_64_1 = arg_64_2.Find("container")

			UIItemList.StaticAlign(var_64_1, var_64_1.Find("item_tpl"), #var_63_2[var_64_0], function(arg_65_0, arg_65_1, arg_65_2)
				arg_65_1 = arg_65_1 + 1

				if arg_65_0 == UIItemList.EventUpdate:
					local var_65_0 = var_63_2[var_64_0][arg_65_1]

					arg_63_0.rtNGoodsDic[var_65_0.id] = arg_65_2

					local var_65_1 = var_65_0.GetDropInfo()

					updateDrop(arg_65_2.Find("IconTpl"), var_65_1)
					setText(arg_65_2.Find("name_mask/name"), shortenString(var_65_1.getConfig("name"), 6))

					local var_65_2 = var_65_0.GetPriceInfo()

					GetImageSpriteFromAtlasAsync(var_65_2.getIcon(), "", arg_65_2.Find("consume/contain/icon"), False)
					setText(arg_65_2.Find("consume/contain/Text"), var_65_2.count)
					setText(arg_65_2.Find("count_contain/count"), var_65_0.GetPurchasableCnt() .. "/" .. var_65_0.GetLimitGoodCount())
					setText(arg_65_2.Find("count_contain/label"), i18n("activity_shop_exchange_count"))
					setText(arg_65_2.Find("mask/tag/sellout_tag"), i18n("word_sell_out"))
					setActive(arg_65_2.Find("mask"), not var_65_0.canPurchase())
					setText(arg_65_2.Find("lock/Image/Text"), i18n("word_sell_lock"))
					setActive(arg_65_2.Find("lock"), var_63_0 < var_64_0)
					setActive(arg_65_2.Find("new"), var_65_0.buyCount == 0 and var_63_1 < var_64_0 and var_64_0 <= var_63_0)
					onButton(arg_63_0, arg_65_2, function()
						(var_65_0.GetLimitGoodCount() > 1 and arg_63_0.multiWindow or arg_63_0.singleWindow).ExecuteAction("Open", var_65_0, function(arg_67_0, arg_67_1)
							arg_63_0.emit(WorldPortMediator.OnBuyNShopGoods, arg_67_0, arg_67_1)), SFX_PANEL)))
	arg_63_0.atlas.SetPressingUnlockRecordCount(arg_63_1, var_63_0)

def var_0_0.OnUpdateMoneyCount(arg_68_0, arg_68_1, arg_68_2, arg_68_3):
	if not arg_68_1 or arg_68_3.id == WorldItem.PortMoneyId:
		local var_68_0 = arg_68_0.inventory.GetItemCount(WorldItem.PortMoneyId)

		setText(arg_68_0.rtShop.Find("quick_count/value"), var_68_0)
		setText(arg_68_0.rtNShopRes.Find("Text"), var_68_0)

def var_0_0.UpdateRefreshTime(arg_69_0, arg_69_1):
	setText(arg_69_0.cdTF.Find("Text"), pg.TimeMgr.GetInstance().DescCDTime(arg_69_1))

def var_0_0.UpdateCDTip(arg_70_0):
	setActive(arg_70_0.cdTF, #arg_70_0.port.goods > 0 and not arg_70_0.port.IsTempPort())
	setActive(arg_70_0.emptyTF, #arg_70_0.port.goods == 0)

	if not nowWorld().UsePortNShop():
		setActive(arg_70_0.btnSupply.Find("new"), nowWorld().GetAtlas().markPortDic.goods[arg_70_0.port.id])

def var_0_0.UpdateTaskTip(arg_71_0):
	setActive(arg_71_0.btnOperation.Find("new"), False)

def var_0_0.UpdateNShopTip(arg_72_0):
	if nowWorld().UsePortNShop():
		setActive(arg_72_0.btnSupply.Find("new"), arg_72_0.atlas.GetAnyPortMarkNShop())

def var_0_0.showTaskWindow(arg_73_0, arg_73_1):
	local var_73_0 = arg_73_1.config.rare_task_icon
	local var_73_1 = arg_73_0.rtTaskWindow.Find("main_window/left_panel")

	setActive(var_73_1.Find("bg"), arg_73_1.IsSpecialType())

	if #var_73_0 > 0:
		GetImageSpriteFromAtlasAsync("shipyardicon/" .. var_73_0, "", var_73_1.Find("card"), True)
	else
		GetImageSpriteFromAtlasAsync("ui/worldportui_atlas", "nobody", var_73_1.Find("card"), True)

	local var_73_2 = arg_73_0.rtTaskWindow.Find("main_window/right_panel")

	setText(var_73_2.Find("title/Text"), arg_73_1.config.name)
	setText(var_73_2.Find("content/desc"), arg_73_1.config.rare_task_text)
	setText(var_73_2.Find("content/slider_progress/Text"), arg_73_1.getProgress() .. "/" .. arg_73_1.getMaxProgress())
	setSlider(var_73_2.Find("content/slider"), 0, arg_73_1.getMaxProgress(), arg_73_1.getProgress())

	local var_73_3 = var_73_2.Find("content/item_tpl")
	local var_73_4 = var_73_2.Find("content/award_bg/panel/content")
	local var_73_5 = arg_73_1.config.show

	removeAllChildren(var_73_4)

	for iter_73_0, iter_73_1 in ipairs(var_73_5):
		local var_73_6 = cloneTplTo(var_73_3, var_73_4)
		local var_73_7 = {
			type = iter_73_1[1],
			id = iter_73_1[2],
			count = iter_73_1[3]
		}

		updateDrop(var_73_6, var_73_7)
		onButton(arg_73_0, var_73_6, function()
			arg_73_0.emit(var_0_0.ON_DROP, var_73_7), SFX_PANEL)
		setActive(var_73_6, True)

	setActive(var_73_3, False)
	setActive(var_73_2.Find("content/award_bg/arror"), #var_73_5 > 3)
	onButton(arg_73_0, var_73_2.Find("btn_close"), function()
		arg_73_0.hideTaskWindow(), SFX_CANCEL)
	onButton(arg_73_0, arg_73_0.rtTaskWindow.Find("bg"), function()
		arg_73_0.hideTaskWindow(), SFX_CANCEL)
	onButton(arg_73_0, var_73_2.Find("btn_go"), function()
		arg_73_0.hideTaskWindow()
		arg_73_0.emit(WorldPortMediator.OnTaskGoto, arg_73_1.id), SFX_PANEL)
	setButtonEnabled(var_73_2.Find("btn_go"), arg_73_1.GetFollowingAreaId() or arg_73_1.GetFollowingEntrance())
	setActive(arg_73_0.rtTaskWindow, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_73_0.rtTaskWindow, arg_73_0._tf)

def var_0_0.hideTaskWindow(arg_78_0):
	setActive(arg_78_0.rtTaskWindow, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_78_0.rtTaskWindow, arg_78_0._tf)

return var_0_0
