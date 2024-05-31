local var_0_0 = class("MiniGameRequestCommand", pm.SimpleCommand)

var_0_0.REQUEST_HUB_DATA = 1

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.type
	local var_1_2 = var_1_0.callback

	pg.ConnectionMgr.GetInstance().Send(26101, {
		type = var_1_1
	}, 26102, function(arg_2_0)
		local var_2_0 = getProxy(MiniGameProxy)

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.hubs):
			var_2_0.UpdataHubData(iter_2_1)

		if var_1_2:
			var_1_2()

		local var_2_1 = getProxy(MiniGameProxy)

		for iter_2_2, iter_2_3 in ipairs(pg.mini_game.all):
			var_2_1.RequestInitData(iter_2_3, True))

return var_0_0
