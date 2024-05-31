local var_0_0 = class("ActivityPtData")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.dropList = arg_1_1.getDataConfig("drop_client")
	arg_1_0.targets = arg_1_1.getDataConfig("target")
	arg_1_0.resId = arg_1_1.getDataConfig("pt")
	arg_1_0.bindActId = arg_1_1.getDataConfig("id_2")
	arg_1_0.unlockDay = arg_1_1.getDataConfig("day_unlock")
	arg_1_0.type = arg_1_1.getDataConfig("type")

	arg_1_0.Update(arg_1_1)

def var_0_0.Update(arg_2_0, arg_2_1):
	arg_2_0.activity = arg_2_1
	arg_2_0.count = arg_2_1.data1
	arg_2_0.level = 0

	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.data1_list):
		table.insert(var_2_0, iter_2_1)

	table.sort(var_2_0)

	for iter_2_2, iter_2_3 in ipairs(var_2_0):
		if iter_2_3 == arg_2_0.targets[iter_2_2]:
			arg_2_0.level = iter_2_2
		else
			break

	arg_2_0.startTime = arg_2_1.data2
	arg_2_0.value2 = arg_2_1.data3
	arg_2_0.isDayUnlock = arg_2_0.CheckDayUnlock() and 1 or 0
	arg_2_0.curHasBuffs = arg_2_1.data2_list
	arg_2_0.curBuffs = arg_2_1.data3_list

def var_0_0.CheckDayUnlock(arg_3_0):
	local var_3_0 = math.min(arg_3_0.level + 1, #arg_3_0.targets)
	local var_3_1 = pg.TimeMgr.GetInstance()

	return var_3_1.DiffDay(arg_3_0.startTime, var_3_1.GetServerTime()) + 1 >= (arg_3_0.unlockDay[var_3_0] or 0)

def var_0_0.GetDayUnlockStamps(arg_4_0):
	local var_4_0 = pg.TimeMgr.GetInstance()
	local var_4_1 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.unlockDay):
		local var_4_2 = arg_4_0.startTime + (iter_4_1 - 1) * 86400

		table.insert(var_4_1, var_4_2)

	return var_4_1

def var_0_0.GetLevelProgress(arg_5_0):
	local var_5_0 = arg_5_0.getTargetLevel()

	return var_5_0, #arg_5_0.targets, var_5_0 / #arg_5_0.targets

def var_0_0.GetResProgress(arg_6_0):
	local var_6_0 = arg_6_0.getTargetLevel()

	return arg_6_0.count, arg_6_0.targets[var_6_0], arg_6_0.count / arg_6_0.targets[var_6_0]

def var_0_0.GetUnlockedMaxResRequire(arg_7_0):
	local var_7_0 = pg.TimeMgr.GetInstance()
	local var_7_1 = var_7_0.DiffDay(arg_7_0.startTime, var_7_0.GetServerTime()) + 1

	for iter_7_0 = #arg_7_0.targets, 1, -1:
		if var_7_1 >= arg_7_0.unlockDay[iter_7_0]:
			return arg_7_0.targets[iter_7_0]

	return 1

