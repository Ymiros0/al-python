local var_0_0 = class("BiliTracker")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	return

def var_0_0.Tracking(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	if arg_2_1 == TRACKING_USER_LEVELUP:
		originalPrint("tracking lvl." .. arg_2_3)
		pg.SdkMgr.GetInstance().SdkLevelUp()

return var_0_0
