ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffHealingSteal = class("BattleBuffHealingSteal", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffHealingSteal.__name = "BattleBuffHealingSteal"

local var_0_1 = var_0_0.Battle.BattleBuffHealingSteal

var_0_1.FX_TYPE = var_0_0.Battle.BattleBuffEffect.FX_TYPE_LINK

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._stealRate = var_2_0.stealingRate or 1
	arg_2_0._absorbRate = var_2_0.arsorbRate or 1
end

function var_0_1.onTakeHealing(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	local var_3_0 = arg_3_3.damage
	local var_3_1 = arg_3_2:GetCaster()

	if var_3_1 and var_3_1:IsAlive() and var_3_1 ~= arg_3_1 then
		local var_3_2 = math.ceil(var_3_0 * arg_3_0._stealRate)

		arg_3_3.damage = var_3_0 - var_3_2

		local var_3_3 = var_3_1:GetAttrByName("healingRate")
		local var_3_4 = var_3_2 * arg_3_0._absorbRate
		local var_3_5 = math.ceil(var_3_3 * var_3_4)
		local var_3_6 = {
			isMiss = false,
			isCri = false,
			isHeal = true,
			isShare = false
		}

		var_3_1:UpdateHP(var_3_5, var_3_6)
	end
end
