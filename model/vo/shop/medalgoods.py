local var_0_0 = class("MedalGoods", import("model.vo.BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.configId = arg_1_1.id
	arg_1_0.count = arg_1_1.count

def var_0_0.UpdateCnt(arg_2_0, arg_2_1):
	arg_2_0.count = arg_2_0.count - arg_2_1

def var_0_0.bindConfigTable(arg_3_0):
	return pg.honormedal_goods_list

def var_0_0.CanPurchase(arg_4_0):
	return arg_4_0.count > 0

def var_0_0.GetPrice(arg_5_0):
	return arg_5_0.getConfig("price")

def var_0_0.Selectable(arg_6_0):
	return arg_6_0.getConfig("goods_type") == 2

def var_0_0.GetFirstDropId(arg_7_0):
	return arg_7_0.getConfig("goods")

def var_0_0.GetMaxCnt(arg_8_0):
	return arg_8_0.count

def var_0_0.CanPurchaseCnt(arg_9_0, arg_9_1):
	return arg_9_1 <= arg_9_0.count

def var_0_0.GetLimit(arg_10_0):
	return arg_10_0.getConfig("goods_purchase_limit")

def var_0_0.GetDropInfo(arg_11_0):
	return Drop.New({
		type = arg_11_0.getConfig("type"),
		id = arg_11_0.getConfig("goods")[1],
		count = arg_11_0.getConfig("num")
	})

return var_0_0
