local var_0_0 = class("AcceptFriendRequestCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(FriendProxy)
	local var_1_2 = var_1_1.getFriendCount()

	local function var_1_3(arg_2_0)
		pg.ConnectionMgr.GetInstance().Send(50006, {
			id = var_1_0
		}, 50007, function(arg_3_0)
			if arg_3_0.result == 0:
				getProxy(NotificationProxy).removeRequest(var_1_0)

				if arg_2_0:
					var_1_1.relieveBlackListById(var_1_0)

				pg.TipsMgr.GetInstance().ShowTips(i18n("friend_add_ok"))
				arg_1_0.sendNotification(GAME.FRIEND_ACCEPT_REQUEST_DONE, var_1_0)
			else
				if arg_3_0.result == 6:
					pg.TipsMgr.GetInstance().ShowTips(i18n("friend_max_count_1"))

				pg.TipsMgr.GetInstance().ShowTips(errorTip("friend_acceptFriendRequest", arg_3_0.result)))

	if var_1_2 == MAX_FRIEND_COUNT:
		pg.TipsMgr.GetInstance().ShowTips(i18n("friend_max_count"))

		return

	if var_1_1.isInBlackList(var_1_0):
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("friend_relieve_backlist_tip"),
			def onYes:()
				var_1_3(True)
		})
	else
		var_1_3(False)

return var_0_0
