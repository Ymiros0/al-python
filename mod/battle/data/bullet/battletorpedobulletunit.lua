ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = class("BattleTorpedoBulletUnit", var_0_0.Battle.BattleBulletUnit)

var_0_0.Battle.BattleTorpedoBulletUnit = var_0_2
var_0_2.__name = "BattleTorpedoBulletUnit"

function var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
end

function var_0_2.calcSpeed(arg_2_0)
	local var_2_0 = 1 + var_0_0.Battle.BattleAttr.GetCurrent(arg_2_0, "bulletSpeedRatio")
	local var_2_1 = math.max(0, arg_2_0._velocity + var_0_0.Battle.BattleAttr.GetCurrent(arg_2_0, "torpedoSpeedExtra")) * var_2_0
	local var_2_2 = var_0_1.ConvertBulletSpeed(var_2_1)
	local var_2_3 = math.deg2Rad * arg_2_0._yAngle

	arg_2_0._speed = Vector3(var_2_2 * math.cos(var_2_3), 0, var_2_2 * math.sin(var_2_3))
end

function var_0_2.GetExplodePostion(arg_3_0)
	return arg_3_0._explodePos
end

function var_0_2.SetExplodePosition(arg_4_0, arg_4_1)
	arg_4_0._explodePos = arg_4_1
end

function var_0_2.InitCldComponent(arg_5_0)
	var_0_2.super.InitCldComponent(arg_5_0)
	arg_5_0:ResetCldSurface()
end

function var_0_2.Hit(arg_6_0, arg_6_1, arg_6_2)
	var_0_2.super.Hit(arg_6_0, arg_6_1, arg_6_2)

	arg_6_0._pierceCount = arg_6_0._pierceCount - 1
end
