local var_0_0 = class("ActivityShop", import(".BaseShop"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.activityId = arg_1_1.id

	local var_1_0 = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.data1_list) do
		var_1_0[iter_1_1] = arg_1_1.data2_list[iter_1_0]
	end

	arg_1_0.goods = {}

	local var_1_1 = arg_1_0:bindConfigTable()

	for iter_1_2, iter_1_3 in ipairs(var_1_1.all) do
		if arg_1_1.id == var_1_1[iter_1_3].activity then
			local var_1_2 = var_1_0[iter_1_3] or 0

			arg_1_0.goods[iter_1_3] = Goods.Create({
				shop_id = iter_1_3,
				buy_count = var_1_2
			}, Goods.TYPE_ACTIVITY)
		end
	end

	arg_1_0.type = ShopArgs.ShopActivity
	arg_1_0.config = pg.activity_template[arg_1_0.activityId]
end

function var_0_0.IsSameKind(arg_2_0, arg_2_1)
	return isa(arg_2_1, ActivityShop) and arg_2_1.activityId and arg_2_1.activityId == arg_2_0.activityId
end

function var_0_0.GetCommodityById(arg_3_0, arg_3_1)
	return arg_3_0:getGoodsById(arg_3_1)
end

function var_0_0.GetCommodities(arg_4_0)
	return arg_4_0:getSortGoods()
end

function var_0_0.getSortGoods(arg_5_0)
	local var_5_0 = {}

	for iter_5_0, iter_5_1 in pairs(arg_5_0.goods) do
		table.insert(var_5_0, iter_5_1)
	end

	table.sort(var_5_0, CompareFuncs({
		function(arg_6_0)
			local var_6_0, var_6_1 = arg_6_0:CheckArgLimit()

			return (arg_6_0:canPurchase() or var_6_1) and 0 or 1
		end,
		function(arg_7_0)
			local var_7_0, var_7_1, var_7_2 = arg_7_0:CheckTimeLimit()

			return var_7_0 and var_7_1 and 0 or 1
		end,
		function(arg_8_0)
			return arg_8_0:getConfig("order")
		end,
		function(arg_9_0)
			return arg_9_0.id
		end
	}))

	return var_5_0
end

function var_0_0.bindConfigTable(arg_10_0)
	return pg.activity_shop_template
end

function var_0_0.getGoodsById(arg_11_0, arg_11_1)
	return arg_11_0.goods[arg_11_1]
end

function var_0_0.isEnd(arg_12_0)
	local var_12_0 = getProxy(ActivityProxy):getActivityById(arg_12_0.activityId)

	return not var_12_0 or var_12_0:isEnd()
end

function var_0_0.getOpenTime(arg_13_0)
	local var_13_0 = pg.activity_template[arg_13_0.activityId].time
	local var_13_1 = var_13_0[2][1]
	local var_13_2 = var_13_0[3][1]
	local var_13_3 = var_13_0[3][2]

	return string.format("%d.%d.%d~%d.%d.%d %d:%d:%d", var_13_1[1], var_13_1[2], var_13_1[3], var_13_2[1], var_13_2[2], var_13_2[3], var_13_3[1], var_13_3[2], var_13_3[3])
end

function var_0_0.getStartTime(arg_14_0)
	if arg_14_0:isEnd() then
		return 0
	end

	return getProxy(ActivityProxy):getActivityById(arg_14_0.activityId):getStartTime()
end

function var_0_0.getBgPath(arg_15_0)
	local var_15_0 = pg.activity_template[arg_15_0.activityId]
	local var_15_1 = var_15_0.config_client[2] or {
		255,
		255,
		255,
		255
	}
	local var_15_2 = var_15_0.config_client.outline or {
		0,
		0,
		0,
		1
	}

	return var_15_0.config_client[1], Color.New(var_15_1[1], var_15_1[2], var_15_1[3], var_15_1[4]), Color.New(var_15_2[1], var_15_2[2], var_15_2[3], var_15_2[4])
end

function var_0_0.getToggleImage(arg_16_0)
	return pg.activity_template[arg_16_0.activityId].config_client.toggle or "huodongdduihuan_butten"
end

function var_0_0.getResId(arg_17_0)
	local var_17_0

	for iter_17_0, iter_17_1 in pairs(arg_17_0.goods) do
		var_17_0 = iter_17_1

		break
	end

	return (var_17_0:getConfig("resource_type"))
end

function var_0_0.GetResList(arg_18_0)
	local var_18_0 = {}

	for iter_18_0, iter_18_1 in pairs(arg_18_0.goods) do
		var_18_0[iter_18_1:getConfig("resource_type")] = true
	end

	local var_18_1 = {}

	for iter_18_2, iter_18_3 in pairs(var_18_0) do
		table.insert(var_18_1, iter_18_2)
	end

	return var_18_1
end

function var_0_0.GetEnterVoice(arg_19_0)
	local var_19_0 = arg_19_0.config.config_client.enter

	if var_19_0 then
		return var_19_0[1], var_19_0[2], var_19_0[3]
	end
end

function var_0_0.GetPurchaseVoice(arg_20_0)
	local var_20_0 = arg_20_0.config.config_client.purchase

	if var_20_0 then
		return var_20_0[1], var_20_0[2], var_20_0[3]
	end
end

function var_0_0.GetPurchaseAllVoice(arg_21_0)
	local var_21_0 = arg_21_0.config.config_client.purchase_all

	if var_21_0 then
		return var_21_0[1], var_21_0[2], var_21_0[3]
	end
end

function var_0_0.GetTouchVoice(arg_22_0)
	local var_22_0 = arg_22_0.config.config_client.touch

	if var_22_0 then
		return var_22_0[1], var_22_0[2], var_22_0[3]
	end
end

function var_0_0.IsEventShop(arg_23_0)
	return pg.activity_template[arg_23_0.activityId].config_client.event_shop
end

function var_0_0.GetBGM(arg_24_0)
	return pg.activity_template[arg_24_0.activityId].config_client.bgm or ""
end

return var_0_0
