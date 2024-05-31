﻿local var_0_0 = class("FragmentShoppingCommand", pm.SimpleCommand)

var_0_0.FRAG_SHOP = 2
var_0_0.FRAG_NORMAL_SHOP = 3

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.count
	local var_1_3 = var_1_0.type
	local var_1_4 = getProxy(PlayerProxy):getRawData()
	local var_1_5 = getProxy(ShopsProxy)
	local var_1_6 = var_1_5:getFragmentShop()
	local var_1_7 = var_1_6:getGoodsCfg(var_1_1)
	local var_1_8 = Drop.New({
		type = var_1_7.resource_category,
		id = var_1_7.resource_type
	})

	if var_1_8:getOwnedCount() < var_1_7.resource_num * var_1_2 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_x", var_1_8:getName()))

		return
	end

	if var_1_7.commodity_type == 1 then
		if var_1_7.commodity_id == 1 and var_1_4:GoldMax(var_1_7.num * var_1_2) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_shop"))

			return
		end

		if var_1_7.commodity_id == 2 and var_1_4:OilMax(var_1_7.num * var_1_2) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_shop"))

			return
		end
	end

	local var_1_9 = var_1_6:GetCommodityById(var_1_1)
	local var_1_10 = var_0_0.FRAG_SHOP

	if var_1_9.type == Goods.TYPE_FRAGMENT_NORMAL then
		var_1_10 = var_0_0.FRAG_NORMAL_SHOP
	end

	pg.ConnectionMgr.GetInstance():Send(16201, {
		id = var_1_1,
		type = var_1_10,
		count = var_1_2
	}, 16202, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.drop_list)
			local var_2_1 = var_1_5:getFragmentShop()

			var_2_1:getGoodsById(var_1_1):addBuyCount(var_1_2)
			var_1_5:updateFragmentShop(var_2_1)
			reducePlayerOwn({
				type = var_1_7.resource_category,
				id = var_1_7.resource_type,
				count = var_1_7.resource_num * var_1_2
			})
			arg_1_0:sendNotification(GAME.FRAG_SHOPPING_DONE, {
				awards = var_2_0,
				id = var_1_1
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
