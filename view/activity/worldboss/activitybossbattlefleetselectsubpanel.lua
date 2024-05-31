local var_0_0 = class("ActivityBossBattleFleetSelectSubPanel", import("view.base.BaseSubPanel"))

function var_0_0.getUIName(arg_1_0)
	return "ActivityBossFleetSelectView"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0.tfShipTpl = arg_2_0:findTF("panel/shiptpl")
	arg_2_0.tfEmptyTpl = arg_2_0:findTF("panel/emptytpl")
	arg_2_0.tfFleets = {
		[FleetType.Normal] = {
			arg_2_0:findTF("panel/fleet/1"),
			arg_2_0:findTF("panel/fleet/2")
		},
		[FleetType.Submarine] = {
			arg_2_0:findTF("panel/sub/1")
		}
	}
	arg_2_0.tfLimit = arg_2_0:findTF("panel/limit_list/limit")
	arg_2_0.tfLimitTips = arg_2_0:findTF("panel/limit_list/limit_tip")
	arg_2_0.tfLimitElite = arg_2_0:findTF("panel/limit_list/limit_elite")
	arg_2_0.tfLimitContainer = arg_2_0:findTF("panel/limit_list/limit_elite/limit_list")
	arg_2_0.rtCostLimit = arg_2_0._tf:Find("panel/limit_list/cost_limit")
	arg_2_0.btnBack = arg_2_0:findTF("panel/btnBack")
	arg_2_0.btnGo = arg_2_0:findTF("panel/start_button")
	arg_2_0.btnTry = arg_2_0:findTF("panel/try_button")
	arg_2_0.btnASHelp = arg_2_0:findTF("panel/title/ASvalue")
	arg_2_0.commanderToggle = arg_2_0:findTF("panel/commander_btn")
	arg_2_0.formationToggle = arg_2_0:findTF("panel/formation_btn")
	arg_2_0.toggleMask = arg_2_0:findTF("mask")
	arg_2_0.toggleList = arg_2_0:findTF("mask/list")
	arg_2_0.toggles = {}

	for iter_2_0 = 0, arg_2_0.toggleList.childCount - 1 do
		table.insert(arg_2_0.toggles, arg_2_0.toggleList:Find("item" .. iter_2_0 + 1))
	end

	arg_2_0.btnSp = arg_2_0:findTF("panel/sp")
	arg_2_0.spMask = arg_2_0:findTF("mask_sp")

	setActive(arg_2_0.tfShipTpl, false)
	setActive(arg_2_0.tfEmptyTpl, false)
	setActive(arg_2_0.toggleMask, false)
	setActive(arg_2_0.btnSp, false)
	setActive(arg_2_0.spMask, false)
	setActive(arg_2_0.tfLimitElite, false)
	setActive(arg_2_0.tfLimitTips, false)
	setActive(arg_2_0.tfLimit, false)
	setActive(arg_2_0:findTF("panel/title/ASvalue"), false)
	setText(arg_2_0:findTF("panel/formation_btn/text"), i18n("autofight_formation"))
	setText(arg_2_0:findTF("panel/commander_btn/text"), i18n("autofight_cat"))
	setText(arg_2_0._tf:Find("panel/title/Image/text"), i18n("fleet_select_title"))
	arg_2_0:InitInteractable()
end

function var_0_0.InitInteractable(arg_3_0)
	onButton(arg_3_0, arg_3_0.btnGo, function()
		arg_3_0:OnCombat()
	end, SFX_UI_WEIGHANCHOR_GO)
	onButton(arg_3_0, arg_3_0.btnTry, function()
		arg_3_0:OnTrybat()
	end, SFX_UI_WEIGHANCHOR_GO)
	onButton(arg_3_0, arg_3_0.btnBack, function()
		arg_3_0:OnCancel()
		arg_3_0:OnCommit()
	end, SFX_CANCEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0:OnCancel()
		arg_3_0:OnCommit()
	end, SFX_CANCEL)
	onToggle(arg_3_0, arg_3_0.commanderToggle, function(arg_8_0)
		if arg_8_0 then
			arg_3_0.viewParent.contextData.showCommander = arg_8_0

			for iter_8_0, iter_8_1 in pairs(arg_3_0.tfFleets) do
				for iter_8_2 = 1, #iter_8_1 do
					arg_3_0:updateCommanderBtn(iter_8_0, iter_8_2)
				end
			end
		end
	end, SFX_PANEL)
	onToggle(arg_3_0, arg_3_0.formationToggle, function(arg_9_0)
		if arg_9_0 then
			arg_3_0.viewParent.contextData.showCommander = not arg_9_0

			for iter_9_0, iter_9_1 in pairs(arg_3_0.tfFleets) do
				for iter_9_2 = 1, #iter_9_1 do
					arg_3_0:updateCommanderBtn(iter_9_0, iter_9_2)
				end
			end
		end
	end, SFX_PANEL)
