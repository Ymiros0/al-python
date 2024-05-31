local var_0_0 = class("VoteProxy", import(".NetProxy"))

var_0_0.VOTE_ORDER_BOOK_UPDATE = "VoteProxy.VOTE_ORDER_BOOK_UPDATE"
var_0_0.VOTE_ORDER_BOOK_DELETE = "VoteProxy.VOTE_ORDER_BOOK_DELETE"
var_0_0.VOTES_COUNT_UPDATE = "VoteProxy.VOTES_COUNT_UPDATE"

def var_0_0.register(arg_1_0):
	arg_1_0.voteGroupList = {}
	arg_1_0.tempVoteGroup = {}

def var_0_0.AddTempVoteGroup(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_1.list
	local var_2_1 = _.map(var_2_0, function(arg_3_0)
		return arg_2_0.Data2VoteShip(arg_3_0, arg_2_2))

	arg_2_0.tempVoteGroup[arg_2_2] = VoteGroup.New({
		id = arg_2_2,
		list = var_2_1
	})

def var_0_0.RawGetTempVoteGroup(arg_4_0, arg_4_1):
	return arg_4_0.tempVoteGroup[arg_4_1]

def var_0_0.RawGetVoteGroupByConfigId(arg_5_0, arg_5_1):
	return arg_5_0.voteGroupList[arg_5_1]

def var_0_0.GetVoteActivityByConfigId(arg_6_0, arg_6_1):
	local var_6_0 = getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_VOTE)

	for iter_6_0, iter_6_1 in ipairs(var_6_0):
		if iter_6_1.getDataConfig("is_in_game") == 1 and iter_6_1.getConfig("config_id") == arg_6_1 and not iter_6_1.isEnd():
			return iter_6_1

	return None

def var_0_0.GetVotesByConfigId(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.GetVoteActivityByConfigId(arg_7_1)

	if var_7_0 and not var_7_0.isEnd():
		return var_7_0.data1

	return 0

def var_0_0.AddVoteGroup(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = arg_8_1.list
	local var_8_1 = _.map(var_8_0, function(arg_9_0)
		return arg_8_0.Data2VoteShip(arg_9_0, arg_8_2))

	arg_8_0.voteGroupList[arg_8_2] = VoteGroup.New({
		id = arg_8_2,
		list = var_8_1
	})

def var_0_0.Data2VoteShip(arg_10_0, arg_10_1, arg_10_2):
	if pg.activity_vote_virtual_ship_data[arg_10_1.key]:
		return VirtualVoteShip.New(arg_10_1, arg_10_2)
	elif ShipGroup.GetGroupConfig(arg_10_1.key) != None:
		return VoteShip.New(arg_10_1, arg_10_2)
	else
		assert(False, arg_10_1.key)

def var_0_0.AnyVoteActIsOpening(arg_11_0):
	local var_11_0 = getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_VOTE)

	for iter_11_0, iter_11_1 in ipairs(var_11_0):
		if iter_11_1.getDataConfig("is_in_game") == 1 and not iter_11_1.isEnd():
			return True

	return False

def var_0_0.GetVoteGroupList(arg_12_0):
	local var_12_0 = {}

	for iter_12_0, iter_12_1 in pairs(arg_12_0.voteGroupList):
		table.insert(var_12_0, iter_12_1)

	return var_12_0

def var_0_0.GetOpeningFunVoteGroup(arg_13_0):
	for iter_13_0, iter_13_1 in pairs(arg_13_0.voteGroupList):
		if iter_13_1.IsFunRace() and iter_13_1.IsOpening():
			return iter_13_1

	return None

def var_0_0.GetOpeningNonFunVoteGroup(arg_14_0):
	for iter_14_0, iter_14_1 in pairs(arg_14_0.voteGroupList):
		if not iter_14_1.IsFunRace() and iter_14_1.IsOpening():
			return iter_14_1

	return None

def var_0_0.IsAllRaceEnd(arg_15_0):
	local var_15_0 = pg.TimeMgr.GetInstance().GetServerTime()

	return _.all(pg.activity_vote.all, function(arg_16_0)
		local var_16_0 = pg.activity_vote[arg_16_0]
		local var_16_1 = var_16_0.time_vote

		return var_16_0.is_in_game == 1 and var_15_0 >= pg.TimeMgr.GetInstance().parseTimeFromConfig(var_16_1[2]))

def var_0_0.GetPastVoteData(arg_17_0):
	if not arg_17_0.pastVoteData:
		arg_17_0.pastVoteData = pg.vote_champion.get_id_list_by_group

	return arg_17_0.pastVoteData

def var_0_0.ExistPastVoteAward(arg_18_0):
	local var_18_0 = arg_18_0.GetPastVoteData()
	local var_18_1 = getProxy(AttireProxy)

	for iter_18_0, iter_18_1 in pairs(var_18_0):
		if _.any(iter_18_1, function(arg_19_0)
			local var_19_0 = pg.vote_champion[arg_19_0]
			local var_19_1 = getProxy(TaskProxy).getTaskById(var_19_0.task)
			local var_19_2 = pg.task_data_template[var_19_0.task].award_display[1]
			local var_19_3 = var_18_1.getAttireFrame(AttireConst.TYPE_ICON_FRAME, var_19_2[2])

			return var_19_1 and var_19_1.isFinish() and not var_19_1.isReceive() and (var_19_3 == None or not var_19_3.isOwned())):
			return True

	return False

def var_0_0.IsNewRace(arg_20_0, arg_20_1):
	if not arg_20_1:
		return False

	local var_20_0 = getProxy(PlayerProxy).getRawData().id

	return PlayerPrefs.GetInt(arg_20_1.configId .. "_vote__tip_" .. var_20_0, 0) == 0

def var_0_0.MarkRaceNonNew(arg_21_0, arg_21_1):
	if not arg_21_1 or not arg_21_0.IsNewRace(arg_21_1):
		return

	local var_21_0 = getProxy(PlayerProxy).getRawData().id
	local var_21_1 = PlayerPrefs.SetInt(arg_21_1.configId .. "_vote__tip_" .. var_21_0, 1)

	PlayerPrefs.Save()

return var_0_0
