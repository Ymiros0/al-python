ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillManualWeaponReloadBoost", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillManualWeaponReloadBoost = var_0_1
var_0_1.__name = "BattleSkillManualWeaponReloadBoost"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._weaponType = arg_1_0._tempData.arg_list.weaponType
	arg_1_0._boostValue = arg_1_0._tempData.arg_list.value
	arg_1_0._boostRate = arg_1_0._tempData.arg_list.rate

def var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0.getWeaponQueueByType(arg_2_1, arg_2_0._weaponType)

	if var_2_0:
		local var_2_1 = var_2_0.GetCoolDownList()

		if arg_2_0._boostValue:
			local var_2_2 = arg_2_0._boostValue * -1

			for iter_2_0, iter_2_1 in ipairs(var_2_1):
				iter_2_1.AppendReloadBoost(var_2_2)
		elif arg_2_0._boostRate:
			for iter_2_2, iter_2_3 in ipairs(var_2_1):
				boostValue = iter_2_3.GetReloadTimeByRate(arg_2_0._boostRate) * -1

				iter_2_3.AppendReloadBoost(boostValue)

def var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1):
	arg_3_0.DoDataEffect(arg_3_1, None)

def var_0_1.getWeaponQueueByType(arg_4_0, arg_4_1):
	local var_4_0

	if arg_4_1 == "ChargeWeapon":
		var_4_0 = arg_4_0.GetChargeQueue()
	elif arg_4_1 == "TorpedoWeapon":
		var_4_0 = arg_4_0.GetTorpedoQueue()
	elif arg_4_1 == "AirAssist":
		var_4_0 = arg_4_0.GetAirAssistQueue()

	return var_4_0
