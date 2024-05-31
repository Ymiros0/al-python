pg = pg or {}

local var_0_0 = pg

var_0_0.SimpleConnectionMgr = singletonClass("SimpleConnectionMgr")

local var_0_1 = var_0_0.SimpleConnectionMgr
local var_0_2 = createLog("SimpleConnectionMgr", False)
local var_0_3
local var_0_4
local var_0_5 = False
local var_0_6 = {}
local var_0_7

def var_0_1.Connect(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	var_0_1.stopTimer()

	var_0_3 = Connection.New(arg_1_1, arg_1_2)

	var_0_0.UIMgr.GetInstance().LoadingOn()
	var_0_3.onConnected.AddListener(function()
		var_0_0.UIMgr.GetInstance().LoadingOff()
		var_0_2("Simple Network Connected.")

		var_0_4 = var_0_4 or var_0_0.SendWindow.New(arg_1_0, 0)

		var_0_3.onData.AddListener(var_0_4.onData)

		var_0_5 = True
		var_0_7 = False

		arg_1_3())
	var_0_3.onData.AddListener(arg_1_0.onData)
	var_0_3.onError.AddListener(arg_1_0.onError)
	var_0_3.onDisconnected.AddListener(arg_1_0.onDisconnected)

	var_0_7 = True

	var_0_3.Connect()

	arg_1_4 = defaultValue(arg_1_4, SEND_TIMEOUT)
	var_0_1.timer = Timer.New(function()
		if not var_0_5:
			warning("connect timeout error (custom). " .. arg_1_4)
			var_0_1.stopTimer()
			arg_1_0.onDisconnected(False, DISCONNECT_TIME_OUT)

			if var_0_1.errorCB:
				var_0_1.errorCB(), arg_1_4, 1)

	var_0_1.timer.Start()

def var_0_1.stopTimer():
	if var_0_1.timer:
		var_0_1.timer.Stop()

		var_0_1.timer = None

def var_0_1.onDisconnected(arg_5_0, arg_5_1):
	var_0_2("Simple Network onDisconnected. " .. tostring(arg_5_0))

	if var_0_3:
		if not arg_5_0:
			var_0_3.onDisconnected.RemoveAllListeners()

		var_0_3.Dispose()

		var_0_3 = None

	if arg_5_0:
		var_0_5 = False

	if var_0_7:
		var_0_0.UIMgr.GetInstance().LoadingOff()

	var_0_7 = False

def var_0_1.onData(arg_6_0):
	if var_0_6[arg_6_0.cmd]:
		local var_6_0 = var_0_0.Packer.GetInstance().Unpack(arg_6_0.cmd, arg_6_0.getLuaStringBuffer())

		for iter_6_0, iter_6_1 in ipairs(var_0_6[arg_6_0.cmd]):
			iter_6_1(var_6_0)

def var_0_1.SetErrorCB(arg_7_0, arg_7_1):
	var_0_1.errorCB = arg_7_1

def var_0_1.onError(arg_8_0):
	var_0_0.UIMgr.GetInstance().LoadingOff()
	var_0_1.stopTimer()

	arg_8_0 = tostring(arg_8_0)

	var_0_2("Simple Network Error. " .. arg_8_0)

	if var_0_3:
		var_0_3.Dispose()

		var_0_3 = None

	if var_0_7:
		var_0_7 = False

	if var_0_1.errorCB:
		var_0_1.errorCB()

def var_0_1.Send(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4, arg_9_5, arg_9_6):
	if not var_0_5:
		warning("Simple Network is not connected. msgid " .. arg_9_1)

		return

	var_0_4.Queue(arg_9_1, arg_9_2, arg_9_3, arg_9_4, arg_9_5, None, arg_9_6)

def var_0_1.setPacketIdx(arg_10_0, arg_10_1):
	var_0_4.setPacketIdx(arg_10_1)

def var_0_1.On(arg_11_0, arg_11_1, arg_11_2):
	if var_0_6[arg_11_1] == None:
		var_0_6[arg_11_1] = {}

	table.insert(var_0_6[arg_11_1], arg_11_2)

def var_0_1.Off(arg_12_0, arg_12_1, arg_12_2):
	if var_0_6[arg_12_1] == None:
		return

	if arg_12_2 == None:
		var_0_6[arg_12_1] = None
	else
		for iter_12_0, iter_12_1 in ipairs(var_0_6[arg_12_1]):
			if iter_12_1 == arg_12_2:
				table.remove(var_0_6[arg_12_1], iter_12_0)

				break

def var_0_1.Disconnect(arg_13_0):
	var_0_6 = {}

	var_0_2("Simple Network Disconnect !!!")

	if var_0_3:
		var_0_3.Dispose()

		var_0_3 = None

	var_0_4 = None
	var_0_5 = False

def var_0_1.Reconnect(arg_14_0, arg_14_1):
	arg_14_0.Disconnect()

	if var_0_1.errorCB:
		var_0_1.errorCB()

def var_0_1.resetHBTimer(arg_15_0):
	return

def var_0_1.getConnection(arg_16_0):
	return var_0_3

def var_0_1.isConnecting(arg_17_0):
	return var_0_7

def var_0_1.isConnected(arg_18_0):
	return var_0_5

def var_0_1.SwitchProxy(arg_19_0):
	return
