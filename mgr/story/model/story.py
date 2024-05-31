local var_0_0 = class("Story")

var_0_0.MODE_ASIDE = 1
var_0_0.MODE_DIALOGUE = 2
var_0_0.MODE_BG = 3
var_0_0.MODE_CAROUSE = 4
var_0_0.MODE_VEDIO = 5
var_0_0.MODE_CAST = 6
var_0_0.STORY_AUTO_SPEED = {
	-9,
	0,
	5,
	9
}
var_0_0.TRIGGER_DELAY_TIME = {
	4,
	3,
	1.5,
	0
}

def var_0_0.GetStoryStepCls(arg_1_0):
	return ({
		AsideStep,
		DialogueStep,
		BgStep,
		CarouselStep,
		VedioStep,
		CastStep
	})[arg_1_0]

var_0_0.PLAYER = 2
var_0_0.TB = 4
var_0_0.PlaceholderMap = {
	playername = var_0_0.PLAYER,
	tb = var_0_0.TB
}

def var_0_0.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5):
	arg_2_0.name = arg_2_1.id
	arg_2_0.mode = arg_2_1.mode
	arg_2_0.once = arg_2_1.once
	arg_2_0.fadeOut = arg_2_1.fadeOut
	arg_2_0.hideSkip = defaultValue(arg_2_1.hideSkip, False)
	arg_2_0.skipTip = defaultValue(arg_2_1.skipTip, True)
	arg_2_0.noWaitFade = defaultValue(arg_2_1.noWaitFade, False)
	arg_2_0.dialogueBox = arg_2_1.dialogbox or 1
	arg_2_0.defaultTb = arg_2_1.defaultTb
	arg_2_0.placeholder = 0

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.placeholder or {}):
		local var_2_0 = var_0_0.PlaceholderMap[iter_2_1] or 0

		assert(var_2_0 > 0, iter_2_1)

		arg_2_0.placeholder = bit.bor(arg_2_0.placeholder, var_2_0)

	arg_2_0.hideRecord = defaultValue(arg_2_1.hideRecord, False)
	arg_2_0.hideAutoBtn = defaultValue(arg_2_1.hideAuto, False)
	arg_2_0.storyAlpha = defaultValue(arg_2_1.alpha, 0.568)

	if UnGamePlayState:
		arg_2_0.speedData = arg_2_1.speed or 0
	else
		arg_2_0.speedData = arg_2_1.speed or getProxy(SettingsProxy).GetStorySpeed() or 0

	arg_2_0.steps = {}

	local var_2_1 = 0
	local var_2_2 = arg_2_3 or {}
	local var_2_3 = {}

	for iter_2_2, iter_2_3 in ipairs(arg_2_1.scripts or {}):
		local var_2_4 = iter_2_3.mode or arg_2_0.mode
		local var_2_5 = var_0_0.GetStoryStepCls(var_2_4).New(iter_2_3)

		var_2_5.SetId(iter_2_2)
		var_2_5.SetPlaceholderType(arg_2_0.GetPlaceholder())
		var_2_5.SetDefaultTb(arg_2_0.defaultTb)

		if var_2_5.ExistOption():
			var_2_1 = var_2_1 + 1

			if var_2_2[var_2_1]:
				var_2_5.SetOptionSelCodes(var_2_2[var_2_1])

			if arg_2_4:
				var_2_5.important = True

			table.insert(var_2_3, iter_2_2)

			if arg_2_5:
				var_2_5.AutoShowOption()

		table.insert(arg_2_0.steps, var_2_5)

	if #arg_2_0.steps > 0:
		table.insert(var_2_3, #arg_2_0.steps)

	arg_2_0.HandleRecallOptions(var_2_3)

	arg_2_0.branchCode = None
	arg_2_0.force = arg_2_2

	if UnGamePlayState:
		arg_2_0.isPlayed = False
	else
		arg_2_0.isPlayed = pg.NewStoryMgr.GetInstance().IsPlayed(arg_2_0.name)

	arg_2_0.nextScriptName = None
	arg_2_0.skipAll = False
	arg_2_0.isAuto = False
	arg_2_0.speed = 0

def var_0_0.HandleRecallOptions(arg_3_0, arg_3_1):
	local function var_3_0(arg_4_0, arg_4_1)
		local var_4_0 = arg_3_0.steps[arg_4_0]
		local var_4_1 = {}

		for iter_4_0 = arg_4_0, arg_4_1:
			local var_4_2 = arg_3_0.steps[iter_4_0]

			table.insert(var_4_1, var_4_2)

		local var_4_3 = var_4_0.GetOptionCnt()

		return {
			var_4_1,
			var_4_3,
			arg_4_1,
			arg_4_0
		}

	local function var_3_1(arg_5_0)
		for iter_5_0 = arg_5_0, 1, -1:
			local var_5_0 = arg_3_0.steps[iter_5_0]

			if var_5_0 and var_5_0.branchCode != None:
				return iter_5_0

		assert(False)

	local var_3_2 = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_1):
		if arg_3_0.steps[iter_3_1].IsRecallOption():
			local var_3_3 = iter_3_1
			local var_3_4 = arg_3_1[iter_3_0 + 1]

			if var_3_3 and var_3_4:
				local var_3_5 = var_3_1(var_3_4)

				table.insert(var_3_2, var_3_0(var_3_3, var_3_5))

	local var_3_6 = 0

	for iter_3_2, iter_3_3 in ipairs(var_3_2):
		local var_3_7 = iter_3_3[1]
		local var_3_8 = iter_3_3[2]
		local var_3_9 = iter_3_3[3]
		local var_3_10 = iter_3_3[4]

		for iter_3_4 = 1, var_3_8 - 1:
			local var_3_11 = var_3_9 + var_3_6

			for iter_3_5, iter_3_6 in ipairs(var_3_7):
				local var_3_12 = Clone(iter_3_6)

				var_3_12.SetId(var_3_10)
				table.insert(arg_3_0.steps, var_3_11 + iter_3_5, var_3_12)

		var_3_6 = var_3_6 + (var_3_8 - 1) * #var_3_7

