local var_0_0 = class("Guide")

def var_0_0.Data2GuideStep(arg_1_0, arg_1_1):
	if arg_1_1.hideui:
		return GuideHideUIStep.New(arg_1_1)
	elif arg_1_1.stories:
		return GuideStoryStep.New(arg_1_1)
	elif arg_1_1.notifies:
		return GuideSendNotifiesStep.New(arg_1_1)
	elif arg_1_1.showSign:
		return GuideShowSignStep.New(arg_1_1)
	elif arg_1_1.doFunc:
		return GuideDoFunctionStep.New(arg_1_1)
	elif arg_1_1.ui:
		return GuideFindUIStep.New(arg_1_1)
	else
		return GuideDoNothingStep.New(arg_1_1)

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.steps = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.events):
		local var_2_0 = arg_2_0.Data2GuideStep(iter_2_1)

		if arg_2_1.isWorld != None:
			var_2_0.UpdateIsWorld(arg_2_1.isWorld)

		table.insert(arg_2_0.steps, var_2_0)

def var_0_0.GetStepsWithCode(arg_3_0, arg_3_1):
	local var_3_0 = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_0.steps):
		if not arg_3_1 or iter_3_1.IsMatchWithCode(arg_3_1):
			table.insert(var_3_0, iter_3_1)

	return var_3_0

return var_0_0
