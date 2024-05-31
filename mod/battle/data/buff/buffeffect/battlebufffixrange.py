ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffFixRange = class("BattleBuffFixRange", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffFixRange.__name = "BattleBuffFixRange"

local var_0_1 = var_0_0.Battle.BattleBuffFixRange

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._weaponRange = arg_2_0._tempData.arg_list.weaponRange
	arg_2_0._bulletRange = arg_2_0._tempData.arg_list.bulletRange
	arg_2_0._minRange = arg_2_0._tempData.arg_list.minRange
	arg_2_0._bulletRangeOffset = arg_2_0._tempData.arg_list.bulletRangeOffset

def var_0_1.onAttach(arg_3_0, arg_3_1):
	if arg_3_0._weaponRange or arg_3_0._bulletRange or arg_3_0._bulletRangeOffset:
		arg_3_0.updateBulletRange(arg_3_1, arg_3_0._weaponRange, arg_3_0._bulletRange, arg_3_0._minRange, arg_3_0._bulletRangeOffset)

def var_0_1.onRemove(arg_4_0, arg_4_1):
	arg_4_0.updateBulletRange(arg_4_1)

def var_0_1.updateBulletRange(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4, arg_5_5):
	local var_5_0 = arg_5_1.GetAllWeapon()

	for iter_5_0, iter_5_1 in ipairs(var_5_0):
		local var_5_1 = iter_5_1.GetEquipmentIndex()

		if arg_5_0._indexRequire == None or table.contains(arg_5_0._indexRequire, var_5_1):
			iter_5_1.FixWeaponRange(arg_5_2, arg_5_3, arg_5_4, arg_5_5)
