﻿local var_0_0 = class("GetMailTitleCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.callback
	local var_1_2 = var_1_0.mailList

	pg.ConnectionMgr.GetInstance():Send(30014, {
		id_list = var_1_2
	}, 30015, function(arg_2_0)
		var_1_1(arg_2_0.mail_title_list)
	end)
end

return var_0_0
