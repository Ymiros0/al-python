ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffStory = class("BattleBuffStory", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffStory.__name = "BattleBuffStory"

local var_0_1 = var_0_0.Battle.BattleBuffStory

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._storyID = var_2_0.story_id
	arg_2_0._countType = var_2_0.countType
end

function var_0_1.doOnHPRatioUpdate(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	pg.NewStoryMgr.GetInstance():Play(arg_3_0._storyID)
end
