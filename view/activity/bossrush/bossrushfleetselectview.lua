local var_0_0 = class("BossRushFleetSelectView", import("view.base.BaseUI"))
local var_0_1 = {
	vanguard = 1,
	submarine = 3,
	main = 2
}

function var_0_0.getUIName(arg_1_0)
	return "BossRushFleetSelectUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:InitUI()
end

function var_0_0.InitUI(arg_3_0)
	local var_3_0 = arg_3_0._tf:Find("Panel")

	arg_3_0.tfFleets = {
		[FleetType.Normal] = arg_3_0:findTF("Panel/Fleet/Normal"),
		[FleetType.Submarine] = arg_3_0:findTF("Panel/Fleet/Submarine")
	}
	arg_3_0.btnRecommend = var_3_0:Find("Fleet/BtnRecommend")
	arg_3_0.btnClear = var_3_0:Find("Fleet/BtnClear")
	arg_3_0.rtCostLimit = var_3_0:Find("Fleet/CostLimit")
	arg_3_0.commanderList = var_3_0:Find("Fleet/Commander")
	arg_3_0.fleetIndexToggles = _.map(_.range(var_3_0:Find("Fleet/Indexes").childCount), function(arg_4_0)
		return var_3_0:Find("Fleet/Indexes"):GetChild(arg_4_0 - 1)
	end)
	arg_3_0.modeToggles = {
		var_3_0:Find("Info/Modes/Single"),
		var_3_0:Find("Info/Modes/Multiple")
	}
	arg_3_0.extraAwardTF = arg_3_0._tf:Find("Panel/Reward/Normal/Mode")
	arg_3_0.sonarRangeContainer = arg_3_0._tf:Find("Panel/Fleet/SonarRange")
	arg_3_0.sonarRangeTexts = {
		arg_3_0._tf:Find("Panel/Fleet/SonarRange/Values"):GetChild(0),
		arg_3_0._tf:Find("Panel/Fleet/SonarRange/Values"):GetChild(1)
	}

	setText(arg_3_0.sonarRangeTexts[2], "")

	arg_3_0.btnBack = var_3_0:Find("Info/Title/BtnClose")
	arg_3_0.btnGo = var_3_0:Find("Info/Start")

	setText(arg_3_0._tf:Find("Panel/Fleet/SonarRange/Text"), i18n("fleet_antisub_range") .. ":")
	setText(arg_3_0._tf:Find("Panel/Fleet/CostLimit/Title"), i18n("formationScene_use_oil_limit_tip_worldboss"))
	setText(arg_3_0._tf:Find("Panel/Reward/Normal/Base/Text"), i18n("series_enemy_reward_tip1"))
	setText(arg_3_0._tf:Find("Panel/Reward/Normal/Mode/Text"), i18n("series_enemy_reward_tip2"))
	setText(arg_3_0._tf:Find("Panel/Reward/EX/Title"), i18n("series_enemy_reward_tip4"))
	setText(arg_3_0._tf:Find("Panel/Reward/Tip"), i18n("limit_team_character_tips"))
	setText(arg_3_0._tf:Find("Panel/Info/Modes/Single/On/Text"), i18n("series_enemy_mode_1"))
	setText(arg_3_0._tf:Find("Panel/Info/Modes/Single/Off/Text"), i18n("series_enemy_mode_1"))
	setText(arg_3_0._tf:Find("Panel/Info/Modes/Multiple/On/Text"), i18n("series_enemy_mode_2"))
	setText(arg_3_0._tf:Find("Panel/Info/Modes/Multiple/Off/Text"), i18n("series_enemy_mode_2"))
	table.Foreach(arg_3_0.fleetIndexToggles, function(arg_5_0, arg_5_1)
		if arg_5_0 >= #arg_3_0.fleetIndexToggles then
			setText(arg_5_1:Find("Text"), i18n("formationScene_use_oil_limit_submarine"))
		else
			setText(arg_5_1:Find("Text"), i18n("series_enemy_fleet_prefix", GetRomanDigit(arg_5_0)))
		end
	end)
	setText(arg_3_0._tf:Find("Panel/Fleet/Normal/main/Item/Ship/EnergyWarn/Text"), i18n("series_enemy_mood"))
	setText(arg_3_0._tf:Find("Panel/Fleet/Normal/vanguard/Item/Ship/EnergyWarn/Text"), i18n("series_enemy_mood"))
	setText(arg_3_0._tf:Find("Panel/Fleet/Submarine/submarine/Item/Ship/EnergyWarn/Text"), i18n("series_enemy_mood"))
