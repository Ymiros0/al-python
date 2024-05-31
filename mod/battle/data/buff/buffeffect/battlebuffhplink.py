ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffHPLink = class("BattleBuffHPLink", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffHPLink.__name = "BattleBuffHPLink"

local var_0_1 = var_0_0.Battle.BattleBuffHPLink

var_0_1.FX_TYPE = var_0_0.Battle.BattleBuffEffect.FX_TYPE_LINK

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._number = var_2_0.number or 0
	arg_2_0._absorbRate = var_2_0.absorb or 0
	arg_2_0._restoreRate = 0
	arg_2_0._sumDMG = 0

	if var_2_0.restoreRatio:
		arg_2_0._restoreRate = var_2_0.restoreRatio * 0.0001

def var_0_1.onTakeDamage(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if arg_3_3.isShare:
		return

	local var_3_0 = arg_3_3.damage
	local var_3_1 = arg_3_2.GetCaster()

	if var_3_1 and var_3_1.IsAlive() and var_3_1 != arg_3_1:
		arg_3_3.damage = math.ceil(var_3_0 * arg_3_0._number)

		local var_3_2 = math.ceil((var_3_0 - arg_3_3.damage) * (1 - arg_3_0._absorbRate))

		if var_3_2 > 0:
			arg_3_0._sumDMG = arg_3_0._sumDMG + var_3_2

			local var_3_3 = {
				isMiss = False,
				isCri = False,
				isHeal = False,
				isShare = True
			}

			var_3_1.UpdateHP(-var_3_2, var_3_3)

			if arg_3_3.damageSrc:
				local var_3_4 = arg_3_3.damageSrc

				var_0_0.Battle.BattleDataProxy.GetInstance().DamageStatistics(var_3_4, arg_3_1.GetAttrByName("id"), -var_3_2)
				var_0_0.Battle.BattleDataProxy.GetInstance().DamageStatistics(var_3_4, var_3_1.GetAttrByName("id"), var_3_2)

def var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_2.GetCaster()

	if var_4_0 and var_4_0.IsAlive() and arg_4_0._restoreRate > 0 and var_4_0 != arg_4_1:
		local var_4_1 = var_4_0.GetAttrByName("healingRate")
		local var_4_2 = math.floor(arg_4_0._sumDMG * arg_4_0._restoreRate * var_4_1)

		if var_4_2 != 0:
			local var_4_3 = {
				isMiss = False,
				isCri = False,
				isHeal = True
			}

			var_4_0.UpdateHP(var_4_2, var_4_3)
