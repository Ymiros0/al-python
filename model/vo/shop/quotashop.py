local var_0_0 = class("QuotaShop", import(".BaseShop"))

def var_0_0.Ctor(arg_1_0):
	arg_1_0.type = ShopArgs.ShopQuota

	local var_1_0 = pg.quota_shop_template[1].shop_goods

	arg_1_0.goods = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0):
		local var_1_1 = arg_1_0.getOwnedGoodCount(iter_1_1)

		arg_1_0.goods[iter_1_1] = Goods.Create({
			shop_id = iter_1_1,
			buy_count = var_1_1
		}, Goods.TYPE_QUOTA)

def var_0_0.getOwnedGoodCount(arg_2_0, arg_2_1):
	local var_2_0 = pg.activity_shop_template[arg_2_1]

	assert(var_2_0, "config is missing in activity_shop_template, id. " .. arg_2_1)

	return Drop.New({
		id = var_2_0.commodity_id,
		type = var_2_0.commodity_type,
		count = var_2_0.num
	}).getOwnedCount()

def var_0_0.IsSameKind(arg_3_0, arg_3_1):
	return isa(arg_3_1, QuotaShop)

def var_0_0.GetCommodityById(arg_4_0, arg_4_1):
	return arg_4_0.getGoodsById(arg_4_1)

def var_0_0.GetCommodities(arg_5_0):
	return arg_5_0.getSortGoods()

def var_0_0.getSortGoods(arg_6_0):
	local var_6_0 = {}

	for iter_6_0, iter_6_1 in pairs(arg_6_0.goods):
		table.insert(var_6_0, iter_6_1)

	table.sort(var_6_0, CompareFuncs({
		function(arg_7_0)
			return arg_7_0.canPurchase() and 0 or 1,
		function(arg_8_0)
			return arg_8_0.getConfig("order"),
		function(arg_9_0)
			return arg_9_0.id
	}))

	return var_6_0

def var_0_0.getGoodsCfg(arg_10_0, arg_10_1):
	return pg.activity_shop_template[arg_10_1]

def var_0_0.getGoodsById(arg_11_0, arg_11_1):
	assert(arg_11_0.goods[arg_11_1], "goods should exist")

	return arg_11_0.goods[arg_11_1]

def var_0_0.getLimitGoodCount(arg_12_0, arg_12_1):
	local var_12_0 = pg.activity_shop_template[arg_12_1].limit_args

	if type(var_12_0) == "table":
		for iter_12_0, iter_12_1 in ipairs(var_12_0):
			if iter_12_1[1] == "quota":
				return iter_12_1[2]

	assert(False, "good not limit_args 'quota' with good id. " .. arg_12_1)

return var_0_0
