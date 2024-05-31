ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleSkillDamage = class("BattleSkillDamage", var_0_0.Battle.BattleSkillEffect)
var_0_0.Battle.BattleSkillDamage.__name = "BattleSkillDamage"

def var_0_0.Battle.BattleSkillDamage.Ctor(arg_1_0, arg_1_1):
	var_0_0.Battle.BattleSkillDamage.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._number = arg_1_0._tempData.arg_list.number or 0
	arg_1_0._rate = arg_1_0._tempData.arg_list.rate or 0

def var_0_0.Battle.BattleSkillDamage.DoDataEffect(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = {
		isMiss = False,
		isCri = False,
		isHeal = False
	}
	local var_2_1, var_2_2 = arg_2_2.GetHP()
	local var_2_3 = math.floor(var_2_2 * arg_2_0._rate) + arg_2_0._number
	local var_2_4 = arg_2_2.UpdateHP(-var_2_3, var_2_0)

	var_0_0.Battle.BattleDataProxy.GetInstance().DamageStatistics(arg_2_1.GetAttrByName("id"), arg_2_2.GetAttrByName("id"), -var_2_4)

	if not arg_2_2.IsAlive():
		var_0_0.Battle.BattleAttr.Spirit(arg_2_2)
		var_0_0.Battle.BattleAttr.AppendInvincible(arg_2_2)
