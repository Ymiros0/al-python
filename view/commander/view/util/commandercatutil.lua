local var_0_0 = class("CommanderCatUtil")

local function var_0_1(arg_1_0, arg_1_1)
	local var_1_0 = getProxy(FleetProxy):GetRegularFleets()

	for iter_1_0, iter_1_1 in pairs(var_1_0) do
		for iter_1_2, iter_1_3 in pairs(iter_1_1:getCommanders()) do
			local var_1_1 = iter_1_1.id % 10

			arg_1_1[iter_1_3.id].sub = iter_1_1:isSubmarineFleet()
			arg_1_1[iter_1_3.id].fleetId = var_1_1
			arg_1_1[iter_1_3.id].inFleet = true
		end
	end
end

local function var_0_2(arg_2_0, arg_2_1)
	local var_2_0 = getProxy(FleetProxy)
	local var_2_1 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

	assert(var_2_1 and not var_2_1:isEnd())

	local var_2_2 = var_2_0:getActivityFleets()[var_2_1.id]

	for iter_2_0, iter_2_1 in pairs(var_2_2) do
		local var_2_3 = iter_2_1:isSubmarineFleet()
		local var_2_4 = iter_2_1.id % 10

		for iter_2_2, iter_2_3 in pairs(iter_2_1:getCommanders()) do
			arg_2_1[iter_2_3.id].sub = var_2_3
			arg_2_1[iter_2_3.id].fleetId = var_2_4
			arg_2_1[iter_2_3.id].inFleet = true
		end
	end
end

local function var_0_3(arg_3_0, arg_3_1)
	assert(arg_3_0.chapterId)

	local var_3_0 = getProxy(ChapterProxy):getChapterById(arg_3_0.chapterId)

	for iter_3_0, iter_3_1 in pairs(var_3_0:getEliteFleetCommanders()) do
		for iter_3_2, iter_3_3 in pairs(iter_3_1) do
			arg_3_1[iter_3_3].sub = false
			arg_3_1[iter_3_3].fleetId = iter_3_0
			arg_3_1[iter_3_3].inFleet = true
		end
	end
end

local function var_0_4(arg_4_0, arg_4_1)
	local var_4_0 = getProxy(FleetProxy)
	local var_4_1 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_CHALLENGE)

	assert(var_4_1 and not var_4_1:isEnd())

	local var_4_2 = var_4_0:getActivityFleets()[var_4_1.id]

	for iter_4_0, iter_4_1 in pairs(var_4_2) do
		local var_4_3 = iter_4_1:isSubmarineFleet()
		local var_4_4 = iter_4_1.id % 10

		for iter_4_2, iter_4_3 in pairs(iter_4_1:getCommanders()) do
			arg_4_1[iter_4_3.id].sub = var_4_3
			arg_4_1[iter_4_3.id].fleetId = var_4_4
			arg_4_1[iter_4_3.id].inFleet = true
		end
	end
end

local function var_0_5(arg_5_0, arg_5_1)
	local var_5_0 = getProxy(GuildProxy):getRawData():GetActiveEvent()

	assert(var_5_0)

	local var_5_1 = var_5_0:GetBossMission():GetFleets()

	for iter_5_0, iter_5_1 in pairs(var_5_1) do
		local var_5_2 = arg_5_0.fleets[iter_5_0] or iter_5_1
		local var_5_3 = not var_5_2:IsMainFleet()

		for iter_5_2, iter_5_3 in pairs(var_5_2:getCommanders()) do
			arg_5_1[iter_5_3.id].sub = var_5_3
			arg_5_1[iter_5_3.id].fleetId = 1
			arg_5_1[iter_5_3.id].inFleet = true
		end
	end
end

local function var_0_6(arg_6_0, arg_6_1)
	local var_6_0, var_6_1 = nowWorld():BuildFormationIds()

	if arg_6_0.fleets then
		var_6_1 = arg_6_0.fleets
	end

	for iter_6_0, iter_6_1 in pairs(var_6_1) do
		local var_6_2 = FleetType.Submarine == iter_6_0

		for iter_6_2, iter_6_3 in pairs(iter_6_1) do
			local var_6_3 = Fleet.New({
				ship_list = {},
				commanders = iter_6_3.commanders
			})

			for iter_6_4, iter_6_5 in pairs(var_6_3:getCommanders()) do
				arg_6_1[iter_6_5.id].sub = var_6_2
				arg_6_1[iter_6_5.id].fleetId = iter_6_2
				arg_6_1[iter_6_5.id].inFleet = true
			end
		end
	end
