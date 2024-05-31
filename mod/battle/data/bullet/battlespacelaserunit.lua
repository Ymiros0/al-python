ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleTargetChoise
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = class("BattleSpaceLaserUnit", var_0_0.Battle.BattleColumnAreaBulletUnit)

var_0_3.__name = "BattleSpaceLaserUnit"
var_0_0.Battle.BattleSpaceLaserUnit = var_0_3
var_0_3.STATE_READY = "Ready"
var_0_3.STATE_PRECAST = "Precast"
var_0_3.STATE_ATTACK = "Attack"
var_0_3.STATE_DESTROY = "Destroy"

function var_0_3.Ctor(arg_1_0, ...)
	var_0_3.super.Ctor(arg_1_0, ...)

	arg_1_0._collidedTimes = {}
end

function var_0_3.Dispose(arg_2_0)
	arg_2_0._lifeEndCb = nil
	arg_2_0._collidedTimes = nil

	var_0_3.super.Dispose(arg_2_0)
end

function var_0_3.ExecuteLifeEndCallback(arg_3_0)
	if arg_3_0._lifeEndCb then
		arg_3_0._lifeEndCb()
	end
end

function var_0_3.AssertFields(arg_4_0, arg_4_1)
	assert(arg_4_0[arg_4_1], "Lack Field " .. arg_4_1)
end

function var_0_3.SetTemplateData(arg_5_0, arg_5_1)
	arg_5_0.AssertFields(arg_5_1.extra_param, "attack_time")
	arg_5_0.AssertFields(arg_5_1.hit_type, "interval")
	var_0_3.super.SetTemplateData(arg_5_0, arg_5_1)

	arg_5_0._hitInterval = arg_5_1.hit_type.interval
end

function var_0_3.GetHitInterval(arg_6_0)
	return arg_6_0._hitInterval
end

function var_0_3.DoTrack(arg_7_0)
	local var_7_0 = arg_7_0
	local var_7_1 = var_7_0:getTrackingTarget()

	if not var_7_1 or var_7_1 == -1 then
		return
	elseif not var_7_1:IsAlive() then
		var_7_0:setTrackingTarget(-1)
		var_7_0._speed:SetNormalize():Mul(arg_7_0._convertedVelocity)

		return
	elseif var_7_0:GetDistance(var_7_1) > var_7_0._trackRange then
		var_7_0:setTrackingTarget(-1)
		var_7_0._speed:SetNormalize():Mul(arg_7_0._convertedVelocity)

		return
	end

	local var_7_2 = var_7_1:GetPosition() - var_7_0:GetPosition()
	local var_7_3 = var_7_2:Magnitude()

	if var_7_3 <= 1e-05 then
		arg_7_0._speed:Set(0, 0, 0)

		return
	end

	local var_7_4 = arg_7_0._speedNormal

	var_7_2:SetNormalize()

	local var_7_5 = var_7_2.x * var_7_4.x + var_7_2.z * var_7_4.z
	local var_7_6 = var_7_2.z * var_7_4.x - var_7_2.x * var_7_4.z
	local var_7_7 = var_7_0:GetSpeedRatio()
	local var_7_8 = math.cos(var_7_0._cosAngularSpeed * var_7_7)
	local var_7_9 = math.sin(var_7_0._sinAngularSpeed * var_7_7)
	local var_7_10 = var_7_5
	local var_7_11 = var_7_6

	if var_7_5 < var_7_8 then
		var_7_10 = var_7_8
		var_7_11 = var_7_9 * (var_7_11 > 0 and 1 or -1)
	end

	local var_7_12 = var_7_4.x * var_7_10 - var_7_4.z * var_7_11
	local var_7_13 = var_7_4.z * var_7_10 + var_7_4.x * var_7_11
	local var_7_14 = math.min(arg_7_0._convertedVelocity, var_7_3)

	var_7_0._speed:Set(var_7_12, 0, var_7_13)
	var_7_0._speed:Mul(var_7_14)
	arg_7_0._speedNormal:Set(var_7_12, 0, var_7_13)
	arg_7_0._speedNormal:SetNormalize()

	arg_7_0._yAngle = math.rad2Deg * math.atan2(var_7_12, var_7_13)
end

function var_0_3.InitSpeed(arg_8_0, ...)
	var_0_3.super.InitSpeed(arg_8_0, ...)

	if arg_8_0:IsTracker() then
		local var_8_0 = math.deg2Rad * arg_8_0._yAngle

		arg_8_0._speedNormal = Vector3(math.cos(var_8_0), 0, math.sin(var_8_0))
		arg_8_0.updateSpeed = arg_8_0.DoTrack
	elseif arg_8_0:IsCircle() and arg_8_0:IsAlert() then
		arg_8_0._centripetalSpeed = arg_8_0._centripetalSpeed * arg_8_0.alertSpeedRatio
	end
end

function var_0_3.SetLifeTime(arg_9_0, arg_9_1)
	arg_9_0._lifeTime = arg_9_1
end

function var_0_3.SetAlert(arg_10_0, arg_10_1)
	arg_10_0._alertFlag = arg_10_1

	local var_10_0 = arg_10_0:GetTemplate().extra_param

	if not var_10_0.alertSpeed then
		return
	end

	arg_10_0:ResetVelocity(arg_10_0._velocity * var_10_0.alertSpeed)

	arg_10_0.alertSpeedRatio = var_10_0.alertSpeed
end

function var_0_3.IsAlert(arg_11_0)
	return arg_11_0._alertFlag
end

function var_0_3.Update(arg_12_0, arg_12_1)
	var_0_3.super.Update(arg_12_0, arg_12_1)

	arg_12_0._reachDestFlag = arg_12_1 > arg_12_0._timeStamp + arg_12_0._lifeTime

	local var_12_0 = pg.TimeMgr.GetInstance():GetCombatTime()

	for iter_12_0, iter_12_1 in pairs(arg_12_0._collidedTimes) do
		if var_12_0 > iter_12_1 + arg_12_0._hitInterval then
			arg_12_0._collidedTimes[iter_12_0] = nil
			arg_12_0._collidedList[iter_12_0] = nil
		end
	end
end

function var_0_3.GetCollidedList(arg_13_0)
	return arg_13_0._collidedList, arg_13_0._collidedTimes
end

function var_0_3.RegisterLifeEndCB(arg_14_0, arg_14_1)
	arg_14_0._lifeEndCb = arg_14_1
end

function var_0_3.UnRegisterLifeEndCB(arg_15_0)
	arg_15_0._lifeEndCb = nil
end
