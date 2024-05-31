local var_0_0 = class("SystemTimeUtil")

def var_0_0.Ctor(arg_1_0):
	return

def var_0_0.SetUp(arg_2_0, arg_2_1):
	arg_2_0.callback = arg_2_1

	arg_2_0.Flush()

def var_0_0.Flush(arg_3_0):
	local var_3_0 = pg.TimeMgr.GetInstance().GetServerHour()
	local var_3_1 = var_3_0 < 12 and "AM" or "PM"
	local var_3_2 = pg.TimeMgr.GetInstance().CurrentSTimeDesc("%M", True)

	if arg_3_0.callback:
		arg_3_0.callback(var_3_0, var_3_2, var_3_1)

	local var_3_3 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_3_4 = arg_3_0.GetSecondsToNextMinute(var_3_3)

	arg_3_0.AddTimer(var_3_4)

def var_0_0.GetSecondsToNextMinute(arg_4_0, arg_4_1):
	local var_4_0 = math.ceil(arg_4_1 / 60) * 60 - arg_4_1

	if var_4_0 <= 0:
		return 60

	return var_4_0

def var_0_0.AddTimer(arg_5_0, arg_5_1):
	arg_5_0.RemoveTimer()

	arg_5_0.timer = Timer.New(function()
		arg_5_0.Flush(), arg_5_1, 1)

	arg_5_0.timer.Start()

def var_0_0.RemoveTimer(arg_7_0):
	if arg_7_0.timer:
		arg_7_0.timer.Stop()

		arg_7_0.timer = None

def var_0_0.Dispose(arg_8_0):
	arg_8_0.RemoveTimer()

return var_0_0
