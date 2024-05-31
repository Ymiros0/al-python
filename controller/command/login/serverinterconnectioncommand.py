local var_0_0 = class("ServerInterconnectionCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.user
	local var_1_2 = var_1_0.platform
	local var_1_3 = getProxy(UserProxy)

	var_1_3.SetDefaultGateway()
	var_1_3.ActiveGatewaySwitcher()

	local function var_1_4(arg_2_0)
		NetConst.GATEWAY_HOST = arg_2_0.host
		NetConst.GATEWAY_PORT = arg_2_0.port
		NetConst.PROXY_GATEWAY_HOST = arg_2_0.proxyHost
		NetConst.PROXY_GATEWAY_PORT = arg_2_0.proxyPort

		originalPrint("switch to.", NetConst.GATEWAY_HOST, NetConst.GATEWAY_PORT)
		pg.m02.sendNotification(GAME.PLATFORM_LOGIN_DONE, {
			user = var_1_1
		})

	if var_1_3.ShouldSwitchGateway(var_1_2 or PLATFORM, var_1_1.arg2):
		local var_1_5 = var_1_2 or var_1_3.GetCacheGatewayFlag(var_1_1.arg2)
		local var_1_6 = var_1_3.GetGateWayByPlatform(var_1_5)

		if not var_1_6:
			arg_1_0.GetGateWayByServer(var_1_5, function(arg_3_0)
				var_1_3.SetGatewayForPlatform(var_1_5, arg_3_0)
				var_1_3.SetCacheGatewayFlag(var_1_5)
				var_1_4(arg_3_0))
		else
			var_1_3.SetCacheGatewayFlag(var_1_5)
			var_1_4(var_1_6)
	else
		pg.m02.sendNotification(GAME.PLATFORM_LOGIN_DONE, {
			user = var_1_1
		})

def var_0_0.GetGateWayByServer(arg_4_0, arg_4_1, arg_4_2):
	pg.ConnectionMgr.GetInstance().Connect(NetConst.GATEWAY_HOST, NetConst.GATEWAY_PORT, function()
		pg.ConnectionMgr.GetInstance().Send(10802, {
			platform = arg_4_1,
			state = NetConst.GatewayState
		}, 10803, function(arg_6_0)
			pg.ConnectionMgr.GetInstance().Disconnect()

			local var_6_0 = arg_6_0.gateway_ip
			local var_6_1 = arg_6_0.gateway_port
			local var_6_2 = System.String.IsNullOrEmpty(arg_6_0.proxy_ip)
			local var_6_3 = var_6_2 and var_6_0 or arg_6_0.proxy_ip
			local var_6_4 = var_6_2 and var_6_1 or arg_6_0.proxy_port
			local var_6_5 = GatewayInfo.New(var_6_0, var_6_1, var_6_3, var_6_4)

			arg_4_2(var_6_5)))

return var_0_0