end

local function var_0_7(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_0.fleets

	assert(var_7_0)

	for iter_7_0, iter_7_1 in pairs(var_7_0) do
		local var_7_1 = iter_7_0 == #var_7_0

		for iter_7_2, iter_7_3 in pairs(iter_7_1:getCommanders()) do
			arg_7_1[iter_7_3.id].sub = var_7_1
			arg_7_1[iter_7_3.id].fleetId = iter_7_1.id
			arg_7_1[iter_7_3.id].inFleet = true
		end
	end
end

local function var_0_8(arg_8_0, arg_8_1)
	local var_8_0 = getProxy(FleetProxy)
	local var_8_1 = _.map({
		FleetProxy.CHALLENGE_FLEET_ID,
		FleetProxy.CHALLENGE_SUB_FLEET_ID
	}, function(arg_9_0)
		return var_8_0:getFleetById(arg_9_0)
	end)

	for iter_8_0, iter_8_1 in pairs(var_8_1) do
		local var_8_2 = iter_8_1:isSubmarineFleet()
		local var_8_3 = iter_8_1.id

		for iter_8_2, iter_8_3 in pairs(iter_8_1:getCommanders()) do
			arg_8_1[iter_8_3.id].sub = var_8_2
			arg_8_1[iter_8_3.id].fleetId = var_8_3
			arg_8_1[iter_8_3.id].inFleet = true
		end
	end
end

local function var_0_9(arg_10_0, arg_10_1)
	local var_10_0 = getProxy(FleetProxy)
	local var_10_1 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSSSINGLE)

	assert(var_10_1 and not var_10_1:isEnd())

	local var_10_2 = var_10_0:getActivityFleets()[var_10_1.id]

	for iter_10_0, iter_10_1 in pairs(var_10_2) do
		local var_10_3 = iter_10_1:isSubmarineFleet()
		local var_10_4 = iter_10_1.id % 10

		for iter_10_2, iter_10_3 in pairs(iter_10_1:getCommanders()) do
			arg_10_1[iter_10_3.id].sub = var_10_3
			arg_10_1[iter_10_3.id].fleetId = var_10_4
			arg_10_1[iter_10_3.id].inFleet = true
		end
	end
end

function var_0_0.GetCommanderList(arg_11_0)
	local var_11_0 = getProxy(CommanderProxy):getData()

	if CommanderCatScene.FLEET_TYPE_COMMON == arg_11_0.fleetType then
		var_0_1(arg_11_0, var_11_0)
	elseif CommanderCatScene.FLEET_TYPE_ACTBOSS == arg_11_0.fleetType then
		var_0_2(arg_11_0, var_11_0)
	elseif CommanderCatScene.FLEET_TYPE_HARD_CHAPTER == arg_11_0.fleetType then
		var_0_3(arg_11_0, var_11_0)
	elseif CommanderCatScene.FLEET_TYPE_CHALLENGE == arg_11_0.fleetType then
		var_0_4(arg_11_0, var_11_0)
	elseif CommanderCatScene.FLEET_TYPE_GUILDBOSS == arg_11_0.fleetType then
		var_0_5(arg_11_0, var_11_0)
	elseif CommanderCatScene.FLEET_TYPE_WORLD == arg_11_0.fleetType then
		var_0_6(arg_11_0, var_11_0)
	elseif CommanderCatScene.FLEET_TYPE_BOSSRUSH == arg_11_0.fleetType then
		var_0_7(arg_11_0, var_11_0)
	elseif CommanderCatScene.FLEET_TYPE_LIMIT_CHALLENGE == arg_11_0.fleetType then
		var_0_8(arg_11_0, var_11_0)
	elseif CommanderCatScene.FLEET_TYPE_BOSSSINGLE == arg_11_0.fleetType then
		var_0_9(arg_11_0, var_11_0)
	end

	local var_11_1 = getProxy(ChapterProxy):getActiveChapter()

	if var_11_1 then
		_.each(var_11_1.fleets, function(arg_12_0)
			local var_12_0 = arg_12_0:getCommanders()

			for iter_12_0, iter_12_1 in pairs(arg_12_0:getCommanders()) do
				var_11_0[iter_12_1.id].inBattle = true
			end
		end)
	end

	local var_11_2 = {}

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.ignoredIds or {}) do
		var_11_2[iter_11_1] = true
	end

	local var_11_3 = {}

	for iter_11_2, iter_11_3 in pairs(var_11_0) do
		if not var_11_2[iter_11_2] then
			table.insert(var_11_3, iter_11_3)
		end
	end

	return var_11_3
