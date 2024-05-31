local var_0_0 = class("BackYardSeachThemeTemplateCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().str

	if not var_1_0 or var_1_0 == "":
		arg_1_0.sendNotification(GAME.BACKYARD_SEARCH_THEME_TEMPLATE_ERRO)

		return

	local function var_1_1(arg_2_0)
		local var_2_0 = arg_2_0.theme
		local var_2_1 = arg_2_0.has_fav and 1 or 0
		local var_2_2 = arg_2_0.has_like and 1 or 0
		local var_2_3 = BackYardThemeTemplate.New({
			id = var_2_0.id,
			name = var_2_0.name,
			furniture_put_list = var_2_0.furniture_put_list,
			user_id = var_2_0.user_id,
			pos = var_2_0.pos,
			like_count = var_2_0.like_count,
			fav_count = var_2_0.fav_count,
			upload_time = var_2_0.upload_time,
			is_collection = var_2_1,
			is_like = var_2_2,
			image_md5 = var_2_0.image_md5,
			icon_image_md5 = var_2_0.icon_image_md5
		})

		arg_1_0.sendNotification(GAME.BACKYARD_SEARCH_THEME_TEMPLATE_DONE, {
			template = var_2_3
		})

	local function var_1_2(arg_3_0)
		arg_1_0.sendNotification(GAME.BACKYARD_SEARCH_THEME_TEMPLATE_ERRO)

	pg.ConnectionMgr.GetInstance().Send(19113, {
		theme_id = var_1_0
	}, 19114, function(arg_4_0)
		if arg_4_0.result == 0:
			var_1_1(arg_4_0)
		else
			var_1_2(arg_4_0)

			if arg_4_0.result == 20:
				pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_not_found_theme_template"))
			else
				pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_4_0.result] .. arg_4_0.result))

return var_0_0
