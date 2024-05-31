local var_0_0 = class("SpWeaponStoreHouseScene", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "SpWeaponStoreHouseUI"

def var_0_0.setEquipments(arg_2_0, arg_2_1):
	arg_2_0.equipmentVOs = arg_2_1

def var_0_0.SetCraftList(arg_3_0, arg_3_1):
	arg_3_0.craftList = arg_3_1

local var_0_1 = require("view.equipment.SpWeaponSortCfg")

def var_0_0.init(arg_4_0):
	arg_4_0.topItems = arg_4_0.findTF("topItems")
	arg_4_0.equipmentView = arg_4_0.findTF("ScrollView")
	arg_4_0.equipmentsGrid = arg_4_0.equipmentView.Find("Viewport/Content/StoreHouse/Grid")
	arg_4_0.craftsGrid = arg_4_0.equipmentView.Find("Viewport/Content/Craft/Grid")

	setActive(arg_4_0.equipmentView.Find("Template"), False)

	arg_4_0.blurPanel = arg_4_0.findTF("blur_panel")
	arg_4_0.topPanel = arg_4_0.findTF("adapt/top", arg_4_0.blurPanel)
	arg_4_0.indexBtn = arg_4_0.findTF("buttons/index_button", arg_4_0.topPanel)
	arg_4_0.sortBtn = arg_4_0.findTF("buttons/sort_button", arg_4_0.topPanel)
	arg_4_0.sortPanel = arg_4_0.findTF("sort", arg_4_0.topItems)
	arg_4_0.sortContain = arg_4_0.findTF("adapt/mask/panel", arg_4_0.sortPanel)
	arg_4_0.sortTpl = arg_4_0.findTF("tpl", arg_4_0.sortContain)

	setActive(arg_4_0.sortTpl, False)

	local var_4_0
	local var_4_1 = getProxy(SettingsProxy)

	if NotchAdapt.CheckNotchRatio == 2 or not var_4_1.CheckLargeScreen():
		var_4_0 = arg_4_0.equipmentView.rect.width > 2000
	else
		var_4_0 = NotchAdapt.CheckNotchRatio >= 2

	arg_4_0.equipmentsGrid.GetComponent(typeof(GridLayoutGroup)).constraintCount = var_4_0 and 8 or 7
	arg_4_0.craftsGrid.GetComponent(typeof(GridLayoutGroup)).constraintCount = var_4_0 and 8 or 7
	arg_4_0.decBtn = findTF(arg_4_0.topPanel, "buttons/dec_btn")
	arg_4_0.sortImgAsc = findTF(arg_4_0.decBtn, "asc")
	arg_4_0.sortImgDec = findTF(arg_4_0.decBtn, "desc")
	arg_4_0.filterBusyToggle = arg_4_0._tf.Find("blur_panel/adapt/left_length/frame/toggle_equip")

	setActive(arg_4_0.filterBusyToggle, False)

	arg_4_0.bottomBack = arg_4_0.findTF("adapt/bottom_back", arg_4_0.topItems)
	arg_4_0.capacityTF = arg_4_0.findTF("bottom_left/tip/capcity/Text", arg_4_0.bottomBack)
	arg_4_0.tipTF = arg_4_0.findTF("bottom_left/tip", arg_4_0.bottomBack)
	arg_4_0.tip = arg_4_0.tipTF.Find("label")
	arg_4_0.helpBtn = arg_4_0.findTF("adapt/help_btn", arg_4_0.topItems)

	setActive(arg_4_0.helpBtn, True)

	arg_4_0.backBtn = arg_4_0.findTF("blur_panel/adapt/top/back_btn")
	arg_4_0.listEmptyTF = arg_4_0.findTF("empty")

	setActive(arg_4_0.listEmptyTF, False)

	arg_4_0.listEmptyTxt = arg_4_0.findTF("Text", arg_4_0.listEmptyTF)

	setText(arg_4_0.listEmptyTxt, i18n("list_empty_tip_storehouseui_equip"))
	setText(arg_4_0.equipmentView.Find("Viewport/Content/Craft/Banner/Text"), i18n("spweapon_ui_create"))
	setText(arg_4_0.equipmentView.Find("Viewport/Content/StoreHouse/Banner/Text"), i18n("spweapon_ui_storage"))

	arg_4_0.isEquipingOn = False
	arg_4_0.filterImportance = None

def var_0_0.setEquipmentUpdate(arg_5_0):
	arg_5_0.filterEquipment()
	arg_5_0.updateCapacity()

def var_0_0.didEnter(arg_6_0):
	onButton(arg_6_0, arg_6_0.helpBtn, function()
		local var_7_0 = pg.gametip.spweapon_help_storage.tip

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = var_7_0
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.backBtn, function()
		GetOrAddComponent(arg_6_0._tf, typeof(CanvasGroup)).interactable = False

		arg_6_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onToggle(arg_6_0, arg_6_0.sortBtn, function(arg_9_0)
		if arg_9_0:
			pg.UIMgr.GetInstance().OverlayPanel(arg_6_0.sortPanel, {
				groupName = LayerWeightConst.GROUP_EQUIPMENTSCENE
			})
			setActive(arg_6_0.sortPanel, True)
		else
			pg.UIMgr.GetInstance().UnOverlayPanel(arg_6_0.sortPanel, arg_6_0.topItems)
			setActive(arg_6_0.sortPanel, False), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.sortPanel, function()
		triggerToggle(arg_6_0.sortBtn, False), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.indexBtn, function()
		local var_11_0 = {
			indexDatas = Clone(arg_6_0.contextData.indexDatas),
			customPanels = {
				typeIndex = {
					mode = CustomIndexLayer.Mode.OR,
					options = IndexConst.SpWeaponTypeIndexs,
					names = IndexConst.SpWeaponTypeNames
				},
				rarityIndex = {
					mode = CustomIndexLayer.Mode.AND,
					options = IndexConst.SpWeaponRarityIndexs,
					names = IndexConst.SpWeaponRarityNames
				}
			},
			groupList = {
				{
					dropdown = False,
					titleTxt = "indexsort_type",
					titleENTxt = "indexsort_typeeng",
					tags = {
						"typeIndex"
					}
				},
				{
					dropdown = False,
					titleTxt = "indexsort_rarity",
					titleENTxt = "indexsort_rarityeng",
					tags = {
						"rarityIndex"
					}
				}
			},
			def callback:(arg_12_0)
				arg_6_0.contextData.indexDatas.typeIndex = arg_12_0.typeIndex
				arg_6_0.contextData.indexDatas.rarityIndex = arg_12_0.rarityIndex

				arg_6_0.filterEquipment()
		}

		arg_6_0.emit(SpWeaponStoreHouseMediator.OPEN_EQUIPMENT_INDEX, var_11_0), SFX_PANEL)

	local var_6_0 = arg_6_0.equipmentView.Find("Viewport/Content/Craft/Banner/Arrow")

	onToggle(arg_6_0, var_6_0, function(arg_13_0)
		arg_6_0.hideCraft = not arg_13_0

		arg_6_0.UpdateCraftCount(), SFX_PANEL, SFX_PANEL)

	local var_6_1 = arg_6_0.equipmentView.Find("Viewport/Content/StoreHouse/Banner/Arrow")

	onToggle(arg_6_0, var_6_1, function(arg_14_0)
		arg_6_0.hideSpweapon = not arg_14_0

		arg_6_0.updateEquipmentCount(), SFX_PANEL, SFX_PANEL)

	arg_6_0.equipmetItems = {}
	arg_6_0.craftItems = {}

	arg_6_0.initEquipments()

	arg_6_0.asc = arg_6_0.contextData.asc or False
	arg_6_0.contextData.sortData = arg_6_0.contextData.sortData or var_0_1.sort[1]
	arg_6_0.contextData.indexDatas = arg_6_0.contextData.indexDatas or {}

	arg_6_0.initSort()
	onToggle(arg_6_0, arg_6_0.filterBusyToggle, function(arg_15_0)
		arg_6_0.SetShowBusyFlag(arg_15_0)
		arg_6_0.filterEquipment(), SFX_PANEL)
	triggerToggle(arg_6_0.filterBusyToggle, arg_6_0.shipVO)
	pg.UIMgr.GetInstance().OverlayPanel(arg_6_0.blurPanel, {
		groupName = LayerWeightConst.GROUP_EQUIPMENTSCENE
	})
	pg.UIMgr.GetInstance().OverlayPanel(arg_6_0.topItems, {
		groupName = LayerWeightConst.GROUP_EQUIPMENTSCENE
	})

	local var_6_2 = arg_6_0.contextData.mode or StoreHouseConst.OVERVIEW

	arg_6_0.contextData.mode = var_6_2

	arg_6_0.updateCapacity()
	setActive(arg_6_0.tip, False)
	setActive(arg_6_0.capacityTF.parent, True)
	setActive(arg_6_0.filterBusyToggle, True)
	setActive(arg_6_0.indexBtn, True)
	setActive(arg_6_0.sortBtn, False)
	triggerToggle(var_6_0, True)
	triggerToggle(var_6_1, True)

def var_0_0.isDefaultStatus(arg_16_0):
	return (not arg_16_0.contextData.indexDatas.typeIndex or arg_16_0.contextData.indexDatas.typeIndex == IndexConst.SpWeaponTypeAll) and (not arg_16_0.contextData.indexDatas.rarityIndex or arg_16_0.contextData.indexDatas.rarityIndex == IndexConst.SpWeaponRarityAll)

def var_0_0.onBackPressed(arg_17_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	if isActive(arg_17_0.sortPanel):
		triggerButton(arg_17_0.sortPanel)
	else
		triggerButton(arg_17_0.backBtn)

def var_0_0.updateCapacity(arg_18_0):
	setText(arg_18_0.tip, "")

	local var_18_0 = getProxy(EquipmentProxy).GetSpWeaponCount()
	local var_18_1 = getProxy(EquipmentProxy).GetSpWeaponCapacity()

	setText(arg_18_0.capacityTF, var_18_0 .. "/" .. var_18_1)

def var_0_0.setShip(arg_19_0, arg_19_1):
	arg_19_0.shipVO = arg_19_1

def var_0_0.setPlayer(arg_20_0, arg_20_1):
	arg_20_0.player = arg_20_1

def var_0_0.initSort(arg_21_0):
	onButton(arg_21_0, arg_21_0.decBtn, function()
		arg_21_0.asc = not arg_21_0.asc
		arg_21_0.contextData.asc = arg_21_0.asc

		arg_21_0.filterEquipment())

	arg_21_0.sortButtons = {}

	eachChild(arg_21_0.sortContain, function(arg_23_0)
		setActive(arg_23_0, False))

	for iter_21_0, iter_21_1 in ipairs(var_0_1.sort):
		local var_21_0 = iter_21_0 <= arg_21_0.sortContain.childCount and arg_21_0.sortContain.GetChild(iter_21_0 - 1) or cloneTplTo(arg_21_0.sortTpl, arg_21_0.sortContain)

		setActive(var_21_0, True)
		setImageSprite(findTF(var_21_0, "Image"), GetSpriteFromAtlas("ui/equipmentui_atlas", iter_21_1.spr), True)
		onToggle(arg_21_0, var_21_0, function(arg_24_0)
			if arg_24_0:
				arg_21_0.contextData.sortData = iter_21_1

				arg_21_0.filterEquipment()
				triggerToggle(arg_21_0.sortBtn, False), SFX_PANEL)

		arg_21_0.sortButtons[iter_21_0] = var_21_0

def var_0_0.initEquipments(arg_25_0):
	arg_25_0.equipmentRect = UIItemList.New(arg_25_0.equipmentsGrid, arg_25_0.equipmentView.Find("Template"))

	arg_25_0.equipmentRect.make(function(arg_26_0, arg_26_1, arg_26_2)
		local var_26_0 = go(arg_26_2)

		if arg_26_0 == UIItemList.EventInit:
			arg_25_0.InitSpWeapon(var_26_0)
		elif arg_26_0 == UIItemList.EventUpdate:
			arg_25_0.UpdateSpWeapon(arg_26_1, var_26_0)
		elif arg_26_0 == UIItemList.EventExcess:
			arg_25_0.ReturnSpWeapon(arg_26_1, var_26_0))

	arg_25_0.craftRect = UIItemList.New(arg_25_0.craftsGrid, arg_25_0.equipmentView.Find("Template"))

	arg_25_0.craftRect.make(function(arg_27_0, arg_27_1, arg_27_2)
		local var_27_0 = go(arg_27_2)

		if arg_27_0 == UIItemList.EventInit:
			arg_25_0.InitCraftItem(var_27_0)
		elif arg_27_0 == UIItemList.EventUpdate:
			arg_25_0.UpdateCraftItem(arg_27_1, var_27_0)
		elif arg_27_0 == UIItemList.EventExcess:
			arg_25_0.ReturnCraftItem(arg_27_1, var_27_0))

def var_0_0.InitSpWeapon(arg_28_0, arg_28_1):
	local var_28_0 = SpWeaponItemView.New(arg_28_1)

	onButton(arg_28_0, var_28_0.unloadBtn, function()
		arg_28_0.emit(SpWeaponStoreHouseMediator.ON_UNEQUIP), SFX_PANEL)

	arg_28_0.equipmetItems[arg_28_1] = var_28_0

def var_0_0.UpdateSpWeapon(arg_30_0, arg_30_1, arg_30_2):
	local var_30_0 = arg_30_0.equipmetItems[arg_30_2]

	assert(var_30_0, "without init item")

	local var_30_1 = arg_30_0.loadEquipmentVOs[arg_30_1 + 1]

	var_30_0.update(var_30_1)

	if not var_30_1 or var_30_1.mask:
		removeOnButton(var_30_0.go)
	else
		onButton(arg_30_0, var_30_0.go, function()
			local var_31_0 = arg_30_0.shipVO and {
				type = EquipmentInfoMediator.TYPE_REPLACE,
				shipId = arg_30_0.contextData.shipId,
				oldSpWeaponUid = var_30_1.GetUID(),
				oldShipId = var_30_1.GetShipId()
			} or var_30_1.GetShipId() and {
				type = EquipmentInfoMediator.TYPE_DISPLAY,
				spWeaponUid = var_30_1.GetUID(),
				shipId = var_30_1.GetShipId()
			} or {
				type = EquipmentInfoMediator.TYPE_DEFAULT,
				spWeaponUid = var_30_1.GetUID()
			}

			arg_30_0.emit(var_0_0.ON_SPWEAPON, var_31_0), SFX_PANEL)

def var_0_0.ReturnSpWeapon(arg_32_0, arg_32_1, arg_32_2):
	if arg_32_0.exited:
		return

	local var_32_0 = arg_32_0.equipmetItems[arg_32_2]

	if var_32_0:
		removeOnButton(var_32_0.go)
		var_32_0.clear()

def var_0_0.updateEquipmentCount(arg_33_0):
	local var_33_0 = arg_33_0.hideSpweapon and 0 or #arg_33_0.loadEquipmentVOs

	arg_33_0.equipmentRect.align(var_33_0)

	local var_33_1 = arg_33_0.equipmentsGrid.GetComponent(typeof(GridLayoutGroup))
	local var_33_2 = var_33_1.padding

	if var_33_0:
		var_33_2.top = 31
		var_33_2.bottom = 25
	else
		var_33_2.top = 0
		var_33_2.bottom = 0

	var_33_1.padding = var_33_2

def var_0_0.filterEquipment(arg_34_0):
	local var_34_0 = arg_34_0.isDefaultStatus() and "shaixuan_off" or "shaixuan_on"

	GetSpriteFromAtlasAsync("ui/share/index_atlas", var_34_0, function(arg_35_0)
		setImageSprite(arg_34_0.indexBtn, arg_35_0, True))

	local var_34_1 = arg_34_0.contextData.sortData

	;(function()
		arg_34_0.loadEquipmentVOs = {}

		local var_36_0 = {}

		for iter_36_0, iter_36_1 in pairs(arg_34_0.equipmentVOs):
			table.insert(var_36_0, iter_36_1)

		for iter_36_2, iter_36_3 in pairs(var_36_0):
			if arg_34_0.checkFitBusyCondition(iter_36_3) and IndexConst.filterSpWeaponByType(iter_36_3, arg_34_0.contextData.indexDatas.typeIndex) and IndexConst.filterSpWeaponByRarity(iter_36_3, arg_34_0.contextData.indexDatas.rarityIndex) and (arg_34_0.filterImportance == None or iter_36_3.IsImportant()):
				table.insert(arg_34_0.loadEquipmentVOs, iter_36_3)

		if var_34_1:
			local var_36_1 = arg_34_0.asc

			table.sort(arg_34_0.loadEquipmentVOs, CompareFuncs(var_0_1.sortFunc(var_34_1, var_36_1)))

		if arg_34_0.contextData.qiutBtn:
			table.insert(arg_34_0.loadEquipmentVOs, 1, False))()
	arg_34_0.updateEquipmentCount()
	;(function()
		arg_34_0.showCraftList = {}

		local var_37_0 = {}

		for iter_37_0, iter_37_1 in pairs(arg_34_0.craftList):
			table.insert(var_37_0, iter_37_1)

		for iter_37_2, iter_37_3 in pairs(var_37_0):
			if arg_34_0.checkFitBusyCondition(iter_37_3) and IndexConst.filterSpWeaponByType(iter_37_3, arg_34_0.contextData.indexDatas.typeIndex) and IndexConst.filterSpWeaponByRarity(iter_37_3, arg_34_0.contextData.indexDatas.rarityIndex) and (arg_34_0.filterImportance == None or iter_37_3.IsImportant()):
				table.insert(arg_34_0.showCraftList, iter_37_3)

		if var_34_1:
			local var_37_1 = arg_34_0.asc

			table.sort(arg_34_0.showCraftList, CompareFuncs(var_0_1.sortFunc(var_34_1, var_37_1))))()
	arg_34_0.UpdateCraftCount()
	setImageSprite(arg_34_0.findTF("Image", arg_34_0.sortBtn), GetSpriteFromAtlas("ui/equipmentui_atlas", var_34_1.spr), True)
	setActive(arg_34_0.sortImgAsc, arg_34_0.asc)
	setActive(arg_34_0.sortImgDec, not arg_34_0.asc)

def var_0_0.InitCraftItem(arg_38_0, arg_38_1):
	local var_38_0 = SpWeaponItemView.New(arg_38_1)

	arg_38_0.craftItems[arg_38_1] = var_38_0

def var_0_0.UpdateCraftItem(arg_39_0, arg_39_1, arg_39_2):
	local var_39_0 = arg_39_0.craftItems[arg_39_2]

	assert(var_39_0, "without init item")

	local var_39_1 = arg_39_0.showCraftList[arg_39_1 + 1]

	var_39_0.update(var_39_1)
	onButton(arg_39_0, var_39_0.go, function()
		arg_39_0.emit(SpWeaponStoreHouseMediator.ON_COMPOSITE, var_39_1.GetConfigID()), SFX_PANEL)

def var_0_0.ReturnCraftItem(arg_41_0, arg_41_1, arg_41_2):
	local var_41_0 = arg_41_0.craftItems[arg_41_2]

	if var_41_0:
		removeOnButton(var_41_0.go)
		var_41_0.clear()

def var_0_0.UpdateCraftCount(arg_42_0):
	local var_42_0 = arg_42_0.hideCraft and 0 or #arg_42_0.showCraftList

	arg_42_0.craftRect.align(var_42_0)

	local var_42_1 = arg_42_0.craftsGrid.GetComponent(typeof(GridLayoutGroup))
	local var_42_2 = var_42_1.padding

	if var_42_0 > 0:
		var_42_2.top = 31
		var_42_2.bottom = 25
	else
		var_42_2.top = 0
		var_42_2.bottom = 0

	var_42_1.padding = var_42_2

def var_0_0.GetShowBusyFlag(arg_43_0):
	return arg_43_0.isEquipingOn

def var_0_0.SetShowBusyFlag(arg_44_0, arg_44_1):
	arg_44_0.isEquipingOn = arg_44_1

def var_0_0.checkFitBusyCondition(arg_45_0, arg_45_1):
	return arg_45_0.GetShowBusyFlag() or not arg_45_1.GetShipId()

def var_0_0.willExit(arg_46_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_46_0.blurPanel, arg_46_0._tf)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_46_0.topItems, arg_46_0._tf)

return var_0_0
