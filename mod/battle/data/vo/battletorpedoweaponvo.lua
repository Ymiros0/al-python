ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig.TorpedoCFG
local var_0_2 = class("BattleTorpedoWeaponVO", var_0_0.Battle.BattlePlayerWeaponVO)

var_0_0.Battle.BattleTorpedoWeaponVO = var_0_2
var_0_2.__name = "BattleTorpedoWeaponVO"

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0, var_0_1.GCD)
end

function var_0_2.AppendWeapon(arg_2_0, arg_2_1)
	var_0_2.super.AppendWeapon(arg_2_0, arg_2_1)
	arg_2_1:SetPlayerTorpedoWeaponVO(arg_2_0)
end

function var_0_2.GetCurrentWeaponIconIndex(arg_3_0)
	return 2
end
