ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleEnvironmentBehaviourDamage", var_0_0.Battle.BattleEnvironmentBehaviour)

var_0_0.Battle.BattleEnvironmentBehaviourDamage = var_0_3
var_0_3.__name = "BattleEnvironmentBehaviourDamage"

function var_0_3.Ctor(arg_1_0)
	var_0_3.super.Ctor(arg_1_0)
end

function var_0_3.SetTemplate(arg_2_0, arg_2_1)
	var_0_3.super.SetTemplate(arg_2_0, arg_2_1)

	arg_2_0._rate = arg_2_0._tmpData.hp_rate or 0
	arg_2_0._damage = arg_2_0._tmpData.damage or 0
	arg_2_0._offset = arg_2_0._tmpData.offset or 0
end

function var_0_3.doBehaviour(arg_3_0)
	for iter_3_0, iter_3_1 in ipairs(arg_3_0._cldUnitList) do
		local var_3_0 = {
			isMiss = false,
			isCri = false,
			isHeal = false
		}
		local var_3_1, var_3_2 = iter_3_1:GetHP()
		local var_3_3 = math.max(0, math.floor(var_3_2 * arg_3_0._rate) + arg_3_0._damage + math.random(-arg_3_0._offset, arg_3_0._offset))

		iter_3_1:UpdateHP(-var_3_3, var_3_0)

		if not iter_3_1:IsAlive() then
			var_0_0.Battle.BattleAttr.Spirit(iter_3_1)
			var_0_0.Battle.BattleAttr.AppendInvincible(iter_3_1)
		end
	end

	var_0_3.super.doBehaviour(arg_3_0)
end
