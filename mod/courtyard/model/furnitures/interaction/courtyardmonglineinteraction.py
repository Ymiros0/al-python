local var_0_0 = class("CourtYardMonglineInteraction", import(".CourtYardInteraction"))

def var_0_0.DoStep(arg_1_0):
	arg_1_0.statesCnt[arg_1_0.host.user] = 1
	arg_1_0.statesCnt[arg_1_0.host.owner] = 1
	arg_1_0.totalUserActionCnt = #arg_1_0.userActions
	arg_1_0.totalOwnerActionCnt = #arg_1_0.ownerActions

	var_0_0.super.DoStep(arg_1_0)

def var_0_0.PlayUserAction(arg_2_0):
	local var_2_0 = arg_2_0.statesCnt[arg_2_0.host.user] + 1

	if var_2_0 > arg_2_0.totalUserActionCnt:
		return

	arg_2_0.statesCnt[arg_2_0.host.user] = var_2_0
	arg_2_0.states[arg_2_0.host.user] = False

	print("ship..............", var_2_0, arg_2_0.userActions[var_2_0])
	arg_2_0.host.GetUser().UpdateInteraction(arg_2_0.PackData(arg_2_0.userActions[var_2_0]))

def var_0_0.PlayOwnerAction(arg_3_0):
	local var_3_0 = arg_3_0.statesCnt[arg_3_0.host.owner] + 1

	if var_3_0 > arg_3_0.totalOwnerActionCnt:
		return

	arg_3_0.statesCnt[arg_3_0.host.owner] = var_3_0
	arg_3_0.states[arg_3_0.host.owner] = False

	print("furn", var_3_0, arg_3_0.ownerActions[var_3_0])
	arg_3_0.host.GetOwner().UpdateInteraction(arg_3_0.PackData(arg_3_0.ownerActions[var_3_0]))

def var_0_0.StepEnd(arg_4_0, arg_4_1):
	if arg_4_0.preheatProcess:
		arg_4_0.DoStep()

		arg_4_0.preheatProcess = False
	else
		if arg_4_0.index == 0:
			return

		arg_4_0.states[arg_4_1] = True

		if arg_4_0.host.GetUser() == arg_4_1:
			arg_4_0.PlayUserAction()
		elif arg_4_0.host.GetOwner() == arg_4_1:
			arg_4_0.PlayOwnerAction()

		if arg_4_0.IsFinishAll():
			arg_4_0.AllStepEnd()

def var_0_0.IsFinishAll(arg_5_0):
	return arg_5_0.statesCnt[arg_5_0.host.owner] >= arg_5_0.totalOwnerActionCnt and arg_5_0.statesCnt[arg_5_0.host.user] >= arg_5_0.totalUserActionCnt

def var_0_0.Clear(arg_6_0):
	var_0_0.super.Clear(arg_6_0)

	arg_6_0.statesCnt = {}

return var_0_0
