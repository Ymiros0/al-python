local var_0_0 = class("AccountDeletePanel", import(".MsgboxSubPanel"))

var_0_0.ConfigData = {}

def var_0_0.getUIName(arg_1_0):
	return "AccountDeleteBox"

def var_0_0.UpdateView(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_1.onYes

	print("onYesFunc", tostring(var_2_0))

	if var_2_0:
		function arg_2_1.onYes()
			local var_3_0 = getInputText(arg_2_0.inputField)

			var_2_0(var_3_0)

	arg_2_0.PreRefresh(arg_2_1)

	rtf(arg_2_0.viewParent._window).sizeDelta = Vector2.New(1000, 638)
	arg_2_0.inputField = arg_2_0.findTF("InputField", arg_2_0._tf)

	local var_2_1 = arg_2_0.findTF("Title", arg_2_0._tf)
	local var_2_2 = arg_2_0.findTF("InputField/Placeholder", arg_2_0._tf)
	local var_2_3 = i18n("box_account_del_target")
	local var_2_4 = i18n("box_account_del_input", var_2_3)

	setText(var_2_1, var_2_4)
	setText(var_2_2, i18n("box_account_del_click"))
	arg_2_0.PostRefresh(arg_2_1)

return var_0_0
