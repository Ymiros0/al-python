local var_0_0 = class("ActivityPermanentStartCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().activity_id

	pg.ConnectionMgr.GetInstance().Send(11206, {
		activity_id = var_1_0
	}, 11207, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(ActivityPermanentProxy).startSelectActivity(var_1_0)
			arg_1_0.sendNotification(GAME.ACTIVITY_PERMANENT_START_DONE, {
				id = var_1_0
			})
		else
			warning("error permanent"))

return var_0_0
