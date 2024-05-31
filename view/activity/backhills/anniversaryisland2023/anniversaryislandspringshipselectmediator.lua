local var_0_0 = class("AnniversaryIslandSpringShipSelectMediator", import("view.activity.BackHills.NewYearFestival.NewYearHotSpringShipSelectMediator"))

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.LOOG_PRESS_SHIP, function(arg_2_0, arg_2_1, arg_2_2)
		pg.m02:sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_2_2.id
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_CHUANWU, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0:sendNotification(AnniversaryIslandHotSpringMediator.OPEN_CHUANWU, {
			arg_3_1,
			arg_3_2
		})
	end)

	local var_1_0 = getProxy(ActivityProxy):getActivityById(arg_1_0.contextData.actId)

	arg_1_0.viewComponent:SetActivity(var_1_0)
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == GAME.EXTEND_BACKYARD_DONE then
		pg.TipsMgr.GetInstance():ShowTips(i18n("backyard_backyardShipInfoMediator_ok_unlock"))
		arg_4_0.viewComponent:UpdateSlots()
	elseif var_4_0 == ActivityProxy.ACTIVITY_UPDATED and var_4_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_HOTSPRING_2 then
		arg_4_0.viewComponent:SetActivity(var_4_1)
		arg_4_0.viewComponent:UpdateSlots()
	end
end

return var_0_0
