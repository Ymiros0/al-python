local var_0_0 = class("AtelierCompositeScene", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "AtelierCompositeUI"

local var_0_1 = import("model.vo.AtelierFormula")
local var_0_2 = import("model.vo.AtelierFormulaCircle")
local var_0_3 = import("Mgr.Pool.PoolPlural")

var_0_0.FilterAll = bit.bor(1, 2, 4)

def var_0_0.Ctor(arg_2_0, ...):
	var_0_0.super.Ctor(arg_2_0, ...)

	arg_2_0.loader = AutoLoader.New()

def var_0_0.init(arg_3_0):
	arg_3_0.layerEmpty = arg_3_0._tf.Find("Empty")
	arg_3_0.layerFormula = arg_3_0._tf.Find("FormulaList")
	arg_3_0.painting = arg_3_0._tf.Find("Painting")
	arg_3_0.chat = arg_3_0.painting.Find("Chat")
	arg_3_0.layerFormulaDetail = arg_3_0._tf.Find("FormulaDetail")
	arg_3_0.layerFormulaOverlay = arg_3_0.layerFormulaDetail.Find("Overlay")
	arg_3_0.layerMaterialSelect = arg_3_0.layerFormulaOverlay.Find("AvaliableMaterials")
	arg_3_0.layerCompositeConfirm = arg_3_0._tf.Find("CompositeConfirmWindow")
	arg_3_0.layerCompositeResult = arg_3_0._tf.Find("CompositeResultWindow")
	arg_3_0.layerStoreHouse = arg_3_0._tf.Find("StoreHouseWindow")
	arg_3_0.layerMaterialsPreview = arg_3_0._tf.Find("FormulaMaterialsPreview")
	arg_3_0.top = arg_3_0._tf.Find("Top")
	arg_3_0.formulaRect = arg_3_0.layerFormula.Find("Frame/ScrollView").GetComponent("LScrollRect")

	local var_3_0 = arg_3_0.layerFormula.Find("Frame/Item")

	setActive(var_3_0, False)

	function arg_3_0.formulaRect.onUpdateItem(arg_4_0, arg_4_1)
		arg_3_0.UpdateFormulaItem(arg_4_0 + 1, arg_4_1)

	arg_3_0.formulaFilterButtons = _.map({
		1,
		2,
		3
	}, function(arg_5_0)
		return arg_3_0.layerFormula.Find("Frame/Tabs").GetChild(arg_5_0 - 1))
	arg_3_0.candicatesRect = arg_3_0.layerMaterialSelect.Find("Frame/List").GetComponent("LScrollRect")

	local var_3_1 = arg_3_0.layerMaterialSelect.Find("Frame/Item")

	setActive(var_3_1, False)

	function arg_3_0.candicatesRect.onUpdateItem(arg_6_0, arg_6_1)
		arg_3_0.UpdateCandicateItem(arg_6_0 + 1, arg_6_1)

	arg_3_0.storehouseRect = arg_3_0.layerStoreHouse.Find("Window/ScrollView").GetComponent("LScrollRect")

	local var_3_2 = arg_3_0.layerStoreHouse.Find("Window/ScrollView/Item")

	setActive(var_3_2, False)
	setActive(arg_3_0.layerFormula, False)
	setActive(arg_3_0.layerFormulaDetail, False)
	setActive(arg_3_0.layerMaterialSelect, False)
	setActive(arg_3_0.layerEmpty, False)
	setActive(arg_3_0.layerStoreHouse, False)
	setActive(arg_3_0.chat, False)
	pg.ViewUtils.SetSortingOrder(arg_3_0._tf.Find("Mask/BG").GetChild(0), -1)
	setText(arg_3_0._tf.Find("Empty/Bar/Text"), i18n("ryza_tip_composite_unlock"))
	setText(arg_3_0.layerFormula.Find("Frame/Filter/Text"), i18n("ryza_toggle_only_composite"))
	setText(arg_3_0.layerFormula.Find("Frame/Empty"), i18n("ryza_tip_no_recipe"))
	setText(arg_3_0.layerFormula.Find("Frame/Item/Lock/Text"), i18n("ryza_tip_unlock_all_tools"))
	setText(arg_3_0.layerFormula.Find("Bar/Text"), i18n("ryza_tip_select_recipe"))
	setText(arg_3_0.layerStoreHouse.Find("Window/Empty"), i18n("ryza_tip_no_item"))
	setText(arg_3_0.layerCompositeResult.Find("Window/CountBG/Tip"), i18n("ryza_composite_count"))
	setText(arg_3_0.layerMaterialsPreview.Find("Frame/Text"), i18n("ryza_tip_item_access"))
	setText(var_3_1.Find("IconBG/Lack/Text"), i18n("ryza_ui_show_acess"))

def var_0_0.SetEnabled(arg_7_0, arg_7_1):
	arg_7_0.unlockSystem = arg_7_1

def var_0_0.SetActivity(arg_8_0, arg_8_1):
	arg_8_0.activity = arg_8_1

local var_0_4 = "ui/AtelierCompositeUI_atlas"
local var_0_5 = "ui/AtelierCommonUI_atlas"

def var_0_0.preload(arg_9_0, arg_9_1):
	table.ParallelIpairsAsync({
		var_0_4,
		var_0_5
	}, function(arg_10_0, arg_10_1, arg_10_2)
		arg_9_0.loader.LoadBundle(arg_10_1, arg_10_2), arg_9_1)

def var_0_0.didEnter(arg_11_0):
	arg_11_0.contextData.filterType = var_0_0.FilterAll

	table.Foreach(arg_11_0.formulaFilterButtons, function(arg_12_0, arg_12_1)
		onButton(arg_11_0, arg_12_1, function()
			if arg_11_0.contextData.filterType == var_0_0.FilterAll:
				arg_11_0.contextData.filterType = bit.lshift(1, arg_12_0 - 1)
			else
				arg_11_0.contextData.filterType = bit.bxor(arg_11_0.contextData.filterType, bit.lshift(1, arg_12_0 - 1))

				if arg_11_0.contextData.filterType == 0:
					arg_11_0.contextData.filterType = var_0_0.FilterAll

			arg_11_0.UpdateFilterButtons()
			arg_11_0.FilterFormulas()
			arg_11_0.UpdateFormulaList(), SFX_PANEL))
	onToggle(arg_11_0, arg_11_0.layerFormula.Find("Frame/Filter/Toggle"), function(arg_14_0)
		arg_11_0.showOnlyComposite = arg_14_0

		arg_11_0.FilterFormulas()
		arg_11_0.UpdateFormulaList())
	onButton(arg_11_0, arg_11_0.layerFormulaOverlay.Find("Description/List"), function()
		arg_11_0.HideFormulaDetail()

		arg_11_0.contextData.formulaId = None

		arg_11_0.ShowFormulaList())
	onButton(arg_11_0, arg_11_0._tf.Find("Top/Back"), function()
		arg_11_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_11_0, arg_11_0._tf.Find("Top/Home"), function()
		arg_11_0.quickExitFunc(), SFX_CANCEL)
	onButton(arg_11_0, arg_11_0._tf.Find("Top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("ryza_composite_help_tip")
		}), SFX_PANEL)
	onButton(arg_11_0, arg_11_0.layerMaterialSelect.Find("BG"), function()
		arg_11_0.CloseCandicatePanel(), SFX_CANCEL)
	onButton(arg_11_0, arg_11_0.layerCompositeConfirm.Find("BG"), function()
		arg_11_0.HideCompositeConfirmWindow(), SFX_CANCEL)
	onButton(arg_11_0, arg_11_0.layerCompositeConfirm.Find("Window/Cancel"), function()
		arg_11_0.HideCompositeConfirmWindow(), SFX_CANCEL)
	onButton(arg_11_0, arg_11_0.layerCompositeResult.Find("BG"), function()
		arg_11_0.HideCompositeResult(), SFX_CANCEL)
	onButton(arg_11_0, arg_11_0._tf.Find("Top/StoreHouse"), function()
		arg_11_0.contextData.showStoreHouse = True

		arg_11_0.ShowStoreHouseWindow(), SFX_PANEL)
	onButton(arg_11_0, arg_11_0.layerStoreHouse.Find("Window/Close"), function()
		arg_11_0.CloseStoreHouseWindow(), SFX_CANCEL)
	onButton(arg_11_0, arg_11_0.layerStoreHouse.Find("BG"), function()
		arg_11_0.CloseStoreHouseWindow(), SFX_CANCEL)
	onButton(arg_11_0, arg_11_0.layerMaterialsPreview.Find("BG"), function()
		arg_11_0.HideMaterialsPreview(), SFX_CANCEL)
	pg.UIMgr.GetInstance().OverlayPanel(arg_11_0.top)

	if not arg_11_0.unlockSystem:
		setActive(arg_11_0.layerEmpty, True)
		setActive(arg_11_0.painting, False)
	else
		if arg_11_0.contextData.formulaId:
			local var_11_0 = arg_11_0.activity.GetFormulas()[arg_11_0.contextData.formulaId]

			arg_11_0.ShowFormulaDetail(var_11_0)
		else
			arg_11_0.DispalyChat({
				"ryza_atellier1"
			})
			arg_11_0.ShowFormulaList()

		if arg_11_0.contextData.showStoreHouse:
			arg_11_0.ShowStoreHouseWindow()

	if arg_11_0.unlockSystem and PlayerPrefs.GetInt("first_enter_ryza_atelier_" .. getProxy(PlayerProxy).getRawData().id, 0) == 0:
		triggerButton(arg_11_0._tf.Find("Top/Help"))
		PlayerPrefs.SetInt("first_enter_ryza_atelier_" .. getProxy(PlayerProxy).getRawData().id, 1)

