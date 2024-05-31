local var_0_0 = class("GuildShopCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.goodsId
	local var_1_2 = var_1_0.selectedId
	local var_1_3 = #var_1_2
	local var_1_4 = getProxy(PlayerProxy)
	local var_1_5 = var_1_4:getData()
	local var_1_6 = var_1_5:getResource(8)
	local var_1_7 = getProxy(ShopsProxy)
	local var_1_8 = var_1_7:getGuildShop():getGoodsById(var_1_1)
	local var_1_9 = var_1_8:GetPrice()

	if var_1_6 < var_1_9 * var_1_3 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_resource"))

		return
	end

	if not var_1_8:CanPurchaseCnt(var_1_3) then
		pg.TipsMgr.GetInstance():ShowTips(i18n("guild_shop_cnt_no_enough"))

		return
	end

	local var_1_10 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_2) do
		if not var_1_10[iter_1_1] then
			var_1_10[iter_1_1] = {
				count = 1,
				id = iter_1_1
			}
		else
			var_1_10[iter_1_1].count = var_1_10[iter_1_1].count + 1
		end
	end

	pg.ConnectionMgr.GetInstance():Send(60035, {
		goodsid = var_1_8.configId,
		index = var_1_8.index,
		selected = _.values(var_1_10)
	}, 60036, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.drop_list)
			local var_2_1 = var_1_7:getGuildShop()

			var_2_1:UpdateGoodsCnt(var_1_1, var_1_3)
			var_1_7:updateGuildShop(var_2_1)
			var_1_5:consume({
				guildCoin = var_1_9 * var_1_3
			})
			var_1_4:updatePlayer(var_1_5)
			arg_1_0:sendNotification(GAME.ON_GUILD_SHOP_PURCHASE_DONE, {
				awards = var_2_0
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
