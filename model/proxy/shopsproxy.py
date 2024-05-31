local var_0_0 = class("ShopsProxy", import(".NetProxy"))

var_0_0.MERITOROUS_SHOP_UPDATED = "ShopsProxy.MERITOROUS_SHOP_UPDATED"
var_0_0.SHOPPINGSTREET_UPDATE = "ShopsProxy.SHOPPINGSTREET_UPDATE"
var_0_0.FIRST_CHARGE_IDS_UPDATED = "ShopsProxy.FIRST_CHARGE_IDS_UPDATED"
var_0_0.CHARGED_LIST_UPDATED = "ShopsProxy.CHARGED_LIST_UPDATED"
var_0_0.NORMAL_LIST_UPDATED = "ShopsProxy.NORMAL_LIST_UPDATED"
var_0_0.NORMAL_GROUP_LIST_UPDATED = "ShopsProxy.NORMAL_GROUP_LIST_UPDATED"
var_0_0.ACTIVITY_SHOP_UPDATED = "ShopsProxy.ACTIVITY_SHOP_UPDATED"
var_0_0.GUILD_SHOP_ADDED = "ShopsProxy.GUILD_SHOP_ADDED"
var_0_0.GUILD_SHOP_UPDATED = "ShopsProxy.GUILD_SHOP_UPDATED"
var_0_0.ACTIVITY_SHOPS_UPDATED = "ShopsProxy.ACTIVITY_SHOPS_UPDATED"
var_0_0.SHAM_SHOP_UPDATED = "ShopsProxy.SHAM_SHOP_UPDATED"
var_0_0.FRAGMENT_SHOP_UPDATED = "ShopsProxy.FRAGMENT_SHOP_UPDATED"
var_0_0.ACTIVITY_SHOP_GOODS_UPDATED = "ShopsProxy.ACTIVITY_SHOP_GOODS_UPDATED"
var_0_0.META_SHOP_GOODS_UPDATED = "ShopsProxy.META_SHOP_GOODS_UPDATED"
var_0_0.MEDAL_SHOP_UPDATED = "ShopsProxy.MEDAL_SHOP_UPDATED"
var_0_0.QUOTA_SHOP_UPDATED = "ShopsProxy.QUOTA_SHOP_UPDATED"

def var_0_0.register(arg_1_0):
	arg_1_0.shopStreet = None
	arg_1_0.meritorousShop = None
	arg_1_0.guildShop = None
	arg_1_0.refreshChargeList = False
	arg_1_0.metaShop = None
	arg_1_0.miniShop = None

	arg_1_0.on(22102, function(arg_2_0)
		local var_2_0 = getProxy(ShopsProxy)
		local var_2_1 = ShoppingStreet.New(arg_2_0.street)

		var_2_0.setShopStreet(var_2_1))

	arg_1_0.shamShop = ShamBattleShop.New()
	arg_1_0.fragmentShop = FragmentShop.New()

	arg_1_0.on(16200, function(arg_3_0)
		arg_1_0.shamShop.update(arg_3_0.month, arg_3_0.core_shop_list)
		arg_1_0.fragmentShop.update(arg_3_0.month, arg_3_0.blue_shop_list, arg_3_0.normal_shop_list))

	arg_1_0.timers = {}
	arg_1_0.tradeNoPrev = ""

	local var_1_0 = pg.shop_template

	arg_1_0.freeGiftIdList = {}

	for iter_1_0, iter_1_1 in pairs(var_1_0.all):
		if var_1_0[iter_1_1].genre == "gift_package" and var_1_0[iter_1_1].discount == 100:
			table.insert(arg_1_0.freeGiftIdList, iter_1_1)

def var_0_0.setShopStreet(arg_4_0, arg_4_1):
	arg_4_0.shopStreet = arg_4_1

	arg_4_0.sendNotification(var_0_0.SHOPPINGSTREET_UPDATE, {
		shopStreet = Clone(arg_4_0.shopStreet)
	})

def var_0_0.UpdateShopStreet(arg_5_0, arg_5_1):
	arg_5_0.shopStreet = arg_5_1

def var_0_0.getShopStreet(arg_6_0):
	return Clone(arg_6_0.shopStreet)

def var_0_0.getMeritorousShop(arg_7_0):
	return Clone(arg_7_0.meritorousShop)

def var_0_0.addMeritorousShop(arg_8_0, arg_8_1):
	arg_8_0.meritorousShop = arg_8_1

	arg_8_0.sendNotification(var_0_0.MERITOROUS_SHOP_UPDATED, Clone(arg_8_1))

