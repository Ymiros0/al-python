local var_0_0 = class("StopBluePrintCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.callback
	local var_1_3 = getProxy(TechnologyProxy)
	local var_1_4 = var_1_3.getBluePrintById(var_1_1)

	if not var_1_4:
		return

	if not var_1_4.isDeving() and not var_1_4.isFinished():
		return

	pg.ConnectionMgr.GetInstance().Send(63206, {
		blueprint_id = var_1_1
	}, 63207, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = pg.TimeMgr.GetInstance().GetServerTime() - var_1_4.startTime

			var_1_4.updateStartUpTime(var_2_0)
			var_1_4.reset()
			var_1_3.updateBluePrint(var_1_4)
			arg_1_0.sendNotification(GAME.STOP_BLUEPRINT_DONE, {
				id = var_1_4.id
			})

			if var_1_2:
				var_1_2()
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("technology_stop_erro") .. arg_2_0.result))

return var_0_0
