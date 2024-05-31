local var_0_0 = class("WorldInventoryLayer", import("..base.BaseUI"))
local var_0_1 = require("view.equipment.EquipmentSortCfg")

var_0_0.PAGE = {
	Equipment = 2,
	Property = 1,
	Material = 3
}

def var_0_0.getUIName(arg_1_0):
	return "WorldInventoryUI"

def var_0_0.init(arg_2_0):
	function arg_2_0.itemUpdateListenerFunc(...)
		arg_2_0.setItemList(arg_2_0.inventoryProxy.GetItemList())

	arg_2_0.blurPanel = arg_2_0.findTF("blur_panel")
	arg_2_0.backBtn = arg_2_0.findTF("adapt/top/back_btn", arg_2_0.blurPanel)
	arg_2_0.topItems = arg_2_0.findTF("topItems")
	arg_2_0.itemView = arg_2_0.findTF("item_scrollview")
	arg_2_0.equipmentView = arg_2_0.findTF("equipment_scrollview")
	arg_2_0.materialtView = arg_2_0.findTF("material_scrollview")

	local var_2_0
	local var_2_1 = getProxy(SettingsProxy)

	if NotchAdapt.CheckNotchRatio == 2 or not var_2_1.CheckLargeScreen():
		var_2_0 = arg_2_0.itemView.rect.width > 2000
	else
		var_2_0 = NotchAdapt.CheckNotchRatio >= 2

	arg_2_0.itemView.Find("Viewport/item_grid").GetComponent(typeof(GridLayoutGroup)).constraintCount = var_2_0 and 8 or 7
	arg_2_0.equipmentView.Find("Viewport/moudle_grid").GetComponent(typeof(GridLayoutGroup)).constraintCount = var_2_0 and 8 or 7
	arg_2_0.materialtView.Find("Viewport/item_grid").GetComponent(typeof(GridLayoutGroup)).constraintCount = var_2_0 and 8 or 7
	arg_2_0.itemUsagePanel = ItemUsagePanel.New(arg_2_0.findTF("item_usage_panel"), arg_2_0._tf)
	arg_2_0.itemResetPanel = ItemResetPanel.New(arg_2_0.findTF("reset_info_panel"), arg_2_0._tf)
	arg_2_0.assignedItemView = WorldAssignedItemView.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.itemCards = {}
	arg_2_0.equipmetItems = {}
	arg_2_0.materialCards = {}
	arg_2_0._itemToggle = arg_2_0.findTF("topItems/bottom_back/types/properties")
	arg_2_0._weaponToggle = arg_2_0.findTF("topItems/bottom_back/types/siren_weapon")
	arg_2_0._materialToggle = arg_2_0.findTF("topItems/bottom_back/types/material")
	arg_2_0.exchangeTips = arg_2_0.findTF("topItems/bottom_back/reset_exchange")
	arg_2_0.filterBusyToggle = arg_2_0.findTF("adapt/left_length/frame/toggle_equip", arg_2_0.blurPanel)
	arg_2_0.sortBtn = arg_2_0.findTF("adapt/top/buttons/sort_button", arg_2_0.blurPanel)
	arg_2_0.indexBtn = arg_2_0.findTF("adapt/top/buttons/index_button", arg_2_0.blurPanel)
	arg_2_0.decBtn = arg_2_0.findTF("adapt/top/buttons/dec_btn", arg_2_0.blurPanel)
	arg_2_0.upOrderTF = arg_2_0.findTF("asc", arg_2_0.decBtn)
	arg_2_0.downOrderTF = arg_2_0.findTF("desc", arg_2_0.decBtn)
	arg_2_0.sortPanel = arg_2_0.findTF("sort", arg_2_0.topItems)
	arg_2_0.sortContain = arg_2_0.findTF("adapt/mask/panel", arg_2_0.sortPanel)
	arg_2_0.sortTpl = arg_2_0.findTF("tpl", arg_2_0.sortContain)

	setActive(arg_2_0.sortTpl, False)
	arg_2_0.initData()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_4_0):
	arg_4_0.initItems()
	arg_4_0.initEquipments()
	arg_4_0.InitMaterials()
	setActive(arg_4_0._weaponToggle, True)
	setActive(arg_4_0._itemToggle, True)

	local var_4_0 = arg_4_0.contextData.pageNum

	arg_4_0.contextData.pageNum = None

	if var_4_0 == var_0_0.PAGE.Property:
		triggerToggle(arg_4_0._itemToggle, True)
	elif var_4_0 == var_0_0.PAGE.Equipment:
		triggerToggle(arg_4_0._weaponToggle, True)
	elif var_4_0 == var_0_0.PAGE.Material:
		triggerToggle(arg_4_0._materialToggle, True)

	if arg_4_0.contextData.equipScrollPos:
		arg_4_0.ScrollEquipPos(arg_4_0.contextData.equipScrollPos.y)

	onButton(arg_4_0, arg_4_0.exchangeTips.Find("capcity"), function()
		arg_4_0.emit(var_0_0.ON_DROP, {
			type = DROP_TYPE_RESOURCE,
			id = WorldConst.ResourceID
		}), SFX_PANEL)
	pg.UIMgr.GetInstance().OverlayPanel(arg_4_0._tf, {
		groupName = arg_4_0.getGroupNameFromData()
	})

