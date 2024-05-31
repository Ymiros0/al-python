local var_0_0 = class("Trophy", import(".BaseVO"))

var_0_0.INTAMACT_TYPE = 1043
var_0_0.COMPLEX_TROPHY_TYPE = 160
var_0_0.ALWAYS_SHOW = 0
var_0_0.ALWAYS_HIDE = 1
var_0_0.HIDE_BEFORE_UNLOCK = 2
var_0_0.COMING_SOON = 3

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_1.id
	arg_1_0.subTrophyList = {}

	arg_1_0.update(arg_1_1)

def var_0_0.generateDummyTrophy(arg_2_0):
	return (Trophy.New({
		progress = 0,
		timestamp = -1,
		id = arg_2_0
	}))

def var_0_0.bindConfigTable(arg_3_0):
	return pg.medal_template

def var_0_0.update(arg_4_0, arg_4_1):
	arg_4_0.progress = arg_4_1.progress
	arg_4_0.timestamp = arg_4_1.timestamp
	arg_4_0.new = arg_4_1.new

def var_0_0.isNew(arg_5_0):
	return arg_5_0.isNew == True

def var_0_0.clearNew(arg_6_0):
	arg_6_0.isNew = None

def var_0_0.updateTimeStamp(arg_7_0, arg_7_1):
	if arg_7_1 > 0:
		arg_7_0.isNew = True

	arg_7_0.timestamp = arg_7_1

def var_0_0.isComplexTrophy(arg_8_0):
	return arg_8_0.getConfig("target_type") == arg_8_0.COMPLEX_TROPHY_TYPE

def var_0_0.bindTrophys(arg_9_0, arg_9_1):
	arg_9_0.subTrophyList[arg_9_1.id] = arg_9_1

def var_0_0.getSubTrophy(arg_10_0):
	return arg_10_0.subTrophyList

def var_0_0.getTargetID(arg_11_0):
	return arg_11_0.getConfig("target_id")

def var_0_0.canClaimed(arg_12_0):
	return arg_12_0.getProgressRate() >= 1

def var_0_0.isClaimed(arg_13_0):
	return arg_13_0.timestamp > 0

def var_0_0.isDummy(arg_14_0):
	return arg_14_0.timestamp == -1

def var_0_0.getProgressRate(arg_15_0):
	local var_15_0, var_15_1 = arg_15_0.getProgress()

	return var_15_0 / var_15_1

def var_0_0.getProgress(arg_16_0):
	if arg_16_0.isComplexTrophy():
		local var_16_0 = 0

		for iter_16_0, iter_16_1 in pairs(arg_16_0.subTrophyList):
			if iter_16_1.isClaimed():
				var_16_0 = var_16_0 + 1

		return var_16_0, arg_16_0.getConfig("target_num")
	else
		return arg_16_0.progress, arg_16_0.getConfig("target_num")

def var_0_0.getHideType(arg_17_0):
	return arg_17_0.getConfig("hide")

def var_0_0.isHide(arg_18_0):
	local var_18_0 = arg_18_0.getConfig("hide")

	if var_18_0 == var_0_0.ALWAYS_HIDE:
		return True
	elif var_18_0 == var_0_0.HIDE_BEFORE_UNLOCK and arg_18_0.timestamp <= 0:
		return True
	else
		return False

def var_0_0.isMaxLevel(arg_19_0):
	local var_19_0 = arg_19_0.getConfig("next")
	local var_19_1 = arg_19_0.bindConfigTable()

	return var_19_0 == 0 or var_19_1[var_19_0] == None

def var_0_0.getTargetType(arg_20_0):
	return arg_20_0.getConfig("target_type")

return var_0_0