def var_0_0.GetTotalResRequire(arg_8_0):
	return arg_8_0.targets[#arg_8_0.targets]

def var_0_0.GetId(arg_9_0):
	return arg_9_0.activity.id

def var_0_0.GetRes(arg_10_0):
	return {
		type = 1,
		id = arg_10_0.resId
	}

def var_0_0.GetAward(arg_11_0):
	local var_11_0 = arg_11_0.dropList[arg_11_0.getTargetLevel()]

	return Drop.New({
		type = var_11_0[1],
		id = var_11_0[2],
		count = var_11_0[3]
	})

def var_0_0.GetResItemId(arg_12_0):
	return arg_12_0.GetAward().id

def var_0_0.GetValue2(arg_13_0):
	return arg_13_0.value2

def var_0_0.getTargetLevel(arg_14_0):
	return math.min(arg_14_0.level + arg_14_0.isDayUnlock, #arg_14_0.targets)

def var_0_0.GetLevel(arg_15_0):
	return arg_15_0.level

def var_0_0.CanGetAward(arg_16_0):
	local function var_16_0()
		local var_17_0, var_17_1, var_17_2 = arg_16_0.GetResProgress()

		return var_17_2 >= 1

	return arg_16_0.CanGetNextAward() and var_16_0()

def var_0_0.CanGetNextAward(arg_18_0):
	return arg_18_0.isDayUnlock > 0 and arg_18_0.level < #arg_18_0.targets

def var_0_0.CanGetMorePt(arg_19_0):
	local var_19_0 = getProxy(ActivityProxy).getActivityById(arg_19_0.bindActId)

	return var_19_0 and not var_19_0.isEnd()

def var_0_0.CanTrain(arg_20_0):
	if not arg_20_0.isInBuffTime():
		return False

	local function var_20_0(arg_21_0)
		for iter_21_0, iter_21_1 in ipairs(arg_20_0.curHasBuffs):
			if arg_21_0 == iter_21_1:
				return False

		return True

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.activity.getDataConfig("target_buff")):
		if var_20_0(iter_20_1) and iter_20_1 <= arg_20_0.level + 1:
			return iter_20_1

	return False

def var_0_0.GetCurBuffInfos(arg_22_0):
	local var_22_0 = {}
	local var_22_1 = #arg_22_0.activity.getDataConfig("buff_group")

	for iter_22_0, iter_22_1 in ipairs(arg_22_0.curBuffs):
		for iter_22_2, iter_22_3 in ipairs(arg_22_0.activity.getDataConfig("buff_group")):
			for iter_22_4, iter_22_5 in ipairs(iter_22_3):
				if iter_22_1 == iter_22_5:
					local var_22_2 = {
						id = iter_22_5,
						lv = iter_22_4,
						group = iter_22_2,
						next = iter_22_3[iter_22_4 + 1],
						award = arg_22_0.GetBuffAwardInfo(iter_22_3[#iter_22_3])
					}

					table.insert(var_22_0, var_22_2)

	return var_22_0

def var_0_0.GetBuffAwardInfo(arg_23_0, arg_23_1):
	local var_23_0 = arg_23_0.activity.getDataConfig("drop_display")

	if var_23_0 == "":
		return None

	for iter_23_0, iter_23_1 in ipairs(var_23_0):
		if arg_23_1 == iter_23_1[1]:
			local var_23_1 = iter_23_1[2]

			return {
				type = var_23_1[1],
				id = var_23_1[2],
				count = var_23_1[3]
			}

	return None

def var_0_0.GetBuffLevelProgress(arg_24_0):
	local var_24_0 = False
	local var_24_1, var_24_2 = (function()
		for iter_25_0, iter_25_1 in ipairs(arg_24_0.activity.getDataConfig("target_buff")):
			if iter_25_1 > arg_24_0.level:
				return iter_25_0, iter_25_1

		var_24_0 = True

		return #arg_24_0.activity.getDataConfig("target_buff") + 1, 1)()
	local var_24_3 = (var_24_1 == 1 and True or False) and 0 or arg_24_0.activity.getDataConfig("target_buff")[var_24_1 - 1]

	return var_24_1, var_24_0 and 1 or (arg_24_0.level - var_24_3) / (var_24_2 - var_24_3)

def var_0_0.isInBuffTime(arg_26_0):
	local var_26_0 = arg_26_0.activity.getDataConfig("buff_time")

	if type(var_26_0) == "table":
		local var_26_1 = pg.TimeMgr.GetInstance().GetServerTime()
		local var_26_2 = {
			year = var_26_0[1][1],
			month = var_26_0[1][2],
			day = var_26_0[1][3],
			hour = var_26_0[2][1],
			min = var_26_0[2][2],
			sec = var_26_0[2][3]
		}

		return var_26_1 < pg.TimeMgr.GetInstance().Table2ServerTime(var_26_2) and True or False
	elif var_26_0 == "always":
		return True
	elif var_26_0 == "stop":
		return False

	return False

def var_0_0.GetDrop(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_0.dropList[arg_27_1]

	return {
		type = var_27_0[1],
		id = var_27_0[2],
		count = var_27_0[3]
	}

def var_0_0.GetPtTarget(arg_28_0, arg_28_1):
	if arg_28_1 <= 0:
		return 0
	elif arg_28_1 > #arg_28_0.targets:
		return arg_28_0.targets[#arg_28_0.targets]
	else
		return arg_28_0.targets[arg_28_1]

def var_0_0.GetCurrLevel(arg_29_0):
	for iter_29_0, iter_29_1 in ipairs(arg_29_0.targets):
		if iter_29_1 > arg_29_0.count:
			return iter_29_0 - 1

	return #arg_29_0.targets

def var_0_0.IsMaxLevel(arg_30_0):
	return arg_30_0.GetCurrLevel() == #arg_30_0.targets

def var_0_0.GetNextLevel(arg_31_0):
	for iter_31_0, iter_31_1 in ipairs(arg_31_0.targets):
		if iter_31_1 > arg_31_0.count:
			return iter_31_0

	return #arg_31_0.targets

def var_0_0.GetCurrTarget(arg_32_0):
	local var_32_0 = arg_32_0.GetCurrLevel()

	return arg_32_0.GetPtTarget(var_32_0)

def var_0_0.GetNextLevelTarget(arg_33_0):
	local var_33_0 = arg_33_0.GetNextLevel()

	return arg_33_0.GetPtTarget(var_33_0)

def var_0_0.IsGotLevelAward(arg_34_0, arg_34_1):
	local var_34_0 = arg_34_0.GetPtTarget(arg_34_1)

	for iter_34_0, iter_34_1 in ipairs(arg_34_0.activity.data1_list):
		if iter_34_1 == var_34_0:
			return True

	return False

def var_0_0.GetLastAward(arg_35_0):
	local var_35_0 = arg_35_0.dropList[#arg_35_0.targets]

	return {
		type = var_35_0[1],
		id = var_35_0[2],
		count = var_35_0[3]
	}

var_0_0.STATE_LOCK = 1
var_0_0.STATE_CAN_GET = 2
var_0_0.STATE_GOT = 3

def var_0_0.GetDroptItemState(arg_36_0, arg_36_1):
	if arg_36_1 > arg_36_0.GetCurrLevel():
		return var_0_0.STATE_LOCK
	elif arg_36_0.IsGotLevelAward(arg_36_1):
		return var_0_0.STATE_GOT
	else
		return var_0_0.STATE_CAN_GET

def var_0_0.AnyAwardCanGet(arg_37_0):
	for iter_37_0, iter_37_1 in ipairs(arg_37_0.targets):
		if arg_37_0.GetDroptItemState(iter_37_0) == var_0_0.STATE_CAN_GET:
			return True

	return False

return var_0_0
