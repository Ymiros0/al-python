local var_0_0 = class("InformBackYardThemeTemplateCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.playerName

	if getProxy(PlayerProxy).getRawData().level < 20:
		pg.TipsMgr.GetInstance().ShowTips(i18n("inform_level_limit"))

		return

	local var_1_2 = var_1_0.uid
	local var_1_3 = var_1_0.tid
	local var_1_4 = 0

	for iter_1_0, iter_1_1 in ipairs(var_1_0.content):
		var_1_4 = iter_1_1 + var_1_4

	local var_1_5 = getProxy(DormProxy)
	local var_1_6 = var_1_5.GetShopThemeTemplateById(var_1_3) or var_1_5.GetCollectionThemeTemplateById(var_1_3)

	if not var_1_6 or not var_1_6.name:
		return

	pg.ConnectionMgr.GetInstance().Send(19129, {
		target_id = var_1_2,
		target_name = var_1_1,
		theme_id = var_1_3,
		theme_name = var_1_6.name,
		reason = var_1_4
	}, 19130, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(ChatProxy)

			table.insert(var_2_0.informs, var_1_2 .. var_1_3)
			arg_1_0.sendNotification(GAME.INFORM_THEME_TEMPLATE_DONE)
			pg.TipsMgr.GetInstance().ShowTips(i18n("inform_sueecss"))
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
