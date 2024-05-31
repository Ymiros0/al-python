ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffAddTag", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffAddTag = var_0_1
var_0_1.__name = "BattleBuffAddTag"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._labelTag = arg_2_0._tempData.arg_list.tag

def var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2):
	arg_3_1.AddLabelTag(arg_3_0._labelTag)

def var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2):
	arg_4_1.RemoveLabelTag(arg_4_0._labelTag)
