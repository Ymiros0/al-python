local var_0_0 = class("ReloadSceneCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(ContextProxy):popContext()

	var_1_1:extendData(var_1_0)
	arg_1_0:sendNotification(GAME.LOAD_SCENE, {
		isReload = true,
		context = var_1_1
	})
end

return var_0_0
