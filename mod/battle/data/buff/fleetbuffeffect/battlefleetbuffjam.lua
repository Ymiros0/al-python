ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleFleetBuffJam = class("BattleFleetBuffJam", var_0_0.Battle.BattleFleetBuffEffect)
var_0_0.Battle.BattleFleetBuffJam.__name = "BattleFleetBuffJam"

local var_0_1 = var_0_0.Battle.BattleFleetBuffJam

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.onAttach(arg_2_0, arg_2_1, arg_2_2)
	var_0_0.Battle.BattleDataProxy.GetInstance():JamManualCast(true)
	arg_2_1:Jamming(true)
	arg_2_1:SetWeaponBlock(1)
end

function var_0_1.onRemove(arg_3_0, arg_3_1, arg_3_2)
	var_0_0.Battle.BattleDataProxy.GetInstance():JamManualCast(false)
	arg_3_1:Jamming(false)
	arg_3_1:SetWeaponBlock(-1)
end
