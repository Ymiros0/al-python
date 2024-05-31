local var_0_0 = import("...patterns.mediator.Mediator")
local var_0_1 = class("StateMachine", var_0_0)

var_0_1.NAME = "StateMachine"
var_0_1.ACTION = var_0_1.NAME .. "/notes/action"
var_0_1.CHANGED = var_0_1.NAME .. "/notes/changed"
var_0_1.CANCEL = var_0_1.NAME .. "/notes/cancel"

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0, var_0_1.NAME, null)

	arg_1_0.states = {}

def var_0_1.onRegister(arg_2_0):
	if arg_2_0.initial != None:
		arg_2_0.transitionTo(arg_2_0.initial, null)

def var_0_1.registerState(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_1 == None or arg_3_0.states[arg_3_1.name] != None:
		return

	arg_3_0.states[arg_3_1.name] = arg_3_1

	if arg_3_2:
		arg_3_0.initial = arg_3_1

def var_0_1.retrieveState(arg_4_0, arg_4_1):
	return arg_4_0.states[arg_4_1]

def var_0_1.removeState(arg_5_0, arg_5_1):
	if arg_5_0.states[arg_5_1] == None:
		return

	arg_5_0.states[arg_5_1] = None

def var_0_1.transitionTo(arg_6_0, arg_6_1, arg_6_2):
	if arg_6_1 == None:
		return

	arg_6_0.canceled = False

	local var_6_0 = arg_6_0.getCurrentState()

	if var_6_0 != None and var_6_0.exiting != None:
		arg_6_0.sendNotification(var_6_0.exiting, arg_6_2, arg_6_1.name)

	if arg_6_0.canceled:
		arg_6_0.canceled = False

		return

	if arg_6_1.entering != None:
		arg_6_0.sendNotification(arg_6_1.entering, arg_6_2)

	if arg_6_0.canceled:
		arg_6_0.canceled = False

		return

	arg_6_0.setCurrentState(arg_6_1)

	if arg_6_1.changed != None:
		arg_6_0.sendNotification(arg_6_1.changed, arg_6_2)

	arg_6_0.sendNotification(var_0_1.CHANGED, arg_6_2, arg_6_1.name)

def var_0_1.listNotificationInterests(arg_7_0):
	return {
		var_0_1.ACTION,
		var_0_1.CANCEL
	}

def var_0_1.handleNotification(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.getName()

	if var_8_0 == var_0_1.ACTION:
		local var_8_1 = arg_8_1.getType()
		local var_8_2 = arg_8_0.getCurrentState().getTarget(var_8_1)

		if var_8_2 != None:
			local var_8_3 = arg_8_0.states[var_8_2]

			if var_8_3 != None:
				arg_8_0.transitionTo(var_8_3, arg_8_1.getBody())
			else
				print("state not found, target. " .. var_8_2)
		else
			print("target not found, action. " .. var_8_1)
	elif var_8_0 == var_0_1.CANCEL:
		arg_8_0.canceled = True

def var_0_1.getCurrentState(arg_9_0):
	return arg_9_0.viewComponent

def var_0_1.setCurrentState(arg_10_0, arg_10_1):
	arg_10_0.viewComponent = arg_10_1

return var_0_1