def var_0_0.onBackPressed(arg_27_0):
	if arg_27_0.animating:
		return True

	if arg_27_0.CloseStoreHouseWindow():
		return True

	if arg_27_0.HideMaterialsPreview():
		return True

	if arg_27_0.HideCompositeResult():
		return True

	if arg_27_0.HideCompositeConfirmWindow():
		return True

	if arg_27_0.HideCandicatePanel():
		return True

	if arg_27_0.HideFormulaDetail():
		arg_27_0.contextData.formulaId = None

		arg_27_0.ShowFormulaList()

		return True

	arg_27_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.UpdateFilterButtons(arg_28_0):
	table.Foreach(arg_28_0.formulaFilterButtons, function(arg_29_0, arg_29_1)
		local var_29_0 = arg_28_0.contextData.filterType != var_0_0.FilterAll

		var_29_0 = var_29_0 and bit.band(arg_28_0.contextData.filterType, bit.lshift(1, arg_29_0 - 1)) > 0

		setActive(arg_29_1.Find("Selected"), var_29_0))

def var_0_0.AddIdleTimer(arg_30_0):
	arg_30_0.RemoveIdleTimer()

	arg_30_0.idleTimer = Timer.New(function()
		arg_30_0.DispalyChat({
			"ryza_atellier1"
		})
		arg_30_0.AddIdleTimer(), 8 + math.random() * 4)

	arg_30_0.idleTimer.Start()

def var_0_0.RemoveIdleTimer(arg_32_0):
	if not arg_32_0.idleTimer:
		return

	arg_32_0.idleTimer.Stop()

	arg_32_0.idleTimer = None

def var_0_0.ShowFormulaList(arg_33_0):
	arg_33_0.AddIdleTimer()
	setActive(arg_33_0.layerFormula, True)
	setParent(arg_33_0.layerFormula, arg_33_0.top)
	arg_33_0.layerFormula.SetSiblingIndex(0)
	arg_33_0.UpdateFilterButtons()
	arg_33_0.FilterFormulas()
	arg_33_0.UpdateFormulaList()

def var_0_0.HideFormulaList(arg_34_0):
	if not arg_34_0.layerFormula:
		return

	arg_34_0.RemoveIdleTimer()
	setParent(arg_34_0.layerFormula, arg_34_0._tf)
	setActive(arg_34_0.layerFormula, False)

	return True

def var_0_0.FilterFormulas(arg_35_0):
	arg_35_0.filterFormulas = {}

	local var_35_0 = arg_35_0.contextData.filterType

	local function var_35_1(arg_36_0)
		if var_35_0 == var_0_0.FilterAll:
			return True

		return switch(arg_36_0.GetType(), {
			[var_0_1.TYPE.EQUIP] = function()
				return bit.band(var_35_0, 1) > 0,
			[var_0_1.TYPE.ITEM] = function()
				return bit.band(var_35_0, 2) > 0,
			[var_0_1.TYPE.TOOL] = function()
				return bit.band(var_35_0, 4) > 0,
			[var_0_1.TYPE.OTHER] = function()
				return bit.band(var_35_0, 4) > 0
		})

	for iter_35_0, iter_35_1 in ipairs(_.values(arg_35_0.activity.GetFormulas())):
		if var_35_1(iter_35_1) and (not arg_35_0.showOnlyComposite or iter_35_1.IsAvaliable() and var_0_1.IsFormualCanComposite(iter_35_1, arg_35_0.activity)):
			table.insert(arg_35_0.filterFormulas, iter_35_1)

	local function var_35_2(arg_41_0, arg_41_1)
		local var_41_0 = {
			function(arg_42_0)
				return arg_42_0.IsAvaliable() and 0 or 1,
			function(arg_43_0)
				if arg_43_0.GetType() != var_0_1.TYPE.TOOL and not arg_35_0.activity.IsCompleteAllTools():
					return 1
				else
					return 0,
			function(arg_44_0)
				return arg_44_0.GetConfigID()
		}

		for iter_41_0, iter_41_1 in ipairs(var_41_0):
			local var_41_1 = iter_41_1(arg_41_0)
			local var_41_2 = iter_41_1(arg_41_1)

			if var_41_1 != var_41_2:
				return var_41_1 < var_41_2

		return False

	table.sort(arg_35_0.filterFormulas, var_35_2)

