local var_0_0 = class("ExerciseCountRecoverUpCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local function var_1_0()
		local var_2_0 = pg.TimeMgr.GetInstance().STimeDescS(pg.TimeMgr.GetInstance().GetServerTime(), "*t")
		local var_2_1 = 3600 * SeasonInfo.RECOVER_UP_SIX_HOUR

		if var_2_0.hour == 0:
			var_2_1 = 3600 * SeasonInfo.RECOVER_UP_TWELVE_HOUR

		return var_2_1

	local var_1_1 = getProxy(MilitaryExerciseProxy)
	local var_1_2 = var_1_1.getSeasonInfo()

	var_1_2.updateResetTime(var_1_0() + pg.TimeMgr.GetInstance().GetServerTime())
	var_1_2.updateExerciseCount(SeasonInfo.RECOVER_UP_COUNT)
	var_1_1.updateSeasonInfo(var_1_2)
	var_1_1.addRefreshCountTimer()

return var_0_0
