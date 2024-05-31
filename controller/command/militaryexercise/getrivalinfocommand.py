local var_0_0 = class("GetRivalInfoCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(18104, {
		id = var_1_0
	}, 18105, function(arg_2_0)
		if arg_2_0.info.id == 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_get_player_info_erro"))
		else
			local var_2_0 = Rival.New(arg_2_0.info)

			arg_1_0.sendNotification(GAME.GET_RIVAL_INFO_DONE, {
				rival = var_2_0
			}))

return var_0_0
