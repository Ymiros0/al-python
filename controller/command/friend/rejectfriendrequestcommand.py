local var_0_0 = class("RejectFriendRequestCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(NotificationProxy)

	if var_1_1.getRequestCount() == 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("friend_no_request"))

		return

	pg.ConnectionMgr.GetInstance().Send(50009, {
		id = var_1_0
	}, 50010, function(arg_2_0)
		if arg_2_0.result == 0:
			if var_1_0 == 0:
				var_1_1.removeAllRequest()
				pg.TipsMgr.GetInstance().ShowTips(i18n("reject_all_friend_ok"))
			else
				var_1_1.removeRequest(var_1_0)
				pg.TipsMgr.GetInstance().ShowTips(i18n("reject_friend_ok"))

			arg_1_0.sendNotification(GAME.FRIEND_REJECT_REQUEST_DONE, var_1_0)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("friend_rejectFriendRequest", arg_2_0.result)))

return var_0_0
