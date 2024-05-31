local var_0_0 = class("OtherworldTerminalMediator", import("view.base.ContextMediator"))

var_0_0.ON_GET_PT_ALL_AWARD = "OtherworldTerminalMediator.ON_GET_PT_AWARD"
var_0_0.ON_BUFF_LIST_CHANGE = "OtherworldTerminalMediator.ON_BUFF_LIST_CHANGE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_GET_PT_ALL_AWARD, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.ACT_NEW_PT, {
			cmd = 4,
			activity_id = arg_2_1.actId,
			arg1 = arg_2_1.arg1
		}))
	arg_1_0.bind(var_0_0.ON_BUFF_LIST_CHANGE, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 3,
			activity_id = arg_3_1.actId,
			arg_list = arg_3_1.ids
		}))

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		ActivityProxy.ACTIVITY_UPDATED,
		GAME.ACT_NEW_PT_DONE
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == ActivityProxy.ACTIVITY_UPDATED:
		local var_5_2 = var_5_1

		if var_5_2.id == TerminalAdventurePage.BIND_PT_ACT_ID:
			arg_5_0.viewComponent.UpdateAdventurePtAct(var_5_2)
		elif var_5_2.id == TerminalAdventurePage.BIND_TASK_ACT_ID:
			arg_5_0.viewComponent.UpdateAdventureTaskAct(var_5_2)
		elif var_5_2.id == ActivityConst.OTHER_WORLD_TERMINAL_LOTTERY_ID:
			arg_5_0.viewComponent.UpdateGuardianAct(var_5_2)
	elif var_5_0 == GAME.ACT_NEW_PT_DONE:
		arg_5_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_5_1.awards)
		arg_5_0.viewComponent.UpdateAdventureTip()

return var_0_0
