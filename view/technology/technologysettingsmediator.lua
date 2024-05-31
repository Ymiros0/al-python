local var_0_0 = class("TechnologySettingsMediator", import("..base.ContextMediator"))

var_0_0.CHANGE_TENDENCY = "TechnologySettingsMediator.CHANGE_TENDENCY"
var_0_0.EXIT_CALL = "TechnologySettingsMediator.EXIT_CALL"

function var_0_0.register(arg_1_0)
	arg_1_0:bindEvent()
end

function var_0_0.bindEvent(arg_2_0)
	arg_2_0:bind(var_0_0.CHANGE_TENDENCY, function(arg_3_0, arg_3_1)
		arg_2_0:sendNotification(GAME.CHANGE_REFRESH_TECHNOLOGYS_TENDENCY, {
			pool_id = 2,
			tendency = arg_3_1
		})
	end)
end

function var_0_0.listNotificationInterests(arg_4_0)
	return {
		GAME.CHANGE_REFRESH_TECHNOLOGYS_TENDENCY_DONE,
		GAME.SELECT_TEC_TARGET_CATCHUP_DONE
	}
end

function var_0_0.handleNotification(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1:getName()
	local var_5_1 = arg_5_1:getBody()

	if var_5_0 == GAME.CHANGE_REFRESH_TECHNOLOGYS_TENDENCY_DONE then
		local var_5_2 = getProxy(TechnologyProxy):getTendency(2)

		arg_5_0.viewComponent:updateTendencyPage(var_5_2)
		arg_5_0.viewComponent:updateTendencyBtn(var_5_2)
	elseif var_5_0 == GAME.SELECT_TEC_TARGET_CATCHUP_DONE then
		arg_5_0.viewComponent:updateTargetCatchupPage(var_5_1.tecID)
		arg_5_0.viewComponent:updateTargetCatchupBtns()
	end
end

function var_0_0.remove(arg_6_0)
	arg_6_0:sendNotification(var_0_0.EXIT_CALL)
end

return var_0_0
