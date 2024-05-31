local var_0_0 = class("GuildStartTechCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().id
	local var_1_1 = getProxy(PlayerProxy)
	local var_1_2 = getProxy(GuildProxy)
	local var_1_3 = var_1_2.getData()
	local var_1_4 = var_1_1.getData()

	if not var_1_3:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_no_exist"))

		return

	local var_1_5 = var_1_3.getTechnologyById(var_1_0)

	if not var_1_5:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_not_exist_tech"))

		return

	if not var_1_5.CanUpgrade():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tech_is_max_level"))

		return

	local var_1_6, var_1_7 = var_1_5.GetConsume()

	if var_1_7 > var_1_4.gold:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tech_gold_no_enough"))

		return

	if var_1_6 > var_1_4.guildCoin:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tech_guildgold_no_enough"))

		return

	pg.ConnectionMgr.GetInstance().Send(62015, {
		id = var_1_5.id
	}, 62016, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = var_1_2.getData()

			var_1_4.consume({
				gold = var_1_7,
				guildCoin = var_1_6
			})
			var_1_1.updatePlayer(var_1_4)

			var_1_5 = var_2_0.getTechnologyById(var_1_0)

			var_1_5.levelUp()
			var_1_2.updateGuild(var_2_0)
			arg_1_0.sendNotification(GAME.GUILD_START_TECH_DONE)
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tech_upgrade_done"))
		elif arg_2_0.result == 4305:
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_is_frozen_when_start_tech"))
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
