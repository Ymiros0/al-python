local var_0_0 = class("BackYardDecrationLayer", import("...base.BaseUI"))

var_0_0.INNER_SELECTED_FURNITRUE = "BackYardDecrationLayer.INNER_SELECTED_FURNITRUE"

local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5 = 5
local var_0_6 = 6
local var_0_7 = 7
local var_0_8 = 8
local var_0_9 = 9

def var_0_0.getUIName(arg_1_0):
	return "BackYardDecorationUI"

def var_0_0.init(arg_2_0):
	arg_2_0.animation = arg_2_0._tf.GetComponent(typeof(Animation))
	arg_2_0.dftAniEvent = arg_2_0._tf.GetComponent(typeof(DftAniEvent))
	arg_2_0.adpter = arg_2_0.findTF("adpter")
	arg_2_0.pageConainer = arg_2_0.findTF("adpter/bottom/animroot/root/pages")
	arg_2_0.bAnimtion = arg_2_0.findTF("adpter/bottom").GetComponent(typeof(Animation))
	arg_2_0.shopBtn = arg_2_0.findTF("adpter/shop_btn")
	arg_2_0.saveBtn = arg_2_0.findTF("adpter/bottom/animroot/save_btn")
	arg_2_0.clearBtn = arg_2_0.findTF("adpter/bottom/animroot/clear_btn")
	arg_2_0.bottomTr = arg_2_0.findTF("adpter/bottom")
	arg_2_0.orderBtn = arg_2_0.findTF("adpter/bottom/animroot/root/fliter_container/order")
	arg_2_0.orderBtnTxt = arg_2_0.orderBtn.Find("Text").GetComponent(typeof(Image))
	arg_2_0.orderBtnIcon = arg_2_0.orderBtn.Find("icon")
	arg_2_0.filterBtn = arg_2_0.findTF("adpter/bottom/animroot/root/fliter_container/filter")
	arg_2_0.filterBtnTxt = arg_2_0.filterBtn.Find("Text").GetComponent(typeof(Image))
	arg_2_0.filterBtnTxt.sprite = GetSpriteFromAtlas("ui/NewBackYardDecorateUI_atlas", "text_default")

	arg_2_0.filterBtnTxt.SetNativeSize()

	arg_2_0.searchInput = arg_2_0.findTF("adpter/bottom/animroot/root/fliter_container/search/search")

	setText(arg_2_0.searchInput.Find("holder"), i18n("courtyard_label_search_holder"))

	arg_2_0.searchClear = arg_2_0.findTF("adpter/bottom/animroot/root/fliter_container/search/search/clear")
	arg_2_0.hideBtn = arg_2_0.findTF("adpter/bottom/animroot/root/fliter_container/hide")
	arg_2_0.showBtn = arg_2_0.findTF("adpter/bottom/animroot/show_btn")
	arg_2_0.showPutListBtn = arg_2_0.findTF("adpter/putlist_btn")
	arg_2_0.themePage = BackYardDecorationThemePage.New(arg_2_0.pageConainer, arg_2_0.event, arg_2_0.contextData)
	arg_2_0.furniturePage = BackYardDecorationFurniturePage.New(arg_2_0.pageConainer, arg_2_0.event, arg_2_0.contextData)
	arg_2_0.putListPage = BackYardDecorationPutlistPage.New(arg_2_0.adpter, arg_2_0.event, arg_2_0.contextData)

	function arg_2_0.putListPage.OnShow(arg_3_0)
		setActive(arg_2_0.showPutListBtn, not arg_3_0)

	function arg_2_0.putListPage.OnShowImmediately()
		setActive(arg_2_0.showPutListBtn, False)

	arg_2_0.contextData.furnitureDescMsgBox = BackYardDecorationDecBox.New(arg_2_0._tf, arg_2_0.event, arg_2_0.contextData)
	arg_2_0.contextData.filterPanel = BackYardDecorationFilterPanel.New(arg_2_0._tf, arg_2_0.event, arg_2_0.contextData)
	arg_2_0.pages = {
		[var_0_1] = arg_2_0.themePage,
		[var_0_2] = arg_2_0.furniturePage,
		[var_0_3] = arg_2_0.furniturePage,
		[var_0_4] = arg_2_0.furniturePage,
		[var_0_5] = arg_2_0.furniturePage,
		[var_0_6] = arg_2_0.furniturePage,
		[var_0_7] = arg_2_0.furniturePage,
		[var_0_8] = arg_2_0.furniturePage,
		[var_0_9] = arg_2_0.furniturePage
	}
	arg_2_0.themeTag = arg_2_0.findTF("adpter/bottom/animroot/root/theme")

	setText(arg_2_0.shopBtn.Find("Text"), i18n("courtyard_label_shop_1"))
	setText(arg_2_0.showPutListBtn.Find("Text"), i18n("courtyard_label_placed_furniture"))
	setText(arg_2_0.saveBtn.Find("Text"), i18n("courtyard_label_save"))
	setText(arg_2_0.clearBtn.Find("Text"), i18n("courtyard_label_clear"))