def var_0_0.updateMeritorousShop(arg_9_0, arg_9_1):
	arg_9_0.meritorousShop = arg_9_1

def var_0_0.getMiniShop(arg_10_0):
	return Clone(arg_10_0.miniShop)

def var_0_0.setMiniShop(arg_11_0, arg_11_1):
	arg_11_0.miniShop = arg_11_1

def var_0_0.setNormalList(arg_12_0, arg_12_1):
	arg_12_0.normalList = arg_12_1 or {}

def var_0_0.GetNormalList(arg_13_0):
	return Clone(arg_13_0.normalList)

def var_0_0.GetNormalByID(arg_14_0, arg_14_1):
	if not arg_14_0.normalList:
		arg_14_0.normalList = {}

	local var_14_0 = arg_14_0.normalList[arg_14_1] or Goods.Create({
		buyCount = 0,
		id = arg_14_1
	}, Goods.TYPE_GIFT_PACKAGE)

	arg_14_0.normalList[arg_14_1] = var_14_0

	return arg_14_0.normalList[arg_14_1]

def var_0_0.updateNormalByID(arg_15_0, arg_15_1):
	arg_15_0.normalList[arg_15_1.id] = arg_15_1

def var_0_0.checkHasFreeNormal(arg_16_0):
	for iter_16_0, iter_16_1 in ipairs(arg_16_0.freeGiftIdList):
		if arg_16_0.checkNormalCanPurchase(iter_16_1):
			return True

	return False

def var_0_0.checkNormalCanPurchase(arg_17_0, arg_17_1):
	if arg_17_0.normalList[arg_17_1] != None:
		local var_17_0 = arg_17_0.normalList[arg_17_1]

		if not var_17_0.inTime():
			return False

		local var_17_1 = var_17_0.getConfig("group") or 0

		if var_17_1 > 0:
			local var_17_2 = var_17_0.getConfig("group_limit")
			local var_17_3 = arg_17_0.getGroupLimit(var_17_1)

			return var_17_2 > 0 and var_17_3 < var_17_2
		elif var_17_0.canPurchase():
			return True
	else
		return arg_17_0.GetNormalByID(arg_17_1).inTime()

def var_0_0.setNormalGroupList(arg_18_0, arg_18_1):
	arg_18_0.normalGroupList = arg_18_1

def var_0_0.GetNormalGroupList(arg_19_0):
	return arg_19_0.normalGroupList

def var_0_0.updateNormalGroupList(arg_20_0, arg_20_1, arg_20_2):
	if arg_20_1 <= 0:
		return

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.normalGroupList):
		if iter_20_1.shop_id == arg_20_1:
			local var_20_0 = arg_20_0.normalGroupList[iter_20_0].pay_count or 0

			arg_20_0.normalGroupList[iter_20_0].pay_count = var_20_0 + arg_20_2

			return

	table.insert(arg_20_0.normalGroupList, {
		shop_id = arg_20_1,
		pay_count = arg_20_2
	})

def var_0_0.getGroupLimit(arg_21_0, arg_21_1):
	if not arg_21_0.normalGroupList:
		return 0

	for iter_21_0, iter_21_1 in ipairs(arg_21_0.normalGroupList):
		if iter_21_1.shop_id == arg_21_1:
			return iter_21_1.pay_count

	return 0

def var_0_0.addActivityShops(arg_22_0, arg_22_1):
	arg_22_0.activityShops = arg_22_1

	arg_22_0.sendNotification(var_0_0.ACTIVITY_SHOPS_UPDATED)

def var_0_0.getActivityShopById(arg_23_0, arg_23_1):
	assert(arg_23_0.activityShops[arg_23_1], "activity shop should exist" .. arg_23_1)

	return arg_23_0.activityShops[arg_23_1]

def var_0_0.updateActivityShop(arg_24_0, arg_24_1, arg_24_2):
	assert(arg_24_0.activityShops, "activityShops can not be None")

	arg_24_0.activityShops[arg_24_1] = arg_24_2

	arg_24_0.sendNotification(var_0_0.ACTIVITY_SHOP_UPDATED, {
		activityId = arg_24_1,
		shop = arg_24_2.clone()
	})

