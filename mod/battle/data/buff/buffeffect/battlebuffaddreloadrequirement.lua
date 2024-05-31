ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleAttr
local var_0_3 = class("BattleBuffAddReloadRequirement", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffAddReloadRequirement = var_0_3
var_0_3.__name = "BattleBuffAddReloadRequirement"

function var_0_3.Ctor(arg_1_0, arg_1_1)
	var_0_3.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_3.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._weaponIndex = arg_2_0._tempData.arg_list.index
	arg_2_0._weaponType = arg_2_0._tempData.arg_list.type
	arg_2_0._value = arg_2_0._tempData.arg_list.number or 0
	arg_2_0._convertAttr = arg_2_0._tempData.arg_list.convert_attr
	arg_2_0._convertValue = arg_2_0._tempData.arg_list.convert_value
end

function var_0_3.onAttach(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = {}

	if arg_3_0._weaponType then
		local var_3_1

		if arg_3_0._weaponType == var_0_1.EquipmentType.POINT_HIT_AND_LOCK then
			var_3_1 = arg_3_1:GetChargeList()
		elseif arg_3_0._weaponType == var_0_1.EquipmentType.MANUAL_TORPEDO then
			var_3_1 = arg_3_1:GetTorpedoList()
		elseif arg_3_0._weaponType == var_0_1.EquipmentType.INTERCEPT_AIRCRAFT or arg_3_0._weaponType == var_0_1.EquipmentType.STRIKE_AIRCRAFT then
			var_3_1 = arg_3_1:GetHiveList()
		elseif arg_3_0._weaponType == var_0_1.EquipmentType.AIR_ASSIST then
			var_3_1 = arg_3_1:GetAirAssistList()
		else
			var_3_1 = arg_3_1:GetAutoWeapons()
		end

		if var_3_1 then
			for iter_3_0, iter_3_1 in ipairs(var_3_1) do
				var_3_0[#var_3_0 + 1] = iter_3_1
			end
		end
	elseif arg_3_0._weaponIndex then
		local var_3_2 = arg_3_1:GetTotalWeapon()

		for iter_3_2, iter_3_3 in ipairs(var_3_2) do
			if iter_3_3:GetEquipmentIndex() == arg_3_0._weaponIndex then
				var_3_0[#var_3_0 + 1] = iter_3_3
			end
		end
	else
		assert(false, "BattleBuffAddReloadRequirement：缺少指定类型或索引")
	end

	for iter_3_4, iter_3_5 in ipairs(var_3_0) do
		iter_3_5:AppendReloadFactor(arg_3_2, arg_3_0:calcFactor(arg_3_2:GetCaster()))

		local var_3_3 = iter_3_5:GetReloadFactorList()
		local var_3_4 = 1

		for iter_3_6, iter_3_7 in pairs(var_3_3) do
			var_3_4 = var_3_4 + iter_3_7
		end

		iter_3_5:FlushReloadMax(var_3_4)
	end

	arg_3_0._targetWeaponList = var_3_0
end

function var_0_3.onRemove(arg_4_0, arg_4_1, arg_4_2)
	for iter_4_0, iter_4_1 in ipairs(arg_4_0._targetWeaponList) do
		iter_4_1:RemoveReloadFactor(arg_4_2)

		local var_4_0 = iter_4_1:GetReloadFactorList()
		local var_4_1 = 1

		for iter_4_2, iter_4_3 in pairs(var_4_0) do
			var_4_1 = var_4_1 + iter_4_3
		end

		iter_4_1:FlushReloadMax(var_4_1)
	end
end

function var_0_3.calcFactor(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_0._value
	local var_5_1 = 0

	if arg_5_0._convertAttr == nil then
		-- block empty
	elseif arg_5_0._convertAttr == "HPRate" or arg_5_0._convertAttr == "DMGRate" then
		var_5_1 = var_0_2.GetCurrent(arg_5_1, arg_5_0._convertAttr) * arg_5_0._convertValue
	else
		var_5_1 = var_0_2.GetBase(arg_5_1, arg_5_0._convertAttr) * arg_5_0._convertValue
	end

	return var_5_0 + var_5_1
end