def var_0_0.didEnter(arg_5_0):
	arg_5_0.orderMode = BackYardDecorationFilterPanel.ORDER_MODE_DASC

	local function var_5_0(arg_6_0)
		local var_6_0 = ""

		if arg_6_0 == BackYardDecorationFilterPanel.ORDER_MODE_ASC:
			var_6_0 = "text_asc"
			arg_5_0.orderBtnIcon.localEulerAngles = Vector3(0, 0, 0)
		elif arg_6_0 == BackYardDecorationFilterPanel.ORDER_MODE_DASC:
			var_6_0 = "text_dasc"
			arg_5_0.orderBtnIcon.localEulerAngles = Vector3(0, 0, 180)

		arg_5_0.orderBtnTxt.sprite = GetSpriteFromAtlas("ui/NewBackYardDecorateUI_atlas", var_6_0)

		arg_5_0.orderBtnTxt.SetNativeSize()

	onToggle(arg_5_0, arg_5_0.orderBtn, function(arg_7_0)
		arg_5_0.orderMode = arg_7_0 and BackYardDecorationFilterPanel.ORDER_MODE_ASC or BackYardDecorationFilterPanel.ORDER_MODE_DASC

		if arg_5_0.pageType:
			arg_5_0.pages[arg_5_0.pageType].ExecuteAction("OrderModeUpdated", arg_5_0.orderMode)

		var_5_0(arg_5_0.orderMode), SFX_PANEL)
	var_5_0(arg_5_0.orderMode)
	onButton(arg_5_0, arg_5_0.shopBtn, function()
		arg_5_0.emit(BackYardDecorationMediator.OPEN_SHOP), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.searchClear, function()
		setInputText(arg_5_0.searchInput, ""), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.saveBtn, function()
		arg_5_0.dftAniEvent.SetEndEvent(function()
			arg_5_0.dftAniEvent.SetEndEvent(None)
			arg_5_0.emit(BackYardDecorationMediator.SAVE_ALL))
		arg_5_0.animation.Play("anim_courtyard_decoration_out"), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.clearBtn, function()
		arg_5_0.emit(BackYardDecorationMediator.ClEAR_ALL, True), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.filterBtn, function()
		if not arg_5_0.pageType:
			return

		arg_5_0.pages[arg_5_0.pageType].ShowFilterPanel(function(arg_14_0)
			local var_14_0
			local var_14_1 = i18n("backyard_sort_tag_price") == arg_14_0 and "text_price" or i18n("backyard_sort_tag_comfortable") == arg_14_0 and "text_comfortable" or i18n("backyard_sort_tag_size") == arg_14_0 and "text_area" or "text_default"

			arg_5_0.filterBtnTxt.sprite = GetSpriteFromAtlas("ui/NewBackYardDecorateUI_atlas", var_14_1)

			arg_5_0.filterBtnTxt.SetNativeSize()), SFX_PANEL)
	onInputChanged(arg_5_0, arg_5_0.searchInput, function(arg_15_0)
		if not arg_5_0.pageType:
			return

		setActive(arg_5_0.searchClear, arg_15_0 != "")
		arg_5_0.pages[arg_5_0.pageType].ExecuteAction("SearchKeyUpdated", arg_15_0))
	onButton(arg_5_0, arg_5_0.showPutListBtn, function()
		arg_5_0.putListPage.ExecuteAction("SetUp", 0, arg_5_0.dorm, arg_5_0.themes, arg_5_0.orderMode), SFX_PANEL)
	onToggle(arg_5_0, arg_5_0.themeTag, function(arg_17_0)
		if arg_17_0:
			arg_5_0.SwitchToPage(var_0_1), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.hideBtn, function()
		arg_5_0.bAnimtion.Play("anim_courtyard_decoration_bottomout"), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.showBtn, function()
		arg_5_0.bAnimtion.Play("anim_courtyard_decoration_bottomin"), SFX_PANEL)

	arg_5_0.tags = {
		arg_5_0.findTF("adpter/bottom/animroot/root/tags/1"),
		arg_5_0.findTF("adpter/bottom/animroot/root/tags/2"),
		arg_5_0.findTF("adpter/bottom/animroot/root/tags/3"),
		arg_5_0.findTF("adpter/bottom/animroot/root/tags/4"),
		arg_5_0.findTF("adpter/bottom/animroot/root/tags/5"),
		arg_5_0.findTF("adpter/bottom/animroot/root/tags/6"),
		arg_5_0.findTF("adpter/bottom/animroot/root/tags/7"),
		arg_5_0.findTF("adpter/bottom/animroot/root/tags/8")
	}

	onNextTick(function()
		arg_5_0.emit(BackYardDecorationMediator.ON_SET_UP))

