local var_0_0 = class("LoadLayersCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	var_1_0.type = LOAD_TYPE_LAYER

	var_1_0.context.extendData({
		isLayer = True
	})
	SCENE.CheckPreloadData(var_1_0, function()
		arg_1_0.sendNotification(GAME.LOAD_CONTEXT, var_1_0))

return var_0_0