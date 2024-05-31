local var_0_0 = class("CommonBuff", import(".BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.timestamp = arg_1_1.timestamp

def var_0_0.IsActiveType(arg_2_0):
	return False

def var_0_0.bindConfigTable(arg_3_0):
	return pg.benefit_buff_template

def var_0_0.checkShow(arg_4_0):
	return arg_4_0.getConfig("hide") != 1

def var_0_0.BackYardExpUsage(arg_5_0):
	return arg_5_0.getConfig("benefit_type") == BuffUsageConst.DORM_EXP

def var_0_0.BattleUsage(arg_6_0):
	return arg_6_0.getConfig("benefit_type") == BuffUsageConst.BATTLE

def var_0_0.RookieBattleExpUsage(arg_7_0):
	return arg_7_0.getConfig("benefit_type") == BuffUsageConst.ROOKIEBATTLEEXP

def var_0_0.ShipModExpUsage(arg_8_0):
	return arg_8_0.getConfig("benefit_type") == BuffUsageConst.SHIP_MOD_EXP

def var_0_0.BackyardEnergyUsage(arg_9_0):
	return arg_9_0.getConfig("benefit_type") == BuffUsageConst.DORM_ENERGY

def var_0_0.GetRookieBattleExpMaxLevel(arg_10_0):
	return arg_10_0.getConfig("benefit_condition")[3]

def var_0_0.isActivate(arg_11_0):
	return pg.TimeMgr.GetInstance().GetServerTime() <= arg_11_0.timestamp

def var_0_0.getLeftTime(arg_12_0):
	local var_12_0 = pg.TimeMgr.GetInstance().GetServerTime()

	return arg_12_0.timestamp - var_12_0

return var_0_0
