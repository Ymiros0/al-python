ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleAttr
local var_0_3 = class("BattleBuffAddReloadRequirement", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffAddReloadRequirement = var_0_3
var_0_3.__name = "BattleBuffAddReloadRequirement"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_3.super.Ctor(arg_1_0, arg_1_1)

def var_0_3.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._weaponIndex = arg_2_0._tempData.arg_list.index
	arg_2_0._weaponType = arg_2_0._tempData.arg_list.type
	arg_2_0._value = arg_2_0._tempData.arg_list.number or 0
	arg_2_0._convertAttr = arg_2_0._tempData.arg_list.convert_attr
	arg_2_0._convertValue = arg_2_0._tempData.arg_list.convert_value

def var_0_3.onAttach(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = {}

	if arg_3_0._weaponType:
		local var_3_1

		if arg_3_0._weaponType == var_0_1.EquipmentType.POINT_HIT_AND_LOCK:
			var_3_1 = arg_3_1.GetChargeList()
		elif arg_3_0._weaponType == var_0_1.EquipmentType.MANUAL_TORPEDO:
			var_3_1 = arg_3_1.GetTorpedoList()
		elif arg_3_0._weaponType == var_0_1.EquipmentType.INTERCEPT_AIRCRAFT or arg_3_0._weaponType == var_0_1.EquipmentType.STRIKE_AIRCRAFT:
			var_3_1 = arg_3_1.GetHiveList()
		elif arg_3_0._weaponType == var_0_1.EquipmentType.AIR_ASSIST:
			var_3_1 = arg_3_1.GetAirAssistList()
		else
			var_3_1 = arg_3_1.GetAutoWeapons()

		if var_3_1:
			for iter_3_0, iter_3_1 in ipairs(var_3_1):
				var_3_0[#var_3_0 + 1] = iter_3_1
	elif arg_3_0._weaponIndex:
		local var_3_2 = arg_3_1.GetTotalWeapon()

		for iter_3_2, iter_3_3 in ipairs(var_3_2):
			if iter_3_3.GetEquipmentIndex() == arg_3_0._weaponIndex:
				var_3_0[#var_3_0 + 1] = iter_3_3
	else
		assert(False, "BattleBuffAddReloadRequirement：缺少指定类型或索引")

	for iter_3_4, iter_3_5 in ipairs(var_3_0):
		iter_3_5.AppendReloadFactor(arg_3_2, arg_3_0.calcFactor(arg_3_2.GetCaster()))

		local var_3_3 = iter_3_5.GetReloadFactorList()
		local var_3_4 = 1

		for iter_3_6, iter_3_7 in pairs(var_3_3):
			var_3_4 = var_3_4 + iter_3_7

		iter_3_5.FlushReloadMax(var_3_4)

	arg_3_0._targetWeaponList = var_3_0

def var_0_3.onRemove(arg_4_0, arg_4_1, arg_4_2):
	for iter_4_0, iter_4_1 in ipairs(arg_4_0._targetWeaponList):
		iter_4_1.RemoveReloadFactor(arg_4_2)

		local var_4_0 = iter_4_1.GetReloadFactorList()
		local var_4_1 = 1

		for iter_4_2, iter_4_3 in pairs(var_4_0):
			var_4_1 = var_4_1 + iter_4_3

		iter_4_1.FlushReloadMax(var_4_1)

def var_0_3.calcFactor(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0._value
	local var_5_1 = 0

	if arg_5_0._convertAttr == None:
		-- block empty
	elif arg_5_0._convertAttr == "HPRate" or arg_5_0._convertAttr == "DMGRate":
		var_5_1 = var_0_2.GetCurrent(arg_5_1, arg_5_0._convertAttr) * arg_5_0._convertValue
	else
		var_5_1 = var_0_2.GetBase(arg_5_1, arg_5_0._convertAttr) * arg_5_0._convertValue

	return var_5_0 + var_5_1
