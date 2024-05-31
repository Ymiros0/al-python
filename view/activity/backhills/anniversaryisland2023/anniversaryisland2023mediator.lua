﻿local var_0_0 = class("AnniversaryIsland2023Mediator", import("..TemplateMV.BackHillMediatorTemplate"))

function var_0_0.register(arg_1_0)
	var_0_0.super.register(arg_1_0)

	local var_1_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2)

	arg_1_0:sendNotification(GAME.ACTIVITY_OPERATION, {
		cmd = 2,
		activity_id = var_1_0.id
	})
end

function var_0_0.listNotificationInterests(arg_2_0)
	local var_2_0 = var_0_0.super.listNotificationInterests(arg_2_0)

	table.insertto(var_2_0, {
		ActivityProxy.ACTIVITY_SHOW_AWARDS
	})

	return var_2_0
end

function var_0_0.handleNotification(arg_3_0, arg_3_1)
	var_0_0.super.handleNotification(arg_3_0, arg_3_1)

	local var_3_0 = arg_3_1:getName()
	local var_3_1 = arg_3_1:getBody()

	if var_3_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS then
		arg_3_0:addSubLayers(Context.New({
			mediator = AwardInfoMediator,
			viewComponent = AnniversaryIslandAwardLayer,
			data = {
				items = var_3_1.awards
			},
			onRemoved = var_3_1.callback
		}))
	end
end

function var_0_0.CheckPreloadData(arg_4_0, arg_4_1)
	if getProxy(ContextProxy):getContextByMediator(AnniversaryIsland2023Mediator) then
		local var_4_0 = getProxy(ContextProxy):getCurrentContext()

		arg_4_0.prevContext = arg_4_0.prevContext or var_4_0

		getProxy(ContextProxy):CleanUntilMediator(AnniversaryIsland2023Mediator)
	else
		local var_4_1 = Context.New()

		SCENE.SetSceneInfo(var_4_1, SCENE.ANNIVERSARY_ISLAND_BACKHILL_2023)

		local var_4_2 = getProxy(ContextProxy):getCurrentContext()

		var_4_1:extendData({
			fromMediatorName = var_4_2.mediator.__cname
		})
		getProxy(ContextProxy):pushContext(var_4_1)

		arg_4_0.prevContext = arg_4_0.prevContext or var_4_2
	end

	existCall(arg_4_1)
end

return var_0_0
