local var_0_0 = class("FeastProxy", import("model.proxy.NetProxy"))

def var_0_0.register(arg_1_0):
	return

local function var_0_1(arg_2_0, arg_2_1, arg_2_2)
	if arg_2_0.getRawData() != None:
		arg_2_2()

		return

	arg_2_0.sendNotification(GAME.GET_FEAST_DATA, {
		activityId = arg_2_1.id,
		callback = arg_2_2
	})

local function var_0_2(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = arg_3_1.getConfig("config_data")
	local var_3_1 = var_3_0[1] or 5

	if not arg_3_0.getRawData().ShouldRandomShips():
		arg_3_2()

		return

	local var_3_2 = var_3_0[3] or {}
	local var_3_3 = arg_3_0.RandomShips(var_3_2, var_3_1)
	local var_3_4 = _.map(var_3_3, function(arg_4_0)
		return arg_4_0.id)

	arg_3_0.sendNotification(GAME.FEAST_OP, {
		activityId = arg_3_1.id,
		cmd = FeastDorm.OP_RANDOM_SHIPS,
		argList = var_3_4,
		callback = arg_3_2
	})

def var_0_0.RequestData(arg_5_0, arg_5_1):
	local var_5_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_FEAST)

	if not var_5_0 or var_5_0.isEnd():
		arg_5_1()

		return

	seriesAsync({
		function(arg_6_0)
			var_0_1(arg_5_0, var_5_0, arg_6_0),
		function(arg_7_0)
			var_0_2(arg_5_0, var_5_0, arg_7_0)
	}, arg_5_1)

def var_0_0.SetData(arg_8_0, arg_8_1):
	assert(isa(arg_8_1, FeastDorm))

	arg_8_0.data = arg_8_1

	arg_8_0.AddRefreshTimer()

def var_0_0.UpdateData(arg_9_0, arg_9_1):
	assert(isa(arg_9_1, FeastDorm))

	arg_9_0.data = arg_9_1

def var_0_0.GetConsumeList(arg_10_0):
	local var_10_0 = (getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_FEAST).getConfig("config_data")[3] or {})[1]
	local var_10_1 = pg.activity_partyinvitation_template[var_10_0]
	local var_10_2 = var_10_1.invitationID[2]
	local var_10_3 = var_10_1.giftID[2]

	return var_10_2, var_10_3

local function var_0_3(arg_11_0)
	local var_11_0 = _.filter(pg.ship_data_group.all, function(arg_12_0)
		return pg.ship_data_group[arg_12_0].handbook_type != 1)
	local var_11_1 = {}
	local var_11_2 = {}

	for iter_11_0, iter_11_1 in ipairs(var_11_0):
		local var_11_3 = pg.ship_data_group[iter_11_1]
		local var_11_4 = arg_11_0[var_11_3.group_type]

		if var_11_4:
			table.insert(var_11_1, var_11_4)
		else
			table.insert(var_11_1, ShipGroup.New({
				id = var_11_3.group_type
			}))

	return var_11_1, var_11_2

local function var_0_4(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
	local var_13_0 = {}

	for iter_13_0, iter_13_1 in pairs(arg_13_0):
		if not table.contains(arg_13_1, iter_13_1.id):
			table.insert(var_13_0, iter_13_1)

	local var_13_1 = {}
	local var_13_2 = {}
	local var_13_3 = {}

	for iter_13_2, iter_13_3 in ipairs(var_13_0):
		local var_13_4 = ShipGroup.getSkinList(iter_13_3.id)

		for iter_13_4, iter_13_5 in ipairs(var_13_4):
			local var_13_5 = ShipSkin.GetShopTypeIdBySkinId(iter_13_5.id, var_13_3) == 7 and var_13_1 or var_13_2

			table.insert(var_13_5, iter_13_3)

	shuffle(var_13_1)
	shuffle(var_13_2)

	for iter_13_6, iter_13_7 in ipairs(var_13_1):
		if table.getCount(arg_13_2) == arg_13_3:
			break

		arg_13_2[iter_13_7.id] = iter_13_7

	for iter_13_8, iter_13_9 in ipairs(var_13_2):
		if table.getCount(arg_13_2) == arg_13_3:
			break

		arg_13_2[iter_13_9.id] = iter_13_9

def var_0_0.RandomShips(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = pg.activity_partyinvitation_template or {}
	local var_14_1 = {}

	for iter_14_0, iter_14_1 in ipairs(arg_14_1):
		table.insert(var_14_1, var_14_0[iter_14_1].groupid)

	local var_14_2 = arg_14_0.getRawData().GetFeastShipList()

	for iter_14_2, iter_14_3 in pairs(var_14_2):
		if not table.contains(var_14_1, iter_14_2):
			table.insert(var_14_1, iter_14_2)

	local var_14_3 = getProxy(CollectionProxy).RawgetGroups()
	local var_14_4, var_14_5 = var_0_3(var_14_3)
	local var_14_6 = {}

	var_0_4(var_14_4, var_14_1, var_14_6, arg_14_2)
	var_0_4(var_14_5, var_14_1, var_14_6, arg_14_2)

	local var_14_7 = {}

	for iter_14_4, iter_14_5 in pairs(var_14_6):
		table.insert(var_14_7, iter_14_5)

	return var_14_7

def var_0_0.AddRefreshTimer(arg_15_0):
	arg_15_0.RemoveRefreshTimer()

	local var_15_0 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_15_1 = GetZeroTime() - var_15_0

	arg_15_0.timer = Timer.New(function()
		arg_15_0.RemoveRefreshTimer()

		local var_16_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_FEAST)

		if var_16_0 and not var_16_0.isEnd():
			var_0_2(arg_15_0, var_16_0, function()
				return), var_15_1 + 1, 1)

	arg_15_0.timer.Start()

def var_0_0.RemoveRefreshTimer(arg_18_0):
	if arg_18_0.timer:
		arg_18_0.timer.Stop()

		arg_18_0.timer = None

def var_0_0.remove(arg_19_0):
	arg_19_0.RemoveRefreshTimer()

def var_0_0.GetBuffList(arg_20_0):
	local var_20_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.FEAST_PT_ACT)

	if not var_20_0 or var_20_0.isEnd():
		return {}

	return var_20_0.GetBuffList()

