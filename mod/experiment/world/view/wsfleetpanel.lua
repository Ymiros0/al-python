local var_0_0 = class("WSFleetPanel", import("...BaseEntity"))

var_0_0.Fields = {
	map = "table",
	onCancel = "function",
	btnGo = "userdata",
	rtLimitTips = "userdata",
	toggles = "table",
	btnBack = "userdata",
	rtEmptyTpl = "userdata",
	fleets = "table",
	toggleMask = "userdata",
	rtShipTpl = "userdata",
	transform = "userdata",
	toggleList = "userdata",
	onConfirm = "function",
	rtFleets = "table",
	rtLimitElite = "userdata",
	rtLimit = "userdata",
	selectIds = "table"
}

function var_0_0.Setup(arg_1_0)
	pg.DelegateInfo.New(arg_1_0)
	arg_1_0:Init()
end

function var_0_0.Dispose(arg_2_0)
	pg.DelegateInfo.Dispose(arg_2_0)
	arg_2_0:Clear()
end

function var_0_0.Init(arg_3_0)
	local var_3_0 = arg_3_0.transform

	arg_3_0.rtShipTpl = var_3_0:Find("panel/shiptpl")
	arg_3_0.rtEmptyTpl = var_3_0:Find("panel/emptytpl")
	arg_3_0.rtFleets = {
		[FleetType.Normal] = {
			var_3_0:Find("panel/bg/content/fleet/1"),
			var_3_0:Find("panel/bg/content/fleet/2"),
			var_3_0:Find("panel/bg/content/fleet/3"),
			var_3_0:Find("panel/bg/content/fleet/4")
		},
		[FleetType.Submarine] = {
			var_3_0:Find("panel/bg/content/sub/1")
		}
	}
	arg_3_0.rtLimit = var_3_0:Find("panel/limit")
	arg_3_0.rtLimitElite = var_3_0:Find("panel/limit_elite")
	arg_3_0.rtLimitTips = var_3_0:Find("panel/limit_tip")
	arg_3_0.btnBack = var_3_0:Find("panel/btnBack")
	arg_3_0.btnGo = var_3_0:Find("panel/start_button")
	arg_3_0.toggleMask = var_3_0:Find("mask")
	arg_3_0.toggleList = var_3_0:Find("mask/list")
	arg_3_0.toggles = {}

	for iter_3_0 = 0, arg_3_0.toggleList.childCount - 1 do
		table.insert(arg_3_0.toggles, arg_3_0.toggleList:Find("item" .. iter_3_0 + 1))
	end

	setActive(arg_3_0.rtShipTpl, false)
	setActive(arg_3_0.rtEmptyTpl, false)
	setActive(arg_3_0.toggleMask, false)
end

