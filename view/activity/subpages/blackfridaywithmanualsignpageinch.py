local var_0_0 = class("BlackFridayWithManualSignPageInCH", import(".BlackFridayWithManualSignPage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)
	setText(arg_1_0._tf.Find("AD/signMask/Image/Text"), i18n("challenge_end_tip"))

def var_0_0.FlushSignBtn(arg_2_0):
	var_0_0.super.FlushSignBtn(arg_2_0)

	local var_2_0 = getProxy(ActivityProxy).getActivityById(arg_2_0.signInActId)
	local var_2_1 = not var_2_0 or var_2_0.isEnd()

	setActive(arg_2_0._tf.Find("AD/signMask"), var_2_1)

return var_0_0
