﻿local var_0_0 = class("MetaShoppingCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(ShopsProxy)
	local var_1_2 = var_1_1:GetMetaShop()

	assert(var_1_2, "should exist shop")

	local var_1_3 = var_1_2:GetCommodityById(var_1_0.arg1)

	assert(var_1_3, "commodity cant not be nil")

	local var_1_4 = getProxy(ActivityProxy):getActivityById(var_1_0.activity_id)

	if not var_1_4 or var_1_4:isEnd() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_end"))

		return
	end

	if not PlayerConst.CheckResForShopping(var_1_3:GetConsume(), var_1_0.arg2) then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_resource"))

		return
	end

	local var_1_5 = getProxy(PlayerProxy):getRawData()
	local var_1_6 = var_1_0.arg2
	local var_1_7 = var_1_3:getConfig("commodity_type")
	local var_1_8 = var_1_3:getConfig("commodity_id")
	local var_1_9 = var_1_3:getConfig("num")

	if var_1_7 == 1 then
		if var_1_8 == 1 and var_1_5:GoldMax(var_1_9 * var_1_6) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_shop"))

			return
		end

		if var_1_8 == 2 and var_1_5:OilMax(var_1_9 * var_1_6) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_shop"))

			return
		end
	end

	pg.ConnectionMgr.GetInstance():Send(11202, {
		activity_id = var_1_0.activity_id,
		cmd = var_1_0.cmd,
		arg1 = var_1_0.arg1,
		arg2 = var_1_0.arg2,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = var_1_1:GetMetaShop()

			if table.contains(var_1_4.data1_list, var_1_0.arg1) then
				for iter_2_0, iter_2_1 in ipairs(var_1_4.data1_list) do
					if iter_2_1 == var_1_0.arg1 then
						var_1_4.data2_list[iter_2_0] = var_1_4.data2_list[iter_2_0] + var_1_0.arg2

						break
					end
				end
			else
				table.insert(var_1_4.data1_list, var_1_0.arg1)
				table.insert(var_1_4.data2_list, var_1_0.arg2)
			end

			getProxy(ActivityProxy):updateActivity(var_1_4)
			PlayerConst.ConsumeResForShopping(var_1_3:GetConsume(), var_1_0.arg2)

			local var_2_1 = PlayerConst.GetTranAwards(var_1_0, arg_2_0)

			var_1_1:UpdateMetaShopGoods(var_1_0.arg1, var_1_0.arg2)
			arg_1_0:sendNotification(GAME.ON_META_SHOPPING_DONE, {
				awards = var_2_1
			})
			pg.TipsMgr.GetInstance():ShowTips(i18n("common_buy_success"))
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
