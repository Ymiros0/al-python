local var_0_0 = class("ActivityCommodity", import(".BaseCommodity"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.activity_shop_template

def var_0_0.CheckCntLimit(arg_2_0):
	if arg_2_0.getConfig("num_limit") == 0:
		return True

	return arg_2_0.GetPurchasableCnt() > 0

def var_0_0.CheckArgLimit(arg_3_0):
	local var_3_0 = arg_3_0.getConfig("limit_args")

	if not var_3_0 or var_3_0 == "" or #var_3_0 == 0:
		return True

	local var_3_1 = False

	for iter_3_0, iter_3_1 in ipairs(var_3_0):
		local var_3_2 = iter_3_1[1]
		local var_3_3 = iter_3_1[2]
		local var_3_4 = iter_3_1[3]

		if (var_3_2 == ShopArgs.LIMIT_ARGS_META_SHIP_EXISTENCE or var_3_2 == ShopArgs.LIMIT_ARGS_TRAN_ITEM_WHEN_FULL) and (var_3_4 or 1) == 1:
			var_3_1 = getProxy(BayProxy).getMetaShipByGroupId(var_3_3) != None

			if not var_3_1:
				return var_3_1, var_3_2, i18n("meta_shop_exchange_limit"), var_3_3
		elif var_3_2 == ShopArgs.LIMIT_ARGS_SALE_START_TIME:
			var_3_1 = pg.TimeMgr.GetInstance().passTime(var_3_3)

			if not var_3_1:
				return var_3_1, var_3_2, i18n("meta_shop_exchange_limit_2"), var_3_3
		elif var_3_2 == "pass":
			local var_3_5 = getProxy(ChapterProxy).getChapterById(var_3_3)

			var_3_1 = var_3_5 and var_3_5.isClear()

			if not var_3_1:
				return var_3_1, var_3_2, var_3_4, var_3_3

	return var_3_1

local function var_0_1(arg_4_0, arg_4_1)
	local var_4_0 = getProxy(BayProxy).getMetaShipByGroupId(arg_4_1)

	if var_4_0:
		local var_4_1 = var_4_0.getMetaCharacter().getSpecialMaterialInfoToMaxStar()
		local var_4_2 = getProxy(BagProxy).getItemCountById(var_4_1.itemID)

		print(var_4_1, var_4_2)

		return math.max(var_4_1.count - var_4_2, 0)
	else
		return arg_4_0.getConfig("num_limit") - arg_4_0.buyCount

	return 0

def var_0_0.GetTranCntWhenFull(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0.getConfig("limit_args")
	local var_5_1 = 0
	local var_5_2

	if not var_5_0 or var_5_0 == "" or #var_5_0 == 0:
		-- block empty
	else
		for iter_5_0, iter_5_1 in ipairs(var_5_0):
			local var_5_3 = iter_5_1[1]
			local var_5_4 = iter_5_1[2]
			local var_5_5 = iter_5_1[3]
			local var_5_6 = iter_5_1[4]

			if var_5_3 == ShopArgs.LIMIT_ARGS_TRAN_ITEM_WHEN_FULL:
				local var_5_7 = var_0_1(arg_5_0, var_5_4) - arg_5_1

				if var_5_7 < 0:
					var_5_1 = math.abs(var_5_7)
					var_5_2 = Drop.Create(var_5_6)

	return var_5_1, var_5_2

def var_0_0.CheckTimeLimit(arg_6_0):
	local var_6_0 = False
	local var_6_1 = False
	local var_6_2 = False
	local var_6_3 = arg_6_0.getConfig("commodity_type")
	local var_6_4 = arg_6_0.getConfig("commodity_id")
	local var_6_5 = Item.getConfigData(var_6_4)

	if var_6_3 == DROP_TYPE_VITEM and var_6_5.virtual_type == 22:
		var_6_0 = True
		var_6_2 = True

		local var_6_6 = getProxy(ActivityProxy).getActivityById(var_6_5.link_id)

		if var_6_6 and not var_6_6.isEnd():
			var_6_1 = True
	elif var_6_3 == DROP_TYPE_ITEM and var_6_5.time_limit == 1:
		var_6_0 = False
		var_6_1 = True

	return var_6_0, var_6_1, var_6_2

def var_0_0.canPurchase(arg_7_0):
	local var_7_0, var_7_1, var_7_2 = arg_7_0.CheckCntLimit()
	local var_7_3, var_7_4, var_7_5 = arg_7_0.CheckArgLimit()

	if not var_7_0:
		return False, var_7_1, var_7_2

	if not var_7_3:
		return False, var_7_4, var_7_5

	return True

def var_0_0.getSkinId(arg_8_0):
	if arg_8_0.getConfig("commodity_type") == DROP_TYPE_SKIN:
		return arg_8_0.getConfig("commodity_id")

	return None

def var_0_0.checkCommodityType(arg_9_0, arg_9_1):
	return arg_9_0.getConfig("commodity_type") == arg_9_1

def var_0_0.GetPurchasableCnt(arg_10_0):
	local var_10_0 = arg_10_0.getConfig("commodity_type")
	local var_10_1 = arg_10_0.getConfig("commodity_id")

	if var_10_0 == DROP_TYPE_SKIN:
		return getProxy(ShipSkinProxy).hasSkin(var_10_1) and 0 or 1
	elif var_10_0 == DROP_TYPE_FURNITURE:
		local var_10_2 = getProxy(DormProxy).getRawData().GetOwnFurnitureCount(var_10_1)
		local var_10_3 = pg.furniture_data_template[var_10_1]

		return math.min(var_10_3.count - var_10_2, arg_10_0.getConfig("num_limit") - arg_10_0.buyCount)
	else
		local var_10_4 = arg_10_0.getConfig("limit_args")
		local var_10_5

		if type(var_10_4) == "table":
			var_10_5 = _.detect(var_10_4, function(arg_11_0)
				return arg_11_0[1] == ShopArgs.LIMIT_ARGS_META_SHIP_EXISTENCE)

		if var_10_5:
			return var_0_1(arg_10_0, var_10_5[2])
		else
			return arg_10_0.getConfig("num_limit") - arg_10_0.buyCount

def var_0_0.GetConsume(arg_12_0):
	return Drop.New({
		type = arg_12_0.getConfig("resource_category"),
		id = arg_12_0.getConfig("resource_type"),
		count = arg_12_0.getConfig("resource_num")
	})

return var_0_0
