local var_0_0 = class("NeihuadaSkinPage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnUpdateFlush(arg_1_0):
	var_0_0.super.OnUpdateFlush(arg_1_0)
	setText(arg_1_0.dayTF, setColorStr(arg_1_0.nday, "#edb46b") .. "/" .. #arg_1_0.taskGroup)

def var_0_0.GetProgressColor(arg_2_0):
	return "#edb46b"

return var_0_0
