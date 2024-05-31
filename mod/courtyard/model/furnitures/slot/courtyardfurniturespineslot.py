local var_0_0 = class("CourtYardFurnitureSpineSlot", import(".CourtYardFurnitureBaseSlot"))
local var_0_1 = 0
local var_0_2 = 1
local var_0_3 = 2
local var_0_4 = 3

def var_0_0.OnInit(arg_1_0, arg_1_1):
	arg_1_0.name = arg_1_1[1][1]
	arg_1_0.defaultAction = arg_1_1[1][2]
	arg_1_0.mask = arg_1_1[2] and arg_1_1[2][1]

	if arg_1_0.mask:
		arg_1_0.maskDefaultAction = arg_1_1[2][2]

	arg_1_0.bodyMask = arg_1_1[4] and #arg_1_1[4] > 0 and {
		offset = arg_1_1[4][1] and Vector3(arg_1_1[4][1][1], arg_1_1[4][1][2], 0) or Vector3.zero,
		size = arg_1_1[4][2] and Vector3(arg_1_1[4][2][1], arg_1_1[4][2][2], 0) or Vector3.zero,
		img = arg_1_1[4][3]
	}
	arg_1_0.offset = arg_1_1[5] and Vector3(arg_1_1[5][1], arg_1_1[5][2], 0) or Vector3.zero
	arg_1_0.scale = arg_1_1[6] and Vector3(arg_1_1[6][1], arg_1_1[6][2], 0) or Vector3.one
	arg_1_0.substituteActions = {}
	arg_1_0.actions = {}
	arg_1_0.loop = False
	arg_1_0.vaild = tobool(arg_1_1[3]) and tobool(arg_1_1[3][3])

	if arg_1_0.vaild:
		arg_1_0.actions = arg_1_1[3][2]

		local var_1_0 = arg_1_1[3][3][2] or var_0_1

		if var_1_0 == True:
			var_1_0 = var_0_2

		if arg_1_1[3][5]:
			var_1_0 = var_0_4

		arg_1_0.strategyType = var_1_0
		arg_1_0.updateStrategy = arg_1_0.InitUpdateStrategy(var_1_0)
		arg_1_0.preheatAction = arg_1_1[3][3][3]
		arg_1_0.tailAction = arg_1_1[3][3][4]
		arg_1_0.loop = arg_1_1[3][4][1] == 1
		arg_1_0.variedActions = arg_1_1[3][5]

def var_0_0.InitUpdateStrategy(arg_2_0, arg_2_1):
	local var_2_0

	if arg_2_1 == var_0_2:
		var_2_0 = CourtYardFollowInteraction.New(arg_2_0)
	elif arg_2_1 == var_0_3:
		var_2_0 = CourtYardMonglineInteraction.New(arg_2_0)
	elif arg_2_1 == var_0_4:
		var_2_0 = CourtYardVariedInteraction.New(arg_2_0)
	else
		var_2_0 = CourtYardInteraction.New(arg_2_0)

	return var_2_0

