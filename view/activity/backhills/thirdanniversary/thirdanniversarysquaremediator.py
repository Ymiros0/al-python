local var_0_0 = class("ThirdAnniversarySquareMediator", import("..TemplateMV.BackHillMediatorTemplate"))

var_0_0.MINIGAME_OPERATION = "MINIGAME_OPERATION"
var_0_0.ON_OPEN_TOWERCLIMBING_SIGNED = "ON_OPEN_TOWERCLIMBING_SIGNED"
var_0_0.ACTIVITY_OPERATION = "ACTIVITY_OPERATION"

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

	local var_1_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF)

	assert(var_1_0, "Building Activity Not Found")

	arg_1_0.activity = var_1_0

	arg_1_0.viewComponent.UpdateActivity(var_1_0)

def var_0_0.BindEvent(arg_2_0):
	var_0_0.super.BindEvent(arg_2_0)
	arg_2_0.bind(var_0_0.ON_OPEN_TOWERCLIMBING_SIGNED, function()
		arg_2_0.sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.TOWERCLIMBING_SIGN
		}))
	arg_2_0.bind(var_0_0.ACTIVITY_OPERATION, function(arg_4_0, arg_4_1)
		assert(arg_2_0.activity, "Cant Initialize Activity")

		arg_4_1.activity_id = arg_2_0.activity.id

		arg_2_0.sendNotification(GAME.ACTIVITY_OPERATION, arg_4_1))

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		GAME.SEND_MINI_GAME_OP_DONE,
		ActivityProxy.ACTIVITY_UPDATED
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == GAME.SEND_MINI_GAME_OP_DONE:
		local var_6_2 = {
			function(arg_7_0)
				local var_7_0 = var_6_1.awards

				if #var_7_0 > 0:
					arg_6_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_7_0, arg_7_0)
				else
					arg_7_0(),
			function(arg_8_0)
				arg_6_0.viewComponent.UpdateView()
		}

		seriesAsync(var_6_2)
	elif var_6_0 == ActivityProxy.ACTIVITY_UPDATED and var_6_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF:
		arg_6_0.activity = var_6_1

		arg_6_0.viewComponent.UpdateActivity(var_6_1)

return var_0_0
