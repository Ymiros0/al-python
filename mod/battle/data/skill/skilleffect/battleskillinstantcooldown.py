ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillInstantCoolDown", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillInstantCoolDown = var_0_1
var_0_1.__name = "BattleSkillInstantCoolDown"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._weaponType = arg_1_0._tempData.arg_list.weaponType

def var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0._GetWeapon(arg_2_1)

	if var_2_0:
		var_2_0.QuickCoolDown()

def var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1):
	arg_3_0.DoDataEffect(arg_3_1, None)

def var_0_1._GetWeapon(arg_4_0, arg_4_1):
	local var_4_0

	if arg_4_0._weaponType == "AirAssist":
		var_4_0 = arg_4_1.GetAirAssistQueue().GetQueueHead()

	return var_4_0
