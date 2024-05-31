local var_0_0 = class("VoteStoryUtil")

var_0_0.ENTER_SCENE = 1
var_0_0.ENTER_MAIN_STAGE = 2
var_0_0.ENTER_SUB_STAGE = 3
var_0_0.ENTER_SCHEDULE = 4
var_0_0.ENTER_HALL = 5
var_0_0.ENTER_EXCHANGE = 6
var_0_0.END = 7

def var_0_0.GetStoryNameByType(arg_1_0):
	local var_1_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.VOTE_ENTRANCE_ACT_ID)

	if not var_1_0 or var_1_0.isEnd():
		return None

	return var_1_0.getConfig("config_client")[arg_1_0 + 2]

def var_0_0.FinalRaceIsEnd():
	local var_2_0 = pg.activity_vote.all

	for iter_2_0 = #var_2_0, 1, -1:
		local var_2_1 = var_2_0[iter_2_0]
		local var_2_2 = pg.activity_vote[var_2_1]

		if var_2_2.type == VoteConst.RACE_TYPE_FINAL:
			return pg.TimeMgr.GetInstance().GetServerTime() >= pg.TimeMgr.GetInstance().parseTimeFromConfig(var_2_2.time_vote[2])

	return True

def var_0_0.AllPreheatStoriesPlayed():
	if var_0_0.FinalRaceIsEnd():
		return True

	local var_3_0 = {
		var_0_0.ENTER_SCENE,
		var_0_0.ENTER_MAIN_STAGE,
		var_0_0.ENTER_SUB_STAGE,
		var_0_0.ENTER_SCHEDULE,
		var_0_0.ENTER_HALL,
		var_0_0.ENTER_EXCHANGE
	}
	local var_3_1 = _.map(var_3_0, function(arg_4_0)
		return var_0_0.GetStoryNameByType(arg_4_0))

	return _.all(var_3_1, function(arg_5_0)
		return pg.NewStoryMgr.GetInstance().IsPlayed(arg_5_0))

def var_0_0.Notify(arg_6_0):
	local var_6_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VOTE)

	if not var_6_0 or var_6_0.isEnd():
		var_0_0.HandleEndStory()

		return

	local var_6_1 = var_6_0.getConfig("config_id")
	local var_6_2 = pg.activity_vote[var_6_1].type == VoteConst.RACE_TYPE_PRE
	local var_6_3 = {}
	local var_6_4 = {}

	if arg_6_0 == var_0_0.ENTER_SCENE:
		var_0_0.CollectEnterStory(var_6_2, var_6_3)
		var_0_0.CollectEnterGuide(var_6_2, var_6_4)
	elif var_6_2 and arg_6_0 == var_0_0.ENTER_MAIN_STAGE:
		var_0_0.CollectEnterMainStory(var_6_3)
	elif var_6_2 and arg_6_0 == var_0_0.ENTER_SUB_STAGE:
		var_0_0.CollectEnterSubStory(var_6_3)
	elif var_6_2 and arg_6_0 == var_0_0.ENTER_SCHEDULE:
		var_0_0.CollectEnterScheduleStory(var_6_3)
	elif var_6_2 and arg_6_0 == var_0_0.ENTER_HALL:
		var_0_0.CollectEnterHallStory(var_6_3)
	elif var_6_2 and arg_6_0 == var_0_0.ENTER_EXCHANGE:
		var_0_0.CollectEnterExchangeStory(var_6_3)

	seriesAsync({
		function(arg_7_0)
			var_0_0.Play(var_6_3, arg_7_0),
		function(arg_8_0)
			var_0_0.HandleCurrActStory(var_6_0, arg_8_0),
		function(arg_9_0)
			var_0_0.HandleGuide(var_6_4, arg_9_0)
	})

def var_0_0.HandleGuide(arg_10_0, arg_10_1):
	local var_10_0 = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_0):
		table.insert(var_10_0, function(arg_11_0)
			pg.NewGuideMgr.GetInstance().Play(iter_10_1, None, arg_11_0))

	seriesAsync(var_10_0, arg_10_1)

def var_0_0.HandleCurrActStory(arg_12_0, arg_12_1):
	if var_0_0.AllPreheatStoriesPlayed():
		local var_12_0 = arg_12_0.getConfig("config_client")[1]

		var_0_0.Play({
			var_12_0
		}, arg_12_1)
	else
		arg_12_1()

def var_0_0.PreRaceIsEnd():
	local var_13_0

	for iter_13_0, iter_13_1 in ipairs(pg.activity_vote.all):
		if pg.activity_vote[iter_13_1].type == VoteConst.RACE_TYPE_PRE:
			var_13_0 = iter_13_1

			break

	if not var_13_0:
		return False

	local var_13_1 = pg.activity_vote[var_13_0]

	return pg.TimeMgr.GetInstance().GetServerTime() >= pg.TimeMgr.GetInstance().parseTimeFromConfig(var_13_1.time_vote[2])

