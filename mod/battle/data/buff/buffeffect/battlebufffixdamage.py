ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffFixDamage = class("BattleBuffFixDamage", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffFixDamage.__name = "BattleBuffFixDamage"

local var_0_1 = var_0_0.Battle.BattleBuffFixDamage

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._fixProb = arg_2_0._tempData.arg_list.rant or 10000
	arg_2_0._fixValue = arg_2_0._tempData.arg_list.value
	arg_2_0._fixRate = arg_2_0._tempData.arg_list.rate

def var_0_1.onBeforeTakeDamage(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if not arg_3_0.damageCheck(arg_3_3):
		return

	local var_3_0 = arg_3_3.damage
	local var_3_1 = arg_3_3.damage

	if (arg_3_0._fixProb >= 10000 or var_0_0.Battle.BattleFormulas.IsHappen(arg_3_0._fixProb)) and (arg_3_0._fixValue or arg_3_0._fixRate):
		if arg_3_0._fixRate:
			var_3_1 = math.max(1, var_3_0 * arg_3_0._fixRate)
			arg_3_3.fixFlag = True
		elif var_3_0 > arg_3_0._fixValue:
			var_3_1 = arg_3_0._fixValue
			arg_3_3.fixFlag = True

	local var_3_2 = arg_3_0._tempData.arg_list
	local var_3_3
	local var_3_4, var_3_5 = arg_3_1.GetHP()

	if var_3_2.cap_value:
		var_3_3 = var_3_2.cap_value
	elif var_3_2.cap_hp_rate:
		var_3_3 = math.floor(var_3_4 * var_3_2.cap_hp_rate)
	elif var_3_2.cap_hp_rate_max:
		var_3_3 = math.floor(var_3_5 * var_3_2.cap_hp_rate_max)

	if var_3_3:
		if var_3_2.cap_ceiling:
			var_3_3 = math.max(var_3_3, var_3_2.cap_ceiling)
		elif var_3_2.cap_ceiling_rate:
			var_3_3 = math.max(var_3_3, math.floor(var_3_2.cap_ceiling_rate * var_3_5))

		if var_3_3 < var_3_1:
			arg_3_3.capFlag = True
			var_3_1 = var_3_3

	arg_3_3.damage = var_3_1
