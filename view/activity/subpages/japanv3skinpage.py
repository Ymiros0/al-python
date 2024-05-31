local var_0_0 = class("JapanV3SkinPage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnUpdateFlush(arg_1_0):
	var_0_0.super.OnUpdateFlush(arg_1_0)
	setText(arg_1_0.dayTF, setColorStr(arg_1_0.nday, "#f7ecd9") .. "/" .. #arg_1_0.taskGroup)
	GetImageSpriteFromAtlasAsync("ui/activityuipage/japanv3skinpage_atlas", "bj_" .. arg_1_0.nday, arg_1_0.findTF("painting", arg_1_0.bg))

def var_0_0.GetProgressColor(arg_2_0):
	return "#b37a4a"

return var_0_0