def var_0_0.OverlayPanel(arg_6_0, arg_6_1):
	arg_6_0.overlayIndex = arg_6_0.overlayIndex or 0
	arg_6_0.overlayIndex = arg_6_0.overlayIndex + 1

	setParent(tf(arg_6_1), arg_6_0._tf.parent, False)
	tf(arg_6_1).SetSiblingIndex(arg_6_0._tf.GetSiblingIndex() + arg_6_0.overlayIndex)

def var_0_0.UnOverlayPanel(arg_7_0, arg_7_1, arg_7_2):
	setParent(tf(arg_7_1), arg_7_2, False)

	arg_7_0.overlayIndex = arg_7_0.overlayIndex or 0
	arg_7_0.overlayIndex = arg_7_0.overlayIndex - 1
	arg_7_0.overlayIndex = math.max(arg_7_0.overlayIndex, 0)

def var_0_0.onBackPressed(arg_8_0):
	if isActive(arg_8_0.itemResetPanel._go):
		arg_8_0.itemResetPanel.Close()
	elif isActive(arg_8_0.itemUsagePanel._go):
		arg_8_0.itemUsagePanel.Close()
	elif arg_8_0.assignedItemView.isShowing():
		arg_8_0.assignedItemView.Hide()
	else
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
		triggerButton(arg_8_0.backBtn)

def var_0_0.willExit(arg_9_0):
	arg_9_0.assignedItemView.Destroy()
	arg_9_0.inventoryProxy.RemoveListener(WorldInventoryProxy.EventUpdateItem, arg_9_0.itemUpdateListenerFunc)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_9_0._tf)

def var_0_0.initData(arg_10_0):
	arg_10_0.contextData.pageNum = arg_10_0.contextData.pageNum or var_0_0.PAGE.Property
	arg_10_0.contextData.asc = arg_10_0.contextData.asc or False

	if not arg_10_0.contextData.sortData:
		arg_10_0.contextData.sortData = var_0_1.sort[1]

	arg_10_0.contextData.indexDatas = arg_10_0.contextData.indexDatas or {}
	arg_10_0.isEquipingOn = False

def var_0_0.GetShowBusyFlag(arg_11_0):
	return arg_11_0.isEquipingOn

def var_0_0.SetShowBusyFlag(arg_12_0, arg_12_1):
	arg_12_0.isEquipingOn = arg_12_1

