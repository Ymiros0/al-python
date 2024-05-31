local var_0_0 = class("BackYardLikeThemeTemplateCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.templateId
	local var_1_2 = var_1_0.uploadTime

	local function var_1_3(arg_2_0)
		local var_2_0 = getProxy(DormProxy)
		local var_2_1 = var_2_0.GetCollectionThemeTemplateById(var_1_1)

		if var_2_1:
			var_2_1.AddLike()
			var_2_0.UpdateCollectionThemeTemplate(var_2_1)

		local var_2_2 = var_2_0.GetShopThemeTemplateById(var_1_1)

		if var_2_2:
			var_2_2.AddLike()
			var_2_0.UpdateShopThemeTemplate(var_2_2)

		arg_1_0.sendNotification(GAME.BACKYARD_LIKE_THEME_TEMPLATE_DONE)

	pg.ConnectionMgr.GetInstance().Send(19121, {
		theme_id = var_1_1,
		upload_time = var_1_2
	}, 19122, function(arg_3_0)
		if arg_3_0.result == 0:
			var_1_3(arg_3_0)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_3_0.result] .. arg_3_0.result))

return var_0_0
