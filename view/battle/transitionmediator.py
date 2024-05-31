local var_0_0 = class("TransitionMediator", import("..base.ContextMediator"))

var_0_0.FINISH = "TransitionMediator.FINISH"

def var_0_0.register(arg_1_0):
	return

def var_0_0.remove(arg_2_0):
	return

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		GAME.LOAD_SCENE_DONE,
		GAME.BEGIN_STAGE_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == GAME.LOAD_SCENE_DONE:
		if var_4_1 == SCENE.TRANSITION:
			arg_4_0.contextData.afterLoadFunc()
	elif var_4_0 == GAME.BEGIN_STAGE_DONE:
		local var_4_2 = getProxy(ContextProxy).getContextByMediator(BattleMediator)

		if var_4_2:
			getProxy(ContextProxy).RemoveContext(var_4_2)

		arg_4_0.sendNotification(GAME.CHANGE_SCENE, SCENE.COMBATLOAD, var_4_1)

return var_0_0