def var_0_0.UpdateActivityGoods(arg_25_0, arg_25_1, arg_25_2, arg_25_3):
	local var_25_0 = arg_25_0.getActivityShopById(arg_25_1)

	var_25_0.getGoodsById(arg_25_2).addBuyCount(arg_25_3)

	arg_25_0.activityShops[arg_25_1] = var_25_0

	arg_25_0.sendNotification(var_0_0.ACTIVITY_SHOP_GOODS_UPDATED, {
		activityId = arg_25_1,
		goodsId = arg_25_2
	})

def var_0_0.getActivityShops(arg_26_0):
	return arg_26_0.activityShops

def var_0_0.setFirstChargeList(arg_27_0, arg_27_1):
	arg_27_0.firstChargeList = arg_27_1

	arg_27_0.sendNotification(var_0_0.FIRST_CHARGE_IDS_UPDATED, Clone(arg_27_1))

def var_0_0.getFirstChargeList(arg_28_0):
	return Clone(arg_28_0.firstChargeList)

def var_0_0.setChargedList(arg_29_0, arg_29_1):
	arg_29_0.chargeList = arg_29_1

	arg_29_0.sendNotification(var_0_0.CHARGED_LIST_UPDATED, Clone(arg_29_1))

def var_0_0.getChargedList(arg_30_0):
	return Clone(arg_30_0.chargeList)

local var_0_1 = 3
local var_0_2 = 10

def var_0_0.chargeFailed(arg_31_0, arg_31_1, arg_31_2):
	if not arg_31_0.timers[arg_31_1]:
		pg.UIMgr.GetInstance().LoadingOn()

		arg_31_0.timers[arg_31_1] = Timer.New(function()
			if arg_31_0.timers[arg_31_1].loop == 1:
				pg.UIMgr.GetInstance().LoadingOff()

			PaySuccess(arg_31_1, arg_31_2), var_0_1, var_0_2)

		arg_31_0.timers[arg_31_1].Start()

def var_0_0.removeChargeTimer(arg_33_0, arg_33_1):
	if arg_33_0.timers[arg_33_1]:
		pg.UIMgr.GetInstance().LoadingOff()
		arg_33_0.timers[arg_33_1].Stop()

		arg_33_0.timers[arg_33_1] = None

def var_0_0.addWaitTimer(arg_34_0):
	pg.UIMgr.GetInstance().LoadingOn()

	arg_34_0.waitBiliTimer = Timer.New(function()
		arg_34_0.removeWaitTimer()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			content = i18n("charge_time_out")
		}), 25, 1)

	arg_34_0.waitBiliTimer.Start()

def var_0_0.removeWaitTimer(arg_36_0):
	if arg_36_0.waitBiliTimer:
		pg.UIMgr.GetInstance().LoadingOff()
		arg_36_0.waitBiliTimer.Stop()

		arg_36_0.waitBiliTimer = None

def var_0_0.setGuildShop(arg_37_0, arg_37_1):
	assert(isa(arg_37_1, GuildShop), "shop should instance of GuildShop")
	assert(arg_37_0.guildShop == None, "shop already exist")

	arg_37_0.guildShop = arg_37_1

	arg_37_0.sendNotification(var_0_0.GUILD_SHOP_ADDED, arg_37_0.guildShop)

def var_0_0.getGuildShop(arg_38_0):
	return arg_38_0.guildShop

def var_0_0.updateGuildShop(arg_39_0, arg_39_1, arg_39_2):
	assert(isa(arg_39_1, GuildShop), "shop should instance of GuildShop")
	assert(arg_39_0.guildShop, "should exist shop")

	arg_39_0.guildShop = arg_39_1

	arg_39_0.sendNotification(var_0_0.GUILD_SHOP_UPDATED, {
		shop = arg_39_0.guildShop,
		reset = arg_39_2
	})

def var_0_0.AddShamShop(arg_40_0, arg_40_1):
	arg_40_0.shamShop = arg_40_1

	arg_40_0.sendNotification(var_0_0.SHAM_SHOP_UPDATED, arg_40_1)

def var_0_0.updateShamShop(arg_41_0, arg_41_1):
	arg_41_0.shamShop = arg_41_1

def var_0_0.getShamShop(arg_42_0):
	return arg_42_0.shamShop

def var_0_0.AddFragmentShop(arg_43_0, arg_43_1):
	arg_43_0.fragmentShop = arg_43_1

	arg_43_0.sendNotification(var_0_0.FRAGMENT_SHOP_UPDATED, arg_43_1)

def var_0_0.updateFragmentShop(arg_44_0, arg_44_1):
	arg_44_0.fragmentShop = arg_44_1

