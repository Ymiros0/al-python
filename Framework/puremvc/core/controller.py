local var_0_0 = import(".View")
local var_0_1 = import("..patterns.observer.Observer")
local var_0_2 = class("Controller")

def var_0_2.Ctor(arg_1_0, arg_1_1):
	if var_0_2.instanceMap[arg_1_1] != None:
		error(var_0_2.MULTITON_MSG)

	arg_1_0.multitonKey = arg_1_1
	var_0_2.instanceMap[arg_1_0.multitonKey] = arg_1_0
	arg_1_0.commandMap = {}

	arg_1_0.initializeController()

def var_0_2.initializeController(arg_2_0):
	arg_2_0.view = var_0_0.getInstance(arg_2_0.multitonKey)

def var_0_2.getInstance(arg_3_0):
	if arg_3_0 == None:
		return None

	if var_0_2.instanceMap[arg_3_0] == None:
		return var_0_2.New(arg_3_0)
	else
		return var_0_2.instanceMap[arg_3_0]

def var_0_2.executeCommand(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.commandMap[arg_4_1.getName()]

	if var_4_0 == None:
		return

	local var_4_1 = var_4_0.New()

	var_4_1.initializeNotifier(arg_4_0.multitonKey)
	var_4_1.execute(arg_4_1)

def var_0_2.registerCommand(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_0.commandMap[arg_5_1] == None:
		arg_5_0.view.registerObserver(arg_5_1, var_0_1.New(arg_5_0.executeCommand, arg_5_0))

	arg_5_0.commandMap[arg_5_1] = arg_5_2

def var_0_2.hasCommand(arg_6_0, arg_6_1):
	return arg_6_0.commandMap[arg_6_1] != None

def var_0_2.removeCommand(arg_7_0, arg_7_1):
	if arg_7_0.hasCommand(arg_7_1):
		arg_7_0.view.removeObserver(arg_7_1, arg_7_0)

		arg_7_0.commandMap[arg_7_1] = None

def var_0_2.removeController(arg_8_0):
	var_0_2.instanceMap[arg_8_0] = None

var_0_2.instanceMap = {}
var_0_2.MULTITON_MSG = "controller key for this Multiton key already constructed"

return var_0_2
