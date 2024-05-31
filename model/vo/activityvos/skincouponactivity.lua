local var_0_0 = class("SkinCouponActivity", import("model.vo.Activity"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.dataConfig = pg.activity_event_shop_discount[arg_1_0.configId]
end

function var_0_0.GetDiscountPrice(arg_2_0)
	return arg_2_0.dataConfig.discount_price
end

function var_0_0.GetNewPrice(arg_3_0, arg_3_1)
	return arg_3_1 - arg_3_0:GetDiscountPrice()
end

function var_0_0.GetShopIdList(arg_4_0)
	return arg_4_0.dataConfig.shop_list
end

function var_0_0.Left3Day(arg_5_0)
	if arg_5_0.stopTime - pg.TimeMgr.GetInstance():GetServerTime() < 259200 then
		return true
	end

	return false
end

function var_0_0.ShouldTipUsage(arg_6_0)
	local function var_6_0()
		local var_7_0 = getProxy(PlayerProxy):getRawData().id
		local var_7_1 = PlayerPrefs.GetInt(arg_6_0.id .. "_SkinCouponActivity_Tip" .. var_7_0, 0)

		if var_7_1 <= 0 then
			return true
		end

		local var_7_2 = pg.TimeMgr.GetInstance():GetServerTime()

		return var_7_1 < var_7_2 and not pg.TimeMgr.GetInstance():IsSameDay(var_7_2, var_7_1)
	end

	return arg_6_0:GetCanUsageCnt() > 0 and arg_6_0:Left3Day() and var_6_0()
end

function var_0_0.SaveTipTime(arg_8_0)
	local var_8_0 = pg.TimeMgr.GetInstance():GetServerTime()
	local var_8_1 = getProxy(PlayerProxy):getRawData().id

	PlayerPrefs.SetInt(arg_8_0.id .. "_SkinCouponActivity_Tip" .. var_8_1, var_8_0)
	PlayerPrefs.Save()
end

function var_0_0.IncludeShop(arg_9_0, arg_9_1)
	local var_9_0 = arg_9_0:GetShopIdList()

	return table.contains(var_9_0, arg_9_1)
end

function var_0_0.GetCanUsageCnt(arg_10_0)
	return arg_10_0.data1 - arg_10_0.data2
end

function var_0_0.CanUsageSkinCoupon(arg_11_0, arg_11_1)
	return arg_11_0:IncludeShop(arg_11_1) and arg_11_0:GetCanUsageCnt() > 0
end

function var_0_0.GetEquivalentRes(arg_12_0)
	if arg_12_0.dataConfig.change_resource_type == 0 or arg_12_0.dataConfig.change_resource_num == 0 then
		return nil
	end

	local var_12_0 = Drop.New({
		type = DROP_TYPE_RESOURCE,
		id = arg_12_0.dataConfig.change_resource_type,
		count = arg_12_0.dataConfig.change_resource_num
	})

	var_12_0.name = var_12_0:getName()
end

function var_0_0.GetLimitCnt(arg_13_0)
	if arg_13_0.dataConfig.max_count == 0 then
		return math.huge
	else
		return arg_13_0.dataConfig.max_count
	end
end

function var_0_0.IsMaxCnt(arg_14_0)
	return arg_14_0.data1 > arg_14_0:GetLimitCnt()
end

function var_0_0.GetItemId(arg_15_0)
	return arg_15_0.dataConfig.item_id
end

function var_0_0.GetItemConfig(arg_16_0)
	local var_16_0 = arg_16_0:GetItemId()

	return Item.getConfigData(var_16_0) or {}
end

function var_0_0.GetItemName(arg_17_0)
	local var_17_0 = arg_17_0:GetItemId()
	local var_17_1 = Item.getConfigData(var_17_0)

	return var_17_1 and var_17_1.name or ""
end

function var_0_0.ShopId2SkinId(arg_18_0, arg_18_1)
	return pg.shop_template[arg_18_1].effect_args[1]
end

function var_0_0.OwnAllSkin(arg_19_0)
	local var_19_0 = arg_19_0:GetShopIdList()
	local var_19_1 = _.map(var_19_0, function(arg_20_0)
		return arg_19_0:ShopId2SkinId(arg_20_0)
	end)

	return _.all(var_19_1, function(arg_21_0)
		return getProxy(ShipSkinProxy):hasSkin(arg_21_0)
	end)
end

function var_0_0.GetSkinCouponAct()
	local var_22_0 = pg.activity_template.get_id_list_by_type[ActivityConst.ACTIVITY_TYPE_SKIN_COUPON] or {}

	if #var_22_0 <= 0 then
		return nil
	end

	for iter_22_0 = #var_22_0, 1, -1 do
		local var_22_1 = var_22_0[iter_22_0]
		local var_22_2 = getProxy(ActivityProxy):RawGetActivityById(var_22_1)

		if var_22_2 and not var_22_2:isEnd() then
			return var_22_2
		end
	end

	return nil
end

function var_0_0.StaticExistActivity()
	local var_23_0 = var_0_0.GetSkinCouponAct()

	return var_23_0 and not var_23_0:isEnd()
end

function var_0_0.StaticExistActivityAndCoupon()
	if not var_0_0.StaticExistActivity() then
		return false
	end

	return var_0_0.GetSkinCouponAct():GetCanUsageCnt() > 0
end

function var_0_0.StaticOwnMaxCntSkinCoupon()
	if not var_0_0.StaticExistActivity() then
		return false
	end

	return var_0_0.GetSkinCouponAct():IsMaxCnt()
end

function var_0_0.StaticOwnAllSkin()
	if not var_0_0.StaticExistActivity() then
		return false
	end

	return var_0_0.GetSkinCouponAct():OwnAllSkin()
end

function var_0_0.StaticGetEquivalentRes()
	if not var_0_0.StaticExistActivity() then
		return false
	end

	return var_0_0.GetSkinCouponAct():GetEquivalentRes()
end

function var_0_0.StaticCanUsageSkinCoupon(arg_28_0)
	if not var_0_0.StaticExistActivity() then
		return false
	end

	return var_0_0.GetSkinCouponAct():CanUsageSkinCoupon(arg_28_0)
end

function var_0_0.StaticIsShop(arg_29_0)
	if not var_0_0.StaticExistActivity() then
		return true
	end

	return var_0_0.GetSkinCouponAct():IncludeShop(arg_29_0)
end

function var_0_0.StaticGetNewPrice(arg_30_0)
	if not var_0_0.StaticExistActivity() then
		return arg_30_0
	end

	return var_0_0.GetSkinCouponAct():GetNewPrice(arg_30_0)
end

function var_0_0.StaticGetItemConfig()
	if not var_0_0.StaticExistActivity() then
		return {}
	end

	return var_0_0.GetSkinCouponAct():GetItemConfig()
end

function var_0_0.AddSkinCoupon(arg_32_0)
	if not var_0_0.StaticExistActivity() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_end"))

		return
	end

	local var_32_0 = var_0_0.GetSkinCouponAct()

	if var_32_0:IsMaxCnt() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_already owned"))

		return
	end

	var_32_0.data1 = var_32_0.data1 + 1

	getProxy(ActivityProxy):updateActivity(var_32_0)
end

function var_0_0.UseSkinCoupon()
	if not var_0_0.StaticExistActivity() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_end"))

		return
	end

	local var_33_0 = var_0_0.GetSkinCouponAct()

	var_33_0.data2 = var_33_0.data2 + 1

	getProxy(ActivityProxy):updateActivity(var_33_0)
end

return var_0_0
