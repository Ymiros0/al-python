ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffHP", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffHP = var_0_1
var_0_1.__name = "BattleBuffHP"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._number = arg_2_0._tempData.arg_list.number or 0
	arg_2_0._numberBase = arg_2_0._number
	arg_2_0._currentHPRatio = 0

	if arg_2_0._tempData.arg_list.currentHPRatio:
		arg_2_0._currentHPRatio = arg_2_0._tempData.arg_list.currentHPRatio * 0.0001

	local var_2_0, var_2_1 = arg_2_1.GetHP()
	local var_2_2, var_2_3 = arg_2_0._caster.GetHP()

	arg_2_0._maxHPRatio = arg_2_0._tempData.arg_list.maxHPRatio or 0
	arg_2_0._maxHPNumber = var_2_1 * arg_2_0._maxHPRatio
	arg_2_0._castMaxHPRatio = arg_2_0._tempData.arg_list.casterMaxHPRatio or 0
	arg_2_0._castMaxHPNumber = arg_2_0._castMaxHPRatio * var_2_3
	arg_2_0._weaponType = arg_2_0._tempData.arg_list.weaponType
	arg_2_0._damageConvert = 0

	if arg_2_0._tempData.arg_list.damageConvertRatio:
		arg_2_0._damageConvert = arg_2_0._tempData.arg_list.damageConvertRatio * 0.0001

	arg_2_0._incorruptible = arg_2_0._tempData.arg_list.incorrupt

def var_0_1.onBulletHit(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if not arg_3_0.equipIndexRequire(arg_3_3.equipIndex):
		return

	if not arg_3_0.bulletTagRequire(arg_3_3.bulletTag):
		return

	if not arg_3_0.victimRequire(arg_3_3.target, arg_3_1):
		return

	local var_3_0 = arg_3_1.GetAttrByName("healingRate")
	local var_3_1 = arg_3_3.target

	if not arg_3_0._weaponType:
		local var_3_2 = arg_3_0._number
		local var_3_3 = var_3_2 > 0

		if var_3_3:
			var_3_2 = math.floor(var_3_2 * var_3_0)

		local var_3_4 = {
			isMiss = False,
			isCri = False,
			isHeal = var_3_3
		}

		var_3_1.UpdateHP(var_3_2, var_3_4)
	elif arg_3_3.weaponType == arg_3_0._weaponType:
		local var_3_5 = math.floor(arg_3_3.damage * arg_3_0._damageConvert * var_3_0)
		local var_3_6 = {
			isMiss = False,
			isCri = False,
			isHeal = True,
			incorrupt = arg_3_0._incorruptible
		}

		arg_3_1.UpdateHP(var_3_5, var_3_6)

def var_0_1.onAttach(arg_4_0, arg_4_1, arg_4_2):
	onDelayTick(function()
		var_0_1.super.onAttach(arg_4_0, arg_4_1, arg_4_2), 0.03)

def var_0_1.onTrigger(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = arg_6_0.CalcNumber(arg_6_1)
	local var_6_1 = var_6_0 > 0

	if var_6_1:
		local var_6_2 = arg_6_1.GetAttrByName("healingRate")

		var_6_0 = math.floor(var_6_0 * var_6_2)

	local var_6_3 = {
		isMiss = False,
		isCri = False,
		isHeal = var_6_1,
		incorrupt = arg_6_0._incorruptible
	}

	arg_6_1.UpdateHP(var_6_0, var_6_3)

def var_0_1.CalcNumber(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.GetHP()
	local var_7_1 = arg_7_0._caster.GetAttrByName("healingEnhancement") + 1

	return math.floor((var_7_0 * arg_7_0._currentHPRatio + arg_7_0._maxHPNumber + arg_7_0._number + arg_7_0._castMaxHPNumber) * var_7_1)
