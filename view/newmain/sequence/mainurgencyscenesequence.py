local var_0_0 = class("MainUrgencySceneSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = {
		"SkipToActivity",
		"SkipToReFluxActivity",
		"SkipToTechnology"
	}

	arg_1_0.NextOne(1, var_1_0, arg_1_1)

def var_0_0.NextOne(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	local var_2_0 = arg_2_0[arg_2_2[arg_2_1]](arg_2_0)

	if not var_2_0:
		return

	if var_2_0 and arg_2_1 < #arg_2_2:
		arg_2_0.NextOne(arg_2_1 + 1, arg_2_2, arg_2_3)
	else
		arg_2_3()

def var_0_0.SkipToActivity(arg_3_0):
	if getProxy(ActivityProxy).findNextAutoActivity():
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY)

		return False

	return True

def var_0_0.SkipToReFluxActivity(arg_4_0):
	local var_4_0 = getProxy(RefluxProxy)

	if var_4_0.isCanSign() and var_4_0.isInRefluxTime():
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.REFLUX)

		return False

	return True

def var_0_0.SkipToTechnology(arg_5_0):
	local var_5_0 = getProxy(PlayerProxy).getRawData().level

	if not LOCK_TECHNOLOGY and pg.SystemOpenMgr.GetInstance().isOpenSystem(var_5_0, "TechnologyMediator") and not pg.NewStoryMgr.GetInstance().IsPlayed("FANGAN1"):
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SELTECHNOLOGY)
		pg.NewStoryMgr.GetInstance().Play("FANGAN1", function()
			return, True)

		return False

	return True

return var_0_0
