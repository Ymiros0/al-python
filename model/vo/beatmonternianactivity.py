local var_0_0 = class("BeatMonterNianActivity", import(".Activity"))

def var_0_0.GetDataConfig(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0.getConfig("config_id")
	local var_1_1 = pg.activity_event_nianshou[tonumber(var_1_0)]

	return var_1_1 and var_1_1[arg_1_1]

def var_0_0.GetCountForHitMonster(arg_2_0):
	local var_2_0 = arg_2_0.getStartTime()
	local var_2_1 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_2_2 = pg.TimeMgr.GetInstance().parseTimeFrom(var_2_1 - var_2_0)
	local var_2_3 = arg_2_0.GetDataConfig("daily_count")
	local var_2_4 = arg_2_0.GetDataConfig("first_extra_count")

	return (var_2_2 + 1) * var_2_3 + var_2_4 - arg_2_0.data2

return var_0_0
