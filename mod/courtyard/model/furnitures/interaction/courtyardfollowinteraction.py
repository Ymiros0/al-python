local var_0_0 = class("CourtYardFollowInteraction", import(".CourtYardInteraction"))

def var_0_0.OnStepEnd(arg_1_0):
	if arg_1_0.IsCompleteOwnerStep():
		arg_1_0.DoStep()

return var_0_0
