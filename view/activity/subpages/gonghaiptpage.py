local var_0_0 = class("GongHaiPtPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)
	setText(arg_1_0.findTF("title", arg_1_0.bg), i18n("pt_count_tip"))

return var_0_0
