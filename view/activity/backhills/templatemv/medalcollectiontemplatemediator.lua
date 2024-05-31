﻿local var_0_0 = class("MedalCollectionTemplateMediator", import("view.base.ContextMediator"))

var_0_0.MEMORYBOOK_UNLOCK = "MEMORYBOOK_UNLOCK"

function var_0_0.register(arg_1_0)
	arg_1_0:BindEvent()

	local var_1_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_PUZZLA)

	arg_1_0.viewComponent:UpdateActivity(var_1_0)
end

function var_0_0.BindEvent(arg_2_0)
	arg_2_0:bind(var_0_0.MEMORYBOOK_UNLOCK, function(arg_3_0, ...)
		arg_2_0:sendNotification(GAME.MEMORYBOOK_UNLOCK, ...)
	end)
end

function var_0_0.listNotificationInterests(arg_4_0)
	return {
		ActivityProxy.ACTIVITY_OPERATION_DONE,
		GAME.MEMORYBOOK_UNLOCK_DONE,
		GAME.ACTIVITY_OPERATION_DONE,
		ActivityProxy.ACTIVITY_SHOW_AWARDS
	}
end

function var_0_0.handleNotification(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1:getName()
	local var_5_1 = arg_5_1:getBody()

	if var_5_0 == ActivityProxy.ACTIVITY_ADDED or var_5_0 == ActivityProxy.ACTIVITY_UPDATED then
		if var_5_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_PUZZLA then
			arg_5_0.viewComponent:UpdateActivity(var_5_1)
		end
	elseif var_5_0 == GAME.MEMORYBOOK_UNLOCK_DONE then
		local var_5_2 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_PUZZLA)

		arg_5_0.viewComponent:UpdateActivity(var_5_2)
		arg_5_0.viewComponent:UpdateAfterSubmit(var_5_1)
	elseif var_5_0 == ActivityProxy.ACTIVITY_OPERATION_DONE then
		local var_5_3 = getProxy(ActivityProxy):getActivityById(var_5_1)

		if var_5_3:getConfig("type") == ActivityConst.ACTIVITY_TYPE_PUZZLA then
			arg_5_0.viewComponent:UpdateActivity(var_5_3)
			arg_5_0.viewComponent:UpdateAfterFinalMedal()
		end
	elseif var_5_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS then
		if getProxy(ContextProxy):getContextByMediator(ActivityMediator) then
			return
		end

		arg_5_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_5_1.awards, var_5_1.callback)
	end
end

return var_0_0
