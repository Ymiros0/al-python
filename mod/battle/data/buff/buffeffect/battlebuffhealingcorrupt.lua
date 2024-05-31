ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffHealingCorrupt = class("BattleBuffHealingCorrupt", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffHealingCorrupt.__name = "BattleBuffHealingCorrupt"

local var_0_1 = var_0_0.Battle.BattleBuffHealingCorrupt

var_0_1.FX_TYPE = var_0_0.Battle.BattleBuffEffect.FX_TYPE_LINK

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._corruptRate = var_2_0.corruptRate or 1
	arg_2_0._damageRate = var_2_0.damageRate or 1
end

function var_0_1.onTakeHealing(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	if arg_3_3.incorrupt then
		return
	end

	local var_3_0 = arg_3_3.damage
	local var_3_1 = math.ceil(var_3_0 * arg_3_0._corruptRate)

	arg_3_3.damage = var_3_0 - var_3_1

	local var_3_2 = math.ceil(var_3_1 * arg_3_0._damageRate) * -1
	local var_3_3 = {
		isMiss = false,
		isCri = false,
		isHeal = false,
		isShare = false
	}

	arg_3_1:UpdateHP(var_3_2, var_3_3)
end