def var_0_0.addListener(arg_13_0):
	onButton(arg_13_0, arg_13_0.backBtn, function()
		arg_13_0.closeView(), SFX_CANCEL)
	onButton(arg_13_0, arg_13_0.decBtn, function()
		arg_13_0.contextData.asc = not arg_13_0.contextData.asc

		if arg_13_0.contextData.pageNum == var_0_0.PAGE.Equipment:
			arg_13_0.filterEquipment(), SFX_PANEL)

	arg_13_0.sortButtons = {}

	eachChild(arg_13_0.sortContain, function(arg_16_0)
		setActive(arg_16_0, False))

	for iter_13_0, iter_13_1 in ipairs(var_0_1.sort):
		local var_13_0 = iter_13_0 <= arg_13_0.sortContain.childCount and arg_13_0.sortContain.GetChild(iter_13_0 - 1) or cloneTplTo(arg_13_0.sortTpl, arg_13_0.sortContain)

		setActive(var_13_0, True)
		setImageSprite(findTF(var_13_0, "Image"), GetSpriteFromAtlas("ui/equipmentui_atlas", iter_13_1.spr), True)
		onToggle(arg_13_0, var_13_0, function(arg_17_0)
			if arg_17_0:
				arg_13_0.contextData.sortData = iter_13_1

				arg_13_0.filterEquipment()
				triggerToggle(arg_13_0.sortBtn, False), SFX_PANEL)

		arg_13_0.sortButtons[iter_13_0] = var_13_0

	onToggle(arg_13_0, arg_13_0.sortBtn, function(arg_18_0)
		if arg_18_0:
			arg_13_0.OverlayPanel(arg_13_0.sortPanel)
			setActive(arg_13_0.sortPanel, True)
		else
			arg_13_0.UnOverlayPanel(arg_13_0.sortPanel, arg_13_0.topItems)
			setActive(arg_13_0.sortPanel, False), SFX_PANEL)
	onButton(arg_13_0, arg_13_0.sortPanel, function()
		triggerToggle(arg_13_0.sortBtn, False), SFX_PANEL)
	onToggle(arg_13_0, arg_13_0.filterBusyToggle, function(arg_20_0)
		arg_13_0.SetShowBusyFlag(arg_20_0)

		if arg_13_0.contextData.pageNum == var_0_0.PAGE.Equipment:
			arg_13_0.filterEquipment(), SFX_PANEL)
	onButton(arg_13_0, arg_13_0.indexBtn, function()
		local var_21_0 = {
			indexDatas = Clone(arg_13_0.contextData.indexDatas),
			customPanels = {
				minHeight = 650,
				typeIndex = {
					mode = CustomIndexLayer.Mode.OR,
					options = IndexConst.EquipmentTypeIndexs,
					names = IndexConst.EquipmentTypeNames
				},
				equipPropertyIndex = {
					mode = CustomIndexLayer.Mode.OR,
					options = IndexConst.EquipPropertyIndexs,
					names = IndexConst.EquipPropertyNames
				},
				equipPropertyIndex2 = {
					mode = CustomIndexLayer.Mode.OR,
					options = IndexConst.EquipPropertyIndexs,
					names = IndexConst.EquipPropertyNames
				},
				equipAmmoIndex1 = {
					mode = CustomIndexLayer.Mode.OR,
					options = IndexConst.EquipAmmoIndexs_1,
					names = IndexConst.EquipAmmoIndexs_1_Names
				},
				equipAmmoIndex2 = {
					mode = CustomIndexLayer.Mode.OR,
					options = IndexConst.EquipAmmoIndexs_2,
					names = IndexConst.EquipAmmoIndexs_2_Names
				},
				equipCampIndex = {
					mode = CustomIndexLayer.Mode.AND,
					options = IndexConst.EquipCampIndexs,
					names = IndexConst.EquipCampNames
				},
				rarityIndex = {
					mode = CustomIndexLayer.Mode.AND,
					options = IndexConst.EquipmentRarityIndexs,
					names = IndexConst.RarityNames
				},
				extraIndex = {
					mode = CustomIndexLayer.Mode.OR,
					options = IndexConst.EquipmentExtraIndexs,
					names = IndexConst.EquipmentExtraNames
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
					dropdown = True,
					titleTxt = "indexsort_index",
					titleENTxt = "indexsort_indexeng",
					tags = {
						"equipPropertyIndex",
						"equipPropertyIndex2",
						"equipAmmoIndex1",
						"equipAmmoIndex2"
					}
				},
				{
					dropdown = False,
					titleTxt = "indexsort_camp",
					titleENTxt = "indexsort_campeng",
					tags = {
						"equipCampIndex"
					}
				},
				{
					dropdown = False,
					titleTxt = "indexsort_rarity",
					titleENTxt = "indexsort_rarityeng",
					tags = {
						"rarityIndex"
					}
				},
				{
					dropdown = False,
					titleTxt = "indexsort_extraindex",
					titleENTxt = "indexsort_indexeng",
					tags = {
						"extraIndex"
					}
				}
			},
			dropdownLimit = {
				equipPropertyIndex = {
					include = {
						typeIndex = IndexConst.EquipmentTypeAll
					},
					exclude = {}
				},
				equipPropertyIndex2 = {
					include = {
						typeIndex = IndexConst.EquipmentTypeEquip
					},
					exclude = {
						typeIndex = IndexConst.EquipmentTypeAll
					}
				},
				equipAmmoIndex1 = {
					include = {
						typeIndex = IndexConst.BitAll({
							IndexConst.EquipmentTypeSmallCannon,
							IndexConst.EquipmentTypeMediumCannon,
							IndexConst.EquipmentTypeBigCannon
						})
					},
					exclude = {
						typeIndex = IndexConst.EquipmentTypeAll
					}
				},
				equipAmmoIndex2 = {
					include = {
						typeIndex = IndexConst.BitAll({
							IndexConst.EquipmentTypeWarshipTorpedo,
							IndexConst.EquipmentTypeSubmaraineTorpedo
						})
					},
					exclude = {
						typeIndex = IndexConst.EquipmentTypeAll
					}
				}
			},
			def callback:(arg_22_0)
				arg_13_0.contextData.indexDatas.typeIndex = arg_22_0.typeIndex
				arg_13_0.contextData.indexDatas.equipPropertyIndex = arg_22_0.equipPropertyIndex
				arg_13_0.contextData.indexDatas.equipPropertyIndex2 = arg_22_0.equipPropertyIndex2
				arg_13_0.contextData.indexDatas.equipAmmoIndex1 = arg_22_0.equipAmmoIndex1
				arg_13_0.contextData.indexDatas.equipAmmoIndex2 = arg_22_0.equipAmmoIndex2
				arg_13_0.contextData.indexDatas.equipCampIndex = arg_22_0.equipCampIndex
				arg_13_0.contextData.indexDatas.rarityIndex = arg_22_0.rarityIndex
				arg_13_0.contextData.indexDatas.extraIndex = arg_22_0.extraIndex

				if arg_13_0.filterBusyToggle.GetComponent(typeof(Toggle)):
					if bit.band(arg_22_0.extraIndex, IndexConst.EquipmentExtraEquiping) > 0:
						arg_13_0.SetShowBusyFlag(True)

					triggerToggle(arg_13_0.filterBusyToggle, arg_13_0.GetShowBusyFlag())
				else
					arg_13_0.filterEquipment()
		}

		arg_13_0.emit(WorldInventoryMediator.OPEN_EQUIPMENT_INDEX, var_21_0), SFX_PANEL)
	onToggle(arg_13_0, arg_13_0._itemToggle, function(arg_23_0)
		if arg_23_0 and arg_13_0.contextData.pageNum != var_0_0.PAGE.Property:
			arg_13_0.contextData.pageNum = var_0_0.PAGE.Property

			arg_13_0.activeResetExchange(arg_13_0.contextData.pageNum == var_0_0.PAGE.Property)
			arg_13_0.sortItems(), SFX_PANEL)
	onToggle(arg_13_0, arg_13_0._weaponToggle, function(arg_24_0)
		if arg_24_0 and arg_13_0.contextData.pageNum != var_0_0.PAGE.Equipment:
			arg_13_0.contextData.pageNum = var_0_0.PAGE.Equipment

			arg_13_0.activeResetExchange(arg_13_0.contextData.pageNum == var_0_0.PAGE.Property)
			arg_13_0.filterEquipment(), SFX_PANEL)
	onToggle(arg_13_0, arg_13_0._materialToggle, function(arg_25_0)
		if arg_25_0 and arg_13_0.contextData.pageNum != var_0_0.PAGE.Material:
			arg_13_0.contextData.pageNum = var_0_0.PAGE.Material

			arg_13_0.activeResetExchange(arg_13_0.contextData.pageNum == var_0_0.PAGE.Property)
			arg_13_0.SortMaterials(), SFX_PANEL)

