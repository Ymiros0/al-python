local var_0_0 = class("CourtYardBGMAgent", import(".CourtYardAgent"))
local var_0_1 = 0
local var_0_2 = 1

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.recoders = {}
	arg_1_0.playName = None
	arg_1_0.waitForStop = False
	arg_1_0.defaultBgm = arg_1_0.GetDefaultBgm()

	arg_1_0.PlayVoice(arg_1_0.defaultBgm)

def var_0_0.Play(arg_2_0, arg_2_1, arg_2_2):
	if not arg_2_1 or arg_2_1 == "":
		return

	arg_2_2 = arg_2_2 or var_0_1

	if not arg_2_0.recoders[arg_2_1]:
		arg_2_0.recoders = {}

		arg_2_0.PlayVoice(arg_2_1, function(arg_3_0)
			if arg_2_2 == var_0_2:
				arg_2_0.HandlePlayOnce(arg_3_0))

	arg_2_0.recoders[arg_2_1] = (arg_2_0.recoders[arg_2_1] or 0) + 1

def var_0_0.HandlePlayOnce(arg_4_0, arg_4_1):
	local var_4_0 = long2int(arg_4_1.length) * 0.001

	arg_4_0.AddTimerToStopBgm(var_4_0)

def var_0_0.AddTimerToStopBgm(arg_5_0, arg_5_1):
	arg_5_0.waitForStop = True
	arg_5_0.timer = Timer.New(function()
		arg_5_0.Reset()

		arg_5_0.waitForStop = False, arg_5_1, 1)

	arg_5_0.timer.Start()

def var_0_0.RemoveTimer(arg_7_0):
	if arg_7_0.timer:
		arg_7_0.timer.Stop()

		arg_7_0.timer = None

def var_0_0.Stop(arg_8_0, arg_8_1):
	if arg_8_0.waitForStop:
		return

	if not arg_8_0.recoders[arg_8_1]:
		return

	arg_8_0.recoders[arg_8_1] = arg_8_0.recoders[arg_8_1] - 1

	if arg_8_0.recoders[arg_8_1] == 0:
		arg_8_0.Reset()

def var_0_0.Reset(arg_9_0):
	arg_9_0.recoders = {}

	arg_9_0.PlayVoice(arg_9_0.defaultBgm)

def var_0_0.PlayVoice(arg_10_0, arg_10_1, arg_10_2):
	if arg_10_0.playName == arg_10_1:
		return

	local var_10_0 = "bgm-" .. arg_10_1

	CriWareMgr.Inst.PlayBGM(var_10_0, CriWareMgr.CRI_FADE_TYPE.FADE_INOUT, function(arg_11_0)
		if arg_11_0 == None:
			warning("Missing BGM ." .. (arg_10_1 or "NIL"))
		elif arg_10_2:
			arg_10_2(arg_11_0.cueInfo))

	arg_10_0.playName = arg_10_1

def var_0_0.Clear(arg_12_0):
	arg_12_0.RemoveTimer()

	arg_12_0.recoders = {}
	arg_12_0.playName = None
	arg_12_0.waitForStop = False

	pg.CriMgr.GetInstance().StopBGM()

def var_0_0.Dispose(arg_13_0):
	arg_13_0.recoders = None

	arg_13_0.RemoveTimer()

return var_0_0
