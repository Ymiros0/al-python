ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleSkillSetCloak = class("BattleSkillSetCloak", var_0_0.Battle.BattleSkillEffect)
var_0_0.Battle.BattleSkillSetCloak.__name = "BattleSkillSetCloak"

local var_0_1 = var_0_0.Battle.BattleSkillSetCloak

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._rate = arg_1_0._tempData.arg_list.cloak_rate or 0
end

function var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0:doSetCloakValue(arg_2_2)
end

function var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1)
	arg_3_0:doSetCloakValue(arg_3_1)
end

function var_0_1.doSetCloakValue(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:GetCloak()

	if var_4_0 then
		var_4_0:ForceToRate(arg_4_0._rate)
	end
end