end

function var_0_0.SetFleets(arg_10_0, arg_10_1)
	arg_10_0.fleets = {
		[FleetType.Normal] = {},
		[FleetType.Submarine] = {}
	}

	for iter_10_0, iter_10_1 in pairs(arg_10_1) do
		iter_10_1:RemoveUnusedItems()

		if iter_10_1:isSubmarineFleet() then
			if #arg_10_0.fleets[FleetType.Submarine] < arg_10_0:getLimitNums(FleetType.Submarine) then
				table.insert(arg_10_0.fleets[FleetType.Submarine], iter_10_1)
			end
		elseif #arg_10_0.fleets[FleetType.Normal] < arg_10_0:getLimitNums(FleetType.Normal) then
			table.insert(arg_10_0.fleets[FleetType.Normal], iter_10_1)
		end
	end
end

function var_0_0.SetOilLimit(arg_11_0, arg_11_1)
	local var_11_0 = _.any(arg_11_1, function(arg_12_0)
		return arg_12_0 > 0
	end)

	setActive(arg_11_0.rtCostLimit, var_11_0)
	setText(arg_11_0.rtCostLimit:Find("text"), i18n("formationScene_use_oil_limit_tip_worldboss"))

	if var_11_0 then
		local var_11_1 = 0
		local var_11_2 = arg_11_1[1]

		setActive(arg_11_0.rtCostLimit:Find("cost_noraml/Text"), var_11_2 > 0)

		if var_11_2 > 0 then
			setText(arg_11_0.rtCostLimit:Find("cost_noraml/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_surface"), var_11_2))
		end

		local var_11_3 = 0

		setActive(arg_11_0.rtCostLimit:Find("cost_boss/Text"), var_11_3 > 0)

		local var_11_4 = arg_11_1[2]

		setActive(arg_11_0.rtCostLimit:Find("cost_sub/Text"), var_11_4 > 0)

		if var_11_4 > 0 then
			setText(arg_11_0.rtCostLimit:Find("cost_sub/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_submarine"), var_11_4))
		end
	end
end

