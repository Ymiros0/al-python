ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleEvent
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleSkillOverrideAutoPilot", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillOverrideAutoPilot = var_0_3
var_0_3.__name = "BattleSkillOverrideAutoPilot"

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_3.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._AIID = arg_1_0._tempData.arg_list.ai_id

def var_0_3.DoDataEffect(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_1.GetFleetVO()

	if not var_2_0:
		return

	var_2_0.OverrideJoyStickAutoBot(arg_2_0._AIID)

def var_0_3.DataEffectWithoutTarget(arg_3_0, arg_3_1):
	arg_3_0.DoDataEffect(arg_3_1)
