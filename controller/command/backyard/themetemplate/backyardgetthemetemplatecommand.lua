﻿local var_0_0 = class("BackYardGetThemeTemplateCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.type
	local var_1_2 = var_1_0.callback
	local var_1_3 = getProxy(DormProxy)

	local function var_1_4(arg_2_0, arg_2_1)
		if var_1_1 == BackYardConst.THEME_TEMPLATE_TYPE_SHOP then
			local var_2_0 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.theme_id_list or {}) do
				local var_2_1
				local var_2_2 = BackYardThemeTemplate.New({
					id = iter_2_1
				})

				var_2_2:SetSortIndex(iter_2_0)

				var_2_0[var_2_2.id] = var_2_2
			end

			var_1_3:SetShopThemeTemplates(var_2_0)
		elseif var_1_1 == BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM then
			local var_2_3 = {}

			for iter_2_2, iter_2_3 in ipairs(arg_2_0.theme_list or {}) do
				local var_2_4
				local var_2_5 = BackYardSelfThemeTemplate.New(iter_2_3)

				var_2_3[var_2_5.id] = var_2_5
			end

			var_1_3:SetCustomThemeTemplates(var_2_3)
		elseif var_1_1 == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION then
			local var_2_6 = {}

			for iter_2_4, iter_2_5 in ipairs(arg_2_0.theme_profile_list or {}) do
				local var_2_7
				local var_2_8 = BackYardThemeTemplate.New({
					id = iter_2_5.id,
					upload_time = iter_2_5.upload_time
				})

				var_2_6[var_2_8.id] = var_2_8
			end

			var_1_3:SetCollectionThemeTemplates(var_2_6)
		end

		if arg_2_1 then
			arg_2_1()
		end
	end

	local function var_1_5(arg_3_0)
		arg_1_0:sendNotification(GAME.BACKYARD_GET_IMG_MD5, {
			type = var_1_1,
			callback = arg_3_0
		})
	end

	local function var_1_6(arg_4_0)
		seriesAsync({
			function(arg_5_0)
				var_1_4(arg_4_0, arg_5_0)
			end,
			function(arg_6_0)
				var_1_5(arg_6_0)
			end
		}, function()
			arg_1_0:sendNotification(GAME.BACKYARD_GET_THEME_TEMPLATE_DONE)

			if var_1_2 then
				var_1_2()
			end
		end)
	end

	if var_1_1 == BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM then
		pg.ConnectionMgr.GetInstance():Send(19105, {
			typ = var_1_1
		}, 19106, function(arg_8_0)
			if arg_8_0.result == 0 then
				var_1_4(arg_8_0)
				arg_1_0:sendNotification(GAME.BACKYARD_GET_THEME_TEMPLATE_DONE)

				if var_1_2 then
					var_1_2()
				end
			else
				pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_8_0.result] .. arg_8_0.result)
			end
		end)
	elseif var_1_1 == BackYardConst.THEME_TEMPLATE_TYPE_SHOP then
		pg.ConnectionMgr.GetInstance():Send(19117, {
			typ = var_1_3.TYPE,
			page = var_1_3.PAGE,
			num = BackYardConst.THEME_TEMPLATE_SHOP_REFRSH_CNT
		}, 19118, function(arg_9_0)
			if arg_9_0.result == 0 then
				var_1_6(arg_9_0)
			else
				pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_9_0.result] .. arg_9_0.result)
			end
		end)
	elseif var_1_1 == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION then
		pg.ConnectionMgr.GetInstance():Send(19115, {
			typ = 3
		}, 19116, function(arg_10_0)
			if arg_10_0.result == 0 then
				var_1_6(arg_10_0)
			else
				pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_10_0.result] .. arg_10_0.result)
			end
		end)
	end
end

return var_0_0
