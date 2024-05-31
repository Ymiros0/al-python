local var_0_0 = class("CheaterMarkCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().reason

	pg.ConnectionMgr.GetInstance().Send(10994, {
		type = var_1_0
	}, 10995, function(arg_2_0)
		if var_1_0 != CC_TYPE_99 and var_1_0 != CC_TYPE_100:
			pg.m02.sendNotification(GAME.LOGOUT, {
				code = 7
			}))

return var_0_0
