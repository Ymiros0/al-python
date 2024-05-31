local var_0_0 = class("ConfirmSecondaryPasswordCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.UIMgr.GetInstance().LoadingOn()
	pg.ConnectionMgr.GetInstance().Send(11609, {
		password = var_1_0.pwd
	}, 11610, function(arg_2_0)
		pg.UIMgr.GetInstance().LoadingOff()

		if arg_2_0.result == 0:
			local var_2_0 = getProxy(SecondaryPWDProxy).getRawData()

			var_2_0.state = 2
			var_2_0.fail_cd = None
			var_2_0.fail_count = 0

		arg_1_0.sendNotification(GAME.CONFIRM_PASSWORD_DONE, arg_2_0))

return var_0_0
