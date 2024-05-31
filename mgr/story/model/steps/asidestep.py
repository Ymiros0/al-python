local var_0_0 = class("AsideStep", import(".StoryStep"))

var_0_0.ASIDE_TYPE_HRZ = 1
var_0_0.ASIDE_TYPE_VEC = 2
var_0_0.ASIDE_TYPE_LEFTBOTTOMVEC = 3
var_0_0.ASIDE_TYPE_CENTERWITHFRAME = 4
var_0_0.SHOW_MODE_DEFAUT = 1
var_0_0.SHOW_MODE_BUBBLE = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.sequence = arg_1_1.sequence
	arg_1_0.asideType = arg_1_1.asideType or var_0_0.ASIDE_TYPE_HRZ
	arg_1_0.signDate = arg_1_1.signDate
	arg_1_0.hideBgAlpha = arg_1_1.hideBgAlpha
	arg_1_0.rectOffset = arg_1_1.rectOffset
	arg_1_0.spacing = arg_1_1.spacing
	arg_1_0.typewriterSpeed = arg_1_1.typewriterTime

	if arg_1_0.asideType == var_0_0.ASIDE_TYPE_LEFTBOTTOMVEC and not arg_1_1.showMode:
		arg_1_0.showMode = var_0_0.SHOW_MODE_BUBBLE
	else
		arg_1_0.showMode = arg_1_1.showMode or var_0_0.SHOW_MODE_DEFAUT

	if arg_1_0.asideType == var_0_0.ASIDE_TYPE_CENTERWITHFRAME:
		arg_1_0.hideBgAlpha = True

def var_0_0.GetMode(arg_2_0):
	return Story.MODE_ASIDE

def var_0_0.GetTypewriterSpeed(arg_3_0):
	return arg_3_0.typewriterSpeed or 0.1

def var_0_0.GetSequence(arg_4_0):
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.sequence or {}):
		table.insert(var_4_0, {
			iter_4_1[1],
			iter_4_1[2]
		})

	return var_4_0

def var_0_0.GetAsideType(arg_5_0):
	return arg_5_0.asideType

def var_0_0.GetDateSign(arg_6_0):
	return arg_6_0.signDate

def var_0_0.GetShowMode(arg_7_0):
	return arg_7_0.showMode

def var_0_0.ShouldHideBGAlpha(arg_8_0):
	return arg_8_0.hideBgAlpha

def var_0_0.ShouldUpdateSpacing(arg_9_0):
	return arg_9_0.spacing != None

def var_0_0.GetSpacing(arg_10_0):
	return arg_10_0.spacing

def var_0_0.ShouldUpdatePadding(arg_11_0):
	return arg_11_0.rectOffset != None

def var_0_0.GetPadding(arg_12_0):
	local var_12_0 = arg_12_0.rectOffset

	return var_12_0[1] or 0, var_12_0[2] or 0, var_12_0[3] or 0, var_12_0[4] or 0

return var_0_0
