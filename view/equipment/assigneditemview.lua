local var_0_0 = class("AssignedItemView", import("..base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "StoreHouseItemAssignedView"
end

function var_0_0.OnInit(arg_2_0)
	local var_2_0 = arg_2_0._tf:Find("operate")

	arg_2_0.ulist = UIItemList.New(var_2_0:Find("got/bottom/list"), var_2_0:Find("got/bottom/list/tpl"))
	arg_2_0.confirmBtn = var_2_0:Find("actions/confirm")

	setText(arg_2_0.confirmBtn:Find("Image"), i18n("text_confirm"))

	arg_2_0.cancelBtn = var_2_0:Find("actions/cancel")

	setText(arg_2_0.cancelBtn:Find("Image"), i18n("text_cancel"))

	arg_2_0.rightArr = var_2_0:Find("calc/value_bg/add")
	arg_2_0.leftArr = var_2_0:Find("calc/value_bg/mius")
	arg_2_0.maxBtn = var_2_0:Find("calc/max")
	arg_2_0.valueText = var_2_0:Find("calc/value_bg/Text")
	arg_2_0.itemTF = var_2_0:Find("item")
	arg_2_0.nameTF = arg_2_0.itemTF:Find("display_panel/name_container/name/Text")
	arg_2_0.descTF = arg_2_0.itemTF:Find("display_panel/desc/Text")

	onButton(arg_2_0, arg_2_0._tf:Find("bg"), function()
		arg_2_0:Hide()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.cancelBtn, function()
		arg_2_0:Hide()
	end, SFX_PANEL)
	pressPersistTrigger(arg_2_0.rightArr, 0.5, function()
		if not arg_2_0.itemVO then
			return
		end

		arg_2_0.count = math.min(arg_2_0.count + 1, arg_2_0.itemVO.count)

		arg_2_0:updateValue()
	end, nil, true, true, 0.1, SFX_PANEL)
	pressPersistTrigger(arg_2_0.leftArr, 0.5, function()
		if not arg_2_0.itemVO then
			return
		end

		arg_2_0.count = math.max(arg_2_0.count - 1, 1)

		arg_2_0:updateValue()
	end, nil, true, true, 0.1, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.maxBtn, function()
		if not arg_2_0.itemVO then
			return
		end

		arg_2_0.count = arg_2_0.itemVO.count

		arg_2_0:updateValue()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.confirmBtn, function()
		if not arg_2_0.selectedIndex or not arg_2_0.itemVO or arg_2_0.count <= 0 then
			return
		end

		local var_8_0 = {}

		if arg_2_0.itemVO:IsDoaSelectCharItem() then
			table.insert(var_8_0, function(arg_9_0)
				local var_9_0 = arg_2_0.displayDrops[arg_2_0.selectedIndex].id
				local var_9_1 = HXSet.hxLan(pg.ship_data_statistics[var_9_0].name)

				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					content = i18n("doa_character_select_confirm", var_9_1),
					onYes = arg_9_0
				})
			end)
		end

		local var_8_1 = arg_2_0.displayDrops[arg_2_0.selectedIndex].type == DROP_TYPE_ITEM and arg_2_0.displayDrops[arg_2_0.selectedIndex]:getSubClass()

		if var_8_1 and var_8_1:getConfig("type") == Item.SKIN_ASSIGNED_TYPE and var_8_1:IsAllSkinOwner() then
			table.insert(var_8_0, function(arg_10_0)
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					content = i18n("blackfriday_pack_select_skinall"),
					onYes = arg_10_0
				})
			end)
		end

		seriesAsync(var_8_0, function()
			arg_2_0:emit(EquipmentMediator.ON_USE_ITEM, arg_2_0.itemVO.id, arg_2_0.count, arg_2_0.itemVO:getConfig("usage_arg")[arg_2_0.selectedIndex])
			arg_2_0:Hide()
		end)
	end, SFX_PANEL)
end

function var_0_0.Show(arg_12_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_12_0._tf)
	setActive(arg_12_0._tf, true)
