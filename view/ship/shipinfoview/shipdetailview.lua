local var_0_0 = class("ShipDetailView", import("...base.BaseSubView"))
local var_0_1 = require("view.equipment.EquipmentSortCfg")
local var_0_2 = {
	equipCampIndex = 2047,
	equipPropertyIndex = 4095,
	equipPropertyIndex2 = 4095,
	equipAmmoIndex1 = 15,
	equipAmmoIndex2 = 3,
	extraIndex = 0,
	typeIndex = 2047,
	rarityIndex = 31
}

function var_0_0.getUIName(arg_1_0)
	return "ShipDetailView"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0:InitDetail()
	arg_2_0:InitEvent()
end

function var_0_0.InitDetail(arg_3_0)
	arg_3_0.mainPanel = arg_3_0._parentTf.parent
	arg_3_0.detailPanel = arg_3_0._tf
	arg_3_0.attrs = arg_3_0.detailPanel:Find("attrs")

	setActive(arg_3_0.attrs, false)

	arg_3_0.shipDetailLogicPanel = ShipDetailLogicPanel.New(arg_3_0.attrs)

	arg_3_0.shipDetailLogicPanel:attach(arg_3_0)

	arg_3_0.equipments = arg_3_0.detailPanel:Find("equipments")
	arg_3_0.equipmentsGrid = arg_3_0.equipments:Find("equipments")
	arg_3_0.detailEquipmentTpl = arg_3_0.equipments:Find("equipment_tpl")
	arg_3_0.emptyGridTpl = arg_3_0.equipments:Find("empty_tpl")
	arg_3_0.showRecordBtn = arg_3_0.equipments:Find("unload_all")
	arg_3_0.showQuickBtn = arg_3_0.equipments:Find("quickButton")
	arg_3_0.showECodeShareBtn = arg_3_0.equipments:Find("shareButton")
	arg_3_0.equipCodeBtn = arg_3_0.equipments:Find("equip_code")
	arg_3_0.lockBtn = arg_3_0.detailPanel:Find("lock_btn")
	arg_3_0.unlockBtn = arg_3_0.detailPanel:Find("unlock_btn")
	arg_3_0.viewBtn = arg_3_0.detailPanel:Find("view_btn")
	arg_3_0.evaluationBtn = arg_3_0.detailPanel:Find("evaluation_btn")
	arg_3_0.profileBtn = arg_3_0.detailPanel:Find("profile_btn")
	arg_3_0.fashionToggle = arg_3_0.detailPanel:Find("fashion_toggle")
	arg_3_0.fashionTag = arg_3_0.fashionToggle:Find("Tag")
	arg_3_0.commonTagToggle = arg_3_0.detailPanel:Find("common_toggle")
	arg_3_0.spWeaponSlot = arg_3_0.equipments:Find("SpSlot")
	arg_3_0.propertyIcons = arg_3_0.detailPanel:Find("attrs/attrs/property/icons")
	arg_3_0.intimacyTF = arg_3_0:findTF("intimacy")
	arg_3_0.updateItemTick = 0
	arg_3_0.quickPanel = arg_3_0.detailPanel:Find("quick_panel")
	arg_3_0.equiping = arg_3_0.quickPanel:Find("equiping")
	arg_3_0.fillter = arg_3_0.quickPanel:Find("fillter")
	arg_3_0.selectTitle = arg_3_0.quickPanel:Find("frame/selectTitle")
	arg_3_0.emptyTitle = arg_3_0.quickPanel:Find("frame/emptyTitle")
	arg_3_0.list = arg_3_0.quickPanel:Find("frame/container/Content"):GetComponent("LScrollRect")
	arg_3_0.indexData = {}

	arg_3_0:CloseQuickPanel()
	setText(arg_3_0.quickPanel:Find("fillter/on/text2"), i18n("quick_equip_tip2"))
	setText(arg_3_0.quickPanel:Find("fillter/off/text2"), i18n("quick_equip_tip2"))
	setText(arg_3_0.quickPanel:Find("equiping/on/text2"), i18n("quick_equip_tip1"))
	setText(arg_3_0.quickPanel:Find("equiping/off/text2"), i18n("quick_equip_tip1"))
	setText(arg_3_0.quickPanel:Find("title/text"), i18n("quick_equip_tip3"))
	setText(arg_3_0.quickPanel:Find("frame/emptyTitle/text"), i18n("quick_equip_tip4"))
	setText(arg_3_0.quickPanel:Find("frame/selectTitle/text"), i18n("quick_equip_tip5"))

	arg_3_0.equipmentProxy = getProxy(EquipmentProxy)
	arg_3_0.recordPanel = arg_3_0.detailPanel:Find("record_panel")
	arg_3_0.unloadAllBtn = arg_3_0.recordPanel:Find("frame/unload_all")
	arg_3_0.recordBars = _.map({
		1,
		2,
		3
	}, function(arg_4_0)
		return arg_3_0.recordPanel:Find("frame/container"):GetChild(arg_4_0 - 1)
	end)
	arg_3_0.recordBtns = {
		arg_3_0.recordPanel:Find("frame/container/record_1/record_btn"),
		arg_3_0.recordPanel:Find("frame/container/record_2/record_btn"),
		arg_3_0.recordPanel:Find("frame/container/record_3/record_btn")
	}
	arg_3_0.recordEquipmentsTFs = {
		arg_3_0.recordPanel:Find("frame/container/record_1/equipments"),
		arg_3_0.recordPanel:Find("frame/container/record_2/equipments"),
		arg_3_0.recordPanel:Find("frame/container/record_3/equipments")
	}
	arg_3_0.equipRecordBtns = {
		arg_3_0.recordPanel:Find("frame/container/record_1/equip_btn"),
		arg_3_0.recordPanel:Find("frame/container/record_2/equip_btn"),
		arg_3_0.recordPanel:Find("frame/container/record_3/equip_btn")
	}

	setActive(arg_3_0.detailPanel, true)
	setActive(arg_3_0.attrs, true)
	setActive(arg_3_0.recordPanel, false)
	setActive(arg_3_0.detailEquipmentTpl, false)
	setActive(arg_3_0.emptyGridTpl, false)
	setActive(arg_3_0.detailPanel, true)

	arg_3_0.onSelected = false

	if PLATFORM_CODE == PLATFORM_CHT and LOCK_SP_WEAPON then
		setActive(arg_3_0.showRecordBtn, false)
		setActive(arg_3_0.showQuickBtn, false)
		setActive(arg_3_0.spWeaponSlot, false)

		arg_3_0.showRecordBtn = arg_3_0.equipments:Find("unload_all_2")
		arg_3_0.showQuickBtn = arg_3_0.equipments:Find("quickButton_2")

		setActive(arg_3_0.showRecordBtn, true)
		setActive(arg_3_0.showQuickBtn, true)
	end
