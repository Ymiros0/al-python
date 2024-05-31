local var_0_0 = class("ZProjectPage", import(".TemplatePage.PreviewTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.awardTF = arg_1_0.findTF("AD/award")

def var_0_0.OnFirstFlush(arg_2_0):
	var_0_0.super.OnFirstFlush(arg_2_0)

	local var_2_0 = arg_2_0.activity.getConfig("config_client").drop

	updateDrop(arg_2_0.awardTF, var_2_0)
	onButton(arg_2_0, arg_2_0.awardTF, function()
		arg_2_0.emit(BaseUI.ON_DROP, var_2_0), SFX_PANEL)

return var_0_0
