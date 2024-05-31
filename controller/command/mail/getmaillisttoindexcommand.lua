﻿local var_0_0 = class("GetMailListToIndexCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.index
	local var_1_2 = var_1_0.callback
	local var_1_3 = getProxy(MailProxy)
	local var_1_4

	local function var_1_5(arg_2_0)
		local var_2_0 = 1
		local var_2_1, var_2_2 = getProxy(MailProxy):GetNextIndex()

		pg.ConnectionMgr.GetInstance():Send(30002, {
			type = 1,
			index_begin = var_2_1,
			index_end = var_2_2
		}, 30003, function(arg_3_0)
			local var_3_0 = underscore.map(arg_3_0.mail_list, function(arg_4_0)
				return Mail.New(arg_4_0)
			end)

			var_1_3:AddNextMails(var_3_0)

			if #var_1_3.ids < var_1_1 then
				var_1_5(arg_2_0)
			else
				arg_2_0()
			end
		end)
	end

	var_1_5(function()
		existCall(var_1_2)
		arg_1_0:sendNotification(GAME.GET_MAIL_LIST_TO_INDEX_DONE)
	end)
end

return var_0_0
