local var_0_0 = class("SendMsgCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(50102, {
		type = 1,
		content = var_1_0
	})

return var_0_0
