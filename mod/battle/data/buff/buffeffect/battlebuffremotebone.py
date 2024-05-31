ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffRemoteBone", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffRemoteBone = var_0_1
var_0_1.__name = "BattleBuffRemoteBone"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._group = arg_2_2.GetID()
	arg_2_0._targetChoice = arg_2_0._tempData.arg_list.bone_target
	arg_2_0._bone = arg_2_0._tempData.arg_list.bone_name

def var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2):
	arg_3_1.SetRemoteBoundBone(arg_3_0._group, arg_3_0._bone, arg_3_0._targetChoice)

def var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2):
	arg_4_1.RemoveRemoteBoundBone(arg_4_0._group)
