local var_0_0 = class("WorldKillCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	pg.ConnectionMgr.GetInstance().Send(33112, {
		type = 0
	}, 33113, function(arg_2_0)
		local var_2_0

		if arg_2_0.result == 0:
			getProxy(WorldProxy).BuildWorld(World.TypeFull)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("world_reset_error_", arg_2_0.result))

		arg_1_0.sendNotification(GAME.WORLD_KILL_DONE, {
			result = arg_2_0.result
		}))

return var_0_0
