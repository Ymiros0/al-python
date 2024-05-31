local var_0_0 = class("ChapterStoryItem", import("model.vo.BaseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.story_template

def var_0_0.GetStoryName(arg_2_0):
	return arg_2_0.getConfig("story")

def var_0_0.GetName(arg_3_0):
	return arg_3_0.getConfig("name")

def var_0_0.GetIcon(arg_4_0):
	local var_4_0 = arg_4_0.getConfig("icon")

	return "StoryPointIcon/" .. var_4_0, var_4_0

def var_0_0.GetPosition(arg_5_0):
	return arg_5_0.getConfig("pos")

def var_0_0.IsClear(arg_6_0):
	return pg.NewStoryMgr.GetInstance().IsPlayed(arg_6_0.GetStoryName())

return var_0_0
