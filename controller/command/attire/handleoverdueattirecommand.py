local var_0_0 = class("HandleOverDueAttireCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(AttireProxy).getExpiredChaces()

	if #var_1_0 > 0:
		arg_1_0.sendNotification(GAME.HANDLE_OVERDUE_ATTIRE_DONE, var_1_0)

return var_0_0