def var_0_0.GetTaskList(arg_21_0):
	local var_21_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.FEAST_TASK_ACT)

	assert(var_21_0)

	local var_21_1 = {}
	local var_21_2 = getProxy(TaskProxy)

	for iter_21_0, iter_21_1 in ipairs(var_21_0.getConfig("config_data")):
		if var_21_2.getTaskById(iter_21_1) or var_21_2.getFinishTaskById(iter_21_1):
			table.insert(var_21_1, iter_21_1)

	return var_21_1

def var_0_0.GetPtActData(arg_22_0):
	local var_22_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.FEAST_PT_ACT)

	assert(var_22_0)

	return (ActivityPtData.New(var_22_0))

def var_0_0.GetSubmittedTaskStories(arg_23_0):
	local var_23_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_FEAST)

	if not var_23_0 or var_23_0.isEnd():
		return {}

	local var_23_1 = var_23_0.getConfig("config_client")
	local var_23_2 = {
		var_23_1[8],
		var_23_1[9]
	}
	local var_23_3 = {}

	for iter_23_0, iter_23_1 in ipairs(var_23_2):
		local var_23_4 = iter_23_1[1]
		local var_23_5 = iter_23_1[2]

		if not pg.NewStoryMgr.GetInstance().IsPlayed(var_23_5):
			var_23_3[var_23_4] = var_23_5

	return var_23_3

def var_0_0.ShouldTipPt(arg_24_0):
	if arg_24_0.GetPtActData().AnyAwardCanGet():
		return True

	return False

def var_0_0.ShouldTipFeastTask(arg_25_0):
	local var_25_0 = getProxy(TaskProxy)
	local var_25_1 = arg_25_0.GetTaskList()

	for iter_25_0, iter_25_1 in ipairs(var_25_1):
		local var_25_2 = var_25_0.getTaskById(iter_25_1)

		if var_25_2 and var_25_2.isFinish() and not var_25_2.isReceive():
			return True

	return False

def var_0_0.ShouldTipTask(arg_26_0):
	if arg_26_0.ShouldTipPt():
		return True

	if arg_26_0.ShouldTipFeastTask():
		return True

	return False

def var_0_0.ShouldTipInvitation(arg_27_0):
	local var_27_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)
	local var_27_1, var_27_2 = arg_27_0.GetConsumeList()
	local var_27_3 = var_27_0.getVitemNumber(var_27_1)
	local var_27_4 = var_27_0.getVitemNumber(var_27_2)
	local var_27_5 = arg_27_0.data.GetInvitedFeastShipList()

	for iter_27_0, iter_27_1 in ipairs(var_27_5):
		if not iter_27_1.GotGift() and var_27_4 > 0 or not iter_27_1.GotTicket() and var_27_3 > 0:
			return True

	return False

def var_0_0.ShouldTip(arg_28_0):
	if not arg_28_0.data:
		return False

	local var_28_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.FEAST_TASK_ACT)

	if not var_28_0 or var_28_0.isEnd():
		return False

	local var_28_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.FEAST_PT_ACT)

	if not var_28_1 or var_28_1.isEnd():
		return False

	local var_28_2 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

	if not var_28_2 or var_28_2.isEnd():
		return False

	if arg_28_0.data == None:
		return False

	local var_28_3 = arg_28_0.data.GetFeastShipList()

	for iter_28_0, iter_28_1 in pairs(var_28_3):
		if iter_28_1.HasBubble():
			return True

	if arg_28_0.ShouldTipTask():
		return True

	if arg_28_0.ShouldTipInvitation():
		return True

	return False

def var_0_0.HandleTaskStories(arg_29_0, arg_29_1, arg_29_2):
	local var_29_0 = arg_29_0.GetSubmittedTaskStories()

	if not var_29_0 or table.getCount(var_29_0) == 0:
		if arg_29_2:
			arg_29_2()

		return

	local var_29_1 = {}

	for iter_29_0, iter_29_1 in ipairs(arg_29_1):
		if var_29_0[iter_29_1] != None:
			table.insert(var_29_1, var_29_0[iter_29_1])

	if #var_29_1 > 0:
		if arg_29_2:
			pg.NewStoryMgr.GetInstance().SeriesPlay(var_29_1, arg_29_2)
		else
			pg.NewStoryMgr.GetInstance().SeriesPlay(var_29_1)

return var_0_0
