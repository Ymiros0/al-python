local var_0_0 = class("BaseShop", import("..BaseVO"))

def var_0_0.IsSameKind(arg_1_0, arg_1_1):
	assert(False)

def var_0_0.GetCommodityById(arg_2_0, arg_2_1):
	assert(False)

def var_0_0.GetCommodities(arg_3_0):
	assert(False)

def var_0_0.IsPurchaseAll(arg_4_0):
	local var_4_0 = arg_4_0.GetCommodities()

	for iter_4_0, iter_4_1 in pairs(var_4_0):
		if iter_4_1.canPurchase():
			return False

	return True

return var_0_0
