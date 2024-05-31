local var_0_0 = class("StoreHouseScene", import("view.base.BaseUI"))
local var_0_1 = 1
local var_0_2 = 0
local var_0_3 = 1
local var_0_4 = 2
local var_0_5 = 1
local var_0_6 = 2

def var_0_0.getUIName(arg_1_0):
	return "StoreHouseUI"

def var_0_0.setEquipments(arg_2_0, arg_2_1):
	arg_2_0.equipmentVOs = arg_2_1

	arg_2_0.setEquipmentByIds(arg_2_1)

def var_0_0.setEquipmentByIds(arg_3_0, arg_3_1):
	arg_3_0.equipmentVOByIds = {}

	for iter_3_0, iter_3_1 in pairs(arg_3_1):
		if not iter_3_1.isSkin:
			arg_3_0.equipmentVOByIds[iter_3_1.id] = iter_3_1

local var_0_7 = require("view.equipment.EquipmentSortCfg")
local var_0_8 = require("view.equipment.SpWeaponSortCfg")

def var_0_0.init(arg_4_0):
	arg_4_0.filterEquipWaitting = 0

	local var_4_0 = arg_4_0.contextData

	arg_4_0.topItems = arg_4_0.findTF("topItems")
	arg_4_0.equipmentView = arg_4_0.findTF("equipment_scrollview")
	arg_4_0.blurPanel = arg_4_0.findTF("blur_panel")
	arg_4_0.topPanel = arg_4_0.findTF("adapt/top", arg_4_0.blurPanel)
	arg_4_0.indexBtn = arg_4_0.findTF("buttons/index_button", arg_4_0.topPanel)
	arg_4_0.sortBtn = arg_4_0.findTF("buttons/sort_button", arg_4_0.topPanel)
	arg_4_0.sortPanel = arg_4_0.findTF("sort", arg_4_0.topItems)
	arg_4_0.sortContain = arg_4_0.findTF("adapt/mask/panel", arg_4_0.sortPanel)
	arg_4_0.sortTpl = arg_4_0.findTF("tpl", arg_4_0.sortContain)

	setActive(arg_4_0.sortTpl, False)

	arg_4_0.equipSkinFilteBtn = arg_4_0.findTF("buttons/EquipSkinFilteBtn", arg_4_0.topPanel)
	arg_4_0.itemView = arg_4_0.findTF("item_scrollview")

	local var_4_1
	local var_4_2 = getProxy(SettingsProxy)

	if NotchAdapt.CheckNotchRatio == 2 or not var_4_2.CheckLargeScreen():
		var_4_1 = arg_4_0.itemView.rect.width > 2000
	else
		var_4_1 = NotchAdapt.CheckNotchRatio >= 2

	arg_4_0.equipmentView.Find("equipment_grid").GetComponent(typeof(GridLayoutGroup)).constraintCount = var_4_1 and 8 or 7
	arg_4_0.itemView.Find("item_grid").GetComponent(typeof(GridLayoutGroup)).constraintCount = var_4_1 and 8 or 7
	arg_4_0.decBtn = findTF(arg_4_0.topPanel, "buttons/dec_btn")
	arg_4_0.sortImgAsc = findTF(arg_4_0.decBtn, "asc")
	arg_4_0.sortImgDec = findTF(arg_4_0.decBtn, "desc")
	arg_4_0.equipmentToggle = arg_4_0._tf.Find("blur_panel/adapt/left_length/frame/toggle_root")

	setActive(arg_4_0.equipmentToggle, False)

	arg_4_0.filterBusyToggle = arg_4_0._tf.Find("blur_panel/adapt/left_length/frame/toggle_equip")

	setActive(arg_4_0.filterBusyToggle, False)

	arg_4_0.designTabRoot = arg_4_0._tf.Find("blur_panel/adapt/left_length/frame/toggle_design")

	setActive(arg_4_0.designTabRoot, False)

	arg_4_0.designTabs = CustomIndexLayer.Clone2Full(arg_4_0.designTabRoot, 2)
	arg_4_0.bottomBack = arg_4_0.findTF("adapt/bottom_back", arg_4_0.topItems)
	arg_4_0.bottomPanel = arg_4_0.findTF("types", arg_4_0.bottomBack)
	arg_4_0.materialToggle = arg_4_0.bottomPanel.Find("material")
	arg_4_0.weaponToggle = arg_4_0.bottomPanel.Find("weapon")
	arg_4_0.designToggle = arg_4_0.bottomPanel.Find("design")
	arg_4_0.capacityTF = arg_4_0.findTF("bottom_left/tip/capcity/Text", arg_4_0.bottomBack)
	arg_4_0.tipTF = arg_4_0.findTF("bottom_left/tip", arg_4_0.bottomBack)
	arg_4_0.tip = arg_4_0.tipTF.Find("label")
	arg_4_0.helpBtn = arg_4_0.findTF("adapt/help_btn", arg_4_0.topItems)

	setActive(arg_4_0.helpBtn, True)

	arg_4_0.backBtn = arg_4_0.findTF("blur_panel/adapt/top/back_btn")
	arg_4_0.selectedMin = defaultValue(var_4_0.selectedMin, 1)
	arg_4_0.selectedMax = defaultValue(var_4_0.selectedMax, pg.gameset.equip_select_limit.key_value or 0)
	arg_4_0.selectedIds = Clone(var_4_0.selectedIds or {})
	arg_4_0.checkEquipment = var_4_0.onEquipment or function(arg_5_0, arg_5_1, arg_5_2)
		return True
	arg_4_0.onSelected = var_4_0.onSelected or function()
		warning("not implemented.")
	arg_4_0.BatchDisposeBtn = arg_4_0.findTF("dispos", arg_4_0.bottomPanel)

	if not arg_4_0.BatchDisposeBtn:
		arg_4_0.BatchDisposeBtn = arg_4_0.findTF("dispos", arg_4_0.bottomBack)

	arg_4_0.selectPanel = arg_4_0.findTF("adapt/select_panel", arg_4_0.topItems)

	setActive(arg_4_0.selectPanel, True)
	setAnchoredPosition(arg_4_0.selectPanel, {
		y = -124
	})

	arg_4_0.selectTransformPanel = arg_4_0.findTF("adapt/select_transform_panel", arg_4_0.topItems)

	setActive(arg_4_0.selectTransformPanel, False)

	arg_4_0.listEmptyTF = arg_4_0.findTF("empty")

	setActive(arg_4_0.listEmptyTF, False)

	arg_4_0.listEmptyTxt = arg_4_0.findTF("Text", arg_4_0.listEmptyTF)
	arg_4_0.destroyConfirmView = DestroyConfirmView.New(arg_4_0.topItems, arg_4_0.event)
	arg_4_0.assignedItemView = AssignedItemView.New(arg_4_0.topItems, arg_4_0.event)
	arg_4_0.blueprintAssignedItemView = BlueprintAssignedItemView.New(arg_4_0.topItems, arg_4_0.event)
	arg_4_0.equipDestroyConfirmWindow = EquipDestoryConfirmWindow.New(arg_4_0.topItems, arg_4_0.event)
	arg_4_0.isEquipingOn = False
	arg_4_0.msgBox = SelectSkinMsgbox.New(arg_4_0._tf, arg_4_0.event)

def var_0_0.setEquipment(arg_7_0, arg_7_1):
	local var_7_0 = #arg_7_0.equipmentVOs + 1

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.equipmentVOs):
		if not iter_7_1.shipId and iter_7_1.id == arg_7_1.id:
			var_7_0 = iter_7_0

			break

	if arg_7_1.count > 0:
		arg_7_0.equipmentVOs[var_7_0] = arg_7_1
		arg_7_0.equipmentVOByIds[arg_7_1.id] = arg_7_1
	else
		table.remove(arg_7_0.equipmentVOs, var_7_0)

		arg_7_0.equipmentVOByIds[arg_7_1.id] = None