end

function var_0_0.InitEvent(arg_5_0)
	onButton(arg_5_0, arg_5_0.fashionToggle, function()
		arg_5_0:emit(ShipViewConst.SWITCH_TO_PAGE, ShipViewConst.PAGE.FASHION)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.propertyIcons, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_shipinfo_attr.tip,
			onClose = function()
				return
			end
		})
	end)
	onToggle(arg_5_0, arg_5_0.commonTagToggle, function(arg_9_0)
		local var_9_0 = arg_5_0:GetShipVO().preferenceTag
		local var_9_1 = var_9_0 == Ship.PREFERENCE_TAG_COMMON

		if var_9_1 ~= arg_9_0 then
			if var_9_0 == Ship.PREFERENCE_TAG_COMMON then
				var_9_1 = Ship.PREFERENCE_TAG_NONE
			else
				var_9_1 = Ship.PREFERENCE_TAG_COMMON
			end

			arg_5_0:emit(ShipMainMediator.ON_TAG, arg_5_0:GetShipVO().id, var_9_1)
		end
	end)
	onButton(arg_5_0, arg_5_0.lockBtn, function()
		arg_5_0:emit(ShipMainMediator.ON_LOCK, {
			arg_5_0:GetShipVO().id
		}, arg_5_0:GetShipVO().LOCK_STATE_LOCK)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.unlockBtn, function()
		arg_5_0:emit(ShipMainMediator.ON_LOCK, {
			arg_5_0:GetShipVO().id
		}, arg_5_0:GetShipVO().LOCK_STATE_UNLOCK)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.viewBtn, function()
		Input.multiTouchEnabled = true

		arg_5_0:emit(ShipViewConst.PAINT_VIEW, true)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.evaluationBtn, function()
		arg_5_0:emit(ShipMainMediator.OPEN_EVALUATION, arg_5_0:GetShipVO():getGroupId(), arg_5_0:GetShipVO():isActivityNpc())
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.profileBtn, function()
		arg_5_0:emit(ShipMainMediator.OPEN_SHIPPROFILE, arg_5_0:GetShipVO():getGroupId(), arg_5_0:GetShipVO():isRemoulded())
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.intimacyTF, function()
		if arg_5_0:GetShipVO():isActivityNpc() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("npc_propse_tip"))

			return
		end

		if LOCK_PROPOSE then
			return
		end

		arg_5_0:emit(ShipMainMediator.PROPOSE, arg_5_0:GetShipVO().id, function()
			return
		end)
	end)
	onToggle(arg_5_0, arg_5_0.showRecordBtn, function(arg_17_0)
		local var_17_0, var_17_1 = ShipStatus.ShipStatusCheck("onModify", arg_5_0:GetShipVO())

		if not var_17_0 then
			if arg_17_0 then
				pg.TipsMgr.GetInstance():ShowTips(var_17_1)
				onNextTick(function()
					triggerToggle(arg_5_0.showRecordBtn, false)
				end)
			end

			return
		end

		if arg_17_0 then
			arg_5_0:displayRecordPanel()

			if arg_5_0.isShowQuick then
				triggerToggle(arg_5_0.showQuickBtn, false)
			end
		else
			arg_5_0:CloseRecordPanel(true)
		end
	end, SFX_PANEL)
	onToggle(arg_5_0, arg_5_0.showQuickBtn, function(arg_19_0)
		local var_19_0, var_19_1 = ShipStatus.ShipStatusCheck("onModify", arg_5_0:GetShipVO())

		if not var_19_0 then
			if arg_19_0 then
				pg.TipsMgr.GetInstance():ShowTips(var_19_1)
				onNextTick(function()
					triggerToggle(arg_5_0.showQuickBtn, false)
				end)
			end

			arg_5_0:CloseRecordPanel(true)
			arg_5_0:CloseQuickPanel()

			return
		end

		if arg_19_0 then
			arg_5_0:displayQuickPanel()

			if arg_5_0.selectedEquip then
				arg_5_0:selectedEquipItem(arg_5_0.selectedEquip.index)
			else
				arg_5_0:quickSelectEmpty()
			end

			if arg_5_0.isShowRecord then
				triggerToggle(arg_5_0.showRecordBtn, false)
			end
		else
			arg_5_0:CloseQuickPanel()
		end
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.equipCodeBtn, function()
		arg_5_0:emit(ShipMainMediator.OPEN_EQUIP_CODE, {})
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.showECodeShareBtn, function()
		local var_22_0 = arg_5_0:GetShipVO()

		arg_5_0:emit(ShipMainMediator.OPEN_EQUIP_CODE_SHARE, var_22_0.id, var_22_0:getGroupId())
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.unloadAllBtn, function()
		local var_23_0, var_23_1 = ShipStatus.ShipStatusCheck("onModify", arg_5_0:GetShipVO())

		if not var_23_0 then
			pg.TipsMgr.GetInstance():ShowTips(var_23_1)
		else
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("ship_unequip_all_tip"),
				onYes = function()
					arg_5_0:emit(ShipMainMediator.UNEQUIP_FROM_SHIP_ALL, arg_5_0:GetShipVO().id)
				end
			})
		end
	end, SFX_PANEL)

	function arg_5_0.list.onInitItem(arg_25_0)
		ClearTweenItemAlphaAndWhite(arg_25_0)
	end

	function arg_5_0.list.onReturnItem(arg_26_0, arg_26_1)
		ClearTweenItemAlphaAndWhite(arg_26_1)
	end

	function arg_5_0.list.onUpdateItem(arg_27_0, arg_27_1)
		setActive(findTF(tf(arg_27_1), "IconTpl/icon_bg/icon"), false)
		TweenItemAlphaAndWhite(arg_27_1)

		if arg_27_0 == 0 and not arg_5_0.selectedEquip.empty then
			setActive(findTF(tf(arg_27_1), "unEquip"), true)
			setActive(findTF(tf(arg_27_1), "bg"), false)
			setActive(findTF(tf(arg_27_1), "IconTpl"), false)
			onButton(arg_5_0, tf(arg_27_1), function()
				local var_28_0 = arg_5_0.selectedEquip.index
				local var_28_1 = arg_5_0:GetShipVO()
				local var_28_2 = var_28_1:getEquip(arg_5_0.selectedEquip.index):getConfig("name")
				local var_28_3 = var_28_1:getName()

				arg_5_0:emit(ShipMainMediator.UNEQUIP_FROM_SHIP, {
					shipId = var_28_1.id,
					pos = var_28_0
				})
			end, SFX_PANEL)
		else
			setActive(findTF(tf(arg_27_1), "unEquip"), false)
			setActive(findTF(tf(arg_27_1), "bg"), true)
			setActive(findTF(tf(arg_27_1), "IconTpl"), true)

			local var_27_0 = arg_5_0.selectedEquip.empty and arg_27_0 + 1 or arg_27_0
			local var_27_1 = arg_5_0.fillterEquipments[var_27_0]

			if not var_27_1 then
				return
			end

			setActive(findTF(tf(arg_27_1), "IconTpl/icon_bg/icon"), true)
			updateEquipment(arg_5_0:findTF("IconTpl", tf(arg_27_1)), var_27_1)

			if var_27_1.shipId then
				local var_27_2 = getProxy(BayProxy):getShipById(var_27_1.shipId)

				setImageSprite(findTF(tf(arg_27_1), "IconTpl/icon_bg/equip_flag/Image"), LoadSprite("qicon/" .. var_27_2:getPainting()))
			end

			setActive(findTF(tf(arg_27_1), "IconTpl/icon_bg/equip_flag"), var_27_1.shipId and var_27_1.shipId > 0)
			setActive(findTF(tf(arg_27_1), "IconTpl/mask"), var_27_1.mask)
			onButton(arg_5_0, tf(arg_27_1), function()
				if var_27_1.mask then
					return
				end

				arg_5_0:changeEquip(var_27_1)
			end, SFX_PANEL)
		end
	end

	onToggle(arg_5_0, arg_5_0.equiping, function(arg_30_0)
		arg_5_0.equipingFlag = arg_30_0

		if arg_5_0.selectedEquip then
			arg_5_0:updateQuickPanel(true)
		end
	end, SFX_PANEL)
	triggerToggle(arg_5_0.equiping, true)
	onButton(arg_5_0, arg_5_0.fillter, function()
		arg_5_0.indexData = arg_5_0.indexData or {}

		if not var_0_0.EQUIPMENT_INDEX then
			var_0_0.EQUIPMENT_INDEX = Clone(StoreHouseConst.EQUIPMENT_INDEX_COMMON)

			table.removebyvalue(var_0_0.EQUIPMENT_INDEX.customPanels.extraIndex.options, IndexConst.EquipmentExtraEquiping)
			table.removebyvalue(var_0_0.EQUIPMENT_INDEX.customPanels.extraIndex.names, "index_equip")
		end

		local var_31_0 = setmetatable({
			indexDatas = Clone(arg_5_0.indexData),
			callback = function(arg_32_0)
				arg_5_0.indexData.typeIndex = arg_32_0.typeIndex
				arg_5_0.indexData.equipPropertyIndex = arg_32_0.equipPropertyIndex
				arg_5_0.indexData.equipPropertyIndex2 = arg_32_0.equipPropertyIndex2
				arg_5_0.indexData.equipAmmoIndex1 = arg_32_0.equipAmmoIndex1
				arg_5_0.indexData.equipAmmoIndex2 = arg_32_0.equipAmmoIndex2
				arg_5_0.indexData.equipCampIndex = arg_32_0.equipCampIndex
				arg_5_0.indexData.rarityIndex = arg_32_0.rarityIndex
				arg_5_0.indexData.extraIndex = arg_32_0.extraIndex

				local var_32_0 = underscore(arg_5_0.indexData):chain():keys():all(function(arg_33_0)
					return arg_5_0.indexData[arg_33_0] == var_0_0.EQUIPMENT_INDEX.customPanels[arg_33_0].options[1]
				end):value()

				setActive(findTF(arg_5_0.fillter, "on"), not var_32_0)
				setActive(findTF(arg_5_0.fillter, "off"), var_32_0)
				arg_5_0:updateQuickPanel(true)
			end
		}, {
			__index = var_0_0.EQUIPMENT_INDEX
		})

		arg_5_0:emit(ShipMainMediator.OPEN_EQUIPMENT_INDEX, var_31_0)
	end, SFX_PANEL)
