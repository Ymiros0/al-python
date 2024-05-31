﻿local var_0_0 = class("NewBattleResultDataExtender")

function var_0_0.NeedCloseCamera(arg_1_0)
	return arg_1_0 ~= SYSTEM_BOSS_RUSH and arg_1_0 ~= SYSTEM_BOSS_RUSH_EX and arg_1_0 ~= SYSTEM_ACT_BOSS and arg_1_0 ~= SYSTEM_WORLD_BOSS and arg_1_0 ~= SYSTEM_BOSS_SINGLE
end

function var_0_0.NeedVibrate(arg_2_0)
	local var_2_0 = PlayerPrefs.GetInt(AUTO_BATTLE_LABEL, 0) > 0

	return ys.Battle.BattleState.IsAutoBotActive() and var_2_0 and not arg_2_0
end

function var_0_0.NeedHelpMessage(arg_3_0, arg_3_1)
	if (arg_3_0 == SYSTEM_SCENARIO or arg_3_0 == SYSTEM_ROUTINE or arg_3_0 == SYSTEM_SUB_ROUTINE or arg_3_0 == SYSTEM_DUEL) and arg_3_1 <= 0 then
		return true
	end

	return false
end

function var_0_0.GetAutoSkipFlag(arg_4_0, arg_4_1)
	if arg_4_1 == SYSTEM_SCENARIO then
		local var_4_0 = getProxy(ChapterProxy):getActiveChapter()

		return getProxy(ChapterProxy):GetChapterAutoFlag(var_4_0.id) == 1
	elseif arg_4_1 == SYSTEM_WORLD then
		return nowWorld().isAutoFight
	end

	return arg_4_0.autoSkipFlag or false
end

function var_0_0.GetExpBuffs(arg_5_0)
	local var_5_0

	if arg_5_0 == SYSTEM_SCENARIO or arg_5_0 == SYSTEM_ROUTINE or arg_5_0 == SYSTEM_ACT_BOSS or arg_5_0 == SYSTEM_HP_SHARE_ACT_BOSS or arg_5_0 == SYSTEM_SUB_ROUTINE or arg_5_0 == SYSTEM_WORLD or arg_5_0 == SYSTEM_BOSS_SINGLE then
		var_5_0 = _.detect(BuffHelper.GetBuffsByActivityType(ActivityConst.ACTIVITY_TYPE_BUFF), function(arg_6_0)
			return arg_6_0:getConfig("benefit_type") == "rookie_battle_exp"
		end)
	end

	return var_5_0
end

function var_0_0.GetShipBuffs(arg_7_0)
	local var_7_0

	if arg_7_0 == SYSTEM_SCENARIO or arg_7_0 == SYSTEM_ROUTINE or arg_7_0 == SYSTEM_ACT_BOSS or arg_7_0 == SYSTEM_HP_SHARE_ACT_BOSS or arg_7_0 == SYSTEM_SUB_ROUTINE or arg_7_0 == SYSTEM_WORLD or arg_7_0 == SYSTEM_BOSS_SINGLE then
		var_7_0 = getProxy(ActivityProxy):getBuffShipList()
	end

	return var_7_0
end

local function var_0_1()
	local var_8_0 = {}
	local var_8_1 = getProxy(ChapterProxy):getActiveChapter()
	local var_8_2 = var_8_1.fleet
	local var_8_3 = var_8_2[TeamType.Main]
	local var_8_4 = var_8_2[TeamType.Vanguard]

	for iter_8_0, iter_8_1 in ipairs(var_8_3) do
		table.insert(var_8_0, iter_8_1)
	end

	for iter_8_2, iter_8_3 in ipairs(var_8_4) do
		table.insert(var_8_0, iter_8_3)
	end

	local var_8_5 = _.detect(var_8_1.fleets, function(arg_9_0)
		return arg_9_0:getFleetType() == FleetType.Submarine
	end)

	if var_8_5 then
		local var_8_6 = var_8_5:getShipsByTeam(TeamType.Submarine, true)

		for iter_8_4, iter_8_5 in ipairs(var_8_6) do
			table.insert(var_8_0, iter_8_5)
		end
	end

	return var_8_0
end

local function var_0_2()
	local var_10_0 = {}
	local var_10_1 = nowWorld():GetActiveMap()
	local var_10_2 = var_10_1:GetFleet()
	local var_10_3 = var_10_2:GetTeamShipVOs(TeamType.Main, true)
	local var_10_4 = var_10_2:GetTeamShipVOs(TeamType.Vanguard, true)

	for iter_10_0, iter_10_1 in ipairs(var_10_3) do
		table.insert(var_10_0, iter_10_1)
	end

	for iter_10_2, iter_10_3 in ipairs(var_10_4) do
		table.insert(var_10_0, iter_10_3)
	end

	local var_10_5 = var_10_1:GetSubmarineFleet()

	if var_10_5 then
		local var_10_6 = var_10_5:GetTeamShipVOs(TeamType.Submarine, true)

		for iter_10_4, iter_10_5 in ipairs(var_10_6) do
			table.insert(var_10_0, iter_10_5)
		end
	end

	return var_10_0
