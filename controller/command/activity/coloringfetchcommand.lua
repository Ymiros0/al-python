local var_0_0 = class("ColoringFetchCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().activityId

	pg.ConnectionMgr.GetInstance():Send(26008, {
		act_id = var_1_0
	}, 26001, function(arg_2_0)
		getProxy(ColoringProxy):netUpdateData(arg_2_0)
		arg_1_0:sendNotification(GAME.COLORING_FETCH_DONE)
	end)
end

return var_0_0
