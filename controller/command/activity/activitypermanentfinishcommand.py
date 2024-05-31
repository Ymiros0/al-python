local var_0_0 = class("ActivityPermanentFinishCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().activity_id

	pg.ConnectionMgr.GetInstance().Send(11208, {
		activity_id = var_1_0
	}, 11209, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(ActivityPermanentProxy).finishNowActivity(var_1_0)
			getProxy(ActivityProxy).deleteActivityById(var_1_0)
			arg_1_0.sendNotification(GAME.ACTIVITY_PERMANENT_FINISH_DONE, {
				activity_id = var_1_0
			})
		else
			warning("error permanent"))

return var_0_0
