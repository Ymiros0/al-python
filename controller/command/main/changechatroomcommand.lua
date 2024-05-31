local var_0_0 = class("ChangeChatRoomCommand", pm.SimpleCommand)
local var_0_1 = 99

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(PlayerProxy)

	if not var_1_1 then
		return
	end

	local var_1_2 = var_1_1:getData()

	if not var_1_2 then
		return
	end

	if not var_1_0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("main_notificationLayer_not_roomId"))

		return
	end

	if var_1_0 > var_0_1 or var_1_0 < 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("main_notificationLayer_roomId_invaild"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(11401, {
		room_id = var_1_0
	}, 11402, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_2:changeChatRoom(arg_2_0.room_id or var_1_0)
			var_1_1:updatePlayer(var_1_2)
			getProxy(ChatProxy):clearMsg()
			arg_1_0:sendNotification(GAME.CHANGE_CHAT_ROOM_DONE, var_1_2)
		elseif arg_2_0.result == 6 then
			arg_1_0:sendNotification(GAME.CHAT_ROOM_MAX_NUMBER)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("player_change_chat_room_erro", arg_2_0.result))
		end
	end)
end

return var_0_0
