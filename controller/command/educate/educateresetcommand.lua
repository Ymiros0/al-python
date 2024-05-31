local var_0_0 = class("EducateResetCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1

	var_1_1 = var_1_0 and var_1_0.callback

	pg.ConnectionMgr.GetInstance():Send(27029, {
		type = 1
	}, 27030, function(arg_2_0)
		if arg_2_0.result == 0 then
			getProxy(EducateProxy):Reset(function()
				arg_1_0:sendNotification(GAME.EDUCATE_REFRESH_DONE)
			end)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("educate reset error: ", arg_2_0.result))
		end
	end)
end

return var_0_0
