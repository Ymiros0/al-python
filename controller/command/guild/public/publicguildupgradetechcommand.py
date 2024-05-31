local var_0_0 = class("PublicGuildUpgradeTechCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().id
	local var_1_1 = getProxy(PlayerProxy)
	local var_1_2 = getProxy(GuildProxy).GetPublicGuild()
	local var_1_3 = var_1_1.getData()
	local var_1_4 = var_1_2.GetTechnologyById(var_1_0)

	if not var_1_4:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_not_exist_tech"))

		return

	if var_1_4.isMaxLevel():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tech_is_max_level"))

		return

	local var_1_5, var_1_6 = var_1_4.GetConsume()

	if var_1_6 > var_1_3.gold:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tech_gold_no_enough"))

		return

	if var_1_5 > var_1_3.guildCoin:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tech_guildgold_no_enough"))

		return

	pg.ConnectionMgr.GetInstance().Send(62015, {
		id = var_1_4.id
	}, 62016, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_3.consume({
				gold = var_1_6,
				guildCoin = var_1_5
			})
			var_1_1.updatePlayer(var_1_3)
			var_1_4.levelUp()
			arg_1_0.sendNotification(GAME.PULIC_GUILD_UPGRADE_TECH_DONE, {
				id = var_1_0
			})
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tech_upgrade_done"))
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
