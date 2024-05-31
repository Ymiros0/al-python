local var_0_0 = import("..patterns.observer.Observer")
local var_0_1 = class("View")

def var_0_1.Ctor(arg_1_0, arg_1_1):
	if var_0_1.instanceMap[arg_1_1] != None:
		error(var_0_1.MULTITON_MSG)

	arg_1_0.multitonKey = arg_1_1
	var_0_1.instanceMap[arg_1_0.multitonKey] = arg_1_0
	arg_1_0.mediatorMap = {}
	arg_1_0.observerMap = {}

	arg_1_0.initializeView()

def var_0_1.initializeView(arg_2_0):
	return

def var_0_1.getInstance(arg_3_0):
	if arg_3_0 == None:
		return None

	if var_0_1.instanceMap[arg_3_0] == None:
		return var_0_1.New(arg_3_0)
	else
		return var_0_1.instanceMap[arg_3_0]

def var_0_1.registerObserver(arg_4_0, arg_4_1, arg_4_2):
	if arg_4_0.observerMap[arg_4_1] != None:
		table.insert(arg_4_0.observerMap[arg_4_1], arg_4_2)
	else
		if arg_4_1 == None:
			print(debug.traceback())

		arg_4_0.observerMap[arg_4_1] = {
			arg_4_2
		}

def var_0_1.notifyObservers(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0.observerMap[arg_5_1.getName()]

	if var_5_0 != None:
		local var_5_1 = table.shallowCopy(var_5_0)

		for iter_5_0, iter_5_1 in pairs(var_5_1):
			if table.contains(var_5_0, iter_5_1):
				iter_5_1.notifyObserver(arg_5_1)

		local var_5_2

def var_0_1.removeObserver(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = arg_6_0.observerMap[arg_6_1]

	for iter_6_0, iter_6_1 in pairs(var_6_0):
		if iter_6_1.compareNotifyContext(arg_6_2):
			table.remove(var_6_0, iter_6_0)

			break

	if #var_6_0 == 0:
		arg_6_0.observerMap[arg_6_1] = None

def var_0_1.registerMediator(arg_7_0, arg_7_1):
	if arg_7_0.mediatorMap[arg_7_1.getMediatorName()] != None:
		return

	arg_7_1.initializeNotifier(arg_7_0.multitonKey)

	arg_7_0.mediatorMap[arg_7_1.getMediatorName()] = arg_7_1

	local var_7_0 = arg_7_1.listNotificationInterests()

	if #var_7_0 > 0:
		local var_7_1 = var_0_0.New(arg_7_1.handleNotification, arg_7_1)

		for iter_7_0, iter_7_1 in pairs(var_7_0):
			arg_7_0.registerObserver(iter_7_1, var_7_1)

	arg_7_1.onRegister()

def var_0_1.retrieveMediator(arg_8_0, arg_8_1):
	return arg_8_0.mediatorMap[arg_8_1]

def var_0_1.removeMediator(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.mediatorMap[arg_9_1]

	if var_9_0 != None:
		local var_9_1 = var_9_0.listNotificationInterests()

		for iter_9_0, iter_9_1 in pairs(var_9_1):
			arg_9_0.removeObserver(iter_9_1, var_9_0)

		arg_9_0.mediatorMap[arg_9_1] = None

		var_9_0.onRemove()

	return var_9_0

def var_0_1.hasMediator(arg_10_0, arg_10_1):
	return arg_10_0.mediatorMap[arg_10_1] != None

def var_0_1.removeView(arg_11_0):
	var_0_1.instanceMap[arg_11_0] = None

var_0_1.instanceMap = {}
var_0_1.MULTITON_MSG = "View instance for this Multiton key already constructed!"

return var_0_1