def var_0_0.HandleEndStory():
	if getProxy(VoteProxy).IsAllRaceEnd():
		local var_14_0 = var_0_0.GetStoryNameByType(var_0_0.END)

		var_0_0.Play({
			var_14_0
		})
	elif var_0_0.PreRaceIsEnd():
		local var_14_1 = {
			var_0_0.ENTER_SCENE,
			var_0_0.ENTER_MAIN_STAGE,
			var_0_0.ENTER_SUB_STAGE,
			var_0_0.ENTER_SCHEDULE,
			var_0_0.ENTER_HALL,
			var_0_0.ENTER_EXCHANGE
		}
		local var_14_2 = _.map(var_14_1, function(arg_15_0)
			return var_0_0.GetStoryNameByType(arg_15_0))

		var_0_0.Play(var_14_2)

def var_0_0.CollectEnterGuide(arg_16_0, arg_16_1):
	if arg_16_0:
		local var_16_0 = var_0_0.GetStoryNameByType(var_0_0.ENTER_SCENE)

		if not pg.NewStoryMgr.GetInstance().IsPlayed(var_16_0):
			table.insert(arg_16_1, "NG0042")

def var_0_0.CollectEnterStory(arg_17_0, arg_17_1):
	if arg_17_0:
		local var_17_0 = var_0_0.GetStoryNameByType(var_0_0.ENTER_SCENE)

		table.insert(arg_17_1, var_17_0)
	else
		local var_17_1 = {
			var_0_0.ENTER_SCENE,
			var_0_0.ENTER_MAIN_STAGE,
			var_0_0.ENTER_SUB_STAGE,
			var_0_0.ENTER_SCHEDULE,
			var_0_0.ENTER_HALL,
			var_0_0.ENTER_EXCHANGE
		}
		local var_17_2 = _.map(var_17_1, function(arg_18_0)
			return var_0_0.GetStoryNameByType(arg_18_0))

		for iter_17_0, iter_17_1 in ipairs(var_17_2):
			table.insert(arg_17_1, iter_17_1)

		local var_17_3 = var_0_0.GetPrevRaceStories()

		for iter_17_2, iter_17_3 in ipairs(var_17_3):
			table.insert(arg_17_1, iter_17_3)

def var_0_0.GetPrevRaceStories():
	local var_19_0 = {}
	local var_19_1 = pg.TimeMgr.GetInstance().GetServerTime()

	for iter_19_0, iter_19_1 in ipairs(pg.activity_template.all):
		local var_19_2 = pg.activity_template[iter_19_1]

		if var_19_2.type == ActivityConst.ACTIVITY_TYPE_VOTE and var_19_1 > pg.TimeMgr.GetInstance().parseTimeFromConfig(var_19_2.time[3]):
			table.insert(var_19_0, var_19_2.config_client[1])

	return var_19_0

def var_0_0.CollectEnterMainStory(arg_20_0):
	local var_20_0 = var_0_0.GetStoryNameByType(var_0_0.ENTER_MAIN_STAGE)

	table.insert(arg_20_0, var_20_0)

def var_0_0.CollectEnterSubStory(arg_21_0):
	local var_21_0 = var_0_0.GetStoryNameByType(var_0_0.ENTER_SUB_STAGE)

	table.insert(arg_21_0, var_21_0)

def var_0_0.CollectEnterScheduleStory(arg_22_0):
	local var_22_0 = var_0_0.GetStoryNameByType(var_0_0.ENTER_SCHEDULE)

	table.insert(arg_22_0, var_22_0)

def var_0_0.CollectEnterHallStory(arg_23_0):
	local var_23_0 = var_0_0.GetStoryNameByType(var_0_0.ENTER_HALL)

	table.insert(arg_23_0, var_23_0)

def var_0_0.CollectEnterExchangeStory(arg_24_0):
	local var_24_0 = var_0_0.GetStoryNameByType(var_0_0.ENTER_EXCHANGE)

	table.insert(arg_24_0, var_24_0)

def var_0_0.Play(arg_25_0, arg_25_1):
	local var_25_0 = _.select(arg_25_0, function(arg_26_0)
		return not pg.NewStoryMgr.GetInstance().IsPlayed(arg_26_0))
	local var_25_1 = {}

	for iter_25_0, iter_25_1 in ipairs(var_25_0):
		table.insert(var_25_1, function(arg_27_0)
			pg.NewStoryMgr.GetInstance().Play(iter_25_1, arg_27_0))

	seriesAsync(var_25_1, arg_25_1)

return var_0_0
