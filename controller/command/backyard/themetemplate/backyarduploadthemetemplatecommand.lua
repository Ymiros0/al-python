local var_0_0 = class("BackYardUploadThemeTemplateCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().templateId
	local var_1_1 = getProxy(DormProxy)
	local var_1_2 = var_1_1:GetCustomThemeTemplateById(var_1_0)

	local function var_1_3(arg_2_0)
		pg.UIMgr.GetInstance():LoadingOn()
		seriesAsync({
			function(arg_3_0)
				BackYardThemeTempalteUtil.UploadTexture(var_1_2:GetTextureName(), function(arg_4_0)
					if arg_4_0 then
						arg_3_0()
					end
				end)
			end,
			function(arg_5_0)
				BackYardThemeTempalteUtil.UploadTexture(var_1_2:GetTextureIconName(), function(arg_6_0)
					if arg_6_0 then
						arg_5_0()
					end
				end)
			end
		}, function()
			pg.UIMgr.GetInstance():LoadingOff()
			arg_2_0()
		end)
	end

	local function var_1_4(arg_8_0)
		var_1_2:Upload()
		var_1_1:UpdateCustomThemeTemplate(var_1_2)
		arg_1_0:sendNotification(GAME.BACKYARD_UPLOAD_THEME_TEMPLATE_DONE)
	end

	local function var_1_5()
		pg.ConnectionMgr.GetInstance():Send(19111, {
			pos = var_1_2.pos
		}, 19112, function(arg_10_0)
			if arg_10_0.result == 0 then
				var_1_4(arg_10_0)
			else
				pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_10_0.result] .. arg_10_0.result)
			end
		end)
	end

	var_1_3(function()
		var_1_5()
	end)
end

return var_0_0
