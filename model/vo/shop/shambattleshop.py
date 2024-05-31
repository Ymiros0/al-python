local var_0_0 = class("ShamBattleShop", import(".MonthlyShop"))

var_0_0.GoodsType = Goods.TYPE_SHAM_BATTLE
var_0_0.type = ShopArgs.ShopShamBattle

def var_0_0.update(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.id = arg_1_1
	arg_1_0.configId = arg_1_1

	local var_1_0 = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_2):
		var_1_0[iter_1_1.shop_id] = iter_1_1.pay_count

	table.clear(arg_1_0.goods)

	if arg_1_0.id and arg_1_0.id > 0 and arg_1_0.getConfigTable():
		for iter_1_2, iter_1_3 in ipairs(arg_1_0.getConfig("core_shop_goods")):
			local var_1_1 = var_1_0[iter_1_3] or 0

			arg_1_0.goods[iter_1_3] = Goods.Create({
				shop_id = iter_1_3,
				buy_count = var_1_1
			}, arg_1_0.GoodsType)

return var_0_0
