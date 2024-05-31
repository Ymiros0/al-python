local var_0_0 = class("MainCVLoader")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	return

def var_0_0.Load(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	if arg_2_0.preCvCueSheetName == arg_2_1:
		arg_2_0.Play(arg_2_2, arg_2_3, arg_2_4)
	else
		arg_2_0.Unload()
		pg.CriMgr.GetInstance().LoadCueSheet(arg_2_1, function(arg_3_0)
			arg_2_0.preCvCueSheetName = arg_2_1

			if arg_3_0:
				arg_2_0.Play(arg_2_2, arg_2_3, arg_2_4)
			else
				arg_2_4(-1))

def var_0_0.Play(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	arg_4_0.Stop()

	local function var_4_0()
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(arg_4_1, function(arg_6_0)
			if arg_6_0:
				arg_4_0._currentVoice = arg_6_0.playback

				local var_6_0 = arg_6_0.GetLength() * 0.001

				arg_4_3(var_6_0)
			else
				arg_4_3(-1))

	if (arg_4_2 or 0) <= 0:
		var_4_0()
	else
		arg_4_0.timer = Timer.New(var_4_0, arg_4_2, 1)

		arg_4_0.timer.Start()

def var_0_0.Stop(arg_7_0):
	arg_7_0.RemoveTimer()

	if arg_7_0._currentVoice:
		arg_7_0._currentVoice.Stop(True)

def var_0_0.Unload(arg_8_0):
	arg_8_0.Stop()

	if arg_8_0.preCvCueSheetName:
		pg.CriMgr.GetInstance().UnloadCueSheet(arg_8_0.preCvCueSheetName)

		arg_8_0.preCvCueSheetName = None

def var_0_0.RemoveTimer(arg_9_0):
	if arg_9_0.timer:
		arg_9_0.timer.Stop()

		arg_9_0.timer = None

def var_0_0.Dispose(arg_10_0):
	arg_10_0.Unload()

return var_0_0
