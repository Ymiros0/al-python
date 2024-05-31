local var_0_0 = class("NewPlayerMediator", import("..base.ContextMediator"))

var_0_0.ON_CREATE = "NewPlayerMediator.ON_CREATE"
var_0_0.ON_SKILLINFO = "NewPlayerMediator.ON_SKILLINFO"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_CREATE, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.CREATE_NEW_PLAYER, {
			nickname = arg_2_1,
			shipId = arg_2_2
		}))
	arg_1_0.bind(var_0_0.ON_SKILLINFO, function(arg_3_0, arg_3_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = SkillInfoMediator,
			viewComponent = SkillInfoLayer,
			data = {
				fromNewShip = True,
				skillId = arg_3_1
			}
		})))

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		GAME.CREATE_NEW_PLAYER_DONE,
		GAME.LOAD_PLAYER_DATA_DONE
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == GAME.CREATE_NEW_PLAYER_DONE:
		arg_5_0.facade.sendNotification(GAME.LOAD_PLAYER_DATA, {
			isNewPlayer = True,
			id = var_5_1
		})
	elif var_5_0 == GAME.LOAD_PLAYER_DATA_DONE:
		arg_5_0.sendNotification(GAME.GO_SCENE, SCENE.MAINUI)

return var_0_0
