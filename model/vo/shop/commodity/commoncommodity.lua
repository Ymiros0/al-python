﻿local var_0_0 = class("CommonCommodity", import(".BaseCommodity"))

function var_0_0.InCommodityDiscountTime(arg_1_0)
	local var_1_0 = pg.shop_template[arg_1_0].discount_time

	if var_1_0 == "always" then
		return true
	end

	if type(var_1_0) == "table" then
		return table.getCount(var_1_0) == 0 or pg.TimeMgr.GetInstance():inTime(var_1_0)
	end

	return false
end

function var_0_0.bindConfigTable(arg_2_0)
	return pg.shop_template
end

function var_0_0.canPurchase(arg_3_0)
	if arg_3_0.type == Goods.TYPE_MILITARY then
		return arg_3_0.buyCount == 0
	elseif arg_3_0.type == Goods.TYPE_GIFT_PACKAGE or arg_3_0.type == Goods.TYPE_SKIN or arg_3_0.type == Goods.TYPE_WORLD or arg_3_0.type == Goods.TYPE_NEW_SERVER then
		local var_3_0 = arg_3_0:getLimitCount()

		return var_3_0 <= 0 or var_3_0 > arg_3_0.buyCount
	else
		return var_0_0.super.canPurchase(arg_3_0)
	end
end

function var_0_0.isDisCount(arg_4_0)
	local var_4_0 = var_0_0.InCommodityDiscountTime(arg_4_0.id)

	if arg_4_0:IsItemDiscountType() then
		return true
	else
		return arg_4_0:getConfig("discount") ~= 0 and var_4_0
	end
end

function var_0_0.GetDiscountEndTime(arg_5_0)
	local var_5_0 = arg_5_0:getConfig("discount_time")
	local var_5_1, var_5_2 = unpack(var_5_0)
	local var_5_3 = var_5_2[1]
	local var_5_4, var_5_5, var_5_6 = unpack(var_5_3)

	return (pg.TimeMgr.GetInstance():Table2ServerTime({
		year = var_5_4,
		month = var_5_5,
		day = var_5_6,
		hour = var_5_2[2][1],
		min = var_5_2[2][2],
		sec = var_5_2[2][3]
	}))
end

function var_0_0.IsGroupSale(arg_6_0)
	local var_6_0 = arg_6_0:getConfig("group") > 0
	local var_6_1 = arg_6_0:getConfig("limit_args2")[1]

	return arg_6_0.type == Goods.TYPE_MILITARY and var_6_0 and var_6_1[1] == "purchase"
end

function var_0_0.IsShowWhenGroupSale(arg_7_0, arg_7_1)
	if arg_7_0:IsGroupSale() then
		local var_7_0 = arg_7_0:getConfig("limit_args2")[1]
		local var_7_1 = var_7_0[2]
		local var_7_2 = var_7_0[3]

		if arg_7_1 == var_7_2 and var_7_2 == arg_7_0:getConfig("group_limit") then
			return true
		end

		arg_7_1 = arg_7_1 + 1

		return var_7_1 <= arg_7_1 and arg_7_1 <= var_7_2
	end

	return true
end

function var_0_0.GetPrice(arg_8_0)
	local var_8_0 = 0
	local var_8_1 = arg_8_0:getConfig("resource_num")
	local var_8_2 = arg_8_0:isDisCount()

	if var_8_2 and arg_8_0:IsItemDiscountType() then
		local var_8_3 = SkinCouponActivity.StaticGetNewPrice(var_8_1)

		var_8_0 = (var_8_1 - var_8_3) / var_8_1 * 100
		var_8_1 = var_8_3
	elseif var_8_2 then
		var_8_0 = arg_8_0:getConfig("discount")
		var_8_1 = (100 - var_8_0) / 100 * var_8_1
	end

	return var_8_1, var_8_0
end

function var_0_0.GetBasePrice(arg_9_0)
	return arg_9_0:getConfig("resource_num")
end

function var_0_0.GetName(arg_10_0)
	return arg_10_0:getDropInfo():getName()
end

function var_0_0.GetResType(arg_11_0)
	return arg_11_0:getConfig("resource_type")
end

function var_0_0.IsItemDiscountType(arg_12_0)
	return arg_12_0:getConfig("genre") == ShopArgs.SkinShop and SkinCouponActivity.StaticCanUsageSkinCoupon(arg_12_0.id)
end

function var_0_0.CanUseVoucherType(arg_13_0)
	local var_13_0 = getProxy(BagProxy):GetSkinShopDiscountItemList()

	return arg_13_0:StaticCanUseVoucherType(var_13_0)
end

function var_0_0.StaticCanUseVoucherType(arg_14_0, arg_14_1)
	if #arg_14_1 <= 0 then
		return false
	end

	for iter_14_0, iter_14_1 in ipairs(arg_14_1) do
		if iter_14_1:CanUseForShop(arg_14_0.id) then
			return true
		end
	end

	return false
end

function var_0_0.GetVoucherIdList(arg_15_0)
	local var_15_0 = {}
	local var_15_1 = getProxy(BagProxy):GetSkinShopDiscountItemList()

	for iter_15_0, iter_15_1 in pairs(var_15_1) do
		if iter_15_1:CanUseForShop(arg_15_0.id) then
			table.insert(var_15_0, iter_15_1.id)
		end
	end

	return var_15_0
end

