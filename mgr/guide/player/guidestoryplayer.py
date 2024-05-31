local var_0_0 = class("GuideStoryPlayer", import(".GuidePlayer"))

def var_0_0.OnExecution(arg_1_0, arg_1_1, arg_1_2):
	local var_1_0 = arg_1_1.GetStories()
	local var_1_1 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0):
		table.insert(var_1_1, function(arg_2_0)
			pg.NewStoryMgr.GetInstance().Play(iter_1_1, arg_2_0, True))

	table.insert(var_1_1, function(arg_3_0)
		pg.m02.sendNotification(GAME.START_GUIDE)
		arg_3_0())
	seriesAsync(var_1_1, arg_1_2)

return var_0_0
