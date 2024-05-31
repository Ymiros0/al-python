ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleResourceManager

var_0_0.Battle.BattleStrayBullet = class("BattleStrayBullet", var_0_0.Battle.BattleBullet)
var_0_0.Battle.BattleStrayBullet.__name = "BattleStrayBullet"

local var_0_2 = var_0_0.Battle.BattleStrayBullet

function var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
end

function var_0_2.SetSpawn(arg_2_0, arg_2_1)
	var_0_2.super.SetSpawn(arg_2_0, arg_2_1)

	arg_2_0._targetPos = Clone(arg_2_0._bulletData:GetExplodePostion())
	arg_2_0._spawnDir = arg_2_0._speed.normalized

	local var_2_0 = 1 + var_0_0.Battle.BattleAttr.GetCurrent(arg_2_0._bulletData, "bulletSpeedRatio")

	arg_2_0._velocity = arg_2_0._bulletData:GetVelocity() * var_2_0
	arg_2_0._velocity = var_0_0.Battle.BattleFormulas.ConvertBulletSpeed(arg_2_0._velocity)
	arg_2_0._step = Vector3.Distance(arg_2_0._targetPos, arg_2_0._spawnPos) / arg_2_0._velocity
	arg_2_0._count = math.random(600) - 300
	arg_2_0.updateSpeed = var_0_2._doStray
end

function var_0_2._doStray(arg_3_0)
	local var_3_0 = arg_3_0._targetPos

	if arg_3_0._step > 0 and var_3_0 and not var_3_0:EqualZero() then
		arg_3_0._count = arg_3_0._count / 1.06
		arg_3_0._step = arg_3_0._step - 1

		local var_3_1 = arg_3_0._bulletData:GetPosition()
		local var_3_2 = arg_3_0._velocity

		arg_3_0._speed = Vector3(var_3_0.x - var_3_1.x, 0, var_3_0.z - var_3_1.z).normalized
		arg_3_0._speed = arg_3_0._speed + Vector3(arg_3_0._speed.z * arg_3_0._count / 100, 0, -arg_3_0._speed.x * arg_3_0._count / 100)
		arg_3_0._speed = arg_3_0._speed.normalized
		arg_3_0._speed = Vector3(arg_3_0._speed.x * var_3_2, 0, arg_3_0._speed.z * var_3_2)
	else
		arg_3_0.updateSpeed = var_0_2._updateSpeed
	end
end
