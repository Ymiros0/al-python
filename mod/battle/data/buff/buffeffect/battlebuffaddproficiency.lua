ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffAddProficiency", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffAddProficiency = var_0_1
var_0_1.__name = "BattleBuffAddProficiency"

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._group = arg_2_0._tempData.arg_list.group or arg_2_2:GetID()
	arg_2_0._weaponLabelList = arg_2_0._tempData.arg_list.label or {}
	arg_2_0._weaponIndexList = arg_2_0._tempData.arg_list.index
	arg_2_0._number = arg_2_0._tempData.arg_list.number
end

function var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = arg_3_1:GetAllWeapon()

	arg_3_0:calcEnhancement(var_3_0, true)
end

function var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = arg_4_1:GetAllWeapon()

	arg_4_0:calcEnhancement(var_4_0, false)
end

function var_0_1.calcEnhancement(arg_5_0, arg_5_1, arg_5_2)
	local var_5_0 = arg_5_0._number

	if not arg_5_2 then
		var_5_0 = var_5_0 * -1
	end

	for iter_5_0, iter_5_1 in ipairs(arg_5_1) do
		local var_5_1 = 1
		local var_5_2 = iter_5_1:GetEquipmentLabel()

		for iter_5_2, iter_5_3 in ipairs(arg_5_0._weaponLabelList) do
			if not table.contains(var_5_2, iter_5_3) then
				var_5_1 = 0

				break
			end
		end

		if arg_5_0._weaponIndexList then
			local var_5_3 = iter_5_1:GetEquipmentIndex()

			if not table.contains(arg_5_0._weaponIndexList, var_5_3) then
				var_5_1 = var_5_1 * 0
			end
		end

		if var_5_1 == 1 then
			local var_5_4 = iter_5_1:GetPotential() + var_5_0

			iter_5_1:SetPotentialFactor(var_5_4)
		end
	end
end
