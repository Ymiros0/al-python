local var_0_0 = class("AmusementParkMediator", import("..TemplateMV.BackHillMediatorTemplate"))

var_0_0.MINIGAME_OPERATION = "MINIGAME_OPERATION"
var_0_0.ACTIVITY_OPERATION = "ACTIVITY_OPERATION"

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

	local var_1_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF)

	assert(var_1_0, "Building Activity Not Found")

	arg_1_0.activity = var_1_0

	arg_1_0.viewComponent.UpdateActivity(var_1_0)

def var_0_0.BindEvent(arg_2_0):
	arg_2_0.bind(var_0_0.ACTIVITY_OPERATION, function(arg_3_0, arg_3_1)
		assert(arg_2_0.activity, "Cant Initialize Activity")

		arg_3_1.activity_id = arg_2_0.activity.id

		arg_2_0.sendNotification(GAME.ACTIVITY_OPERATION, arg_3_1))

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		GAME.SEND_MINI_GAME_OP_DONE,
		ActivityProxy.ACTIVITY_UPDATED
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == GAME.SEND_MINI_GAME_OP_DONE:
		local var_5_2 = {
			function(arg_6_0)
				local var_6_0 = var_5_1.awards

				if #var_6_0 > 0:
					arg_5_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_6_0, arg_6_0)
				else
					arg_6_0(),
			function(arg_7_0)
				arg_5_0.viewComponent.UpdateView()
		}

		seriesAsync(var_5_2)
	elif var_5_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_5_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF:
			arg_5_0.activity = var_5_1

			arg_5_0.viewComponent.UpdateActivity(var_5_1)
		elif var_5_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_SHOP_PROGRESS_REWARD:
			local var_5_3 = var_5_1

			arg_5_0.viewComponent.UpdateView()

return var_0_0
