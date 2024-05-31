local var_0_0 = class("VedioStep", import(".StoryStep"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.cpkPath = arg_1_1.cpkPath
	arg_1_0.skippable = defaultValue(arg_1_1.skippable, True)
	arg_1_0.blackFg = 1

def var_0_0.GetMode(arg_2_0):
	return Story.MODE_VEDIO

def var_0_0.GetVedioPath(arg_3_0):
	return arg_3_0.cpkPath

def var_0_0.GetSkipFlag(arg_4_0):
	return arg_4_0.skippable

return var_0_0
