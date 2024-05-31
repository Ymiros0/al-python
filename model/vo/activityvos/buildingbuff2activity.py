local var_0_0 = class("BuildingBuff2Activity", import("model.vo.Activity"))

def var_0_0.GetBuildingConfigTable(arg_1_0, arg_1_1):
	return pg.activity_event_building[arg_1_1]

def var_0_0.GetBuildingLevel(arg_2_0, arg_2_1):
	return arg_2_0.data1KeyValueList[2][arg_2_1] or 1

def var_0_0.SetBuildingLevel(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.data1KeyValueList[2][arg_3_1] = arg_3_2

def var_0_0.GetBuildingIds(arg_4_0):
	return arg_4_0.getConfig("config_data")[1]

def var_0_0.GetTotalBuildingLevel(arg_5_0):
	local var_5_0 = arg_5_0.GetBuildingIds()
	local var_5_1 = 0

	for iter_5_0, iter_5_1 in ipairs(var_5_0):
		var_5_1 = var_5_1 + arg_5_0.GetBuildingLevel(iter_5_1)

	return math.floor(var_5_1 / #var_5_0)

def var_0_0.GetBuildingLevelSum(arg_6_0):
	local var_6_0 = arg_6_0.GetBuildingIds()
	local var_6_1 = 0

	for iter_6_0, iter_6_1 in ipairs(var_6_0):
		var_6_1 = var_6_1 + (arg_6_0.GetBuildingLevel(iter_6_1) - 1)

	return var_6_1

def var_0_0.GetSceneBuildingId(arg_7_0):
	return arg_7_0.getConfig("config_id")

def var_0_0.GetLastRequestTime(arg_8_0):
	return arg_8_0.data1

def var_0_0.RecordLastRequestTime(arg_9_0):
	arg_9_0.data1 = pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.CanRequest(arg_10_0):
	return pg.TimeMgr.GetInstance().GetNextTime(0, 0, 0) - 86400 > arg_10_0.GetLastRequestTime()

return var_0_0