def var_0_0.UpdateFormulaList(arg_45_0):
	local var_45_0 = #arg_45_0.filterFormulas == 0

	setActive(arg_45_0.layerFormula.Find("Frame/Empty"), var_45_0)
	setActive(arg_45_0.layerFormula.Find("Frame/ScrollView"), not var_45_0)
	arg_45_0.formulaRect.SetTotalCount(#arg_45_0.filterFormulas)

local var_0_6 = {
	[var_0_1.TYPE.EQUIP] = "ryza_word_equip",
	[var_0_1.TYPE.ITEM] = "word_item",
	[var_0_1.TYPE.TOOL] = "word_tool",
	[var_0_1.TYPE.OTHER] = "word_other"
}

def var_0_0.UpdateFormulaItem(arg_46_0, arg_46_1, arg_46_2):
	local var_46_0 = tf(arg_46_2)
	local var_46_1 = arg_46_0.filterFormulas[arg_46_1]
	local var_46_2 = var_46_1.GetProduction()

	arg_46_0.UpdateRyzaDrop(var_46_0.Find("BG/Icon"), {
		type = var_46_2[1],
		id = var_46_2[2]
	}, True)

	local var_46_3 = var_0_6[var_46_1.GetType()]
	local var_46_4 = var_46_1.GetType() != var_0_1.TYPE.TOOL and not arg_46_0.activity.IsCompleteAllTools()

	setActive(var_46_0.Find("Lock"), var_46_4)
	setActive(var_46_0.Find("BG"), not var_46_4)
	setText(var_46_0.Find("BG/Type"), i18n(var_46_3))
	setScrollText(var_46_0.Find("BG/Name/Text"), var_46_1.GetName())

	local var_46_5

	if var_46_1.GetMaxLimit() > 0:
		var_46_5 = var_46_1.GetMaxLimit() - var_46_1.GetUsedCount() .. "/" .. var_46_1.GetMaxLimit()
	else
		var_46_5 = "∞"

	local var_46_6 = var_46_1.IsAvaliable()

	setActive(var_46_0.Find("BG/Count"), var_46_6)
	setActive(var_46_0.Find("Completed"), not var_46_6)

	if var_46_6:
		local var_46_7 = var_0_1.IsFormualCanComposite(var_46_1, arg_46_0.activity)
		local var_46_8 = SummerFeastScene.TransformColor(var_46_7 and "4fb3a3" or "d55a54")

		setTextColor(var_46_0.Find("BG/Count"), var_46_8)

	setText(var_46_0.Find("BG/Count"), var_46_5)
	onButton(arg_46_0, var_46_0, function()
		if not var_46_6:
			pg.TipsMgr.GetInstance().ShowTips(i18n("ryza_tip_composite_invalid"))

			return

		if var_46_4:
			pg.TipsMgr.GetInstance().ShowTips(i18n("ryza_tip_unlock_all_tools"))

			return

		arg_46_0.HideFormulaList()
		arg_46_0.ShowFormulaDetail(var_46_1)
		arg_46_0.DispalyChat({
			"ryza_atellier2",
			"ryza_atellier3",
			"ryza_atellier4"
		})
		pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/ryza_atellier_ui_1"), SFX_PANEL)

def var_0_0.UpdateRyzaDrop(arg_48_0, arg_48_1, arg_48_2, arg_48_3):
	updateDrop(arg_48_1, arg_48_2)
	SetCompomentEnabled(arg_48_1.Find("icon_bg"), typeof(Image), False)
	setActive(arg_48_1.Find("bg"), False)
	setActive(arg_48_1.Find("icon_bg/frame"), False)
	setActive(arg_48_1.Find("icon_bg/stars"), False)

	local var_48_0 = arg_48_2.getConfig("rarity")

	if arg_48_2.type == DROP_TYPE_EQUIP or arg_48_2.type == DROP_TYPE_EQUIPMENT_SKIN:
		var_48_0 = var_48_0 - 1

	local var_48_1 = "icon_frame_" .. var_48_0

	if arg_48_3:
		var_48_1 = var_48_1 .. "_small"

	arg_48_0.loader.GetSpriteQuiet(var_0_5, var_48_1, arg_48_1)

	if arg_48_2.type == DROP_TYPE_EQUIP or arg_48_2.type == DROP_TYPE_SPWEAPON:
		onButton(arg_48_0, arg_48_1, function()
			arg_48_0.emit(var_0_0.ON_DROP, arg_48_2), SFX_PANEL)
	else
		removeOnButton(arg_48_1)

local var_0_7 = {
	[var_0_2.TYPE.BASE] = "circle",
	[var_0_2.TYPE.NORMAL] = "hexagon",
	[var_0_2.TYPE.SAIREN] = "doubleHexagon",
	[var_0_2.TYPE.ANY] = "anyHexagon"
}

def var_0_0.ShowFormulaDetail(arg_50_0, arg_50_1):
	setActive(arg_50_0.layerFormulaDetail, True)
	setParent(arg_50_0.layerFormulaOverlay, arg_50_0.top)
	arg_50_0.layerFormulaOverlay.SetSiblingIndex(0)
	setParent(arg_50_0.painting, arg_50_0.layerFormulaOverlay)
	arg_50_0.painting.SetSiblingIndex(0)

	if not arg_50_0.nodePools:
		arg_50_0.nodePools = {
			circle = var_0_3.New(arg_50_0.layerFormulaDetail.Find("CircleNode").gameObject, 100),
			hexagon = var_0_3.New(arg_50_0.layerFormulaDetail.Find("HexagonNode").gameObject, 100),
			anyHexagon = var_0_3.New(arg_50_0.layerFormulaDetail.Find("AnyHexagonNode").gameObject, 100),
			doubleHexagon = var_0_3.New(arg_50_0.layerFormulaDetail.Find("DoubleHexagonNode").gameObject, 100)
		}

		table.Foreach(arg_50_0.nodePools, function(arg_51_0, arg_51_1)
			setActive(arg_51_1.prefab, False))

	arg_50_0.pluralRoot = arg_50_0.pluralRoot or pg.PoolMgr.GetInstance().root
	arg_50_0.nodeList = arg_50_0.nodeList or {}

	_.each(arg_50_0.nodeList, function(arg_52_0)
		local var_52_0 = arg_50_0.nodePools[var_0_7[arg_52_0.Data.GetType()]]
		local var_52_1 = tf(arg_52_0.GO)

		SetCompomentEnabled(var_52_1.Find("Item"), typeof(Image), False)
		arg_50_0.loader.ClearRequest(var_52_1.Find("Ring"))
		table.Foreach(arg_52_0.links, function(arg_53_0)
			local var_53_0 = var_52_1.Find("Links/" .. arg_53_0)

			arg_50_0.loader.ClearRequest(var_53_0))
		arg_50_0.loader.ClearRequest(var_52_1)

		if not var_52_0.Enqueue(go(arg_52_0.GO)):
			setParent(go(arg_52_0.GO), arg_50_0.pluralRoot)
			setActive(go(arg_52_0.GO), False))
	table.clean(arg_50_0.nodeList)
	arg_50_0.InitFormula(arg_50_1)

def var_0_0.HideFormulaDetail(arg_54_0):
	if not isActive(arg_54_0.layerFormulaDetail):
		return

	arg_54_0.HideCandicatePanel()
	setParent(arg_54_0.painting, arg_54_0._tf)
	arg_54_0.painting.SetSiblingIndex(1)
	setParent(arg_54_0.layerFormulaOverlay, arg_54_0.layerFormulaDetail)
	setActive(arg_54_0.layerFormulaDetail, False)

	return True

local var_0_8 = {
	{
		0,
		1
	},
	{
		-1,
		1
	},
	{
		-1,
		0
	},
	{
		0,
		-1
	},
	{
		1,
		-1
	},
	{
		1,
		0
	}
}
local var_0_9 = {
	[var_0_1.TYPE.EQUIP] = "text_equip",
	[var_0_1.TYPE.ITEM] = "text_item",
	[var_0_1.TYPE.TOOL] = "text_other",
	[var_0_1.TYPE.OTHER] = "text_other"
}

def var_0_0.InitFormula(arg_55_0, arg_55_1):
	arg_55_0.contextData.formulaId = arg_55_1.GetConfigID()

	local var_55_0 = arg_55_0.layerFormulaOverlay.Find("Description")

	arg_55_0.loader.GetSpriteQuiet(var_0_4, var_0_9[arg_55_1.GetType()], var_55_0.Find("Type"))

	local var_55_1 = {
		type = arg_55_1.GetProduction()[1],
		id = arg_55_1.GetProduction()[2]
	}

	arg_55_0.UpdateRyzaDrop(var_55_0.Find("Icon"), var_55_1)
	setText(var_55_0.Find("Name"), arg_55_1.GetName())
	setText(var_55_0.Find("Description/Text"), arg_55_1.GetDesc())

	local var_55_2 = tostring(arg_55_1.GetMaxLimit() - arg_55_1.GetUsedCount())

	if arg_55_1.GetMaxLimit() < 0:
		var_55_2 = "∞"

	setText(var_55_0.Find("RestCount/Text"), i18n("ryza_rest_produce_count", var_55_2))
	setActive(arg_55_0.layerMaterialSelect, False)

	local var_55_3 = arg_55_0.layerFormulaDetail.Find("ScrollView/Content")

	setAnchoredPosition(var_55_3, Vector2.zero)
	_.each(arg_55_1.GetCircleList(), function(arg_56_0)
		local var_56_0 = var_0_2.New({
			configId = arg_56_0
		})
		local var_56_1 = arg_55_0.nodePools[var_0_7[var_56_0.GetType()]].Dequeue()

		var_56_1.name = arg_56_0

		setActive(var_56_1, True)
		setParent(tf(var_56_1), var_55_3)

		local var_56_2 = {
			Change = True,
			Data = var_56_0,
			GO = var_56_1
		}

		table.insert(arg_55_0.nodeList, var_56_2))

	local var_55_4 = 280
	local var_55_5 = math.deg2Rad * 30
	local var_55_6 = var_55_4 * Vector2.New(math.cos(var_55_5), math.sin(var_55_5))
	local var_55_7 = var_55_4 * Vector2(0, 1)
	local var_55_8 = Vector2.zero

	local function var_55_9(arg_57_0, arg_57_1)
		setAnchoredPosition(arg_57_0.GO, arg_57_1)

		local var_57_0 = arg_57_0.Data.GetNeighbors()

		arg_57_0.links = {}

		_.each(var_57_0, function(arg_58_0)
			local var_58_0 = arg_58_0[1]
			local var_58_1 = arg_58_0[2]
			local var_58_2 = var_0_8[var_58_0]
			local var_58_3 = var_58_2[1] * var_55_6 + var_58_2[2] * var_55_7
			local var_58_4 = _.detect(arg_55_0.nodeList, function(arg_59_0)
				return arg_59_0.Data.GetConfigID() == var_58_1)

			var_58_4.prevLink = {
				(var_58_0 + 2) % 5 + 1,
				arg_57_0
			}
			arg_57_0.links[var_58_0] = var_58_4

			local var_58_5 = arg_57_1 + var_58_3

			var_55_9(var_58_4, var_58_5)

			var_55_8 = Vector2.Max(var_55_8, -var_58_5)
			var_55_8 = Vector2.Max(var_55_8, var_58_5))

	var_55_9(arg_55_0.nodeList[1], Vector2.zero)
	setSizeDelta(var_55_3, (var_55_8 + Vector2.New(var_55_4, var_55_4)) * 2)
	onButton(arg_55_0, arg_55_0.layerFormulaDetail.Find("Composite"), function()
		if not _.all(arg_55_0.nodeList, function(arg_61_0)
			return arg_61_0.Instance):
			arg_55_0.ShowMaterialsPreview()

			return

		if not arg_55_0.activity.GetFormulas()[arg_55_0.contextData.formulaId].IsAvaliable():
			pg.TipsMgr.GetInstance().ShowTips(i18n("ryza_tip_composite_invalid"))

			return

		arg_55_0.ShowCompositeConfirmWindow(), SFX_PANEL)
	onButton(arg_55_0, arg_55_0.layerFormulaDetail.Find("AutoFill"), function()
		local var_62_0 = {}
		local var_62_1 = arg_55_0.activity.GetItems()

		local function var_62_2(arg_63_0)
			local var_63_0 = var_62_0[arg_63_0.GetConfigID()] or Clone(var_62_1[arg_63_0.GetConfigID()])

			assert(var_63_0, "Using Unexist material")

			var_63_0.count = var_63_0.count - 1
			var_62_0[arg_63_0.GetConfigID()] = var_63_0

		local var_62_3 = {}

		_.each(arg_55_0.nodeList, function(arg_64_0)
			if arg_64_0.Instance:
				var_62_2(arg_64_0.Instance)
			else
				table.insert(var_62_3, arg_64_0))

		if #var_62_3 <= 0:
			return

		local var_62_4 = True

		local function var_62_5()
			if not var_62_4:
				return

			arg_55_0.DispalyChat({
				"ryza_atellier5",
				"ryza_atellier6",
				"ryza_atellier7"
			})

			var_62_4 = False

		local var_62_6 = False
		local var_62_7

		local function var_62_8()
			if var_62_7 and coroutine.status(var_62_7) == "suspended":
				local var_66_0, var_66_1 = coroutine.resume(var_62_7)

				assert(var_66_0, debug.traceback(var_62_7, var_66_1))

		var_62_7 = coroutine.create(function()
			_.each(var_62_3, function(arg_68_0)
				local var_68_0 = arg_68_0.Data

				if var_68_0.GetType() == var_0_2.TYPE.BASE or var_68_0.GetType() == var_0_2.TYPE.SAIREN:
					local var_68_1 = var_68_0.GetLimitItemID()
					local var_68_2 = var_62_0[var_68_1] or var_62_1[var_68_1]

					if var_68_2 and var_68_2.count > 0:
						var_62_2(var_68_2)
						var_62_5()
						arg_55_0.FillNodeAndPlayAnim(arg_68_0, AtelierMaterial.New({
							count = 1,
							configId = var_68_1
						}), var_62_8, True)
						coroutine.yield()
					else
						var_62_6 = True)

			if not var_62_6:
				local var_67_0 = False
				local var_67_1 = False

				arg_55_0.DisPlayUnlockEffect(function()
					var_67_0 = True

					if var_67_1:
						var_62_8())

				if not var_67_0:
					var_67_1 = True

					coroutine.yield()

				local var_67_2 = True

				local function var_67_3()
					if not var_67_2:
						return

					pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/ryza_atellier_ui_5")

					var_67_2 = False

				local var_67_4 = AtelierMaterial.bindConfigTable()

				local function var_67_5(arg_71_0)
					local var_71_0 = arg_71_0.Data

					for iter_71_0, iter_71_1 in ipairs(var_67_4.all):
						local var_71_1 = var_62_0[iter_71_1] or var_62_1[iter_71_1]

						if var_71_1 and var_71_1.count > 0 and var_71_1.IsNormal() and var_71_0.CanUseMaterial(var_71_1, arg_55_1):
							var_62_2(var_71_1)
							var_62_5()
							var_67_3()
							arg_55_0.FillNodeAndPlayAnim(arg_71_0, AtelierMaterial.New({
								count = 1,
								configId = var_71_1.GetConfigID()
							}), True)

							return

					var_62_6 = True

				_.each(var_62_3, function(arg_72_0)
					if arg_72_0.Data.GetType() == var_0_2.TYPE.NORMAL:
						var_67_5(arg_72_0))
				_.each(var_62_3, function(arg_73_0)
					if arg_73_0.Data.GetType() == var_0_2.TYPE.ANY:
						var_67_5(arg_73_0))

			if var_62_6:
				pg.TipsMgr.GetInstance().ShowTips(i18n("ryza_material_not_enough"))

			arg_55_0.UpdateFormulaDetail())

		var_62_8(), SFX_PANEL)
	arg_55_0.UpdateFormulaDetail()

def var_0_0.CleanNodeInstance(arg_74_0):
	local var_74_0 = arg_74_0.activity.GetFormulas()[arg_74_0.contextData.formulaId]

	if not var_74_0.IsAvaliable():
		arg_74_0.HideFormulaDetail()

		arg_74_0.contextData.formulaId = None

		arg_74_0.ShowFormulaList()

		return

	_.each(arg_74_0.nodeList, function(arg_75_0)
		arg_75_0.Instance = None
		arg_75_0.Change = True)
	arg_74_0.ShowFormulaDetail(var_74_0)

def var_0_0.UpdateFormulaDetail(arg_76_0):
	local var_76_0 = 0
	local var_76_1 = 0
	local var_76_2 = tobool(arg_76_0.unlockAllBase)

	arg_76_0.unlockAllBase = True

	_.each(arg_76_0.nodeList, function(arg_77_0)
		var_76_0 = var_76_0 + 1
		var_76_1 = var_76_1 + (arg_77_0.Instance and 1 or 0)
		arg_76_0.unlockAllBase = arg_76_0.unlockAllBase and (arg_77_0.Data.GetType() != var_0_2.TYPE.BASE and arg_77_0.Data.GetType() != var_0_2.TYPE.SAIREN or arg_77_0.Instance))
	_.each(arg_76_0.nodeList, function(arg_78_0)
		local var_78_0 = not arg_76_0.unlockAllBase and arg_78_0.Data.GetType() != var_0_2.TYPE.BASE and arg_78_0.Data.GetType() != var_0_2.TYPE.SAIREN

		arg_78_0.ChangeLock = arg_78_0.ChangeLock or tobool(arg_78_0.Lock) and not var_78_0
		arg_78_0.Lock = var_78_0)

	local var_76_3 = arg_76_0.unlockAllBase != var_76_2

	_.each(arg_76_0.nodeList, function(arg_79_0)
		if var_76_3:
			arg_79_0.Change = True

		arg_76_0.UpdateNodeView(arg_79_0))
	setText(arg_76_0.layerFormulaDetail.Find("Bar/Text"), i18n("ryza_tip_put_materials", var_76_1, var_76_0))
	setGray(arg_76_0.layerFormulaDetail.Find("AutoFill"), not arg_76_0.activity.GetFormulas()[arg_76_0.contextData.formulaId].IsAvaliable())
	setActive(arg_76_0.layerFormulaDetail.Find("Composite/Disabled"), var_76_1 < var_76_0)

local var_0_10 = {
	[var_0_2.ELEMENT_TYPE.PYRO] = "laisha_ui_huo",
	[var_0_2.ELEMENT_TYPE.CRYO] = "laisha_ui_bing",
	[var_0_2.ELEMENT_TYPE.ELECTRO] = "laisha_ui_lei",
	[var_0_2.ELEMENT_TYPE.ANEMO] = "laisha_ui_feng",
	[var_0_2.ELEMENT_TYPE.SAIREN] = "laisha_ui_sairen"
}
local var_0_11 = "laisha_ui_wupinshanguang"
local var_0_12 = "laisha_ui_jiesuo"
local var_0_13 = {
	"laisha_ui_lianjie01",
	"laisha_ui_lianjie02",
	"laisha_ui_lianjie_qiehuan"
}

def var_0_0.UpdateNodeView(arg_80_0, arg_80_1):
	local var_80_0 = tf(arg_80_1.GO)

	for iter_80_0 = 1, 6:
		setActive(var_80_0.Find("Links").GetChild(iter_80_0 - 1), False)

	local var_80_1 = arg_80_1.Data

	_.each(var_80_1.GetNeighbors(), function(arg_81_0)
		setActive(var_80_0.Find("Links").GetChild(arg_81_0[1] - 1), True))

	local var_80_2 = var_80_1.GetElementName()
	local var_80_3 = arg_80_1.Lock

	setActive(var_80_0.Find("Lock"), var_80_3)

	if var_80_3:
		if var_80_1.GetType() != var_0_2.TYPE.ANY:
			arg_80_0.loader.GetSpriteQuiet(var_0_5, "element_" .. var_80_2, var_80_0.Find("Lock/Require/Icon"))

		setText(var_80_0.Find("Lock/Require/Text"), "X" .. var_80_1.GetLevel())

	for iter_80_1 = 3, var_80_1.GetLevel() + 1, -1:
		local var_80_4 = var_80_0.Find("Slots").GetChild(iter_80_1 - 1)

		arg_80_0.loader.GetSpriteQuiet(var_0_4, "slot_BLOCKED", var_80_4.Find("Image"))

	local var_80_5 = arg_80_1.Instance

	if not var_80_5:
		if var_80_1.GetType() == var_0_2.TYPE.ANY:
			setActive(var_80_0.Find("All"), True)
		else
			setActive(var_80_0.Find("Icon"), True)
			arg_80_0.loader.GetSpriteQuiet(var_0_4, "icon_" .. var_80_2, var_80_0.Find("Icon"), True)

		setActive(var_80_0.Find("Item"), False)

		if var_80_1.GetType() == var_0_2.TYPE.BASE or var_80_1.GetType() == var_0_2.TYPE.SAIREN:
			local var_80_6 = AtelierMaterial.New({
				configId = var_80_1.GetLimitItemID()
			})

			setActive(var_80_0.Find("Name"), True)
			setScrollText(var_80_0.Find("Name/Rect/Text"), var_80_6.GetName())
		else
			setActive(var_80_0.Find("Name"), False)

		for iter_80_2 = 1, var_80_1.GetLevel():
			local var_80_7 = var_80_0.Find("Slots").GetChild(iter_80_2 - 1)

			arg_80_0.loader.GetSpriteQuiet(var_0_4, "slot_NULL", var_80_7.Find("Image"))
	else
		local var_80_8 = var_80_1.GetRingElement(var_80_5)
		local var_80_9 = var_0_2.ELEMENT_NAME[var_80_8]

		if var_80_1.GetType() == var_0_2.TYPE.ANY:
			setActive(var_80_0.Find("All"), False)
		else
			setActive(var_80_0.Find("Icon"), False)

		setActive(var_80_0.Find("Item"), True)

		local var_80_10

		if var_80_1.GetType() == var_0_2.TYPE.BASE or var_80_1.GetType() == var_0_2.TYPE.SAIREN:
			var_80_10 = var_80_5.GetBaseCircleTransform()
		else
			var_80_10 = var_80_5.GetNormalCircleTransform()

		setLocalScale(var_80_0.Find("Item"), Vector3.New(unpack(var_80_10, 1, 3)))
		setAnchoredPosition(var_80_0.Find("Item"), Vector2.New(unpack(var_80_10, 4, 5)))
		arg_80_0.loader.GetSpriteQuiet(var_80_5.GetIconPath(), "", var_80_0.Find("Item"), True)
		setActive(var_80_0.Find("Name"), True)
		setScrollText(var_80_0.Find("Name/Rect/Text"), var_80_5.GetName())

		for iter_80_3 = 1, var_80_1.GetLevel():
			local var_80_11 = var_80_0.Find("Slots").GetChild(iter_80_3 - 1)

			arg_80_0.loader.GetSpriteQuiet(var_0_4, "slot_" .. var_80_9, var_80_11.Find("Image"))

	local var_80_12 = var_80_0.Find("Ring")

	setImageColor(var_80_12, var_80_1.GetElementRingColor(var_80_5))

	if arg_80_1.Change:
		local var_80_13 = arg_80_1.Data.GetRingElement(var_80_5)

		if var_80_3:
			var_80_13 = None

		if var_0_10[var_80_13]:
			local var_80_14 = arg_80_1.Data.GetType() == var_0_2.TYPE.BASE and "_o" or "_6"

			arg_80_0.loader.GetPrefab("ui/" .. var_0_10[var_80_13] .. var_80_14, "", function(arg_82_0)
				setParent(arg_82_0, var_80_12)
				setAnchoredPosition(arg_82_0, Vector2.zero), var_80_12)
		else
			arg_80_0.loader.ClearRequest(var_80_12)

		table.Foreach(arg_80_1.links, function(arg_83_0, arg_83_1)
			local var_83_0 = var_80_0.Find("Links/" .. arg_83_0)
			local var_83_1 = var_0_13[3]

			if arg_83_1.Lock and var_80_3:
				var_83_1 = var_0_13[1]
			elif not arg_83_1.Lock and not var_80_3:
				var_83_1 = var_0_13[2]

			arg_80_0.loader.GetPrefab("ui/" .. var_83_1, "", function(arg_84_0)
				setParent(arg_84_0, var_83_0.Find("Link"))
				setAnchoredPosition(arg_84_0, Vector2.New(0, -15)), var_83_0))

		arg_80_1.Change = None

	if arg_80_1.ChangeInstance:
		local var_80_15 = var_80_0.Find("Item")

		if var_80_5:
			arg_80_0.loader.GetPrefab("ui/" .. var_0_11, "", function(arg_85_0)
				setParent(arg_85_0, var_80_15)
				setAnchoredPosition(arg_85_0, Vector2.zero), var_80_0)
		else
			arg_80_0.loader.ClearRequest(var_80_0)

		arg_80_1.ChangeInstance = None

	onButton(arg_80_0, var_80_0, function()
		if var_80_3:
			return

		local var_86_0 = arg_80_0.layerMaterialSelect.Find("TargetBG")

		var_86_0.localRotation = Quaternion.identity

		local var_86_1 = var_80_1.GetType() == var_0_2.TYPE.BASE and 300 or 245

		setSizeDelta(var_86_0, {
			x = var_86_1,
			y = var_86_1
		})

		local var_86_2 = arg_80_0.layerMaterialSelect.Find("Target")

		arg_80_0.ShowCandicatePanel()

		local var_86_3 = tf(Instantiate(var_80_0))

		SetCompomentEnabled(var_86_3, typeof(Button), False)
		setParent(var_86_3, var_86_2)
		setAnchoredPosition(var_86_3, Vector2.zero)

		for iter_86_0 = 1, 6:
			setActive(var_86_3.Find("Links").GetChild(iter_86_0 - 1), False)

		local var_86_4 = var_86_2.anchoredPosition
		local var_86_5 = arg_80_0.layerFormulaDetail.Find("ScrollView/Content")
		local var_86_6 = var_80_0.anchoredPosition + arg_80_0.layerFormulaDetail.Find("ScrollView").anchoredPosition

		setAnchoredPosition(var_86_5, var_86_4 - var_86_6)

		arg_80_0.candicateTarget = arg_80_1

		GetComponent(var_86_0, typeof(Animator)).SetBool("Selecting", True)
		arg_80_0.UpdateCandicatePanel(), SFX_PANEL)

def var_0_0.FillNodeAndPlayAnim(arg_87_0, arg_87_1, arg_87_2, arg_87_3, arg_87_4):
	arg_87_0.LoadingOn()

	arg_87_1.ChangeInstance = arg_87_1.ChangeInstance or tobool(arg_87_1.Instance) != tobool(arg_87_2)
	arg_87_1.Instance = arg_87_2
	arg_87_1.Change = True

	local var_87_0 = {}
	local var_87_1 = {}

	seriesAsync({
		function(arg_88_0)
			table.ParallelIpairsAsync({
				"ui/laisha_ui_wupinzhiru",
				"ui/laisha_ui_baoshi"
			}, function(arg_89_0, arg_89_1, arg_89_2)
				var_87_0[arg_89_0] = arg_87_0.loader.GetPrefab(arg_89_1, "", function(arg_90_0)
					setParent(arg_90_0, tf(arg_87_1.GO))
					setAnchoredPosition(arg_90_0, Vector2.zero)

					var_87_1[arg_89_0] = arg_90_0

					setActive(arg_90_0, False)
					arg_89_2()), arg_88_0),
		function(arg_91_0)
			setActive(var_87_1[1], True)
			arg_87_0.managedTween(LeanTween.delayedCall, function()
				if not arg_87_4:
					arg_87_0.UpdateFormulaDetail()
				else
					arg_87_0.UpdateNodeView(arg_87_1)

				pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/ryza_atellier_ui_4")
				arg_91_0(), 0.2, None),
		function(arg_93_0)
			setActive(var_87_1[2], True)
			arg_87_0.managedTween(LeanTween.delayedCall, function()
				arg_93_0(), 0.5, None),
		function(arg_95_0)
			arg_87_0.loader.ClearRequest(var_87_0[1])
			arg_87_0.loader.ClearRequest(var_87_0[2])
			arg_87_0.LoadingOff()
			existCall(arg_87_3)
	})

def var_0_0.DisPlayUnlockEffect(arg_96_0, arg_96_1):
	arg_96_0.unlockAllBase = True

	_.each(arg_96_0.nodeList, function(arg_97_0)
		arg_96_0.unlockAllBase = arg_96_0.unlockAllBase and (arg_97_0.Data.GetType() != var_0_2.TYPE.BASE and arg_97_0.Data.GetType() != var_0_2.TYPE.SAIREN or arg_97_0.Instance))
	_.each(arg_96_0.nodeList, function(arg_98_0)
		local var_98_0 = not arg_96_0.unlockAllBase and arg_98_0.Data.GetType() != var_0_2.TYPE.BASE and arg_98_0.Data.GetType() != var_0_2.TYPE.SAIREN

		arg_98_0.ChangeLock = arg_98_0.ChangeLock or tobool(arg_98_0.Lock) and not var_98_0
		arg_98_0.Lock = var_98_0)

	if not _.any(arg_96_0.nodeList, function(arg_99_0)
		return arg_99_0.ChangeLock):
		existCall(arg_96_1)

		return

	arg_96_0.LoadingOn()

	local var_96_0 = {}

	_.each(arg_96_0.nodeList, function(arg_100_0)
		local var_100_0 = tf(arg_100_0.GO)

		if arg_100_0.ChangeLock:
			if arg_100_0.prevLink:
				arg_100_0.prevLink[2].Change = True

			local var_100_1 = arg_96_0.loader.GetPrefab("ui/" .. var_0_12, "", function(arg_101_0)
				setParent(arg_101_0, var_100_0)
				setAnchoredPosition(arg_101_0, Vector2.zero))

			table.insert(var_96_0, var_100_1)

			arg_100_0.ChangeLock = None)
	arg_96_0.managedTween(LeanTween.delayedCall, function()
		pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/ryza_atellier_ui_3"), 0.7, None)
	arg_96_0.managedTween(LeanTween.delayedCall, function()
		_.each(var_96_0, function(arg_104_0)
			arg_96_0.loader.ClearRequest(arg_104_0))
		arg_96_0.LoadingOff()
		existCall(arg_96_1), 1.7, None)

def var_0_0.ShowCandicatePanel(arg_105_0):
	arg_105_0.DispalyChat({
		"ryza_atellier2",
		"ryza_atellier3",
		"ryza_atellier4"
	})
	pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/ryza_atellier_ui_1")
	pg.UIMgr.GetInstance().BlurPanel(arg_105_0.top)
	setActive(arg_105_0.layerMaterialSelect, True)
	SetCompomentEnabled(arg_105_0.layerFormulaDetail.Find("ScrollView"), typeof(ScrollRect), False)
	removeAllChildren(arg_105_0.layerMaterialSelect.Find("Target"))

def var_0_0.CloseCandicatePanel(arg_106_0):
	arg_106_0.LoadingOn()

	local var_106_0 = GetComponent(arg_106_0.layerMaterialSelect.Find("TargetBG"), typeof(DftAniEvent))

	var_106_0.SetEndEvent(function()
		arg_106_0.LoadingOff()
		arg_106_0.HideCandicatePanel()
		var_106_0.SetEndEvent(None))
	GetComponent(arg_106_0.layerMaterialSelect.Find("TargetBG"), typeof(Animator)).SetBool("Selecting", False)

def var_0_0.HideCandicatePanel(arg_108_0):
	if not isActive(arg_108_0.layerMaterialSelect):
		return

	pg.UIMgr.GetInstance().OverlayPanel(arg_108_0.top)
	arg_108_0.painting.SetSiblingIndex(1)
	setActive(arg_108_0.layerMaterialSelect, False)
	removeAllChildren(arg_108_0.layerMaterialSelect.Find("Target"))
	SetCompomentEnabled(arg_108_0.layerFormulaDetail.Find("ScrollView"), typeof(ScrollRect), True)

	arg_108_0.candicateTarget = None

	return True

def var_0_0.UpdateCandicatePanel(arg_109_0):
	arg_109_0.candicates = {}

	local var_109_0 = arg_109_0.activity.GetItems()
	local var_109_1 = arg_109_0.activity.GetFormulas()[arg_109_0.contextData.formulaId]
	local var_109_2 = AtelierMaterial.bindConfigTable()
	local var_109_3 = _.map(var_109_2.all, function(arg_110_0)
		local var_110_0 = var_109_0[arg_110_0] or AtelierMaterial.New({
			configId = arg_110_0
		})

		if arg_109_0.candicateTarget.Data.CanUseMaterial(var_110_0, var_109_1):
			if var_109_0[arg_110_0]:
				var_110_0 = AtelierMaterial.New({
					configId = arg_110_0,
					count = var_109_0[arg_110_0].count
				})
				var_110_0.count = _.reduce(arg_109_0.nodeList, var_110_0.count, function(arg_111_0, arg_111_1)
					if arg_111_1.Instance and arg_111_1.Instance.GetConfigID() == arg_110_0:
						arg_111_0 = arg_111_0 - 1

					return arg_111_0)

			return var_110_0)

	table.sort(var_109_3, function(arg_112_0, arg_112_1)
		if arg_112_0.count * arg_112_1.count == 0 and arg_112_0.count - arg_112_1.count != 0:
			return arg_112_0.count < arg_112_1.count
		else
			return arg_112_0.GetConfigID() < arg_112_1.GetConfigID())
	_.each(var_109_3, function(arg_113_0)
		for iter_113_0 = 1, math.max(arg_113_0.count, 1):
			table.insert(arg_109_0.candicates, arg_113_0))
	arg_109_0.candicatesRect.SetTotalCount(#arg_109_0.candicates, 0)

def var_0_0.UpdateCandicateItem(arg_114_0, arg_114_1, arg_114_2):
	local var_114_0 = tf(arg_114_2)
	local var_114_1 = arg_114_0.candicates[arg_114_1]

	arg_114_0.UpdateRyzaItem(var_114_0.Find("IconBG"), var_114_1, True)

	local var_114_2 = var_114_1.count <= 0

	setActive(var_114_0.Find("IconBG/Lack"), var_114_2)
	onButton(arg_114_0, var_114_0, function()
		if var_114_2:
			var_114_1 = CreateShell(var_114_1)
			var_114_1.count = False

			arg_114_0.ShowItemDetail(var_114_1)
		else
			arg_114_0.DispalyChat({
				"ryza_atellier5",
				"ryza_atellier6",
				"ryza_atellier7"
			})
			pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/ryza_atellier_ui_2")

			local var_115_0 = arg_114_0.candicateTarget

			arg_114_0.HideCandicatePanel()
			seriesAsync({
				function(arg_116_0)
					arg_114_0.FillNodeAndPlayAnim(var_115_0, AtelierMaterial.New({
						count = 1,
						configId = var_114_1.GetConfigID()
					}), arg_116_0, True),
				function(arg_117_0)
					arg_114_0.DisPlayUnlockEffect(arg_117_0),
				function(arg_118_0)
					arg_114_0.UpdateFormulaDetail()
			}), SFX_PANEL)

def var_0_0.UpdateRyzaItem(arg_119_0, arg_119_1, arg_119_2, arg_119_3):
	local var_119_0 = "icon_frame_" .. arg_119_2.GetRarity()

	if arg_119_3:
		var_119_0 = var_119_0 .. "_small"

	arg_119_0.loader.GetSpriteQuiet(var_0_5, var_119_0, arg_119_1)
	arg_119_0.loader.GetSpriteQuiet(arg_119_2.GetIconPath(), "", arg_119_1.Find("Icon"))

	if not IsNil(arg_119_1.Find("Lv")):
		setText(arg_119_1.Find("Lv/Text"), arg_119_2.GetLevel())

	local var_119_1 = arg_119_2.GetProps()
	local var_119_2 = CustomIndexLayer.Clone2Full(arg_119_1.Find("List"), #var_119_1)

	for iter_119_0, iter_119_1 in ipairs(var_119_2):
		arg_119_0.loader.GetSpriteQuiet(var_0_5, "element_" .. var_0_2.ELEMENT_NAME[var_119_1[iter_119_0]], iter_119_1)

	if not IsNil(arg_119_1.Find("Text")):
		setText(arg_119_1.Find("Text"), arg_119_2.count)

def var_0_0.ShowItemDetail(arg_120_0, arg_120_1):
	arg_120_0.emit(AtelierMaterialDetailMediator.SHOW_DETAIL, arg_120_1)

local var_0_14 = 41
local var_0_15 = 5

def var_0_0.ShowCompositeConfirmWindow(arg_121_0):
	setActive(arg_121_0.layerCompositeConfirm, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_121_0.layerCompositeConfirm)

	local var_121_0 = 1
	local var_121_1 = {}
	local var_121_2 = {}

	_.each(arg_121_0.nodeList, function(arg_122_0)
		local var_122_0 = arg_122_0.Instance.GetConfigID()

		table.insert(var_121_1, {
			key = arg_122_0.Data.GetConfigID(),
			value = var_122_0
		})

		var_121_2[var_122_0] = (var_121_2[var_122_0] or 0) + 1)
	onButton(arg_121_0, arg_121_0.layerCompositeConfirm.Find("Window/Confirm"), function()
		arg_121_0.emit(GAME.COMPOSITE_ATELIER_RECIPE, var_121_1, var_121_0)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/ryza_atellier_ui_6"), SFX_PANEL)

	local var_121_3 = arg_121_0.activity.GetFormulas()[arg_121_0.contextData.formulaId]
	local var_121_4 = var_121_3.GetMaxLimit() != 1
	local var_121_5 = var_121_3.GetMaxLimit() > 0 and var_121_3.GetMaxLimit() - var_121_3.GetUsedCount() or 10000
	local var_121_6 = arg_121_0.activity.GetItems()

	for iter_121_0, iter_121_1 in pairs(var_121_2):
		local var_121_7 = var_121_6[iter_121_0] and var_121_6[iter_121_0].count or 0

		var_121_5 = math.min(var_121_5, math.floor(var_121_7 / iter_121_1))

	local var_121_8 = var_121_5
	local var_121_9 = {
		1,
		var_121_4 and var_121_8 or 1
	}
	local var_121_10 = Drop.New({
		type = var_121_3.GetProduction()[1],
		id = var_121_3.GetProduction()[2]
	})

	arg_121_0.UpdateRyzaDrop(arg_121_0.layerCompositeConfirm.Find("Window/Icon"), var_121_10)

	local var_121_11 = arg_121_0.layerCompositeConfirm.Find("Window/Counters")
	local var_121_12 = var_121_10.getConfig("name")

	setActive(var_121_11, var_121_4)

	if var_121_4:
		setAnchoredPosition(arg_121_0.layerCompositeConfirm.Find("Window/Icon"), {
			y = var_0_14
		})

		local function var_121_13()
			setText(var_121_11.Find("Number"), var_121_0)
			setText(arg_121_0.layerCompositeConfirm.Find("Window/Text"), i18n("ryza_composite_confirm", var_121_12, var_121_0))

		var_121_13()
		onButton(arg_121_0, var_121_11.Find("Plus"), function()
			local var_125_0 = var_121_0

			var_121_0 = var_121_0 + 1
			var_121_0 = math.clamp(var_121_0, var_121_9[1], var_121_9[2])

			if var_125_0 == var_121_0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("ryza_tip_max_composite_count"))

				return

			var_121_13())
		onButton(arg_121_0, var_121_11.Find("Minus"), function()
			var_121_0 = var_121_0 - 1
			var_121_0 = math.clamp(var_121_0, var_121_9[1], var_121_9[2])

			var_121_13())
		onButton(arg_121_0, var_121_11.Find("Plus10"), function()
			local var_127_0 = var_121_0

			var_121_0 = var_121_0 + 10
			var_121_0 = math.clamp(var_121_0, var_121_9[1], var_121_9[2])

			if var_127_0 == var_121_0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("ryza_tip_max_composite_count"))

				return

			var_121_13())
		onButton(arg_121_0, var_121_11.Find("Minus10"), function()
			var_121_0 = var_121_0 - 10
			var_121_0 = math.clamp(var_121_0, var_121_9[1], var_121_9[2])

			var_121_13())
	else
		setAnchoredPosition(arg_121_0.layerCompositeConfirm.Find("Window/Icon"), {
			y = var_0_15
		})
		setText(arg_121_0.layerCompositeConfirm.Find("Window/Text"), i18n("ryza_composite_confirm_single", var_121_12, var_121_0))

def var_0_0.HideCompositeConfirmWindow(arg_129_0):
	if not isActive(arg_129_0.layerCompositeConfirm):
		return

	pg.UIMgr.GetInstance().UnblurPanel(arg_129_0.layerCompositeConfirm, arg_129_0._tf)
	setActive(arg_129_0.layerCompositeConfirm, False)

	return True

local var_0_16 = "laisha_lianjin"

def var_0_0.OnCompositeResult(arg_130_0, arg_130_1):
	arg_130_0.LoadingOn()
	arg_130_0.DispalyChat({
		"ryza_atellier8",
		"ryza_atellier9"
	})

	local var_130_0 = 1.5
	local var_130_1 = 0.5

	arg_130_0.loader.GetPrefab("ui/" .. var_0_16, "", function(arg_131_0)
		pg.UIMgr.GetInstance().OverlayPanel(tf(arg_131_0), {
			weight = LayerWeightConst.SECOND_LAYER
		})
		setAnchoredPosition(arg_131_0, Vector2.zero)
		arg_130_0.managedTween(LeanTween.alphaCanvas, None, GetComponent(arg_130_0._tf, typeof(CanvasGroup)), 0, var_130_0).setFrom(1)
		arg_130_0.managedTween(LeanTween.alphaCanvas, None, GetComponent(arg_130_0.top, typeof(CanvasGroup)), 0, var_130_0).setFrom(1)
		arg_130_0.managedTween(LeanTween.alphaCanvas, None, GetComponent(arg_130_0.layerCompositeConfirm, typeof(CanvasGroup)), 0, var_130_0).setFrom(1)
		arg_130_0.managedTween(LeanTween.delayedCall, function()
			arg_130_0.HideCompositeConfirmWindow()
			setCanvasGroupAlpha(arg_130_0.layerCompositeConfirm, 1)
			arg_130_0.CleanNodeInstance()
			arg_130_0.ShowCompositeResult(arg_130_1)
			arg_130_0.DispalyChat({
				"ryza_atellier10",
				"ryza_atellier11"
			})
			arg_130_0.managedTween(LeanTween.alphaCanvas, None, GetComponent(arg_130_0._tf, typeof(CanvasGroup)), 1, var_130_1).setFrom(0)
			arg_130_0.managedTween(LeanTween.alphaCanvas, None, GetComponent(arg_130_0.top, typeof(CanvasGroup)), 1, var_130_1).setFrom(0)
			arg_130_0.managedTween(LeanTween.alphaCanvas, None, GetOrAddComponent(arg_130_0.layerCompositeResult, typeof(CanvasGroup)), 1, var_130_1).setFrom(0)
			arg_130_0.managedTween(LeanTween.delayedCall, function()
				arg_130_0.LoadingOff()
				pg.UIMgr.GetInstance().UnOverlayPanel(tf(arg_131_0), arg_130_0._tf)
				arg_130_0.loader.ClearRequest("CompositeResult"), go(arg_130_0.layerCompositeResult), var_130_1, None), go(arg_130_0.layerCompositeResult), var_130_0, None), "CompositeResult")

def var_0_0.ShowCompositeResult(arg_134_0, arg_134_1):
	setActive(arg_134_0.layerCompositeResult, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_134_0.layerCompositeResult)

	local var_134_0 = arg_134_1[1]

	arg_134_0.UpdateRyzaDrop(arg_134_0.layerCompositeResult.Find("Window/Icon"), var_134_0)
	setScrollText(arg_134_0.layerCompositeResult.Find("Window/NameBG/Rect/Name"), var_134_0.getName())
	setText(arg_134_0.layerCompositeResult.Find("Window/CountBG/Text"), var_134_0.count)

def var_0_0.HideCompositeResult(arg_135_0):
	if not isActive(arg_135_0.layerCompositeResult):
		return

	pg.UIMgr.GetInstance().UnblurPanel(arg_135_0.layerCompositeResult, arg_135_0._tf)
	setActive(arg_135_0.layerCompositeResult, False)

	if pg.NewStoryMgr.GetInstance().IsPlayed("NG0032"):
		pg.SystemGuideMgr.GetInstance().PlayByGuideId("NG0033", {
			2
		})

	return True

def var_0_0.ShowStoreHouseWindow(arg_136_0):
	setActive(arg_136_0.layerStoreHouse, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_136_0.layerStoreHouse)

	local var_136_0 = _.filter(_.values(arg_136_0.activity.GetItems()), function(arg_137_0)
		return arg_137_0.count > 0)

	table.sort(var_136_0, function(arg_138_0, arg_138_1)
		return arg_138_0.GetConfigID() < arg_138_1.GetConfigID())
	setActive(arg_136_0.layerStoreHouse.Find("Window/Empty"), #var_136_0 == 0)
	setActive(arg_136_0.layerStoreHouse.Find("Window/ScrollView"), #var_136_0 > 0)

	if #var_136_0 == 0:
		return

	function arg_136_0.storehouseRect.onUpdateItem(arg_139_0, arg_139_1)
		arg_139_0 = arg_139_0 + 1

		local var_139_0 = tf(arg_139_1)
		local var_139_1 = var_136_0[arg_139_0]

		arg_136_0.UpdateRyzaItem(var_139_0.Find("IconBG"), var_139_1)
		setScrollText(var_139_0.Find("NameBG/Rect/Name"), var_139_1.GetName())
		onButton(arg_136_0, var_139_0, function()
			arg_136_0.ShowItemDetail(var_139_1), SFX_PANEL)

	arg_136_0.storehouseRect.SetTotalCount(#var_136_0)

def var_0_0.CloseStoreHouseWindow(arg_141_0):
	arg_141_0.contextData.showStoreHouse = None

	return arg_141_0.HideStoreHouseWindow()

def var_0_0.HideStoreHouseWindow(arg_142_0):
	if not isActive(arg_142_0.layerStoreHouse):
		return

	pg.UIMgr.GetInstance().UnblurPanel(arg_142_0.layerStoreHouse, arg_142_0._tf)
	setActive(arg_142_0.layerStoreHouse, False)

	return True

def var_0_0.ShowMaterialsPreview(arg_143_0):
	setActive(arg_143_0.layerMaterialsPreview, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_143_0.layerMaterialsPreview)

	local var_143_0 = arg_143_0.activity.GetItems()
	local var_143_1 = arg_143_0.activity.GetFormulas()[arg_143_0.contextData.formulaId]
	local var_143_2 = AtelierMaterial.bindConfigTable()
	local var_143_3 = {}
	local var_143_4 = {}
	local var_143_5 = {}

	local function var_143_6(arg_144_0)
		local var_144_0 = var_143_5[arg_144_0.GetConfigID()] or Clone(var_143_0[arg_144_0.GetConfigID()])

		assert(var_144_0, "Using Unexist material")

		var_144_0.count = var_144_0.count - 1
		var_143_5[arg_144_0.GetConfigID()] = var_144_0

	_.each(arg_143_0.nodeList, function(arg_145_0)
		local var_145_0 = arg_145_0.Data

		if var_145_0.GetType() == var_0_2.TYPE.BASE or var_145_0.GetType() == var_0_2.TYPE.SAIREN:
			local var_145_1 = var_145_0.GetLimitItemID()
			local var_145_2 = var_143_5[var_145_1] or var_143_0[var_145_1]

			if var_145_2 and var_145_2.count > 0:
				local var_145_3 = AtelierMaterial.New({
					configId = var_145_1
				})

				var_145_3.count = False

				table.insert(var_143_3, var_145_3)
				var_143_6(var_145_2)
			else
				local var_145_4 = AtelierMaterial.New({
					configId = var_145_1
				})

				var_145_4.count = False

				table.insert(var_143_4, var_145_4))

	local function var_143_7(arg_146_0)
		if arg_146_0.Instance:
			local var_146_0 = AtelierMaterial.New({
				configId = arg_146_0.Instance.GetConfigID()
			})

			var_146_0.count = False

			table.insert(var_143_3, var_146_0)
			var_143_6(arg_146_0.Instance)

			return

		local var_146_1 = arg_146_0.Data
		local var_146_2

		for iter_146_0, iter_146_1 in ipairs(var_143_2.all):
			local var_146_3 = var_143_5[iter_146_1] or var_143_0[iter_146_1] or AtelierMaterial.New({
				configId = iter_146_1
			})

			if var_146_3.IsNormal() and var_146_1.CanUseMaterial(var_146_3, var_143_1):
				var_146_2 = var_146_2 or iter_146_1

				if var_146_3.count > 0:
					local var_146_4 = AtelierMaterial.New({
						configId = iter_146_1
					})

					var_146_4.count = False

					table.insert(var_143_3, var_146_4)
					var_143_6(var_146_3)

					return

		local var_146_5 = AtelierMaterial.New({
			configId = var_146_2
		})

		var_146_5.count = False

		table.insert(var_143_4, var_146_5)

	_.each(arg_143_0.nodeList, function(arg_147_0)
		if arg_147_0.Data.GetType() == var_0_2.TYPE.NORMAL:
			var_143_7(arg_147_0))
	_.each(arg_143_0.nodeList, function(arg_148_0)
		if arg_148_0.Data.GetType() == var_0_2.TYPE.ANY:
			var_143_7(arg_148_0))

	local function var_143_8(arg_149_0, arg_149_1)
		return arg_149_0.GetConfigID() < arg_149_1.GetConfigID()

	table.sort(var_143_3, var_143_8)
	table.sort(var_143_4, var_143_8)

	local function var_143_9()
		local var_150_0 = arg_143_0.layerMaterialsPreview.Find("Frame/Scroll/Content/Owned/List")

		setActive(var_150_0.parent, #var_143_3 > 0)

		if #var_143_3 == 0:
			return

		local var_150_1 = CustomIndexLayer.Clone2Full(var_150_0, #var_143_3)

		table.Foreach(var_150_1, function(arg_151_0, arg_151_1)
			local var_151_0 = var_143_3[arg_151_0]

			arg_143_0.UpdateRyzaItem(arg_151_1.Find("IconBG"), var_151_0, True)
			onButton(arg_143_0, arg_151_1, function()
				arg_143_0.ShowItemDetail(var_151_0), SFX_PANEL))

	local function var_143_10()
		local var_153_0 = arg_143_0.layerMaterialsPreview.Find("Frame/Scroll/Content/Lack/List")

		setActive(var_153_0.parent, #var_143_4 > 0)

		if #var_143_4 == 0:
			return

		local var_153_1 = CustomIndexLayer.Clone2Full(var_153_0, #var_143_4)

		table.Foreach(var_153_1, function(arg_154_0, arg_154_1)
			local var_154_0 = var_143_4[arg_154_0]

			arg_143_0.UpdateRyzaItem(arg_154_1.Find("IconBG"), var_154_0, True)
			onButton(arg_143_0, arg_154_1, function()
				arg_143_0.ShowItemDetail(var_154_0), SFX_PANEL))

	var_143_9()
	var_143_10()

def var_0_0.HideMaterialsPreview(arg_156_0):
	if not isActive(arg_156_0.layerMaterialsPreview):
		return

	pg.UIMgr.GetInstance().UnblurPanel(arg_156_0.layerMaterialsPreview, arg_156_0._tf)
	setActive(arg_156_0.layerMaterialsPreview, False)

	return True

def var_0_0.OnReceiveFormualRequest(arg_157_0, arg_157_1):
	arg_157_0.HideCandicatePanel()
	arg_157_0.HideCompositeConfirmWindow()
	arg_157_0.HideCompositeResult()
	arg_157_0.HideMaterialsPreview()
	arg_157_0.CloseStoreHouseWindow()
	arg_157_0.HideFormulaList()

	local var_157_0 = arg_157_0.activity.GetFormulas()[arg_157_1]

	arg_157_0.ShowFormulaDetail(var_157_0)

def var_0_0.DispalyChat(arg_158_0, arg_158_1):
	arg_158_0.HideChat()
	setActive(arg_158_0.chat, True)

	arg_158_0.chatTween = LeanTween.delayedCall(go(arg_158_0.chat), 4, System.Action(function()
		arg_158_0.HideChat())).uniqueId

	local var_158_0 = arg_158_1[math.random(#arg_158_1)]
	local var_158_1 = pg.gametip.ryza_composite_words.tip
	local var_158_2 = _.detect(var_158_1, function(arg_160_0)
		return arg_160_0[1] == var_158_0)
	local var_158_3 = var_158_2 and var_158_2[2]

	setText(arg_158_0.chat.Find("Text"), var_158_3)

	local var_158_4 = 1090001
	local var_158_5 = "event./cv/" .. var_158_4 .. "/" .. var_158_0

	arg_158_0.PlaySound(var_158_5)

def var_0_0.HideChat(arg_161_0):
	if arg_161_0.chatTween:
		LeanTween.cancel(arg_161_0.chatTween)

		arg_161_0.chatTween = None

	setActive(arg_161_0.chat, False)

def var_0_0.PlaySound(arg_162_0, arg_162_1, arg_162_2):
	if not arg_162_0.playbackInfo or arg_162_1 != arg_162_0.prevCvPath or arg_162_0.playbackInfo.channelPlayer == None:
		arg_162_0.StopSound()
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(arg_162_1, function(arg_163_0)
			if arg_163_0:
				arg_162_0.playbackInfo = arg_163_0

				arg_162_0.playbackInfo.SetIgnoreAutoUnload(True)

				if arg_162_2:
					arg_162_2(arg_162_0.playbackInfo.cueInfo)
			elif arg_162_2:
				arg_162_2())

		arg_162_0.prevCvPath = arg_162_1

		if arg_162_0.playbackInfo == None:
			return None

		return arg_162_0.playbackInfo.cueInfo
	elif arg_162_0.playbackInfo:
		arg_162_0.playbackInfo.PlaybackStop()
		arg_162_0.playbackInfo.SetStartTimeAndPlay()

		if arg_162_2:
			arg_162_2(arg_162_0.playbackInfo.cueInfo)

		return arg_162_0.playbackInfo.cueInfo
	elif arg_162_2:
		arg_162_2()

	return None

def var_0_0.StopSound(arg_164_0):
	if arg_164_0.playbackInfo:
		pg.CriMgr.GetInstance().StopPlaybackInfoForce(arg_164_0.playbackInfo)
		arg_164_0.playbackInfo.SetIgnoreAutoUnload(False)

def var_0_0.ClearSound(arg_165_0):
	arg_165_0.StopSound()

	if arg_165_0.playbackInfo:
		arg_165_0.playbackInfo.Dispose()

		arg_165_0.playbackInfo = None

def var_0_0.LoadingOn(arg_166_0):
	if arg_166_0.animating:
		return

	arg_166_0.animating = True

	pg.UIMgr.GetInstance().LoadingOn(False)

def var_0_0.LoadingOff(arg_167_0):
	if not arg_167_0.animating:
		return

	pg.UIMgr.GetInstance().LoadingOff()

	arg_167_0.animating = False

def var_0_0.willExit(arg_168_0):
	arg_168_0.loader.Clear()
	arg_168_0.LoadingOff()
	arg_168_0.HideChat()
	arg_168_0.ClearSound()
	arg_168_0.HideStoreHouseWindow()
	arg_168_0.HideMaterialsPreview()
	arg_168_0.HideCompositeResult()
	arg_168_0.HideCompositeConfirmWindow()
	arg_168_0.HideCandicatePanel()
	arg_168_0.HideFormulaDetail()
	arg_168_0.HideFormulaList()
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_168_0.top, arg_168_0._tf)

	if arg_168_0.nodePools:
		for iter_168_0, iter_168_1 in pairs(arg_168_0.nodePools):
			iter_168_1.ClearItems()

return var_0_0
