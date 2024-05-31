local var_0_0 = class("SynGraftingActivityCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().id
	local var_1_1 = getProxy(ActivityProxy)
	local var_1_2 = var_1_1.getActivitiesByType(ActivityConst.ACTIVITY_TYPE_GRAFTING)

	if #var_1_2 == 0:
		return

	local var_1_3 = var_1_1.getActivityById(var_1_0)

	if not var_1_3 or var_1_3.isEnd():
		return

	local function var_1_4(arg_2_0, arg_2_1)
		if not arg_2_0 or arg_2_0.isEnd():
			return False

		return arg_2_1 == arg_2_0.getConfig("config_id")

	for iter_1_0, iter_1_1 in ipairs(var_1_2):
		if var_1_4(iter_1_1, var_1_0):
			arg_1_0.HandleLinkAct(iter_1_1, var_1_3)

def var_0_0.HandleLinkAct(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_0.IsBuildShipType(arg_3_2.getConfig("type")):
		arg_3_0.SynBuildShipAct(arg_3_1, arg_3_2)

def var_0_0.IsBuildShipType(arg_4_0, arg_4_1):
	return arg_4_1 == ActivityConst.ACTIVITY_TYPE_BUILDSHIP_1 or arg_4_1 == ActivityConst.ACTIVITY_TYPE_BUILD or arg_4_1 == ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD

def var_0_0.SynBuildShipAct(arg_5_0, arg_5_1, arg_5_2):
	arg_5_1.data1 = arg_5_2.data1
	arg_5_1.data2 = arg_5_2.data2

	print("syn........", arg_5_1.data1, arg_5_1.data2)
	getProxy(ActivityProxy).updateActivity(arg_5_1)

return var_0_0