def var_0_0.setWorldFleet(arg_26_0, arg_26_1):
	arg_26_0.worldFleetList = arg_26_1

def var_0_0.setInventoryProxy(arg_27_0, arg_27_1):
	arg_27_0.inventoryProxy = arg_27_1

	arg_27_0.inventoryProxy.AddListener(WorldInventoryProxy.EventUpdateItem, arg_27_0.itemUpdateListenerFunc)
	arg_27_0.setItemList(arg_27_0.inventoryProxy.GetItemList())

def var_0_0.setItemList(arg_28_0, arg_28_1):
	arg_28_0.itemList = arg_28_1

	if arg_28_0.isInitItems:
		arg_28_0.sortItems()

def var_0_0.initItems(arg_29_0):
	arg_29_0.isInitItems = True
	arg_29_0.itemRect = arg_29_0.itemView.GetComponent("LScrollRect")

	function arg_29_0.itemRect.onInitItem(arg_30_0)
		arg_29_0.initItem(arg_30_0)

	function arg_29_0.itemRect.onUpdateItem(arg_31_0, arg_31_1)
		arg_29_0.updateItem(arg_31_0, arg_31_1)

	function arg_29_0.itemRect.onReturnItem(arg_32_0, arg_32_1)
		arg_29_0.returnItem(arg_32_0, arg_32_1)

