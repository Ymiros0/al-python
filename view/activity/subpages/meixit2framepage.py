local var_0_0 = class("MeixiT2FramePage", import(".TemplatePage.NewFrameTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	for iter_1_0, iter_1_1 in ipairs(arg_1_0.phases):
		setActive(iter_1_1, True)

		GetOrAddComponent(iter_1_1, typeof(CanvasGroup)).alpha = 0

	var_0_0.super.OnFirstFlush(arg_1_0)

def var_0_0.Switch(arg_2_0, arg_2_1):
	arg_2_0.isSwitching = True

	setToggleEnabled(arg_2_0.switchBtn, False)

	local var_2_0
	local var_2_1

	if arg_2_1:
		var_2_0, var_2_1 = arg_2_0.phases[1], arg_2_0.phases[2]
	else
		var_2_0, var_2_1 = arg_2_0.phases[2], arg_2_0.phases[1]

	local var_2_2 = var_2_0.localPosition
	local var_2_3 = var_2_1.localPosition

	var_2_1.SetAsLastSibling()

	local var_2_4 = {}

	table.insert(var_2_4, function(arg_3_0)
		LeanTween.moveLocal(go(var_2_0), var_2_3, 0.4)
		LeanTween.alphaCanvas(GetOrAddComponent(var_2_0, typeof(CanvasGroup)), 0, 0.4)
		LeanTween.moveLocal(go(var_2_1), var_2_2, 0.4)
		LeanTween.alphaCanvas(GetOrAddComponent(var_2_1, typeof(CanvasGroup)), 1, 0.4).setOnComplete(System.Action(arg_3_0)))
	seriesAsync(var_2_4, function()
		arg_2_0.isSwitching = None

		setToggleEnabled(arg_2_0.switchBtn, True))

return var_0_0
