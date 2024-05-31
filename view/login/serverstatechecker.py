local var_0_0 = class("ServerStateChecker")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = {
		True
	}

	seriesAsync({
		function(arg_2_0)
			onNextTick(arg_2_0),
		function(arg_3_0)
			arg_1_0.DoCheck(var_1_0, arg_3_0)
	}, function()
		arg_1_1(var_1_0[1]))

def var_0_0.DoCheck(arg_5_0, arg_5_1, arg_5_2):
	if IsUnityEditor:
		arg_5_1[1] = False

		arg_5_2()

		return

	pg.ConnectionMgr.GetInstance().Connect(NetConst.GATEWAY_HOST, NetConst.GATEWAY_PORT, function()
		pg.ConnectionMgr.GetInstance().Send(10018, {
			arg = 0
		}, 10019, function(arg_7_0)
			pg.ConnectionMgr.GetInstance().Disconnect()

			for iter_7_0, iter_7_1 in ipairs(arg_7_0.serverlist or {}):
				if iter_7_1.state != Server.STATUS.VINDICATE:
					arg_5_1[1] = False

					break

			arg_5_2()))

return var_0_0
