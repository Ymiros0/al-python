local var_0_0 = class("WorldFleetRedeployCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(33409, var_1_0, 33410, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(WorldProxy)
			local var_2_1 = nowWorld()

			var_2_1.SetFleets(var_2_0.NetBuildMapFleetList(arg_2_0.group_list))

			local var_2_2 = var_2_1.GetActiveMap()

			var_2_2.SetValid(False)
			var_2_2.UnbindFleets()

			local var_2_3 = arg_2_0.group_list[1].id

			var_2_2.findex = table.indexof(var_2_1.fleets, var_2_1.GetFleet(var_2_3))

			var_2_2.BindFleets(var_2_1.fleets)

			local var_2_4 = var_2_1.CalcOrderCost(WorldConst.OpReqRedeploy)

			var_2_1.staminaMgr.ConsumeStamina(var_2_4)
			var_2_1.SetReqCDTime(WorldConst.OpReqRedeploy, pg.TimeMgr.GetInstance().GetServerTime())
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_redeploy_2"))
			var_2_1.GetBossProxy().GenFleet()
			arg_1_0.sendNotification(GAME.WORLD_FLEET_REDEPLOY_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("world_fleet_redeploy_error_", arg_2_0.result)))

return var_0_0
