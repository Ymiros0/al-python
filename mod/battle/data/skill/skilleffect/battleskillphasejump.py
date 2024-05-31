ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillPhaseJump", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillPhaseJump = var_0_1
var_0_1.__name = "BattleSkillPhaseJump"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._phaseIndex = arg_1_0._tempData.arg_list.index or 0

def var_0_1.DoDataEffect(arg_2_0, arg_2_1):
	arg_2_0.doJump(arg_2_1)

def var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1):
	arg_3_0.doJump(arg_3_1)

def var_0_1.doJump(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.GetPhaseSwitcher()

	if var_4_0:
		var_4_0.ForceSwitch(arg_4_0._phaseIndex)
