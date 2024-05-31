local var_0_0 = class("ServerLoginCommand", pm.SimpleCommand)

var_0_0.LoginLastTime = 0
var_0_0.LoginSafeLock = 0

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	assert(isa(var_1_0, Server), "should be an instance of Server")

	local var_1_1 = var_1_0.getHost()
	local var_1_2 = var_1_0.getPort()

	originalPrint("connect to game server - " .. var_1_1 .. "." .. var_1_2)

	local var_1_3 = getProxy(UserProxy)
	local var_1_4 = var_1_3.getData()
	local var_1_5 = pg.SdkMgr.GetInstance().GetChannelUID()

	if var_1_5 == "":
		var_1_5 = PLATFORM_LOCAL

	local function var_1_6(arg_2_0)
		pg.ConnectionMgr.GetInstance().Send(10022, {
			platform = var_1_5,
			account_id = var_1_4.uid,
			server_ticket = arg_2_0 or var_1_4.token,
			serverid = var_1_0.id,
			check_key = HashUtil.CalcMD5(var_1_4.token .. AABBUDUD),
			device_id = pg.SdkMgr.GetInstance().GetDeviceId()
		}, 10023, function(arg_3_0)
			if arg_3_0.result == 0:
				originalPrint("connect success. " .. arg_3_0.user_id)

				if var_1_0.status == Server.STATUS.REGISTER_FULL and arg_3_0.user_id == 0:
					pg.TipsMgr.GetInstance().ShowTips(i18n("login_register_full"))
					pg.ConnectionMgr.GetInstance().onDisconnected(True)
				else
					var_1_4.token = arg_3_0.server_ticket
					var_1_4.server = var_1_0.id

					var_1_3.setLastLogin(var_1_4)
					var_1_3.SaveCacheGatewayFlag(var_1_4.arg2)
					getProxy(ServerProxy).setLastServer(var_1_0.id, var_1_4.uid)
					arg_1_0.sendNotification(GAME.SERVER_LOGIN_SUCCESS, {
						uid = arg_3_0.user_id
					})
					pg.TrackerMgr.GetInstance().Tracking(TRACKING_ROLE_LOGIN, None, arg_3_0.user_id)

					if arg_3_0.user_id == 0:
						pg.SdkMgr.GetInstance().ChooseServer(tostring(var_1_0.id), var_1_0.name)
			elif arg_3_0.result == 13:
				pg.TipsMgr.GetInstance().ShowTips(i18n("login_game_not_ready"))
			elif arg_3_0.result == 15:
				pg.TipsMgr.GetInstance().ShowTips(i18n("login_game_rigister_full"))
			elif arg_3_0.result == 17:
				arg_1_0.sendNotification(GAME.SERVER_LOGIN_FAILED_USER_BANNED, arg_3_0.user_id)
			elif arg_3_0.result == 6:
				pg.TipsMgr.GetInstance().ShowTips(i18n("login_game_login_full"))
			elif arg_3_0.result == 18:
				local var_3_0 = arg_3_0.db_load
				local var_3_1 = arg_3_0.server_load
				local var_3_2 = math.floor(var_3_0 / 100 + var_3_1 / 1000 + 1)

				arg_1_0.sendNotification(GAME.SERVER_LOGIN_WAIT, var_3_2)
			else
				arg_1_0.sendNotification(GAME.SERVER_LOGIN_FAILED, arg_3_0.result), False)

	local var_1_7 = os.time()

	var_0_0.LoginSafeLock = var_0_0.LoginSafeLock + 1

	if math.abs(var_1_7 - var_0_0.LoginLastTime) > 1 or var_0_0.LoginSafeLock >= 5:
		var_0_0.LoginLastTime = var_1_7
		var_0_0.LoginSafeLock = 0

		if pg.ConnectionMgr.GetInstance().getConnection() and pg.ConnectionMgr.GetInstance().isConnected():
			var_1_6()
		else
			pg.ConnectionMgr.GetInstance().SetProxyHost(var_1_0.proxyHost, var_1_0.proxyPort)
			pg.ConnectionMgr.GetInstance().Connect(var_1_1, var_1_2, function()
				originalPrint("server. " .. var_1_0.id .. " uid. " .. var_1_4.uid)
				var_1_6(), 6)
	else
		pg.TipsMgr.GetInstance().ShowTips(i18n("login_game_frequence"))

return var_0_0
