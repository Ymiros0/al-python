local var_0_0 = class("InstagramActivity", import("..Activity"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.configIds = arg_1_0.getConfig("config_data")
	arg_1_0.times = arg_1_0.data2_list

def var_0_0.UpdateActiveCnt(arg_2_0):
	arg_2_0.data1 = arg_2_0.data1 - 1

def var_0_0.GetNextPushTime(arg_3_0):
	local var_3_0 = getProxy(InstagramProxy)

	for iter_3_0, iter_3_1 in ipairs(arg_3_0.configIds):
		local var_3_1 = pg.activity_ins_template[iter_3_1].group_id
		local var_3_2 = arg_3_0.times[iter_3_0]

		if not var_3_0.ExistGroup(var_3_1):
			return var_3_2, iter_3_1

def var_0_0.GetCanActiveCnt(arg_4_0):
	return arg_4_0.data1

def var_0_0.CanBeActivated(arg_5_0):
	return True

def var_0_0.ExistMsg(arg_6_0):
	return #getProxy(InstagramProxy).GetMessages() > 0

return var_0_0