end

function var_0_0.changeEquip(arg_34_0, arg_34_1)
	local var_34_0 = arg_34_0.selectedEquip.index
	local var_34_1 = arg_34_0:GetShipVO()
	local var_34_2 = {
		quickFlag = true,
		type = EquipmentInfoMediator.TYPE_REPLACE,
		equipmentId = arg_34_1.id,
		shipId = var_34_1.id,
		pos = var_34_0,
		oldShipId = arg_34_1.shipId,
		oldPos = arg_34_1.shipPos
	}

	if var_34_2 then
		if PlayerPrefs.GetInt("QUICK_CHANGE_EQUIP", 1) == 1 then
			arg_34_0:emit(BaseUI.ON_EQUIPMENT, var_34_2)
		else
			local var_34_3, var_34_4 = var_34_1:canEquipAtPos(arg_34_1, var_34_0)

			if not var_34_3 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("equipment_equipmentInfoLayer_error_canNotEquip", var_34_4))

				return
			end

			if arg_34_1.shipId then
				local var_34_5 = getProxy(BayProxy):getShipById(arg_34_1.shipId)
				local var_34_6, var_34_7 = ShipStatus.ShipStatusCheck("onModify", var_34_5)

				if not var_34_6 then
					pg.TipsMgr.GetInstance():ShowTips(var_34_7)
				else
					arg_34_0:emit(ShipMainMediator.EQUIP_CHANGE_NOTICE, {
						notice = GAME.EQUIP_FROM_SHIP,
						data = var_34_2
					})
				end
			else
				arg_34_0:emit(ShipMainMediator.EQUIP_CHANGE_NOTICE, {
					notice = GAME.EQUIP_TO_SHIP,
					data = var_34_2
				})
			end
		end
	end
