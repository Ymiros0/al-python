local var_0_0 = class("VoteFameHallMediator", import("..base.ContextMediator"))

var_0_0.ON_SUBMIT_TASK = "VoteFameHallMediator:ON_SUBMIT_TASK"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_SUBMIT_TASK, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.SUBMIT_TASK, arg_2_1)
	end)
	arg_1_0.viewComponent:SetPastVoteData(getProxy(VoteProxy):GetPastVoteData())
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		GAME.SUBMIT_TASK_DONE
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == GAME.SUBMIT_TASK_DONE then
		arg_4_0.viewComponent:UpdateTips(arg_4_0.viewComponent.year)
		arg_4_0.viewComponent:UpdateBtnsTip()
	end
end

return var_0_0
