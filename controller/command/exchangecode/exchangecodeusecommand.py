local var_0_0 = class("ExchangeCodeUseCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().key
	local var_1_1 = pg.SdkMgr.GetInstance().GetChannelUID()

	if var_1_1 == "":
		var_1_1 = PLATFORM_LOCAL

	pg.ConnectionMgr.GetInstance().Send(11508, {
		key = var_1_0,
		platform = var_1_1
	}, 11509, function(arg_2_0)
		if arg_2_0.result == 0:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = True,
				content = i18n("exchangecode_use_ok")
			})
			pg.m02.sendNotification(GAME.EXCHANGECODE_USE_SUCCESS)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("exchangecode_use", arg_2_0.result)))

return var_0_0