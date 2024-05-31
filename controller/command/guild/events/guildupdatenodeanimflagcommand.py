local var_0_0 = class("GuildUpdateNodeAnimFlagCommand", import(".GuildEventBaseCommand"))

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.position

	if not arg_1_0.ExistMission(var_1_1):
		return

	local var_1_3 = {
		event_id = var_1_1,
		index = var_1_2
	}

	pg.ConnectionMgr.GetInstance().Send(61025, {
		perf = {
			var_1_3
		}
	}, 61026, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(GuildProxy)
			local var_2_1 = var_2_0.getData()

			var_2_1.GetActiveEvent().GetMissionById(var_1_1).UpdateNodeAnimFlagIndex(var_1_2)
			var_2_0.updateGuild(var_2_1)
			arg_1_0.sendNotification(GAME.GUILD_UPDATE_NODE_ANIM_FLAG_DONE, {
				id = var_1_1
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
