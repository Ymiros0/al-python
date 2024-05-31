local var_0_0 = class("BackYardDeleteThemeTemplateCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().templateId
	local var_1_1 = getProxy(DormProxy)
	local var_1_2 = var_1_1.GetCustomThemeTemplateById(var_1_0)

	local function var_1_3(arg_2_0)
		if not var_1_2.IsPushed():
			if arg_2_0:
				arg_2_0()

			return

		pg.UIMgr.GetInstance().LoadingOn()
		seriesAsync({
			function(arg_3_0)
				BackYardThemeTempalteUtil.DeleteTexture(var_1_2.GetTextureName(), function(arg_4_0)
					if arg_4_0:
						arg_3_0()),
			function(arg_5_0)
				BackYardThemeTempalteUtil.DeleteTexture(var_1_2.GetTextureIconName(), function(arg_6_0)
					if arg_6_0:
						arg_5_0())
		}, function()
			pg.UIMgr.GetInstance().LoadingOff()

			if arg_2_0:
				arg_2_0())

	local function var_1_4(arg_8_0)
		BackYardThemeTempalteUtil.ClearCaches({
			var_1_2.GetTextureName(),
			var_1_2.GetTextureIconName()
		})
		var_1_1.DeleteCustomThemeTemplate(var_1_0)

		if var_1_1.IsInitShopThemeTemplates():
			if var_1_1.GetShopThemeTemplateById(var_1_0):
				var_1_1.DeleteShopThemeTemplate(var_1_0)

			if var_1_1.GetCollectionThemeTemplateById(var_1_0):
				var_1_1.DeleteCollectionThemeTemplate(var_1_0)

		arg_1_0.sendNotification(GAME.BACKYARD_DELETE_THEME_TEMPLATE_DONE)

	;(function()
		pg.ConnectionMgr.GetInstance().Send(19123, {
			pos = var_1_2.pos
		}, 19124, function(arg_10_0)
			if arg_10_0.result == 0:
				var_1_4(arg_10_0)
				var_1_3()
			else
				pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_10_0.result] .. arg_10_0.result)))()

return var_0_0
