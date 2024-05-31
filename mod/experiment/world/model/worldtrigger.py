local var_0_0 = class("WorldTrigger", import("...BaseEntity"))

var_0_0.Fields = {
	config = "table",
	progress = "number",
	id = "number",
	maxProgress = "number",
	desc = "string"
}

def var_0_0.Setup(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1

def var_0_0.GetProgress(arg_2_0):
	return arg_2_0.progress

def var_0_0.GetMaxProgress(arg_3_0):
	return arg_3_0.maxProgress

def var_0_0.GetDesc(arg_4_0):
	return string.format("%s(%s/%s)", arg_4_0.desc, arg_4_0.progress, arg_4_0.maxProgress)

def var_0_0.IsAchieved(arg_5_0):
	return arg_5_0.GetProgress() >= arg_5_0.GetMaxProgress()

return var_0_0
