ChargeConst = {}

local var_0_0 = ChargeConst

def var_0_0.getBuyCount(arg_1_0, arg_1_1):
	if not arg_1_0:
		return 0

	local var_1_0 = arg_1_0[arg_1_1]

	return var_1_0 and var_1_0.buyCount or 0

def var_0_0.getGroupLimit(arg_2_0, arg_2_1):
	if not arg_2_0:
		return 0

	for iter_2_0, iter_2_1 in ipairs(arg_2_0):
		if iter_2_1.shop_id == arg_2_1:
			return iter_2_1.pay_count

	return 0

def var_0_0.getGoodsLimitInfo(arg_3_0):
	local var_3_0
	local var_3_1
	local var_3_2
	local var_3_3 = pg.shop_template[arg_3_0]

	if var_3_3:
		local var_3_4 = var_3_3.limit_args[1]

		if type(var_3_4) == "table":
			for iter_3_0, iter_3_1 in ipairs(var_3_3.limit_args):
				local var_3_5 = iter_3_1[1]

				if var_3_5 == "level":
					var_3_0 = iter_3_1[2]
				elif var_3_5 == "count":
					var_3_1 = iter_3_1[2]
					var_3_2 = iter_3_1[3]
		elif type(var_3_4) == "string":
			if var_3_4 == "level":
				var_3_0 = var_3_3.limit_args[2]
			elif var_3_4 == "count":
				var_3_1 = var_3_3.limit_args[2]
				var_3_2 = var_3_3.limit_args[3]

	return var_3_0, var_3_1, var_3_2

def var_0_0.isNeedSetBirth():
	if PLATFORM_CODE == PLATFORM_JP and pg.SdkMgr.GetInstance().GetIsPlatform() and not pg.SdkMgr.GetInstance().GetIsBirthSet():
		return True

	return False

return var_0_0
