local var_0_0 = class("RefluxSignCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0):
	pg.ConnectionMgr.GetInstance().Send(11753, {
		type = 0
	}, 11754, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(RefluxProxy)

			var_2_0.setSignLastTimestamp()
			var_2_0.addSignCount()

			local var_2_1 = PlayerConst.addTranDrop(arg_2_0.award_list)

			pg.m02.sendNotification(GAME.REFLUX_SIGN_DONE, {
				awards = var_2_1
			})
		else
			pg.TipsMgr.GetInstance().ShowTips("Sign Error." .. arg_2_0.result)
			getProxy(RefluxProxy).setAutoActionForbidden(True))

return var_0_0
