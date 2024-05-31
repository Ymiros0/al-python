ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillWeaponFire", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillWeaponFire = var_0_1
var_0_1.__name = "BattleSkillWeaponFire"

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._weaponType = arg_1_0._tempData.arg_list.weaponType
	arg_1_0._useTempBullet = arg_1_0._tempData.arg_list.preShiftBullet
end

function var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_0:_GetWeapon(arg_2_1)

	for iter_2_0, iter_2_1 in ipairs(var_2_0) do
		iter_2_1:SingleFire(arg_2_2, nil, nil, arg_2_0._useTempBullet)
	end
end

function var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1)
	arg_3_0:DoDataEffect(arg_3_1, nil)
end

function var_0_1._GetWeapon(arg_4_0, arg_4_1)
	local var_4_0 = {}

	if arg_4_0._weaponType == "ChargeWeapon" then
		table.insert(var_4_0, arg_4_1:GetChargeList()[1])
	elseif arg_4_0._weaponType == "TorpedoWeapon" then
		table.insert(var_4_0, arg_4_1:GetTorpedoList()[1])
	elseif arg_4_0._weaponType == "AirAssist" then
		table.insert(var_4_0, arg_4_1:GetAirAssistList()[1])
	elseif arg_4_0._weaponType == "Aircraft" then
		local var_4_1 = arg_4_1:GetHiveList()

		for iter_4_0, iter_4_1 in ipairs(var_4_1) do
			table.insert(var_4_0, iter_4_1)
		end
	else
		table.insert(var_4_0, arg_4_1:GetAutoWeapons()[1])
	end

	return var_4_0
end
