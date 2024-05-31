local var_0_0 = class("NewServerShop", import("..BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.startTime = arg_1_1.start_time
	arg_1_0.stopTime = arg_1_1.stop_time
	arg_1_0.goods = {}
	arg_1_0.phases = {}
	arg_1_0.activityId = arg_1_1.id

	local var_1_0 = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.goods):
		var_1_0[iter_1_1.id] = NewServerCommodity.New(iter_1_1)

	local var_1_1 = getProxy(ActivityProxy).getActivityById(arg_1_0.activityId)
	local var_1_2 = {}

	for iter_1_2, iter_1_3 in ipairs(var_1_1.getConfig("config_data")):
		var_1_2[iter_1_3] = True

	local var_1_3 = pg.newserver_shop_template.get_id_list_by_unlock_time

	for iter_1_4, iter_1_5 in pairs(var_1_3):
		local var_1_4 = arg_1_0.WrapPhaseGoods(iter_1_5, var_1_0, var_1_2)

		arg_1_0.goods[iter_1_4] = var_1_4

		table.insert(arg_1_0.phases, iter_1_4)

def var_0_0.GetPtId(arg_2_0):
	local var_2_0 = getProxy(ActivityProxy).getActivityById(arg_2_0.activityId).getConfig("config_data")

	return pg.newserver_shop_template[var_2_0[1]].resource_type

def var_0_0.WrapPhaseGoods(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	local var_3_0 = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_1):
		if arg_3_3[iter_3_1]:
			local var_3_1 = arg_3_2[iter_3_1] or NewServerCommodity.New({
				id = iter_3_1
			})

			var_3_0[var_3_1.id] = var_3_1

	return var_3_0

def var_0_0.GetStartTime(arg_4_0):
	return arg_4_0.startTime

def var_0_0.GetEndTime(arg_5_0):
	return arg_5_0.stopTime

def var_0_0.GetCommodityById(arg_6_0, arg_6_1):
	for iter_6_0, iter_6_1 in pairs(arg_6_0.goods):
		for iter_6_2, iter_6_3 in pairs(iter_6_1):
			if iter_6_2 == arg_6_1:
				return iter_6_3

def var_0_0.GetOpeningGoodsList(arg_7_0, arg_7_1):
	local var_7_0 = {}
	local var_7_1 = arg_7_0.goods[arg_7_1]

	for iter_7_0, iter_7_1 in pairs(var_7_1):
		table.insert(var_7_0, iter_7_1)

	return var_7_0

def var_0_0.IsOpenPhase(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0.phases[arg_8_1]

	return arg_8_0.GetStartTime() + var_8_0 <= pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.GetPhases(arg_9_0):
	return arg_9_0.phases

return var_0_0
