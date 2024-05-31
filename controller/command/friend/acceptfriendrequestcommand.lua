﻿local var_0_0 = class("AcceptFriendRequestCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(FriendProxy)
	local var_1_2 = var_1_1:getFriendCount()

	local function var_1_3(arg_2_0)
		pg.ConnectionMgr.GetInstance():Send(50006, {
			id = var_1_0
		}, 50007, function(arg_3_0)
			if arg_3_0.result == 0 then
				getProxy(NotificationProxy):removeRequest(var_1_0)

				if arg_2_0 then
					var_1_1:relieveBlackListById(var_1_0)
				end

				pg.TipsMgr.GetInstance():ShowTips(i18n("friend_add_ok"))
				arg_1_0:sendNotification(GAME.FRIEND_ACCEPT_REQUEST_DONE, var_1_0)
			else
				if arg_3_0.result == 6 then
					pg.TipsMgr.GetInstance():ShowTips(i18n("friend_max_count_1"))
				end

				pg.TipsMgr.GetInstance():ShowTips(errorTip("friend_acceptFriendRequest", arg_3_0.result))
			end
		end)
	end

	if var_1_2 == MAX_FRIEND_COUNT then
		pg.TipsMgr.GetInstance():ShowTips(i18n("friend_max_count"))

		return
	end

	if var_1_1:isInBlackList(var_1_0) then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("friend_relieve_backlist_tip"),
			onYes = function()
				var_1_3(true)
			end
		})
	else
		var_1_3(false)
	end
end

return var_0_0
