ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillRemoveAllWeapon", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillRemoveAllWeapon = var_0_1
var_0_1.__name = "BattleSkillRemoveAllWeapon"

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1, lv)
end

function var_0_1.DoDataEffect(arg_2_0, arg_2_1)
	arg_2_0:doRemove(arg_2_1)
end

function var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1)
	arg_3_0:doRemove(arg_3_1)
end

function var_0_1.doRemove(arg_4_0, arg_4_1)
	arg_4_1:RemoveAllAutoWeapon()
end
