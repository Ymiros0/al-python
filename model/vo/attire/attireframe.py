local var_0_0 = class("AttireFrame", import("..BaseVO"))

var_0_0.STATE_LOCK = 1
var_0_0.STATE_UNLOCKABLE = 2
var_0_0.STATE_UNLOCK = 3

def var_0_0.attireFrameRes(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	local var_1_0 = arg_1_0.attireInfo[arg_1_2]

	if arg_1_1:
		local var_1_1 = getProxy(PlayerProxy).getRawData()

		arg_1_3 = arg_1_3 and (not HXSet.isHxPropose() or var_1_1.GetProposeShipId() == var_1_1.character)
	else
		arg_1_3 = arg_1_3 and not HXSet.isHxPropose()

	if arg_1_2 == AttireConst.TYPE_ICON_FRAME and var_1_0 == 0 and arg_1_3:
		local var_1_2 = pg.ship_data_template[arg_1_0.icon]

		if var_1_2 and ShipGroup.IsMetaGroup(var_1_2.group_type):
			return "meta_propose"
		else
			return "propose"
	elif arg_1_2 == AttireConst.TYPE_CHAT_FRAME:
		return arg_1_1 and var_1_0 .. "_self" or var_1_0 .. "_other"
	else
		return var_1_0

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.id = arg_2_1.id
	arg_2_0.configId = arg_2_0.id

	arg_2_0.updateData(arg_2_1)

def var_0_0.isNew(arg_3_0):
	return arg_3_0.new == True

def var_0_0.clearNew(arg_4_0):
	arg_4_0.new = None

def var_0_0.updateData(arg_5_0, arg_5_1):
	arg_5_0.endTime = arg_5_1.end_time or arg_5_1.time or -1
	arg_5_0.new = arg_5_1.isNew

def var_0_0.getState(arg_6_0):
	local var_6_0 = var_0_0.STATE_LOCK
	local var_6_1 = arg_6_0.isOwned()

	if var_6_1:
		var_6_0 = var_0_0.STATE_UNLOCK
	elif not var_6_1 and arg_6_0.canUnlock():
		var_6_0 = var_0_0.STATE_UNLOCKABLE

	return var_6_0

def var_0_0.canUnlock(arg_7_0):
	return False

def var_0_0.isOwned(arg_8_0):
	return arg_8_0.endTime >= 0 and not arg_8_0.isExpired()

def var_0_0.isExpired(arg_9_0):
	local var_9_0 = pg.TimeMgr.GetInstance().GetServerTime()

	return arg_9_0.expiredType() and var_9_0 >= arg_9_0.getExpiredTime()

def var_0_0.getExpiredTime(arg_10_0):
	if arg_10_0.expiredType():
		return arg_10_0.endTime

	assert(False)

def var_0_0.updateEndTime(arg_11_0, arg_11_1):
	arg_11_0.endTime = arg_11_1

def var_0_0.expiredType(arg_12_0):
	return arg_12_0.getConfig("time_limit_type") == 1

def var_0_0.getTimerKey(arg_13_0):
	return arg_13_0.getType() .. "_" .. arg_13_0.id

def var_0_0.getType(arg_14_0):
	assert(False)

def var_0_0.bindConfigTable(arg_15_0):
	assert(False)

def var_0_0.getDropType(arg_16_0):
	assert(False)

return var_0_0
