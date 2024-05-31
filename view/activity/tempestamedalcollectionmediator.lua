local var_0_0 = class("TempestaMedalCollectionMediator", import("..base.ContextMediator"))

var_0_0.ON_TASK_SUBMIT = "TempestaMedalCollectionMediator.ON_TASK_SUBMIT"
var_0_0.ON_TASK_GO = "TempestaMedalCollectionMediator.ON_TASK_GO"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_TASK_SUBMIT, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.SUBMIT_TASK, arg_2_1.id)
	end)
	arg_1_0:bind(var_0_0.ON_TASK_GO, function(arg_3_0, arg_3_1)
		arg_1_0:sendNotification(GAME.TASK_GO, {
			taskVO = arg_3_1
		})
	end)

	local var_1_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.PIRATE_MEDAL_ACT_ID)

	arg_1_0.viewComponent:setActivity(var_1_0)
end

function var_0_0.initNotificationHandleDic(arg_4_0)
	arg_4_0.handleDic = {
		[GAME.SUBMIT_TASK_DONE] = function(arg_5_0, arg_5_1)
			local var_5_0 = arg_5_1:getBody()

			arg_5_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_5_0, function()
				arg_5_0.viewComponent:updateTaskLayers()
			end)
		end
	}
end

return var_0_0
