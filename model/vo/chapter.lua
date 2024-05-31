local var_0_0 = class("Chapter", import(".BaseVO"))

var_0_0.SelectFleet = 1
var_0_0.CustomFleet = 2
var_0_0.CHAPTER_STATE = {
	i18n("level_chapter_state_high_risk"),
	i18n("level_chapter_state_risk"),
	i18n("level_chapter_state_low_risk"),
	i18n("level_chapter_state_safety")
}

function var_0_0.bindConfigTable(arg_1_0)
	return pg.chapter_template
end

function var_0_0.Ctor(arg_2_0, arg_2_1)
	arg_2_0.configId = arg_2_1.id
	arg_2_0.id = arg_2_0.configId
	arg_2_0.active = false
	arg_2_0.progress = defaultValue(arg_2_1.progress, 0)
	arg_2_0.defeatCount = arg_2_1.defeat_count or 0
	arg_2_0.passCount = arg_2_1.pass_count or 0
	arg_2_0.todayDefeatCount = arg_2_1.today_defeat_count or 0

	local var_2_0 = {
		defaultValue(arg_2_1.kill_boss_count, 0),
		defaultValue(arg_2_1.kill_enemy_count, 0),
		defaultValue(arg_2_1.take_box_count, 0)
	}

	arg_2_0.achieves = {}

	for iter_2_0 = 1, 3 do
		local var_2_1 = arg_2_0:getConfig("star_require_" .. iter_2_0)

		if var_2_1 > 0 then
			table.insert(arg_2_0.achieves, {
				type = var_2_1,
				config = arg_2_0:getConfig("num_" .. iter_2_0),
				count = var_2_0[iter_2_0]
			})
		end
	end

	arg_2_0.dropShipIdList = {}
	arg_2_0.eliteFleetList = {
		{},
		{},
		{}
	}
	arg_2_0.eliteCommanderList = {
		{},
		{},
		{}
	}
	arg_2_0.supportFleet = {}
	arg_2_0.loopFlag = 0
end