end

function var_0_0.GetSkillExpAndCommanderExp(arg_13_0, arg_13_1)
	local var_13_0 = 0
	local var_13_1 = 0
	local var_13_2 = getProxy(CommanderProxy)

	for iter_13_0, iter_13_1 in pairs(arg_13_1) do
		local var_13_3 = var_13_2:getCommanderById(iter_13_1)

		var_13_1 = var_13_1 + var_13_3:getDestoryedExp(arg_13_0.groupId)
		var_13_0 = var_13_0 + var_13_3:getDestoryedSkillExp(arg_13_0.groupId)
	end

	return math.floor(var_13_1), math.floor(var_13_0)
end

function var_0_0.AnySSRCommander(arg_14_0)
	local var_14_0 = getProxy(CommanderProxy)

	if _.any(arg_14_0, function(arg_15_0)
		return var_14_0:RawGetCommanderById(arg_15_0):getRarity() >= 5
	end) then
		return true
	end

	return false
end

function var_0_0.CalcCommanderConsume(arg_16_0)
	local var_16_0 = getProxy(CommanderProxy)
	local var_16_1 = 0

	for iter_16_0, iter_16_1 in ipairs(arg_16_0) do
		local var_16_2 = var_16_0:RawGetCommanderById(iter_16_1)

		assert(var_16_2, iter_16_1)

		var_16_1 = var_16_1 + var_16_2:getUpgradeConsume()
	end

	return math.floor(var_16_1)
end

function var_0_0.SetActive(arg_17_0, arg_17_1)
	local var_17_0 = GetOrAddComponent(arg_17_0, typeof(CanvasGroup))

	var_17_0.alpha = arg_17_1 and 1 or 0
	var_17_0.blocksRaycasts = arg_17_1
end

function var_0_0.CommanderInChapter(arg_18_0)
	local var_18_0 = getProxy(ChapterProxy):getActiveChapter()

	if var_18_0 then
		local var_18_1 = var_18_0.fleets

		for iter_18_0, iter_18_1 in pairs(var_18_1) do
			local var_18_2 = iter_18_1:getCommanders()

			if _.any(_.values(var_18_2), function(arg_19_0)
				return arg_19_0.id == arg_18_0.id
			end) then
				return true
			end
		end
	end

	return false
end

function var_0_0.GetAllTalentNames()
	local var_20_0 = {}

	for iter_20_0, iter_20_1 in ipairs(pg.commander_ability_group.all) do
		local var_20_1 = pg.commander_ability_group[iter_20_1]

		if var_20_1.ability_list and #var_20_1.ability_list > 0 then
			local var_20_2 = var_20_1.ability_list[1]
			local var_20_3 = pg.commander_ability_template[var_20_2].name

			table.insert(var_20_0, {
				id = var_20_1.id,
				name = var_20_3
			})
		end
	end

	return var_20_0
end

function var_0_0.ShortenString(arg_21_0, arg_21_1)
	local function var_21_0(arg_22_0)
		if not arg_22_0 then
			return 0, 1
		elseif arg_22_0 > 240 then
			return 4, 1
		elseif arg_22_0 > 225 then
			return 3, 1
		elseif arg_22_0 > 192 then
			return 2, 1
		elseif arg_22_0 < 126 then
			return 1, 0.75
		else
			return 1, 1
		end
	end

	local var_21_1 = 1
	local var_21_2 = 0
	local var_21_3 = 0
	local var_21_4 = #arg_21_0
	local var_21_5 = false

	while var_21_1 <= var_21_4 do
		local var_21_6 = string.byte(arg_21_0, var_21_1)
		local var_21_7, var_21_8 = var_21_0(var_21_6)

		var_21_1 = var_21_1 + var_21_7
		var_21_2 = var_21_2 + var_21_8

		local var_21_9 = math.ceil(var_21_2)

		if var_21_9 == arg_21_1 - 1 then
			var_21_3 = var_21_1
		elseif arg_21_1 < var_21_9 then
			var_21_5 = true

			break
		end
	end

	if var_21_3 == 0 or var_21_4 < var_21_3 or not var_21_5 then
		return arg_21_0
	end

	return string.sub(arg_21_0, 1, var_21_3 - 1) .. ".."
end

return var_0_0
