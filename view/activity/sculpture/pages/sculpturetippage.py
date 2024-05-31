local var_0_0 = class("SculptureTipPage", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "SculptureTipUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.tip = arg_2_0.findTF("tip")

def var_0_0.OnInit(arg_3_0):
	return

def var_0_0.Show(arg_4_0):
	var_0_0.super.Show(arg_4_0)
	setActive(arg_4_0.tip, True)
	onDelayTick(function()
		arg_4_0.Hide(), 2)

def var_0_0.Hide(arg_6_0):
	var_0_0.super.Hide(arg_6_0)
	setActive(arg_6_0.tip, False)

def var_0_0.OnDestroy(arg_7_0):
	return

return var_0_0
