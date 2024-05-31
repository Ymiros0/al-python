local var_0_0 = class("MainSublayerSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0.GetContextData()

	if var_1_0 and var_1_0.subContext:
		var_1_0.subContext.onRemoved = arg_1_1

		arg_1_0.AddSubLayers(var_1_0.subContext)

		var_1_0.subContext = None
	else
		arg_1_1()

def var_0_0.GetContextData(arg_2_0):
	local var_2_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(NewMainMediator)

	return var_2_0 and var_2_0.data

def var_0_0.AddSubLayers(arg_3_0, arg_3_1):
	local var_3_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(NewMainMediator)

	pg.m02.sendNotification(GAME.LOAD_LAYERS, {
		parentContext = var_3_0,
		context = arg_3_1
	})

return var_0_0
