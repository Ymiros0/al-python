local var_0_0 = class("UrExchangeTrackingCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.trackType
	local var_1_2 = var_1_0.arg1
	local var_1_3 = var_1_0.arg2

	pg.ConnectionMgr.GetInstance().Send(11212, {
		track_typ = var_1_1,
		ship_tid = var_1_2,
		from = var_1_3
	})

return var_0_0
