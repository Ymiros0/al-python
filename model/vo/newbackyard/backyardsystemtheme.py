local var_0_0 = class("BackYardSystemTheme", import(".BackYardSelfThemeTemplate"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.level = 1
	arg_1_0.order = arg_1_0.getConfig("order")

def var_0_0.GetRawPutList(arg_2_0):
	arg_2_0.CheckLevel()

	local var_2_0 = getProxy(DormProxy).getRawData().level

	if not arg_2_0.putInfo:
		local var_2_1

		pcall(function()
			var_2_1 = require("GameCfg.backyardTheme.theme_" .. arg_2_0.id))

		var_2_1 = var_2_1 or require("GameCfg.backyardTheme.theme_empty")

		local var_2_2 = var_2_1["furnitures_" .. var_2_0] or {}

		arg_2_0.putInfo = _.select(var_2_2, function(arg_4_0)
			return pg.furniture_data_template[arg_4_0.id])

	return arg_2_0.putInfo

def var_0_0.CheckLevel(arg_5_0):
	local var_5_0 = getProxy(DormProxy).getRawData().level

	if arg_5_0.level != var_5_0:
		arg_5_0.furniTruesByIds = None
		arg_5_0.putInfo = None
		arg_5_0.level = var_5_0

def var_0_0.GetAllFurniture(arg_6_0):
	arg_6_0.CheckLevel()

	local var_6_0 = not arg_6_0.furniTruesByIds

	var_0_0.super.GetAllFurniture(arg_6_0)

	if var_6_0:
		arg_6_0.CheckData()

	return arg_6_0.furniTruesByIds

def var_0_0.GetWarpFurnitures(arg_7_0):
	arg_7_0.CheckLevel()

	return var_0_0.super.GetWarpFurnitures(arg_7_0)

def var_0_0.CheckData(arg_8_0):
	local var_8_0 = getProxy(DormProxy).getRawData()
	local var_8_1 = {}
	local var_8_2 = {}

	for iter_8_0, iter_8_1 in pairs(arg_8_0.furniTruesByIds):
		if not var_8_0.IsPurchasedFurniture(iter_8_1.configId):
			if iter_8_1.parent != 0:
				table.insert(var_8_2, {
					pid = iter_8_1.parent,
					id = iter_8_0
				})
			elif table.getCount(iter_8_1.child) > 0:
				for iter_8_2, iter_8_3 in pairs(iter_8_1.child):
					table.insert(var_8_1, iter_8_2)

			table.insert(var_8_1, iter_8_0)

	local var_8_3 = #var_8_1 > 0 or #var_8_2 > 0

	for iter_8_4, iter_8_5 in ipairs(var_8_1):
		arg_8_0.furniTruesByIds[iter_8_5] = None

	for iter_8_6, iter_8_7 in pairs(var_8_2):
		local var_8_4 = arg_8_0.furniTruesByIds[iter_8_7.pid]

		if var_8_4:
			for iter_8_8, iter_8_9 in pairs(var_8_4.child):
				if iter_8_8 == iter_8_7.id:
					var_8_4.child[iter_8_7.id] = None

					break

	return var_8_3

def var_0_0.bindConfigTable(arg_9_0):
	return pg.backyard_theme_template

def var_0_0.IsOverTime(arg_10_0):
	local var_10_0 = pg.furniture_shop_template
	local var_10_1 = arg_10_0.getConfig("ids")

	return _.all(var_10_1, function(arg_11_0)
		return not var_10_0[arg_11_0] or not pg.TimeMgr.GetInstance().inTime(var_10_0[arg_11_0].time))

def var_0_0.GetFurnitures(arg_12_0):
	return arg_12_0.getConfig("ids")

def var_0_0.HasDiscount(arg_13_0):
	local var_13_0 = arg_13_0.GetFurnitures()

	return _.any(var_13_0, function(arg_14_0)
		local var_14_0 = Furniture.New({
			id = arg_14_0
		})

		return var_14_0.getConfig("dorm_icon_price") > var_14_0.getPrice(PlayerConst.ResDormMoney))

def var_0_0.GetDiscount(arg_15_0):
	local var_15_0 = arg_15_0.GetFurnitures()
	local var_15_1 = _.map(var_15_0, function(arg_16_0)
		return Furniture.New({
			id = arg_16_0
		}))
	local var_15_2 = _.reduce(var_15_1, 0, function(arg_17_0, arg_17_1)
		return arg_17_0 + arg_17_1.getPrice(PlayerConst.ResDormMoney))
	local var_15_3 = _.reduce(var_15_1, 0, function(arg_18_0, arg_18_1)
		return arg_18_0 + arg_18_1.getConfig("dorm_icon_price"))

	return (var_15_3 - var_15_2) / var_15_3 * 100

def var_0_0.IsPurchased(arg_19_0, arg_19_1):
	for iter_19_0, iter_19_1 in ipairs(arg_19_0.getConfig("ids")):
		if not arg_19_1[iter_19_1]:
			return False

	return True

def var_0_0.GetName(arg_20_0):
	return arg_20_0.getConfig("name")

def var_0_0.GetDesc(arg_21_0):
	return arg_21_0.getConfig("desc")

def var_0_0.IsSystem(arg_22_0):
	return True

def var_0_0.getName(arg_23_0):
	return arg_23_0.GetName()

def var_0_0.getIcon(arg_24_0):
	return arg_24_0.getConfig("icon")

def var_0_0.isUnLock(arg_25_0, arg_25_1):
	return arg_25_0.getConfig("deblocking") <= arg_25_1.level

return var_0_0
