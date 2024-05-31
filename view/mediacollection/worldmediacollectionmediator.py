local var_0_0 = class("WorldMediaCollectionMediator", ContextMediator)

var_0_0.BEGIN_STAGE = "WorldMediaCollectionMediator BEGIN_STAGE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.BEGIN_STAGE, function(arg_2_0, arg_2_1)
		arg_1_0.contextData.revertBgm = pg.CriMgr.GetInstance().bgmNow

		arg_1_0.sendNotification(GAME.BEGIN_STAGE, arg_2_1))

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		PlayerProxy.UPDATED,
		GAME.BEGIN_STAGE_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == PlayerProxy.UPDATED:
		arg_4_0.viewComponent.UpdateView()
	elif var_4_0 == GAME.BEGIN_STAGE_DONE:
		arg_4_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_4_1)

return var_0_0
