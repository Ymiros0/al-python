local var_0_0 = class("TimeSynchronizationCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.TimeMgr.GetInstance().SetServerTime(var_1_0.timestamp, var_1_0.monday_0oclock_timestamp)
	getProxy(BuildShipProxy).setBuildShipState()

	local var_1_1 = getProxy(PlayerProxy)

	if var_1_1.getData():
		var_1_1.flushTimesListener()

	local var_1_2 = getProxy(MilitaryExerciseProxy)

	if var_1_2.getSeasonInfo():
		var_1_2.addRefreshCountTimer()
		var_1_2.addSeasonOverTimer()

return var_0_0
