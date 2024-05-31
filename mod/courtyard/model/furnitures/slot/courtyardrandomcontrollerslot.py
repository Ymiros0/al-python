local var_0_0 = class("CourtYardRandomControllerSlot", import(".CourtYardFurnitureBaseSlot"))

def var_0_0.OnInit(arg_1_0, arg_1_1):
	arg_1_0.name = arg_1_1[1][1]
	arg_1_0.defaultAction = arg_1_1[1][2]
	arg_1_0.mask = arg_1_1[2] and arg_1_1[2][1]

	if arg_1_0.mask:
		arg_1_0.maskDefaultAction = arg_1_1[2][2]

	arg_1_0.actions = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1[3][2]):
		table.insert(arg_1_0.actions, {
			userAction = iter_1_1[3],
			controller = iter_1_1[2],
			ownerAction = iter_1_1[1]
		})

def var_0_0.SetAnimators(arg_2_0, arg_2_1):
	for iter_2_0, iter_2_1 in ipairs(arg_2_1[1]):
		table.insert(arg_2_0.animators, {
			key = arg_2_0.id .. "_" .. iter_2_0,
			value = iter_2_1
		})

def var_0_0.GetSpineDefaultAction(arg_3_0):
	return arg_3_0.defaultAction

def var_0_0.GetSpineMaskDefaultAcation(arg_4_0):
	return arg_4_0.maskDefaultAction

def var_0_0.OnAwake(arg_5_0):
	local var_5_0 = arg_5_0.actions[math.random(1, #arg_5_0.actions)]

	arg_5_0.animatorIndex = 0

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.animators):
		if iter_5_1.value == var_5_0.controller:
			arg_5_0.animatorIndex = iter_5_0

	arg_5_0.actionData = var_5_0

def var_0_0.OnStart(arg_6_0):
	local var_6_0 = arg_6_0.actionData

	arg_6_0.user.UpdateInteraction({
		action = var_6_0.userAction,
		slot = arg_6_0
	})
	arg_6_0.owner.UpdateInteraction({
		action = var_6_0.ownerAction,
		slot = arg_6_0
	})

def var_0_0.OnContinue(arg_7_0, arg_7_1):
	if arg_7_1 == arg_7_0.owner:
		arg_7_0.End()

def var_0_0.Clear(arg_8_0, arg_8_1):
	var_0_0.super.Clear(arg_8_0, arg_8_1)

	arg_8_0.actionData = None

return var_0_0
