local var_0_0 = class("OpenOrCloseCatteryCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().open
	local var_1_1 = var_1_0 and 0 or 1

	pg.ConnectionMgr.GetInstance().Send(25036, {
		is_open = var_1_1
	})

	local var_1_2 = getProxy(CommanderProxy)

	var_1_2.UpdateOpenCommanderScene(var_1_0)

	if var_1_0:
		local var_1_3 = var_1_2.GetCommanderHome()

		if var_1_3:
			local var_1_4 = var_1_3.GetCatteries()

			for iter_1_0, iter_1_1 in pairs(var_1_4):
				iter_1_1.ClearCacheExp()

return var_0_0
