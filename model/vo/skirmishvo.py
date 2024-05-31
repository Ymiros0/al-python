local var_0_0 = class("SkirmishVO", import(".BaseVO"))

var_0_0.TypeStoryOrExpedition = 1
var_0_0.TypeChapter = 2
var_0_0.StateInactive = 0
var_0_0.StateActive = 1
var_0_0.StateWorking = 2
var_0_0.StateClear = 3

def var_0_0.bindConfigTable(arg_1_0):
	return pg.activity_skirmish_event

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.id = arg_2_1
	arg_2_0.configId = arg_2_1
	arg_2_0.state = var_0_0.StateInactive
	arg_2_0.flagNew = None

def var_0_0.SetState(arg_3_0, arg_3_1):
	arg_3_1 = arg_3_1 or 0

	if arg_3_1 == arg_3_0.state:
		return

	if arg_3_0.state != None and arg_3_1 == SkirmishVO.StateWorking:
		arg_3_0.flagNew = True

	arg_3_0.state = arg_3_1

def var_0_0.GetState(arg_4_0):
	return arg_4_0.state

def var_0_0.GetType(arg_5_0):
	return arg_5_0.getConfig("type")

def var_0_0.GetEvent(arg_6_0):
	return arg_6_0.getConfig("event")

return var_0_0