def var_0_0.initItem(arg_33_0, arg_33_1):
	local var_33_0 = WSInventoryItem.New(arg_33_1)

	onButton(arg_33_0, var_33_0.go, function()
		local var_34_0 = var_33_0.itemVO.getWorldItemType()

		if var_34_0 == WorldItem.UsageBuff or var_34_0 == WorldItem.UsageHPRegenerate or var_34_0 == WorldItem.UsageHPRegenerateValue:
			arg_33_0.emit(WorldInventoryMediator.OnOpenAllocateLayer, {
				itemVO = var_33_0.itemVO,
				fleetList = arg_33_0.worldFleetList,
				fleetIndex = arg_33_0.contextData.currentFleetIndex,
				def confirmCallback:(arg_35_0, arg_35_1)
					arg_33_0.emit(WorldInventoryMediator.OnUseItem, arg_35_0, 1, arg_35_1),
				def onResetInfo:(arg_36_0)
					arg_33_0.itemResetPanel.Open(arg_36_0)
			})
		elif var_34_0 == WorldItem.UsageWorldMap:
			arg_33_0.itemUsagePanel.Open({
				item = var_33_0.itemVO,
				mode = ItemUsagePanel.SEE,
				def onUse:()
					arg_33_0.PlayOpenBox(var_33_0.itemVO.getWorldItemOpenDisplay(), function()
						arg_33_0.emit(WorldInventoryMediator.OnMap, var_33_0.itemVO.id)
						arg_33_0.closeView()),
				def onResetInfo:(arg_39_0)
					arg_33_0.itemResetPanel.Open(arg_39_0)
			})
		elif var_34_0 == WorldItem.UsageDrop or var_34_0 == WorldItem.UsageRecoverAp or var_34_0 == WorldItem.UsageWorldItem or var_34_0 == WorldItem.UsageWorldBuff:
			arg_33_0.itemUsagePanel.Open({
				item = var_33_0.itemVO,
				mode = ItemUsagePanel.BATCH,
				def onUseBatch:(arg_40_0)
					arg_33_0.emit(WorldInventoryMediator.OnUseItem, var_33_0.itemVO.id, arg_40_0, {}),
				def onUseOne:()
					arg_33_0.emit(WorldInventoryMediator.OnUseItem, var_33_0.itemVO.id, 1, {}),
				def onResetInfo:(arg_42_0)
					arg_33_0.itemResetPanel.Open(arg_42_0)
			})
		elif var_34_0 == WorldItem.UsageLoot:
			arg_33_0.itemUsagePanel.Open({
				item = var_33_0.itemVO,
				mode = ItemUsagePanel.INFO,
				def onResetInfo:(arg_43_0)
					arg_33_0.itemResetPanel.Open(arg_43_0)
			})
		elif var_34_0 == WorldItem.UsageWorldClean or var_34_0 == WorldItem.UsageWorldFlag:
			arg_33_0.itemUsagePanel.Open({
				item = var_33_0.itemVO,
				def onUse:()
					arg_33_0.emit(WorldInventoryMediator.OnUseItem, var_33_0.itemVO.id, 1, {}),
				def onResetInfo:(arg_45_0)
					arg_33_0.itemResetPanel.Open(arg_45_0)
			})
		elif var_34_0 == WorldItem.UsageDropAppointed:
			arg_33_0.assignedItemView.Load()
			arg_33_0.assignedItemView.ActionInvoke("update", var_33_0.itemVO)
			arg_33_0.assignedItemView.ActionInvoke("Show"), SFX_PANEL)

	arg_33_0.itemCards[arg_33_1] = var_33_0

def var_0_0.updateItem(arg_46_0, arg_46_1, arg_46_2):
	local var_46_0 = arg_46_0.itemCards[arg_46_2]

	if not var_46_0:
		arg_46_0.initItem(arg_46_2)

		var_46_0 = arg_46_0.itemCards[arg_46_2]

	local var_46_1 = arg_46_0.itemList[arg_46_1 + 1]

	var_46_0.update(var_46_1)

def var_0_0.returnItem(arg_47_0, arg_47_1, arg_47_2):
	if arg_47_0.exited:
		return

	local var_47_0 = arg_47_0.itemCards[arg_47_2]

	if var_47_0:
		var_47_0.clear()

