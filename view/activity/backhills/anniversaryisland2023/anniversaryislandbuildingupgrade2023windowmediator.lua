﻿local var_0_0 = class("AnniversaryIslandBuildingUpgrade2023WindowMediator", import("view.base.ContextMediator"))

var_0_0.ACTIVITY_OPERATION = "ACTIVITY_OPERATION"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ACTIVITY_OPERATION, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.ACTIVITY_OPERATION, arg_2_1)
	end)
	arg_1_0:bind(WorkBenchItemDetailMediator.SHOW_DETAIL, function(arg_3_0, arg_3_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = WorkBenchItemDetailMediator,
			viewComponent = WorkBenchItemDetailLayer,
			data = {
				material = arg_3_1
			}
		}))
	end)
end

function var_0_0.listNotificationInterests(arg_4_0)
	return {
		ActivityProxy.ACTIVITY_UPDATED
	}
end

function var_0_0.handleNotification(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1:getName()
	local var_5_1 = arg_5_1:getBody()

	if var_5_0 == ActivityProxy.ACTIVITY_UPDATED and var_5_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2 then
		arg_5_0.viewComponent:UpdateView()
	end
end

function var_0_0.remove(arg_6_0)
	return
end

return var_0_0