end

function var_0_0.Hide(arg_13_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_13_0._tf, arg_13_0._parentTf)
	setActive(arg_13_0._tf, false)
end

function var_0_0.updateValue(arg_14_0)
	setText(arg_14_0.valueText, arg_14_0.count)
	arg_14_0.ulist:each(function(arg_15_0, arg_15_1)
		if not isActive(arg_15_1) then
			return
		end

		setText(arg_15_1:Find("item/icon_bg/count"), arg_14_0.count * arg_14_0.displayDrops[arg_15_0 + 1].count)
	end)
end

local function var_0_1(arg_16_0)
	local var_16_0 = pg.ship_data_template[arg_16_0].group_type

	return getProxy(CollectionProxy):getShipGroup(var_16_0) ~= nil
end

function var_0_0.update(arg_17_0, arg_17_1)
	arg_17_0.count = 1
	arg_17_0.selectedIndex = nil
	arg_17_0.selectedItem = nil
	arg_17_0.itemVO = arg_17_1
	arg_17_0.displayDrops = underscore.map(arg_17_1:getConfig("display_icon"), function(arg_18_0)
		return Drop.Create(arg_18_0)
	end)

	local var_17_0 = arg_17_1:getConfig("time_limit") == 1

	arg_17_0.ulist:make(function(arg_19_0, arg_19_1, arg_19_2)
		arg_19_1 = arg_19_1 + 1

		if arg_19_0 == UIItemList.EventUpdate then
			local var_19_0 = arg_17_0.displayDrops[arg_19_1]

			updateDrop(arg_19_2:Find("item"), var_19_0)
			onToggle(arg_17_0, arg_19_2, function(arg_20_0)
				if arg_20_0 then
					arg_17_0.selectedIndex = arg_19_1
					arg_17_0.selectedItem = arg_19_2
				end
			end, SFX_PANEL)
			triggerToggle(arg_19_2, false)
			setScrollText(arg_19_2:Find("name_bg/Text"), arg_17_0.displayDrops[arg_19_1]:getConfig("name"))

			arg_17_0.selectedItem = arg_17_0.selectedItem or arg_19_2

			local var_19_1 = var_17_0 and var_19_0.type == DROP_TYPE_SHIP and var_0_1(var_19_0.id)

			if var_19_1 then
				setText(arg_19_2:Find("item/tip/Text"), i18n("tech_character_get"))
			end

			setActive(arg_19_2:Find("item/tip"), var_19_1)
		end
	end)
	arg_17_0.ulist:align(#arg_17_0.displayDrops)
	triggerToggle(arg_17_0.selectedItem, true)
	arg_17_0:updateValue()

	local var_17_1 = Drop.New({
		type = DROP_TYPE_ITEM,
		id = arg_17_1.id,
		count = arg_17_1.count
	})

	updateDrop(arg_17_0.itemTF:Find("left/IconTpl"), setmetatable({
		count = 0
	}, {
		__index = var_17_1
	}))
	UpdateOwnDisplay(arg_17_0.itemTF:Find("left/own"), var_17_1)

	if underscore.any(arg_17_0.displayDrops, function(arg_21_0)
		return arg_21_0.type == DROP_TYPE_ITEM and arg_21_0:getConfig("type") == Item.SKIN_ASSIGNED_TYPE
	end) or var_17_1.type == DROP_TYPE_ITEM and var_17_1:getConfig("type") == Item.ASSIGNED_TYPE then
		RegisterDetailButton(arg_17_0, arg_17_0.itemTF:Find("left/detail"), var_17_1)
	else
		removeOnButton(arg_17_0.itemTF:Find("left/detail"))
	end

	setText(arg_17_0.nameTF, arg_17_1:getConfig("name"))
	setText(arg_17_0.descTF, arg_17_1:getConfig("display"))
end

function var_0_0.OnDestroy(arg_22_0)
	if arg_22_0:isShowing() then
		arg_22_0:Hide()
	end
end

return var_0_0