def var_0_0.sortItems(arg_48_0):
	table.sort(arg_48_0.itemList, CompareFuncs({
		function(arg_49_0)
			return -arg_49_0.getConfig("sort_priority"),
		function(arg_50_0)
			return arg_50_0.getConfig("id")
	}))
	arg_48_0.itemRect.SetTotalCount(#arg_48_0.itemList, -1)
	arg_48_0.updateResetExchange()

def var_0_0.updateResetExchange(arg_51_0):
	local var_51_0 = arg_51_0.inventoryProxy.CalcResetExchangeResource()

	setText(arg_51_0.exchangeTips.Find("capcity/Text"), defaultValue(checkExist(var_51_0, {
		DROP_TYPE_RESOURCE
	}, {
		WorldConst.ResourceID
	}), 0))

def var_0_0.activeResetExchange(arg_52_0, arg_52_1):
	local var_52_0 = nowWorld().IsSystemOpen(WorldConst.SystemResetExchange)

	setActive(arg_52_0.exchangeTips, var_52_0 and arg_52_1)

def var_0_0.PlayOpenBox(arg_53_0, arg_53_1, arg_53_2):
	if not arg_53_1 or arg_53_1 == "":
		arg_53_2()

		return

	local function var_53_0()
		if arg_53_0.playing or not arg_53_0[arg_53_1]:
			return

		arg_53_0.playing = True

		arg_53_0[arg_53_1].SetActive(True)

		local var_54_0 = tf(arg_53_0[arg_53_1])

		var_54_0.SetParent(arg_53_0._tf, False)
		var_54_0.SetAsLastSibling()

		local var_54_1 = var_54_0.GetComponent("DftAniEvent")

		var_54_1.SetTriggerEvent(function(arg_55_0)
			arg_53_2())
		var_54_1.SetEndEvent(function(arg_56_0)
			if arg_53_0[arg_53_1]:
				SetActive(arg_53_0[arg_53_1], False)

				arg_53_0.playing = False)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_EQUIPMENT_OPEN)

	local var_53_1 = arg_53_0.findTF(arg_53_1 .. "(Clone)")

	if var_53_1:
		arg_53_0[arg_53_1] = go(var_53_1)

	if not arg_53_0[arg_53_1]:
		PoolMgr.GetInstance().GetPrefab("ui/" .. string.lower(arg_53_1), "", True, function(arg_57_0)
			arg_57_0.SetActive(True)

			arg_53_0[arg_53_1] = arg_57_0

			var_53_0())
	else
		var_53_0()

def var_0_0.setEquipments(arg_58_0, arg_58_1):
	arg_58_0.equipmentVOs = arg_58_1

def var_0_0.setEquipment(arg_59_0, arg_59_1):
	local var_59_0 = #arg_59_0.equipmentVOs + 1

	for iter_59_0, iter_59_1 in ipairs(arg_59_0.equipmentVOs):
		if not iter_59_1.shipId and iter_59_1.id == arg_59_1.id:
			var_59_0 = iter_59_0

			break

	if arg_59_1.count > 0:
		arg_59_0.equipmentVOs[var_59_0] = arg_59_1
	else
		table.remove(arg_59_0.equipmentVOs, var_59_0)

	if arg_59_0.contextData.pageNum == var_0_0.PAGE.Equipment:
		arg_59_0.filterEquipment()

def var_0_0.initEquipments(arg_60_0):
	arg_60_0.isInitWeapons = True
	arg_60_0.equipmentRect = arg_60_0.equipmentView.GetComponent("LScrollRect")

	function arg_60_0.equipmentRect.onInitItem(arg_61_0)
		arg_60_0.initEquipment(arg_61_0)

	function arg_60_0.equipmentRect.onUpdateItem(arg_62_0, arg_62_1)
		arg_60_0.updateEquipment(arg_62_0, arg_62_1)

	function arg_60_0.equipmentRect.onReturnItem(arg_63_0, arg_63_1)
		arg_60_0.returnEquipment(arg_63_0, arg_63_1)

	arg_60_0.equipmentRect.decelerationRate = 0.07

