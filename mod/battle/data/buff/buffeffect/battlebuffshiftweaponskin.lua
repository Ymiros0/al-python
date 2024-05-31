ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffShiftWeaponSkin = class("BattleBuffShiftWeaponSkin", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffShiftWeaponSkin.__name = "BattleBuffShiftWeaponSkin"

local var_0_1 = var_0_0.Battle.BattleBuffShiftWeaponSkin

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._weaponIndex = arg_2_0._tempData.arg_list.index
	arg_2_0._skinID = arg_2_0._tempData.arg_list.skin_id
end

function var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0:shiftWeaponSkin(arg_3_1)
end

function var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2)
	return
end

function var_0_1.shiftWeaponSkin(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1:GetAllWeapon()

	for iter_5_0, iter_5_1 in ipairs(arg_5_0._indexRequire) do
		for iter_5_2, iter_5_3 in ipairs(var_5_0) do
			if iter_5_3:GetEquipmentIndex() == iter_5_1 then
				iter_5_3:SetSkinData(arg_5_0._skinID)
			end
		end
	end
end
