ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleDirectHitWeaponUnit = class("BattleDirectHitWeaponUnit", var_0_0.Battle.BattleWeaponUnit)
var_0_0.Battle.BattleDirectHitWeaponUnit.__name = "BattleDirectHitWeaponUnit"

local var_0_1 = var_0_0.Battle.BattleDirectHitWeaponUnit

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.Spawn(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = var_0_1.super.Spawn(arg_2_0, arg_2_1, arg_2_2)

	var_2_0:SetDirectHitUnit(arg_2_2)

	return var_2_0
end