end

function var_0_0.didEnter(arg_6_0)
	local var_6_0 = arg_6_0.contextData.seriesData

	onButton(arg_6_0, arg_6_0.btnGo, function()
		for iter_7_0 = 1, #arg_6_0.contextData.fleets - 1 do
			if arg_6_0.contextData.fleets[iter_7_0]:isLegalToFight() ~= true then
				pg.TipsMgr.GetInstance():ShowTips(i18n("series_enemy_team_notenough"))

				return
			end
		end

		if _.any(arg_6_0.contextData.fleets, function(arg_8_0)
			local var_8_0, var_8_1 = arg_8_0:HaveShipsInEvent()

			if var_8_0 then
				pg.TipsMgr.GetInstance():ShowTips(var_8_1)

				return true
			end
		end) then
			return
		end

		arg_6_0:emit(BossRushFleetSelectMediator.ON_PRECOMBAT)
	end, SFX_UI_WEIGHANCHOR_GO)
	onButton(arg_6_0, arg_6_0.sonarRangeContainer, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.fleet_antisub_range_tip.tip
		})
	end, SFX_PANEL)
	onButton(arg_6_0, arg_6_0.btnBack, function()
		arg_6_0:onCancelHard()
	end, SFX_CANCEL)
	onButton(arg_6_0, arg_6_0._tf:Find("BG"), function()
		arg_6_0:onCancelHard()
	end, SFX_CANCEL)

	local var_6_1 = var_6_0:IsSingleFight()

	setActive(arg_6_0.modeToggles[1].parent, var_6_1)

	if var_6_1 then
		table.Foreach(arg_6_0.modeToggles, function(arg_12_0, arg_12_1)
			triggerToggle(arg_12_1, arg_12_0 == arg_6_0.contextData.mode)
		end)
		table.Foreach(arg_6_0.modeToggles, function(arg_13_0, arg_13_1)
			onToggle(arg_6_0, arg_13_1, function(arg_14_0)
				if not arg_14_0 then
					return
				end

				arg_6_0:emit(BossRushFleetSelectMediator.ON_SWITCH_MODE, arg_13_0)
				table.Foreach(arg_6_0.fleetIndexToggles, function(arg_15_0, arg_15_1)
					triggerToggle(arg_15_1, arg_15_0 == arg_6_0.contextData.fleetIndex)
				end)
			end, SFX_PANEL)
		end)
	end

	local var_6_2 = #arg_6_0.contextData.fullFleets

	table.Foreach(arg_6_0.fleetIndexToggles, function(arg_16_0, arg_16_1)
		setActive(arg_16_1, arg_16_0 <= var_6_2 - 1 or arg_16_0 == #arg_6_0.fleetIndexToggles)
	end)

	for iter_6_0 = #arg_6_0.fleetIndexToggles - 1, var_6_2, -1 do
		table.remove(arg_6_0.fleetIndexToggles, iter_6_0)
	end

	local var_6_3 = Color.white
	local var_6_4 = Color.New(1, 1, 1, 0.5)

	local function var_6_5(arg_17_0, arg_17_1)
		setActive(arg_17_0:Find("Selected"), arg_17_1)
		setTextColor(arg_17_0:Find("Text"), arg_17_1 and var_6_3 or var_6_4)
	end

	table.Foreach(arg_6_0.fleetIndexToggles, function(arg_18_0, arg_18_1)
		onToggle(arg_6_0, arg_18_1, function(arg_19_0)
			var_6_5(arg_18_1, arg_19_0)
		end)
	end)
	table.Foreach(arg_6_0.fleetIndexToggles, function(arg_20_0, arg_20_1)
		triggerToggle(arg_20_1, arg_20_0 == arg_6_0.contextData.fleetIndex)
	end)
	table.Foreach(arg_6_0.fleetIndexToggles, function(arg_21_0, arg_21_1)
		onToggle(arg_6_0, arg_21_1, function(arg_22_0)
			var_6_5(arg_21_1, arg_22_0)

			if not arg_22_0 then
				return
			end

			if arg_21_0 == #arg_6_0.fleetIndexToggles then
				arg_6_0.contextData.fleetIndex = #arg_6_0.contextData.fleets
			else
				arg_6_0.contextData.fleetIndex = arg_21_0
			end

			arg_6_0:updateEliteFleets()
		end, SFX_PANEL)
	end)
	setText(arg_6_0._tf:Find("Panel/Info/Title/Text"), var_6_0:GetName())
	setText(arg_6_0._tf:Find("Panel/Info/Title/Text/EN"), var_6_0:GetSeriesCode())
	setText(arg_6_0._tf:Find("Panel/Info/Description/Text"), var_6_0:GetDescription())

	local var_6_6 = var_6_0:GetExpeditionIds()
	local var_6_7 = var_6_0:GetBossIcons()
	local var_6_8 = arg_6_0._tf:Find("Panel/Info/Boss")

	UIItemList.StaticAlign(var_6_8, var_6_8:GetChild(0), #var_6_6, function(arg_23_0, arg_23_1, arg_23_2)
		if arg_23_0 ~= UIItemList.EventUpdate then
			return
		end

		local var_23_0 = var_6_6[arg_23_1 + 1]
		local var_23_1 = var_6_7[arg_23_1 + 1][1]
		local var_23_2 = pg.expedition_data_template[var_23_0].level
		local var_23_3 = arg_23_2:Find("shiptpl")
		local var_23_4 = findTF(var_23_3, "icon_bg")
		local var_23_5 = findTF(var_23_3, "icon_bg/frame")

		SetCompomentEnabled(var_23_4, "Image", false)
		SetCompomentEnabled(var_23_5, "Image", false)
		setActive(arg_23_2:Find("shiptpl/icon_bg/lv"), false)

		local var_23_6 = arg_23_2:Find("shiptpl/icon_bg/icon")

		GetImageSpriteFromAtlasAsync("SquareIcon/" .. var_23_1, "", var_23_6)

		local var_23_7 = findTF(var_23_3, "ship_type")

		if var_23_7 then
			setActive(var_23_7, true)
			setImageSprite(var_23_7, GetSpriteFromAtlas("shiptype", shipType2print(var_6_7[arg_23_1 + 1][2])))
		end
	end)

	local function var_6_9(arg_24_0)
		if type(arg_24_0) ~= "table" then
			return {}
		end

		return arg_24_0
	end

	local var_6_10 = var_6_0:GetType() == BossRushSeriesData.TYPE.EXTRA

	setActive(arg_6_0._tf:Find("Panel/Reward/Normal"), not var_6_10)
	setActive(arg_6_0._tf:Find("Panel/Reward/EX"), var_6_10)

	if not var_6_10 then
		local var_6_11 = arg_6_0._tf:Find("Panel/Reward/Normal/Base/Items")
		local var_6_12 = var_6_9(var_6_0:GetPassAwards())

		UIItemList.StaticAlign(var_6_11, var_6_11:GetChild(0), #var_6_12, function(arg_25_0, arg_25_1, arg_25_2)
			if arg_25_0 ~= UIItemList.EventUpdate then
				return
			end

			local var_25_0 = var_6_12[arg_25_1 + 1]
			local var_25_1 = {
				type = var_25_0[1],
				id = var_25_0[2]
			}

			updateDrop(arg_25_2, var_25_1)
			onButton(arg_6_0, arg_25_2, function()
				arg_6_0:ShowDropDetail(var_25_1)
			end, SFX_PANEL)
		end)

		local var_6_13 = arg_6_0.extraAwardTF:Find("Items")
		local var_6_14 = var_6_9(var_6_0:GetAdditionalAwards())

		UIItemList.StaticAlign(var_6_13, var_6_13:GetChild(0), #var_6_14, function(arg_27_0, arg_27_1, arg_27_2)
			if arg_27_0 ~= UIItemList.EventUpdate then
				return
			end

			local var_27_0 = var_6_14[arg_27_1 + 1]
			local var_27_1 = {
				type = var_27_0[1],
				id = var_27_0[2]
			}

			updateDrop(arg_27_2, var_27_1)
			onButton(arg_6_0, arg_27_2, function()
				arg_6_0:ShowDropDetail(var_27_1)
			end, SFX_PANEL)
		end)
	else
		local var_6_15 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_EXTRA_BOSSRUSH_RANK):GetScore()
		local var_6_16 = arg_6_0._tf:Find("Panel/Reward/EX/Title/Text")

		setText(var_6_16, math.floor(var_6_15))
	end

	arg_6_0:updateEliteFleets()
	pg.UIMgr.GetInstance():BlurPanel(arg_6_0._tf, nil, {})
