local var_0_0 = class("LimitChallengeProxy", import(".NetProxy"))

def var_0_0.register(arg_1_0):
	arg_1_0.initData()

def var_0_0.initData(arg_2_0):
	arg_2_0.passTimeDict = {}
	arg_2_0.awardedDict = {}
	arg_2_0.curMonthPassedIDList = {}

def var_0_0.setTimeDataFromServer(arg_3_0, arg_3_1):
	for iter_3_0, iter_3_1 in ipairs(arg_3_1):
		local var_3_0 = iter_3_1.key
		local var_3_1 = iter_3_1.value

		arg_3_0.passTimeDict[var_3_0] = var_3_1

def var_0_0.setAwardedDataFromServer(arg_4_0, arg_4_1):
	for iter_4_0, iter_4_1 in ipairs(arg_4_1):
		local var_4_0 = iter_4_1.key
		local var_4_1 = iter_4_1.value > 0

		arg_4_0.awardedDict[var_4_0] = var_4_1

def var_0_0.setCurMonthPassedIDList(arg_5_0, arg_5_1):
	for iter_5_0, iter_5_1 in ipairs(arg_5_1):
		table.insert(arg_5_0.curMonthPassedIDList, iter_5_1)

def var_0_0.setPassTime(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = arg_6_0.passTimeDict[arg_6_1]

	if not var_6_0:
		arg_6_0.passTimeDict[arg_6_1] = arg_6_2
	elif arg_6_2 < var_6_0:
		arg_6_0.passTimeDict[arg_6_1] = arg_6_2

		arg_6_0.sendNotification(LimitChallengeConst.UPDATE_PASS_TIME)

	if not table.contains(arg_6_0.curMonthPassedIDList, arg_6_1):
		table.insert(arg_6_0.curMonthPassedIDList, arg_6_1)

def var_0_0.setAwarded(arg_7_0, arg_7_1):
	arg_7_0.awardedDict[arg_7_1] = True

def var_0_0.getPassTimeByChallengeID(arg_8_0, arg_8_1):
	return arg_8_0.passTimeDict[arg_8_1]

def var_0_0.getMissAwardChallengeIDLIst(arg_9_0):
	local var_9_0 = {}
	local var_9_1 = LimitChallengeConst.GetCurMonthConfig().stage

	for iter_9_0, iter_9_1 in ipairs(var_9_1):
		local var_9_2 = table.contains(arg_9_0.curMonthPassedIDList, iter_9_1)
		local var_9_3 = arg_9_0.isAwardedByChallengeID(iter_9_1)

		if var_9_2 and not var_9_3:
			table.insert(var_9_0, iter_9_1)

	return var_9_0

def var_0_0.isAwardedByChallengeID(arg_10_0, arg_10_1):
	return arg_10_0.awardedDict[arg_10_1]

def var_0_0.isLevelUnlock(arg_11_0, arg_11_1):
	if arg_11_1 == 1:
		return True

	if arg_11_1 > 1:
		local var_11_0 = LimitChallengeConst.GetChallengeIDByLevel(arg_11_1 - 1)

		return arg_11_0.awardedDict[var_11_0]

return var_0_0