def var_0_0.GetPlaceholder(arg_6_0):
	return arg_6_0.placeholder

def var_0_0.ShouldReplaceContent(arg_7_0):
	return arg_7_0.placeholder > 0

def var_0_0.GetStoryAlpha(arg_8_0):
	return arg_8_0.storyAlpha

def var_0_0.ShouldHideAutoBtn(arg_9_0):
	return arg_9_0.hideAutoBtn

def var_0_0.ShouldHideRecord(arg_10_0):
	return arg_10_0.hideRecord

def var_0_0.GetDialogueStyleName(arg_11_0):
	return arg_11_0.dialogueBox

def var_0_0.IsDialogueStyle2(arg_12_0):
	return arg_12_0.GetDialogueStyleName() == 2

def var_0_0.GetTriggerDelayTime(arg_13_0):
	local var_13_0 = table.indexof(var_0_0.STORY_AUTO_SPEED, arg_13_0.speed)

	if var_13_0:
		return var_0_0.TRIGGER_DELAY_TIME[var_13_0] or 0

	return 0

def var_0_0.SetAutoPlay(arg_14_0):
	arg_14_0.isAuto = True

	arg_14_0.SetPlaySpeed(arg_14_0.speedData)

def var_0_0.UpdatePlaySpeed(arg_15_0):
	local var_15_0 = getProxy(SettingsProxy).GetStorySpeed() or 0

	arg_15_0.SetPlaySpeed(var_15_0)

def var_0_0.GetPlaySpeed(arg_16_0):
	return arg_16_0.speed

def var_0_0.StopAutoPlay(arg_17_0):
	arg_17_0.isAuto = False

	arg_17_0.ResetSpeed()

def var_0_0.SetPlaySpeed(arg_18_0, arg_18_1):
	arg_18_0.speed = arg_18_1

def var_0_0.ResetSpeed(arg_19_0):
	arg_19_0.speed = 0

