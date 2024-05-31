local var_0_0 = class("UpdateGuideIndexCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.index
	local var_1_2 = var_1_0.callback

	print("update index.....", var_1_1)
	pg.ConnectionMgr.GetInstance().Send(11016, {
		guide_index = var_1_1
	})

	local var_1_3 = getProxy(PlayerProxy).getData()

	var_1_3.guideIndex = var_1_1

	getProxy(PlayerProxy).updatePlayer(var_1_3)
	pg.SeriesGuideMgr.GetInstance().setPlayer(var_1_3)

	if pg.SeriesGuideMgr.GetInstance().isEnd():
		pg.TrackerMgr.GetInstance().Tracking(TRACKING_TUTORIAL_COMPLETE_1)

	if var_1_2:
		var_1_2()

return var_0_0
