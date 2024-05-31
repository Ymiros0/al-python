local var_0_0 = class("EducateCharCvLoader")

def var_0_0.Play(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	arg_1_0.Stop()

	local function var_1_0()
		pg.CriMgr.GetInstance().PlayCV_V3(arg_1_2, arg_1_1, function(arg_3_0)
			if arg_3_0:
				local var_3_0 = arg_3_0.GetLength() * 0.001

				arg_1_0._currentVoice = arg_3_0.playback

				arg_1_4(var_3_0)
			else
				arg_1_4(-1))

	if (arg_1_3 or 0) <= 0:
		var_1_0()
	else
		arg_1_0.timer = Timer.New(var_1_0, arg_1_3, 1)

		arg_1_0.timer.Start()

def var_0_0.Stop(arg_4_0):
	arg_4_0.RemoveTimer()

	if arg_4_0._currentVoice:
		arg_4_0._currentVoice.Stop(True)

def var_0_0.Unload(arg_5_0):
	arg_5_0.Stop()

def var_0_0.RemoveTimer(arg_6_0):
	if arg_6_0.timer:
		arg_6_0.timer.Stop()

		arg_6_0.timer = None

def var_0_0.Dispose(arg_7_0):
	arg_7_0.Unload()

return var_0_0
