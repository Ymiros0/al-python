local var_0_0 = class("CourtYardInteraction")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.host = arg_1_1
	arg_1_0.isReset = False

	arg_1_0.Clear()

def var_0_0.Update(arg_2_0, arg_2_1):
	arg_2_0.loop = arg_2_1

	arg_2_0.InitData()
	arg_2_0.DoPreheatStep(arg_2_0.ownerPreheat, arg_2_0.userPreheat)

def var_0_0.InitData(arg_3_0):
	local var_3_0, var_3_1, var_3_2, var_3_3, var_3_4, var_3_5 = arg_3_0.host.GetActions()

	arg_3_0.ownerPreheat = var_3_3
	arg_3_0.userPreheat = var_3_4
	arg_3_0.tailAction = var_3_5
	arg_3_0.ownerActions = var_3_0
	arg_3_0.userActions = var_3_1
	arg_3_0.closeBodyMask = var_3_2
	arg_3_0.total = #var_3_0
	arg_3_0.index = 0

def var_0_0.DoPreheatStep(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.preheatProcess = False

	if arg_4_1:
		arg_4_0.preheatProcess = True

		arg_4_0.host.GetOwner().UpdateInteraction(arg_4_0.PackData(arg_4_1))

		if arg_4_2:
			arg_4_0.host.GetUser().UpdateInteraction(arg_4_0.PackData(arg_4_2))
	else
		arg_4_0.DoStep()

def var_0_0.DoStep(arg_5_0):
	if arg_5_0.index >= arg_5_0.total:
		arg_5_0.AllStepEnd()

		return

	arg_5_0.index = arg_5_0.index + 1
	arg_5_0.states[arg_5_0.host.user] = False
	arg_5_0.states[arg_5_0.host.owner] = False

	arg_5_0.host.GetUser().UpdateInteraction(arg_5_0.PackData(arg_5_0.GetUserAction()))
	arg_5_0.host.GetOwner().UpdateInteraction(arg_5_0.PackData(arg_5_0.GetOwnerAction()))

	arg_5_0.isReset = False

def var_0_0.GetUserAction(arg_6_0):
	return arg_6_0.userActions[arg_6_0.index]

def var_0_0.GetOwnerAction(arg_7_0):
	return arg_7_0.ownerActions[arg_7_0.index]

def var_0_0.DoTailStep(arg_8_0):
	arg_8_0.index = 0

	arg_8_0.host.GetUser().UpdateInteraction(arg_8_0.PackData(arg_8_0.tailAction))
	arg_8_0.host.GetOwner().UpdateInteraction(arg_8_0.PackData(arg_8_0.tailAction))

def var_0_0.PackData(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.index / arg_9_0.total

	return {
		action = arg_9_1,
		slot = arg_9_0.host,
		closeBodyMask = arg_9_0.closeBodyMask[arg_9_0.index],
		progress = var_9_0,
		total = arg_9_0.total,
		index = arg_9_0.index,
		isReset = arg_9_0.isReset
	}

def var_0_0.StepEnd(arg_10_0, arg_10_1):
	if arg_10_0.preheatProcess:
		arg_10_0.DoStep()
	else
		if arg_10_0.index == 0:
			return

		arg_10_0.states[arg_10_1] = True

		arg_10_0.OnStepEnd()

def var_0_0.AllStepEnd(arg_11_0):
	if arg_11_0.loop and arg_11_0.total > 1:
		arg_11_0.isReset = True
		arg_11_0.index = 0

		arg_11_0.DoStep()
	elif arg_11_0.loop and arg_11_0.total == 1:
		-- block empty
	elif not arg_11_0.loop and arg_11_0.tailAction:
		arg_11_0.DoTailStep()
	else
		arg_11_0.host.End()
		arg_11_0.Clear()

def var_0_0.Clear(arg_12_0):
	arg_12_0.index = 0
	arg_12_0.states = {}
	arg_12_0.total = 0
	arg_12_0.loop = None

def var_0_0.GetIndex(arg_13_0):
	return arg_13_0.index

def var_0_0.IsCompleteStep(arg_14_0):
	return arg_14_0.IsCompleteUserStep() and arg_14_0.IsCompleteOwnerStep()

def var_0_0.IsCompleteUserStep(arg_15_0):
	return arg_15_0.states[arg_15_0.host.user] == True

def var_0_0.IsCompleteOwnerStep(arg_16_0):
	return arg_16_0.states[arg_16_0.host.owner] == True

def var_0_0.OnStepEnd(arg_17_0):
	if arg_17_0.IsCompleteStep():
		arg_17_0.DoStep()

def var_0_0.Reset(arg_18_0):
	return

return var_0_0