end

local var_0_2 = {
	[99] = true
}

function var_0_0.ShowDropDetail(arg_29_0, arg_29_1)
	local var_29_0 = Item.getConfigData(arg_29_1.id)

	if var_29_0 and var_0_2[var_29_0.type] then
		local var_29_1 = var_29_0.display_icon
		local var_29_2 = {}

		for iter_29_0, iter_29_1 in ipairs(var_29_1) do
			local var_29_3 = iter_29_1[1]
			local var_29_4 = iter_29_1[2]

			var_29_2[#var_29_2 + 1] = {
				hideName = true,
				type = var_29_3,
				id = var_29_4
			}
		end

		arg_29_0:emit(var_0_0.ON_DROP_LIST, {
			item2Row = true,
			itemList = var_29_2,
			content = var_29_0.display
		})
	else
		arg_29_0:emit(var_0_0.ON_DROP, arg_29_1)
	end
end

function var_0_0.willExit(arg_30_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_30_0._tf)
end

function var_0_0.onCancelHard(arg_31_0)
	arg_31_0:emit(BossRushFleetSelectMediator.ON_UPDATE_CUSTOM_FLEET)
	arg_31_0:closeView()
end

function var_0_0.onBackPressed(arg_32_0)
	arg_32_0:onCancelHard()
	var_0_0.super.onBackPressed(arg_32_0)
