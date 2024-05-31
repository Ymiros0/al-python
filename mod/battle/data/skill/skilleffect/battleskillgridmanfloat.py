ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleSkillGridmanFloat = class("BattleSkillGridmanFloat", var_0_0.Battle.BattleSkillEffect)
var_0_0.Battle.BattleSkillGridmanFloat.__name = "BattleSkillGridmanFloat"

local var_0_1 = var_0_0.Battle.BattleSkillGridmanFloat

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._iconType = arg_1_0._tempData.arg_list.icon_type

def var_0_1.DoDataEffect(arg_2_0, arg_2_1):
	arg_2_0.doGridmanSkillFloat(arg_2_1)

def var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1):
	arg_3_0.doGridmanSkillFloat(arg_3_1)

def var_0_1.doGridmanSkillFloat(arg_4_0, arg_4_1):
	var_0_0.Battle.BattleDataProxy.GetInstance().DispatchGridmanSkill(arg_4_0._iconType, arg_4_1.GetIFF())
