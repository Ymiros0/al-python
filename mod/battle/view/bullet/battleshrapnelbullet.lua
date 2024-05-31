ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBulletEvent
local var_0_2 = class("BattleShrapnelBullet", var_0_0.Battle.BattleBullet)

var_0_0.Battle.BattleShrapnelBullet = var_0_2
var_0_2.__name = "BattleShrapnelBullet"

function var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
end

function var_0_2.AddBulletEvent(arg_2_0)
	var_0_2.super.AddBulletEvent(arg_2_0)
	arg_2_0._bulletData:RegisterEventListener(arg_2_0, var_0_1.SPLIT, arg_2_0.onBulletSplit)
end

function var_0_2.RemoveBulletEvent(arg_3_0)
	var_0_2.super.RemoveBulletEvent(arg_3_0)
	arg_3_0._bulletData:UnregisterEventListener(arg_3_0, var_0_1.SPLIT)
end

function var_0_2.onBulletSplit(arg_4_0, arg_4_1)
	arg_4_0._bulletHitFunc(arg_4_0)
end
