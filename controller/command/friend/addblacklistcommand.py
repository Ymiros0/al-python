local var_0_0 = class("AddBlackListCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	if var_1_0.isFriend():
		pg.TipsMgr.GetInstance().ShowTips(i18n("friend_player_is_friend_tip"))

		return

	pg.ConnectionMgr.GetInstance().Send(50109, {
		id = var_1_0.id
	}, 50110, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(FriendProxy).addIntoBlackList(var_1_0)
			arg_1_0.sendNotification(GAME.FRIEND_ADD_BLACKLIST_DONE)
			pg.TipsMgr.GetInstance().ShowTips(i18n("friend_addblacklist_success"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("friend_addblacklist", arg_2_0.result)))

return var_0_0