function var_0_0.SetSettings(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
	arg_13_0.groupNum = arg_13_1
	arg_13_0.submarineNum = arg_13_2
	arg_13_0.showTryBtn = arg_13_3
end

function var_0_0.UpdateView(arg_14_0)
	arg_14_0:clearFleets()
	arg_14_0:UpdateFleets()

	local var_14_0 = not LOCK_COMMANDER and pg.SystemOpenMgr.GetInstance():isOpenSystem(getProxy(PlayerProxy):getRawData().level, "CommanderCatMediator")

	triggerToggle(arg_14_0.viewParent.contextData.showCommander and var_14_0 and arg_14_0.commanderToggle or arg_14_0.formationToggle, true)
	setActive(arg_14_0.commanderToggle, var_14_0)
	setActive(arg_14_0.btnTry, arg_14_0.showTryBtn)
end

function var_0_0.getLimitNums(arg_15_0, arg_15_1)
	local var_15_0 = 0

	if arg_15_1 == FleetType.Normal then
		var_15_0 = arg_15_0.groupNum
	elseif arg_15_1 == FleetType.Submarine then
		var_15_0 = arg_15_0.submarineNum
	end

	return var_15_0 or 0
end

function var_0_0.UpdateFleets(arg_16_0)
	for iter_16_0, iter_16_1 in pairs(arg_16_0.tfFleets) do
		for iter_16_2 = 1, #iter_16_1 do
			arg_16_0:updateFleet(iter_16_0, iter_16_2)
		end
	end
end

function var_0_0.updateFleet(arg_17_0, arg_17_1, arg_17_2)
	arg_17_0:updateCommanderBtn(arg_17_1, arg_17_2)

	local var_17_0 = arg_17_2 <= arg_17_0:getLimitNums(arg_17_1)
	local var_17_1 = var_17_0 and arg_17_0.fleets[arg_17_1][arg_17_2]
	local var_17_2 = arg_17_0.tfFleets[arg_17_1][arg_17_2]
	local var_17_3 = findTF(var_17_2, "bg/name")
	local var_17_4 = arg_17_0:findTF(TeamType.Main, var_17_2)
	local var_17_5 = arg_17_0:findTF(TeamType.Vanguard, var_17_2)
	local var_17_6 = arg_17_0:findTF(TeamType.Submarine, var_17_2)
	local var_17_7 = arg_17_0:findTF("btn_recom", var_17_2)
	local var_17_8 = arg_17_0:findTF("btn_clear", var_17_2)
	local var_17_9 = arg_17_0:findTF("selected", var_17_2)
	local var_17_10 = arg_17_0:findTF("commander", var_17_2)

	setActive(var_17_9, false)
	setText(var_17_3, "")

	if var_17_4 then
		setActive(var_17_4, var_17_0 and var_17_1)
	end

	if var_17_5 then
		setActive(var_17_5, var_17_0 and var_17_1)
	end

	if var_17_6 then
		setActive(var_17_6, var_17_0 and var_17_1)
	end

	if var_17_0 and var_17_1 then
		setText(var_17_3, Fleet.DEFAULT_NAME_BOSS_ACT[var_17_1.id] or "")

		if arg_17_1 == FleetType.Submarine then
			arg_17_0:updateShips(var_17_6, var_17_1.subShips, var_17_1.id, TeamType.Submarine)
		else
			arg_17_0:updateShips(var_17_4, var_17_1.mainShips, var_17_1.id, TeamType.Main)
			arg_17_0:updateShips(var_17_5, var_17_1.vanguardShips, var_17_1.id, TeamType.Vanguard)
		end

		arg_17_0:updateCommanders(var_17_10, var_17_1)
		onButton(arg_17_0, var_17_7, function()
			arg_17_0:emit(arg_17_0.viewParent.contextData.mediatorClass.ON_FLEET_RECOMMEND, var_17_1.id)
		end)
		onButton(arg_17_0, var_17_8, function()
			arg_17_0:emit(arg_17_0.viewParent.contextData.mediatorClass.ON_FLEET_CLEAR, var_17_1.id)
		end, SFX_UI_CLICK)
	end
end

function var_0_0.updateShips(arg_20_0, arg_20_1, arg_20_2, arg_20_3, arg_20_4)
	removeAllChildren(arg_20_1)

	local var_20_0 = getProxy(BayProxy)

	for iter_20_0 = 1, 3 do
		local var_20_1 = var_20_0:getShipById(arg_20_2[iter_20_0])
		local var_20_2 = var_20_1 and arg_20_0.tfShipTpl or arg_20_0.tfEmptyTpl
		local var_20_3 = cloneTplTo(var_20_2, arg_20_1)

		setActive(var_20_3, true)

		if var_20_1 then
			updateShip(var_20_3, var_20_1)
			setActive(var_20_3:Find("event_block"), var_20_1:getFlag("inEvent"))
		end

		setActive(arg_20_0:findTF("ship_type", var_20_3), false)

		local var_20_4 = GetOrAddComponent(var_20_3, typeof(UILongPressTrigger))

		var_20_4.onLongPressed:RemoveAllListeners()

		local function var_20_5()
			arg_20_0:emit(arg_20_0.viewParent.contextData.mediatorClass.ON_OPEN_DOCK, {
				fleet = arg_20_2,
				shipVO = var_20_1,
				fleetIndex = arg_20_3,
				teamType = arg_20_4
			})
		end

		onButton(arg_20_0, var_20_3, var_20_5)
		var_20_4.onLongPressed:AddListener(function()
			if var_20_1 then
				arg_20_0:OnLongPressShip(arg_20_2[iter_20_0], arg_20_3)
			else
				var_20_5()
			end
		end)
	end
end

function var_0_0.updateCommanderBtn(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = arg_23_2 <= arg_23_0:getLimitNums(arg_23_1)
	local var_23_1 = var_23_0 and arg_23_0.fleets[arg_23_1][arg_23_2]
	local var_23_2 = arg_23_0.tfFleets[arg_23_1][arg_23_2]
	local var_23_3 = arg_23_0:findTF("btn_select", var_23_2)
	local var_23_4 = arg_23_0:findTF("btn_clear", var_23_2)
	local var_23_5 = arg_23_0:findTF("btn_recom", var_23_2)
	local var_23_6 = arg_23_0:findTF("blank", var_23_2)
	local var_23_7 = arg_23_0:findTF("commander", var_23_2)

	setActive(var_23_3, false)
	setActive(var_23_4, var_23_0 and not arg_23_0.viewParent.contextData.showCommander)
	setActive(var_23_5, var_23_0 and not arg_23_0.viewParent.contextData.showCommander)
	setActive(var_23_7, var_23_0 and var_23_1 and arg_23_0.viewParent.contextData.showCommander)
	setActive(var_23_6, not var_23_0 or var_23_0 and not var_23_1 and arg_23_0.viewParent.contextData.showCommander)
end

function var_0_0.updateCommanders(arg_24_0, arg_24_1, arg_24_2)
	for iter_24_0 = 1, 2 do
		local var_24_0 = arg_24_2:getCommanderByPos(iter_24_0)
		local var_24_1 = arg_24_1:Find("pos" .. iter_24_0)
		local var_24_2 = var_24_1:Find("add")
		local var_24_3 = var_24_1:Find("info")

		setActive(var_24_2, not var_24_0)
		setActive(var_24_3, var_24_0)

		if var_24_0 then
			local var_24_4 = Commander.rarity2Frame(var_24_0:getRarity())

			setImageSprite(var_24_3:Find("frame"), GetSpriteFromAtlas("weaponframes", "commander_" .. var_24_4))
			GetImageSpriteFromAtlasAsync("CommanderHrz/" .. var_24_0:getPainting(), "", var_24_3:Find("mask/icon"))
		end

		onButton(arg_24_0, var_24_2, function()
			arg_24_0:InvokeParent("openCommanderPanel", arg_24_2, arg_24_2.id)
		end, SFX_PANEL)
		onButton(arg_24_0, var_24_3, function()
			arg_24_0:InvokeParent("openCommanderPanel", arg_24_2, arg_24_2.id)
		end, SFX_PANEL)
	end
end

function var_0_0.clearFleets(arg_27_0)
	for iter_27_0, iter_27_1 in pairs(arg_27_0.tfFleets) do
		_.each(iter_27_1, function(arg_28_0)
			arg_27_0:clearFleet(arg_28_0)
		end)
	end
end

function var_0_0.clearFleet(arg_29_0, arg_29_1)
	local var_29_0 = arg_29_0:findTF(TeamType.Main, arg_29_1)
	local var_29_1 = arg_29_0:findTF(TeamType.Vanguard, arg_29_1)
	local var_29_2 = arg_29_0:findTF(TeamType.Submarine, arg_29_1)

	if var_29_0 then
		removeAllChildren(var_29_0)
	end

	if var_29_1 then
		removeAllChildren(var_29_1)
	end

	if var_29_2 then
		removeAllChildren(var_29_2)
	end
end

function var_0_0.OnShow(arg_30_0)
	local var_30_0 = #getProxy(ContextProxy):getCurrentContext().children > 0 and LayerWeightConst.LOWER_LAYER or nil

	pg.UIMgr.GetInstance():BlurPanel(arg_30_0._tf, nil, {
		groupName = LayerWeightConst.GROUP_FORMATION_PAGE,
		weight = var_30_0
	})
end

function var_0_0.OnHide(arg_31_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_31_0._tf, arg_31_0.viewParent._tf)
	triggerToggle(arg_31_0.commanderToggle, false)
end

function var_0_0.OnCancel(arg_32_0)
	arg_32_0:InvokeParent("hideFleetEdit")
end

function var_0_0.OnCommit(arg_33_0)
	arg_33_0:InvokeParent("commitEdit")
end

function var_0_0.OnCombat(arg_34_0)
	arg_34_0:InvokeParent("commitEdit")
	arg_34_0:InvokeParent("commitCombat")
end

function var_0_0.OnTrybat(arg_35_0)
	arg_35_0:InvokeParent("commitEdit")
	arg_35_0:InvokeParent("commitTrybat")
end

function var_0_0.OnLongPressShip(arg_36_0, arg_36_1, arg_36_2)
	arg_36_0:InvokeParent("openShipInfo", arg_36_1, arg_36_2)
end

return var_0_0
