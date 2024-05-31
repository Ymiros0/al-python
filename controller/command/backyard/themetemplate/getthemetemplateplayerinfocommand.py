local var_0_0 = class("GetThemeTemplatePlayerInfoCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.type
	local var_1_2 = var_1_0.templateId
	local var_1_3 = var_1_0.userId
	local var_1_4 = var_1_0.callback
	local var_1_5 = getProxy(DormProxy)

	if var_1_1 == BackYardConst.THEME_TEMPLATE_TYPE_SHOP or var_1_1 == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION:
		local function var_1_6(arg_2_0)
			local var_2_0 = CourtYardThemeOwner.New(arg_2_0.player)
			local var_2_1 = var_1_5.GetShopThemeTemplateById(var_1_2)

			if var_2_1:
				var_2_1.SetPlayerInfo(var_2_0)
				var_1_5.UpdateShopThemeTemplate(var_2_1)

			local var_2_2 = var_1_5.GetCollectionThemeTemplateById(var_1_2)

			if var_2_2:
				var_2_2.SetPlayerInfo(var_2_0)
				var_1_5.UpdateCollectionThemeTemplate(var_2_2)

			if var_1_4:
				var_1_4(var_2_0)

		pg.ConnectionMgr.GetInstance().Send(50113, {
			user_id = var_1_3
		}, 50114, function(arg_3_0)
			if arg_3_0.result == 0:
				var_1_6(arg_3_0)
			else
				pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_3_0.result] .. arg_3_0.result))
	elif var_1_1 == BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM:
		local var_1_7 = getProxy(PlayerProxy).getData()
		local var_1_8 = var_1_5.GetCustomThemeTemplateById(var_1_2)

		if var_1_8:
			var_1_8.SetPlayerInfo(var_1_7)
			var_1_5.UpdateCustomThemeTemplate(var_1_8)

		if var_1_4:
			var_1_4(var_1_7)

return var_0_0
