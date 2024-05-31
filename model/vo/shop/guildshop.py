local var_0_0 = class("GuildShop", import(".BaseShop"))

var_0_0.AUTO_REFRESH = 1
var_0_0.MANUAL_REFRESH = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id or 1
	arg_1_0.configId = arg_1_0.id
	arg_1_0.goods = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.good_list):
		local var_1_0 = GuildGoods.New(iter_1_1)

		arg_1_0.goods[var_1_0.id] = var_1_0

	arg_1_0.refreshCount = arg_1_1.refresh_count
	arg_1_0.nextTime = arg_1_1.next_refresh_time
	arg_1_0.type = ShopArgs.ShopGUILD

def var_0_0.IsSameKind(arg_2_0, arg_2_1):
	return isa(arg_2_1, GuildShop)

def var_0_0.GetCommodityById(arg_3_0, arg_3_1):
	return arg_3_0.getGoodsById(arg_3_1)

def var_0_0.GetCommodities(arg_4_0):
	return arg_4_0.getSortGoods()

def var_0_0.updateNextRefreshTime(arg_5_0, arg_5_1):
	arg_5_0.nextTime = arg_5_1

def var_0_0.CanRefresh(arg_6_0):
	return arg_6_0.refreshCount <= 0

def var_0_0.getSortGoods(arg_7_0):
	local var_7_0 = {}

	for iter_7_0, iter_7_1 in pairs(arg_7_0.goods):
		table.insert(var_7_0, iter_7_1)

	table.sort(var_7_0, function(arg_8_0, arg_8_1)
		local var_8_0 = arg_8_0.getConfig("order") or 0
		local var_8_1 = arg_8_1.getConfig("order") or 0

		if var_8_0 == var_8_1:
			return arg_8_0.id < arg_8_1.id
		else
			return var_8_1 < var_8_0)

	return var_7_0

def var_0_0.getGoodsById(arg_9_0, arg_9_1):
	assert(arg_9_0.goods[arg_9_1], "goods should exist")

	return arg_9_0.goods[arg_9_1]

def var_0_0.GetResetConsume(arg_10_0):
	return pg.guildset.store_reset_cost.key_value

def var_0_0.UpdateGoodsCnt(arg_11_0, arg_11_1, arg_11_2):
	arg_11_0.getGoodsById(arg_11_1).UpdateCnt(arg_11_2)

return var_0_0
