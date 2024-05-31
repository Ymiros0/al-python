local var_0_0 = class("EquipmentTraceBackLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "EquipmentTraceBackUI"

def var_0_0.init(arg_2_0):
	local var_2_0 = arg_2_0._tf.Find("Adapt/Left/Operation")

	arg_2_0.sortOrderBtn = var_2_0.Find("Bar1")
	arg_2_0.orderText = var_2_0.Find("OrderText")
	arg_2_0.sortBarBtn = var_2_0.Find("Bar2")
	arg_2_0.sortImg = var_2_0.Find("SortImg")
	arg_2_0.sortBar = arg_2_0._tf.Find("Adapt/Left/SortBar")

	setActive(arg_2_0.sortBar, False)

	arg_2_0.equipLayout = arg_2_0._tf.Find("Adapt/Left/Scroll View")
	arg_2_0.equipLayoutScroll = arg_2_0.equipLayout.GetComponent("LScrollRect")
	arg_2_0.equipLayoutContent = arg_2_0.equipLayout.Find("Viewport/Content")
	arg_2_0.equipLayoutContent.GetComponent(typeof(GridLayoutGroup)).constraintCount = 6

	local var_2_1 = arg_2_0._tf.Find("Adapt/Right")

	arg_2_0.sourceEquip = var_2_1.Find("Source")
	arg_2_0.sourceEquipStatus = var_2_1.Find("Status")
	arg_2_0.formulaWire = var_2_1.Find("Wire")
	arg_2_0.targetEquip = var_2_1.Find("Target")
	arg_2_0.confirmBtn = var_2_1.Find("ConfirmBtn")
	arg_2_0.cancelBtn = var_2_1.Find("CancelBtn")
	arg_2_0.materialLayout = var_2_1.Find("Scroll View")
	arg_2_0.materialLayoutContent = arg_2_0.materialLayout.Find("Viewport/Content")
	arg_2_0.goldText = var_2_1.Find("GoldText")

	setText(var_2_0.Find("Field/Text"), i18n("equipment_upgrade_quick_interface_source_chosen"))
	setText(var_2_1.Find("Text"), i18n("equipment_upgrade_quick_interface_materials_consume"))

	arg_2_0.loader = AutoLoader.New()

var_0_0.SortType = {
	Rarity = "rarity",
	Strengthen = "level",
	Type = "type"
}

local var_0_1 = {
	var_0_0.SortType.Rarity,
	var_0_0.SortType.Type,
	var_0_0.SortType.Strengthen
}
local var_0_2 = {
	[var_0_0.SortType.Rarity] = "rarity",
	[var_0_0.SortType.Type] = "type",
	[var_0_0.SortType.Strengthen] = "strengthen"
}

var_0_0.SortOrder = {
	Descend = 0,
	Ascend = 1
}

local var_0_3 = {
	[var_0_0.SortOrder.Descend] = "word_desc",
	[var_0_0.SortOrder.Ascend] = "word_asc"
}

def var_0_0.SetEnv(arg_3_0, arg_3_1):
	arg_3_0.env = arg_3_1

def var_0_0.GetAllPaths(arg_4_0, arg_4_1):
	local var_4_0 = {}
	local var_4_1 = {
		{
			arg_4_1
		}
	}

	while #var_4_1 > 0:
		local var_4_2 = table.remove(var_4_1, 1)
		local var_4_3 = EquipmentProxy.GetTransformSources(var_4_2[1])

		for iter_4_0, iter_4_1 in ipairs(var_4_3):
			local var_4_4 = pg.equip_upgrade_data[iter_4_1].upgrade_from
			local var_4_5 = var_4_2[2] and Clone(var_4_2[2]) or {}

			table.insert(var_4_5, 1, iter_4_1)
			table.insert(var_4_1, {
				var_4_4,
				var_4_5
			})

			local var_4_6 = arg_4_0.env.tracebackHelper.GetEquipmentTransformCandicates(var_4_4)

			if #var_4_6 > 0:
				table.insertto(var_4_0, _.map(var_4_6, function(arg_5_0)
					return {
						source = arg_5_0,
						formulas = var_4_5
					}))

	return var_4_0

def var_0_0.UpdateSourceEquipmentPaths(arg_6_0):
	arg_6_0.totalPaths = arg_6_0.GetAllPaths(arg_6_0.contextData.TargetEquipmentId)

	if arg_6_0.contextData.sourceEquipmentInstance:
		local var_6_0 = _.detect(arg_6_0.totalPaths, function(arg_7_0)
			return EquipmentTransformUtil.SameDrop(arg_7_0.source, arg_6_0.contextData.sourceEquipmentInstance))

		arg_6_0.contextData.sourceEquipmentInstance = var_6_0 and var_6_0.source or None

def var_0_0.UpdateSort(arg_8_0):
	for iter_8_0, iter_8_1 in ipairs(arg_8_0.totalPaths):
		iter_8_1.isSourceEnough = iter_8_1.source.type != DROP_TYPE_ITEM or iter_8_1.source.template.count >= iter_8_1.source.composeCfg.material_num
		iter_8_1.isMaterialEnough = iter_8_1.isSourceEnough and EquipmentTransformUtil.CheckTransformFormulasSucceed(iter_8_1.formulas, iter_8_1.source)

	table.sort(arg_8_0.totalPaths, function(arg_9_0, arg_9_1)
		if arg_9_0.isSourceEnough != arg_9_1.isSourceEnough:
			return arg_9_0.isSourceEnough

		if arg_9_0.isMaterialEnough != arg_9_1.isMaterialEnough:
			return arg_9_0.isMaterialEnough

		if arg_9_0.source.type != arg_9_1.source.type:
			return arg_9_0.source.type < arg_9_1.source.type

		local var_9_0 = arg_8_0.contextData.sortType
		local var_9_1 = arg_8_0.contextData.sortOrder == var_0_0.SortOrder.Descend and 1 or -1

		if arg_9_0.source.type == DROP_TYPE_ITEM:
			return (arg_9_0.source.template.id - arg_9_1.source.template.id) * var_9_1 > 0

		local var_9_2 = arg_9_0.source.template.shipId or -1
		local var_9_3 = arg_9_1.source.template.shipId or -1

		if var_9_2 != var_9_3:
			return var_9_2 < var_9_3

		local var_9_4 = arg_9_0.source.template.getConfigTable()[var_9_0] - arg_9_1.source.template.getConfigTable()[var_9_0]

		var_9_4 = var_9_4 != 0 and var_9_4 or arg_9_0.source.template.id - arg_9_1.source.template.id

		return var_9_4 * var_9_1 > 0)
	setText(arg_8_0.orderText, i18n(var_0_3[arg_8_0.contextData.sortOrder]))
	arg_8_0.loader.GetSprite("ui/equipmenttracebackui_atlas", var_0_2[arg_8_0.contextData.sortType], arg_8_0.sortImg)

def var_0_0.didEnter(arg_10_0):
	function arg_10_0.equipLayoutScroll.onUpdateItem(arg_11_0, arg_11_1)
		arg_10_0.UpdateSourceListItem(arg_11_0, tf(arg_11_1))
		TweenItemAlphaAndWhite(arg_11_1)

	function arg_10_0.equipLayoutScroll.onReturnItem(arg_12_0, arg_12_1)
		ClearTweenItemAlphaAndWhite(arg_12_1)

	onButton(arg_10_0, arg_10_0.sortBarBtn, function()
		local var_13_0 = isActive(arg_10_0.sortBar)

		setActive(arg_10_0.sortBar, not var_13_0), SFX_PANEL)

	for iter_10_0 = 1, arg_10_0.sortBar.childCount:
		local var_10_0 = arg_10_0.sortBar.GetChild(iter_10_0 - 1)

		onButton(arg_10_0, var_10_0, function()
			arg_10_0.contextData.sortType = var_0_1[iter_10_0]

			arg_10_0.UpdateSort()
			arg_10_0.UpdateSourceList()
			setActive(arg_10_0.sortBar, False), SFX_PANEL)

	onButton(arg_10_0, arg_10_0.sortOrderBtn, function()
		arg_10_0.contextData.sortOrder = var_0_0.SortOrder.Ascend - arg_10_0.contextData.sortOrder

		arg_10_0.UpdateSort()
		arg_10_0.UpdateSourceList(), SFX_PANEL)
	onButton(arg_10_0, arg_10_0.cancelBtn, function()
		arg_10_0.closeView(), SFX_CANCEL)
	onButton(arg_10_0, arg_10_0.confirmBtn, function()
		local var_17_0 = arg_10_0.contextData.sourceEquipmentInstance

		if not var_17_0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_upgrade_quick_interface_feedback_source_chosen"))

			return

		if not EquipmentTransformUtil.CheckTransformFormulasSucceed(arg_10_0.contextData.sourceEquipmentFormulaList, var_17_0):
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_upgrade_feedback_lack_of_materials"))

			return

		arg_10_0.emit(EquipmentTraceBackMediator.TRANSFORM_EQUIP, var_17_0, arg_10_0.contextData.sourceEquipmentFormulaList), SFX_PANEL)

	arg_10_0.contextData.sortOrder = arg_10_0.contextData.sortOrder or var_0_0.SortOrder.Descend
	arg_10_0.contextData.sortType = arg_10_0.contextData.sortType or var_0_0.SortType.Rarity

	arg_10_0.UpdateSourceEquipmentPaths()
	arg_10_0.UpdateSort()
	arg_10_0.UpdateSourceList()
	arg_10_0.UpdateFormula()
	updateDrop(arg_10_0.targetEquip, {
		type = DROP_TYPE_EQUIP,
		id = arg_10_0.contextData.TargetEquipmentId
	})
	pg.UIMgr.GetInstance().BlurPanel(arg_10_0._tf, True)

def var_0_0.UpdateSourceList(arg_18_0):
	arg_18_0.lastSourceItem = None

	arg_18_0.equipLayoutScroll.SetTotalCount(#arg_18_0.totalPaths)

def var_0_0.UpdateSourceListItem(arg_19_0, arg_19_1, arg_19_2):
	local var_19_0 = arg_19_0.totalPaths[arg_19_1 + 1].source
	local var_19_1 = var_19_0.template

	updateDrop(arg_19_2.Find("Item"), var_19_0)
	setText(arg_19_2.Find("Item/icon_bg/count"), var_19_1.count)
	setActive(arg_19_2.Find("EquipShip"), var_19_1.shipId)
	setActive(arg_19_2.Find("Selected"), False)

	if var_19_0 == arg_19_0.contextData.sourceEquipmentInstance:
		arg_19_0.lastSourceItem = arg_19_2

		setActive(arg_19_2.Find("Selected"), True)

	setActive(arg_19_2.Find("Item/mask"), False)

	if var_19_0.type == DROP_TYPE_ITEM:
		local var_19_2 = arg_19_2.Find("Item/icon_bg/count")
		local var_19_3 = var_19_1.count
		local var_19_4 = var_19_0.composeCfg.material_num
		local var_19_5 = var_19_4 <= var_19_3
		local var_19_6 = setColorStr(var_19_3 .. "/" .. var_19_4, var_19_5 and COLOR_WHITE or COLOR_RED)

		setText(var_19_2, var_19_6)
		setActive(arg_19_2.Find("Item/mask"), not var_19_5)

	if var_19_1.shipId:
		local var_19_7 = getProxy(BayProxy).getShipById(var_19_1.shipId)

		arg_19_0.loader.GetSprite("qicon/" .. var_19_7.getPainting(), "", arg_19_2.Find("EquipShip/Image"))

	arg_19_2.Find("Mask/NameText").GetComponent(typeof(ScrollText)).SetText(var_19_1.getConfig("name"))
	onButton(arg_19_0, arg_19_2.Find("Item"), function()
		if var_19_0.type == DROP_TYPE_ITEM and not (var_19_0.template.count >= var_19_0.composeCfg.material_num):
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_upgrade_feedback_lack_of_fragment", var_19_0.template.getConfig("name")))

			return

		if arg_19_0.lastSourceItem:
			setActive(arg_19_0.lastSourceItem.Find("Selected"), False)

		arg_19_0.lastSourceItem = arg_19_2

		setActive(arg_19_2.Find("Selected"), True)

		arg_19_0.contextData.sourceEquipmentInstance = var_19_0
		arg_19_0.contextData.sourceEquipmentFormulaList = arg_19_0.totalPaths[arg_19_1 + 1].formulas

		arg_19_0.UpdateFormula(), SFX_PANEL)

def var_0_0.UpdatePlayer(arg_21_0, arg_21_1):
	arg_21_0.player = arg_21_1

	arg_21_0.UpdateConsumeComparer()

def var_0_0.UpdateConsumeComparer(arg_22_0):
	local var_22_0 = 0
	local var_22_1 = 0
	local var_22_2 = True

	if arg_22_0.contextData.sourceEquipmentInstance:
		var_22_2, var_22_0, var_22_1 = EquipmentTransformUtil.CheckTransformEnoughGold(arg_22_0.contextData.sourceEquipmentFormulaList, arg_22_0.contextData.sourceEquipmentInstance)

	local var_22_3 = setColorStr(var_22_0, var_22_2 and COLOR_WHITE or COLOR_RED)

	if var_22_1 > 0:
		var_22_3 = var_22_3 .. setColorStr(" + " .. var_22_1, var_22_2 and COLOR_GREEN or COLOR_RED)

	arg_22_0.goldText.GetComponent(typeof(Text)).text = var_22_3

def var_0_0.UpdateFormula(arg_23_0):
	local var_23_0 = arg_23_0.contextData.sourceEquipmentInstance

	setActive(arg_23_0.sourceEquipStatus, not var_23_0)
	setActive(arg_23_0.sourceEquip, var_23_0)
	setActive(arg_23_0.materialLayout, var_23_0)

	if var_23_0:
		updateDrop(arg_23_0.sourceEquip, var_23_0)

		local var_23_1 = arg_23_0.sourceEquip.Find("icon_bg/count")
		local var_23_2 = ""

		if var_23_0 and var_23_0.type == DROP_TYPE_ITEM:
			var_23_2 = var_23_0.composeCfg.material_num

		setText(var_23_1, var_23_2)

		local var_23_3 = arg_23_0.contextData.sourceEquipmentFormulaList
		local var_23_4 = not var_23_3 or #var_23_3 <= 1

		arg_23_0.loader.GetSprite("ui/equipmenttracebackui_atlas", var_23_4 and "wire" or "wire2", arg_23_0.formulaWire)
		arg_23_0.UpdateFormulaMaterials()
	else
		arg_23_0.UpdateConsumeComparer()

def var_0_0.UpdateFormulaMaterials(arg_24_0):
	if not arg_24_0.contextData.sourceEquipmentFormulaList:
		return

	local var_24_0 = {}
	local var_24_1 = 0

	for iter_24_0, iter_24_1 in ipairs(arg_24_0.contextData.sourceEquipmentFormulaList):
		local var_24_2 = pg.equip_upgrade_data[iter_24_1]

		for iter_24_2, iter_24_3 in ipairs(var_24_2.material_consume):
			var_24_0[iter_24_3[1]] = (var_24_0[iter_24_3[1]] or 0) + iter_24_3[2]

		var_24_1 = var_24_1 + var_24_2.coin_consume

	local var_24_3 = {}

	for iter_24_4, iter_24_5 in pairs(var_24_0):
		table.insert(var_24_3, {
			id = iter_24_4,
			count = iter_24_5
		})

	table.sort(var_24_3, function(arg_25_0, arg_25_1)
		return arg_25_0.id > arg_25_1.id)

	arg_24_0.consumeMaterials = var_24_3

	UIItemList.StaticAlign(arg_24_0.materialLayoutContent, arg_24_0.materialLayoutContent.GetChild(0), #arg_24_0.consumeMaterials, function(arg_26_0, arg_26_1, arg_26_2)
		if arg_26_0 == UIItemList.EventUpdate:
			arg_24_0.UpdateFormulaMaterialItem(arg_26_1, arg_26_2))
	Canvas.ForceUpdateCanvases()

	local var_24_4 = arg_24_0.materialLayoutContent.rect.height < arg_24_0.materialLayout.rect.height

	arg_24_0.materialLayout.GetComponent(typeof(ScrollRect)).enabled = not var_24_4

	setActive(arg_24_0.materialLayout.Find("Scrollbar"), not var_24_4)

	if var_24_4:
		arg_24_0.materialLayoutContent.anchoredPosition = Vector2.zero

	arg_24_0.UpdateConsumeComparer()

def var_0_0.UpdateFormulaMaterialItem(arg_27_0, arg_27_1, arg_27_2):
	local var_27_0 = arg_27_0.consumeMaterials[arg_27_1 + 1]
	local var_27_1 = {
		type = DROP_TYPE_ITEM,
		id = var_27_0.id
	}

	updateDrop(arg_27_2.Find("Item"), var_27_1)

	local var_27_2 = getProxy(BagProxy).getItemCountById(var_27_0.id)

	setText(arg_27_2.Find("Count"), setColorStr(var_27_0.count, var_27_2 >= var_27_0.count and COLOR_GREEN or COLOR_RED) .. "/" .. var_27_2)
	onButton(arg_27_0, arg_27_2.Find("Item"), function()
		arg_27_0.emit(var_0_0.ON_DROP, var_27_1))

def var_0_0.willExit(arg_29_0):
	arg_29_0.loader.Clear()
	pg.UIMgr.GetInstance().UnblurPanel(arg_29_0._tf)

return var_0_0
