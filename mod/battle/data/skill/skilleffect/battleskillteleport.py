ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillTeleport", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillTeleport = var_0_1
var_0_1.__name = "BattleSkillTeleport"

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

def var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0.calcCorrdinate(arg_2_0._tempData.arg_list, arg_2_1, arg_2_2)

	arg_2_1.SetPosition(var_2_0)

def var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.calcCorrdinate(arg_3_0._tempData.arg_list, arg_3_1)

	arg_3_1.SetPosition(var_3_0)
