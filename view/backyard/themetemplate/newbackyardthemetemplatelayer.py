local var_0_0 = class("NewBackYardThemeTemplateLayer", import("...base.BaseUI"))

local function var_0_1(arg_1_0, arg_1_1, arg_1_2)
	local function var_1_0(arg_2_0, arg_2_1)
		setActive(arg_2_0.Find("sel"), arg_2_1)
		setActive(arg_2_0.Find("unsel"), not arg_2_1)

	onButton(arg_1_0, arg_1_1, function()
		if not arg_1_2():
			return

		if arg_1_0.btn:
			var_1_0(arg_1_0.btn, False)

		var_1_0(arg_1_1, True)

		arg_1_0.btn = arg_1_1, SFX_PANEL)
	var_1_0(arg_1_1, False)

def var_0_0.forceGC(arg_4_0):
	return True

def var_0_0.getUIName(arg_5_0):
	return "NewBackYardTemplateUI"

def var_0_0.preload(arg_6_0, arg_6_1):
	_backYardThemeTemplateMsgbox = BackyardMsgBoxMgr.New()

	_backYardThemeTemplateMsgbox.Init(arg_6_0, arg_6_1)

def var_0_0.init(arg_7_0):
	arg_7_0.tpl = arg_7_0.findTF("adpter/tag/list/tpl")
	arg_7_0.container = arg_7_0.findTF("adpter/tag/list")
	arg_7_0.pageContainer = arg_7_0.findTF("pages")
	arg_7_0.backBtn = arg_7_0.findTF("adpter/top/fanhui")
	arg_7_0.homeBtn = arg_7_0.findTF("adpter/top/help")
	arg_7_0.goldTxt = arg_7_0.findTF("adpter/top/res_gold/Text").GetComponent(typeof(Text))
	arg_7_0.gemTxt = arg_7_0.findTF("adpter/top/res_gem/Text").GetComponent(typeof(Text))
	arg_7_0.gemAddBtn = arg_7_0.findTF("adpter/top/res_gem/jiahao")
	arg_7_0.goldAddBtn = arg_7_0.findTF("adpter/top/res_gold/jiahao")
	arg_7_0.tags = {
		[BackYardConst.THEME_TEMPLATE_TYPE_SHOP] = i18n("backyard_theme_shop_title"),
		[BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM] = i18n("backyard_theme_mine_title"),
		[BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION] = i18n("backyard_theme_collection_title")
	}
	arg_7_0.listPage = BackYardThemeTemplateListPage.New(arg_7_0.pageContainer, arg_7_0.event, arg_7_0.contextData)
	arg_7_0.contextData.msgBox = BackYardThemeTemplateMsgBox.New(arg_7_0._tf, arg_7_0.event, arg_7_0.contextData)

def var_0_0.SetShopThemeTemplate(arg_8_0, arg_8_1):
	arg_8_0.shopThemeTemplate = arg_8_1

def var_0_0.ShopThemeTemplateUpdate(arg_9_0, arg_9_1):
	for iter_9_0, iter_9_1 in pairs(arg_9_0.shopThemeTemplate):
		if iter_9_1.id == arg_9_1.id:
			arg_9_0.shopThemeTemplate[iter_9_0] = arg_9_1

			break

	if arg_9_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		arg_9_0.listPage.ExecuteAction("ThemeTemplateUpdate", arg_9_1)

def var_0_0.OnShopTemplatesUpdated(arg_10_0, arg_10_1):
	arg_10_0.SetShopThemeTemplate(arg_10_1)

	if arg_10_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		local var_10_0 = arg_10_0.GetDataForType(arg_10_0.pageType)

		arg_10_0.listPage.ExecuteAction("ThemeTemplatesUpdate", var_10_0)

def var_0_0.OnShopTemplatesErro(arg_11_0):
	if arg_11_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		local var_11_0 = arg_11_0.GetDataForType(arg_11_0.pageType)

		arg_11_0.listPage.ExecuteAction("ThemeTemplatesErro", var_11_0)

def var_0_0.SetCustomThemeTemplate(arg_12_0, arg_12_1):
	arg_12_0.customThemeTemplate = arg_12_1