end

function var_0_0.setHardShipVOs(arg_33_0, arg_33_1)
	arg_33_0.shipVOs = arg_33_1
end

function var_0_0.initAddButton(arg_34_0, arg_34_1, arg_34_2, arg_34_3)
	local var_34_0 = arg_34_0.contextData.fleets[arg_34_3]:getShipIds()
	local var_34_1 = {}
	local var_34_2 = {}

	for iter_34_0, iter_34_1 in ipairs(var_34_0) do
		var_34_1[arg_34_0.shipVOs[iter_34_1]] = true

		if arg_34_2 == arg_34_0.shipVOs[iter_34_1]:getTeamType() then
			table.insert(var_34_2, iter_34_1)
		end
	end

	local var_34_3 = _.map(var_34_0, function(arg_35_0)
		return arg_34_0.shipVOs[arg_35_0]
	end)

	table.sort(var_34_3, function(arg_36_0, arg_36_1)
		return var_0_1[arg_36_0:getTeamType()] < var_0_1[arg_36_1:getTeamType()] or var_0_1[arg_36_0:getTeamType()] == var_0_1[arg_36_1:getTeamType()] and table.indexof(var_34_0, arg_36_0.id) < table.indexof(var_34_0, arg_36_1.id)
	end)

	local var_34_4 = findTF(arg_34_1, arg_34_2)
	local var_34_5 = var_34_4:GetComponent("ContentSizeFitter")
	local var_34_6 = var_34_4:GetComponent("HorizontalLayoutGroup")

	var_34_5.enabled = true
	var_34_6.enabled = true
	arg_34_0.isDraging = false

	UIItemList.StaticAlign(var_34_4, var_34_4:GetChild(0), 3, function(arg_37_0, arg_37_1, arg_37_2)
		if arg_37_0 ~= UIItemList.EventUpdate then
			return
		end

		arg_37_1 = arg_37_1 + 1

		local var_37_0 = var_34_2[arg_37_1] and arg_34_0.shipVOs[var_34_2[arg_37_1]] or nil

		setActive(arg_37_2:Find("Ship"), var_37_0)
		setActive(arg_37_2:Find("Empty"), not var_37_0)

		local var_37_1 = var_37_0 and arg_37_2:Find("Ship") or arg_37_2:Find("Empty")

		if var_37_0 then
			updateShip(var_37_1, var_37_0)
			setActive(var_37_1:Find("EnergyWarn"), arg_34_0.contextData.mode == BossRushSeriesData.MODE.SINGLE and var_37_0:getEnergy() <= pg.gameset.series_enemy_mood_limit.key_value)
			setActive(var_37_1:Find("event_block"), var_37_0:getFlag("inEvent"))
		end

		setActive(var_37_1:Find("ship_type"), false)

		local var_37_2 = GetOrAddComponent(var_37_1, typeof(UILongPressTrigger))

		var_37_2.onLongPressed:RemoveAllListeners()

		if var_37_0 then
			var_37_2.onLongPressed:AddListener(function()
				arg_34_0:emit(BossRushFleetSelectMediator.ON_FLEET_SHIPINFO, {
					shipId = var_37_0.id,
					shipVOs = var_34_3
				})
			end)
		end

		local var_37_3 = GetOrAddComponent(var_37_1, "EventTriggerListener")

		var_37_3:RemovePointClickFunc()
		var_37_3:AddPointClickFunc(function(arg_39_0, arg_39_1)
			if arg_34_0.isDraging then
				return
			end

			arg_34_0:emit(BossRushFleetSelectMediator.ON_OPEN_DECK, {
				fleet = var_34_1,
				chapter = arg_34_0.chapter,
				shipVO = var_37_0,
				fleetIndex = arg_34_3,
				teamType = arg_34_2
			})
		end)
		var_37_3:RemoveBeginDragFunc()
		var_37_3:RemoveDragFunc()
		var_37_3:RemoveDragEndFunc()
	end)
