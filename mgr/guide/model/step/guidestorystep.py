local var_0_0 = class("GuideStoryStep", import(".GuideStep"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.stories = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.stories):
		table.insert(arg_1_0.stories, iter_1_1)

def var_0_0.GetType(arg_2_0):
	return GuideStep.TYPE_STORY

def var_0_0.GetStories(arg_3_0):
	return arg_3_0.stories

return var_0_0