def var_0_0.CustomThemeTemplateUpdate(arg_13_0, arg_13_1):
	for iter_13_0, iter_13_1 in pairs(arg_13_0.customThemeTemplate):
		if iter_13_1.id == arg_13_1.id:
			arg_13_0.customThemeTemplate[iter_13_0] = arg_13_1

			break

	if arg_13_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM:
		arg_13_0.listPage.ExecuteAction("ThemeTemplateUpdate", arg_13_1)

def var_0_0.SetCollectionThemeTemplate(arg_14_0, arg_14_1):
	arg_14_0.collectionThemeTemplate = arg_14_1

def var_0_0.CollectionThemeTemplateUpdate(arg_15_0, arg_15_1):
	for iter_15_0, iter_15_1 in pairs(arg_15_0.collectionThemeTemplate):
		if iter_15_1.id == arg_15_1.id:
			arg_15_0.collectionThemeTemplate[iter_15_0] = arg_15_1

			break

	if arg_15_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION:
		arg_15_0.listPage.ExecuteAction("ThemeTemplateUpdate", arg_15_1)

def var_0_0.SetDorm(arg_16_0, arg_16_1):
	arg_16_0.dorm = arg_16_1

def var_0_0.UpdateDorm(arg_17_0, arg_17_1):
	arg_17_0.SetDorm(arg_17_1)

	if arg_17_0.pageType:
		arg_17_0.listPage.ExecuteAction("UpdateDorm", arg_17_1)

def var_0_0.SetPlayer(arg_18_0, arg_18_1):
	arg_18_0.player = arg_18_1

def var_0_0.PlayerUpdated(arg_19_0, arg_19_1):
	arg_19_0.SetPlayer(arg_19_1)
	arg_19_0.UpdateRes()

	if arg_19_0.pageType:
		arg_19_0.listPage.ExecuteAction("PlayerUpdated", arg_19_1)

def var_0_0.FurnituresUpdated(arg_20_0, arg_20_1):
	if arg_20_0.pageType:
		arg_20_0.listPage.ExecuteAction("FurnituresUpdated", arg_20_1)

def var_0_0.SearchKeyChange(arg_21_0, arg_21_1):
	if arg_21_0.pageType and (arg_21_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM or arg_21_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION):
		arg_21_0.listPage.ExecuteAction("SearchKeyChange", arg_21_1)

def var_0_0.ShopSearchKeyChange(arg_22_0, arg_22_1):
	if arg_22_0.pageType and arg_22_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		arg_22_0.listPage.ExecuteAction("ShopSearchKeyChange", arg_22_1)

def var_0_0.ClearShopSearchKey(arg_23_0):
	if arg_23_0.pageType and arg_23_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		arg_23_0.listPage.ExecuteAction("ClearShopSearchKey")

def var_0_0.DeleteCustomThemeTemplate(arg_24_0, arg_24_1):
	if not arg_24_0.customThemeTemplate:
		return

	for iter_24_0, iter_24_1 in pairs(arg_24_0.customThemeTemplate):
		if iter_24_1.id == arg_24_1:
			arg_24_0.customThemeTemplate[iter_24_0] = None

			break

	if arg_24_0.pageType and arg_24_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM:
		arg_24_0.listPage.ExecuteAction("DeleteCustomThemeTemplate", arg_24_1)

def var_0_0.DeleteCollectionThemeTemplate(arg_25_0, arg_25_1):
	if not arg_25_0.collectionThemeTemplate:
		return

	for iter_25_0, iter_25_1 in pairs(arg_25_0.collectionThemeTemplate):
		if iter_25_1.id == arg_25_1:
			arg_25_0.collectionThemeTemplate[iter_25_0] = None

			break

	if arg_25_0.pageType and arg_25_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION:
		arg_25_0.listPage.ExecuteAction("DeleteCollectionThemeTemplate", arg_25_1)

def var_0_0.DeleteShopThemeTemplate(arg_26_0, arg_26_1):
	if not arg_26_0.shopThemeTemplate:
		return

	for iter_26_0, iter_26_1 in pairs(arg_26_0.shopThemeTemplate):
		if iter_26_1.id == arg_26_1:
			arg_26_0.shopThemeTemplate[iter_26_0] = None

			break

	if arg_26_0.pageType and arg_26_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		arg_26_0.listPage.ExecuteAction("DeleteShopThemeTemplate", arg_26_1)