end

local function var_0_3(arg_11_0)
	local var_11_0 = nowWorld():GetBossProxy():GetFleet(arg_11_0.bossId)

	return (getProxy(BayProxy):getShipsByFleet(var_11_0))
end

local function var_0_4(arg_12_0)
	local var_12_0 = getProxy(FleetProxy):getActivityFleets()[arg_12_0.actId]
	local var_12_1 = var_12_0[arg_12_0.mainFleetId]
	local var_12_2 = getProxy(BayProxy):getShipsByFleet(var_12_1)
	local var_12_3 = var_12_0[arg_12_0.mainFleetId + 10]
	local var_12_4 = getProxy(BayProxy):getShipsByFleet(var_12_3)

	for iter_12_0, iter_12_1 in ipairs(var_12_4) do
		table.insert(var_12_2, iter_12_1)
	end

	return var_12_2
end

local function var_0_5()
	local var_13_0 = {}
	local var_13_1 = getProxy(GuildProxy):getRawData():GetActiveEvent():GetBossMission()
	local var_13_2 = var_13_1:GetMainFleet()

	for iter_13_0, iter_13_1 in ipairs(var_13_2:GetShips()) do
		table.insert(var_13_0, iter_13_1.ship)
	end

	local var_13_3 = var_13_1:GetSubFleet()

	for iter_13_2, iter_13_3 in ipairs(var_13_3:GetShips()) do
		table.insert(var_13_0, iter_13_3.ship)
	end

	return var_13_0
end

local function var_0_6(arg_14_0)
	local var_14_0 = arg_14_0.actId
	local var_14_1 = getProxy(ActivityProxy):getActivityById(var_14_0):GetSeriesData()

	assert(var_14_1)

	local var_14_2 = var_14_1:GetStaegLevel()
	local var_14_3 = var_14_1:GetFleetIds()
	local var_14_4 = var_14_3[var_14_2]

	if var_14_1:GetMode() == BossRushSeriesData.MODE.SINGLE then
		var_14_4 = var_14_3[1]
	end

	local var_14_5 = getProxy(FleetProxy):getActivityFleets()[var_14_0][var_14_4]

	return (getProxy(BayProxy):getShipsByFleet(var_14_5))
end

local function var_0_7(arg_15_0)
	local var_15_0 = {}
	local var_15_1 = getProxy(FleetProxy):getFleetById(FleetProxy.CHALLENGE_FLEET_ID)

	table.insertto(var_15_0, getProxy(BayProxy):getShipsByFleet(var_15_1))

	local var_15_2 = getProxy(FleetProxy):getFleetById(FleetProxy.CHALLENGE_SUB_FLEET_ID)

	table.insertto(var_15_0, getProxy(BayProxy):getShipsByFleet(var_15_2))

	return var_15_0
end

local function var_0_8(arg_16_0)
	local var_16_0 = arg_16_0.mainFleetId
	local var_16_1 = getProxy(FleetProxy):getFleetById(var_16_0)

	return (getProxy(BayProxy):getShipsByFleet(var_16_1))
end

function var_0_0.GetNewMainShips(arg_17_0)
	local var_17_0 = arg_17_0.system
	local var_17_1 = {}

	if var_17_0 == SYSTEM_SCENARIO then
		var_17_1 = var_0_1()
	elseif var_17_0 == SYSTEM_WORLD then
		var_17_1 = var_0_2()
	elseif var_17_0 == SYSTEM_WORLD_BOSS then
		var_17_1 = var_0_3(arg_17_0)
	elseif var_17_0 == SYSTEM_HP_SHARE_ACT_BOSS or var_17_0 == SYSTEM_ACT_BOSS or var_17_0 == SYSTEM_ACT_BOSS_SP or var_17_0 == SYSTEM_BOSS_EXPERIMENT or var_17_0 == SYSTEM_BOSS_SINGLE then
		var_17_1 = var_0_4(arg_17_0)
	elseif var_17_0 == SYSTEM_GUILD then
		var_17_1 = var_0_5()
	elseif var_17_0 == SYSTEM_BOSS_RUSH or var_17_0 == SYSTEM_BOSS_RUSH_EX then
		var_17_1 = var_0_6(arg_17_0)
	elseif var_17_0 == SYSTEM_DODGEM or var_17_0 == SYSTEM_SUBMARINE_RUN or var_17_0 == SYSTEM_REWARD_PERFORM or var_17_0 == SYSTEM_AIRFIGHT or var_17_0 == SYSTEM_CARDPUZZLE or var_17_0 == SYSTEM_CHALLENGE then
		-- block empty
	elseif var_17_0 == SYSTEM_LIMIT_CHALLENGE then
		var_17_1 = var_0_7(arg_17_0)
	else
		var_17_1 = var_0_8(arg_17_0)
	end

	local var_17_2 = {}

	for iter_17_0, iter_17_1 in ipairs(var_17_1) do
		var_17_2[iter_17_1.id] = iter_17_1
	end

	return var_17_2
end

return var_0_0
