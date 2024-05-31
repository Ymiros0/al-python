local var_0_0 = class("GetDormThemeListCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = 0
	local var_1_2

	if var_1_0 and type(var_1_0) == "table":
		var_1_2 = var_1_0.callback
	else
		var_1_1 = var_1_0 or 0

	pg.ConnectionMgr.GetInstance().Send(19018, {
		id = var_1_1
	}, 19019, function(arg_2_0)
		local var_2_0 = getProxy(DormProxy)

		if var_1_1 == 0:
			var_2_0.initThemes(arg_2_0.theme_list or {})
		else
			for iter_2_0, iter_2_1 in ipairs(arg_2_0.theme_list):
				var_2_0.updateTheme(iter_2_1)

		arg_1_0.sendNotification(GAME.GET_DORMTHEME_DONE)

		if var_1_2:
			var_1_2())

return var_0_0
