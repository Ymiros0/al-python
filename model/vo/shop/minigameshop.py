local var_0_0 = class("MiniGameShop", import(".BaseShop"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.goodsData = arg_1_1.goods
	arg_1_0.nextFlashTime = arg_1_1.next_flash_time
	arg_1_0.goods = {}

	for iter_1_0, iter_1_1 in ipairs(pg.gameroom_shop_template):
		local var_1_0 = Goods.Create(iter_1_1, Goods.TYPE_MINI_GAME)
		local var_1_1 = arg_1_0.getGoodData(iter_1_1.id) or 0

		var_1_0.UpdateCnt(var_1_1)

		arg_1_0.goods[var_1_0.getId()] = var_1_0

	arg_1_0.type = ShopArgs.ShopMiniGame

def var_0_0.setNextTime(arg_2_0, arg_2_1):
	arg_2_0.nextFlashTime = arg_2_1

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.goodsData):
		local var_2_0 = iter_2_1.id
		local var_2_1 = False

		if pg.gameroom_shop_template[var_2_0]:
			var_2_1 = pg.gameroom_shop_template[var_2_0].month_re != 0
		else
			warning("gameroom_shop_template 不存在 id = " .. tostring(var_2_0) .. "的物品")

		if var_2_1:
			arg_2_0.goodsData[iter_2_0].count = 0

def var_0_0.checkShopFlash(arg_3_0):
	local var_3_0 = pg.TimeMgr.GetInstance().GetServerTime()

	if arg_3_0.nextFlashTime and arg_3_0.nextFlashTime > 0:
		return var_3_0 > arg_3_0.nextFlashTime

	return False

def var_0_0.getGoodData(arg_4_0, arg_4_1):
	for iter_4_0, iter_4_1 in ipairs(arg_4_0.goodsData):
		if iter_4_1 and iter_4_1.id == arg_4_1:
			return iter_4_1.count

def var_0_0.consume(arg_5_0, arg_5_1, arg_5_2):
	arg_5_0.goods[arg_5_1].UpdateCnt(arg_5_2)

def var_0_0.IsSameKind(arg_6_0, arg_6_1):
	return isa(arg_6_1, MiniGameShop)

def var_0_0.GetCommodityById(arg_7_0, arg_7_1):
	return arg_7_0.getGoodsById(arg_7_1)

def var_0_0.GetCommodities(arg_8_0):
	local var_8_0 = {}

	for iter_8_0, iter_8_1 in pairs(arg_8_0.goods):
		table.insert(var_8_0, iter_8_1)

	table.sort(var_8_0, function(arg_9_0, arg_9_1)
		local var_9_0 = arg_9_0.CanPurchase() and 1 or 0
		local var_9_1 = arg_9_1.CanPurchase() and 1 or 0

		if var_9_0 == var_9_1:
			return arg_9_0.getConfig("order") < arg_9_1.getConfig("order")
		else
			return var_9_1 < var_9_0)

	return var_8_0

def var_0_0.bindConfigTable(arg_10_0):
	return None

def var_0_0.getRefreshCount(arg_11_0):
	return arg_11_0.refreshCount

def var_0_0.resetRefreshCount(arg_12_0):
	arg_12_0.refreshCount = 1

def var_0_0.increaseRefreshCount(arg_13_0):
	arg_13_0.refreshCount = arg_13_0.refreshCount + 1

def var_0_0.updateAllGoods(arg_14_0, arg_14_1):
	arg_14_0.goods = arg_14_1

def var_0_0.getGoodsById(arg_15_0, arg_15_1):
	assert(arg_15_0.goods[arg_15_1], "should exist good" .. arg_15_1)

	return Clone(arg_15_0.goods[arg_15_1])

def var_0_0.updateGoods(arg_16_0, arg_16_1):
	assert(arg_16_0.goods[arg_16_1.id], "should exist good" .. arg_16_1.id)

	arg_16_0.goods[arg_16_1.id] = arg_16_1

return var_0_0
