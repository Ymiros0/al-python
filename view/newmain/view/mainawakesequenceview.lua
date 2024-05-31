local var_0_0 = class("MainAwakeSequenceView", import(".MainSequenceView"))

function var_0_0.Ctor(arg_1_0)
	arg_1_0.sequence = {
		MainCompatibleDataSequence.New(),
		MainRandomFlagShipSequence.New(),
		MainFixSettingDefaultValue.New()
	}
end

return var_0_0
