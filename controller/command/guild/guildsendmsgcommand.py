local var_0_0 = class("GuildSendMsgCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(60007, {
		chat = var_1_0
	})

return var_0_0
