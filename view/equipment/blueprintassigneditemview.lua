local var_0_0 = class("BlueprintAssignedItemView", import(".AssignedItemView"))

function var_0_0.getUIName(arg_1_0)
	return "BlueprintItemAssignedView"
end

function var_0_0.OnInit(arg_2_0)
	var_0_0.super.OnInit(arg_2_0)

	arg_2_0.countOver = arg_2_0._tf:Find("operate/calc/value_bg/over_count")

	setText(arg_2_0.countOver, i18n("blueprint_select_overflow"))
	onButton(arg_2_0, arg_2_0.maxBtn, function()
		if not arg_2_0.itemVO or not arg_2_0.selectedIndex then
			return
		end

		local var_3_0 = arg_2_0.displayDrops[arg_2_0.selectedIndex]
		local var_3_1 = arg_2_0.count * var_3_0.count
		local var_3_2 = arg_2_0:GetBlueprintNeed(var_3_0.id)

		if var_3_1 < var_3_2 then
			arg_2_0.count = math.floor((var_3_2 + var_3_0.count - 1) / var_3_0.count)
			arg_2_0.count = math.min(arg_2_0.count, arg_2_0.itemVO.count)
		else
			arg_2_0.count = arg_2_0.itemVO.count
		end

		arg_2_0:updateValue()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.confirmBtn, function()
		if not arg_2_0.selectedIndex or not arg_2_0.itemVO or arg_2_0.count <= 0 then
			return
		end

		local var_4_0 = arg_2_0.displayDrops[arg_2_0.selectedIndex]
		local var_4_1 = arg_2_0.count * var_4_0.count
		local var_4_2 = arg_2_0:GetBlueprintNeed(var_4_0.id)
		local var_4_3 = {}

		if not arg_2_0.isAllNeedZero and var_4_2 < var_4_1 then
			table.insert(var_4_3, function(arg_5_0)
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					content = i18n("blueprint_select_overflow_tip", var_4_0:getConfig("name"), var_4_1 - var_4_2),
					onYes = arg_5_0
				})
			end)
		end

		seriesAsync(var_4_3, function()
			arg_2_0:emit(EquipmentMediator.ON_USE_ITEM, arg_2_0.itemVO.id, arg_2_0.count, arg_2_0.itemVO:getConfig("usage_arg")[arg_2_0.selectedIndex])
			arg_2_0:Hide()
		end)
	end, SFX_PANEL)

	arg_2_0.toggleSwitch = arg_2_0._tf:Find("operate/got/top/switch_btn")

	setText(arg_2_0.toggleSwitch:Find("Text_off"), i18n("show_design_demand_count"))
	setText(arg_2_0.toggleSwitch:Find("Text_on"), i18n("show_fate_demand_count"))
	onToggle(arg_2_0, arg_2_0.toggleSwitch, function(arg_7_0)
		arg_2_0.isSwitch = arg_7_0

		arg_2_0:updateValue()
	end, SFX_PANEL)
end

function var_0_0.GetBlueprintNeed(arg_8_0, arg_8_1)
	arg_8_0.technologyProxy = arg_8_0.technologyProxy or getProxy(TechnologyProxy)

	local var_8_0 = arg_8_0.technologyProxy:getBluePrintById(arg_8_0.technologyProxy:GetBlueprint4Item(arg_8_1))

	arg_8_0.bagProxy = arg_8_0.bagProxy or getProxy(BagProxy)

	return math.max(var_8_0:getUseageMaxItem() + (arg_8_0.isSwitch and var_8_0:getFateMaxLeftOver() or 0) - arg_8_0.bagProxy:getItemCountById(var_8_0:getItemId()), 0)
end

function var_0_0.checkBlueprintIsUnlock(arg_9_0, arg_9_1)
	arg_9_0.technologyProxy = arg_9_0.technologyProxy or getProxy(TechnologyProxy)

	return arg_9_0.technologyProxy:getBluePrintById(arg_9_0.technologyProxy:GetBlueprint4Item(arg_9_1)):isUnlock()
end

