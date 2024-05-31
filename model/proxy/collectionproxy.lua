local var_0_0 = class("CollectionProxy", import(".NetProxy"))

var_0_0.AWARDS_UPDATE = "awards update"
var_0_0.GROUP_INFO_UPDATE = "group info update"
var_0_0.GROUP_EVALUATION_UPDATE = "group evaluation update"
var_0_0.TROPHY_UPDATE = "trophy update"
var_0_0.MAX_DAILY_EVA_COUNT = 1
var_0_0.KEY_17001_TIME_STAMP = "KEY_17001_TIME_STAMP"

function var_0_0.register(arg_1_0)
	arg_1_0.shipGroups = {}
	arg_1_0.awards = {}
	arg_1_0.trophy = {}
	arg_1_0.trophyGroup = {}
	arg_1_0.dailyEvaCount = 0

	arg_1_0:on(17001, function(arg_2_0)
		arg_1_0.shipGroups = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.ship_info_list) do
			arg_1_0.shipGroups[iter_2_1.id] = ShipGroup.New(iter_2_1)
		end

		for iter_2_2, iter_2_3 in ipairs(arg_2_0.transform_list) do
			if arg_1_0.shipGroups[iter_2_3] then
				arg_1_0.shipGroups[iter_2_3].trans = true
			end
		end

		arg_1_0.awards = {}

		for iter_2_4, iter_2_5 in ipairs(arg_2_0.ship_award_list) do
			table.sort(iter_2_5.award_index)

			arg_1_0.awards[iter_2_5.id] = iter_2_5.award_index[#iter_2_5.award_index]
		end

		for iter_2_6, iter_2_7 in ipairs(arg_2_0.progress_list) do
			arg_1_0.trophy[iter_2_7.id] = Trophy.New(iter_2_7)
		end

		arg_1_0:bindTrophyGroup()
		arg_1_0:bindComplexTrophy()
		arg_1_0:hiddenTrophyAutoClaim()
		arg_1_0:updateTrophy()
	end)
	arg_1_0:on(17002, function(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(arg_3_0.progress_list) do
			local var_3_0 = false
			local var_3_1 = iter_3_1.id

			if arg_1_0.trophy[var_3_1] then
				local var_3_2 = arg_1_0.trophy[var_3_1]
				local var_3_3 = var_3_2:canClaimed()

				var_3_2:update(iter_3_1)

				local var_3_4 = var_3_2:canClaimed()

				if not var_3_2:isHide() and var_3_3 ~= var_3_4 then
					var_3_0 = true
				end
			else
				arg_1_0.trophy[var_3_1] = Trophy.New(iter_3_1)

				if arg_1_0.trophy[var_3_1]:canClaimed() then
					var_3_0 = true
				end
			end

			if var_3_0 then
				arg_1_0:dispatchClaimRemind(var_3_1)
			end
		end

		arg_1_0:hiddenTrophyAutoClaim()
		arg_1_0:updateTrophy()
	end)
	arg_1_0:on(17004, function(arg_4_0)
		local var_4_0 = arg_4_0.ship_info

		arg_1_0.shipGroups[var_4_0.id] = ShipGroup.New(var_4_0)
	end)
end

function var_0_0.resetEvaCount(arg_5_0)
	for iter_5_0, iter_5_1 in pairs(arg_5_0.shipGroups) do
		local var_5_0 = iter_5_1.evaluation

		if var_5_0 then
			var_5_0.ievaCount = 0
		end
	end
end

function var_0_0.updateDailyEvaCount(arg_6_0, arg_6_1)
	arg_6_0.dailyEvaCount = arg_6_1
end

function var_0_0.updateAward(arg_7_0, arg_7_1, arg_7_2)
	arg_7_0.awards[arg_7_1] = arg_7_2

	arg_7_0:sendNotification(var_0_0.AWARDS_UPDATE, Clone(arg_7_0.awards))
end

function var_0_0.getShipGroup(arg_8_0, arg_8_1)
	return Clone(arg_8_0.shipGroups[arg_8_1])
end

function var_0_0.updateShipGroup(arg_9_0, arg_9_1)
	assert(arg_9_1, "update ship group: group cannot be nil.")

	arg_9_0.shipGroups[arg_9_1.id] = Clone(arg_9_1)
end

function var_0_0.getGroups(arg_10_0)
	return Clone(arg_10_0.shipGroups)
end

function var_0_0.RawgetGroups(arg_11_0)
	return arg_11_0.shipGroups
end

function var_0_0.getAwards(arg_12_0)
	return Clone(arg_12_0.awards)
end

function var_0_0.hasFinish(arg_13_0)
	local var_13_0 = pg.storeup_data_template

	for iter_13_0, iter_13_1 in ipairs(var_13_0.all) do
		if Favorite.New({
			id = iter_13_1
		}):canGetRes(arg_13_0.shipGroups, arg_13_0.awards) then
			return true
		end
	end

	return false
end

function var_0_0.getCollectionRate(arg_14_0)
	local var_14_0 = arg_14_0:getCollectionCount()
	local var_14_1 = arg_14_0:getCollectionTotal()

	return string.format("%0.3f", var_14_0 / var_14_1), var_14_0, var_14_1
end

function var_0_0.getCollectionCount(arg_15_0)
	return _.reduce(_.values(arg_15_0.shipGroups), 0, function(arg_16_0, arg_16_1)
		return arg_16_0 + (Nation.IsLinkType(arg_16_1:getNation()) and 0 or arg_16_1.trans and 2 or 1)
	end)
end

function var_0_0.getCollectionTotal(arg_17_0)
	return _.reduce(pg.ship_data_group.all, 0, function(arg_18_0, arg_18_1)
		local var_18_0 = pg.ship_data_group[arg_18_1].group_type
		local var_18_1 = ShipGroup.getDefaultShipConfig(var_18_0)

		return arg_18_0 + (Nation.IsLinkType(var_18_1.nationality) and 0 or 1)
	end) + #pg.ship_data_trans.all
end

function var_0_0.getLinkCollectionCount(arg_19_0)
	return _.reduce(_.values(arg_19_0.shipGroups), 0, function(arg_20_0, arg_20_1)
		return arg_20_0 + (Nation.IsLinkType(arg_20_1:getNation()) and 1 or 0)
	end)
end

function var_0_0.flushCollection(arg_21_0, arg_21_1)
	local var_21_0 = arg_21_0:getShipGroup(arg_21_1.groupId)
	local var_21_1

	if not var_21_0 then
		var_21_0 = ShipGroup.New({
			heart_count = 0,
			heart_flag = 0,
			lv_max = 1,
			id = arg_21_1.groupId,
			star = arg_21_1:getStar(),
			marry_flag = arg_21_1.propose and 1 or 0,
			intimacy_max = arg_21_1.intimacy
		})

		if OPEN_TEC_TREE_SYSTEM and table.indexof(pg.fleet_tech_ship_template.all, arg_21_1.groupId, 1) then
			var_21_1 = true
		end
	else
		if OPEN_TEC_TREE_SYSTEM and table.indexof(pg.fleet_tech_ship_template.all, arg_21_1.groupId, 1) then
			if var_21_0.star < arg_21_1:getStar() and arg_21_1:getStar() == pg.fleet_tech_ship_template[arg_21_1.groupId].max_star then
				var_21_1 = true

				local var_21_2 = pg.fleet_tech_ship_template[arg_21_1.groupId].pt_upgrage

				pg.ToastMgr.GetInstance():ShowToast(pg.ToastMgr.TYPE_TECPOINT, {
					point = var_21_2
				})
			end

			if var_21_0.maxLV < arg_21_1.level and arg_21_1.level == TechnologyConst.SHIP_LEVEL_FOR_BUFF then
				var_21_1 = true

				local var_21_3 = pg.fleet_tech_ship_template[arg_21_1.groupId].pt_level
				local var_21_4 = ShipType.FilterOverQuZhuType(pg.fleet_tech_ship_template[arg_21_1.groupId].add_level_shiptype)
				local var_21_5 = pg.fleet_tech_ship_template[arg_21_1.groupId].add_level_attr
				local var_21_6 = pg.fleet_tech_ship_template[arg_21_1.groupId].add_level_value

				pg.ToastMgr.GetInstance():ShowToast(pg.ToastMgr.TYPE_TECPOINT, {
					point = var_21_3,
					typeList = var_21_4,
					attr = var_21_5,
					value = var_21_6
				})
			end
		end

		var_21_0.star = math.max(var_21_0.star, arg_21_1:getStar())
		var_21_0.maxIntimacy = math.max(var_21_0.maxIntimacy, arg_21_1.intimacy)
		var_21_0.married = math.max(var_21_0.married, arg_21_1.propose and 1 or 0)
		var_21_0.maxLV = math.max(var_21_0.maxLV, arg_21_1.level)
	end

	arg_21_0:updateShipGroup(var_21_0)

	if var_21_1 then
		getProxy(TechnologyNationProxy):flushData()
	end
end

function var_0_0.updateTrophyClaim(arg_22_0, arg_22_1, arg_22_2)
	arg_22_0.trophy[arg_22_1]:updateTimeStamp(arg_22_2)
end

function var_0_0.unlockNewTrophy(arg_23_0, arg_23_1)
	for iter_23_0, iter_23_1 in ipairs(arg_23_1) do
		arg_23_0.trophy[iter_23_1.id] = iter_23_1
	end

	arg_23_0:bindTrophyGroup()
	arg_23_0:bindComplexTrophy()
	arg_23_0:hiddenTrophyAutoClaim()
end

function var_0_0.getTrophyGroup(arg_24_0)
	return Clone(arg_24_0.trophyGroup)
end

function var_0_0.getTrophys(arg_25_0)
	local var_25_0 = Clone(arg_25_0.trophy)

	for iter_25_0, iter_25_1 in pairs(arg_25_0.trophy) do
		iter_25_1:clearNew()
	end

	return var_25_0
end

function var_0_0.hiddenTrophyAutoClaim(arg_26_0)
	for iter_26_0, iter_26_1 in pairs(arg_26_0.trophy) do
		if iter_26_1:getHideType() ~= Trophy.ALWAYS_SHOW and iter_26_1:getHideType() ~= Trophy.COMING_SOON and iter_26_1:canClaimed() and not iter_26_1:isClaimed() then
			arg_26_0:sendNotification(GAME.TROPHY_CLAIM, {
				trophyID = iter_26_0
			})
		end
	end
end

function var_0_0.unclaimTrophyCount(arg_27_0)
	local var_27_0 = 0

	for iter_27_0, iter_27_1 in pairs(arg_27_0.trophy) do
		if iter_27_1:getHideType() == Trophy.ALWAYS_SHOW and iter_27_1:canClaimed() and not iter_27_1:isClaimed() then
			var_27_0 = var_27_0 + 1
		end
	end

	return var_27_0
end

function var_0_0.updateTrophy(arg_28_0)
	arg_28_0:sendNotification(var_0_0.TROPHY_UPDATE, Clone(arg_28_0.trophy))
end

function var_0_0.dispatchClaimRemind(arg_29_0, arg_29_1)
	pg.ToastMgr.GetInstance():ShowToast(pg.ToastMgr.TYPE_TROPHY, {
		id = arg_29_1
	})
end

function var_0_0.bindComplexTrophy(arg_30_0)
	for iter_30_0, iter_30_1 in pairs(arg_30_0.trophyGroup) do
		local var_30_0 = iter_30_1:getTrophyList()

		for iter_30_2, iter_30_3 in pairs(var_30_0) do
			if iter_30_3:isComplexTrophy() then
				for iter_30_4, iter_30_5 in ipairs(iter_30_3:getTargetID()) do
					local var_30_1 = arg_30_0.trophy[iter_30_5] or Trophy.generateDummyTrophy(iter_30_5)

					iter_30_3:bindTrophys(var_30_1)
				end
			end
		end
	end
end

function var_0_0.bindTrophyGroup(arg_31_0)
	local var_31_0 = pg.medal_template

	for iter_31_0, iter_31_1 in ipairs(var_31_0.all) do
		if var_31_0[iter_31_1].hide == Trophy.ALWAYS_SHOW then
			local var_31_1 = math.floor(iter_31_1 / 10)

			if not arg_31_0.trophyGroup[var_31_1] then
				arg_31_0.trophyGroup[var_31_1] = TrophyGroup.New(var_31_1)
			end

			local var_31_2 = arg_31_0.trophyGroup[var_31_1]

			if arg_31_0.trophy[iter_31_1] then
				var_31_2:addTrophy(arg_31_0.trophy[iter_31_1])
			else
				var_31_2:addDummyTrophy(iter_31_1)
			end
		end
	end

	for iter_31_2, iter_31_3 in pairs(arg_31_0.trophyGroup) do
		iter_31_3:sortGroup()
	end

	table.sort(arg_31_0.trophyGroup, function(arg_32_0, arg_32_1)
		return arg_32_0:getGroupID() < arg_32_1:getGroupID()
	end)
end

return var_0_0
