local var_0_0 = class("GuideSendNotifiesPlayer", import(".GuidePlayer"))

def var_0_0.OnExecution(arg_1_0, arg_1_1, arg_1_2):
	local var_1_0 = arg_1_1.GetNotifies()

	for iter_1_0, iter_1_1 in ipairs(var_1_0):
		pg.m02.sendNotification(iter_1_1.notify, iter_1_1.body)

	arg_1_2()

return var_0_0