end

function var_0_0.SetShareData(arg_35_0, arg_35_1)
	arg_35_0.shareData = arg_35_1
end

function var_0_0.GetShipVO(arg_36_0)
	if arg_36_0.shareData and arg_36_0.shareData.shipVO then
		return arg_36_0.shareData.shipVO
	end

	return nil
end

function var_0_0.OnSelected(arg_37_0, arg_37_1)
	local var_37_0 = pg.UIMgr.GetInstance()

	if arg_37_1 then
		var_37_0:OverlayPanelPB(arg_37_0._parentTf, {
			pbList = {
				arg_37_0.detailPanel:Find("attrs"),
				arg_37_0.detailPanel:Find("equipments"),
				arg_37_0.detailPanel:Find("quick_panel")
			},
			groupName = LayerWeightConst.GROUP_SHIPINFOUI,
			overlayType = LayerWeightConst.OVERLAY_UI_ADAPT
		})
	else
		var_37_0:UnOverlayPanel(arg_37_0._parentTf, arg_37_0.mainPanel)
	end

	arg_37_0.onSelected = arg_37_1

	if arg_37_0.onSelected and arg_37_0.selectedEquip then
		local var_37_1 = arg_37_0.selectedEquip.index

		arg_37_0:selectedEquipItem(nil)
		arg_37_0:selectedEquipItem(var_37_1)
	end
