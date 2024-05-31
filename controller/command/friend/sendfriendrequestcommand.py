local var_0_0 = class("SendFriendRequestCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.msg
	local var_1_3 = getProxy(PlayerProxy).getData()

	if wordVer(var_1_2) > 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("friend_msg_forbid"))

		return

	if var_1_3.id == var_1_1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("dont_add_self"))

		return

	local var_1_4 = getProxy(FriendProxy)

	if var_1_4.isFriend(var_1_1):
		pg.TipsMgr.GetInstance().ShowTips(i18n("friend_already_add"))

		return

	if var_1_4.getFriendCount() == MAX_FRIEND_COUNT:
		pg.TipsMgr.GetInstance().ShowTips(i18n("friend_max_count"))

		return

	pg.ConnectionMgr.GetInstance().Send(50003, {
		id = var_1_1,
		content = var_1_2
	}, 50004, function(arg_2_0)
		if arg_2_0.result == 0:
			arg_1_0.sendNotification(GAME.FRIEND_SEND_REQUEST_DONE, var_1_1)
			pg.TipsMgr.GetInstance().ShowTips(i18n("friend_sendFriendRequest_success"))
		elif arg_2_0.result == 1:
			pg.TipsMgr.GetInstance().ShowTips(i18n("friend_sendFriendRequest_success"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("friend_sendFriendRequest", arg_2_0.result)))

return var_0_0
