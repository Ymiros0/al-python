local var_0_0 = class("TechnologyCatchup", import(".BaseVO"))

var_0_0.STATE_UNSELECT = 1
var_0_0.STATE_CATCHUPING = 2
var_0_0.STATE_FINISHED_ALL = 3

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.version
	arg_1_0.configId = arg_1_0.id
	arg_1_0.ssrNum = arg_1_1.number or 0
	arg_1_0.urNums = arg_1_1.dr_numbers or {}

	arg_1_0.bulidTargetNums()

	arg_1_0.state = var_0_0.STATE_UNSELECT

	arg_1_0.updateState()

def var_0_0.bindConfigTable(arg_2_0):
	return pg.technology_catchup_template

def var_0_0.isUr(arg_3_0, arg_3_1):
	for iter_3_0, iter_3_1 in ipairs(arg_3_0.getConfig("ur_char")):
		if arg_3_1 == iter_3_1:
			return True

	return False

def var_0_0.bulidTargetNums(arg_4_0):
	arg_4_0.targetNums = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.getConfig("char_choice")):
		if arg_4_0.isUr(iter_4_1):
			for iter_4_2, iter_4_3 in pairs(arg_4_0.urNums):
				if iter_4_3.id == iter_4_1:
					arg_4_0.targetNums[iter_4_1] = iter_4_3.number or 0
		else
			arg_4_0.targetNums[iter_4_1] = arg_4_0.ssrNum

		if not arg_4_0.targetNums[iter_4_1]:
			arg_4_0.targetNums[iter_4_1] = 0

def var_0_0.getTargetNum(arg_5_0, arg_5_1):
	return arg_5_0.targetNums[arg_5_1]

def var_0_0.addTargetNum(arg_6_0, arg_6_1, arg_6_2):
	if arg_6_0.isUr(arg_6_1):
		arg_6_0.targetNums[arg_6_1] = arg_6_0.targetNums[arg_6_1] + arg_6_2
	else
		for iter_6_0, iter_6_1 in ipairs(arg_6_0.getConfig("char_choice")):
			if not arg_6_0.isUr(iter_6_1):
				arg_6_0.targetNums[iter_6_1] = arg_6_0.targetNums[iter_6_1] + arg_6_2

	arg_6_0.updateState()

def var_0_0.isFinish(arg_7_0, arg_7_1):
	if arg_7_0.isUr(arg_7_1):
		return arg_7_0.targetNums[arg_7_1] >= arg_7_0.getConfig("obtain_max_per_ur")
	else
		return arg_7_0.targetNums[arg_7_1] >= arg_7_0.getConfig("obtain_max")

def var_0_0.isFinishSSR(arg_8_0):
	local var_8_0 = True

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.getConfig("char_choice")):
		if not arg_8_0.isUr(iter_8_1) and not arg_8_0.isFinish(iter_8_1):
			var_8_0 = False

	return var_8_0

def var_0_0.isFinishAll(arg_9_0):
	local var_9_0 = True

	for iter_9_0, iter_9_1 in ipairs(arg_9_0.getConfig("char_choice")):
		if not arg_9_0.isFinish(iter_9_1):
			var_9_0 = False

	return var_9_0

def var_0_0.updateState(arg_10_0):
	local var_10_0 = getProxy(TechnologyProxy).curCatchupGroupID

	if arg_10_0.isFinishAll():
		arg_10_0.state = var_0_0.STATE_FINISHED_ALL
	elif arg_10_0.targetNums[var_10_0]:
		arg_10_0.state = var_0_0.STATE_CATCHUPING
	else
		arg_10_0.state = var_0_0.STATE_UNSELECT

def var_0_0.getState(arg_11_0):
	return arg_11_0.state

return var_0_0
