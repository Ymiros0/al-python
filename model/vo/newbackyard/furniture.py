local var_0_0 = class("Furniture", import("..BaseVO"))

var_0_0.TYPE_WALLPAPER = 1
var_0_0.TYPE_FURNITURE = 2
var_0_0.TYPE_DECORATE = 3
var_0_0.TYPE_FLOORPAPER = 4
var_0_0.TYPE_MAT = 5
var_0_0.TYPE_WALL = 6
var_0_0.TYPE_COLLECTION = 7
var_0_0.TYPE_STAGE = 8
var_0_0.TYPE_ARCH = 9
var_0_0.TYPE_WALL_MAT = 10
var_0_0.TYPE_MOVEABLE = 11
var_0_0.TYPE_TRANSPORT = 12
var_0_0.TYPE_RANDOM_CONTROLLER = 13
var_0_0.TYPE_FOLLOWER = 14
var_0_0.TYPE_LUTE = 15
var_0_0.TYPE_RANDOM_SLOT = 16
var_0_0.INDEX_TO_COMFORTABLE_TYPE = {
	var_0_0.TYPE_WALLPAPER,
	var_0_0.TYPE_FURNITURE,
	var_0_0.TYPE_DECORATE,
	var_0_0.TYPE_FLOORPAPER,
	var_0_0.TYPE_MAT,
	var_0_0.TYPE_WALL,
	var_0_0.TYPE_COLLECTION,
	var_0_0.TYPE_FURNITURE,
	var_0_0.TYPE_FURNITURE,
	var_0_0.TYPE_WALL,
	var_0_0.TYPE_FURNITURE,
	var_0_0.TYPE_FURNITURE,
	var_0_0.TYPE_FURNITURE,
	var_0_0.TYPE_FURNITURE,
	var_0_0.TYPE_FURNITURE,
	var_0_0.TYPE_FURNITURE
}
var_0_0.INDEX_TO_SHOP_TYPE = {
	{
		var_0_0.TYPE_WALLPAPER
	},
	{
		var_0_0.TYPE_FLOORPAPER
	},
	{
		var_0_0.TYPE_FURNITURE,
		var_0_0.TYPE_MAT,
		var_0_0.TYPE_COLLECTION,
		var_0_0.TYPE_STAGE,
		var_0_0.TYPE_ARCH,
		var_0_0.TYPE_MOVEABLE,
		var_0_0.TYPE_TRANSPORT,
		var_0_0.TYPE_RANDOM_CONTROLLER,
		var_0_0.TYPE_FOLLOWER,
		var_0_0.TYPE_LUTE,
		var_0_0.TYPE_RANDOM_SLOT
	},
	{},
	{
		var_0_0.TYPE_DECORATE
	},
	{
		var_0_0.TYPE_WALL,
		var_0_0.TYPE_WALL_MAT
	}
}

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = tonumber(arg_1_1.id)
	arg_1_0.configId = arg_1_1.configId or tonumber(arg_1_1.id)
	arg_1_0.count = arg_1_1.count or 0
	arg_1_0.date = arg_1_1.get_time or arg_1_1.date or 0
	arg_1_0.newFlag = False

def var_0_0.MarkNew(arg_2_0):
	arg_2_0.newFlag = True

def var_0_0.ClearNewFlag(arg_3_0):
	arg_3_0.newFlag = False

def var_0_0.getDate(arg_4_0):
	if arg_4_0.date > 0:
		return pg.TimeMgr.GetInstance().STimeDescS(arg_4_0.date, "%Y/%m/%d")

def var_0_0.GetOwnCnt(arg_5_0):
	return arg_5_0.count

def var_0_0.setCount(arg_6_0, arg_6_1):
	arg_6_0.count = arg_6_1

def var_0_0.isNotForSale(arg_7_0):
	return arg_7_0.getConfig("not_for_sale") == 1

def var_0_0.isForActivity(arg_8_0):
	return arg_8_0.getConfig("not_for_sale") == 2

def var_0_0.addFurniTrueCount(arg_9_0, arg_9_1):
	arg_9_0.count = arg_9_0.count + arg_9_1

def var_0_0.canPurchase(arg_10_0):
	return arg_10_0.count < arg_10_0.getConfig("count")

def var_0_0.bindConfigTable(arg_11_0):
	return pg.furniture_data_template

def var_0_0.bindShopConfigTable(arg_12_0):
	return pg.furniture_shop_template

def var_0_0.isFurniture(arg_13_0):
	return arg_13_0.getConfig("type") != 0

def var_0_0.IsNew(arg_14_0):
	return arg_14_0.getConfig("new") != 0