end

function var_0_0.UpdateUI(arg_38_0)
	local var_38_0 = arg_38_0:GetShipVO()

	arg_38_0:UpdateIntimacy(var_38_0)
	arg_38_0:UpdateDetail(var_38_0)
	arg_38_0:UpdateEquipments(var_38_0)
	arg_38_0:UpdateLock()
	arg_38_0:UpdatePreferenceTag()
end

function var_0_0.UpdateIntimacy(arg_39_0, arg_39_1)
	setActive(arg_39_0.intimacyTF, not LOCK_PROPOSE)
	setIntimacyIcon(arg_39_0.intimacyTF, arg_39_1:getIntimacyIcon())
end

function var_0_0.UpdateDetail(arg_40_0, arg_40_1)
	arg_40_0.shipDetailLogicPanel:flush(arg_40_1)

	local var_40_0 = arg_40_0.shipDetailLogicPanel.attrs:Find("icons/hunting_range/bg")

	removeOnButton(var_40_0)

	if table.contains(TeamType.SubShipType, arg_40_1:getShipType()) then
		onButton(arg_40_0, var_40_0, function()
			arg_40_0:emit(ShipViewConst.DISPLAY_HUNTING_RANGE, true)
		end, SFX_PANEL)
	end

	if not HXSet.isHxSkin() then
		setActive(arg_40_0.fashionToggle, arg_40_0.shareData:HasFashion())
	else
		setActive(arg_40_0.fashionToggle, false)
	end

	arg_40_0:UpdateFashionTag()
	setActive(arg_40_0.profileBtn, not arg_40_1:isActivityNpc())
end

