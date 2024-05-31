local var_0_0 = class("GuildJoinMissionCommand", import(".GuildEventBaseCommand"))

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.shipIds

	if not var_1_1 or #var_1_2 == 0:
		return

	if not arg_1_0.CanFormationMission(var_1_1):
		return

	pg.ConnectionMgr.GetInstance().Send(61007, {
		event_tid = var_1_1,
		ship_ids = var_1_2
	}, 61008, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(GuildProxy)
			local var_2_1 = var_2_0.getData()
			local var_2_2 = var_2_1.GetActiveEvent().GetMissionById(var_1_1)
			local var_2_3 = var_2_2.GetCanFormationIndex()

			var_2_2.UpdateFleet(var_2_3, var_1_2)
			var_2_2.UpdateFormationTime(pg.TimeMgr.GetInstance().GetServerTime())
			var_2_0.updateGuild(var_2_1)
			arg_1_0.sendNotification(GAME.GUILD_JOIN_MISSION_DONE, {
				id = var_1_1
			})
			pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inGuildEvent")
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
