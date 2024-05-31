local var_0_0 = class("ActivityPermanentProxy", import(".NetProxy"))

def var_0_0.register(arg_1_0):
	arg_1_0.on(11210, function(arg_2_0)
		arg_1_0.finishActivity = {}

		underscore.each(arg_2_0.permanent_activity, function(arg_3_0)
			arg_1_0.finishActivity[arg_3_0] = True)

		arg_1_0.doingActivity = arg_2_0.permanent_now)

def var_0_0.startSelectActivity(arg_4_0, arg_4_1):
	arg_4_0.doingActivity = arg_4_1

def var_0_0.finishNowActivity(arg_5_0, arg_5_1):
	arg_5_0.finishActivity[arg_5_1] = True
	arg_5_0.doingActivity = 0

def var_0_0.isActivityFinish(arg_6_0, arg_6_1):
	return arg_6_0.finishActivity[arg_6_1]

def var_0_0.getDoingActivity(arg_7_0):
	if arg_7_0.doingActivity != 0:
		return getProxy(ActivityProxy).getActivityById(arg_7_0.doingActivity)

	return None

return var_0_0