def var_0_0.initEquipment(arg_64_0, arg_64_1):
	local var_64_0 = EquipmentItem.New(arg_64_1)

	onButton(arg_64_0, var_64_0.go, function()
		if arg_64_0.equipmentRect.GetContentAnchoredPositionOriginal:
			arg_64_0.contextData.equipScrollPos = arg_64_0.equipmentRect.GetContentAnchoredPositionOriginal()

		if var_64_0.equipmentVO == None or var_64_0.equipmentVO.mask:
			return

		local var_65_0 = arg_64_0.shipVO and {
			type = EquipmentInfoMediator.TYPE_REPLACE,
			equipmentId = var_64_0.equipmentVO.id,
			shipId = arg_64_0.contextData.shipId,
			pos = arg_64_0.contextData.pos,
			oldShipId = var_64_0.equipmentVO.shipId,
			oldPos = var_64_0.equipmentVO.shipPos
		} or var_64_0.equipmentVO.shipId and {
			type = EquipmentInfoMediator.TYPE_DISPLAY,
			equipmentId = var_64_0.equipmentVO.id,
			shipId = var_64_0.equipmentVO.shipId,
			pos = var_64_0.equipmentVO.shipPos
		} or {
			destroy = True,
			type = EquipmentInfoMediator.TYPE_DEFAULT,
			equipmentId = var_64_0.equipmentVO.id
		}

		arg_64_0.emit(var_0_0.ON_EQUIPMENT, var_65_0), SFX_PANEL)

	arg_64_0.equipmetItems[arg_64_1] = var_64_0

def var_0_0.updateEquipment(arg_66_0, arg_66_1, arg_66_2):
	local var_66_0 = arg_66_0.equipmetItems[arg_66_2]

	if not var_66_0:
		arg_66_0.initEquipment(arg_66_2)

		var_66_0 = arg_66_0.equipmetItems[arg_66_2]

	local var_66_1 = arg_66_0.loadEquipmentVOs[arg_66_1 + 1]

	var_66_0.update(var_66_1)

def var_0_0.returnEquipment(arg_67_0, arg_67_1, arg_67_2):
	if arg_67_0.exited:
		return

	local var_67_0 = arg_67_0.equipmetItems[arg_67_2]

	if var_67_0:
		var_67_0.clear()

def var_0_0.filterEquipment(arg_68_0):
	local var_68_0 = arg_68_0.contextData.sortData

	arg_68_0.loadEquipmentVOs = arg_68_0.loadEquipmentVOs or {}

	table.clean(arg_68_0.loadEquipmentVOs)

	local var_68_1 = arg_68_0.loadEquipmentVOs
	local var_68_2 = {
		arg_68_0.contextData.indexDatas.equipPropertyIndex,
		arg_68_0.contextData.indexDatas.equipPropertyIndex2
	}

	for iter_68_0, iter_68_1 in pairs(arg_68_0.equipmentVOs):
		if (not iter_68_1.shipId or arg_68_0.GetShowBusyFlag()) and not iter_68_1.isSkin and IndexConst.filterEquipByType(iter_68_1, arg_68_0.contextData.indexDatas.typeIndex) and IndexConst.filterEquipByProperty(iter_68_1, var_68_2) and IndexConst.filterEquipAmmo1(iter_68_1, arg_68_0.contextData.indexDatas.equipAmmoIndex1) and IndexConst.filterEquipAmmo2(iter_68_1, arg_68_0.contextData.indexDatas.equipAmmoIndex2) and IndexConst.filterEquipByCamp(iter_68_1, arg_68_0.contextData.indexDatas.equipCampIndex) and IndexConst.filterEquipByRarity(iter_68_1, arg_68_0.contextData.indexDatas.rarityIndex) and IndexConst.filterEquipByExtra(iter_68_1, arg_68_0.contextData.indexDatas.extraIndex):
			table.insert(arg_68_0.loadEquipmentVOs, iter_68_1)

	if var_68_0:
		local var_68_3 = arg_68_0.contextData.asc

		table.sort(var_68_1, CompareFuncs(var_0_1.sortFunc(var_68_0, var_68_3)))

	arg_68_0.updateEquipmentCount()
	setImageSprite(arg_68_0.findTF("Image", arg_68_0.sortBtn), GetSpriteFromAtlas("ui/equipmentui_atlas", var_68_0.spr), True)
	setActive(arg_68_0.downOrderTF, not arg_68_0.contextData.asc)
	setActive(arg_68_0.upOrderTF, arg_68_0.contextData.asc)