def var_0_0.getConfig(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_0.bindConfigTable()[arg_15_0.configId]

	assert(var_15_0, arg_15_0.configId)

	if var_15_0[arg_15_1]:
		return var_15_0[arg_15_1]
	else
		local var_15_1 = arg_15_0.bindShopConfigTable()[arg_15_0.configId]

		if var_15_1:
			return var_15_1[arg_15_1]

def var_0_0.getTypeForComfortable(arg_16_0):
	local var_16_0 = arg_16_0.getConfig("type")
	local var_16_1 = var_0_0.INDEX_TO_COMFORTABLE_TYPE[var_16_0]

	return var_16_1 and var_16_1 or var_0_0.TYPE_FURNITURE

def var_0_0.getDeblocking(arg_17_0):
	local var_17_0 = arg_17_0.getConfig("themeId")
	local var_17_1 = pg.backyard_theme_template[var_17_0]

	assert(var_17_1, "pg.backyard_theme_template>>> id" .. var_17_0)

	return var_17_1.deblocking

def var_0_0.inTheme(arg_18_0):
	local var_18_0 = arg_18_0.getConfig("themeId")

	if var_18_0 == 0:
		return False

	local var_18_1 = pg.backyard_theme_template[var_18_0]

	assert(var_18_1, "pg.backyard_theme_template>>id" .. var_18_0)

	return table.contains(var_18_1.ids, arg_18_0.id)

def var_0_0.isLock(arg_19_0, arg_19_1):
	return arg_19_0.inTheme() and arg_19_1 < arg_19_0.getDeblocking()

def var_0_0.isPaper(arg_20_0):
	local var_20_0 = arg_20_0.getConfig("type")

	return var_20_0 == 4 or var_20_0 == 1

def var_0_0.GetThemeName(arg_21_0):
	local var_21_0 = arg_21_0.getConfig("themeId")
	local var_21_1 = pg.backyard_theme_template[var_21_0]

	if var_21_1:
		return var_21_1.name

	return ""

def var_0_0.inTime(arg_22_0):
	local var_22_0 = arg_22_0.getConfig("time")

	return pg.TimeMgr.GetInstance().inTime(var_22_0)

def var_0_0.isTimeLimit(arg_23_0):
	local var_23_0 = arg_23_0.getConfig("time")

	return var_23_0 and type(var_23_0) == "table"

def var_0_0.isRecordTime(arg_24_0):
	return arg_24_0.getConfig("is_get_time_note") == 1

def var_0_0.isDisCount(arg_25_0):
	return (arg_25_0.getConfig("discount") or 0) > 0 and pg.TimeMgr.GetInstance().inTime(arg_25_0.getConfig("discount_time"))

def var_0_0.sortSizeFunc(arg_26_0):
	local var_26_0 = arg_26_0.getConfig("size")

	return (var_26_0[1] or 0) * (var_26_0[2] or 0)

def var_0_0.getPrice(arg_27_0, arg_27_1):
	local var_27_0 = (100 - (arg_27_0.isDisCount() and arg_27_0.getConfig("discount") or 0)) / 100
	local var_27_1 = arg_27_1 == 4 and arg_27_0.getConfig("gem_price") or arg_27_1 == 6 and arg_27_0.getConfig("dorm_icon_price")

	if var_27_1:
		local var_27_2 = math.floor(var_27_1 * var_27_0)

		return var_27_1 > 0 and var_27_2 == 0 and 1 or var_27_2

def var_0_0.canPurchaseByGem(arg_28_0):
	local var_28_0 = arg_28_0.getPrice(4)

	return var_28_0 and var_28_0 != 0

def var_0_0.canPurchaseByDormMoeny(arg_29_0):
	local var_29_0 = arg_29_0.getPrice(6)

	return var_29_0 and var_29_0 != 0

def var_0_0.getSortCurrency(arg_30_0):
	local var_30_0 = 0

	if arg_30_0.canPurchaseByGem():
		var_30_0 = var_30_0 + 2
	elif arg_30_0.canPurchaseByDormMoeny():
		var_30_0 = var_30_0 + 1

	return var_30_0

def var_0_0.sortPriceFunc(arg_31_0):
	local var_31_0 = arg_31_0.getConfig("gem_price") or 0
	local var_31_1 = arg_31_0.getConfig("dorm_icon_price") or 0

	if var_31_0 > 0:
		return var_31_0 + 1000000
	else
		return var_31_1

def var_0_0.isMatchSearchKey(arg_32_0, arg_32_1):
	if arg_32_1 == "" or not arg_32_1:
		return True

	local var_32_0 = arg_32_0.getConfig("name")
	local var_32_1 = arg_32_0.getConfig("describe")

	arg_32_1 = string.lower(arg_32_1)

	local var_32_2 = string.lower(var_32_0)
	local var_32_3 = string.lower(var_32_1)

	if string.find(var_32_2, arg_32_1) or string.find(var_32_2, arg_32_1):
		return True

	return False

def var_0_0.IsShopType(arg_33_0):
	return arg_33_0.bindShopConfigTable()[arg_33_0.configId] != None

return var_0_0
