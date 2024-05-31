local var_0_0 = class("BackYardOpenAddExpCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()

	print("add exp ::", var_1_0)
	pg.ConnectionMgr.GetInstance():Send(19015, {
		is_open = var_1_0
	})
	arg_1_0:sendNotification(GAME.OPEN_ADD_EXP_DONE)
end

return var_0_0