function var_0_0.UpdateMulti(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	arg_4_0.map = arg_4_1
	arg_4_0.fleets = _(_.values(arg_4_2)):chain():filter(function(arg_5_0)
		return arg_5_0:isRegularFleet()
	end):sort(function(arg_6_0, arg_6_1)
		return arg_6_0.id < arg_6_1.id
	end):value()
	arg_4_0.selectIds = {
		[FleetType.Normal] = {},
		[FleetType.Submarine] = {}
	}

	for iter_4_0, iter_4_1 in ipairs(arg_4_3 or {}) do
		local var_4_0 = arg_4_0:getFleetById(iter_4_1)

		if var_4_0 then
			local var_4_1 = var_4_0:getFleetType()
			local var_4_2 = arg_4_0.selectIds[var_4_1]

			if #var_4_2 < arg_4_0:getLimitNums(var_4_1) then
				table.insert(var_4_2, iter_4_1)
			end
		end
	end

	setActive(arg_4_0.rtLimitElite, false)
	setActive(arg_4_0.rtLimitTips, false)
	setActive(arg_4_0.rtLimit, true)
	onButton(arg_4_0, arg_4_0.btnGo, function()
		arg_4_0.onConfirm(arg_4_0:getSelectIds())
	end, SFX_UI_WEIGHANCHOR_GO)
	onButton(arg_4_0, arg_4_0.btnBack, function()
		arg_4_0.onCancel()
	end, SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.transform, function()
		arg_4_0.onCancel()
	end, SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.toggleMask, function()
		arg_4_0:hideToggleMask()
	end, SFX_CANCEL)
	arg_4_0:clearFleets()
	arg_4_0:updateFleets()
	arg_4_0:updateLimit()
end

function var_0_0.getFleetById(arg_11_0, arg_11_1)
	return _.detect(arg_11_0.fleets, function(arg_12_0)
		return arg_12_0.id == arg_11_1
	end)
end

function var_0_0.getLimitNums(arg_13_0, arg_13_1)
	local var_13_0 = 0

	if arg_13_1 == FleetType.Normal then
		var_13_0 = 4
	elseif arg_13_1 == FleetType.Submarine then
		var_13_0 = 1
	end

	return var_13_0
end

function var_0_0.getSelectIds(arg_14_0)
	local var_14_0 = {}

	for iter_14_0, iter_14_1 in pairs(arg_14_0.selectIds) do
		for iter_14_2, iter_14_3 in ipairs(iter_14_1) do
			if iter_14_3 > 0 then
				table.insert(var_14_0, iter_14_3)
			end
		end
	end

	_.sort(var_14_0, function(arg_15_0, arg_15_1)
		return arg_15_0 < arg_15_1
	end)

	return var_14_0
end

function var_0_0.updateFleets(arg_16_0)
	for iter_16_0, iter_16_1 in pairs(arg_16_0.rtFleets) do
		for iter_16_2 = 1, #iter_16_1 do
			arg_16_0:updateFleet(iter_16_0, iter_16_2)
		end
	end
end

function var_0_0.updateLimit(arg_17_0)
	local var_17_0 = #_.filter(arg_17_0.selectIds[FleetType.Normal], function(arg_18_0)
		return arg_18_0 > 0
	end)
	local var_17_1 = #_.filter(arg_17_0.selectIds[FleetType.Submarine], function(arg_19_0)
		return arg_19_0 > 0
	end)
	local var_17_2 = arg_17_0:getLimitNums(FleetType.Normal)

	setText(arg_17_0.rtLimit:Find("number"), string.format("%d/%d", var_17_0, var_17_2))

	local var_17_3 = arg_17_0:getLimitNums(FleetType.Submarine)

	setText(arg_17_0.rtLimit:Find("number_sub"), string.format("%d/%d", var_17_1, var_17_3))
end

function var_0_0.selectFleet(arg_20_0, arg_20_1, arg_20_2, arg_20_3)
	if fleetId ~= arg_20_3 then
		local var_20_0 = arg_20_0.selectIds[arg_20_1]

		if arg_20_3 > 0 and table.contains(var_20_0, arg_20_3) then
			return
		end

		if arg_20_1 == FleetType.Normal and arg_20_0:getLimitNums(arg_20_1) > 0 and arg_20_3 == 0 and #_.filter(var_20_0, function(arg_21_0)
			return arg_21_0 > 0
		end) == 1 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("level_fleet_lease_one_ship"))

			return
		end

		local var_20_1 = arg_20_0:getFleetById(arg_20_3)

		if var_20_1 then
			if not var_20_1:isUnlock() then
				return
			end

			if var_20_1:isLegalToFight() ~= true then
				pg.TipsMgr.GetInstance():ShowTips(i18n("level_fleet_not_enough"))

				return
			end
		end

		var_20_0[arg_20_2] = arg_20_3

		arg_20_0:updateFleet(arg_20_1, arg_20_2)
		arg_20_0:updateLimit()
	end
end

function var_0_0.updateFleet(arg_22_0, arg_22_1, arg_22_2)
	local var_22_0 = arg_22_0.selectIds[arg_22_1][arg_22_2]
	local var_22_1 = arg_22_0:getFleetById(var_22_0)
	local var_22_2 = arg_22_2 <= arg_22_0:getLimitNums(arg_22_1)
	local var_22_3 = arg_22_0.rtFleets[arg_22_1][arg_22_2]
	local var_22_4 = var_22_3:Find("bg/name")
	local var_22_5 = var_22_3:Find("main")
	local var_22_6 = var_22_3:Find("vanguard")
	local var_22_7 = var_22_3:Find("sub")
	local var_22_8 = var_22_3:Find("btn_select")
	local var_22_9 = var_22_3:Find("btn_recom")
	local var_22_10 = var_22_3:Find("btn_clear")
	local var_22_11 = var_22_3:Find("blank")
	local var_22_12 = var_22_3:Find("selected")

	setText(var_22_4, "")
	setActive(var_22_12, false)
	setActive(var_22_8, var_22_2)
	setActive(var_22_10, var_22_2)
	setActive(var_22_9, false)
	setActive(var_22_11, not var_22_2)

	if var_22_5 then
		setActive(var_22_5, var_22_2 and var_22_1)
	end

	if var_22_6 then
		setActive(var_22_6, var_22_2 and var_22_1)
	end

	if var_22_7 then
		setActive(var_22_7, var_22_2 and var_22_1)
	end

	if var_22_2 then
		if var_22_1 then
			setText(var_22_4, var_22_1.name == "" and Fleet.DEFAULT_NAME[var_22_1.id] or var_22_1.name)

			if arg_22_1 == FleetType.Submarine then
				arg_22_0:updateShips(var_22_7, var_22_1.subShips)
			else
				arg_22_0:updateShips(var_22_5, var_22_1.mainShips)
				arg_22_0:updateShips(var_22_6, var_22_1.vanguardShips)
			end
		end

		onButton(arg_22_0, var_22_8, function()
			arg_22_0.toggleList.position = (var_22_8.position + var_22_10.position) / 2
			arg_22_0.toggleList.anchoredPosition = arg_22_0.toggleList.anchoredPosition + Vector2(-arg_22_0.toggleList.rect.width / 2, -var_22_8.rect.height / 2)

			arg_22_0:showToggleMask(arg_22_1, function(arg_24_0)
				arg_22_0:hideToggleMask()
				arg_22_0:selectFleet(arg_22_1, arg_22_2, arg_24_0)
			end)
		end, SFX_UI_CLICK)
		onButton(arg_22_0, var_22_10, function()
			arg_22_0:selectFleet(arg_22_1, arg_22_2, 0)
		end, SFX_UI_CLICK)
	end