function var_0_0.updateValue(arg_10_0)
	arg_10_0.isAllNeedZero = underscore.all(arg_10_0.displayDrops, function(arg_11_0)
		return arg_10_0:GetBlueprintNeed(arg_11_0.id) == 0
	end)

	arg_10_0:updateCountText()
	arg_10_0.ulist:each(function(arg_12_0, arg_12_1)
		if not isActive(arg_12_1) then
			return
		end

		arg_12_0 = arg_12_0 + 1

		local var_12_0 = arg_10_0.displayDrops[arg_12_0]
		local var_12_1 = arg_10_0.count * var_12_0.count
		local var_12_2 = arg_10_0:GetBlueprintNeed(var_12_0.id)

		setText(arg_12_1:Find("item/icon_bg/count"), setColorStr(var_12_1, not arg_10_0.isAllNeedZero and var_12_2 < var_12_1 and "#FF5A5A" or "#FFEC6E") .. "/" .. var_12_2)
	end)
end

function var_0_0.updateCountText(arg_13_0)
	local var_13_0 = arg_13_0.displayDrops[arg_13_0.selectedIndex]
	local var_13_1 = arg_13_0.count * var_13_0.count
	local var_13_2 = arg_13_0:GetBlueprintNeed(var_13_0.id)

	setText(arg_13_0.valueText, not arg_13_0.isAllNeedZero and var_13_2 < var_13_1 and setColorStr(arg_13_0.count, "#FF5A5A") or arg_13_0.count)
	setActive(arg_13_0.countOver, not arg_13_0.isAllNeedZero and var_13_2 < var_13_1)
end

function var_0_0.update(arg_14_0, arg_14_1)
	arg_14_0.count = 1
	arg_14_0.selectedIndex = nil
	arg_14_0.selectedItem = nil
	arg_14_0.isSwitch = false
	arg_14_0.itemVO = arg_14_1
	arg_14_0.displayDrops = underscore.map(arg_14_1:getConfig("display_icon"), function(arg_15_0)
		return {
			type = arg_15_0[1],
			id = arg_15_0[2],
			count = arg_15_0[3]
		}
	end)

	arg_14_0.ulist:make(function(arg_16_0, arg_16_1, arg_16_2)
		arg_16_1 = arg_16_1 + 1

		if arg_16_0 == UIItemList.EventUpdate then
			updateDrop(arg_16_2:Find("item"), arg_14_0.displayDrops[arg_16_1])
			onToggle(arg_14_0, arg_16_2, function(arg_17_0)
				if arg_17_0 then
					arg_14_0.selectedIndex = arg_16_1
					arg_14_0.selectedItem = arg_16_2

					arg_14_0:updateCountText()
				end
			end, SFX_PANEL)
			triggerToggle(arg_16_2, arg_16_1 == 1)
			setScrollText(arg_16_2:Find("name_bg/Text"), arg_14_0.displayDrops[arg_16_1]:getConfig("name"))

			arg_14_0.selectedItem = arg_14_0.selectedItem or arg_16_2

			setText(arg_16_2:Find("item/tip/Text"), i18n("tech_character_get"))
			setActive(arg_16_2:Find("item/tip"), arg_14_0:checkBlueprintIsUnlock(arg_14_0.displayDrops[arg_16_1].id))
		end
	end)
	arg_14_0.ulist:align(#arg_14_0.displayDrops)
	triggerToggle(arg_14_0.selectedItem, true)
	triggerToggle(arg_14_0.toggleSwitch, true)

	local var_14_0 = Drop.New({
		type = DROP_TYPE_ITEM,
		id = arg_14_1.id,
		count = arg_14_1.count
	})

	updateDrop(arg_14_0.itemTF:Find("left/IconTpl"), setmetatable({
		count = 0
	}, {
		__index = var_14_0
	}))
	UpdateOwnDisplay(arg_14_0.itemTF:Find("left/own"), var_14_0)
	setText(arg_14_0.nameTF, arg_14_1:getConfig("name"))
	setText(arg_14_0.descTF, arg_14_1:getConfig("display"))
end

return var_0_0
