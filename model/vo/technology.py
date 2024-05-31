local var_0_0 = class("Technology", import(".BaseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.technology_data_template

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.id = arg_2_1.id
	arg_2_0.configId = arg_2_0.id
	arg_2_0.poolId = arg_2_1.pool_id
	arg_2_0.time = arg_2_1.time
	arg_2_0.isQueue = arg_2_1.queue

def var_0_0.start(arg_3_0, arg_3_1):
	arg_3_0.time = arg_3_1

def var_0_0.isActivate(arg_4_0):
	return arg_4_0.time > 0

def var_0_0.isCompleted(arg_5_0):
	return arg_5_0.isFinish() and arg_5_0.finishCondition()

def var_0_0.isStarting(arg_6_0):
	if not arg_6_0.isActivate():
		return False

	return pg.TimeMgr.GetInstance().GetServerTime() < arg_6_0.time

def var_0_0.isWaiting(arg_7_0):
	if not arg_7_0.isActivate():
		return False

	return pg.TimeMgr.GetInstance().GetServerTime() < arg_7_0.time - arg_7_0.getConfig("time")

def var_0_0.isDoing(arg_8_0):
	if not arg_8_0.isActivate():
		return False

	local var_8_0 = pg.TimeMgr.GetInstance().GetServerTime()

	return var_8_0 >= arg_8_0.time - arg_8_0.getConfig("time") and var_8_0 < arg_8_0.time

def var_0_0.isFinish(arg_9_0):
	if not arg_9_0.isActivate():
		return False

	return pg.TimeMgr.GetInstance().GetServerTime() >= arg_9_0.time

def var_0_0.finishCondition(arg_10_0):
	if arg_10_0.isQueue:
		return True

	local var_10_0 = arg_10_0.getConfig("condition")

	return var_10_0 == 0 or getProxy(TaskProxy).getTaskVO(var_10_0).isFinish()

def var_0_0.hasResToStart(arg_11_0):
	local var_11_0 = arg_11_0.getConfig("consume")
	local var_11_1 = getProxy(PlayerProxy).getData()
	local var_11_2 = getProxy(BagProxy)

	for iter_11_0, iter_11_1 in ipairs(var_11_0):
		if iter_11_1[1] == DROP_TYPE_RESOURCE and var_11_1.getResById(iter_11_1[2]) < iter_11_1[3]:
			return False, i18n("common_no_resource")
		elif iter_11_1[1] == DROP_TYPE_ITEM and var_11_2.getItemCountById(iter_11_1[2]) < iter_11_1[3]:
			return False, i18n("common_no_item_1")

	return True

def var_0_0.reset(arg_12_0):
	arg_12_0.time = 0

return var_0_0
