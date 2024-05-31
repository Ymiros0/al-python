local var_0_0 = class("BaseCommodity", import("...BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.id = arg_1_1.goods_id or arg_1_1.shop_id or arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.discount = arg_1_1.discount or 100
	arg_1_0.buyCount = arg_1_1.buy_count or arg_1_1.count or arg_1_1.pay_count or 0

	assert(arg_1_2, "type should exist")

	arg_1_0.type = arg_1_2
	arg_1_0.groupCount = arg_1_1.groupCount or 0

def var_0_0.bindConfigTable(arg_2_0):
	assert(False, "overwrite!!!")

def var_0_0.GetPrice(arg_3_0):
	assert(False, "overwrite!!!")

def var_0_0.GetPurchasableCnt(arg_4_0):
	assert(False, "overwrite!!!")

def var_0_0.GetName(arg_5_0):
	assert(False, "overwrite!!!")

def var_0_0.GetDropList(arg_6_0):
	assert(False, "overwrite!!!")

def var_0_0.GetResType(arg_7_0):
	assert(False, "overwrite!!!")

def var_0_0.reduceBuyCount(arg_8_0):
	arg_8_0.buyCount = arg_8_0.buyCount - 1

def var_0_0.increaseBuyCount(arg_9_0):
	if not arg_9_0.buyCount:
		arg_9_0.buyCount = 0

	arg_9_0.buyCount = arg_9_0.buyCount + 1

def var_0_0.addBuyCount(arg_10_0, arg_10_1):
	arg_10_0.buyCount = arg_10_0.buyCount + arg_10_1

def var_0_0.canPurchase(arg_11_0):
	return arg_11_0.buyCount > 0

def var_0_0.hasDiscount(arg_12_0):
	return arg_12_0.discount < 100

def var_0_0.isFree(arg_13_0):
	return arg_13_0.getConfig("discount") == 100

def var_0_0.isDisCount(arg_14_0):
	return False

def var_0_0.isChargeType(arg_15_0):
	return False

def var_0_0.isGiftPackage(arg_16_0):
	return arg_16_0.type == Goods.TYPE_GIFT_PACKAGE

def var_0_0.isSham(arg_17_0):
	return arg_17_0.type == Goods.TYPE_SHAM_BATTLE

def var_0_0.IsActivityExtra(arg_18_0):
	return arg_18_0.type == Goods.TYPE_ACTIVITY_EXTRA

def var_0_0.getKey(arg_19_0):
	return arg_19_0.id .. "_" .. arg_19_0.type

def var_0_0.updateBuyCount(arg_20_0, arg_20_1):
	arg_20_0.buyCount = arg_20_1

def var_0_0.updateGroupCount(arg_21_0, arg_21_1):
	arg_21_0.groupCount = arg_21_1

def var_0_0.firstPayDouble(arg_22_0):
	return False

def var_0_0.inTime(arg_23_0):
	if arg_23_0.type == Goods.TYPE_NEW_SERVER:
		local var_23_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_GIFT)

		if var_23_0 and not var_23_0.isEnd():
			return True, var_23_0.stopTime - pg.TimeMgr.GetInstance().GetServerTime()
		else
			return False

	local var_23_1 = arg_23_0.getConfig("time")

	if not var_23_1:
		return True

	if type(var_23_1) == "string":
		return var_23_1 == "always"
	else
		local var_23_2, var_23_3 = arg_23_0.getTimeStamp()

		if var_23_2 and var_23_3:
			local var_23_4 = pg.TimeMgr.GetInstance().GetServerTime()

			return var_23_2 <= var_23_4 and var_23_4 <= var_23_3, var_23_3 - var_23_4
		else
			return True

def var_0_0.getTimeStamp(arg_24_0):
	local var_24_0 = arg_24_0.getConfig("time")

	if var_24_0 and type(var_24_0) == "table":
		local var_24_1
		local var_24_2

		if #var_24_0 > 0:
			local var_24_3 = var_24_0[1][1][1] .. "-" .. var_24_0[1][1][2] .. "-" .. var_24_0[1][1][3] .. " " .. var_24_0[1][2][1] .. "." .. var_24_0[1][2][2] .. "." .. var_24_0[1][2][3]

			var_24_1 = pg.TimeMgr.GetInstance().ParseTimeEx(var_24_3, None, True)

		if #var_24_0 > 1:
			local var_24_4 = var_24_0[2][1][1] .. "-" .. var_24_0[2][1][2] .. "-" .. var_24_0[2][1][3] .. " " .. var_24_0[2][2][1] .. "." .. var_24_0[2][2][2] .. "." .. var_24_0[2][2][3]

			var_24_2 = pg.TimeMgr.GetInstance().ParseTimeEx(var_24_4, None, True)

		if var_24_1 and var_24_2:
			return var_24_1, var_24_2

def var_0_0.calDayLeft(arg_25_0):
	local var_25_0, var_25_1 = arg_25_0.inTime()

	if var_25_0 and var_25_1 and var_25_1 > 0:
		local var_25_2 = pg.TimeMgr.GetInstance().parseTimeFrom(var_25_1)

		return var_25_0, var_25_2 + 1

def var_0_0.GetGiftList(arg_26_0):
	return {}

def var_0_0.GetName(arg_27_0):
	assert(False, "overwrite me !!!!")

def var_0_0.IsGroupLimit(arg_28_0):
	assert(False, "overwrite me !!!!")

def var_0_0.CanUseVoucherType(arg_29_0):
	return False

def var_0_0.StaticCanUseVoucherType(arg_30_0, arg_30_1):
	return False

return var_0_0