def var_0_0.getFragmentShop(arg_45_0):
	return arg_45_0.fragmentShop

def var_0_0.AddMetaShop(arg_46_0, arg_46_1):
	arg_46_0.metaShop = arg_46_1

def var_0_0.GetMetaShop(arg_47_0):
	return arg_47_0.metaShop

def var_0_0.UpdateMetaShopGoods(arg_48_0, arg_48_1, arg_48_2):
	arg_48_0.GetMetaShop().getGoodsById(arg_48_1).addBuyCount(arg_48_2)
	arg_48_0.sendNotification(var_0_0.META_SHOP_GOODS_UPDATED, {
		goodsId = arg_48_1
	})

def var_0_0.SetNewServerShop(arg_49_0, arg_49_1):
	arg_49_0.newServerShop = arg_49_1

def var_0_0.GetNewServerShop(arg_50_0):
	return arg_50_0.newServerShop

def var_0_0.SetMedalShop(arg_51_0, arg_51_1):
	arg_51_0.medalShop = arg_51_1

def var_0_0.UpdateMedalShop(arg_52_0, arg_52_1):
	arg_52_0.medalShop = arg_52_1

	arg_52_0.sendNotification(var_0_0.MEDAL_SHOP_UPDATED, arg_52_1)

def var_0_0.GetMedalShop(arg_53_0):
	return arg_53_0.medalShop

def var_0_0.setQuotaShop(arg_54_0, arg_54_1):
	arg_54_0.quotaShop = arg_54_1

def var_0_0.getQuotaShop(arg_55_0):
	return arg_55_0.quotaShop

def var_0_0.updateQuotaShop(arg_56_0, arg_56_1, arg_56_2):
	arg_56_0.quotaShop = arg_56_1

	arg_56_0.sendNotification(var_0_0.QUOTA_SHOP_UPDATED, {
		shop = arg_56_0.quotaShop,
		reset = arg_56_2
	})

def var_0_0.remove(arg_57_0):
	for iter_57_0, iter_57_1 in pairs(arg_57_0.timers):
		iter_57_1.Stop()

	arg_57_0.timers = None

	arg_57_0.removeWaitTimer()

def var_0_0.ShouldRefreshChargeList(arg_58_0):
	local var_58_0 = arg_58_0.getFirstChargeList()
	local var_58_1 = arg_58_0.getChargedList()
	local var_58_2 = arg_58_0.GetNormalList()
	local var_58_3 = arg_58_0.GetNormalGroupList()

	return not var_58_0 or not var_58_1 or not var_58_2 or not var_58_3 or arg_58_0.refreshChargeList

def var_0_0.GetRecommendCommodities(arg_59_0):
	local var_59_0 = arg_59_0.getChargedList()
	local var_59_1 = arg_59_0.GetNormalList()
	local var_59_2 = arg_59_0.GetNormalGroupList()

	if not var_59_0 or not var_59_1 or not var_59_2:
		return {}

	local var_59_3 = {}

	for iter_59_0, iter_59_1 in ipairs(pg.recommend_shop.all):
		local var_59_4 = pg.recommend_shop[iter_59_1].time

		if pg.TimeMgr.GetInstance().inTime(var_59_4):
			local var_59_5 = RecommendCommodity.New({
				id = iter_59_1,
				chargedList = var_59_0,
				normalList = var_59_1,
				normalGroupList = var_59_2
			})

			if var_59_5.CanShow():
				table.insert(var_59_3, var_59_5)

	table.sort(var_59_3, function(arg_60_0, arg_60_1)
		return arg_60_0.GetOrder() < arg_60_1.GetOrder())

	return var_59_3

def var_0_0.GetGiftCommodity(arg_61_0, arg_61_1, arg_61_2):
	local var_61_0 = Goods.Create({
		shop_id = arg_61_1
	}, arg_61_2)

	if var_61_0.isChargeType():
		local var_61_1 = ChargeConst.getBuyCount(arg_61_0.chargeList, var_61_0.id)

		var_61_0.updateBuyCount(var_61_1)
	else
		local var_61_2 = ChargeConst.getBuyCount(arg_61_0.normalList, var_61_0.id)

		var_61_0.updateBuyCount(var_61_2)

		local var_61_3 = var_61_0.getConfig("group") or 0

		if var_61_3 > 0:
			local var_61_4 = ChargeConst.getGroupLimit(arg_61_0.normalGroupList, var_61_3)

			var_61_0.updateGroupCount(var_61_4)

	return var_61_0

return var_0_0