def var_0_0.updateEquipmentCount(arg_69_0, arg_69_1):
	arg_69_0.equipmentRect.SetTotalCount(arg_69_1 or #arg_69_0.loadEquipmentVOs, -1)
	Canvas.ForceUpdateCanvases()

def var_0_0.Scroll2Equip(arg_70_0, arg_70_1):
	if arg_70_0.contextData.pageNum != var_0_0.PAGE.Equipment:
		return

	for iter_70_0, iter_70_1 in ipairs(arg_70_0.loadEquipmentVOs):
		if EquipmentProxy.SameEquip(iter_70_1, arg_70_1):
			local var_70_0 = arg_70_0.equipmentView.Find("Viewport/moudle_grid").GetComponent(typeof(GridLayoutGroup))
			local var_70_1 = (var_70_0.cellSize.y + var_70_0.spacing.y) * math.floor((iter_70_0 - 1) / var_70_0.constraintCount) + arg_70_0.equipmentRect.paddingFront + arg_70_0.equipmentView.rect.height * 0.5

			arg_70_0.ScrollEquipPos(var_70_1 - arg_70_0.equipmentRect.paddingFront)

			break

def var_0_0.ScrollEquipPos(arg_71_0, arg_71_1):
	local var_71_0 = arg_71_0.equipmentView.Find("Viewport/moudle_grid").GetComponent(typeof(GridLayoutGroup))
	local var_71_1 = (var_71_0.cellSize.y + var_71_0.spacing.y) * math.ceil(#arg_71_0.loadEquipmentVOs / var_71_0.constraintCount) - var_71_0.spacing.y + arg_71_0.equipmentRect.paddingFront + arg_71_0.equipmentRect.paddingEnd
	local var_71_2 = var_71_1 - arg_71_0.equipmentView.rect.height

	var_71_2 = var_71_2 > 0 and var_71_2 or var_71_1

	local var_71_3 = (arg_71_1 - arg_71_0.equipmentView.rect.height * 0.5) / var_71_2

	arg_71_0.equipmentRect.ScrollTo(var_71_3)

def var_0_0.SetMaterials(arg_72_0, arg_72_1):
	arg_72_0.materials = arg_72_1

	if arg_72_0.isInitMaterials and arg_72_0.contextData.pageNum == var_0_0.PAGE.Material:
		arg_72_0.SortMaterials()

def var_0_0.InitMaterials(arg_73_0):
	arg_73_0.isInitMaterials = True
	arg_73_0.materialRect = arg_73_0.materialtView.GetComponent("LScrollRect")

	function arg_73_0.materialRect.onInitItem(arg_74_0)
		arg_73_0.InitMaterial(arg_74_0)

	function arg_73_0.materialRect.onUpdateItem(arg_75_0, arg_75_1)
		arg_73_0.UpdateMaterial(arg_75_0, arg_75_1)

	function arg_73_0.materialRect.onReturnItem(arg_76_0, arg_76_1)
		arg_73_0.ReturnMaterial(arg_76_0, arg_76_1)

	arg_73_0.materialRect.decelerationRate = 0.07

def var_0_0.SortMaterials(arg_77_0):
	table.sort(arg_77_0.materials, CompareFuncs({
		function(arg_78_0)
			return -arg_78_0.getConfig("rarity"),
		function(arg_79_0)
			return arg_79_0.id
	}))
	arg_77_0.materialRect.SetTotalCount(#arg_77_0.materials, -1)
	Canvas.ForceUpdateCanvases()

def var_0_0.InitMaterial(arg_80_0, arg_80_1):
	local var_80_0 = ItemCard.New(arg_80_1)

	onButton(arg_80_0, var_80_0.go, function()
		if var_80_0.itemVO == None:
			return

		if var_80_0.itemVO.getConfig("type") == Item.INVITATION_TYPE:
			arg_80_0.emit(EquipmentMediator.ITEM_GO_SCENE, SCENE.INVITATION, {
				itemVO = var_80_0.itemVO
			})
		else
			arg_80_0.emit(var_0_0.ON_ITEM, var_80_0.itemVO.id), SFX_PANEL)

	arg_80_0.materialCards[arg_80_1] = var_80_0

def var_0_0.UpdateMaterial(arg_82_0, arg_82_1, arg_82_2):
	local var_82_0 = arg_82_0.materialCards[arg_82_2]

	if not var_82_0:
		arg_82_0.initItem(arg_82_2)

		var_82_0 = arg_82_0.materialCards[arg_82_2]

	local var_82_1 = arg_82_0.materials[arg_82_1 + 1]

	var_82_0.update(var_82_1)

def var_0_0.ReturnMaterial(arg_83_0, arg_83_1, arg_83_2):
	if arg_83_0.exited:
		return

	local var_83_0 = arg_83_0.materialCards[arg_83_2]

	if var_83_0:
		var_83_0.clear()

return var_0_0
