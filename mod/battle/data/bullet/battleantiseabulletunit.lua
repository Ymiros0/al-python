ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleAntiSeaBulletUnit = class("BattleAntiSeaBulletUnit", var_0_0.Battle.BattleBulletUnit)
var_0_0.Battle.BattleAntiSeaBulletUnit.__name = "BattleAntiSeaBulletUnit"

local var_0_1 = var_0_0.Battle.BattleAntiSeaBulletUnit

function var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
end

function var_0_1.Update(arg_2_0, arg_2_1)
	return
end

function var_0_1.IsOutRange(arg_3_0)
	return false
end

function var_0_1.SetDirectHitUnit(arg_4_0, arg_4_1)
	arg_4_0._directHitUnit = arg_4_1
end

function var_0_1.GetDirectHitUnit(arg_5_0)
	return arg_5_0._directHitUnit
end

function var_0_1.Dispose(arg_6_0)
	arg_6_0._directHitUnit = nil

	var_0_1.super.Dispose(arg_6_0)
end
