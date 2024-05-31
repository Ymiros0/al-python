﻿local var_0_0 = class("LoadSceneCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()

	var_1_0.type = LOAD_TYPE_SCENE

	if not var_1_0.isReload then
		var_1_0.prevContext = var_1_0.prevContext or getProxy(ContextProxy):getCurrentContext()
	end

	SCENE.CheckPreloadData(var_1_0, function()
		arg_1_0:sendNotification(GAME.LOAD_CONTEXT, var_1_0)
	end)
end

return var_0_0
