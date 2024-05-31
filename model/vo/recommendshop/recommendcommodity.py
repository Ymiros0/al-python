local var_0_0 = class("RecommendCommodity", import("model.vo.BaseVO"))
local var_0_1 = 1
local var_0_2 = 2

var_0_0.PRICE_TYPE_RMB = 1
var_0_0.PRICE_TYPE_RES = 2

local function var_0_3(arg_1_0)
	local var_1_0

	if arg_1_0 == var_0_1:
		var_1_0 = Goods.TYPE_CHARGE
	elif arg_1_0 == var_0_2:
		var_1_0 = Goods.TYPE_GIFT_PACKAGE

	assert(var_1_0)

	return var_1_0

local function var_0_4(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	local var_2_0 = {}

	if arg_2_0 == var_0_1:
		var_2_0 = arg_2_2
	elif arg_2_0 == var_0_2:
		var_2_0 = arg_2_3

	return (ChargeConst.getBuyCount(var_2_0, arg_2_1))

local function var_0_5(arg_3_0, arg_3_1, arg_3_2)
	if arg_3_0 == var_0_1:
		return 0
	elif arg_3_0 == var_0_2:
		return (ChargeConst.getGroupLimit(arg_3_2, arg_3_1 or 0))

def var_0_0.Ctor(arg_4_0, arg_4_1):
	arg_4_0.id = arg_4_1.id
	arg_4_0.configId = arg_4_0.id
	arg_4_0.commodity = arg_4_0.GenCommodity(arg_4_1.chargedList, arg_4_1.normalList, arg_4_1.normalGroupList)

def var_0_0.GenCommodity(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	local var_5_0 = arg_5_0.getConfig("shop_type")
	local var_5_1 = arg_5_0.getConfig("shop_id")
	local var_5_2 = var_0_3(var_5_0)
	local var_5_3 = Goods.Create({
		id = var_5_1
	}, var_5_2)
	local var_5_4 = var_0_4(var_5_0, arg_5_0.getConfig("shop_id"), arg_5_1, arg_5_2)

	var_5_3.updateBuyCount(var_5_4)

	if not var_5_3.isChargeType():
		local var_5_5 = var_0_5(var_5_0, var_5_3.getConfig("group"), arg_5_3)

		var_5_3.updateGroupCount(var_5_5)

	return var_5_3

def var_0_0.bindConfigTable(arg_6_0):
	return pg.recommend_shop

def var_0_0.GetName(arg_7_0):
	return arg_7_0.commodity.GetName() or ""

def var_0_0.GetDesc(arg_8_0):
	if arg_8_0.commodity.isChargeType():
		if arg_8_0.commodity.isMonthCard():
			return i18n("monthly_card_tip")
		else
			return arg_8_0.commodity.getConfig("descrip")
	else
		return arg_8_0.commodity.getDropInfo().getConfig("display")

def var_0_0.GetDropList(arg_9_0):
	if arg_9_0.commodity.isChargeType() and arg_9_0.commodity.isMonthCard():
		return arg_9_0.commodity.GetDropList()
	else
		return {}

def var_0_0.GetGem(arg_10_0):
	if arg_10_0.commodity.isChargeType():
		return arg_10_0.commodity.GetGemCnt()
	else
		return 0

def var_0_0.GetPrice(arg_11_0):
	if arg_11_0.commodity.isChargeType():
		local var_11_0 = arg_11_0.commodity.getConfig("money")

		return var_0_0.PRICE_TYPE_RMB, var_11_0
	else
		local var_11_1 = arg_11_0.commodity.GetPrice()
		local var_11_2 = arg_11_0.commodity.GetResType()

		return var_0_0.PRICE_TYPE_RES, var_11_1, var_11_2

def var_0_0.GetIcon(arg_12_0):
	local var_12_0 = arg_12_0.getConfig("pic")

	if var_12_0 and var_12_0 != "":
		return var_12_0
	elif arg_12_0.commodity.isChargeType():
		local var_12_1 = arg_12_0.commodity.getConfig("picture")

		return "ChargeIcon/" .. var_12_1
	else
		return arg_12_0.commodity.getDropInfo().getIcon() or ""

def var_0_0.InTime(arg_13_0):
	local var_13_0 = arg_13_0.getConfig("time")

	return pg.TimeMgr.GetInstance().inTime(var_13_0)

def var_0_0.GetOrder(arg_14_0):
	return arg_14_0.getConfig("order")

def var_0_0.CanPurchase(arg_15_0):
	local function var_15_0(arg_16_0)
		if arg_16_0.isChargeType():
			return False

		return arg_15_0.commodity.IsGroupLimit()

	return arg_15_0.InTime() and arg_15_0.commodity.canPurchase() and arg_15_0.commodity.inTime() and not var_15_0(arg_15_0.commodity)

def var_0_0.CanShow(arg_17_0):
	if arg_17_0.IsMonthCard():
		return True
	else
		return arg_17_0.CanPurchase()

def var_0_0.IsMonthCard(arg_18_0):
	return arg_18_0.commodity.isChargeType() and arg_18_0.commodity.isMonthCard()

def var_0_0.IsMonthCardAndCantPurchase(arg_19_0):
	if arg_19_0.IsMonthCard():
		local var_19_0 = getProxy(PlayerProxy).getRawData().getCardById(VipCard.MONTH)

		if var_19_0 and var_19_0.GetLeftDay() > (arg_19_0.commodity.getConfig("limit_arg") or 0):
			local var_19_1 = i18n("charge_menu_month_tip", var_19_0.GetLeftDay())

			return True, var_19_1
		else
			return False

	return False

def var_0_0.GetRealCommodity(arg_20_0):
	return arg_20_0.commodity

return var_0_0
