ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattleBulletEvent
local var_0_4 = pg.bfConsts
local var_0_5 = var_0_0.Battle.BattleFormulas
local var_0_6 = var_0_0.Battle.BattleConfig
local var_0_7 = class("BattleMissileUnit", var_0_0.Battle.BattleBulletUnit)

var_0_7.__name = "BattleMissileUnit"
var_0_0.Battle.BattleMissileUnit = var_0_7
var_0_7.STATE_LAUNCH = "Launch"
var_0_7.STATE_ATTACK = "Attack"
var_0_7.TYPE_COORD = 1
var_0_7.TYPE_RANGE = 2
var_0_7.TYPE_TARGET = 3

function var_0_7.Ctor(arg_1_0, ...)
	var_0_7.super.Ctor(arg_1_0, ...)

	arg_1_0._state = arg_1_0.STATE_LAUNCH
end

function var_0_7.SetTemplateData(arg_2_0, arg_2_1)
	var_0_7.super.SetTemplateData(arg_2_0, arg_2_1)
	arg_2_0:ResetVelocity(0)

	local var_2_0 = arg_2_0:GetTemplate().extra_param

	arg_2_0._gravity = var_2_0.gravity or var_0_0.Battle.BattleConfig.GRAVITY
	arg_2_0._targetType = var_2_0.aimType or var_0_7.TYPE_TARGET
end

function var_0_7.GetPierceCount(arg_3_0)
	return 1
end

function var_0_7.RegisterOnTheAir(arg_4_0, arg_4_1)
	arg_4_0._onTheHighest = arg_4_1
end

function var_0_7.SetExplodePosition(arg_5_0, arg_5_1)
	arg_5_0._explodePos = arg_5_1:Clone()
	arg_5_0._explodePos.y = var_0_1.BombDetonateHeight
end

function var_0_7.GetExplodePostion(arg_6_0)
	return arg_6_0._explodePos
end

local var_0_8 = 1 / var_0_6.viewFPS

function var_0_7.SetSpawnPosition(arg_7_0, arg_7_1)
	var_0_7.super.SetSpawnPosition(arg_7_0, arg_7_1)

	arg_7_0._verticalSpeed = arg_7_0:GetTemplate().extra_param.launchVrtSpeed
end

function var_0_7.Update(arg_8_0, arg_8_1)
	var_0_7.super.Update(arg_8_0, arg_8_1)

	if arg_8_0._state == arg_8_0.STATE_LAUNCH and arg_8_1 > arg_8_0:GetTemplate().extra_param.launchRiseTime + arg_8_0._timeStamp then
		arg_8_0:CompleteRise()
	end
end

function var_0_7.CompleteRise(arg_9_0)
	arg_9_0._state = arg_9_0.STATE_ATTACK
	arg_9_0._gravity = 0

	if arg_9_0._onTheHighest then
		arg_9_0._onTheHighest()
	end

	local var_9_0 = arg_9_0:GetTemplate().extra_param.fallTime

	arg_9_0._targetPos = arg_9_0._explodePos
	arg_9_0._yAngle = math.rad2Deg * math.atan2(arg_9_0._explodePos.z - arg_9_0._spawnPos.z, arg_9_0._explodePos.x - arg_9_0._spawnPos.x)
	arg_9_0._verticalSpeed = -(arg_9_0._position.y / var_9_0) * var_0_8

	local var_9_1 = pg.Tool.FilterY(arg_9_0._explodePos - arg_9_0._position):Magnitude()

	arg_9_0:ResetVelocity(var_0_5.ConvertBulletDataSpeed(var_9_1 / var_9_0 * var_0_8))
	arg_9_0:calcSpeed()
end

function var_0_7.IsOutRange(arg_10_0)
	return arg_10_0._state == arg_10_0.STATE_ATTACK and arg_10_0._position.y <= var_0_1.BombDetonateHeight
end

function var_0_7.OutRange(arg_11_0, arg_11_1)
	local var_11_0 = {
		UID = arg_11_1
	}

	arg_11_0:DispatchEvent(var_0_0.Event.New(var_0_3.EXPLODE, var_11_0))
	var_0_7.super.OutRange(arg_11_0)
end

function var_0_7.GetMissileTargetPosition(arg_12_0)
	if arg_12_0._targetType == var_0_7.TYPE_RANGE then
		return arg_12_0:aimRange()
	elseif arg_12_0._targetType == var_0_7.TYPE_COORD then
		return arg_12_0:aimCoord()
	elseif arg_12_0._targetType == var_0_7.TYPE_TARGET then
		return arg_12_0:aimTarget()
	end
end

function var_0_7.aimRange(arg_13_0)
	local var_13_0 = arg_13_0._range
	local var_13_1 = arg_13_0._range * arg_13_0:GetIFF()

	return (Vector3(arg_13_0._spawnPos.x + var_13_1, 0, 0))
end

function var_0_7.aimCoord(arg_14_0)
	local var_14_0 = arg_14_0:GetTemplate().extra_param
	local var_14_1 = var_14_0.missileX
	local var_14_2 = var_14_0.missileZ

	if not var_14_1 or not var_14_2 then
		return arg_14_0:aimRange()
	end

	return (Vector3(var_14_1, 0, var_14_2))
end

function var_0_7.aimTarget(arg_15_0)
	local var_15_0 = arg_15_0:GetWeapon()
	local var_15_1 = var_15_0:GetHost()

	if not var_15_1 or not var_15_1:IsAlive() then
		return arg_15_0:aimCoord()
	end

	local var_15_2 = var_15_0:Tracking()

	return var_15_0:GetTemplateData().aim_type == var_0_2.WeaponAimType.AIM and var_15_2 and var_15_0:CalculateRandTargetPosition(arg_15_0, var_15_2) or var_15_0:CalculateFixedExplodePosition(arg_15_0)
end
