local var_0_0 = class("SummaryAnimationPage", import(".SummaryPage"))

def var_0_0.OnInit(arg_1_0):
	assert(False, "must be overwrite")

def var_0_0.Show(arg_2_0, arg_2_1, arg_2_2):
	arg_2_2 = arg_2_2 or arg_2_0._tf

	setActive(arg_2_0._tf, True)

	arg_2_0.inAniming = True

	arg_2_2.GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_3_0)
		arg_2_0.inAniming = None

		if arg_2_1:
			arg_2_1())

def var_0_0.inAnim(arg_4_0):
	return arg_4_0.inAniming

return var_0_0
