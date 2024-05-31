local var_0_0 = class("MiniGameShopFlushCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0 and var_1_0.callback

	pg.ConnectionMgr.GetInstance().Send(26154, {
		type = 0
	}, 26155, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(ShopsProxy).getMiniShop()

			var_2_0.setNextTime(arg_2_0.next_flash_time[1])
			getProxy(ShopsProxy).setMiniShop(var_2_0)

		if var_1_1:
			var_1_1(arg_2_0.result == 0))

return var_0_0
