local var_0_0 = class("ChargeCommodity", import(".BaseCommodity"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.pay_data_display

def var_0_0.isChargeType(arg_2_0):
	return True

def var_0_0.canPurchase(arg_3_0):
	local var_3_0 = arg_3_0.getLimitCount()

	return var_3_0 <= 0 or var_3_0 > arg_3_0.buyCount

def var_0_0.firstPayDouble(arg_4_0):
	return arg_4_0.getConfig("first_pay_double") != 0

def var_0_0.hasExtraGem(arg_5_0):
	return arg_5_0.getConfig("extra_gem") != 0

def var_0_0.GetGemCnt(arg_6_0):
	return arg_6_0.getConfig("gem") + arg_6_0.getConfig("extra_gem")

def var_0_0.isGem(arg_7_0):
	return arg_7_0.getConfig("extra_service") == Goods.GEM

def var_0_0.isGiftBox(arg_8_0):
	return arg_8_0.getConfig("extra_service") == Goods.GIFT_BOX

def var_0_0.isMonthCard(arg_9_0):
	return arg_9_0.getConfig("extra_service") == Goods.MONTH_CARD

def var_0_0.isItemBox(arg_10_0):
	return arg_10_0.getConfig("extra_service") == Goods.ITEM_BOX

def var_0_0.isPassItem(arg_11_0):
	return arg_11_0.getConfig("extra_service") == Goods.PASS_ITEM

def var_0_0.getLimitCount(arg_12_0):
	return arg_12_0.getConfig("limit_arg")

def var_0_0.GetName(arg_13_0):
	return arg_13_0.getConfig("name")

def var_0_0.GetDropList(arg_14_0):
	local var_14_0 = arg_14_0.getConfig("display")

	if #var_14_0 == 0:
		var_14_0 = arg_14_0.getConfig("extra_service_item")

	local var_14_1 = {}

	for iter_14_0, iter_14_1 in ipairs(var_14_0):
		table.insert(var_14_1, Drop.Create(iter_14_1))

	return var_14_1

def var_0_0.GetExtraServiceItem(arg_15_0):
	local var_15_0 = {}

	if arg_15_0.isPassItem():
		local var_15_1 = arg_15_0.getConfig("sub_display")[1]
		local var_15_2 = pg.battlepass_event_pt[var_15_1].drop_client_pay

		var_15_0 = PlayerConst.MergePassItemDrop(underscore.map(var_15_2, function(arg_16_0)
			return Drop.Create(arg_16_0)))
	else
		local var_15_3 = arg_15_0.getConfig("extra_service_item")

		var_15_0 = underscore.map(var_15_3, function(arg_17_0)
			return Drop.Create(arg_17_0))

	local var_15_4 = arg_15_0.GetGemCnt()

	if not arg_15_0.isMonthCard() and var_15_4 > 0:
		table.insert(var_15_0, Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = PlayerConst.ResDiamond,
			count = var_15_4
		}))

	return var_15_0

def var_0_0.GetBonusItem(arg_18_0):
	local var_18_0

	if arg_18_0.isMonthCard():
		local var_18_1 = arg_18_0.GetGemCnt()

		var_18_0 = {
			id = 4,
			type = 1,
			count = var_18_1
		}

	return var_18_0

def var_0_0.GetChargeTip(arg_19_0):
	local var_19_0
	local var_19_1

	if arg_19_0.isPassItem():
		var_19_0 = i18n("battlepass_pay_tip")
	elif arg_19_0.isMonthCard():
		var_19_0 = i18n("charge_title_getitem_month")
		var_19_1 = i18n("charge_title_getitem_soon")
	else
		var_19_0 = i18n("charge_title_getitem")

	return var_19_0, var_19_1

def var_0_0.GetExtraDrop(arg_20_0):
	local var_20_0

	if arg_20_0.isPassItem():
		local var_20_1 = arg_20_0.getConfig("sub_display")
		local var_20_2 = var_20_1[1]
		local var_20_3 = pg.battlepass_event_pt[var_20_2].pt

		var_20_0 = Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = pg.battlepass_event_pt[var_20_2].pt,
			count = var_20_1[2]
		})

	return var_20_0

