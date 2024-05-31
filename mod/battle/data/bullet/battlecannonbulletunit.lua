ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleCannonBulletUnit = class("BattleCannonBulletUnit", var_0_0.Battle.BattleBulletUnit)
var_0_0.Battle.BattleCannonBulletUnit.__name = "BattleCannonBulletUnit"

local var_0_1 = var_0_0.Battle.BattleCannonBulletUnit

function var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
end

function var_0_1.Hit(arg_2_0, arg_2_1, arg_2_2)
	var_0_1.super.Hit(arg_2_0, arg_2_1, arg_2_2)

	arg_2_0._pierceCount = arg_2_0._pierceCount - 1
end