end

function var_0_0.updateEliteFleets(arg_40_0)
	local var_40_0 = arg_40_0.contextData.seriesData
	local var_40_1 = arg_40_0.contextData.fleetIndex
	local var_40_2 = arg_40_0.contextData.fleets[var_40_1]
	local var_40_3 = var_40_1 == #arg_40_0.contextData.fleets

	setActive(arg_40_0._tf:Find("Panel/Fleet/Normal"), not var_40_3)
	setActive(arg_40_0._tf:Find("Panel/Fleet/Submarine"), var_40_3)

	local var_40_4 = #arg_40_0.contextData.fleets

	table.Foreach(arg_40_0.fleetIndexToggles, function(arg_41_0, arg_41_1)
		setActive(arg_41_1, arg_41_0 <= var_40_4 - 1 or arg_41_0 == #arg_40_0.fleetIndexToggles)
	end)

	local var_40_5 = arg_40_0.btnClear
	local var_40_6 = arg_40_0.btnRecommend
	local var_40_7 = arg_40_0.commanderList

	if not var_40_3 then
		local var_40_8 = arg_40_0.tfFleets[FleetType.Normal]

		setText(arg_40_0:findTF("bg/name", var_40_8), Fleet.DEFAULT_NAME[var_40_1])
		arg_40_0:initAddButton(var_40_8, TeamType.Main, var_40_1)
		arg_40_0:initAddButton(var_40_8, TeamType.Vanguard, var_40_1)
	else
		local var_40_9 = arg_40_0.tfFleets[FleetType.Submarine]
		local var_40_10 = #arg_40_0.contextData.fleets

		setText(arg_40_0:findTF("bg/name", var_40_9), Fleet.DEFAULT_NAME[Fleet.SUBMARINE_FLEET_ID])
		arg_40_0:initAddButton(var_40_9, TeamType.Submarine, var_40_10)
	end

	arg_40_0:initCommander(var_40_2, var_40_7)
	setText(arg_40_0.sonarRangeTexts[1], math.floor(var_40_2:GetFleetSonarRange()))

	local var_40_11 = #var_40_2:GetRawShipIds()
	local var_40_12 = var_40_11 == (var_40_3 and 3 or 6)

	onButton(arg_40_0, var_40_5, function()
		if var_40_11 == 0 then
			return
		end

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("battle_preCombatLayer_clear_confirm"),
			onYes = function()
				arg_40_0:emit(BossRushFleetSelectMediator.ON_ELITE_CLEAR, {
					index = var_40_1
				})
			end
		})
	end)
	onButton(arg_40_0, var_40_6, function()
		if var_40_12 then
			return
		end

		seriesAsync({
			function(arg_45_0)
				if var_40_11 == 0 then
					return arg_45_0()
				end

				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					content = i18n("battle_preCombatLayer_auto_confirm"),
					onYes = arg_45_0
				})
			end,
			function(arg_46_0)
				arg_40_0:emit(BossRushFleetSelectMediator.ON_ELITE_RECOMMEND, {
					index = var_40_1
				})
			end
		})
	end)

	local var_40_13 = var_40_0:GetOilLimit()

	setActive(arg_40_0.rtCostLimit, _.any(var_40_13, function(arg_47_0)
		return arg_47_0 > 0
	end))

	if #var_40_13 > 0 then
		local var_40_14 = var_40_3 and "formationScene_use_oil_limit_submarine" or "formationScene_use_oil_limit_surface"
		local var_40_15 = var_40_3 and var_40_13[2] or var_40_13[1]

		setText(arg_40_0.rtCostLimit:Find("Text"), string.format("%s(%d)", i18n(var_40_14), var_40_15))
	end

	local var_40_16 = (function(arg_48_0)
		if type(arg_48_0) ~= "table" then
			return {}
		end

		return arg_48_0
	end)(var_40_0:GetAdditionalAwards())

	setActive(arg_40_0.extraAwardTF, arg_40_0.contextData.mode == BossRushSeriesData.MODE.MULTIPLE and #var_40_16 > 0)

	local var_40_17 = var_40_0:GetExpeditionIds()
	local var_40_18 = arg_40_0._tf:Find("Panel/Info/Boss")

	UIItemList.StaticAlign(var_40_18, var_40_18:GetChild(0), #var_40_17, function(arg_49_0, arg_49_1, arg_49_2)
		if arg_49_0 ~= UIItemList.EventUpdate then
			return
		end

		local var_49_0 = arg_49_1 + 1 == var_40_1 or var_40_1 > #var_40_17 or arg_40_0.contextData.mode == BossRushSeriesData.MODE.SINGLE

		setActive(arg_49_2:Find("Select"), var_49_0)
		setActive(arg_49_2:Find("Image"), var_49_0)
	end)
end

function var_0_0.initCommander(arg_50_0, arg_50_1, arg_50_2)
	local var_50_0 = arg_50_1:GetRawCommanderIds()

	for iter_50_0 = 1, 2 do
		local var_50_1 = var_50_0[iter_50_0]
		local var_50_2

		if var_50_1 then
			var_50_2 = getProxy(CommanderProxy):getCommanderById(var_50_1)
		end

		local var_50_3 = arg_50_2:Find(iter_50_0)
		local var_50_4 = var_50_3:Find("add")
		local var_50_5 = var_50_3:Find("info")

		setActive(var_50_4, not var_50_2)
		setActive(var_50_5, var_50_2)

		if var_50_2 then
			local var_50_6 = Commander.rarity2Frame(var_50_2:getRarity())

			setImageSprite(var_50_5:Find("frame"), GetSpriteFromAtlas("weaponframes", "commander_" .. var_50_6))
			GetImageSpriteFromAtlasAsync("CommanderHrz/" .. var_50_2:getPainting(), "", var_50_5:Find("mask/icon"))
		end

		onButton(arg_50_0, var_50_4, function()
			arg_50_0:emit(BossRushFleetSelectMediator.OPEN_COMMANDER_PANEL, arg_50_1)
		end, SFX_PANEL)
		onButton(arg_50_0, var_50_5, function()
			arg_50_0:emit(BossRushFleetSelectMediator.OPEN_COMMANDER_PANEL, arg_50_1)
		end, SFX_PANEL)
	end
end

return var_0_0