def var_0_0.GetPlaySpeed(arg_20_0):
	return arg_20_0.speed

def var_0_0.GetAutoPlayFlag(arg_21_0):
	return arg_21_0.isAuto

def var_0_0.ShowSkipTip(arg_22_0):
	return arg_22_0.skipTip

def var_0_0.ShouldWaitFadeout(arg_23_0):
	return not arg_23_0.noWaitFade

def var_0_0.ShouldHideSkip(arg_24_0):
	return arg_24_0.hideSkip

def var_0_0.CanPlay(arg_25_0):
	return arg_25_0.force or not arg_25_0.isPlayed

def var_0_0.GetId(arg_26_0):
	return arg_26_0.name

def var_0_0.GetName(arg_27_0):
	return arg_27_0.name

def var_0_0.GetStepByIndex(arg_28_0, arg_28_1):
	local var_28_0 = arg_28_0.steps[arg_28_1]

	if not var_28_0 or arg_28_0.branchCode and not var_28_0.IsSameBranch(arg_28_0.branchCode):
		return None

	return var_28_0

def var_0_0.GetNextStep(arg_29_0, arg_29_1):
	if arg_29_1 >= #arg_29_0.steps:
		return None

	local var_29_0 = arg_29_1 + 1
	local var_29_1 = arg_29_0.GetStepByIndex(var_29_0)

	if not var_29_1 and var_29_0 < #arg_29_0.steps:
		return arg_29_0.GetNextStep(var_29_0)
	else
		return var_29_1

def var_0_0.GetPrevStep(arg_30_0, arg_30_1):
	if arg_30_1 <= 1:
		return None

	local var_30_0 = arg_30_1 - 1
	local var_30_1 = arg_30_0.GetStepByIndex(var_30_0)

	if not var_30_1 and var_30_0 > 1:
		return arg_30_0.GetPrevStep(var_30_0)
	else
		return var_30_1

def var_0_0.ShouldFadeout(arg_31_0):
	return arg_31_0.fadeOut != None

def var_0_0.GetFadeoutTime(arg_32_0):
	return arg_32_0.fadeOut

def var_0_0.IsPlayed(arg_33_0):
	return arg_33_0.isPlayed

def var_0_0.SetBranchCode(arg_34_0, arg_34_1):
	arg_34_0.branchCode = arg_34_1

def var_0_0.GetBranchCode(arg_35_0):
	return arg_35_0.branchCode

def var_0_0.GetNextScriptName(arg_36_0):
	return arg_36_0.nextScriptName

def var_0_0.SetNextScriptName(arg_37_0, arg_37_1):
	arg_37_0.nextScriptName = arg_37_1

def var_0_0.SkipAll(arg_38_0):
	arg_38_0.skipAll = True

def var_0_0.StopSkip(arg_39_0):
	arg_39_0.skipAll = False

def var_0_0.ShouldSkipAll(arg_40_0):
	return arg_40_0.skipAll

def var_0_0.GetUsingPaintingNames(arg_41_0):
	local var_41_0 = {}

	for iter_41_0, iter_41_1 in ipairs(arg_41_0.steps):
		local var_41_1 = iter_41_1.GetUsingPaintingNames()

		for iter_41_2, iter_41_3 in ipairs(var_41_1):
			var_41_0[iter_41_3] = True

	local var_41_2 = {}

	for iter_41_4, iter_41_5 in pairs(var_41_0):
		table.insert(var_41_2, iter_41_4)

	return var_41_2

def var_0_0.GetAllStepDispatcherRecallName(arg_42_0):
	local var_42_0 = {}

	for iter_42_0, iter_42_1 in ipairs(arg_42_0.steps):
		local var_42_1 = iter_42_1.GetDispatcherRecallName()

		if var_42_1:
			var_42_0[var_42_1] = True

	local var_42_2 = {}

	for iter_42_2, iter_42_3 in pairs(var_42_0):
		table.insert(var_42_2, iter_42_2)

	return var_42_2

return var_0_0
