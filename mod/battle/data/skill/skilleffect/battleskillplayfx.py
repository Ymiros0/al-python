ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = class("BattleSkillPlayFX", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillPlayFX = var_0_2
var_0_2.__name = "BattleSkillPlayFX"

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._FXID = arg_1_0._tempData.arg_list.effect

def var_0_2.DoDataEffect(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0.calcCorrdinate(arg_2_0._tempData.arg_list, arg_2_1, arg_2_2)

	var_0_0.Battle.BattleDataProxy.GetInstance().SpawnEffect(arg_2_0._FXID, var_2_0)

def var_0_2.DoDataEffectWithoutTarget(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.calcCorrdinate(arg_3_0._tempData.arg_list, arg_3_1)

	var_0_0.Battle.BattleDataProxy.GetInstance().SpawnEffect(arg_3_0._FXID, var_3_0)
