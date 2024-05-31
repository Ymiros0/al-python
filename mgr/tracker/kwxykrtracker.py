local var_0_0 = class("KwxyKrTracker")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	return

def var_0_0.Tracking(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	if arg_2_1 == TRACKING_TUTORIAL_COMPLETE_1:
		pg.SdkMgr.GetInstance().CompletedTutorial()
		pg.SdkMgr.GetInstance().UnlockAchievement()
	elif arg_2_1 == TRACKING_USER_LEVELUP:
		pg.SdkMgr.GetInstance().SdkLevelUp(arg_2_4, arg_2_3)

return var_0_0
