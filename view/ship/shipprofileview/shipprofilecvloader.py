local var_0_0 = class("ShipProfileCVLoader")
local var_0_1 = pg.ship_skin_words

def var_0_0.Ctor(arg_1_0):
	arg_1_0.loadedCVBankName = None
	arg_1_0.loadedCVBattleBankName = None
	arg_1_0.playbackInfo = None
	arg_1_0.timers = {}

def var_0_0.Load(arg_2_0, arg_2_1):
	arg_2_0.ClearSound()

	if ShipWordHelper.ExistVoiceKey(arg_2_1):
		local var_2_0 = ShipWordHelper.RawGetCVKey(arg_2_1)

		arg_2_0.SetUp(var_2_0)

def var_0_0.SetUp(arg_3_0, arg_3_1):
	local function var_3_0()
		local var_4_0 = pg.CriMgr.GetCVBankName(arg_3_1)
		local var_4_1 = pg.CriMgr.GetBattleCVBankName(arg_3_1)

		if arg_3_0.exited:
			pg.CriMgr.UnloadCVBank(var_4_0)
			pg.CriMgr.UnloadCVBank(var_4_1)
		else
			arg_3_0.loadedCVBankName = var_4_0
			arg_3_0.loadedCVBattleBankName = var_4_1

	seriesAsync({
		function(arg_5_0)
			pg.CriMgr.GetInstance().LoadCV(arg_3_1, arg_5_0),
		function(arg_6_0)
			pg.CriMgr.GetInstance().LoadBattleCV(arg_3_1, arg_6_0)
	}, var_3_0)

def var_0_0.PlaySound(arg_7_0, arg_7_1, arg_7_2):
	if not arg_7_0.playbackInfo or arg_7_1 != arg_7_0.prevCvPath or arg_7_0.playbackInfo.channelPlayer == None:
		arg_7_0.StopSound()
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(arg_7_1, function(arg_8_0)
			if arg_8_0:
				arg_7_0.playbackInfo = arg_8_0

				arg_7_0.playbackInfo.SetIgnoreAutoUnload(True)

				if arg_7_2:
					arg_7_2(arg_7_0.playbackInfo.cueInfo)
			elif arg_7_2:
				arg_7_2())

		arg_7_0.prevCvPath = arg_7_1

		if arg_7_0.playbackInfo == None:
			return None

		return arg_7_0.playbackInfo.cueInfo
	elif arg_7_0.playbackInfo:
		arg_7_0.playbackInfo.PlaybackStop()
		arg_7_0.playbackInfo.SetStartTimeAndPlay()

		if arg_7_2:
			arg_7_2(arg_7_0.playbackInfo.cueInfo)

		return arg_7_0.playbackInfo.cueInfo
	elif arg_7_2:
		arg_7_2()

	return None

def var_0_0.DelayPlaySound(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	arg_9_0.RemoveTimer(arg_9_1)

	if arg_9_2 > 0:
		arg_9_0.timers[arg_9_1] = Timer.New(function()
			local var_10_0 = arg_9_0.PlaySound(arg_9_1, function(arg_11_0)
				if arg_9_3:
					arg_9_3(arg_11_0)), arg_9_2, 1)

		arg_9_0.timers[arg_9_1].Start()
	else
		local var_9_0 = arg_9_0.PlaySound(arg_9_1, function(arg_12_0)
			if arg_9_3:
				arg_9_3(arg_12_0))

def var_0_0.RawPlaySound(arg_13_0, arg_13_1, arg_13_2):
	arg_13_0.RemoveTimer(arg_13_1)

	if arg_13_2 > 0:
		arg_13_0.timers[arg_13_1] = Timer.New(function()
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(arg_13_1), arg_13_2, 1)

		arg_13_0.timers[arg_13_1].Start()
	else
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(arg_13_1)

def var_0_0.RemoveTimer(arg_15_0, arg_15_1):
	if arg_15_0.timers[arg_15_1]:
		arg_15_0.timers[arg_15_1].Stop()

		arg_15_0.timers[arg_15_1] = None

def var_0_0.StopSound(arg_16_0):
	if arg_16_0.playbackInfo:
		pg.CriMgr.GetInstance().StopPlaybackInfoForce(arg_16_0.playbackInfo)
		arg_16_0.playbackInfo.SetIgnoreAutoUnload(False)

def var_0_0.Unload(arg_17_0):
	if arg_17_0.loadedCVBankName:
		pg.CriMgr.UnloadCVBank(arg_17_0.loadedCVBankName)

		arg_17_0.loadedCVBankName = None

	if arg_17_0.loadedCVBattleBankName:
		pg.CriMgr.UnloadCVBank(arg_17_0.loadedCVBattleBankName)

		arg_17_0.loadedCVBattleBankName = None

def var_0_0.ClearSound(arg_18_0):
	arg_18_0.StopSound()
	arg_18_0.Unload()

	if arg_18_0.playbackInfo:
		arg_18_0.playbackInfo.Dispose()

		arg_18_0.playbackInfo = None

def var_0_0.Dispose(arg_19_0):
	arg_19_0.ClearSound()

	arg_19_0.exited = True

	for iter_19_0, iter_19_1 in pairs(arg_19_0.timers):
		iter_19_1.Stop()

	arg_19_0.timers = None

return var_0_0
