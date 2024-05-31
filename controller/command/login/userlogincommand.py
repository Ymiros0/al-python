local var_0_0 = class("UserLoginCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	assert(isa(var_1_0, User), "should be an instance of User")
	originalPrint("connect to gateway - " .. NetConst.GATEWAY_HOST .. "." .. NetConst.GATEWAY_PORT)

	local var_1_1 = pg.SdkMgr.GetInstance().GetChannelUID()

	if var_1_1 == "":
		var_1_1 = PLATFORM_LOCAL

	if not var_1_0.arg4:
		var_1_0.arg4 = "0"

	local var_1_2 = var_1_0.arg4 == "0" and var_1_0.arg3 or var_1_0.arg4

	originalPrint("login type -- . ", var_1_0.type, ", arg3 -- . ", var_1_2, ", sessionid -- . " .. var_1_0.arg4)
	pg.ConnectionMgr.GetInstance().SetProxyHost(NetConst.PROXY_GATEWAY_HOST, NetConst.PROXY_GATEWAY_PORT)
	pg.ConnectionMgr.GetInstance().Connect(NetConst.GATEWAY_HOST, NetConst.GATEWAY_PORT, function()
		pg.ConnectionMgr.GetInstance().Send(10020, {
			login_type = var_1_0.type,
			arg1 = var_1_0.arg1,
			arg2 = var_1_0.arg2,
			arg3 = var_1_2,
			arg4 = var_1_1,
			check_key = HashUtil.CalcMD5(var_1_0.arg1 .. AABBUDUD),
			device = PLATFORM
		}, 10021, function(arg_3_0)
			originalPrint("disconnect from gateway...")
			pg.ConnectionMgr.GetInstance().Disconnect()

			if arg_3_0.result == 0:
				var_1_0.id = arg_3_0.account_id
				var_1_0.uid = arg_3_0.account_id
				var_1_0.token = arg_3_0.server_ticket
				var_1_0.limitServerIds = arg_3_0.limit_server_ids

				local var_3_0 = getProxy(UserProxy)

				var_3_0.setLastLogin(var_1_0)
				var_3_0.SetLoginedFlag(True)

				local var_3_1 = {}
				local var_3_2 = {
					"*all gate info ."
				}

				for iter_3_0, iter_3_1 in ipairs(arg_3_0.serverlist):
					local var_3_3 = Server.New({
						id = iter_3_1.ids[1],
						host = iter_3_1.ip,
						port = iter_3_1.port,
						proxy_host = iter_3_1.proxy_ip,
						proxy_port = iter_3_1.proxy_port,
						status = iter_3_1.state,
						name = iter_3_1.name,
						tag_state = iter_3_1.tag_state,
						sort = iter_3_1.sort
					})

					var_3_2[#var_3_2 + 1] = iter_3_1.proxy_ip .. "." .. iter_3_1.proxy_port
					var_3_2[#var_3_2 + 1] = iter_3_1.ip .. "." .. iter_3_1.port

					var_3_3.display()
					table.insert(var_3_1, var_3_3)

				originalPrint(table.concat(var_3_2, "\n"))

				local var_3_4 = getProxy(ServerProxy)

				var_3_4.setServers(var_3_1, var_1_0.uid)

				if arg_3_0.limit_server_ids and #arg_3_0.limit_server_ids > 0:
					var_3_4.firstServer = None

				getProxy(GatewayNoticeProxy).setGatewayNotices(arg_3_0.notice_list)
				arg_1_0.facade.sendNotification(GAME.USER_LOGIN_SUCCESS, var_1_0)
				pg.PushNotificationMgr.GetInstance().cancelAll()
				originalPrint("user logined............", #var_3_1)
				pg.SdkMgr.GetInstance().SdkGateWayLogined()
			else
				pg.SdkMgr.GetInstance().SdkLoginGetaWayFailed()
				originalPrint("user login failed ............")

				if arg_3_0.result == 13:
					pg.TipsMgr.GetInstance().ShowTips(i18n("login_gate_not_ready"))
				elif arg_3_0.result == 15:
					pg.TipsMgr.GetInstance().ShowTips(i18n("login_game_rigister_full"))
				elif arg_3_0.result == 18:
					pg.TipsMgr.GetInstance().ShowTips(i18n("system_database_busy"))
				elif arg_3_0.result == 6:
					pg.TipsMgr.GetInstance().ShowTips(i18n("login_game_login_full"))
				else
					arg_1_0.facade.sendNotification(GAME.USER_LOGIN_FAILED, arg_3_0.result), False))

return var_0_0
