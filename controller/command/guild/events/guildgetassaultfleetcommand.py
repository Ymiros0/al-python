local var_0_0 = class("GuildGetAssaultFleetCommand", import(".GuildEventBaseCommand"))

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().callback
	local var_1_1 = getProxy(GuildProxy)

	if not var_1_1.ShouldRequestForamtion():
		if var_1_0:
			var_1_0()

		return

	pg.ConnectionMgr.GetInstance().Send(61011, {
		type = 0
	}, 61012, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = var_1_1.getData()
			local var_2_1 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.recommends or {}):
				if not var_2_1[iter_2_1.user_id]:
					var_2_1[iter_2_1.user_id] = {}

				table.insert(var_2_1[iter_2_1.user_id], iter_2_1.ship_id)

			for iter_2_2, iter_2_3 in ipairs(arg_2_0.ships):
				local var_2_2 = iter_2_3.user_id
				local var_2_3 = var_2_0.getMemberById(var_2_2)

				if var_2_3:
					local var_2_4 = GuildAssaultFleet.New(iter_2_3)
					local var_2_5 = var_2_1[var_2_3.id]

					if var_2_5:
						var_2_4.SetRecommendList(var_2_5)

					var_2_3.UpdateAssaultFleet(var_2_4)

			var_1_1.updateGuild(var_2_0)
			arg_1_0.sendNotification(GAME.GUILD_GET_ASSAULT_FLEET_DONE)
			pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inGuildEvent")

			if var_1_0:
				var_1_0()
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
