local var_0_0 = class("ActivityMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	local var_1_0 = arg_1_0.contextData.id

	arg_1_0.contextData.singleActivity = True

	arg_1_0.bind(ActivityMediator.EVENT_OPERATION, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, arg_2_1))
	arg_1_0.bind(ActivityMediator.EVENT_GO_SCENE, function(arg_3_0, arg_3_1, arg_3_2)
		if arg_3_1 == SCENE.SUMMER_FEAST:
			pg.NewStoryMgr.GetInstance().Play("TIANHOUYUYI1", function()
				arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SUMMER_FEAST))
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, arg_3_1, arg_3_2))

	local var_1_1 = getProxy(PlayerProxy).getRawData()

	arg_1_0.viewComponent.setPlayer(var_1_1)

	local var_1_2 = getProxy(BayProxy).getShipById(var_1_1.character)

	arg_1_0.viewComponent.setFlagShip(var_1_2)

	local var_1_3 = getProxy(ActivityProxy).getActivityById(var_1_0)

	arg_1_0.viewComponent.selectActivity(var_1_3)

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		ActivityProxy.ACTIVITY_ADDED,
		ActivityProxy.ACTIVITY_UPDATED,
		ActivityProxy.ACTIVITY_OPERATION_DONE,
		ActivityProxy.ACTIVITY_SHOW_AWARDS,
		GAME.ACT_NEW_PT_DONE,
		GAME.RETURN_AWARD_OP_DONE,
		GAME.MONOPOLY_AWARD_DONE,
		GAME.SUBMIT_TASK_DONE
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == ActivityProxy.ACTIVITY_ADDED or var_6_0 == ActivityProxy.ACTIVITY_UPDATED:
		arg_6_0.viewComponent.updateActivity(var_6_1)
	elif var_6_0 == ActivityProxy.ACTIVITY_OPERATION_DONE:
		-- block empty
	elif var_6_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS or var_6_0 == GAME.ACT_NEW_PT_DONE or var_6_0 == GAME.RETURN_AWARD_OP_DONE or var_6_0 == GAME.MONOPOLY_AWARD_DONE:
		arg_6_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_6_1.awards, var_6_1.callback)
	elif var_6_0 == GAME.SUBMIT_TASK_DONE:
		arg_6_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_6_1, function()
			arg_6_0.viewComponent.updateTaskLayers())
	elif var_6_0 == GAME.SEND_MINI_GAME_OP_DONE:
		local var_6_2 = {
			function(arg_8_0)
				local var_8_0 = var_6_1.awards

				if #var_8_0 > 0:
					if arg_6_0.viewComponent:
						arg_6_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_8_0, arg_8_0)
					else
						arg_6_0.emit(BaseUI.ON_ACHIEVE, var_8_0, arg_8_0)
				else
					arg_8_0()
		}

		seriesAsync(var_6_2)

return var_0_0