def var_0_0.getConfig(arg_21_0, arg_21_1):
	if arg_21_1 == "money" and PLATFORM_CODE == PLATFORM_CHT:
		local var_21_0 = pg.SdkMgr.GetInstance().GetProduct(arg_21_0.getConfig("id_str"))

		if var_21_0:
			return var_21_0.price
		else
			return arg_21_0.RawGetConfig(arg_21_1)
	elif arg_21_1 == "money" and PLATFORM_CODE == PLATFORM_US:
		local var_21_1 = arg_21_0.RawGetConfig(arg_21_1)

		return math.floor(var_21_1 / 100) .. "." .. var_21_1 - math.floor(var_21_1 / 100) * 100
	else
		return arg_21_0.RawGetConfig(arg_21_1)

def var_0_0.RawGetConfig(arg_22_0, arg_22_1):
	return var_0_0.super.getConfig(arg_22_0, arg_22_1)

def var_0_0.IsLocalPrice(arg_23_0):
	return arg_23_0.getConfig("money") != arg_23_0.RawGetConfig("money")

def var_0_0.isLevelLimit(arg_24_0, arg_24_1, arg_24_2):
	local var_24_0, var_24_1 = arg_24_0.getLevelLimit()

	if arg_24_2 and var_24_1:
		return False

	return var_24_0 > 0 and arg_24_1 < var_24_0

def var_0_0.getLevelLimit(arg_25_0):
	local var_25_0 = arg_25_0.getConfig("limit_args")

	for iter_25_0, iter_25_1 in ipairs(var_25_0):
		if type(iter_25_1) == "table" and iter_25_1[1] == "level":
			return iter_25_1[2], iter_25_1[3]

	return 0

def var_0_0.isTecShipGift(arg_26_0):
	if arg_26_0.getConfig("limit_type") == Goods.Tec_Ship_Gift_Type:
		return True
	else
		return False

def var_0_0.isTecShipShowGift(arg_27_0):
	if arg_27_0.isTecShipGift():
		if arg_27_0.getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.Show:
			return True
		else
			return False
	else
		return False

def var_0_0.getSameGroupTecShipGift(arg_28_0):
	local var_28_0 = {}
	local var_28_1 = arg_28_0.getConfig("limit_group")
	local var_28_2 = arg_28_0.bindConfigTable()

	for iter_28_0, iter_28_1 in ipairs(var_28_2.all):
		local var_28_3 = var_28_2[iter_28_1]

		if var_28_3.limit_type == Goods.Tec_Ship_Gift_Type and var_28_3.limit_group == var_28_1:
			local var_28_4 = Goods.Create({
				shop_id = iter_28_1
			}, Goods.TYPE_CHARGE)

			table.insert(var_28_0, var_28_4)

	return var_28_0

def var_0_0.CanViewSkinProbability(arg_29_0):
	local var_29_0 = arg_29_0.getConfig("skin_inquire_relation")

	if not var_29_0 or var_29_0 <= 0:
		return False

	if pg.gameset.package_view_display.key_value == 0:
		return False

	return True

def var_0_0.GetSkinProbability(arg_30_0):
	local var_30_0 = {}

	if arg_30_0.CanViewSkinProbability():
		local var_30_1 = arg_30_0.getConfig("skin_inquire_relation")

		var_30_0 = Item.getConfigData(var_30_1).combination_display

	return var_30_0

def var_0_0.GetSkinProbabilityItem(arg_31_0):
	if not arg_31_0.CanViewSkinProbability():
		return None

	local var_31_0 = arg_31_0.getConfig("skin_inquire_relation")

	return {
		count = 1,
		type = DROP_TYPE_ITEM,
		id = var_31_0
	}

def var_0_0.GetDropItem(arg_32_0):
	local var_32_0 = arg_32_0.getConfig("drop_item")

	if #var_32_0 > 0:
		return var_32_0
	else
		assert(False, "should exist drop item")

def var_0_0.GetLimitDesc(arg_33_0):
	local var_33_0 = arg_33_0.getLimitCount()
	local var_33_1 = arg_33_0.buyCount or 0

	if var_33_0 > 0:
		return i18n("charge_limit_all", var_33_0 - var_33_1, var_33_0)

	local var_33_2 = arg_33_0.getConfig("group_limit")

	if var_33_2 > 0:
		local var_33_3 = arg_33_0.getConfig("group_type") or 0

		if var_33_3 == 1:
			return i18n("charge_limit_daily", var_33_2 - arg_33_0.groupCount, var_33_2)
		elif var_33_3 == 2:
			return i18n("charge_limit_weekly", var_33_2 - arg_33_0.groupCount, var_33_2)
		elif var_33_3 == 3:
			return i18n("charge_limit_monthly", var_33_2 - arg_33_0.groupCount, var_33_2)

	return ""

return var_0_0
