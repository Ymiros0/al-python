ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleSkillHeal = class("BattleSkillHeal", var_0_0.Battle.BattleSkillEffect)
var_0_0.Battle.BattleSkillHeal.__name = "BattleSkillHeal"

function var_0_0.Battle.BattleSkillHeal.Ctor(arg_1_0, arg_1_1)
	var_0_0.Battle.BattleSkillHeal.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._number = arg_1_0._tempData.arg_list.number or 0
	arg_1_0._maxHPRatio = arg_1_0._tempData.arg_list.maxHPRatio or 0
	arg_1_0._incorruptible = arg_1_0._tempData.arg_list.incorrupt
end

function var_0_0.Battle.BattleSkillHeal.DoDataEffect(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_1:GetAttrByName("healingEnhancement") + 1
	local var_2_1 = var_0_0.Battle.BattleFormulas.HealFixer(var_0_0.Battle.BattleDataProxy.GetInstance():GetInitData().battleType, arg_2_2:GetAttr())
	local var_2_2 = math.floor(arg_2_0._number * var_2_1)
	local var_2_3 = arg_2_1:GetAttrByName("healingRate")
	local var_2_4 = math.max(0, math.floor((arg_2_2:GetMaxHP() * arg_2_0._maxHPRatio + var_2_2) * var_2_0 * var_2_3))
	local var_2_5 = {
		isMiss = false,
		isCri = false,
		isHeal = true,
		incorrupt = arg_2_0._incorruptible
	}

	arg_2_2:UpdateHP(var_2_4, var_2_5)
end
