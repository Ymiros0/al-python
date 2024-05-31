local var_0_0 = class("ActivityItemPool", import(".BaseVO"))
local var_0_1 = pg.activity_random_award_item

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.awards = arg_1_1.awards or {}
	arg_1_0.prevId = arg_1_1.prevId
	arg_1_0.index = arg_1_1.index
end

function var_0_0.bindConfigTable(arg_2_0)
	return pg.activity_random_award_template
end

function var_0_0.getComsume(arg_3_0)
	local var_3_0 = arg_3_0:getConfig("resource_category")
	local var_3_1 = arg_3_0:getConfig("resource_type")
	local var_3_2 = arg_3_0:getConfig("resource_num")

	return {
		type = var_3_0,
		id = var_3_1,
		count = var_3_2
	}
end

function var_0_0.enoughResForUsage(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0:getComsume()

	if var_4_0.type == DROP_TYPE_RESOURCE then
		if getProxy(PlayerProxy):getData():getResById(var_4_0.id) < var_4_0.count * arg_4_1 then
			return false
		end
	elseif var_4_0.type == DROP_TYPE_ITEM and getProxy(BagProxy):getItemCountById(var_4_0.id) < var_4_0.count * arg_4_1 then
		return false
	end

	return true
end

function var_0_0.getItemCount(arg_5_0)
	local var_5_0 = arg_5_0:getConfig("item_list")

	return _.reduce(var_5_0, 0, function(arg_6_0, arg_6_1)
		return arg_6_0 + arg_6_1[2]
	end)
end

function var_0_0.getleftItemCount(arg_7_0)
	return arg_7_0:getItemCount() - arg_7_0:getFetchCount()
end

function var_0_0.getFetchCount(arg_8_0)
	return _.reduce(_.values(arg_8_0.awards), 0, function(arg_9_0, arg_9_1)
		return arg_9_0 + arg_9_1
	end)
end

function var_0_0.getMainItems(arg_10_0)
	return arg_10_0:filterItems(true)
end

function var_0_0.filterItems(arg_11_0, arg_11_1)
	local var_11_0 = arg_11_0:getConfig("main_item")
	local var_11_1 = _.select(arg_11_0:getConfig("item_list"), function(arg_12_0)
		if arg_11_1 then
			return table.contains(var_11_0, arg_12_0[1])
		else
			return not table.contains(var_11_0, arg_12_0[1])
		end
	end)

	return (_.map(var_11_1, function(arg_13_0)
		local var_13_0 = var_0_1[arg_13_0[1]]
		local var_13_1 = arg_11_0.awards[arg_13_0[1]] or 0

		return {
			id = var_13_0.commodity_id,
			type = var_13_0.resource_category,
			count = var_13_0.num,
			surplus = arg_13_0[2] - var_13_1,
			total = arg_13_0[2]
		}
	end))
end

function var_0_0.getItems(arg_14_0)
	local var_14_0 = arg_14_0:filterItems(true)
	local var_14_1 = arg_14_0:filterItems(false)

	return var_14_0, var_14_1
end

function var_0_0.canOpenNext(arg_15_0)
	return _.all(arg_15_0:getMainItems(), function(arg_16_0)
		return arg_16_0.surplus == 0
	end)
end

function var_0_0.getTempleNewChar(arg_17_0, arg_17_1)
	if not arg_17_0.charAwardDisplayData then
		arg_17_0.charAwardDisplayData = {}

		for iter_17_0, iter_17_1 in ipairs(pg.guardian_template.all) do
			if pg.guardian_template[iter_17_1].guardian_gain_pool == arg_17_0.configId then
				local var_17_0 = arg_17_0:getCharLotteryCount(iter_17_1)

				table.insert(arg_17_0.charAwardDisplayData, {
					iter_17_1,
					var_17_0
				})
			end
		end
	end

	local var_17_1 = {}
	local var_17_2 = arg_17_0:getFetchCount()

	for iter_17_2 = arg_17_1 + 1, var_17_2 do
		for iter_17_3, iter_17_4 in ipairs(arg_17_0.charAwardDisplayData) do
			if iter_17_4[2] == iter_17_2 then
				table.insert(var_17_1, iter_17_4[1])
			end
		end
	end

	return var_17_1
end

var_0_0.guardian_type_lottery = 1
var_0_0.guardian_type_lock = 2

function var_0_0.getCharLotteryCount(arg_18_0, arg_18_1)
	local var_18_0 = pg.guardian_template[arg_18_1]

	if var_18_0.type == ActivityItemPool.guardian_type_lottery then
		return var_18_0.guardian_gain[2]
	elseif var_18_0.type == ActivityItemPool.guardian_type_lock then
		local var_18_1 = var_18_0.guardian_gain
		local var_18_2 = 0

		for iter_18_0, iter_18_1 in ipairs(var_18_1) do
			var_18_2 = math.max(var_18_2, arg_18_0:getCharLotteryCount(iter_18_1))
		end

		return var_18_2
	end

	return -1
end

function var_0_0.getGuardianGot(arg_19_0, arg_19_1)
	local var_19_0 = pg.guardian_template[arg_19_1]

	if var_19_0.guardian_gain_pool ~= arg_19_0.id then
		warning("guardian id " .. arg_19_1 .. "不属于该池子 " .. arg_19_0.id .. " 所属对象")

		return false, 0
	end

	if var_19_0.type == ActivityItemPool.guardian_type_lottery then
		return arg_19_0:getFetchCount() >= var_19_0.guardian_gain[2], math.max(var_19_0.guardian_gain[2] - arg_19_0:getFetchCount(), 0)
	elseif var_19_0.type == ActivityItemPool.guardian_type_lock then
		local var_19_1 = var_19_0.guardian_gain
		local var_19_2 = 0

		for iter_19_0, iter_19_1 in ipairs(var_19_1) do
			if not arg_19_0:getGuardianGot(iter_19_1) then
				var_19_2 = var_19_2 + 1
			end
		end

		return var_19_2 == 0, var_19_2
	end

	return false, 0
end

function var_0_0.GetAllGuardianIds(arg_20_0)
	local var_20_0 = pg.activity_template[arg_20_0]

	if not var_20_0 then
		return {}
	end

	if var_20_0.type ~= ActivityConst.ACTIVITY_TYPE_LOTTERY then
		return {}
	end

	local var_20_1 = {}
	local var_20_2 = pg.activity_template[arg_20_0].config_data

	for iter_20_0, iter_20_1 in ipairs(pg.guardian_template.all) do
		local var_20_3 = pg.guardian_template[iter_20_1]

		if table.contains(var_20_2, var_20_3.guardian_gain_pool) then
			local var_20_4 = var_20_3.id

			table.insert(var_20_1, var_20_4)
		end
	end

	return var_20_1
end

function var_0_0.GetAllGuardianIdsStatus(arg_21_0)
	local var_21_0 = pg.activity_template[arg_21_0]
	local var_21_1 = getProxy(ActivityProxy):getActivityById(arg_21_0)

	if not var_21_0 then
		return {}
	end

	if var_21_0.type ~= ActivityConst.ACTIVITY_TYPE_LOTTERY then
		return {}
	end

	if not var_21_1 then
		return
	end

	local var_21_2 = {}
	local var_21_3 = {}
	local var_21_4 = {}
	local var_21_5 = pg.activity_template[arg_21_0].config_data

	for iter_21_0, iter_21_1 in ipairs(var_21_5) do
		local var_21_6 = var_21_1:getAwardInfos()[iter_21_1]

		var_21_4[iter_21_1] = ActivityItemPool.CreateItemPool(iter_21_1, var_21_6, nil, iter_21_0)
	end

	for iter_21_2, iter_21_3 in ipairs(pg.guardian_template.all) do
		local var_21_7 = pg.guardian_template[iter_21_3]

		if table.contains(var_21_5, var_21_7.guardian_gain_pool) then
			local var_21_8 = var_21_7.id
			local var_21_9 = var_21_4[var_21_7.guardian_gain_pool]

			if var_21_9 then
				local var_21_10, var_21_11 = var_21_9:getGuardianGot(var_21_8)

				if var_21_10 then
					table.insert(var_21_2, var_21_8)
				else
					table.insert(var_21_3, {
						var_21_8,
						var_21_11
					})
				end
			end
		end
	end

	return var_21_2, var_21_3
end

function var_0_0.GetGuardianLastCount(arg_22_0, arg_22_1)
	local var_22_0 = pg.activity_template[arg_22_0]
	local var_22_1 = getProxy(ActivityProxy):getActivityById(arg_22_0)

	if not var_22_0 then
		return {}
	end

	if var_22_0.type ~= ActivityConst.ACTIVITY_TYPE_LOTTERY then
		return {}
	end

	if not var_22_1 then
		return
	end

	local var_22_2 = pg.guardian_template[arg_22_1].guardian_gain_pool
	local var_22_3 = var_22_1:getAwardInfos()[var_22_2]

	return ActivityItemPool.CreateItemPool(var_22_2, var_22_3, nil, 1):getGuardianGot(arg_22_1)
end

function var_0_0.CreateItemPool(arg_23_0, arg_23_1, arg_23_2, arg_23_3)
	return (ActivityItemPool.New({
		id = arg_23_0,
		awards = arg_23_1,
		index = arg_23_3
	}))
end

function var_0_0.GetTempleRedTip(arg_24_0, arg_24_1)
	local var_24_0 = pg.activity_template[arg_24_0]

	if not var_24_0 then
		return false
	end

	local var_24_1 = getProxy(ActivityProxy):getActivityById(arg_24_0)

	if not var_24_1 then
		return false
	end

	arg_24_1 = arg_24_1 or 60

	local var_24_2 = getProxy(PlayerProxy):getData()
	local var_24_3 = pg.activity_template[arg_24_0].config_data
	local var_24_4 = 0
	local var_24_5 = 0

	for iter_24_0, iter_24_1 in ipairs(var_24_3) do
		local var_24_6 = pg.activity_random_award_template[iter_24_1]
		local var_24_7 = var_24_6.resource_num
		local var_24_8 = var_24_2:getResById(var_24_6.resource_type)

		var_24_4 = math.max(var_24_4, math.floor(var_24_8 / var_24_7))

		local var_24_9 = var_24_1:getAwardInfos()[iter_24_1]

		var_24_5 = var_24_5 + ActivityItemPool.CreateItemPool(iter_24_1, var_24_9, nil, 1):getleftItemCount()
	end

	if var_24_5 <= 0 then
		return false
	end

	if arg_24_1 <= var_24_4 then
		return true
	end

	local var_24_10 = var_24_0.config_client.red_tip_time

	if var_24_10 then
		local var_24_11 = os.time({
			year = var_24_10[1],
			month = var_24_10[2],
			day = var_24_10[3],
			hour = var_24_10[4],
			min = var_24_10[5],
			sec = var_24_10[6]
		})

		return pg.TimeMgr.GetInstance():GetServerTime() - var_24_11 > 0 and var_24_4 > 1
	end

	return false
end

return var_0_0
