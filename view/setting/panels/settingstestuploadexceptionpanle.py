local var_0_0 = class("SettingsTestUploadExceptionPanle", import(".SettingsBasePanel"))

def var_0_0.GetUIName(arg_1_0):
	return "SettingsServiceCH"

def var_0_0.GetTitle(arg_2_0):
	return "测试异常上传"

def var_0_0.GetTitleEn(arg_3_0):
	return "/ Service"

def var_0_0.OnInit(arg_4_0):
	arg_4_0.serviceBtn = findTF(arg_4_0._tf, "delete")

	onButton(arg_4_0, arg_4_0.serviceBtn, function()
		local var_5_0 = ___inexistence____[0], SFX_PANEL)

def var_0_0.OnUpdate(arg_6_0):
	return

return var_0_0