end

function var_0_0.updateShips(arg_26_0, arg_26_1, arg_26_2)
	local var_26_0 = UIItemList.New(arg_26_1, arg_26_0.rtShipTpl)

	var_26_0:make(function(arg_27_0, arg_27_1, arg_27_2)
		if arg_27_0 == UIItemList.EventUpdate then
			local var_27_0 = getProxy(BayProxy):getShipById(arg_26_2[arg_27_1 + 1])

			updateShip(arg_27_2, var_27_0)

			local var_27_1 = arg_27_2:Find("icon_bg/energy")
			local var_27_2 = var_27_0:getEnergeConfig()

			if var_27_2 and var_27_2.id <= 2 then
				setActive(var_27_1, true)
				GetImageSpriteFromAtlasAsync("energy", var_27_2.icon, var_27_1)
			else
				setActive(var_27_1, false)
			end
		end
	end)
	var_26_0:align(#arg_26_2)
end

function var_0_0.showToggleMask(arg_28_0, arg_28_1, arg_28_2)
	setActive(arg_28_0.toggleMask, true)

	local var_28_0 = _.filter(arg_28_0.fleets, function(arg_29_0)
		return arg_29_0:getFleetType() == arg_28_1
	end)

	for iter_28_0, iter_28_1 in ipairs(arg_28_0.toggles) do
		local var_28_1 = var_28_0[iter_28_0]

		setActive(iter_28_1, var_28_1)

		if var_28_1 then
			local var_28_2, var_28_3 = var_28_1:isUnlock()
			local var_28_4 = iter_28_1:Find("lock")

			setButtonEnabled(iter_28_1, var_28_2)
			setActive(var_28_4, not var_28_2)

			if var_28_2 then
				local var_28_5 = table.contains(arg_28_0.selectIds[arg_28_1], var_28_1.id)

				setActive(iter_28_1:Find("selected"), var_28_5)
				setActive(iter_28_1:Find("text"), not var_28_5)
				setActive(iter_28_1:Find("text_selected"), var_28_5)
				onButton(arg_28_0, iter_28_1, function()
					arg_28_2(var_28_1.id)
				end, SFX_UI_TAG)
			else
				onButton(arg_28_0, var_28_4, function()
					pg.TipsMgr.GetInstance():ShowTips(var_28_3)
				end, SFX_UI_CLICK)
			end
		end
	end
end

function var_0_0.hideToggleMask(arg_32_0)
	setActive(arg_32_0.toggleMask, false)
end

function var_0_0.clearFleets(arg_33_0)
	for iter_33_0, iter_33_1 in pairs(arg_33_0.rtFleets) do
		_.each(iter_33_1, function(arg_34_0)
			arg_33_0:clearFleet(arg_34_0)
		end)
	end
end

function var_0_0.clearFleet(arg_35_0, arg_35_1)
	local var_35_0 = arg_35_1:Find("main")
	local var_35_1 = arg_35_1:Find("vanguard")
	local var_35_2 = arg_35_1:Find("sub")

	if var_35_0 then
		removeAllChildren(var_35_0)
	end

	if var_35_1 then
		removeAllChildren(var_35_1)
	end

	if var_35_2 then
		removeAllChildren(var_35_2)
	end
end

return var_0_0
