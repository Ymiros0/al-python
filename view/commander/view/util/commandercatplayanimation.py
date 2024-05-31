local var_0_0 = class("CommanderCatPlayAnimation")
local var_0_1 = 0.3

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.expSlider = arg_1_1

def var_0_0.Action(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	if arg_2_2.level - arg_2_1.level > 0:
		arg_2_0.DoLevelOffsetAnimation(arg_2_1, arg_2_2, arg_2_3)
	else
		arg_2_0.DoSameLevelAnimation(arg_2_1, arg_2_2, arg_2_3)

def var_0_0.DoLevelOffsetAnimation(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	local var_3_0 = arg_3_2.level - arg_3_1.level
	local var_3_1 = {}

	table.insert(var_3_1, function(arg_4_0)
		local var_4_0 = arg_3_1.getNextLevelExp()

		TweenValue(go(arg_3_0.expSlider), arg_3_1.exp, var_4_0, var_0_1, 0, function(arg_5_0)
			arg_3_0.expSlider.value = arg_5_0, arg_4_0))

	for iter_3_0 = 1, var_3_0 - 1:
		table.insert(var_3_1, function(arg_6_0)
			TweenValue(go(arg_3_0.expSlider), 0, 1, var_0_1, 0, function(arg_7_0)
				arg_3_0.expSlider.value = arg_7_0, arg_6_0))

	table.insert(var_3_1, function(arg_8_0)
		local var_8_0 = arg_3_2.getNextLevelExp()

		TweenValue(go(arg_3_0.expSlider), 0, arg_3_2.exp, var_0_1, 0, function(arg_9_0)
			arg_3_0.expSlider.value = arg_9_0 / var_8_0, arg_8_0))
	seriesAsync(var_3_1, arg_3_3)

def var_0_0.DoSameLevelAnimation(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	local var_10_0 = arg_10_1.getNextLevelExp()

	TweenValue(go(arg_10_0.expSlider), arg_10_1.exp, arg_10_2.exp, var_0_1, 0, function(arg_11_0)
		arg_10_0.expSlider.value = arg_11_0 / var_10_0, arg_10_3)

def var_0_0.Dispose(arg_12_0):
	if LeanTween.isTweening(arg_12_0.expSlider.gameObject):
		LeanTween.cancel(arg_12_0.expSlider.gameObject)

return var_0_0
