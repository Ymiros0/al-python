

class ConnectionMgr:

	var_0_2 = createLog("ConnectionMgr", LOG_CONNECTION)
	var_0_7 = False
	var_0_8 = {}

	ConnectionMgr.needStartSend = False

	def Connect(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
		ConnectionMgr.erroCode = arg_1_4
		var_0_14 = arg_1_3
		var_0_3 = Connection.New(arg_1_1, arg_1_2)

		UIMgr.GetInstance().LoadingOn()
		var_0_3.onConnected.AddListener(function()
			UIMgr.GetInstance().LoadingOff()
			var_0_2("Network Connected.")

			var_0_5 = arg_1_1
			var_0_6 = arg_1_2
			var_0_4 = var_0_4 or SendWindow.New(arg_1_0, 0)

			var_0_3.onData.AddListener(var_0_4.onData)

			if PLATFORM_CODE == PLATFORM_CHT:
				var_0_13 = IPAddress.New()

			pingDelay = -1
			var_0_7 = True
			var_0_10 = False

			arg_1_3()
			arg_1_0.resetHBTimer())
		var_0_3.onData.AddListener(arg_1_0.onData)
		var_0_3.onError.AddListener(arg_1_0.onError)
		var_0_3.onDisconnected.AddListener(arg_1_0.onDisconnected)

		var_0_10 = True

		var_0_3.Connect()
		originalPrint("connect to - " .. arg_1_1 .. "." .. arg_1_2)

	def ConnectByProxy(arg_3_0):
		VersionMgr.Inst.SetUseProxy(True)

		if arg_3_0.GetLastHost() != None and arg_3_0.GetLastPort() != "":
			originalPrint("switch proxy! reason. first connect error")
			arg_3_0.Connect(arg_3_0.GetLastHost(), arg_3_0.GetLastPort(), var_0_14)
		else:
			originalPrint("not proxy -> logout")
			m02.sendNotification(GAME.LOGOUT, {
				code = ConnectionMgr.erroCode or 3
			})

	def ConnectByDomain(arg_4_0, arg_4_1, arg_4_2):
		var_4_0 = LuaHelper.getHostByDomain(arg_4_1)
		var_4_1 = DEFAULT_PORT

		arg_4_0.Connect(var_4_0, var_4_1, arg_4_2)

	def Reconnect(arg_5_0, arg_5_1):
		if not var_0_5 or not var_0_6:
			warning("Network is not connected.")

			return

		if var_0_10:
			warning("connecting, please wait...")

			return

		if var_0_7 and var_0_3 != None:
			warning("Network is connected.")

			return

		var_0_11 = arg_5_1

		arg_5_0.stopHBTimer()
		var_0_4.stopTimer()
		originalPrint("reconnect --> " .. arg_5_0.GetLastHost() .. "." .. arg_5_0.GetLastPort())
		arg_5_0.Connect(arg_5_0.GetLastHost(), arg_5_0.GetLastPort(), function()
			var_6_0 = getProxy(UserProxy)
			var_6_1 = var_6_0.getData()
			var_6_2 = SdkMgr.GetInstance().GetChannelUID()

			if var_6_2 == "":
				var_6_2 = PLATFORM_LOCAL

			if not var_6_1 or not var_6_1.isLogin():
				if var_0_4.currentCS == 10020 and var_0_12 != DISCONNECT_TIME_OUT:
					arg_5_0.needStartSend = False

					var_0_4.StartSend()
				else:
					m02.sendNotification(GAME.LOGOUT, {
						code = 3
					})

				return

			var_0_4.Send(10022, {
				platform = var_6_2,
				account_id = var_6_1.uid,
				server_ticket = var_6_1.token,
				serverid = var_6_1.server,
				check_key = HashUtil.CalcMD5(var_6_1.token .. AABBUDUD),
				device_id = SdkMgr.GetInstance().GetDeviceId()
			}, 10023, function(arg_7_0)
				if arg_7_0.result == 0:
					originalPrint("reconnect success. " .. arg_7_0.user_id, " - ", arg_7_0.server_ticket)

					var_6_1.token = arg_7_0.server_ticket

					var_6_0.setLastLogin(var_6_1)
					arg_5_1()

					if var_0_12 != DISCONNECT_TIME_OUT and var_0_4.getPacketIdx() > 0:
						arg_5_0.needStartSend = False

						var_0_4.Send(11001, {
							timestamp = 1
						}, 11002, function(arg_8_0)
							TimeMgr.GetInstance().SetServerTime(arg_8_0.timestamp, arg_8_0.monday_0oclock_timestamp)
							m02.sendNotification(GAME.CHANGE_CHAT_ROOM, 0))

						var_7_0 = nowWorld()

						if var_7_0 and var_7_0.type != World.TypeBase:
							WorldConst.ReqWorldForServer()
					elif arg_5_0.needStartSend:
						arg_5_0.needStartSend = False

						var_0_4.StartSend()

					var_0_12 = None

					var_7_1 = getProxy(PlayerProxy)

					if var_7_1 and var_7_1.getInited():
						SecondaryPWDMgr.GetInstance().FetchData()

					NewGuideMgr.GetInstance().Resume()
					m02.sendNotification(GAME.ON_RECONNECTION)
				else:
					originalPrint("reconnect failed. " .. arg_7_0.result)
					m02.sendNotification(GAME.LOGOUT, {
						code = 199,
						tip = arg_7_0.result
					}), False, False))

	def onDisconnected(arg_9_0, arg_9_1):
		var_0_2("Network onDisconnected. " .. tostring(arg_9_0))

		var_0_12 = arg_9_1

		if var_0_3:
			if not arg_9_0:
				var_0_3.onDisconnected.RemoveAllListeners()

			var_0_3.Dispose()

			var_0_3 = None

		if arg_9_0:
			var_0_7 = False

		if var_0_10:
			UIMgr.GetInstance().LoadingOff()

		var_0_10 = False

	def onData(arg_10_0):
		if var_0_8[arg_10_0.cmd]:
			var_10_0 = Packer.GetInstance().Unpack(arg_10_0.cmd, arg_10_0.getLuaStringBuffer())

			for iter_10_0, iter_10_1 in ipairs(var_0_8[arg_10_0.cmd]):
				iter_10_1(var_10_0)

	def onError(arg_11_0):
		UIMgr.GetInstance().LoadingOff()

		arg_11_0 = tostring(arg_11_0)

		var_0_2("Network Error. " .. arg_11_0)

		if var_0_3:
			var_0_3.Dispose()

			var_0_3 = None

		function var_11_0()
			m02.sendNotification(GAME.LOGOUT, {
				code = ConnectionMgr.erroCode or 3
			})

		function var_11_1()
			return

		if var_0_10:
			var_0_10 = False
			var_11_1 = var_0_11

		ConnectionMgr.GetInstance().CheckProxyCounter()

		if var_0_5 and var_0_6:
			ConnectionMgr.GetInstance().stopHBTimer()

			if table.contains({
				"NotSocket"
			}, arg_11_0):
				ConnectionMgr.GetInstance().Reconnect(var_11_1)
			else:
				MsgboxMgr.GetInstance().CloseAndHide()
				MsgboxMgr.GetInstance().ShowMsgBox({
					modal = True,
					content = i18n("reconnect_tip", arg_11_0),
					def onYes:()
						ConnectionMgr.GetInstance().Reconnect(var_11_1),
					onNo = var_11_0,
					weight = LayerWeightConst.TOP_LAYER
				})
				NewStoryMgr.GetInstance().Stop()
				NewGuideMgr.GetInstance().Pause()
		else:
			ConnectionMgr.GetInstance().ConnectByProxy()

	def Send(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4, arg_15_5, arg_15_6):
		if not var_0_7:
			warning("Network is not connected. msgid " .. arg_15_1)
			m02.sendNotification(GAME.LOGOUT, {
				code = 5
			})

			return

		function var_15_0(arg_16_0)
			if arg_16_0.result == 9998:
				m02.sendNotification(GAME.EXTRA_PROTO_RESULT, {
					result = arg_16_0.result
				})
			else:
				arg_15_4(arg_16_0)

		var_0_4.Queue(arg_15_1, arg_15_2, arg_15_3, var_15_0, arg_15_5, None, arg_15_6)

	def setPacketIdx(arg_17_0, arg_17_1):
		var_0_4.setPacketIdx(arg_17_1)

	def On(arg_18_0, arg_18_1, arg_18_2):
		if var_0_8[arg_18_1] == None:
			var_0_8[arg_18_1] = {}

		table.insert(var_0_8[arg_18_1], arg_18_2)

	def Off(arg_19_0, arg_19_1, arg_19_2):
		if var_0_8[arg_19_1] == None:
			return

		if arg_19_2 == None:
			var_0_8[arg_19_1] = None
		else:
			for iter_19_0, iter_19_1 in ipairs(var_0_8[arg_19_1]):
				if iter_19_1 == arg_19_2:
					table.remove(var_0_8[arg_19_1], iter_19_0)

					break

	def Disconnect(arg_20_0):
		arg_20_0.stopHBTimer()

		var_0_8 = {}

		var_0_2("Manually Disconnect !!!")

		if var_0_3:
			var_0_3.Dispose()

			var_0_3 = None

		var_0_5 = None
		var_0_6 = None
		lastProxyHost = None
		lastProxyPort = None
		var_0_4 = None
		var_0_7 = False

	def getConnection(arg_21_0):
		return var_0_3

	def isConnecting(arg_22_0):
		return var_0_10

	def isConnected(arg_23_0):
		return var_0_7

	def stopHBTimer(arg_24_0):
		if var_0_9:
			var_0_9.Stop()

			var_0_9 = None

	def resetHBTimer(arg_25_0):
		arg_25_0.stopHBTimer()

		var_0_9 = Timer.New(function()
			heartTime = TimeUtil.GetSystemTime()

			arg_25_0.Send(10100, {
				need_request = 1
			}, 10101, function(arg_27_0)
				var_27_0 = TimeUtil.GetSystemTime() - heartTime

				if pingDelay == -1:
					pingDelay = var_27_0
				else:
					pingDelay = (var_27_0 + pingDelay) / 2, False), HEART_BEAT_TIMEOUT, -1, True)

		var_0_9.Start()

	var_0_15 = 0
	var_0_16 = 2
	var_0_17
	var_0_18

	def SetProxyHost(arg_28_0, arg_28_1, arg_28_2):
		var_0_17 = arg_28_1
		var_0_18 = arg_28_2

		originalPrint("Proxy host --> " .. var_0_17 .. "." .. var_0_18)

	def GetLastHost(arg_29_0):
		if VersionMgr.Inst.OnProxyUsing() and var_0_17 != None and var_0_17 != "":
			return var_0_17

		return var_0_5

	def GetLastPort(arg_30_0):
		if VersionMgr.Inst.OnProxyUsing() and var_0_18 != None and var_0_18 != 0:
			return var_0_18

		return var_0_6

	def CheckProxyCounter(arg_31_0):
		var_0_15 = var_0_15 + 1

		originalPrint("proxyCounter. " .. var_0_15)

		if not VersionMgr.Inst.OnProxyUsing() and var_0_15 == var_0_16:
			originalPrint("switch proxy! reason. " .. var_0_16 .. " error limit")
			VersionMgr.Inst.SetUseProxy(True)

	def SwitchProxy(arg_32_0):
		if var_0_13 and var_0_13.IsSpecialIP():
			if not VersionMgr.Inst.OnProxyUsing():
				originalPrint("switch proxy! reason. tw specialIP send timeout")
				VersionMgr.Inst.SetUseProxy(True)
			else:
				VersionMgr.Inst.SetUseProxy(False)

			ConnectionMgr.onDisconnected(False, DISCONNECT_TIME_OUT)
