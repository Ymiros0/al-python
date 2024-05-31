local var_0_0 = class("DebugPanel", import("..base.BaseUI"))

def var_0_0.Ctor(arg_1_0):
	var_0_0.super.Ctor(arg_1_0)
	arg_1_0.onUILoaded(DebugMgr.Inst.DebugPanel)
	setActive(arg_1_0._tf, False)

	arg_1_0.ctrls = arg_1_0.findTF("ctrls")
	arg_1_0._customBtnTpl = arg_1_0.getTpl("ctrls/custom_button")

def var_0_0.addCustomBtn(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = cloneTplTo(arg_2_0._customBtnTpl, arg_2_0.ctrls)

	arg_2_1 = string.gsub(arg_2_1, "(.)", "%1\n")

	setButtonText(var_2_0, arg_2_1)
	onButton(arg_2_0, var_2_0, arg_2_2)

def var_0_0.hidePanel(arg_3_0):
	triggerButton(arg_3_0.ctrls.Find("hide_button"))

return var_0_0
