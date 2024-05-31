local var_0_0 = class("NewServerCommodity", import("...BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.count = arg_1_1.count or arg_1_0.getConfig("goods_purchase_limit")
	arg_1_0.boughtRecord = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.bought_record or {}):
		arg_1_0.boughtRecord[iter_1_1] = True

def var_0_0.bindConfigTable(arg_2_0):
	return pg.newserver_shop_template

def var_0_0.CanPurchase(arg_3_0):
	return arg_3_0.count > 0

def var_0_0.ReduceCnt(arg_4_0, arg_4_1):
	arg_4_0.count = arg_4_0.count - arg_4_1

def var_0_0.CanPurchaseMulTimes(arg_5_0, arg_5_1):
	return arg_5_1 <= arg_5_0.count

def var_0_0.CanPurchaseSubGoods(arg_6_0, arg_6_1):
	if arg_6_0.LimitPurchaseSubGoods():
		return not (arg_6_0.boughtRecord[arg_6_1] == True)
	else
		return True

def var_0_0.UpdateBoughtRecord(arg_7_0, arg_7_1):
	arg_7_0.boughtRecord[arg_7_1] = True

def var_0_0.LimitPurchaseSubGoods(arg_8_0):
	return arg_8_0.getConfig("goods_type") == 4

def var_0_0.Selectable(arg_9_0):
	local var_9_0 = arg_9_0.getConfig("goods_type")

	return var_9_0 == 2 or var_9_0 == 4

def var_0_0.GetConsume(arg_10_0):
	return Drop.New({
		type = arg_10_0.getConfig("resource_category"),
		id = arg_10_0.getConfig("resource_type"),
		count = arg_10_0.getConfig("resource_num")
	})

def var_0_0.GetDesc(arg_11_0):
	return {
		name = arg_11_0.getConfig("goods_name"),
		icon = arg_11_0.getConfig("goods_icon"),
		rarity = arg_11_0.getConfig("goods_rarity")
	}

def var_0_0.IsOpening(arg_12_0, arg_12_1):
	local var_12_0 = {}
	local var_12_1 = arg_12_1 + arg_12_0.getConfig("unlock_time")
	local var_12_2 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_12_3 = var_12_1 <= var_12_2

	if not var_12_3:
		local var_12_4, var_12_5, var_12_6, var_12_7 = pg.TimeMgr.GetInstance().parseTimeFrom(var_12_1 - var_12_2)

		var_12_0.day = var_12_4
		var_12_0.hour = var_12_5

	return var_12_3, var_12_0

def var_0_0.GetDropCnt(arg_13_0):
	return arg_13_0.getConfig("num")

def var_0_0.GetCanPurchaseCnt(arg_14_0):
	return arg_14_0.count

def var_0_0.GetCanPurchaseMaxCnt(arg_15_0):
	return arg_15_0.getConfig("goods_purchase_limit")

def var_0_0.GetDropType(arg_16_0):
	return arg_16_0.getConfig("type")

def var_0_0.GetSelectableGoods(arg_17_0):
	return arg_17_0.getConfig("goods")

def var_0_0.CheckTimeLimit(arg_18_0):
	local var_18_0 = False
	local var_18_1 = False
	local var_18_2
	local var_18_3 = arg_18_0.getConfig("type")
	local var_18_4 = arg_18_0.getConfig("goods")[1]
	local var_18_5 = Item.getConfigData(var_18_4)

	if var_18_3 == DROP_TYPE_VITEM and var_18_5.virtual_type == 22:
		var_18_0 = True
		var_18_2 = True

		local var_18_6 = getProxy(ActivityProxy).getActivityById(var_18_5.link_id)

		if var_18_6 and not var_18_6.isEnd():
			var_18_1 = True

	return var_18_0, var_18_1, var_18_2

def var_0_0.GetPurchasableCnt(arg_19_0):
	return arg_19_0.count

return var_0_0
