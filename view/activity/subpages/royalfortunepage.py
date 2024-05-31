local var_0_0 = class("RoyalFortunePage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.painting = arg_1_0.findTF("painting", arg_1_0.bg)

def var_0_0.OnUpdateFlush(arg_2_0):
	var_0_0.super.OnUpdateFlush(arg_2_0)

	if arg_2_0.IsLastTaskFinish():
		local var_2_0 = math.random(#arg_2_0.taskGroup)

		GetImageSpriteFromAtlasAsync("ui/activityuipage/royalfortunepage_atlas", var_2_0, arg_2_0.painting)
	else
		GetImageSpriteFromAtlasAsync("ui/activityuipage/royalfortunepage_atlas", arg_2_0.nday, arg_2_0.painting)

def var_0_0.IsLastTaskFinish(arg_3_0):
	if arg_3_0.nday != #arg_3_0.taskGroup:
		return False

	local var_3_0 = arg_3_0.taskGroup[#arg_3_0.taskGroup]
	local var_3_1 = True

	for iter_3_0, iter_3_1 in ipairs(var_3_0):
		if arg_3_0.taskProxy.getTaskVO(iter_3_1).getTaskStatus() != 2:
			var_3_1 = False

	return var_3_1

return var_0_0