function var_0_0.UpdateFashionTag(arg_42_0)
	local var_42_0 = arg_42_0:GetShipVO()

	setActive(arg_42_0.fashionTag, #PaintingGroupConst.GetPaintingNameListByShipVO(var_42_0) > 0)
end

function var_0_0.UpdateEquipments(arg_43_0, arg_43_1)
	arg_43_0:clearListener()
	removeAllChildren(arg_43_0.equipmentsGrid)

	local var_43_0 = arg_43_1:getActiveEquipments()

	arg_43_0.equipItems = {}

	for iter_43_0, iter_43_1 in ipairs(arg_43_1.equipments) do
		local var_43_1 = var_43_0[iter_43_0]
		local var_43_2
		local var_43_3 = iter_43_0
		local var_43_4

		if iter_43_1 then
			var_43_2 = cloneTplTo(arg_43_0.detailEquipmentTpl, arg_43_0.equipmentsGrid)
			var_43_4 = {
				empty = false,
				tf = var_43_2,
				index = var_43_3
			}

			table.insert(arg_43_0.equipItems, var_43_4)
			updateEquipment(arg_43_0:findTF("IconTpl", var_43_2), iter_43_1)
			onButton(arg_43_0, var_43_2, function()
				if arg_43_0.isShowQuick then
					arg_43_0:selectedEquipItem(var_43_3)
				else
					arg_43_0:emit(BaseUI.ON_EQUIPMENT, {
						type = EquipmentInfoMediator.TYPE_SHIP,
						shipId = arg_43_0:GetShipVO().id,
						pos = iter_43_0,
						LayerWeightMgr_weight = LayerWeightConst.SECOND_LAYER
					})
				end
			end, SFX_UI_DOCKYARD_EQUIPADD)
		else
			var_43_2 = cloneTplTo(arg_43_0.emptyGridTpl, arg_43_0.equipmentsGrid)
			var_43_4 = {
				empty = true,
				tf = var_43_2,
				index = var_43_3
			}

			table.insert(arg_43_0.equipItems, var_43_4)
			onButton(arg_43_0, var_43_2, function()
				if arg_43_0.isShowQuick then
					arg_43_0:selectedEquipItem(var_43_3)
				else
					arg_43_0:emit(ShipViewConst.SWITCH_TO_PAGE, ShipViewConst.PAGE.EQUIPMENT)
				end
			end, SFX_UI_DOCKYARD_EQUIPADD)
		end

		local var_43_5 = GetOrAddComponent(var_43_2, typeof(EventTriggerListener))

		var_43_5:AddPointDownFunc(function()
			if var_43_2 and not arg_43_0.isShowQuick then
				LeanTween.delayedCall(go(var_43_2), 1, System.Action(function()
					arg_43_0.selectedEquip = var_43_4

					triggerToggle(arg_43_0.showQuickBtn, true)
				end))
			end
		end)
		var_43_5:AddPointUpFunc(function()
			if var_43_2 and LeanTween.isTweening(go(var_43_2)) then
				LeanTween.cancel(go(var_43_2))
			end
		end)
	end

	local var_43_6, var_43_7 = ShipStatus.ShipStatusCheck("onModify", arg_43_0:GetShipVO())

	if not var_43_6 then
		triggerToggle(arg_43_0.showQuickBtn, false)
	elseif arg_43_1.id ~= arg_43_0.lastShipVo and arg_43_0.isShowQuick then
		onNextTick(function()
			triggerToggle(arg_43_0.showQuickBtn, false)
			triggerToggle(arg_43_0.showQuickBtn, true)
		end)
	elseif arg_43_0.selectedEquip and arg_43_0.isShowQuick then
		local var_43_8 = arg_43_0.selectedEquip.index

		arg_43_0:selectedEquipItem(nil)
		arg_43_0:selectedEquipItem(var_43_8)
	end

	arg_43_0.lastShipVo = arg_43_1.id

	local var_43_9, var_43_10 = arg_43_1:IsSpweaponUnlock()

	setActive(arg_43_0.spWeaponSlot:Find("Lock"), not var_43_9)

	local var_43_11 = arg_43_1:GetSpWeapon()

	setActive(arg_43_0.spWeaponSlot:Find("Icon"), var_43_11)
	setActive(arg_43_0.spWeaponSlot:Find("IconShadow"), var_43_11)

	if var_43_11 then
		UpdateSpWeaponSlot(arg_43_0.spWeaponSlot, var_43_11)
	end

	onButton(arg_43_0, arg_43_0.spWeaponSlot, function()
		if not var_43_9 then
			pg.TipsMgr.GetInstance():ShowTips(i18n(var_43_10))

			return
		elseif var_43_11 then
			arg_43_0:emit(BaseUI.ON_SPWEAPON, {
				type = EquipmentInfoMediator.TYPE_SHIP,
				shipId = arg_43_0:GetShipVO().id
			})
		else
			arg_43_0:emit(ShipViewConst.SWITCH_TO_PAGE, ShipViewConst.PAGE.EQUIPMENT)
		end
	end, SFX_PANEL)
end

function var_0_0.selectedEquipItem(arg_51_0, arg_51_1)
	if not arg_51_1 then
		if arg_51_0.selectedEquip then
			arg_51_0.selectedEquip = nil
			arg_51_0.showEquipItem = nil
		end
	else
		arg_51_0.selectedEquip = arg_51_0.equipItems[arg_51_1]
	end

	if arg_51_0.isShowQuick then
		arg_51_0:updateQuickPanel()
	end
end

function var_0_0.updateQuickPanel(arg_52_0, arg_52_1)
	setActive(arg_52_0.selectTitle, not arg_52_0.selectedEquip)

	if arg_52_0.isShowQuick and arg_52_0.selectedEquip then
		if arg_52_0.selectedEquip ~= arg_52_0.showEquipItem or arg_52_1 then
			arg_52_0.showEquipItem = arg_52_0.selectedEquip

			arg_52_0:updateQuickEquipments()
		end
	else
		arg_52_0:setListCount(0, 0)
		setActive(arg_52_0.emptyTitle, false)
	end

	if arg_52_0.equipItems then
		for iter_52_0 = 1, #arg_52_0.equipItems do
			if arg_52_0.selectedEquip and arg_52_0.selectedEquip.index == iter_52_0 then
				setActive(findTF(arg_52_0.equipItems[iter_52_0].tf, "selected"), true)
			else
				setActive(findTF(arg_52_0.equipItems[iter_52_0].tf, "selected"), false)
			end
		end
	end
end

function var_0_0.updateQuickEquipments(arg_53_0)
	arg_53_0:setListCount(0, 0)

	arg_53_0.fillterEquipments = arg_53_0:getEquipments()

	setActive(arg_53_0.emptyTitle, false)

	if arg_53_0.selectedEquip and arg_53_0.selectedEquip.empty then
		setActive(arg_53_0.emptyTitle, #arg_53_0.fillterEquipments == 0)
	end

	local var_53_0 = arg_53_0.selectedEquip.empty and 0 or 1

	arg_53_0:setListCount(#arg_53_0.fillterEquipments + var_53_0, 0)
end

function var_0_0.setListCount(arg_54_0, arg_54_1, arg_54_2)
	if arg_54_0.onSelected and isActive(arg_54_0._tf) and arg_54_0.list then
		arg_54_0.list:SetTotalCount(arg_54_1, arg_54_2)
	end
end

function var_0_0.getEquipments(arg_55_0)
	local var_55_0 = getProxy(BayProxy)
	local var_55_1 = arg_55_0:GetShipVO()
	local var_55_2 = getProxy(EquipmentProxy)
	local var_55_3 = pg.ship_data_template[var_55_1.configId]["equip_" .. arg_55_0.selectedEquip.index]
	local var_55_4 = var_55_1:getShipType()
	local var_55_5 = var_55_2:getEquipmentsByFillter(var_55_4, var_55_3)

	if arg_55_0.equipingFlag then
		for iter_55_0, iter_55_1 in ipairs(var_55_0:getEquipsInShips(function(arg_56_0, arg_56_1)
			return var_55_1.id ~= arg_56_1 and not var_55_1:isForbiddenAtPos(arg_56_0, arg_55_0.selectedEquip.index)
		end)) do
			table.insert(var_55_5, iter_55_1)
		end
	end

	local var_55_6 = {}
	local var_55_7 = {
		arg_55_0.indexData.equipPropertyIndex,
		arg_55_0.indexData.equipPropertyIndex2
	}

	for iter_55_2, iter_55_3 in pairs(var_55_5) do
		if arg_55_0:checkFillter(iter_55_3, var_55_7) then
			table.insert(var_55_6, iter_55_3)
		end
	end

	_.each(var_55_6, function(arg_57_0)
		if not var_55_1:canEquipAtPos(arg_57_0, arg_55_0.selectedEquip.index) then
			arg_57_0.mask = true
		end
	end)
	table.sort(var_55_6, CompareFuncs(var_0_1.sortFunc(var_0_1.sort[1], false)))

	return var_55_6
end

function var_0_0.checkFillter(arg_58_0, arg_58_1, arg_58_2)
	return (arg_58_1.count > 0 or arg_58_1.shipId and arg_58_0.equipingFlag) and IndexConst.filterEquipByType(arg_58_1, arg_58_0.indexData.typeIndex) and IndexConst.filterEquipByProperty(arg_58_1, arg_58_2) and IndexConst.filterEquipAmmo1(arg_58_1, arg_58_0.indexData.equipAmmoIndex1) and IndexConst.filterEquipAmmo2(arg_58_1, arg_58_0.indexData.equipAmmoIndex2) and IndexConst.filterEquipByCamp(arg_58_1, arg_58_0.indexData.equipCampIndex) and IndexConst.filterEquipByRarity(arg_58_1, arg_58_0.indexData.rarityIndex) and IndexConst.filterEquipByExtra(arg_58_1, arg_58_0.indexData.extraIndex)
end

function var_0_0.UpdateLock(arg_59_0)
	local var_59_0 = arg_59_0:GetShipVO():GetLockState()

	if var_59_0 == arg_59_0:GetShipVO().LOCK_STATE_UNLOCK then
		setActive(arg_59_0.lockBtn, true)
		setActive(arg_59_0.unlockBtn, false)
	elseif var_59_0 == arg_59_0:GetShipVO().LOCK_STATE_LOCK then
		setActive(arg_59_0.lockBtn, false)
		setActive(arg_59_0.unlockBtn, true)
	end
end

function var_0_0.displayQuickPanel(arg_60_0)
	if not arg_60_0:GetShipVO() then
		return
	end

	arg_60_0.isShowQuick = true

	setActive(arg_60_0.attrs, false)
	setActive(arg_60_0.quickPanel, true)
	arg_60_0:updateQuickPanel()
end

function var_0_0.quickSelectEmpty(arg_61_0)
	if not arg_61_0.selectedEquip and arg_61_0.equipItems then
		for iter_61_0 = 1, #arg_61_0.equipItems do
			if arg_61_0.equipItems[iter_61_0].empty then
				arg_61_0:selectedEquipItem(arg_61_0.equipItems[iter_61_0].index)

				return
			end
		end
	end
end

local var_0_3 = 0.2

function var_0_0.displayRecordPanel(arg_62_0)
	if not arg_62_0:GetShipVO() then
		return
	end

	arg_62_0.isShowRecord = true

	setActive(arg_62_0.recordPanel, true)
	setActive(arg_62_0.attrs, false)

	for iter_62_0, iter_62_1 in ipairs(arg_62_0.recordBtns) do
		onButton(arg_62_0, iter_62_1, function()
			arg_62_0:emit(ShipMainMediator.ON_RECORD_EQUIPMENT, arg_62_0:GetShipVO().id, iter_62_0, 1)
		end, SFX_PANEL)
	end

	for iter_62_2, iter_62_3 in ipairs(arg_62_0.equipRecordBtns) do
		onButton(arg_62_0, iter_62_3, function()
			arg_62_0:emit(ShipMainMediator.ON_RECORD_EQUIPMENT, arg_62_0:GetShipVO().id, iter_62_2, 2)
		end, SFX_PANEL)
	end

	for iter_62_4, iter_62_5 in ipairs(arg_62_0.recordEquipmentsTFs) do
		arg_62_0:UpdateRecordEquipments(iter_62_4)
	end

	arg_62_0:UpdateRecordSpWeapons()
end

function var_0_0.CloseRecordPanel(arg_65_0, arg_65_1)
	if arg_65_1 then
		arg_65_0.isShowRecord = nil

		setActive(arg_65_0.recordPanel, false)

		if not arg_65_0.isShowRecord and not arg_65_0.isShowQuick then
			setActive(arg_65_0.attrs, true)
		end
	else
		triggerToggle(arg_65_0.showRecordBtn, false)
	end
end

function var_0_0.CloseQuickPanel(arg_66_0)
	arg_66_0.isShowQuick = nil

	arg_66_0:selectedEquipItem(nil)

	arg_66_0.showEquipItem = nil

	if arg_66_0.list then
		arg_66_0:setListCount(0, 0)
	end

	setActive(arg_66_0.quickPanel, false)

	if not arg_66_0.isShowRecord and not arg_66_0.isShowQuick then
		setActive(arg_66_0.attrs, true)
	end

	arg_66_0:updateQuickPanel()
end

function var_0_0.UpdateRecordEquipments(arg_67_0, arg_67_1)
	local var_67_0 = arg_67_0.recordEquipmentsTFs[arg_67_1]
	local var_67_1 = arg_67_0:GetShipVO():getEquipmentRecord(arg_67_0.shareData.player.id)[arg_67_1] or {}

	for iter_67_0 = 1, 5 do
		local var_67_2 = tonumber(var_67_1[iter_67_0])
		local var_67_3 = var_67_2 and var_67_2 ~= -1
		local var_67_4 = var_67_0:Find("equipment_" .. iter_67_0)
		local var_67_5 = var_67_4:Find("empty")
		local var_67_6 = var_67_4:Find("info")

		setActive(var_67_6, var_67_3)
		setActive(var_67_5, not var_67_3)

		if var_67_3 then
			local var_67_7 = arg_67_0.equipmentProxy:getEquipmentById(var_67_2)
			local var_67_8 = arg_67_0:GetShipVO().equipments[iter_67_0]
			local var_67_9 = not (var_67_8 and var_67_8.id == var_67_2 or false) and (not var_67_7 or not (var_67_7.count > 0))

			setActive(var_67_6:Find("tip"), var_67_9)
			updateEquipment(arg_67_0:findTF("IconTpl", var_67_6), Equipment.New({
				id = var_67_2
			}))

			if var_67_9 then
				onButton(arg_67_0, var_67_6, function()
					pg.TipsMgr.GetInstance():ShowTips(i18n("ship_quick_change_nofreeequip"))
				end, SFX_PANEL)
			end
		else
			removeOnButton(var_67_6)
		end
	end
end

function var_0_0.UpdateRecordSpWeapons(arg_69_0, arg_69_1)
	if LOCK_SP_WEAPON then
		return
	end

	local var_69_0 = arg_69_0:GetShipVO():GetSpWeaponRecord(arg_69_0.shareData.player.id)

	table.Foreach(arg_69_0.recordBars, function(arg_70_0, arg_70_1)
		if arg_69_1 and arg_70_0 ~= arg_69_1 then
			return
		end

		local var_70_0 = var_69_0[arg_70_0]
		local var_70_1 = arg_70_1:Find("SpSlot")
		local var_70_2 = arg_69_0:GetShipVO():IsSpweaponUnlock()

		setActive(var_70_1:Find("Lock"), not var_70_2)
		setActive(var_70_1:Find("Icon"), var_70_0)
		setActive(var_70_1:Find("IconShadow"), var_70_0)

		if var_70_0 then
			UpdateSpWeaponSlot(var_70_1, var_70_0)

			local var_70_3 = not var_70_0:IsReal() or var_70_0:GetShipId() ~= nil and var_70_0:GetShipId() ~= arg_69_0:GetShipVO().id

			setActive(var_70_1:Find("Icon/tip"), var_70_3)

			if var_70_3 then
				onButton(arg_69_0, var_70_1, function()
					pg.TipsMgr.GetInstance():ShowTips(i18n("ship_quick_change_nofreeequip"))
				end, SFX_PANEL)
			else
				removeOnButton(var_70_1)
			end
		else
			removeOnButton(var_70_1)
		end
	end)
end

function var_0_0.UpdatePreferenceTag(arg_72_0)
	triggerToggle(arg_72_0.commonTagToggle, arg_72_0:GetShipVO().preferenceTag == Ship.PREFERENCE_TAG_COMMON)
end

function var_0_0.DoLeveUpAnim(arg_73_0, arg_73_1, arg_73_2, arg_73_3)
	arg_73_0.shipDetailLogicPanel:doLeveUpAnim(arg_73_1, arg_73_2, arg_73_3)
end

function var_0_0.clearListener(arg_74_0)
	if arg_74_0.equipItems then
		for iter_74_0 = 1, #arg_74_0.equipItems do
			local var_74_0 = arg_74_0.equipItems[iter_74_0].tf

			if var_74_0 then
				ClearEventTrigger(GetOrAddComponent(go(var_74_0), typeof(EventTriggerListener)))
				removeOnButton(go(var_74_0))
			end
		end
	end
end

function var_0_0.OnDestroy(arg_75_0)
	arg_75_0:clearListener()
	removeAllChildren(arg_75_0.equipmentsGrid)

	if arg_75_0.list then
		arg_75_0.list:SetTotalCount(0)

		function arg_75_0.list.onUpdateItem()
			return
		end
	end

	arg_75_0.destroy = true

	if arg_75_0.recordPanel then
		if LeanTween.isTweening(go(arg_75_0.recordPanel)) then
			LeanTween.cancel(go(arg_75_0.recordPanel))
		end

		arg_75_0.recordPanel = nil
	end

	arg_75_0.shipDetailLogicPanel:clear()
	arg_75_0.shipDetailLogicPanel:detach()

	arg_75_0.shareData = nil
end

return var_0_0
