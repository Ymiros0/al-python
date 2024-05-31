﻿local var_0_0 = class("RefreshMilitaryShopCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	pg.ConnectionMgr.GetInstance():Send(18102, {
		type = 0
	}, 18103, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(ShopsProxy)
			local var_2_1 = var_2_0:getMeritorousShop()
			local var_2_2 = pg.arena_data_shop[1]
			local var_2_3 = var_2_2.refresh_price[var_2_1.refreshCount] or var_2_2.refresh_price[#var_2_2.refresh_price]
			local var_2_4 = getProxy(PlayerProxy)
			local var_2_5 = var_2_4:getData()

			var_2_5:consume({
				gem = var_2_3
			})
			var_2_4:updatePlayer(var_2_5)
			var_2_1:increaseRefreshCount()

			local var_2_6 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.arena_shop_list) do
				local var_2_7 = Goods.Create(iter_2_1, Goods.TYPE_MILITARY)

				var_2_6[var_2_7.id] = var_2_7
			end

			var_2_1:updateAllGoods(var_2_6)
			var_2_0:addMeritorousShop(var_2_1)
			pg.TipsMgr.GetInstance():ShowTips(i18n("refresh_shopStreet_ok"))
			arg_1_0:sendNotification(GAME.REFRESH_MILITARY_SHOP_DONE, Clone(var_2_1))
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
