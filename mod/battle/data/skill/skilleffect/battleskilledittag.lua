ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillEditTag", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillEditTag = var_0_1
var_0_1.__name = "BattleSkillEditTag"
var_0_1.TAG_OPERATION_APPEND = 1
var_0_1.TAG_OPERATION_REMOVE = -1

function var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._tag = arg_1_0._tempData.arg_list.tag
	arg_1_0._op = arg_1_0._tempData.arg_list.operation
end

function var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2)
	if arg_2_0._op == var_0_1.TAG_OPERATION_APPEND then
		arg_2_2:AddLabelTag(arg_2_0._tag)
	elseif arg_2_0._op == var_0_1.TAG_OPERATION_REMOVE then
		arg_2_2:RemoveLabelTag(arg_2_0._tag)
	end
end
