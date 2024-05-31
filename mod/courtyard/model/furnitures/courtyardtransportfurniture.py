local var_0_0 = class("CourtYardTransportFurniture", import(".CourtYardFurniture"))

def var_0_0.InitSlots(arg_1_0):
	table.insert(arg_1_0.slots, CourtYardTransportSlot.New(1, arg_1_0.config.spine))

	if type(arg_1_0.config.animator) == "table":
		arg_1_0.slots[1].SetAnimators(arg_1_0.config.animator)

def var_0_0.IsUsing(arg_2_0):
	return #arg_2_0.GetUsingSlots() > 0

def var_0_0.Stop(arg_3_0):
	arg_3_0.slots[1].Stop()

return var_0_0
