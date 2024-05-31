local var_0_0 = class("EducateShopProxy")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.binder = arg_1_1
	arg_1_0.data = {}

def var_0_0.SetUp(arg_2_0, arg_2_1):
	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.shops or {}):
		var_2_0[iter_2_1.shop_id] = iter_2_1.goods

	arg_2_0.data = {}

	for iter_2_2, iter_2_3 in ipairs(pg.child_shop.all):
		arg_2_0.data[iter_2_3] = EducateShop.New(iter_2_3, var_2_0[iter_2_3] or {})

	arg_2_0.discountData = {}

	for iter_2_4, iter_2_5 in ipairs(arg_2_1.discountEventIds or {}):
		arg_2_0.AddDiscountEventById(iter_2_5)

def var_0_0.GetShopWithId(arg_3_0, arg_3_1):
	return arg_3_0.data[arg_3_1]

def var_0_0.UpdateShop(arg_4_0, arg_4_1):
	arg_4_0.data[arg_4_1.id] = arg_4_1

def var_0_0.GetDiscountData(arg_5_0):
	return arg_5_0.discountData

def var_0_0.IsDiscountById(arg_6_0, arg_6_1):
	return arg_6_0.discountData[arg_6_1]

def var_0_0.GetDiscountById(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.discountData[arg_7_1]

	return var_7_0 and var_7_0.GetDiscountRatio() or 0

def var_0_0.AddDiscountEventById(arg_8_0, arg_8_1):
	local var_8_0 = EducateSpecialEvent.New(arg_8_1)

	arg_8_0.discountData[var_8_0.GetDiscountShopId()] = var_8_0

def var_0_0.OnNewWeek(arg_9_0, arg_9_1):
	local var_9_0 = {}

	for iter_9_0, iter_9_1 in pairs(arg_9_0.data):
		if iter_9_1.IsRefreshShop(arg_9_1):
			table.insert(var_9_0, function(arg_10_0)
				arg_9_0.binder.sendNotification(GAME.EDUCATE_REQUEST_SHOP_DATA, {
					shopId = iter_9_1.id,
					callback = arg_10_0
				}))

	seriesAsync(var_9_0, function()
		return)

	for iter_9_2, iter_9_3 in pairs(arg_9_0.discountData):
		if not iter_9_3.InDiscountTime(arg_9_1):
			arg_9_0.discountData[iter_9_2] = None

return var_0_0