def var_0_0.setEquipmentUpdate(arg_8_0):
	if arg_8_0.contextData.warp == StoreHouseConst.WARP_TO_WEAPON:
		arg_8_0.filterEquipment()
		arg_8_0.updateCapacity()

def var_0_0.addShipEquipment(arg_9_0, arg_9_1):
	for iter_9_0, iter_9_1 in pairs(arg_9_0.equipmentVOs):
		if EquipmentProxy.SameEquip(iter_9_1, arg_9_1):
			arg_9_0.equipmentVOs[iter_9_0] = arg_9_1

			return

	table.insert(arg_9_0.equipmentVOs, arg_9_1)

def var_0_0.removeShipEquipment(arg_10_0, arg_10_1):
	for iter_10_0 = #arg_10_0.equipmentVOs, 1, -1:
		local var_10_0 = arg_10_0.equipmentVOs[iter_10_0]

		if EquipmentProxy.SameEquip(var_10_0, arg_10_1):
			table.remove(arg_10_0.equipmentVOs, iter_10_0)

def var_0_0.setEquipmentSkin(arg_11_0, arg_11_1):
	local var_11_0 = True

	for iter_11_0, iter_11_1 in pairs(arg_11_0.equipmentVOs):
		if iter_11_1.id == arg_11_1.id and iter_11_1.isSkin:
			arg_11_0.equipmentVOs[iter_11_0] = {
				isSkin = True,
				id = arg_11_1.id,
				count = arg_11_1.count
			}
			var_11_0 = False

	if var_11_0:
		table.insert(arg_11_0.equipmentVOs, {
			isSkin = True,
			id = arg_11_1.id,
			count = arg_11_1.count
		})

def var_0_0.setEquipmentSkinUpdate(arg_12_0):
	if arg_12_0.contextData.warp == StoreHouseConst.WARP_TO_WEAPON:
		arg_12_0.filterEquipment()
		arg_12_0.updateCapacity()

def var_0_0.SetSpWeapons(arg_13_0, arg_13_1):
	arg_13_0.spweaponVOs = arg_13_1

def var_0_0.SetSpWeaponUpdate(arg_14_0):
	if arg_14_0.contextData.warp == StoreHouseConst.WARP_TO_WEAPON and arg_14_0.page == var_0_4:
		arg_14_0.filterEquipment()
		arg_14_0.UpdateSpweaponCapacity()
	elif arg_14_0.contextData.warp == StoreHouseConst.WARP_TO_DESIGN and arg_14_0.contextData.designPage == var_0_6:
		arg_14_0.UpdateSpweaponCapacity()

