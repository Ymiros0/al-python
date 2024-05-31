local var_0_0 = class("BackYardGetThemeTemplateDataCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.templateId
	local var_1_2 = var_1_0.callback

	pg.ConnectionMgr.GetInstance():Send(19113, {
		theme_id = var_1_1
	}, 19114, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = arg_2_0.theme
			local var_2_1 = arg_2_0.has_fav and 1 or 0
			local var_2_2 = arg_2_0.has_like and 1 or 0
			local var_2_3 = BackYardThemeTemplate.New({
				is_fetch = true,
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
			local var_2_4 = getProxy(DormProxy)

			if var_2_4:GetShopThemeTemplateById(var_1_1) then
				var_2_4:UpdateShopThemeTemplate(var_2_3)
			end

			if var_2_4:GetCollectionThemeTemplateById(var_1_1) then
				var_2_4:UpdateCollectionThemeTemplate(var_2_3)
			end

			if var_1_2 then
				var_1_2(var_2_3)
			end

			arg_1_0:sendNotification(GAME.BACKYARD_GET_THEME_TEMPLATE_DATA_DONE, {
				template = var_2_3
			})
		elseif arg_2_0.result == 20 then
			local var_2_5 = getProxy(DormProxy)

			if var_2_5:GetShopThemeTemplateById(var_1_1) then
				var_2_5:DeleteShopThemeTemplate(var_1_1)
			end

			if var_2_5:GetCollectionThemeTemplateById(var_1_1) then
				var_2_5:DeleteCollectionThemeTemplate(var_1_1)
			end

			pg.TipsMgr.GetInstance():ShowTips(i18n("Backyard_theme_template_be_delete_tip"))
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
