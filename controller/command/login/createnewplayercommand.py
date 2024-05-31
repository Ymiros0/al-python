local var_0_0 = class("CreateNewPlayerCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.nickname
	local var_1_2 = var_1_0.shipId

	if var_1_1 == "":
		pg.TipsMgr.GetInstance().ShowTips(i18n("login_createNewPlayer_error_nameNull"))

	pg.ConnectionMgr.GetInstance().Send(10024, {
		nick_name = var_1_1,
		ship_id = var_1_2,
		device_id = pg.SdkMgr.GetInstance().GetDeviceId()
	}, 10025, function(arg_2_0)
		if arg_2_0.result == 0:
			print("created new player. " .. arg_2_0.user_id)
			pg.TrackerMgr.GetInstance().Tracking(TRACKING_ROLE_CREATE, None, arg_2_0.user_id)
			getProxy(SettingsProxy).SetSelectedShipId(var_1_2)
			arg_1_0.sendNotification(GAME.CREATE_NEW_PLAYER_DONE, arg_2_0.user_id)
			pg.TipsMgr.GetInstance().ShowTips(i18n("create_player_success"))
		elif arg_2_0.result == 6:
			pg.TipsMgr.GetInstance().ShowTips(i18n("login_createNewPlayer_full"))
		elif arg_2_0.result == 18:
			pg.TipsMgr.GetInstance().ShowTips(i18n("system_database_busy"))
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result]), False)

return var_0_0
