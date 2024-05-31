local var_0_0 = class("LinerActivity", import("model.vo.Activity"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.curFinishEvents = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.date1_key_value_list or {}):
		if not arg_1_0.curFinishEvents[iter_1_1.key]:
			arg_1_0.curFinishEvents[iter_1_1.key] = {}

		table.insert(arg_1_0.curFinishEvents[iter_1_1.key], iter_1_1.value)

	arg_1_0.timeGroupIds = arg_1_0.getConfig("config_data")[1]
	arg_1_0.roomGroupIds = arg_1_0.getConfig("config_data")[2]
	arg_1_0.eventGroupIds = arg_1_0.getConfig("config_data")[3]
	arg_1_0.times = {}
	arg_1_0.timeMaxIdx = 1
	arg_1_0.timeIdx2Day = {}

	local var_1_0 = 1

	for iter_1_2, iter_1_3 in ipairs(arg_1_0.timeGroupIds):
		for iter_1_4, iter_1_5 in ipairs(pg.activity_liner_time_group[iter_1_3].ids):
			arg_1_0.timeMaxIdx = var_1_0
			arg_1_0.times[var_1_0] = LinerTime.New(iter_1_5)
			arg_1_0.timeIdx2Day[var_1_0] = iter_1_2
			var_1_0 = var_1_0 + 1

	if arg_1_0.data2 == 0:
		arg_1_0.data2 = 1

def var_0_0.GetTimeGroupIds(arg_2_0):
	return arg_2_0.timeGroupIds

def var_0_0.GetRoomGroupIds(arg_3_0):
	return arg_3_0.roomGroupIds

def var_0_0.GetEventGroupIds(arg_4_0):
	return arg_4_0.eventGroupIds

def var_0_0.UpdateRoomIdx(arg_5_0, arg_5_1):
	arg_5_0.data2 = arg_5_1 and 1 or arg_5_0.data2 + 1

def var_0_0.GetRoomIdx(arg_6_0):
	return arg_6_0.data2

def var_0_0.UpdateTimeIdx(arg_7_0):
	arg_7_0.data1 = arg_7_0.data1 + 1

	arg_7_0.ClearCurEventInfo()

def var_0_0.GetCurIdx(arg_8_0):
	return math.min(arg_8_0.data1, arg_8_0.timeMaxIdx)

def var_0_0.GetTimeMaxIdx(arg_9_0):
	return arg_9_0.timeMaxIdx

def var_0_0.IsFinishAllTime(arg_10_0):
	return arg_10_0.data1 > arg_10_0.timeMaxIdx

def var_0_0.GetFinishTimeIds(arg_11_0):
	local var_11_0 = {}
	local var_11_1 = arg_11_0.GetCurIdx()

	for iter_11_0 = 1, arg_11_0.data1 - 1:
		table.insert(var_11_0, arg_11_0.times[iter_11_0].id)

	return var_11_0

def var_0_0.GetDayByIdx(arg_12_0, arg_12_1):
	return arg_12_0.timeIdx2Day[arg_12_1]

def var_0_0.GetTimeByIdx(arg_13_0, arg_13_1):
	return arg_13_0.times[arg_13_1]

def var_0_0.GetCurTime(arg_14_0):
	return arg_14_0.times[arg_14_0.GetCurIdx()]

def var_0_0.CheckTimeFinish(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_1 or arg_15_0.GetCurTime()

	return switch(var_15_0.GetType(), {
		[LinerTime.TYPE.TARGET] = function()
			return pg.NewStoryMgr.GetInstance().IsPlayed(var_15_0.GetStory()),
		[LinerTime.TYPE.EXPLORE] = function()
			return arg_15_0.GetRemainExploreCnt() == 0,
		[LinerTime.TYPE.EVENT] = function()
			local var_18_0 = var_15_0.GetParamInfo()

			if arg_15_0.GetRoomIdx() != #var_18_0:
				return False
			else
				return arg_15_0.CheckRoomFinish(arg_15_1),
		[LinerTime.TYPE.STORY] = function()
			return pg.NewStoryMgr.GetInstance().IsPlayed(var_15_0.GetStory())
	}, function()
		return False)

def var_0_0.CheckRoomFinish(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_1 or arg_21_0.GetCurTime()

	if var_21_0.GetType() != LinerTime.TYPE.EVENT:
		return False

	local var_21_1 = var_21_0.GetParamInfo()[arg_21_0.GetRoomIdx()]

	if var_21_1[2] == LinerTime.EVENT_SUB_TYPE.CLUE:
		local var_21_2 = arg_21_0.GetCurEventInfo()

		return underscore.all(var_21_1[4], function(arg_22_0)
			local var_22_0 = var_21_1[1]

			if not var_21_2[var_22_0]:
				return False

			return table.contains(var_21_2[var_22_0], arg_22_0))
	elif var_21_1[2] == LinerTime.EVENT_SUB_TYPE.STORY:
		return pg.NewStoryMgr.GetInstance().IsPlayed(var_21_1[3])

	return False

def var_0_0.GetRemainExploreCnt(arg_23_0):
	local var_23_0 = 0

	for iter_23_0 = 1, arg_23_0.GetCurIdx():
		var_23_0 = var_23_0 + arg_23_0.times[iter_23_0].GetExploreCnt()

	return var_23_0 - #arg_23_0.GetExploredRoomIds()

def var_0_0.GetTimeId2ExploredIds(arg_24_0):
	local var_24_0 = {}
	local var_24_1 = 1
	local var_24_2 = arg_24_0.GetExploredRoomIds()

	for iter_24_0 = 1, arg_24_0.GetCurIdx():
		local var_24_3 = arg_24_0.times[iter_24_0]

		if var_24_3.GetType() == LinerTime.TYPE.EXPLORE:
			var_24_0[var_24_3.id] = {}

			local var_24_4 = var_24_3.GetExploreCnt()

			for iter_24_1 = var_24_1, math.min(var_24_1 + var_24_4 - 1, #var_24_2):
				table.insert(var_24_0[var_24_3.id], var_24_2[iter_24_1])

			var_24_1 = var_24_1 + var_24_4

	return var_24_0

def var_0_0.GetExploredRoomIds(arg_25_0):
	return arg_25_0.data4_list

def var_0_0.AddExploredRoom(arg_26_0, arg_26_1):
	table.insert(arg_26_0.GetExploredRoomIds(), arg_26_1)

def var_0_0.GetCurEventInfo(arg_27_0):
	return arg_27_0.curFinishEvents

def var_0_0.ClearCurEventInfo(arg_28_0):
	arg_28_0.curFinishEvents = {}

def var_0_0.AddEvent(arg_29_0, arg_29_1, arg_29_2):
	if not arg_29_0.curFinishEvents[arg_29_1]:
		arg_29_0.curFinishEvents[arg_29_1] = {}

	table.insert(arg_29_0.curFinishEvents[arg_29_1], arg_29_2)

def var_0_0.GetFinishEventIds(arg_30_0):
	local var_30_0 = {}

	for iter_30_0 = 1, arg_30_0.GetCurIdx() - 1:
		local var_30_1 = arg_30_0.times[iter_30_0]

		var_30_0 = table.mergeArray(var_30_0, var_30_1.GetEventIds(), True)

	for iter_30_1, iter_30_2 in pairs(arg_30_0.GetCurEventInfo()):
		var_30_0 = table.mergeArray(var_30_0, iter_30_2, True)

	return var_30_0

def var_0_0.AddTimeAwardFlag(arg_31_0, arg_31_1):
	arg_31_0.data1_list[arg_31_1] = 1

def var_0_0.IsGotTimeAward(arg_32_0, arg_32_1):
	return arg_32_0.data1_list[arg_32_1] and arg_32_0.data1_list[arg_32_1] != 0

def var_0_0.AddRoomAwardFlag(arg_33_0, arg_33_1):
	arg_33_0.data2_list[arg_33_1] = 1

def var_0_0.IsGotRoomAward(arg_34_0, arg_34_1):
	return arg_34_0.data2_list[arg_34_1] and arg_34_0.data2_list[arg_34_1] != 0

def var_0_0.AddEventAwardFlag(arg_35_0, arg_35_1, arg_35_2):
	arg_35_0.data3_list[arg_35_1] = arg_35_2

def var_0_0.IsGotEventAward(arg_36_0, arg_36_1):
	return arg_36_0.data3_list[arg_36_1] and arg_36_0.data3_list[arg_36_1] != 0

def var_0_0.GetEventAwardFlag(arg_37_0, arg_37_1):
	return arg_37_0.data3_list[arg_37_1]

def var_0_0.GetAllExploreRoomIds(arg_38_0):
	local var_38_0 = {}

	for iter_38_0, iter_38_1 in ipairs(arg_38_0.roomGroupIds):
		var_38_0 = table.mergeArray(var_38_0, pg.activity_liner_room_group[iter_38_1].ids, True)

	return var_38_0

def var_0_0.GetBgmName(arg_39_0):
	local var_39_0 = arg_39_0.getConfig("config_client").endingstory[1]

	if arg_39_0.IsFinishAllTime() and pg.NewStoryMgr.GetInstance().IsPlayed(var_39_0):
		local var_39_1 = os.date("*t", os.time()).hour
		local var_39_2 = arg_39_0.GetReallyTimeType(var_39_1)

		return arg_39_0.GetCurTime().GetBgm(var_39_2)
	else
		return arg_39_0.GetCurTime().GetBgm()

def var_0_0.GetReallyTimeType(arg_40_0, arg_40_1):
	local var_40_0 = arg_40_0.getConfig("config_client").endingtime

	for iter_40_0, iter_40_1 in ipairs(var_40_0):
		local var_40_1 = iter_40_1[1]

		if arg_40_1 >= var_40_1[1] and arg_40_1 < var_40_1[2]:
			return iter_40_1[2]

	return LinerTime.BG_TYPE.DAY

return var_0_0
