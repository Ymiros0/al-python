local var_0_0 = class("DaofengPTPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnUpdateFlush(arg_1_0):
	var_0_0.super.OnUpdateFlush(arg_1_0)

	local var_1_0, var_1_1, var_1_2 = arg_1_0.ptData.GetResProgress()

	setText(arg_1_0.progress, setColorStr(var_1_0, "#915167") .. "/" .. var_1_1)

	local var_1_3 = Drop.New({
		type = DROP_TYPE_RESOURCE,
		id = arg_1_0.ptData.resId
	}).getIcon()

	LoadImageSpriteAsync(var_1_3, arg_1_0.findTF("AD/icon"), False)

return var_0_0
