local var_0_0 = class("SendFriendMsgCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.playerId
	local var_1_2 = var_1_0.msg
	local var_1_3 = getProxy(FriendProxy)

	if not var_1_3:isFriend(var_1_1) then
		pg.TipsMgr.GetInstance():ShowTips(i18n("friend_sendFriendMsg_error_noFriend"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(50105, {
		id = var_1_1,
		content = var_1_2
	}, 50106, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(PlayerProxy)

			var_1_3:addChatMsg(var_1_1, ChatMsg.New(ChatConst.ChannelFriend, {
				player = var_2_0:getData(),
				content = var_1_2,
				timestamp = pg.TimeMgr.GetInstance():GetServerTime()
			}))
			arg_1_0:sendNotification(GAME.FRIEND_SEND_MSG_DONE)
		elseif arg_2_0.result == 28 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("friend_offline"))
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("friend_sendFriendMsg", arg_2_0.result))
		end
	end)
end

return var_0_0
