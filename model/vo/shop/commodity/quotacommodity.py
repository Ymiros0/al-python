local var_0_0 = class("QuotaCommodity", import(".BaseCommodity"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.activity_shop_template

def var_0_0.canPurchase(arg_2_0):
	return arg_2_0.GetPurchasableCnt() > 0

def var_0_0.GetPurchasableCnt(arg_3_0):
	return arg_3_0.GetLimitGoodCount() - arg_3_0.buyCount

def var_0_0.GetLimitGoodCount(arg_4_0):
	local var_4_0 = arg_4_0.getConfig("limit_args")

	if type(var_4_0) == "table":
		for iter_4_0, iter_4_1 in ipairs(var_4_0):
			if iter_4_1[1] == "quota":
				return iter_4_1[2]

	assert(False, "good not limit_args 'quota' with id. " .. arg_4_0.id)

return var_0_0
