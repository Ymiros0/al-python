local var_0_0 = class("DexiV4FramePage", import(".TemplatePage.FrameTemplatePage"))

def var_0_0.Switch(arg_1_0, arg_1_1):
	arg_1_0.isSwitching = True

	local var_1_0 = GetOrAddComponent(arg_1_0.phases[1], typeof(CanvasGroup))
	local var_1_1 = arg_1_0.phases[1].localPosition
	local var_1_2 = arg_1_0.phases[2].localPosition

	arg_1_0.phases[2].SetAsLastSibling()
	setActive(arg_1_0.phases[1].Find("Image"), False)
	setLocalPosition(go(arg_1_0.phases[1]), var_1_2)
	setActive(arg_1_0.phases[1].Find("label"), True)
	LeanTween.value(go(arg_1_0.phases[1]), 0, 1, 0.4).setOnUpdate(System.Action_float(function(arg_2_0)
		var_1_0.alpha = arg_2_0))
	setActive(arg_1_0.phases[2].Find("Image"), True)

	local var_1_3 = GetOrAddComponent(arg_1_0.phases[2], typeof(CanvasGroup))

	LeanTween.value(go(arg_1_0.phases[2]), 0, 1, 0.4).setOnUpdate(System.Action_float(function(arg_3_0)
		var_1_3.alpha = arg_3_0))
	setActive(arg_1_0.phases[2].Find("label"), False)
	setLocalPosition(go(arg_1_0.phases[2]), var_1_1)

	arg_1_0.isSwitching = None
	arg_1_0.phases[1], arg_1_0.phases[2] = arg_1_0.phases[2], arg_1_0.phases[1]

	arg_1_0.UpdateAwardGot()

return var_0_0
