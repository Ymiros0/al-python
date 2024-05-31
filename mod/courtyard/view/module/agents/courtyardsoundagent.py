local var_0_0 = class("CourtYardSoundAgent", import(".CourtYardAgent"))

def var_0_0.Play(arg_1_0, arg_1_1):
	if not arg_1_1:
		return

	arg_1_0.Stop()

	arg_1_0.curVoiceKey = arg_1_1

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(arg_1_0.curVoiceKey)

def var_0_0.Stop(arg_2_0):
	if arg_2_0.curVoiceKey != None:
		pg.CriMgr.GetInstance().UnloadSoundEffect_V3(arg_2_0.curVoiceKey)

	arg_2_0.curVoiceKey = None

def var_0_0.Clear(arg_3_0):
	arg_3_0.Stop()

def var_0_0.Dispose(arg_4_0):
	arg_4_0.Stop()

return var_0_0
