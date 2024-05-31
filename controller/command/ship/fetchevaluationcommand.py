local var_0_0 = class("FetchEvaluationCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_1_2 = getProxy(CollectionProxy)
	local var_1_3 = var_1_2.getShipGroup(var_1_0)

	if not var_1_3:
		return

	assert(var_1_3, "shipGroup is None" .. var_1_0)

	if var_1_1 - var_1_3.lastReqStamp > ShipGroup.REQ_INTERVAL:
		pg.ConnectionMgr.GetInstance().Send(17101, {
			ship_group_id = var_1_0
		}, 17102, function(arg_2_0)
			local var_2_0 = arg_2_0.ship_discuss

			if var_2_0 and var_2_0.ship_group_id == var_1_0:
				if var_1_3:
					var_1_3.evaluation = ShipEvaluation.New(var_2_0)
					var_1_3.lastReqStamp = pg.TimeMgr.GetInstance().GetServerTime()

					var_1_2.updateShipGroup(var_1_3)
					arg_1_0.sendNotification(GAME.FETCH_EVALUATION_DONE, var_1_0)
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("fetch_ship_eva", arg_2_0.result)))
	elif var_1_3.evaluation:
		arg_1_0.sendNotification(GAME.FETCH_EVALUATION_DONE, var_1_0)

return var_0_0
