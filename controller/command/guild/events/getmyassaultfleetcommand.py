local var_0_0 = class("GetMyAssaultFleetCommand", import(".GuildEventBaseCommand"))

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().callback

	pg.ConnectionMgr.GetInstance().Send(61009, {
		type = 0
	}, 61010, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(GuildProxy)
			local var_2_1 = var_2_0.getData()
			local var_2_2 = getProxy(PlayerProxy).getRawData().id
			local var_2_3 = var_2_1.getMemberById(var_2_2)

			assert(var_2_3)

			local var_2_4 = GuildAssaultFleet.New({})
			local var_2_5 = {}
			local var_2_6 = {}

			_.each(arg_2_0.person_ships, function(arg_3_0)
				local var_3_0 = Ship.New(arg_3_0.ship)

				var_2_5[arg_3_0.pos] = var_3_0
				var_2_6[arg_3_0.pos] = arg_3_0.last_time)
			var_2_4.InitShips(var_2_2, var_2_5)
			var_2_3.UpdateExternalAssaultFleet(var_2_4)
			var_2_0.updateGuild(var_2_1)

			var_2_0.isFetchAssaultFleet = True

			for iter_2_0, iter_2_1 in ipairs(var_2_6):
				var_2_0.UpdatePosCdTime(iter_2_0, iter_2_1)

			arg_1_0.sendNotification(GAME.GUILD_GET_MY_ASSAULT_FLEET_DONE)

			if var_1_0:
				var_1_0()
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