function var_0_0.getLimitCount(arg_16_0)
	local var_16_0 = arg_16_0:getConfig("limit_args") or {}

	for iter_16_0, iter_16_1 in ipairs(var_16_0) do
		if iter_16_1[1] == "time" then
			return iter_16_1[2]
		end
	end

	return 0
end

function var_0_0.GetDiscountItem(arg_17_0)
	if arg_17_0:IsItemDiscountType() then
		return SkinCouponActivity.StaticGetItemConfig()
	end

	return nil
end

function var_0_0.isLevelLimit(arg_18_0, arg_18_1, arg_18_2)
	local var_18_0, var_18_1 = arg_18_0:getLevelLimit()

	if arg_18_2 and var_18_1 then
		return false
	end

	return var_18_0 > 0 and arg_18_1 < var_18_0
end

function var_0_0.getLevelLimit(arg_19_0)
	local var_19_0 = arg_19_0:getConfig("limit_args")

	for iter_19_0, iter_19_1 in ipairs(var_19_0) do
		if type(iter_19_1) == "table" and iter_19_1[1] == "level" then
			return iter_19_1[2], iter_19_1[3]
		end
	end

	return 0
end

function var_0_0.isTimeLimit(arg_20_0)
	local var_20_0 = arg_20_0:getLimitCount()

	return var_20_0 <= 0 or var_20_0 < arg_20_0.buyCount
end

function var_0_0.getSkinId(arg_21_0)
	if arg_21_0.type == Goods.TYPE_SKIN then
		return arg_21_0:getConfig("effect_args")[1]
	end

	assert(false)
end

function var_0_0.getDropInfo(arg_22_0)
	local var_22_0 = switch(arg_22_0:getConfig("effect_args"), {
		ship_bag_size = function()
			return {
				count = 1,
				type = DROP_TYPE_ITEM,
				id = Goods.SHIP_BAG_SIZE_ITEM
			}
		end,
		equip_bag_size = function()
			return {
				count = 1,
				type = DROP_TYPE_ITEM,
				id = Goods.EQUIP_BAG_SIZE_ITEM
			}
		end,
		commander_bag_size = function()
			return {
				count = 1,
				type = DROP_TYPE_ITEM,
				id = Goods.COMMANDER_BAG_SIZE_ITEM
			}
		end,
		spweapon_bag_size = function()
			return {
				count = 1,
				type = DROP_TYPE_ITEM,
				id = Goods.SPWEAPON_BAG_SIZE_ITEM
			}
		end,
		ship_bag_size = function()
			return {
				count = 1,
				type = DROP_TYPE_ITEM,
				id = Goods.SHIP_BAG_SIZE_ITEM
			}
		end,
		ship_bag_size = function()
			return {
				count = 1,
				type = DROP_TYPE_ITEM,
				id = Goods.SHIP_BAG_SIZE_ITEM
			}
		end
	}, function()
		if arg_22_0:getConfig("genre") == ShopArgs.WorldCollection then
			return {
				type = DROP_TYPE_WORLD_ITEM,
				id = arg_22_0:getConfig("effect_args")[1],
				count = arg_22_0:getConfig("num")
			}
		else
			return {
				type = arg_22_0:getConfig("type"),
				id = arg_22_0:getConfig("effect_args")[1],
				count = arg_22_0:getConfig("num")
			}
		end
	end)

	return Drop.New(var_22_0)
end

function var_0_0.GetDropList(arg_30_0)
	local var_30_0 = {}
	local var_30_1 = Item.getConfigData(arg_30_0:getConfig("effect_args")[1]).display_icon

	if type(var_30_1) == "table" then
		for iter_30_0, iter_30_1 in ipairs(var_30_1) do
			table.insert(var_30_0, {
				type = iter_30_1[1],
				id = iter_30_1[2],
				count = iter_30_1[3]
			})
		end
	end

	return var_30_0
end

function var_0_0.IsGroupLimit(arg_31_0)
	if arg_31_0:getConfig("group") <= 0 then
		return false
	end

	local var_31_0 = arg_31_0:getConfig("group_limit")

	return var_31_0 > 0 and var_31_0 <= (arg_31_0.groupCount or 0)
end

function var_0_0.GetLimitDesc(arg_32_0)
	local var_32_0 = arg_32_0:getLimitCount()
	local var_32_1 = arg_32_0.buyCount or 0

	if var_32_0 > 0 then
		return i18n("charge_limit_all", var_32_0 - var_32_1, var_32_0)
	end

	local var_32_2 = arg_32_0:getConfig("group_limit")

	if var_32_2 > 0 then
		local var_32_3 = arg_32_0:getConfig("group_type") or 0

		if var_32_3 == 1 then
			return i18n("charge_limit_daily", var_32_2 - arg_32_0.groupCount, var_32_2)
		elseif var_32_3 == 2 then
			return i18n("charge_limit_weekly", var_32_2 - arg_32_0.groupCount, var_32_2)
		elseif var_32_3 == 3 then
			return i18n("charge_limit_monthly", var_32_2 - arg_32_0.groupCount, var_32_2)
		end
	end

	return ""
end

function var_0_0.GetGiftList(arg_33_0)
	if arg_33_0:getConfig("genre") == ShopArgs.SkinShop then
		local var_33_0 = arg_33_0:getSkinId()

		return ShipSkin.New({
			id = var_33_0
		}):GetRewardList()
	else
		return var_0_0.super.GetGiftList(arg_33_0)
	end
end

return var_0_0
