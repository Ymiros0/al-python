local var_0_0 = class("JapanV3PtPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnUpdateFlush(arg_1_0):
	var_0_0.super.OnUpdateFlush(arg_1_0)

	local var_1_0, var_1_1, var_1_2 = arg_1_0.ptData.GetResProgress()

	setText(arg_1_0.progress, setColorStr(var_1_0, "#1a97cb") .. "/" .. var_1_1)

return var_0_0