def var_0_0.SetDorm(arg_21_0, arg_21_1):
	arg_21_0.dorm = arg_21_1

def var_0_0.UpdateDorm(arg_22_0, arg_22_1):
	arg_22_0.dorm = arg_22_1

	if arg_22_0.pageType:
		arg_22_0.pages[arg_22_0.pageType].ExecuteAction("DormUpdated", arg_22_0.dorm)

	if arg_22_0.putListPage.GetLoaded() and arg_22_0.putListPage.isShowing():
		arg_22_0.putListPage.ExecuteAction("DormUpdated", arg_22_0.dorm)

def var_0_0.OnApplyThemeBefore(arg_23_0):
	if arg_23_0.pageType:
		arg_23_0.pages[arg_23_0.pageType].ExecuteAction("OnApplyThemeBefore")

def var_0_0.OnApplyThemeAfter(arg_24_0, arg_24_1):
	if arg_24_0.pageType:
		arg_24_0.pages[arg_24_0.pageType].ExecuteAction("OnApplyThemeAfter", arg_24_1)

def var_0_0.UpdateFurniTrue(arg_25_0, arg_25_1):
	if arg_25_0.pageType:
		arg_25_0.pages[arg_25_0.pageType].ExecuteAction("FurnitureUpdated", arg_25_1)

def var_0_0.SetThemes(arg_26_0, arg_26_1):
	arg_26_0.themes = arg_26_1

def var_0_0.CustomThemeAdded(arg_27_0, arg_27_1):
	arg_27_0.themes[arg_27_1.id] = arg_27_1

	if arg_27_0.pageType:
		arg_27_0.pages[arg_27_0.pageType].ExecuteAction("CustomThemeAdded", arg_27_1)

def var_0_0.CustomThemeDeleted(arg_28_0, arg_28_1):
	arg_28_0.themes[arg_28_1] = None

	if arg_28_0.pageType:
		arg_28_0.pages[arg_28_0.pageType].ExecuteAction("CustomThemeDeleted", arg_28_1)

def var_0_0.ThemeUpdated(arg_29_0):
	if arg_29_0.pageType:
		arg_29_0.pages[arg_29_0.pageType].ExecuteAction("ThemeUpdated")

def var_0_0.UpdateTagTF(arg_30_0, arg_30_1, arg_30_2):
	onToggle(arg_30_0, arg_30_2, function(arg_31_0)
		if arg_31_0:
			arg_30_0.SwitchToPage(arg_30_1), SFX_PANEL)

def var_0_0.InitPages(arg_32_0):
	for iter_32_0, iter_32_1 in ipairs(arg_32_0.tags):
		arg_32_0.UpdateTagTF(iter_32_0 + 1, iter_32_1)

	triggerToggle(arg_32_0.themeTag, True)

def var_0_0.SwitchToPage(arg_33_0, arg_33_1):
	if arg_33_0.pageType == arg_33_1:
		return

	if arg_33_0.page and not arg_33_0.page.GetLoaded():
		return

	local var_33_0 = arg_33_0.pages[arg_33_1]

	if arg_33_0.page and arg_33_0.page != var_33_0:
		arg_33_0.page.ExecuteAction("Hide")

	var_33_0.ExecuteAction("SetUp", arg_33_1, arg_33_0.dorm, arg_33_0.themes, arg_33_0.orderMode)

	arg_33_0.page = var_33_0
	arg_33_0.pageType = arg_33_1

	setActive(arg_33_0.filterBtn, arg_33_0.pageType != var_0_1)

def var_0_0.willExit(arg_34_0):
	arg_34_0.dftAniEvent.SetEndEvent(None)
	arg_34_0.themePage.Destroy()
	arg_34_0.furniturePage.Destroy()
	arg_34_0.putListPage.Destroy()
	arg_34_0.contextData.furnitureDescMsgBox.Destroy()
	arg_34_0.contextData.filterPanel.Destroy()
	BackYardThemeTempalteUtil.ClearAllCache()

def var_0_0.onBackPressed(arg_35_0):
	if arg_35_0.themePage.OnBackPressed():
		return

	if arg_35_0.furniturePage.OnBackPressed():
		return

	if arg_35_0.putListPage.OnBackPressed():
		return

	if arg_35_0.contextData.furnitureDescMsgBox.GetLoaded() and arg_35_0.contextData.furnitureDescMsgBox.isShowing():
		arg_35_0.contextData.furnitureDescMsgBox.Hide()

		return

	if arg_35_0.contextData.filterPanel.GetLoaded() and arg_35_0.contextData.filterPanel.isShowing():
		arg_35_0.contextData.filterPanel.Hide()

		return

	triggerButton(arg_35_0.saveBtn)

return var_0_0