def var_0_0.didEnter(arg_15_0):
	setText(arg_15_0.findTF("tip", arg_15_0.selectPanel), i18n("equipment_select_device_destroy_tip"))
	setActive(arg_15_0.findTF("adapt/stamp", arg_15_0.topItems), getProxy(TaskProxy).mingshiTouchFlagEnabled())
	onButton(arg_15_0, arg_15_0.findTF("adapt/stamp", arg_15_0.topItems), function()
		getProxy(TaskProxy).dealMingshiTouchFlag(2), SFX_CONFIRM)
	onButton(arg_15_0, arg_15_0.helpBtn, function()
		local var_17_0

		if arg_15_0.contextData.warp == StoreHouseConst.WARP_TO_WEAPON:
			if arg_15_0.page == var_0_2:
				var_17_0 = pg.gametip.help_equipment.tip
			elif arg_15_0.page == var_0_3:
				var_17_0 = pg.gametip.help_equipment_skin.tip
			elif arg_15_0.page == var_0_4:
				var_17_0 = pg.gametip.spweapon_help_storage.tip
		elif arg_15_0.contextData.warp == StoreHouseConst.WARP_TO_DESIGN:
			if arg_15_0.contextData.designPage == var_0_5:
				var_17_0 = pg.gametip.help_equipment.tip
			elif arg_15_0.contextData.designPage == var_0_6:
				var_17_0 = pg.gametip.spweapon_help_storage.tip

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = var_17_0
		}), SFX_PANEL)
	onToggle(arg_15_0, arg_15_0.equipmentToggle.Find("equipment"), function(arg_18_0)
		if arg_18_0:
			arg_15_0.page = var_0_2

			arg_15_0.UpdateWeaponWrapButtons()
			arg_15_0.filterEquipment(), SFX_PANEL)
	onToggle(arg_15_0, arg_15_0.equipmentToggle.Find("skin"), function(arg_19_0)
		if arg_19_0:
			arg_15_0.page = var_0_3

			arg_15_0.UpdateWeaponWrapButtons()
			arg_15_0.filterEquipment(), SFX_PANEL)
	onToggle(arg_15_0, arg_15_0.equipmentToggle.Find("spweapon"), function(arg_20_0)
		if arg_20_0:
			arg_15_0.page = var_0_4

			arg_15_0.UpdateWeaponWrapButtons()
			arg_15_0.filterEquipment(), SFX_PANEL)
	setActive(arg_15_0.equipmentToggle.Find("spweapon"), not LOCK_SP_WEAPON)
	onToggle(arg_15_0, arg_15_0.designTabs[var_0_5], function(arg_21_0)
		if arg_21_0:
			arg_15_0.contextData.designPage = var_0_5

			arg_15_0.emit(EquipmentMediator.OPEN_DESIGN)
			arg_15_0.updateCapacity()
			setActive(arg_15_0.tip, False)
			setActive(arg_15_0.listEmptyTF, False)
		else
			arg_15_0.emit(EquipmentMediator.CLOSE_DESIGN_LAYER), SFX_PANEL)
	onToggle(arg_15_0, arg_15_0.designTabs[var_0_6], function(arg_22_0)
		if arg_22_0:
			arg_15_0.contextData.designPage = var_0_6

			arg_15_0.emit(EquipmentMediator.OPEN_SPWEAPON_DESIGN)
			arg_15_0.UpdateSpweaponCapacity()
			setActive(arg_15_0.tip, False)
			setActive(arg_15_0.listEmptyTF, False)
		else
			arg_15_0.emit(EquipmentMediator.CLOSE_SPWEAPON_DESIGN_LAYER), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.backBtn, function()
		if arg_15_0.mode == StoreHouseConst.DESTROY:
			triggerButton(arg_15_0.BatchDisposeBtn)

			return

		GetOrAddComponent(arg_15_0._tf, typeof(CanvasGroup)).interactable = False

		arg_15_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onToggle(arg_15_0, arg_15_0.sortBtn, function(arg_24_0)
		if arg_24_0:
			pg.UIMgr.GetInstance().OverlayPanel(arg_15_0.sortPanel, {
				groupName = LayerWeightConst.GROUP_EQUIPMENTSCENE
			})
			setActive(arg_15_0.sortPanel, True)
		else
			pg.UIMgr.GetInstance().UnOverlayPanel(arg_15_0.sortPanel, arg_15_0.topItems)
			setActive(arg_15_0.sortPanel, False), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.sortPanel, function()
		triggerToggle(arg_15_0.sortBtn, False), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.indexBtn, function()
		local var_26_0 = switch(arg_15_0.page, {
			[var_0_2] = function()
				return setmetatable({
					indexDatas = Clone(arg_15_0.contextData.indexDatas),
					def callback:(arg_28_0)
						arg_15_0.contextData.indexDatas.typeIndex = arg_28_0.typeIndex
						arg_15_0.contextData.indexDatas.equipPropertyIndex = arg_28_0.equipPropertyIndex
						arg_15_0.contextData.indexDatas.equipPropertyIndex2 = arg_28_0.equipPropertyIndex2
						arg_15_0.contextData.indexDatas.equipAmmoIndex1 = arg_28_0.equipAmmoIndex1
						arg_15_0.contextData.indexDatas.equipAmmoIndex2 = arg_28_0.equipAmmoIndex2
						arg_15_0.contextData.indexDatas.equipCampIndex = arg_28_0.equipCampIndex
						arg_15_0.contextData.indexDatas.rarityIndex = arg_28_0.rarityIndex
						arg_15_0.contextData.indexDatas.extraIndex = arg_28_0.extraIndex

						if arg_15_0.filterBusyToggle.GetComponent(typeof(Toggle)):
							if bit.band(arg_28_0.extraIndex, IndexConst.EquipmentExtraEquiping) > 0:
								arg_15_0.SetShowBusyFlag(True)

							triggerToggle(arg_15_0.filterBusyToggle, arg_15_0.GetShowBusyFlag())
						else
							arg_15_0.filterEquipment()
				}, {
					__index = StoreHouseConst.EQUIPMENT_INDEX_COMMON
				}),
			[var_0_4] = function()
				return setmetatable({
					indexDatas = Clone(arg_15_0.contextData.spweaponIndexDatas),
					def callback:(arg_30_0)
						arg_15_0.contextData.spweaponIndexDatas.typeIndex = arg_30_0.typeIndex
						arg_15_0.contextData.spweaponIndexDatas.rarityIndex = arg_30_0.rarityIndex

						arg_15_0.filterEquipment()
				}, {
					__index = StoreHouseConst.SPWEAPON_INDEX_COMMON
				})
		})

		arg_15_0.emit(EquipmentMediator.OPEN_EQUIPMENT_INDEX, var_26_0), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.equipSkinFilteBtn, function()
		local var_31_0 = {
			display = {
				equipSkinIndex = IndexConst.FlagRange2Bits(IndexConst.EquipSkinIndexAll, IndexConst.EquipSkinIndexAux),
				equipSkinTheme = IndexConst.FlagRange2Str(IndexConst.EquipSkinThemeAll, IndexConst.EquipSkinThemeEnd)
			},
			equipSkinSort = arg_15_0.equipSkinSort or IndexConst.EquipSkinSortType,
			equipSkinIndex = arg_15_0.equipSkinIndex or IndexConst.Flags2Bits({
				IndexConst.EquipSkinIndexAll
			}),
			equipSkinTheme = arg_15_0.equipSkinTheme or IndexConst.Flags2Str({
				IndexConst.EquipSkinThemeAll
			}),
			def callback:(arg_32_0)
				arg_15_0.equipSkinSort = arg_32_0.equipSkinSort
				arg_15_0.equipSkinIndex = arg_32_0.equipSkinIndex
				arg_15_0.equipSkinTheme = arg_32_0.equipSkinTheme

				arg_15_0.filterEquipment()
		}

		arg_15_0.emit(EquipmentMediator.OPEN_EQUIPSKIN_INDEX_LAYER, var_31_0), SFX_PANEL)

	arg_15_0.equipmetItems = {}
	arg_15_0.itemCards = {}

	arg_15_0.initItems()
	arg_15_0.initEquipments()

	arg_15_0.asc = arg_15_0.contextData.asc or False
	arg_15_0.contextData.sortData = arg_15_0.contextData.sortData or var_0_7.sort[1]
	arg_15_0.contextData.indexDatas = arg_15_0.contextData.indexDatas or {}
	arg_15_0.contextData.spweaponIndexDatas = arg_15_0.contextData.spweaponIndexDatas or {}
	arg_15_0.contextData.spweaponSortData = arg_15_0.contextData.spweaponSortData or var_0_8.sort[1]

	arg_15_0.initSort()
	setActive(arg_15_0.itemView, False)
	setActive(arg_15_0.equipmentView, False)
	onToggle(arg_15_0, arg_15_0.materialToggle, function(arg_33_0)
		arg_15_0.inMaterial = arg_33_0

		if arg_33_0 and arg_15_0.contextData.warp != StoreHouseConst.WARP_TO_MATERIAL:
			arg_15_0.contextData.warp = StoreHouseConst.WARP_TO_MATERIAL

			setText(arg_15_0.tip, i18n("equipment_select_materials_tip"))
			setActive(arg_15_0.capacityTF.parent, False)
			setActive(arg_15_0.tip, True)
			arg_15_0.sortItems()

		setActive(arg_15_0.helpBtn, not arg_33_0), SFX_PANEL)
	onToggle(arg_15_0, arg_15_0.weaponToggle, function(arg_34_0)
		if arg_34_0:
			if arg_15_0.contextData.warp != StoreHouseConst.WARP_TO_WEAPON:
				arg_15_0.contextData.warp = StoreHouseConst.WARP_TO_WEAPON

				setActive(arg_15_0.tip, False)
				setActive(arg_15_0.capacityTF.parent, True)

				if arg_15_0.page == var_0_3:
					triggerToggle(arg_15_0.equipmentToggle.Find("skin"), True)
				elif arg_15_0.page == var_0_4:
					triggerToggle(arg_15_0.equipmentToggle.Find("spweapon"), True)
				else
					triggerToggle(arg_15_0.equipmentToggle.Find("equipment"), True)
		else
			setActive(arg_15_0.BatchDisposeBtn, False)
			setActive(arg_15_0.filterBusyToggle, False)
			setActive(arg_15_0.equipmentToggle, False), SFX_PANEL)
	onToggle(arg_15_0, arg_15_0.designToggle, function(arg_35_0)
		if arg_35_0:
			arg_15_0.contextData.warp = StoreHouseConst.WARP_TO_DESIGN

			local var_35_0 = arg_15_0.contextData.designPage or var_0_5

			triggerToggle(arg_15_0.designTabs[var_35_0], True)
			setActive(arg_15_0.capacityTF.parent, True)
		else
			arg_15_0.emit(EquipmentMediator.CLOSE_DESIGN_LAYER)
			arg_15_0.emit(EquipmentMediator.CLOSE_SPWEAPON_DESIGN_LAYER)

		setActive(arg_15_0.designTabRoot, arg_35_0 and not LOCK_SP_WEAPON), SFX_PANEL)
	onToggle(arg_15_0, arg_15_0.filterBusyToggle, function(arg_36_0)
		arg_15_0.SetShowBusyFlag(arg_36_0)
		arg_15_0.filterEquipment(), SFX_PANEL)

	arg_15_0.filterEquipWaitting = arg_15_0.filterEquipWaitting + 1

	triggerToggle(arg_15_0.filterBusyToggle, arg_15_0.shipVO)
	onButton(arg_15_0, arg_15_0.BatchDisposeBtn, function()
		if arg_15_0.mode == StoreHouseConst.DESTROY:
			arg_15_0.mode = StoreHouseConst.OVERVIEW
			arg_15_0.asc = arg_15_0.lastasc
			arg_15_0.lastasc = None
			arg_15_0.filterImportance = None

			shiftPanel(arg_15_0.bottomBack, None, 0, None, 0, True, True)
			shiftPanel(arg_15_0.selectPanel, None, -124, None, 0, True, True)
			arg_15_0.filterEquipment()
		else
			arg_15_0.mode = StoreHouseConst.DESTROY
			arg_15_0.lastasc = arg_15_0.asc
			arg_15_0.filterImportance = True
			arg_15_0.asc = True

			shiftPanel(arg_15_0.bottomBack, None, -124, None, 0, True, True)
			shiftPanel(arg_15_0.selectPanel, None, 0, None, 0, True, True)

			arg_15_0.contextData.asc = arg_15_0.asc
			arg_15_0.contextData.sortData = var_0_7.sort[1]

			arg_15_0.filterEquipment()

		arg_15_0.UpdateWeaponWrapButtons(), SFX_PANEL)
	onButton(arg_15_0, findTF(arg_15_0.selectPanel, "cancel_button"), function()
		arg_15_0.unselecteAllEquips()
		triggerButton(arg_15_0.BatchDisposeBtn), SFX_CANCEL)
	onButton(arg_15_0, findTF(arg_15_0.selectPanel, "confirm_button"), function()
		local var_39_0 = {}

		if underscore.any(arg_15_0.selectedIds, function(arg_40_0)
			local var_40_0 = arg_15_0.equipmentVOByIds[arg_40_0[1]]

			return var_40_0.getConfig("rarity") >= 4 or var_40_0.getConfig("level") > 1):
			table.insert(var_39_0, function(arg_41_0)
				arg_15_0.equipDestroyConfirmWindow.Load()
				arg_15_0.equipDestroyConfirmWindow.ActionInvoke("Show", underscore.map(arg_15_0.selectedIds, function(arg_42_0)
					return setmetatable({
						count = arg_42_0[2]
					}, {
						__index = arg_15_0.equipmentVOByIds[arg_42_0[1]]
					})), arg_41_0))

		seriesAsync(var_39_0, function()
			arg_15_0.destroyConfirmView.Load()
			arg_15_0.destroyConfirmView.ActionInvoke("Show")
			arg_15_0.destroyConfirmView.ActionInvoke("DisplayDestroyBonus", arg_15_0.selectedIds)
			arg_15_0.destroyConfirmView.ActionInvoke("SetConfirmBtnCB", function()
				arg_15_0.unselecteAllEquips())), SFX_CONFIRM)
	pg.UIMgr.GetInstance().OverlayPanel(arg_15_0.blurPanel, {
		groupName = LayerWeightConst.GROUP_EQUIPMENTSCENE
	})
	pg.UIMgr.GetInstance().OverlayPanel(arg_15_0.topItems, {
		groupName = LayerWeightConst.GROUP_EQUIPMENTSCENE
	})

	local var_15_0 = arg_15_0.contextData.warp or StoreHouseConst.WARP_TO_MATERIAL
	local var_15_1 = arg_15_0.contextData.mode or StoreHouseConst.OVERVIEW

	arg_15_0.contextData.warp = None
	arg_15_0.contextData.mode = None
	arg_15_0.mode = arg_15_0.mode or StoreHouseConst.OVERVIEW

	if var_15_0 == StoreHouseConst.WARP_TO_DESIGN:
		triggerToggle(arg_15_0.designToggle, True)
	elif var_15_0 == StoreHouseConst.WARP_TO_MATERIAL:
		triggerToggle(arg_15_0.materialToggle, True)
	elif var_15_0 == StoreHouseConst.WARP_TO_WEAPON:
		if var_15_1 == StoreHouseConst.DESTROY:
			arg_15_0.filterEquipWaitting = arg_15_0.filterEquipWaitting + 1

			triggerToggle(arg_15_0.weaponToggle, True)
			triggerButton(arg_15_0.BatchDisposeBtn)
		else
			if var_15_1 == StoreHouseConst.SKIN:
				arg_15_0.page = var_0_3
			elif var_15_1 == StoreHouseConst.SPWEAPON:
				arg_15_0.page = var_0_4
			else
				arg_15_0.page = var_0_2

			triggerToggle(arg_15_0.weaponToggle, True)

	arg_15_0.bulinTip = AprilFoolBulinSubView.ShowAprilFoolBulin(arg_15_0, arg_15_0.topItems)

def var_0_0.isDefaultStatus(arg_45_0):
	return underscore(arg_45_0.contextData.indexDatas).chain().keys().all(function(arg_46_0)
		return arg_45_0.contextData.indexDatas[arg_46_0] == StoreHouseConst.EQUIPMENT_INDEX_COMMON.customPanels[arg_46_0].options[1]).value()

def var_0_0.isDefaultSpWeaponIndexData(arg_47_0):
	return underscore(arg_47_0.contextData.spweaponIndexDatas).chain().keys().all(function(arg_48_0)
		return arg_47_0.contextData.spweaponIndexDatas[arg_48_0] == StoreHouseConst.SPWEAPON_INDEX_COMMON.customPanels[arg_48_0].options[1]).value()

def var_0_0.onBackPressed(arg_49_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	if isActive(arg_49_0.sortPanel):
		triggerButton(arg_49_0.sortPanel)
	elif arg_49_0.destroyConfirmView.isShowing():
		arg_49_0.destroyConfirmView.Hide()
	elif arg_49_0.assignedItemView.isShowing():
		arg_49_0.assignedItemView.Hide()
	elif arg_49_0.blueprintAssignedItemView.isShowing():
		arg_49_0.blueprintAssignedItemView.Hide()
	elif arg_49_0.equipDestroyConfirmWindow.isShowing():
		arg_49_0.equipDestroyConfirmWindow.Hide()
	else
		triggerButton(arg_49_0.backBtn)

def var_0_0.updateCapacity(arg_50_0):
	if arg_50_0.contextData.warp == StoreHouseConst.WARP_TO_MATERIAL:
		return

	setText(arg_50_0.tip, "")
	setText(arg_50_0.capacityTF, arg_50_0.capacity .. "/" .. arg_50_0.player.getMaxEquipmentBag())

def var_0_0.setCapacity(arg_51_0, arg_51_1):
	arg_51_0.capacity = arg_51_1

def var_0_0.UpdateSpweaponCapacity(arg_52_0):
	local var_52_0 = getProxy(EquipmentProxy)

	setText(arg_52_0.capacityTF, var_52_0.GetSpWeaponCount() .. "/" .. var_52_0.GetSpWeaponCapacity())

def var_0_0.setShip(arg_53_0, arg_53_1):
	arg_53_0.shipVO = arg_53_1

	setActive(arg_53_0.bottomPanel, not tobool(arg_53_1))

def var_0_0.setPlayer(arg_54_0, arg_54_1):
	arg_54_0.player = arg_54_1

	if arg_54_0.contextData.warp == StoreHouseConst.WARP_TO_WEAPON and arg_54_0.page == var_0_2:
		arg_54_0.updateCapacity()
	elif arg_54_0.contextData.warp == StoreHouseConst.WARP_TO_DESIGN and arg_54_0.contextData.designPage == var_0_5:
		arg_54_0.updateCapacity()

def var_0_0.initSort(arg_55_0):
	onButton(arg_55_0, arg_55_0.decBtn, function()
		arg_55_0.asc = not arg_55_0.asc
		arg_55_0.contextData.asc = arg_55_0.asc

		arg_55_0.filterEquipment())

	arg_55_0.sortButtons = {}

	eachChild(arg_55_0.sortContain, function(arg_57_0)
		setActive(arg_57_0, False))

	for iter_55_0, iter_55_1 in ipairs(var_0_7.sort):
		local var_55_0 = iter_55_0 <= arg_55_0.sortContain.childCount and arg_55_0.sortContain.GetChild(iter_55_0 - 1) or cloneTplTo(arg_55_0.sortTpl, arg_55_0.sortContain)

		setActive(var_55_0, True)
		setImageSprite(findTF(var_55_0, "Image"), GetSpriteFromAtlas("ui/equipmentui_atlas", iter_55_1.spr), True)
		onToggle(arg_55_0, var_55_0, function(arg_58_0)
			if arg_58_0:
				if arg_55_0.page == var_0_2:
					arg_55_0.contextData.sortData = iter_55_1
				elif arg_55_0.page == var_0_4:
					arg_55_0.contextData.spweaponSortData = var_0_8.sort[iter_55_0]

				arg_55_0.filterEquipment()
				triggerToggle(arg_55_0.sortBtn, False), SFX_PANEL)

		arg_55_0.sortButtons[iter_55_0] = var_55_0

def var_0_0.UpdateWeaponWrapButtons(arg_59_0):
	local var_59_0 = arg_59_0.page

	setActive(arg_59_0.indexBtn, var_59_0 == var_0_2 or var_59_0 == var_0_4)
	setActive(arg_59_0.sortBtn, var_59_0 == var_0_2 or var_59_0 == var_0_4)
	setActive(arg_59_0.BatchDisposeBtn, var_59_0 == var_0_2)
	setActive(arg_59_0.capacityTF.parent, var_59_0 == var_0_2 or var_59_0 == var_0_4)
	setActive(arg_59_0.equipSkinFilteBtn, var_59_0 == var_0_3)
	setActive(arg_59_0.filterBusyToggle, arg_59_0.mode == StoreHouseConst.OVERVIEW)
	setActive(arg_59_0.equipmentToggle, arg_59_0.mode == StoreHouseConst.OVERVIEW and not arg_59_0.contextData.shipId)
	arg_59_0.updatePageFilterButtons(var_59_0)

def var_0_0.updatePageFilterButtons(arg_60_0, arg_60_1):
	for iter_60_0, iter_60_1 in ipairs(var_0_7.sort):
		triggerToggle(arg_60_0.sortButtons[iter_60_0], False)
		setActive(arg_60_0.sortButtons[iter_60_0], table.contains(iter_60_1.pages, arg_60_1))

def var_0_0.initEquipments(arg_61_0):
	arg_61_0.isInitWeapons = True
	arg_61_0.equipmentRect = arg_61_0.equipmentView.GetComponent("LScrollRect")

	function arg_61_0.equipmentRect.onInitItem(arg_62_0)
		arg_61_0.initEquipment(arg_62_0)

	function arg_61_0.equipmentRect.onUpdateItem(arg_63_0, arg_63_1)
		arg_61_0.updateEquipment(arg_63_0, arg_63_1)

	function arg_61_0.equipmentRect.onReturnItem(arg_64_0, arg_64_1)
		arg_61_0.returnEquipment(arg_64_0, arg_64_1)

	function arg_61_0.equipmentRect.onStart()
		arg_61_0.updateSelected()

	arg_61_0.equipmentRect.decelerationRate = 0.07

def var_0_0.initEquipment(arg_66_0, arg_66_1):
	local var_66_0 = EquipmentItem.New(arg_66_1)

	onButton(arg_66_0, var_66_0.unloadBtn, function()
		if arg_66_0.page == var_0_3:
			arg_66_0.emit(EquipmentMediator.ON_UNEQUIP_EQUIPMENT_SKIN)
		elif arg_66_0.page == var_0_2:
			arg_66_0.emit(EquipmentMediator.ON_UNEQUIP_EQUIPMENT), SFX_PANEL)
	onButton(arg_66_0, var_66_0.reduceBtn, function()
		arg_66_0.selectEquip(var_66_0.equipmentVO, 1), SFX_PANEL)

	arg_66_0.equipmetItems[arg_66_1] = var_66_0

def var_0_0.updateEquipment(arg_69_0, arg_69_1, arg_69_2):
	local var_69_0 = arg_69_0.equipmetItems[arg_69_2]

	assert(var_69_0, "without init item")

	local var_69_1 = arg_69_0.loadEquipmentVOs[arg_69_1 + 1]

	var_69_0.update(var_69_1)

	local var_69_2 = False
	local var_69_3 = 0

	if var_69_1:
		for iter_69_0, iter_69_1 in ipairs(arg_69_0.selectedIds):
			if var_69_1.id == iter_69_1[1]:
				var_69_2 = True
				var_69_3 = iter_69_1[2]

				break

	var_69_0.updateSelected(var_69_2, var_69_3)

	if not var_69_1:
		removeOnButton(var_69_0.go)
	elif isa(var_69_1, SpWeapon):
		onButton(arg_69_0, var_69_0.go, function()
			local var_70_0 = arg_69_0.shipVO and {
				type = EquipmentInfoMediator.TYPE_REPLACE,
				shipId = arg_69_0.contextData.shipId,
				oldSpWeaponUid = var_69_1.GetUID(),
				oldShipId = var_69_1.GetShipId()
			} or var_69_1.GetShipId() and {
				type = EquipmentInfoMediator.TYPE_DISPLAY,
				spWeaponUid = var_69_1.GetUID(),
				shipId = var_69_1.GetShipId()
			} or {
				type = EquipmentInfoMediator.TYPE_DEFAULT,
				spWeaponUid = var_69_1.GetUID()
			}

			arg_69_0.emit(var_0_0.ON_SPWEAPON, var_70_0), SFX_PANEL)
	elif var_69_0.equipmentVO.isSkin:
		if var_69_1.shipId:
			onButton(arg_69_0, var_69_0.go, function()
				local var_71_0 = var_69_1.shipId
				local var_71_1 = var_69_1.shipPos

				assert(var_71_1, "equipment skin pos is None")
				arg_69_0.emit(EquipmentMediator.ON_EQUIPMENT_SKIN_INFO, var_69_1.id, arg_69_0.contextData.pos, {
					id = var_71_0,
					pos = var_71_1
				}), SFX_PANEL)
		else
			onButton(arg_69_0, var_69_0.go, function()
				arg_69_0.emit(EquipmentMediator.ON_EQUIPMENT_SKIN_INFO, var_69_1.id, arg_69_0.contextData.pos), SFX_PANEL)
	elif var_69_1.mask:
		removeOnButton(var_69_0.go)
	elif arg_69_0.mode == StoreHouseConst.DESTROY:
		onButton(arg_69_0, var_69_0.go, function()
			arg_69_0.selectEquip(var_69_1, var_69_1.count), SFX_PANEL)
	else
		onButton(arg_69_0, var_69_0.go, function()
			local var_74_0 = arg_69_0.shipVO and {
				type = EquipmentInfoMediator.TYPE_REPLACE,
				equipmentId = var_69_1.id,
				shipId = arg_69_0.contextData.shipId,
				pos = arg_69_0.contextData.pos,
				oldShipId = var_69_1.shipId,
				oldPos = var_69_1.shipPos
			} or var_69_1.shipId and {
				showTransformTip = True,
				type = EquipmentInfoMediator.TYPE_DISPLAY,
				equipmentId = var_69_1.id,
				shipId = var_69_1.shipId,
				pos = var_69_1.shipPos
			} or {
				destroy = True,
				type = EquipmentInfoMediator.TYPE_DEFAULT,
				equipmentId = var_69_1.id
			}

			arg_69_0.emit(var_0_0.ON_EQUIPMENT, var_74_0), SFX_PANEL)

def var_0_0.returnEquipment(arg_75_0, arg_75_1, arg_75_2):
	if arg_75_0.exited:
		return

	local var_75_0 = arg_75_0.equipmetItems[arg_75_2]

	if var_75_0:
		removeOnButton(var_75_0.go)
		var_75_0.clear()

def var_0_0.updateEquipmentCount(arg_76_0, arg_76_1):
	arg_76_0.equipmentRect.SetTotalCount(arg_76_1 or #arg_76_0.loadEquipmentVOs, -1)
	setActive(arg_76_0.listEmptyTF, (arg_76_1 or #arg_76_0.loadEquipmentVOs) <= 0)
	setText(arg_76_0.listEmptyTxt, i18n("list_empty_tip_storehouseui_equip"))
	Canvas.ForceUpdateCanvases()

def var_0_0.filterEquipment(arg_77_0):
	if arg_77_0.filterEquipWaitting > 0:
		arg_77_0.filterEquipWaitting = arg_77_0.filterEquipWaitting - 1

		return

	if arg_77_0.page == var_0_3:
		arg_77_0.filterEquipSkin()

		return
	elif arg_77_0.page == var_0_4:
		arg_77_0.filterSpWeapon()

		return

	local var_77_0 = arg_77_0.isDefaultStatus() and "shaixuan_off" or "shaixuan_on"

	GetSpriteFromAtlasAsync("ui/share/index_atlas", var_77_0, function(arg_78_0)
		setImageSprite(arg_77_0.indexBtn, arg_78_0, True))

	local var_77_1 = {}

	arg_77_0.loadEquipmentVOs = {}

	for iter_77_0, iter_77_1 in pairs(arg_77_0.equipmentVOs):
		if not iter_77_1.isSkin:
			table.insert(var_77_1, iter_77_1)

	local var_77_2 = {
		arg_77_0.contextData.indexDatas.equipPropertyIndex,
		arg_77_0.contextData.indexDatas.equipPropertyIndex2
	}

	for iter_77_2, iter_77_3 in pairs(var_77_1):
		if (iter_77_3.count > 0 or iter_77_3.shipId) and arg_77_0.checkFitBusyCondition(iter_77_3) and IndexConst.filterEquipByType(iter_77_3, arg_77_0.contextData.indexDatas.typeIndex) and IndexConst.filterEquipByProperty(iter_77_3, var_77_2) and IndexConst.filterEquipAmmo1(iter_77_3, arg_77_0.contextData.indexDatas.equipAmmoIndex1) and IndexConst.filterEquipAmmo2(iter_77_3, arg_77_0.contextData.indexDatas.equipAmmoIndex2) and IndexConst.filterEquipByCamp(iter_77_3, arg_77_0.contextData.indexDatas.equipCampIndex) and IndexConst.filterEquipByRarity(iter_77_3, arg_77_0.contextData.indexDatas.rarityIndex) and IndexConst.filterEquipByExtra(iter_77_3, arg_77_0.contextData.indexDatas.extraIndex):
			table.insert(arg_77_0.loadEquipmentVOs, iter_77_3)

	if arg_77_0.filterImportance != None:
		for iter_77_4 = #arg_77_0.loadEquipmentVOs, 1, -1:
			local var_77_3 = arg_77_0.loadEquipmentVOs[iter_77_4]

			if var_77_3.isSkin or not var_77_3.isSkin and var_77_3.isImportance():
				table.remove(arg_77_0.loadEquipmentVOs, iter_77_4)

	local var_77_4 = arg_77_0.contextData.sortData

	if var_77_4:
		local var_77_5 = arg_77_0.asc

		table.sort(arg_77_0.loadEquipmentVOs, CompareFuncs(var_0_7.sortFunc(var_77_4, var_77_5)))

	if arg_77_0.contextData.qiutBtn:
		table.insert(arg_77_0.loadEquipmentVOs, 1, False)

	arg_77_0.updateSelected()
	arg_77_0.updateEquipmentCount()
	setImageSprite(arg_77_0.findTF("Image", arg_77_0.sortBtn), GetSpriteFromAtlas("ui/equipmentui_atlas", var_77_4.spr), True)
	setActive(arg_77_0.sortImgAsc, arg_77_0.asc)
	setActive(arg_77_0.sortImgDec, not arg_77_0.asc)
	arg_77_0.updateCapacity()

def var_0_0.filterEquipSkin(arg_79_0):
	local var_79_0 = arg_79_0.equipSkinIndex
	local var_79_1 = arg_79_0.equipSkinTheme
	local var_79_2 = arg_79_0.page
	local var_79_3 = {}

	arg_79_0.loadEquipmentVOs = {}

	if var_79_2 != var_0_3:
		assert(False, "不是外观分页")

	for iter_79_0, iter_79_1 in pairs(arg_79_0.equipmentVOs):
		if iter_79_1.isSkin and iter_79_1.count > 0:
			table.insert(var_79_3, iter_79_1)

	for iter_79_2, iter_79_3 in pairs(var_79_3):
		if IndexConst.filterEquipSkinByIndex(iter_79_3, var_79_0) and IndexConst.filterEquipSkinByTheme(iter_79_3, var_79_1) and arg_79_0.checkFitBusyCondition(iter_79_3):
			table.insert(arg_79_0.loadEquipmentVOs, iter_79_3)

	if arg_79_0.filterImportance != None:
		for iter_79_4 = #arg_79_0.loadEquipmentVOs, 1, -1:
			local var_79_4 = arg_79_0.loadEquipmentVOs[iter_79_4]

			if var_79_4.isSkin or not var_79_4.isSkin and var_79_4.isImportance():
				table.remove(arg_79_0.loadEquipmentVOs, iter_79_4)

	local var_79_5 = arg_79_0.contextData.sortData

	if var_79_5:
		local var_79_6 = arg_79_0.asc

		table.sort(arg_79_0.loadEquipmentVOs, CompareFuncs(var_0_7.sortFunc(var_79_5, var_79_6)))

	if arg_79_0.contextData.qiutBtn:
		table.insert(arg_79_0.loadEquipmentVOs, 1, False)

	arg_79_0.updateSelected()
	arg_79_0.updateEquipmentCount()
	setActive(arg_79_0.sortImgAsc, arg_79_0.asc)
	setActive(arg_79_0.sortImgDec, not arg_79_0.asc)

def var_0_0.filterSpWeapon(arg_80_0):
	if arg_80_0.page != var_0_4:
		assert(False, "不是特殊兵装分页")

	local var_80_0 = arg_80_0.isDefaultSpWeaponIndexData() and "shaixuan_off" or "shaixuan_on"

	GetSpriteFromAtlasAsync("ui/share/index_atlas", var_80_0, function(arg_81_0)
		setImageSprite(arg_80_0.indexBtn, arg_81_0, True))

	arg_80_0.loadEquipmentVOs = {}

	local var_80_1 = arg_80_0.contextData.spweaponIndexDatas.typeIndex
	local var_80_2 = arg_80_0.contextData.spweaponIndexDatas.rarityIndex

	for iter_80_0, iter_80_1 in pairs(arg_80_0.spweaponVOs):
		if IndexConst.filterSpWeaponByType(iter_80_1, var_80_1) and IndexConst.filterSpWeaponByRarity(iter_80_1, var_80_2) and arg_80_0.checkFitBusyCondition(iter_80_1) and (arg_80_0.filterImportance == None or iter_80_1.IsImportant()):
			table.insert(arg_80_0.loadEquipmentVOs, iter_80_1)

	local var_80_3 = arg_80_0.contextData.spweaponSortData

	if var_80_3:
		local var_80_4 = arg_80_0.asc

		table.sort(arg_80_0.loadEquipmentVOs, CompareFuncs(var_0_8.sortFunc(var_80_3, var_80_4)))

	if arg_80_0.contextData.qiutBtn:
		table.insert(arg_80_0.loadEquipmentVOs, 1, False)

	arg_80_0.updateSelected()
	arg_80_0.updateEquipmentCount()
	setImageSprite(arg_80_0.findTF("Image", arg_80_0.sortBtn), GetSpriteFromAtlas("ui/equipmentui_atlas", var_80_3.spr), True)
	setActive(arg_80_0.sortImgAsc, arg_80_0.asc)
	setActive(arg_80_0.sortImgDec, not arg_80_0.asc)
	arg_80_0.UpdateSpweaponCapacity()

def var_0_0.GetShowBusyFlag(arg_82_0):
	return arg_82_0.isEquipingOn

def var_0_0.SetShowBusyFlag(arg_83_0, arg_83_1):
	arg_83_0.isEquipingOn = arg_83_1

def var_0_0.Scroll2Equip(arg_84_0, arg_84_1):
	if arg_84_0.contextData.warp != StoreHouseConst.WARP_TO_WEAPON or arg_84_0.page != var_0_2:
		return

	for iter_84_0, iter_84_1 in ipairs(arg_84_0.loadEquipmentVOs):
		if EquipmentProxy.SameEquip(iter_84_1, arg_84_1):
			local var_84_0 = arg_84_0.equipmentView.Find("equipment_grid").GetComponent(typeof(GridLayoutGroup))
			local var_84_1 = (var_84_0.cellSize.y + var_84_0.spacing.y) * math.floor((iter_84_0 - 1) / var_84_0.constraintCount) + arg_84_0.equipmentRect.paddingFront + arg_84_0.equipmentView.rect.height * 0.5

			arg_84_0.ScrollEquipPos(var_84_1 - arg_84_0.equipmentRect.paddingFront)

			break

def var_0_0.ScrollEquipPos(arg_85_0, arg_85_1):
	local var_85_0 = arg_85_0.equipmentView.Find("equipment_grid").GetComponent(typeof(GridLayoutGroup))
	local var_85_1 = (var_85_0.cellSize.y + var_85_0.spacing.y) * math.ceil(#arg_85_0.loadEquipmentVOs / var_85_0.constraintCount) - var_85_0.spacing.y + arg_85_0.equipmentRect.paddingFront + arg_85_0.equipmentRect.paddingEnd
	local var_85_2 = var_85_1 - arg_85_0.equipmentView.rect.height

	var_85_2 = var_85_2 > 0 and var_85_2 or var_85_1

	local var_85_3 = (arg_85_1 - arg_85_0.equipmentView.rect.height * 0.5) / var_85_2

	arg_85_0.equipmentRect.ScrollTo(var_85_3)

def var_0_0.checkFitBusyCondition(arg_86_0, arg_86_1):
	return not arg_86_1.shipId or arg_86_0.GetShowBusyFlag() and arg_86_0.mode != StoreHouseConst.DESTROY

def var_0_0.setItems(arg_87_0, arg_87_1):
	arg_87_0.itemVOs = arg_87_1

	if arg_87_0.isInitItems and arg_87_0.contextData.warp == StoreHouseConst.WARP_TO_MATERIAL:
		arg_87_0.sortItems()

def var_0_0.initItems(arg_88_0):
	arg_88_0.isInitItems = True
	arg_88_0.itemRect = arg_88_0.itemView.GetComponent("LScrollRect")

	function arg_88_0.itemRect.onInitItem(arg_89_0)
		arg_88_0.initItem(arg_89_0)

	function arg_88_0.itemRect.onUpdateItem(arg_90_0, arg_90_1)
		arg_88_0.updateItem(arg_90_0, arg_90_1)

	function arg_88_0.itemRect.onReturnItem(arg_91_0, arg_91_1)
		arg_88_0.returnItem(arg_91_0, arg_91_1)

	arg_88_0.itemRect.decelerationRate = 0.07

def var_0_0.sortItems(arg_92_0):
	table.sort(arg_92_0.itemVOs, CompareFuncs({
		function(arg_93_0)
			return -arg_93_0.getConfig("order"),
		function(arg_94_0)
			return -arg_94_0.getConfig("rarity"),
		function(arg_95_0)
			return arg_95_0.id
	}))
	arg_92_0.itemRect.SetTotalCount(#arg_92_0.itemVOs, -1)
	setActive(arg_92_0.listEmptyTF, #arg_92_0.itemVOs <= 0)
	setText(arg_92_0.listEmptyTxt, i18n("list_empty_tip_storehouseui_item"))
	Canvas.ForceUpdateCanvases()

def var_0_0.initItem(arg_96_0, arg_96_1):
	arg_96_0.itemCards[arg_96_1] = ItemCard.New(arg_96_1)

def var_0_0.updateItem(arg_97_0, arg_97_1, arg_97_2):
	local var_97_0 = arg_97_0.itemCards[arg_97_2]

	assert(var_97_0, "without init item")

	local var_97_1 = arg_97_0.itemVOs[arg_97_1 + 1]

	var_97_0.update(var_97_1)

	if not var_97_1:
		removeOnButton(var_97_0.go)
	elif tobool(getProxy(TechnologyProxy).getItemCanUnlockBluePrint(var_97_1.id)):
		local var_97_2 = getProxy(TechnologyProxy)
		local var_97_3 = underscore.map(var_97_2.getItemCanUnlockBluePrint(var_97_1.id), function(arg_98_0)
			return var_97_2.getBluePrintById(arg_98_0))
		local var_97_4 = underscore.detect(var_97_3, function(arg_99_0)
			return not arg_99_0.isUnlock())

		if var_97_4:
			onButton(arg_97_0, var_97_0.go, function()
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					type = MSGBOX_TYPE_BLUEPRINT_UNLOCK_ITEM,
					item = var_97_1,
					blueprints = var_97_3,
					def onYes:()
						arg_97_0.emit(EquipmentMediator.ITEM_GO_SCENE, SCENE.SHIPBLUEPRINT, {
							shipBluePrintVO = var_97_4
						}),
					yesText = i18n("text_forward")
				}), SFX_PANEL)
		else
			onButton(arg_97_0, var_97_0.go, function()
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					type = MSGBOX_TYPE_BLUEPRINT_UNLOCK_ITEM,
					windowSize = Vector2(1010, 685),
					item = var_97_1,
					blueprints = var_97_3,
					def onYes:()
						pg.MsgboxMgr.GetInstance().ShowMsgBox({
							type = MSGBOX_TYPE_ITEM_BOX,
							content = i18n("techpackage_item_use_confirm"),
							items = underscore.map(var_97_1.getConfig("display_icon"), function(arg_104_0)
								return {
									type = arg_104_0[1],
									id = arg_104_0[2],
									count = arg_104_0[3]
								}),
							def onYes:()
								arg_97_0.emit(EquipmentMediator.ON_USE_ITEM, var_97_1.id, 1)
						})
				}), SFX_PANEL)
	elif var_97_1.getConfig("type") == Item.INVITATION_TYPE:
		onButton(arg_97_0, var_97_0.go, function()
			arg_97_0.emit(EquipmentMediator.ITEM_GO_SCENE, SCENE.INVITATION, {
				itemVO = var_97_1
			}), SFX_PANEL)
	elif var_97_1.getConfig("type") == Item.ASSIGNED_TYPE or var_97_1.getConfig("type") == Item.EQUIPMENT_ASSIGNED_TYPE:
		if underscore.any(pg.gameset.general_blueprint_list.description, function(arg_107_0)
			return var_97_1.id == arg_107_0):
			onButton(arg_97_0, var_97_0.go, function()
				arg_97_0.blueprintAssignedItemView.Load()
				arg_97_0.blueprintAssignedItemView.ActionInvoke("Show")
				arg_97_0.blueprintAssignedItemView.ActionInvoke("update", var_97_1), SFX_PANEL)
		else
			onButton(arg_97_0, var_97_0.go, function()
				arg_97_0.assignedItemView.Load()
				arg_97_0.assignedItemView.ActionInvoke("Show")
				arg_97_0.assignedItemView.ActionInvoke("update", var_97_1), SFX_PANEL)
	elif var_97_1.getConfig("type") == Item.LOVE_LETTER_TYPE:
		onButton(arg_97_0, var_97_0.go, function()
			arg_97_0.emit(var_0_0.ON_ITEM_EXTRA, var_97_1.id, var_97_1.extra), SFX_PANEL)
	elif var_97_1.getConfig("type") == Item.SKIN_ASSIGNED_TYPE:
		onButton(arg_97_0, var_97_0.go, function()
			arg_97_0.emit(var_0_0.ON_ITEM, var_97_1.id, function()
				local var_112_0 = var_97_1.getConfig("usage_arg")

				if var_97_1.IsAllSkinOwner():
					local var_112_1 = Drop.New({
						count = 1,
						type = DROP_TYPE_ITEM,
						id = var_112_0[5]
					})

					arg_97_0.msgBox.ExecuteAction("Show", {
						content = i18n("blackfriday_pack_select_skinall_dialog", var_97_1.getConfig("name"), var_112_1.getName()),
						leftDrop = {
							count = 1,
							type = DROP_TYPE_ITEM,
							id = var_97_1.id
						},
						rightDrop = var_112_1,
						def onYes:()
							arg_97_0.emit(EquipmentMediator.ON_USE_ITEM, var_97_1.id, 1, {
								0
							})
					})
				else
					local var_112_2 = {}

					for iter_112_0, iter_112_1 in ipairs(var_112_0[2]):
						var_112_2[iter_112_1] = True

					arg_97_0.emit(EquipmentMediator.ITEM_ADD_LAYER, Context.New({
						viewComponent = SelectSkinLayer,
						mediator = SkinAtlasMediator,
						data = {
							mode = SelectSkinLayer.MODE_SELECT,
							itemId = var_97_1.id,
							selectableSkinList = underscore.map(var_97_1.GetValidSkinList(), function(arg_114_0)
								return SelectableSkin.New({
									id = arg_114_0,
									isTimeLimit = var_112_2[arg_114_0] or False
								})),
							def OnConfirm:(arg_115_0)
								arg_97_0.emit(EquipmentMediator.ON_USE_ITEM, var_97_1.id, 1, {
									arg_115_0
								})
						}
					}))), SFX_PANEL)
	else
		onButton(arg_97_0, var_97_0.go, function()
			arg_97_0.emit(var_0_0.ON_ITEM, var_97_1.id), SFX_PANEL)

def var_0_0.returnItem(arg_117_0, arg_117_1, arg_117_2):
	if arg_117_0.exited:
		return

	local var_117_0 = arg_117_0.itemCards[arg_117_2]

	if var_117_0:
		removeOnButton(var_117_0.go)
		var_117_0.clear()

def var_0_0.selectCount(arg_118_0):
	local var_118_0 = 0

	for iter_118_0, iter_118_1 in ipairs(arg_118_0.selectedIds):
		var_118_0 = var_118_0 + iter_118_1[2]

	return var_118_0

def var_0_0.selectEquip(arg_119_0, arg_119_1, arg_119_2):
	if not arg_119_0.checkDestroyGold(arg_119_1, arg_119_2):
		return

	if arg_119_0.mode == StoreHouseConst.DESTROY:
		local var_119_0 = False
		local var_119_1
		local var_119_2 = 0

		for iter_119_0, iter_119_1 in pairs(arg_119_0.selectedIds):
			if iter_119_1[1] == arg_119_1.id:
				var_119_0 = True
				var_119_1 = iter_119_0
				var_119_2 = iter_119_1[2]

				break

		if not var_119_0:
			local var_119_3, var_119_4 = arg_119_0.checkEquipment(arg_119_1, function()
				arg_119_0.selectEquip(arg_119_1, arg_119_2), arg_119_0.selectedIds)

			if not var_119_3:
				if var_119_4:
					pg.TipsMgr.GetInstance().ShowTips(var_119_4)

				return

			local var_119_5 = arg_119_0.selectCount()

			if arg_119_0.selectedMax > 0 and var_119_5 + arg_119_2 > arg_119_0.selectedMax:
				arg_119_2 = arg_119_0.selectedMax - var_119_5

			if arg_119_0.selectedMax == 0 or var_119_5 < arg_119_0.selectedMax:
				table.insert(arg_119_0.selectedIds, {
					arg_119_1.id,
					arg_119_2
				})
			elif arg_119_0.selectedMax == 1:
				arg_119_0.selectedIds[1] = {
					arg_119_1.id,
					arg_119_2
				}
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_equipmentScene_selectError_more", arg_119_0.selectedMax))

				return
		elif var_119_2 - arg_119_2 > 0:
			arg_119_0.selectedIds[var_119_1][2] = var_119_2 - arg_119_2
		else
			table.remove(arg_119_0.selectedIds, var_119_1)

	arg_119_0.updateSelected()

def var_0_0.unselecteAllEquips(arg_121_0):
	arg_121_0.selectedIds = {}

	arg_121_0.updateSelected()

def var_0_0.checkDestroyGold(arg_122_0, arg_122_1, arg_122_2):
	local var_122_0 = 0
	local var_122_1 = False

	for iter_122_0, iter_122_1 in pairs(arg_122_0.selectedIds):
		local var_122_2 = iter_122_1[2]

		if Equipment.CanInBag(iter_122_1[1]):
			var_122_0 = var_122_0 + (Equipment.getConfigData(iter_122_1[1]).destory_gold or 0) * var_122_2

		if arg_122_1 and iter_122_1[1] == arg_122_1.configId:
			var_122_1 = True

	if not var_122_1 and arg_122_1 and arg_122_2 > 0:
		var_122_0 = var_122_0 + (arg_122_1.getConfig("destory_gold") or 0) * arg_122_2

	if arg_122_0.player.GoldMax(var_122_0):
		pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_destroy"))

		return False

	return True

def var_0_0.updateSelected(arg_123_0):
	for iter_123_0, iter_123_1 in pairs(arg_123_0.equipmetItems):
		if iter_123_1.equipmentVO:
			local var_123_0 = False
			local var_123_1 = 0

			for iter_123_2, iter_123_3 in pairs(arg_123_0.selectedIds):
				if iter_123_1.equipmentVO.id == iter_123_3[1]:
					var_123_0 = True
					var_123_1 = iter_123_3[2]

					break

			iter_123_1.updateSelected(var_123_0, var_123_1)

	if arg_123_0.mode == StoreHouseConst.DESTROY:
		local var_123_2 = arg_123_0.selectCount()

		if arg_123_0.selectedMax == 0:
			setText(findTF(arg_123_0.selectPanel, "bottom_info/bg_input/count"), var_123_2)
		else
			setText(findTF(arg_123_0.selectPanel, "bottom_info/bg_input/count"), var_123_2 .. "/" .. arg_123_0.selectedMax)

		if #arg_123_0.selectedIds < arg_123_0.selectedMin:
			setActive(findTF(arg_123_0.selectPanel, "confirm_button/mask"), True)
		else
			setActive(findTF(arg_123_0.selectPanel, "confirm_button/mask"), False)

def var_0_0.SwitchToDestroy(arg_124_0):
	arg_124_0.page = var_0_2
	arg_124_0.filterEquipWaitting = arg_124_0.filterEquipWaitting + 1

	triggerToggle(arg_124_0.weaponToggle, True)
	triggerButton(arg_124_0.BatchDisposeBtn)

def var_0_0.SwitchToSpWeaponStoreHouse(arg_125_0):
	arg_125_0.page = var_0_4

	triggerToggle(arg_125_0.weaponToggle, True)

def var_0_0.willExit(arg_126_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_126_0.blurPanel, arg_126_0._tf)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_126_0.topItems, arg_126_0._tf)

	if arg_126_0.bulinTip:
		arg_126_0.bulinTip.Destroy()

		arg_126_0.bulinTip = None

	arg_126_0.destroyConfirmView.Destroy()
	arg_126_0.assignedItemView.Destroy()
	arg_126_0.blueprintAssignedItemView.Destroy()
	arg_126_0.equipDestroyConfirmWindow.Destroy()
	arg_126_0.msgBox.Destroy()

return var_0_0
