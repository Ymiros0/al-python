local var_0_0 = class("CommnaderFleet", import(".BaseVO"))

var_0_0.RENAME_CODE_TIME = 60

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.Update(arg_1_1)

def var_0_0.Update(arg_2_0, arg_2_1):
	arg_2_0.id = arg_2_1.id
	arg_2_0.name = arg_2_1.name or i18n("commander_prefab_name", arg_2_0.id)
	arg_2_0.commanders = arg_2_1.commanders or {}
	arg_2_0.renameTime = 0

def var_0_0.canRename(arg_3_0):
	local var_3_0 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_3_1 = var_0_0.RENAME_CODE_TIME - (var_3_0 - arg_3_0.renameTime)

	if var_3_1 <= 0:
		return True

	return False, i18n("commander_prefab_rename_time", var_3_1)

def var_0_0.updateCommander(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.commanders[arg_4_1] = arg_4_2

def var_0_0.getName(arg_5_0):
	return arg_5_0.name

def var_0_0.updateName(arg_6_0, arg_6_1):
	arg_6_0.name = arg_6_1
	arg_6_0.renameTime = pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.getCommanderByPos(arg_7_0, arg_7_1):
	return arg_7_0.commanders[arg_7_1]

def var_0_0.getCommander(arg_8_0):
	return arg_8_0.commanders

def var_0_0.updateCommanders(arg_9_0, arg_9_1):
	arg_9_0.commanders = arg_9_1

def var_0_0.contains(arg_10_0, arg_10_1):
	for iter_10_0, iter_10_1 in pairs(arg_10_0.commanders):
		if iter_10_1.id == arg_10_1:
			return True

	return False

def var_0_0.getCommanderIds(arg_11_0):
	local var_11_0 = {}

	for iter_11_0, iter_11_1 in pairs(arg_11_0.commanders):
		table.insert(var_11_0, iter_11_1.id)

	return var_11_0

def var_0_0.removeCommander(arg_12_0, arg_12_1):
	for iter_12_0, iter_12_1 in pairs(arg_12_0.commanders):
		if iter_12_1.id == arg_12_1:
			arg_12_0.commanders[iter_12_0] = None

def var_0_0.isEmpty(arg_13_0):
	return table.getCount(arg_13_0.commanders) == 0

def var_0_0.isSame(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_0.commanders[1]
	local var_14_1 = arg_14_1[1]
	local var_14_2 = arg_14_0.commanders[2]
	local var_14_3 = arg_14_1[2]
	local var_14_4 = var_14_0 == None and var_14_1 == None or var_14_0 and var_14_1 and var_14_0.id == var_14_1.id
	local var_14_5 = var_14_2 == None and var_14_3 == None or var_14_2 and var_14_3 and var_14_2.id == var_14_3.id

	return var_14_4 and var_14_5

def var_0_0.isSameId(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_0.commanders[1]
	local var_15_1 = arg_15_1[1]
	local var_15_2 = arg_15_0.commanders[2]
	local var_15_3 = arg_15_1[2]
	local var_15_4 = var_15_0 == None and var_15_1 == None or var_15_0 and var_15_1 and var_15_0.id == var_15_1
	local var_15_5 = var_15_2 == None and var_15_3 == None or var_15_2 and var_15_3 and var_15_2.id == var_15_3

	return var_15_4 and var_15_5

return var_0_0
