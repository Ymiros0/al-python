local var_0_0 = class("GameMediator", pm.Mediator)

def var_0_0.listNotificationInterests(arg_1_0):
	return {
		GAME.GO_SCENE,
		GAME.GO_MINI_GAME,
		GAME.LOAD_SCENE_DONE,
		GAME.SEND_CMD_DONE
	}

def var_0_0.handleNotification(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_1.getName()
	local var_2_1 = arg_2_1.getBody()
	local var_2_2

	if var_2_0 == GAME.GO_SCENE:
		local var_2_3 = arg_2_1.getType()
		local var_2_4 = Context.New()

		var_2_4.extendData(var_2_3)
		SCENE.SetSceneInfo(var_2_4, var_2_1)
		print("load scene. " .. var_2_1)
		arg_2_0.sendNotification(GAME.LOAD_SCENE, {
			context = var_2_4
		})
	elif var_2_0 == GAME.GO_MINI_GAME:
		local var_2_5 = Context.New()
		local var_2_6 = var_2_1

		var_2_5.extendData({
			miniGameId = var_2_6
		})

		local var_2_7 = pg.mini_game[var_2_6]

		var_2_5.mediator = _G[var_2_7.mediator_name]
		var_2_5.viewComponent = _G[var_2_7.view_name]
		var_2_5.scene = var_2_7.view_name

		print("load minigame. " .. var_2_7.view_name)

		local var_2_8 = {
			context = var_2_5
		}
		local var_2_9 = arg_2_1.getType()

		table.merge(var_2_8, var_2_9)
		arg_2_0.sendNotification(GAME.LOAD_SCENE, var_2_8)
	elif var_2_0 == GAME.LOAD_SCENE_DONE:
		print("scene loaded. ", var_2_1)

		if var_2_1 == SCENE.LOGIN:
			pg.UIMgr.GetInstance().displayLoadingBG(False)
			pg.UIMgr.GetInstance().LoadingOff()
	elif var_2_0 == GAME.SEND_CMD_DONE:
		-- block empty

return var_0_0
