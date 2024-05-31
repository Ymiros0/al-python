local var_0_0 = class("GetGuildShopCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.type or 1
	local var_1_2 = var_1_0.callback
	local var_1_3 = getProxy(PlayerProxy)
	local var_1_4 = getProxy(ShopsProxy)

	if var_1_1 == GuildConst.MANUAL_REFRESH and var_1_3.getData().getResource(PlayerConst.ResGuildCoin) < var_1_4.getGuildShop().GetResetConsume():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

		return

	pg.ConnectionMgr.GetInstance().Send(60033, {
		type = var_1_1
	}, 60034, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = GuildShop.New(arg_2_0.info)

			if var_1_4.guildShop:
				var_1_4.updateGuildShop(var_2_0, True)
			else
				var_1_4.setGuildShop(var_2_0)

			if var_1_1 == GuildConst.MANUAL_REFRESH:
				local var_2_1 = var_2_0.GetResetConsume()
				local var_2_2 = var_1_3.getData()

				var_2_2.consume({
					guildCoin = var_2_1
				})
				var_1_3.updatePlayer(var_2_2)
				pg.TipsMgr.GetInstance().ShowTips(i18n("guild_shop_refresh_done"))

			if var_1_2:
				var_1_2(var_2_0)

			arg_1_0.sendNotification(GAME.GET_GUILD_SHOP_DONE)
		else
			if var_1_2:
				var_1_2()

			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