def var_0_0.SetAnimators(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1[1]
	local var_3_1 = var_3_0[arg_3_0.id] or var_3_0[1] or {}
	local var_3_2 = type(var_3_1) == "string" and {
		var_3_1
	} or var_3_1

	for iter_3_0, iter_3_1 in ipairs(var_3_2):
		table.insert(arg_3_0.animators, {
			key = arg_3_0.id .. "_" .. iter_3_0,
			value = iter_3_1
		})

def var_0_0.SetFollower(arg_4_0, arg_4_1):
	arg_4_0.follower = {
		bone = arg_4_1[1],
		scale = Vector3(arg_4_1[2], 1, 1)
	}

def var_0_0.SetSubstitute(arg_5_0, arg_5_1):
	arg_5_0.substituteActions = _.map(arg_5_1, function(arg_6_0)
		return {
			action = arg_6_0[1],
			match = arg_6_0[2],
			replace = arg_6_0[3],
			replace_mode = arg_6_0[4],
			math_mode = arg_6_0[5]
		})

def var_0_0.GetSubstituteAction(arg_7_0, arg_7_1, arg_7_2):
	local function var_7_0(arg_8_0)
		local var_8_0 = arg_7_0.GetUser()
		local var_8_1 = arg_8_0.math_mode == 1 and var_8_0.GetSkinID() or var_8_0.GetGroupID()

		return table.contains(arg_8_0.match, var_8_1) and (arg_8_0.replace_mode == 0 or arg_8_0.replace_mode == arg_7_2)

	local var_7_1 = _.detect(arg_7_0.substituteActions, function(arg_9_0)
		return arg_9_0.action == arg_7_1 and var_7_0(arg_9_0))

	return var_7_1 and var_7_1.replace or arg_7_1

def var_0_0.GetUserSubstituteAction(arg_10_0, arg_10_1):
	return arg_10_0.GetSubstituteAction(arg_10_1, 1)

def var_0_0.GetOwnerSubstituteAction(arg_11_0, arg_11_1):
	return arg_11_0.GetSubstituteAction(arg_11_1, 2)

def var_0_0.IsEmpty(arg_12_0):
	return var_0_0.super.IsEmpty(arg_12_0) and arg_12_0.vaild

def var_0_0.GetScale(arg_13_0):
	if arg_13_0.follower:
		return arg_13_0.follower.scale
	else
		return arg_13_0.scale

local function var_0_5(arg_14_0)
	local var_14_0 = {}
	local var_14_1 = {}
	local var_14_2 = {}
	local var_14_3 = arg_14_0.actions[1][2]
	local var_14_4 = arg_14_0.actions[1][3]

	for iter_14_0, iter_14_1 in ipairs(arg_14_0.variedActions):
		local var_14_5 = iter_14_1[math.random(1, #iter_14_1)]

		table.insert(var_14_0, var_14_5)
		table.insert(var_14_1, var_14_4)
		table.insert(var_14_2, var_14_3)

	return var_14_0, var_14_1, var_14_2

local function var_0_6(arg_15_0)
	local var_15_0 = {}
	local var_15_1 = {}
	local var_15_2 = {}

	for iter_15_0, iter_15_1 in ipairs(arg_15_0.actions):
		local var_15_3 = iter_15_1[1]
		local var_15_4 = iter_15_1[3]
		local var_15_5 = type(var_15_3) == "table" and var_15_3[math.random(1, #var_15_3)] or var_15_3
		local var_15_6 = arg_15_0.GetOwnerSubstituteAction(var_15_5)

		table.insert(var_15_0, var_15_6)

		local var_15_7 = arg_15_0.GetUserSubstituteAction(var_15_4 or var_15_5)

		table.insert(var_15_1, var_15_7)
		table.insert(var_15_2, tobool(iter_15_1[2]))

	return var_15_0, var_15_1, var_15_2

def var_0_0.GetActions(arg_16_0):
	local var_16_0
	local var_16_1

	if arg_16_0.preheatAction and type(arg_16_0.preheatAction) == "string":
		var_16_0 = arg_16_0.preheatAction
	elif arg_16_0.preheatAction and type(arg_16_0.preheatAction) == "table":
		var_16_0, var_16_1 = arg_16_0.preheatAction[1], arg_16_0.preheatAction[2]

	local var_16_2
	local var_16_3
	local var_16_4

	if arg_16_0.strategyType == var_0_4:
		var_16_2, var_16_3, var_16_4 = var_0_5(arg_16_0)
	else
		var_16_2, var_16_3, var_16_4 = var_0_6(arg_16_0)

	return var_16_2, var_16_3, var_16_4, var_16_0, var_16_1, arg_16_0.tailAction

def var_0_0.OnAwake(arg_17_0):
	if #arg_17_0.animators > 0:
		arg_17_0.animatorIndex = math.random(1, #arg_17_0.animators)

def var_0_0.OnStart(arg_18_0):
	arg_18_0.updateStrategy.Update(arg_18_0.loop)

def var_0_0.OnContinue(arg_19_0, arg_19_1):
	arg_19_0.updateStrategy.StepEnd(arg_19_1)

def var_0_0.Reset(arg_20_0):
	arg_20_0.updateStrategy.Reset()

def var_0_0.GetSpineDefaultAction(arg_21_0):
	return arg_21_0.defaultAction

def var_0_0.GetSpineMaskDefaultAcation(arg_22_0):
	return arg_22_0.maskDefaultAction

return var_0_0