def var_0_0.AddCollectionThemeTemplate(arg_27_0, arg_27_1):
	arg_27_0.collectionThemeTemplate[arg_27_1.id] = arg_27_1

	if arg_27_0.pageType and arg_27_0.pageType == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION:
		arg_27_0.listPage.ExecuteAction("AddCollectionThemeTemplate", arg_27_1.id)

def var_0_0.didEnter(arg_28_0):
	onButton(arg_28_0, arg_28_0.backBtn, function()
		arg_28_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_28_0, arg_28_0.homeBtn, function()
		arg_28_0.emit(var_0_0.ON_HOME), SFX_PANEL)
	onButton(arg_28_0, arg_28_0.gemAddBtn, function()
		arg_28_0.emit(NewBackYardThemeTemplateMediator.ON_CHARGE, PlayerConst.ResDiamond), SFX_PANEL)
	onButton(arg_28_0, arg_28_0.goldAddBtn, function()
		arg_28_0.emit(NewBackYardThemeTemplateMediator.ON_CHARGE, PlayerConst.ResDormMoney), SFX_PANEL)
	seriesAsync({
		function(arg_33_0)
			arg_28_0.emit(NewBackYardThemeTemplateMediator.FETCH_ALL_THEME, arg_33_0)
	}, function()
		arg_28_0.InitPages()
		arg_28_0.UpdateRes()
		arg_28_0.ActiveDefaultPage())

def var_0_0.InitPages(arg_35_0):
	arg_35_0.btns = {}

	for iter_35_0, iter_35_1 in pairs(arg_35_0.tags):
		local var_35_0 = cloneTplTo(arg_35_0.tpl, arg_35_0.container)
		local var_35_1 = var_35_0.Find("unsel").GetComponent(typeof(Image))

		var_35_1.sprite = GetSpriteFromAtlas("ui/NewBackYardShopUI_atlas", "text_tp_" .. iter_35_0)

		var_35_1.SetNativeSize()

		local var_35_2 = var_35_0.Find("sel/Text").GetComponent(typeof(Image))

		var_35_2.sprite = GetSpriteFromAtlas("ui/NewBackYardShopUI_atlas", "text_tp_" .. iter_35_0)

		var_35_2.SetNativeSize()
		setActive(var_35_0.Find("line"), iter_35_0 != BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION)
		var_0_1(arg_35_0, var_35_0, function()
			local var_36_0 = arg_35_0.GetDataForType(iter_35_0)

			arg_35_0.listPage.ExecuteAction("SetUp", iter_35_0, var_36_0, arg_35_0.dorm, arg_35_0.player)

			arg_35_0.pageType = iter_35_0

			return True)

		arg_35_0.btns[iter_35_0] = var_35_0

	setActive(arg_35_0.tpl, False)

def var_0_0.ActiveDefaultPage(arg_37_0):
	local var_37_0 = arg_37_0.contextData.page or BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM

	triggerButton(arg_37_0.btns[var_37_0])

def var_0_0.GetDataForType(arg_38_0, arg_38_1):
	if arg_38_1 == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		local var_38_0 = {}

		for iter_38_0, iter_38_1 in pairs(arg_38_0.shopThemeTemplate):
			table.insert(var_38_0, iter_38_1)

		return var_38_0 or {}
	elif arg_38_1 == BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM:
		local var_38_1 = {}

		for iter_38_2, iter_38_3 in pairs(arg_38_0.customThemeTemplate):
			if iter_38_3.CanDispaly():
				table.insert(var_38_1, iter_38_3)

		return var_38_1
	elif arg_38_1 == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION:
		local var_38_2 = {}

		for iter_38_4, iter_38_5 in pairs(arg_38_0.collectionThemeTemplate):
			table.insert(var_38_2, iter_38_5)

		return var_38_2 or {}

	assert(False)

def var_0_0.UpdateRes(arg_39_0):
	arg_39_0.goldTxt.text = arg_39_0.player.getResource(PlayerConst.ResDormMoney)
	arg_39_0.gemTxt.text = arg_39_0.player.getTotalGem()

def var_0_0.willExit(arg_40_0):
	_backYardThemeTemplateMsgbox.Destroy()

	_backYardThemeTemplateMsgbox = None

	arg_40_0.listPage.Destroy()
	arg_40_0.contextData.msgBox.Destroy()
	BackYardThemeTempalteUtil.ClearAllCache()

return var_0_0
