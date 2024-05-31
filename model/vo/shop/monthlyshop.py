local var_0_0 = class("MonthlyShop", import(".BaseShop"))

def var_0_0.Ctor(arg_1_0):
	arg_1_0.goods = {}

var_0_0.GoodsType = None

def var_0_0.IsSameKind(arg_2_0, arg_2_1):
	return isa(arg_2_1, MonthlyShop)

def var_0_0.GetCommodityById(arg_3_0, arg_3_1):
	return arg_3_0.getGoodsById(arg_3_1)

def var_0_0.GetCommodities(arg_4_0):
	return arg_4_0.getSortGoods()

def var_0_0.isOpen(arg_5_0):
	if not arg_5_0.id:
		return False

	local var_5_0 = False

	if arg_5_0.bindConfigTable()[arg_5_0.id]:
		local var_5_1 = pg.TimeMgr.GetInstance()

		var_5_0 = var_5_1.STimeDescS(var_5_1.GetServerTime(), "*t").month == arg_5_0.id

	return var_5_0

def var_0_0.getRestDays(arg_6_0):
	if not arg_6_0.id:
		return 0

	local var_6_0 = pg.TimeMgr.GetInstance()
	local var_6_1 = var_6_0.STimeDescS(var_6_0.GetServerTime(), "*t")
	local var_6_2 = Clone(var_6_1)

	var_6_2.month = arg_6_0.id

	if var_6_2.month >= 12:
		var_6_2.month = 0
		var_6_2.year = var_6_2.year + 1

	var_6_2.month = var_6_2.month + 1
	var_6_2.day = 0

	local var_6_3 = os.date("%d", os.time(var_6_2)) - var_6_1.day + 1

	return (math.max(var_6_3, 1))

def var_0_0.GetRestTime(arg_7_0):
	if not arg_7_0.id:
		return 0

	local var_7_0 = pg.TimeMgr.GetInstance()
	local var_7_1 = var_7_0.STimeDescS(var_7_0.GetServerTime(), "*t")
	local var_7_2 = Clone(var_7_1)

	var_7_2.month = arg_7_0.id

	if var_7_2.month >= 12:
		var_7_2.month = 0
		var_7_2.year = var_7_2.year + 1

	var_7_2.month = var_7_2.month + 1
	var_7_2.day = 0
	var_7_2.hour = 23
	var_7_2.min = 59
	var_7_2.sec = 59
	var_7_2.isdst = False

	local var_7_3 = os.time(var_7_2) - var_7_0.GetServerTime()

	return (math.max(var_7_3, 0))

def var_0_0.getSortGoods(arg_8_0):
	local var_8_0 = {}

	for iter_8_0, iter_8_1 in pairs(arg_8_0.goods):
		table.insert(var_8_0, iter_8_1)

	local function var_8_1(arg_9_0)
		return math.floor(arg_9_0 * 0.1)

	table.sort(var_8_0, function(arg_10_0, arg_10_1)
		local var_10_0 = 100
		local var_10_1 = 1000
		local var_10_2 = arg_10_0.getConfig("order") + arg_10_0.id / 100000
		local var_10_3 = arg_10_1.getConfig("order") + arg_10_1.id / 100000
		local var_10_4 = getProxy(CollectionProxy)

		local function var_10_5(arg_11_0)
			local var_11_0 = arg_11_0.getConfig("commodity_id")

			return arg_11_0.isSham() and arg_11_0.checkCommodityType(DROP_TYPE_SHIP) and var_10_4.getShipGroup(var_8_1(var_11_0))

		local function var_10_6(arg_12_0)
			return not arg_12_0.canPurchase()

		var_10_2 = var_10_5(arg_10_0) and not var_10_6(arg_10_0) and var_10_2 + var_10_0 or var_10_2
		var_10_3 = var_10_5(arg_10_1) and not var_10_6(arg_10_1) and var_10_3 + var_10_0 or var_10_3
		var_10_2 = var_10_6(arg_10_0) and var_10_2 + var_10_1 or var_10_2
		var_10_3 = var_10_6(arg_10_1) and var_10_3 + var_10_1 or var_10_3

		return var_10_2 < var_10_3)

	return var_8_0

def var_0_0.getGoodsCfg(arg_13_0, arg_13_1):
	return pg.activity_shop_template[arg_13_1]

def var_0_0.getGoodsById(arg_14_0, arg_14_1):
	return arg_14_0.goods[arg_14_1]

def var_0_0.bindConfigTable(arg_15_0):
	return pg.month_shop_template

return var_0_0