function var_0_0.BuildEliteFleetList(arg_3_0)
	local var_3_0 = {
		{},
		{},
		{}
	}
	local var_3_1 = {
		{},
		{},
		{}
	}
	local var_3_2 = {
		{}
	}

	for iter_3_0, iter_3_1 in ipairs(arg_3_0 or {}) do
		local var_3_3 = {}

		for iter_3_2, iter_3_3 in ipairs(iter_3_1.main_id) do
			var_3_3[#var_3_3 + 1] = iter_3_3
		end

		if iter_3_0 == 4 then
			var_3_2[1] = var_3_3
		else
			var_3_0[iter_3_0] = var_3_3
		end

		local var_3_4 = {}

		for iter_3_4, iter_3_5 in ipairs(iter_3_1.commanders) do
			local var_3_5 = iter_3_5.id
			local var_3_6 = iter_3_5.pos

			if getProxy(CommanderProxy):getCommanderById(var_3_5) and Commander.canEquipToFleetList(var_3_1, iter_3_0, var_3_6, var_3_5) then
				var_3_4[var_3_6] = var_3_5
			end
		end

		var_3_1[iter_3_0] = var_3_4
	end

	return var_3_0, var_3_1, var_3_2
end

function var_0_0.getMaxCount(arg_4_0)
	local var_4_0 = arg_4_0:getConfig("risk_levels")

	if #var_4_0 == 0 then
		return 0
	end

	return var_4_0[1][1]
end

function var_0_0.hasMitigation(arg_5_0)
	if not LOCK_MITIGATION then
		return arg_5_0:getConfig("mitigation_level") > 0
	else
		return false
	end
end

function var_0_0.getRemainPassCount(arg_6_0)
	local var_6_0 = arg_6_0:getMaxCount()

	return math.max(var_6_0 - arg_6_0.passCount, 0)
end

function var_0_0.getRiskLevel(arg_7_0)
	local var_7_0 = arg_7_0:getRemainPassCount()
	local var_7_1 = arg_7_0:getConfig("risk_levels")

	for iter_7_0, iter_7_1 in ipairs(var_7_1) do
		if var_7_0 <= iter_7_1[1] and var_7_0 >= iter_7_1[2] then
			return iter_7_0
		end
	end

	assert(false, "index can not be nil")
end

function var_0_0.getMitigationRate(arg_8_0)
	local var_8_0 = arg_8_0:getMaxCount()
	local var_8_1 = LOCK_MITIGATION and 0 or arg_8_0:getConfig("mitigation_rate")

	return math.min(arg_8_0.passCount, var_8_0) * var_8_1
end

function var_0_0.getRepressInfo(arg_9_0)
	return {
		repressMax = arg_9_0:getMaxCount(),
		repressCount = arg_9_0.passCount,
		repressReduce = arg_9_0:getMitigationRate(),
		repressLevel = LOCK_MITIGATION and 0 or arg_9_0:getRemainPassCount() > 0 and 0 or arg_9_0:getConfig("mitigation_level") or 0,
		repressEnemyHpRant = 1 - arg_9_0:getStageCell(arg_9_0.fleet.line.row, arg_9_0.fleet.line.column).data / 10000
	}
end

function var_0_0.getChapterState(arg_10_0)
	local var_10_0 = arg_10_0:getRiskLevel()

	assert(var_0_0.CHAPTER_STATE[var_10_0], "state desc is nil")

	return var_0_0.CHAPTER_STATE[var_10_0]
end

function var_0_0.getPlayType(arg_11_0)
	return arg_11_0:getConfig("model")
end

function var_0_0.isTypeDefence(arg_12_0)
	return arg_12_0:getPlayType() == ChapterConst.TypeDefence
end

function var_0_0.IsSpChapter(arg_13_0)
	return getProxy(ChapterProxy):getMapById(arg_13_0:getConfig("map")):getMapType() == Map.ACT_EXTRA and arg_13_0:getPlayType() == ChapterConst.TypeRange
end

function var_0_0.getConfig(arg_14_0, arg_14_1)
	if arg_14_0:isLoop() then
		local var_14_0 = pg.chapter_template_loop[arg_14_0.id]

		assert(var_14_0, "chapter_template_loop not exist: " .. arg_14_0.id)

		if var_14_0[arg_14_1] ~= nil and var_14_0[arg_14_1] ~= "&&" then
			return var_14_0[arg_14_1]
		end

		if (arg_14_1 == "air_dominance" or arg_14_1 == "best_air_dominance") and var_14_0.air_dominance_loop_rate ~= nil then
			local var_14_1 = arg_14_0:getConfigTable()
			local var_14_2 = var_14_0.air_dominance_loop_rate * 0.01

			return math.floor(var_14_1[arg_14_1] * var_14_2)
		end
	end

	return var_0_0.super.getConfig(arg_14_0, arg_14_1)
end

function var_0_0.existLoop(arg_15_0)
	return pg.chapter_template_loop[arg_15_0.id] ~= nil
end

function var_0_0.canActivateLoop(arg_16_0)
	return arg_16_0.progress == 100
end

function var_0_0.isLoop(arg_17_0)
	return arg_17_0.loopFlag == 1
end

function var_0_0.existAmbush(arg_18_0)
	return arg_18_0:getConfig("is_ambush") == 1 or arg_18_0:getConfig("is_air_attack") == 1
end

function var_0_0.isUnlock(arg_19_0)
	return arg_19_0:IsCleanPrevChapter() and arg_19_0:IsCleanPrevStory()
end

function var_0_0.IsCleanPrevChapter(arg_20_0)
	local var_20_0 = arg_20_0:getConfig("pre_chapter")

	if var_20_0 == 0 then
		return true
	end

	return getProxy(ChapterProxy):GetChapterItemById(var_20_0):isClear()
end

function var_0_0.IsCleanPrevStory(arg_21_0)
	local var_21_0 = arg_21_0:getConfig("pre_story")

	if var_21_0 == 0 then
		return true
	end

	return getProxy(ChapterProxy):GetChapterItemById(var_21_0):isClear()
end

function var_0_0.isPlayerLVUnlock(arg_22_0)
	return getProxy(PlayerProxy):getRawData().level >= arg_22_0:getConfig("unlocklevel")
end

function var_0_0.isClear(arg_23_0)
	return arg_23_0.progress >= 100
end

function var_0_0.ifNeedHide(arg_24_0)
	if table.contains(pg.chapter_setting.all, arg_24_0.id) and pg.chapter_setting[arg_24_0.id].hide == 1 then
		return arg_24_0:isClear()
	end
end

function var_0_0.existAchieve(arg_25_0)
	return #arg_25_0.achieves > 0
end

function var_0_0.isAllAchieve(arg_26_0)
	return _.all(arg_26_0.achieves, function(arg_27_0)
		return ChapterConst.IsAchieved(arg_27_0)
	end)
end

function var_0_0.clearEliterFleetByIndex(arg_28_0, arg_28_1)
	if arg_28_1 > #arg_28_0.eliteFleetList then
		return
	end

	arg_28_0.eliteFleetList[arg_28_1] = {}
end

function var_0_0.wrapEliteFleet(arg_29_0, arg_29_1)
	local var_29_0 = {}
	local var_29_1 = arg_29_1 > 2 and FleetType.Submarine or FleetType.Normal
	local var_29_2 = _.flatten(arg_29_0:getEliteFleetList()[arg_29_1])

	for iter_29_0, iter_29_1 in pairs(arg_29_0:getEliteFleetCommanders()[arg_29_1]) do
		table.insert(var_29_0, {
			pos = iter_29_0,
			id = iter_29_1
		})
	end

	return TypedFleet.New({
		id = arg_29_1,
		fleetType = var_29_1,
		ship_list = var_29_2,
		commanders = var_29_0
	})
end

function var_0_0.setEliteCommanders(arg_30_0, arg_30_1)
	arg_30_0.eliteCommanderList = arg_30_1
end

function var_0_0.getEliteFleetCommanders(arg_31_0)
	return arg_31_0.eliteCommanderList
end

function var_0_0.updateCommander(arg_32_0, arg_32_1, arg_32_2, arg_32_3)
	arg_32_0.eliteCommanderList[arg_32_1][arg_32_2] = arg_32_3
end

function var_0_0.getEliteFleetList(arg_33_0)
	arg_33_0:EliteShipTypeFilter()

	return arg_33_0.eliteFleetList
end

function var_0_0.setEliteFleetList(arg_34_0, arg_34_1)
	arg_34_0.eliteFleetList = arg_34_1
end

function var_0_0.IsEliteFleetLegal(arg_35_0)
	local var_35_0 = 0
	local var_35_1 = 0
	local var_35_2 = 0
	local var_35_3 = 0
	local var_35_4
	local var_35_5

	for iter_35_0 = 1, #arg_35_0.eliteFleetList do
		local var_35_6, var_35_7 = arg_35_0:singleEliteFleetVertify(iter_35_0)

		if not var_35_6 then
			if not var_35_7 then
				if iter_35_0 >= 3 then
					var_35_2 = var_35_2 + 1
				else
					var_35_0 = var_35_0 + 1
				end
			else
				var_35_4 = var_35_7
				var_35_5 = iter_35_0
			end
		elseif iter_35_0 >= 3 then
			var_35_3 = var_35_3 + 1
		else
			var_35_1 = var_35_1 + 1
		end
	end

	if var_35_0 == 2 then
		return false, i18n("elite_disable_no_fleet")
	elseif var_35_1 == 0 then
		return false, var_35_4
	elseif var_35_2 + var_35_3 < arg_35_0:getConfig("submarine_num") then
		return false, var_35_4
	end

	local var_35_8 = arg_35_0:IsPropertyLimitationSatisfy()
	local var_35_9 = 1

	for iter_35_1, iter_35_2 in ipairs(var_35_8) do
		var_35_9 = var_35_9 * iter_35_2
	end

	if var_35_9 ~= 1 then
		return false, i18n("elite_disable_property_unsatisfied")
	end

	return true, var_35_5
end

function var_0_0.IsPropertyLimitationSatisfy(arg_36_0)
	local var_36_0 = getProxy(BayProxy):getRawData()
	local var_36_1 = arg_36_0:getConfig("property_limitation")
	local var_36_2 = {}

	for iter_36_0, iter_36_1 in ipairs(var_36_1) do
		var_36_2[iter_36_1[1]] = 0
	end

	local var_36_3 = arg_36_0:getEliteFleetList()
	local var_36_4 = 0

	for iter_36_2 = 1, 2 do
		if not arg_36_0:singleEliteFleetVertify(iter_36_2) then
			-- block empty
		else
			local var_36_5 = {}
			local var_36_6 = {}

			for iter_36_3, iter_36_4 in ipairs(var_36_1) do
				local var_36_7, var_36_8, var_36_9, var_36_10 = unpack(iter_36_4)

				if string.sub(var_36_7, 1, 5) == "fleet" then
					var_36_5[var_36_7] = 0
					var_36_6[var_36_7] = var_36_10
				end
			end

			local var_36_11 = var_36_3[iter_36_2]

			for iter_36_5, iter_36_6 in ipairs(var_36_11) do
				local var_36_12 = var_36_0[iter_36_6]

				var_36_4 = var_36_4 + 1

				local var_36_13 = intProperties(var_36_12:getProperties())

				for iter_36_7, iter_36_8 in pairs(var_36_2) do
					if string.sub(iter_36_7, 1, 5) == "fleet" then
						if iter_36_7 == "fleet_totle_level" then
							var_36_5[iter_36_7] = var_36_5[iter_36_7] + var_36_12.level
						end
					elseif iter_36_7 == "level" then
						var_36_2[iter_36_7] = iter_36_8 + var_36_12.level
					else
						var_36_2[iter_36_7] = iter_36_8 + var_36_13[iter_36_7]
					end
				end
			end

			for iter_36_9, iter_36_10 in pairs(var_36_5) do
				if iter_36_9 == "fleet_totle_level" and iter_36_10 > var_36_6[iter_36_9] then
					var_36_2[iter_36_9] = var_36_2[iter_36_9] + 1
				end
			end
		end
	end

	local var_36_14 = {}

	for iter_36_11, iter_36_12 in ipairs(var_36_1) do
		local var_36_15, var_36_16, var_36_17 = unpack(iter_36_12)

		if var_36_15 == "level" and var_36_4 > 0 then
			var_36_2[var_36_15] = math.ceil(var_36_2[var_36_15] / var_36_4)
		end

		var_36_14[iter_36_11] = AttributeType.EliteConditionCompare(var_36_16, var_36_2[var_36_15], var_36_17) and 1 or 0
	end

	return var_36_14, var_36_2
end

function var_0_0.GetNomralFleetMaxCount(arg_37_0)
	return arg_37_0:getConfig("group_num")
end

function var_0_0.GetSubmarineFleetMaxCount(arg_38_0)
	return arg_38_0:getConfig("submarine_num")
end

function var_0_0.GetSupportFleetMaxCount(arg_39_0)
	return arg_39_0:getConfig("support_group_num")
end

function var_0_0.EliteShipTypeFilter(arg_40_0)
	if arg_40_0:getConfig("type") == Chapter.SelectFleet then
		local var_40_0 = {
			1,
			2,
			3
		}

		for iter_40_0, iter_40_1 in ipairs(var_40_0) do
			table.clear(arg_40_0.eliteFleetList[iter_40_1])
			table.clear(arg_40_0.eliteCommanderList[iter_40_1])
		end
	else
		for iter_40_2 = arg_40_0:GetNomralFleetMaxCount() + 1, 2 do
			table.clear(arg_40_0.eliteFleetList[iter_40_2])
			table.clear(arg_40_0.eliteCommanderList[iter_40_2])
		end

		for iter_40_3 = arg_40_0:GetSubmarineFleetMaxCount() + 2 + 1, 3 do
			table.clear(arg_40_0.eliteFleetList[iter_40_3])
			table.clear(arg_40_0.eliteCommanderList[iter_40_3])
		end
	end

	local var_40_1 = getProxy(BayProxy):getRawData()

	for iter_40_4, iter_40_5 in ipairs(arg_40_0.eliteFleetList) do
		for iter_40_6 = #iter_40_5, 1, -1 do
			if var_40_1[iter_40_5[iter_40_6]] == nil then
				table.remove(iter_40_5, iter_40_6)
			end
		end
	end

	local function var_40_2(arg_41_0, arg_41_1, arg_41_2)
		arg_41_1 = Clone(arg_41_1)

		ChapterProxy.SortRecommendLimitation(arg_41_1)

		for iter_41_0, iter_41_1 in ipairs(arg_41_2) do
			local var_41_0
			local var_41_1 = var_40_1[iter_41_1]:getShipType()

			for iter_41_2, iter_41_3 in ipairs(arg_41_1) do
				if ShipType.ContainInLimitBundle(iter_41_3, var_41_1) then
					var_41_0 = iter_41_2

					break
				end
			end

			if var_41_0 then
				table.remove(arg_41_1, var_41_0)
			else
				table.removebyvalue(arg_41_0, iter_41_1)
			end
		end
	end

	for iter_40_7, iter_40_8 in ipairs(arg_40_0:getConfig("limitation")) do
		local var_40_3 = arg_40_0.eliteFleetList[iter_40_7]
		local var_40_4 = {}
		local var_40_5 = {}
		local var_40_6 = {}

		for iter_40_9, iter_40_10 in ipairs(var_40_3) do
			local var_40_7 = var_40_1[iter_40_10]:getTeamType()

			if var_40_7 == TeamType.Main then
				table.insert(var_40_4, iter_40_10)
			elseif var_40_7 == TeamType.Vanguard then
				table.insert(var_40_5, iter_40_10)
			elseif var_40_7 == TeamType.Submarine then
				table.insert(var_40_6, iter_40_10)
			end
		end

		var_40_2(var_40_3, iter_40_8[1], var_40_4)
		var_40_2(var_40_3, iter_40_8[2], var_40_5)
		var_40_2(var_40_3, {
			0,
			0,
			0
		}, var_40_6)
	end
end

function var_0_0.singleEliteFleetVertify(arg_42_0, arg_42_1)
	local var_42_0 = getProxy(BayProxy):getRawData()
	local var_42_1 = arg_42_0:getEliteFleetList()[arg_42_1]

	if not var_42_1 or #var_42_1 == 0 then
		return false
	end

	if arg_42_1 >= 3 then
		return true
	end

	if arg_42_0:getConfig("type") ~= Chapter.CustomFleet then
		return true
	end

	local var_42_2 = 0
	local var_42_3 = 0
	local var_42_4 = {}

	for iter_42_0, iter_42_1 in ipairs(var_42_1) do
		local var_42_5 = var_42_0[iter_42_1]

		if var_42_5 then
			if var_42_5:getFlag("inEvent") then
				return false, i18n("elite_disable_ship_escort")
			end

			local var_42_6 = var_42_5:getTeamType()

			if var_42_6 == TeamType.Main then
				var_42_2 = var_42_2 + 1
			elseif var_42_6 == TeamType.Vanguard then
				var_42_3 = var_42_3 + 1
			end

			var_42_4[#var_42_4 + 1] = var_42_5:getShipType()
		end
	end

	if var_42_2 * var_42_3 == 0 and var_42_2 + var_42_3 ~= 0 then
		return false
	end

	local var_42_7 = checkExist(arg_42_0:getConfig("limitation"), {
		arg_42_1
	})
	local var_42_8 = 1

	for iter_42_2, iter_42_3 in ipairs(var_42_7 or {}) do
		local var_42_9 = 0
		local var_42_10 = 0

		for iter_42_4, iter_42_5 in ipairs(iter_42_3) do
			if iter_42_5 ~= 0 then
				var_42_9 = var_42_9 + 1

				if underscore.any(var_42_4, function(arg_43_0)
					return ShipType.ContainInLimitBundle(iter_42_5, arg_43_0)
				end) then
					var_42_10 = 1

					break
				end
			end
		end

		if var_42_9 == 0 then
			var_42_10 = 1
		end

		var_42_8 = var_42_8 * var_42_10
	end

	if var_42_8 == 0 then
		return false, i18n("elite_disable_formation_unsatisfied")
	end

	return true
end

function var_0_0.ClearSupportFleetList(arg_44_0, arg_44_1)
	arg_44_0.supportFleet = {}
end

function var_0_0.setSupportFleetList(arg_45_0, arg_45_1)
	arg_45_0.supportFleet = arg_45_1[1]
end

function var_0_0.getSupportFleet(arg_46_0)
	arg_46_0:SupportShipTypeFilter()

	return arg_46_0.supportFleet
end

function var_0_0.SupportShipTypeFilter(arg_47_0)
	if arg_47_0:GetSupportFleetMaxCount() < 1 then
		table.clear(arg_47_0.supportFleet)
	end

	local var_47_0 = getProxy(BayProxy):getRawData()
	local var_47_1 = arg_47_0.supportFleet

	for iter_47_0 = #var_47_1, 1, -1 do
		if var_47_0[var_47_1[iter_47_0]] == nil then
			table.remove(var_47_1, iter_47_0)
		end
	end
end

function var_0_0.activeAlways(arg_48_0)
	if getProxy(ChapterProxy):getMapById(arg_48_0:getConfig("map")):isActivity() then
		local var_48_0 = arg_48_0:GetBindActID()
		local var_48_1 = pg.activity_template[var_48_0]

		if type(var_48_1.config_client) == "table" then
			local var_48_2 = var_48_1.config_client.prevs or {}

			return table.contains(var_48_2, arg_48_0.id)
		end
	end

	return false
end

function var_0_0.getPrevChapterName(arg_49_0)
	local var_49_0 = ""
	local var_49_1 = arg_49_0:getConfig("pre_chapter")

	if var_49_1 ~= 0 then
		var_49_0 = arg_49_0:bindConfigTable()[var_49_1].chapter_name
	end

	return var_49_0
end

function var_0_0.CanQuickPlay(arg_50_0)
	local var_50_0 = pg.chapter_setting[arg_50_0.id]

	return var_50_0 and var_50_0.expedite > 0
end

function var_0_0.GetQuickPlayFlag(arg_51_0)
	return PlayerPrefs.GetInt("chapter_quickPlay_flag_" .. arg_51_0.id, 0) == 1
end

function var_0_0.writeDrops(arg_52_0, arg_52_1)
	_.each(arg_52_1, function(arg_53_0)
		if arg_53_0.type == DROP_TYPE_SHIP and not table.contains(arg_52_0.dropShipIdList, arg_53_0.id) then
			table.insert(arg_52_0.dropShipIdList, arg_53_0.id)
		end
	end)
end

function var_0_0.UpdateDropShipList(arg_54_0, arg_54_1)
	for iter_54_0, iter_54_1 in ipairs(arg_54_1) do
		if not table.contains(arg_54_0.dropShipIdList, iter_54_1) then
			table.insert(arg_54_0.dropShipIdList, iter_54_1)
		end
	end
end

function var_0_0.GetDropShipList(arg_55_0)
	return arg_55_0.dropShipIdList
end

function var_0_0.getOniChapterInfo(arg_56_0)
	return pg.chapter_capture[arg_56_0.id]
end

function var_0_0.getBombChapterInfo(arg_57_0)
	return pg.chapter_boom[arg_57_0.id]
end

function var_0_0.getNpcShipByType(arg_58_0, arg_58_1)
	local var_58_0 = {}
	local var_58_1 = getProxy(TaskProxy)

	local function var_58_2(arg_59_0)
		if arg_59_0 == 0 then
			return true
		end

		local var_59_0 = var_58_1:getTaskVO(arg_59_0)

		return var_59_0 and not var_59_0:isFinish()
	end

	for iter_58_0, iter_58_1 in ipairs(arg_58_0:getConfig("npc_data")) do
		local var_58_3 = pg.npc_squad_template[iter_58_1]

		if not arg_58_1 or arg_58_1 == var_58_3.type and var_58_2(var_58_3.task_id) then
			for iter_58_2, iter_58_3 in ipairs({
				"vanguard_list",
				"main_list"
			}) do
				for iter_58_4, iter_58_5 in ipairs(var_58_3[iter_58_3]) do
					table.insert(var_58_0, NpcShip.New({
						id = iter_58_5[1],
						configId = iter_58_5[1],
						level = iter_58_5[2]
					}))
				end
			end
		end
	end

	return var_58_0
end

function var_0_0.getTodayDefeatCount(arg_60_0)
	return getProxy(DailyLevelProxy):getChapterDefeatCount(arg_60_0.configId)
end

function var_0_0.isTriesLimit(arg_61_0)
	local var_61_0 = arg_61_0:getConfig("count")

	return var_61_0 and var_61_0 > 0
end

function var_0_0.updateTodayDefeatCount(arg_62_0)
	getProxy(DailyLevelProxy):updateChapterDefeatCount(arg_62_0.configId)
end

function var_0_0.enoughTimes2Start(arg_63_0)
	if arg_63_0:isTriesLimit() then
		return arg_63_0:getTodayDefeatCount() < arg_63_0:getConfig("count")
	else
		return true
	end
end

function var_0_0.GetRestDailyBonus(arg_64_0)
	local var_64_0 = 0

	if arg_64_0:IsRemaster() then
		return var_64_0
	end

	local var_64_1 = arg_64_0:getConfig("boss_expedition_id")

	for iter_64_0, iter_64_1 in ipairs(var_64_1) do
		local var_64_2 = pg.expedition_activity_template[iter_64_1]

		var_64_0 = math.max(var_64_0, var_64_2 and var_64_2.bonus_time or 0)
	end

	local var_64_3 = pg.chapter_defense[arg_64_0.id]

	if var_64_3 then
		var_64_0 = math.max(var_64_0, var_64_3.bonus_time or 0)
	end

	return (math.max(var_64_0 - arg_64_0.todayDefeatCount, 0))
end

function var_0_0.GetDailyBonusQuota(arg_65_0)
	return arg_65_0:GetRestDailyBonus() > 0
end

var_0_0.OPERATION_BUFF_TYPE_COST = "more_oil"
var_0_0.OPERATION_BUFF_TYPE_REWARD = "extra_drop"
var_0_0.OPERATION_BUFF_TYPE_EXP = "chapter_up"
var_0_0.OPERATION_BUFF_TYPE_DESC = "desc"

function var_0_0.GetSPOperationItemCacheKey(arg_66_0)
	return "specialOPItem_" .. arg_66_0
end

function var_0_0.GetSpItems(arg_67_0)
	local var_67_0 = {}
	local var_67_1 = getProxy(BagProxy):getItemsByType(Item.SPECIAL_OPERATION_TICKET)
	local var_67_2 = arg_67_0:getConfig("special_operation_list")

	if var_67_2 and #var_67_2 == 0 then
		return var_67_0
	end

	for iter_67_0, iter_67_1 in ipairs(pg.benefit_buff_template.all) do
		local var_67_3 = pg.benefit_buff_template[iter_67_1]

		if var_67_3.benefit_type == Chapter.OPERATION_BUFF_TYPE_DESC and table.contains(var_67_2, var_67_3.id) then
			local var_67_4 = tonumber(var_67_3.benefit_condition)

			for iter_67_2, iter_67_3 in ipairs(var_67_1) do
				if var_67_4 == iter_67_3.configId then
					table.insert(var_67_0, iter_67_3)

					break
				end
			end
		end
	end

	return var_67_0
end

function var_0_0.GetSPBuffByItem(arg_68_0)
	for iter_68_0, iter_68_1 in ipairs(pg.benefit_buff_template.all) do
		buffConfig = pg.benefit_buff_template[iter_68_1]

		if buffConfig.benefit_type == Chapter.OPERATION_BUFF_TYPE_DESC and tonumber(buffConfig.benefit_condition) == arg_68_0 then
			return buffConfig.id
		end
	end
end

function var_0_0.GetActiveSPItemID(arg_69_0)
	local var_69_0 = Chapter.GetSPOperationItemCacheKey(arg_69_0.id)
	local var_69_1 = PlayerPrefs.GetInt(var_69_0, 0)

	if var_69_1 == 0 then
		return 0
	end

	if arg_69_0:GetRestDailyBonus() > 0 then
		return 0
	end

	local var_69_2 = arg_69_0:GetSpItems()

	if _.detect(var_69_2, function(arg_70_0)
		return arg_70_0:GetConfigID() == var_69_1
	end) then
		return var_69_1
	end

	return 0
end

function var_0_0.GetLimitOilCost(arg_71_0, arg_71_1, arg_71_2)
	if not arg_71_0:isLoop() then
		return 9999
	end

	local var_71_0
	local var_71_1

	if arg_71_1 then
		var_71_1 = 3
	else
		local var_71_2 = pg.expedition_data_template[arg_71_2]

		var_71_1 = (var_71_2.type == ChapterConst.ExpeditionTypeBoss or var_71_2.type == ChapterConst.ExpeditionTypeMulBoss) and 2 or 1
	end

	return arg_71_0:getConfig("use_oil_limit")[var_71_1] or 9999
end

function var_0_0.IsRemaster(arg_72_0)
	local var_72_0 = getProxy(ChapterProxy):getMapById(arg_72_0:getConfig("map"))

	return var_72_0 and var_72_0:isRemaster()
end

function var_0_0.GetBindActID(arg_73_0)
	return arg_73_0:getConfig("act_id")
end

function var_0_0.GetMaxBattleCount(arg_74_0)
	local var_74_0 = 0
	local var_74_1 = getProxy(ChapterProxy):getMapById(arg_74_0:getConfig("map"))

	if var_74_1:getMapType() == Map.ELITE then
		var_74_0 = pg.gameset.hard_level_multiple_sorties_times.key_value
		var_74_0 = math.clamp(var_74_0, 0, getProxy(DailyLevelProxy):GetRestEliteCount())
	elseif var_74_1:isRemaster() then
		var_74_0 = pg.gameset.archives_level_multiple_sorties_times.key_value
		var_74_0 = math.clamp(var_74_0, 0, getProxy(ChapterProxy).remasterTickets)
	elseif var_74_1:isActivity() then
		var_74_0 = pg.gameset.activity_level_multiple_sorties_times.key_value
	else
		var_74_0 = pg.gameset.main_level_multiple_sorties_times.key_value
	end

	if arg_74_0:isTriesLimit() then
		local var_74_2 = arg_74_0:getConfig("count") - arg_74_0:getTodayDefeatCount()

		var_74_0 = math.clamp(var_74_0, 0, var_74_2)
	end

	return var_74_0
end

return var_0_0
