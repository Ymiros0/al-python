local var_0_0 = class("MainAwakeSequenceView", import(".MainSequenceView"))

def var_0_0.Ctor(arg_1_0):
	arg_1_0.sequence = {
		MainCompatibleDataSequence.New(),
		MainRandomFlagShipSequence.New(),
		MainFixSettingDefaultValue.New()
	}

return var_0_0
