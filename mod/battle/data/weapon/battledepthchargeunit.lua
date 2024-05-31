ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst

var_0_0.Battle.BattleDepthChargeUnit = class("BattleDepthChargeUnit", var_0_0.Battle.BattleWeaponUnit)
var_0_0.Battle.BattleDepthChargeUnit.__name = "BattleDepthChargeUnit"

local var_0_2 = var_0_0.Battle.BattleDepthChargeUnit
local var_0_3 = var_0_0.Battle.BattleTargetChoise

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0)
end

function var_0_2.TriggerBuffOnFire(arg_2_0)
	arg_2_0._host:TriggerBuff(var_0_1.BuffEffectType.ON_DEPTH_CHARGE_DROP, {
		equipIndex = arg_2_0._equipmentIndex
	})
end
