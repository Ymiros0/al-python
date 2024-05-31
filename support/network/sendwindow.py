pg = pg or {}

local var_0_0 = pg

var_0_0.SendWindow = class("SendWindow")

local var_0_1 = var_0_0.SendWindow
local var_0_2

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.connectionMgr = arg_1_1
	arg_1_0.packetIdx = defaultValue(arg_1_2, 0)
	arg_1_0.isSending = False
	arg_1_0.toSends = {}
	arg_1_0.retryCount = 0
	var_0_2 = {}

def var_0_1.setPacketIdx(arg_2_0, arg_2_1):
	arg_2_0.packetIdx = arg_2_1

def var_0_1.getPacketIdx(arg_3_0):
	return arg_3_0.packetIdx

def var_0_1.incPacketIdx(arg_4_0):
	arg_4_0.packetIdx = arg_4_0.packetIdx + 1

def var_0_1.Queue(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4, arg_5_5, arg_5_6, arg_5_7):
	table.insert(arg_5_0.toSends, {
		arg_5_1,
		arg_5_2,
		arg_5_3,
		arg_5_4 and function(arg_6_0)
			table.remove(arg_5_0.toSends, 1)
			arg_5_4(arg_6_0)

			if arg_6_0 and arg_6_0.result and arg_6_0.result == 0:
				var_0_0.SeriesGuideMgr.GetInstance().receiceProtocol(arg_5_3, arg_5_2, arg_6_0),
		arg_5_5,
		arg_5_6,
		arg_5_7
	})

	if arg_5_0.isSending:
		return

	arg_5_0.StartSend()

def var_0_1.StartSend(arg_7_0):
	if #arg_7_0.toSends > 0:
		arg_7_0.Send(unpack(arg_7_0.toSends[1]))
	else
		warning("No more packets to send.")

def var_0_1.Send(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4, arg_8_5, arg_8_6, arg_8_7):
	arg_8_0.isSending = True
	arg_8_0.currentCS = arg_8_1

	if arg_8_0.connectionMgr.isConnecting():
		arg_8_0.connectionMgr.needStartSend = True

		return

	local var_8_0 = arg_8_0.connectionMgr.getConnection()

	if not var_8_0:
		arg_8_0.connectionMgr.needStartSend = True

		arg_8_0.connectionMgr.Reconnect(function()
			return)

		return

	arg_8_5 = defaultValue(arg_8_5, True)
	arg_8_6 = defaultValue(arg_8_6, True)
	arg_8_7 = defaultValue(arg_8_7, SEND_TIMEOUT)

	local var_8_1 = arg_8_0.getPacketIdx()

	if arg_8_3 != None:
		var_0_0.UIMgr.GetInstance().LoadingOn()

		local var_8_2

		if arg_8_5:
			var_8_2 = arg_8_3 .. "_" .. var_8_1
		else
			var_8_2 = arg_8_3

		var_0_2[var_8_2] = function(arg_10_0)
			arg_8_0.isSending = False

			var_0_0.UIMgr.GetInstance().LoadingOff()
			arg_8_0.connectionMgr.resetHBTimer()

			if arg_8_0.timer:
				arg_8_0.timer.Stop()

				arg_8_0.timer = None

			arg_8_4(arg_10_0)

			if arg_8_6 and not arg_8_0.isSending and #arg_8_0.toSends > 0:
				arg_8_0.StartSend()
		arg_8_0.timer = Timer.New(function()
			var_0_0.UIMgr.GetInstance().LoadingOff()

			var_0_2[var_8_2] = None

			arg_8_0.setPacketIdx(var_8_1)

			if arg_8_0.retryCount > 3:
				arg_8_0.connectionMgr.onDisconnected(False, DISCONNECT_TIME_OUT)

				arg_8_0.retryCount = 0

			if PLATFORM_CODE == PLATFORM_CHT:
				arg_8_0.connectionMgr.SwitchProxy()

			warning("Network is timedOut, resend. " .. var_8_1 .. ", protocal. " .. arg_8_1)

			arg_8_0.retryCount = arg_8_0.retryCount + 1

			arg_8_0.StartSend(), arg_8_7, 1)

		arg_8_0.timer.Start()
	else
		arg_8_5 = False

	local var_8_3 = var_0_0.Packer.GetInstance().GetProtocolWithName("cs_" .. arg_8_1)

	local function var_8_4(arg_12_0, arg_12_1)
		for iter_12_0, iter_12_1 in pairs(arg_12_1):
			assert(arg_12_0[iter_12_0] != None, "key:es not exist. " .. iter_12_0)

			if type(iter_12_1) == "table":
				for iter_12_2, iter_12_3 in ipairs(iter_12_1):
					if arg_12_0[iter_12_0].add:
						var_8_4(arg_12_0[iter_12_0].add(), iter_12_3)
					else
						arg_12_0[iter_12_0].append(iter_12_3)
			else
				arg_12_0[iter_12_0] = iter_12_1

	local var_8_5 = var_8_3.GetMessage()

	var_8_4(var_8_5, arg_8_2)

	if arg_8_5:
		var_8_0.Send(var_0_0.Packer.GetInstance().Pack(var_8_1, var_8_3.GetId(), var_8_5))
		originalPrint("Network sent protocol. " .. arg_8_1 .. " with idx. " .. var_8_1)
		arg_8_0.incPacketIdx()
	else
		var_8_0.Send(var_0_0.Packer.GetInstance().Pack(0, var_8_3.GetId(), var_8_5))
		originalPrint("Network sent protocol. " .. arg_8_1 .. " without idx")

	if not arg_8_3:
		table.remove(arg_8_0.toSends, 1)

		if #arg_8_0.toSends > 0:
			arg_8_0.StartSend()
		else
			arg_8_0.isSending = False

def var_0_1.stopTimer(arg_13_0):
	if arg_13_0.timer:
		arg_13_0.timer.Stop()

		arg_13_0.timer = None

def var_0_1.onData(arg_14_0):
	originalPrint("Network Receive idx. " .. arg_14_0.idx .. " cmd. " .. arg_14_0.cmd)

	local var_14_0 = var_0_0.Packer.GetInstance().Unpack(arg_14_0.cmd, arg_14_0.getLuaStringBuffer())
	local var_14_1 = arg_14_0.cmd .. "_" .. arg_14_0.idx

	if var_0_2[var_14_1]:
		local var_14_2 = var_0_2[var_14_1]

		var_0_2[var_14_1] = None

		var_14_2(var_14_0)
	elif var_0_2[arg_14_0.cmd]:
		local var_14_3 = var_0_2[arg_14_0.cmd]

		var_0_2[arg_14_0.cmd] = None

		var_14_3(var_14_0)
