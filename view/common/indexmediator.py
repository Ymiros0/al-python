local var_0_0 = class("IndexMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	assert(arg_1_0.contextData.display)

	if arg_1_0.contextData.display.sort:
		assert(arg_1_0.contextData.sort)

	if arg_1_0.contextData.display.index:
		assert(arg_1_0.contextData.index)

	if arg_1_0.contextData.display.camp:
		assert(arg_1_0.contextData.camp)

	if arg_1_0.contextData.display.rarity:
		assert(arg_1_0.contextData.rarity)

def var_0_0.listNotificationInterests(arg_2_0):
	return {}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	return

return var_0_0
