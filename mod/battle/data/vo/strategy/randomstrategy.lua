ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = var_0_0.Battle.BattleConfig

var_0_0.Battle.RandomStrategy = class("RandomStrategy", var_0_0.Battle.BattleJoyStickBotBaseStrategy)

local var_0_3 = var_0_0.Battle.RandomStrategy

var_0_3.__name = "RandomStrategy"
var_0_3.STOP_DURATION_MAX = 20
var_0_3.STOP_DURATION_MIN = 10
var_0_3.MOVE_DURATION_MAX = 60
var_0_3.MOVE_DURATION_MIN = 20

function var_0_3.Ctor(arg_1_0, arg_1_1)
	var_0_3.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._stopCount = 0
	arg_1_0._moveCount = 0
	arg_1_0._speed = Vector3.zero
	arg_1_0._speedCross = Vector3.zero
end

function var_0_3.GetStrategyType(arg_2_0)
	return var_0_0.Battle.BattleJoyStickAutoBot.RANDOM
end

function var_0_3.Input(arg_3_0, arg_3_1, arg_3_2)
	var_0_3.super.Input(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0:shiftTick(0, 10)
end

local var_0_4 = Vector3.up

function var_0_3._moveTick(arg_4_0)
	if arg_4_0._moveCount <= 0 then
		arg_4_0:shiftTick(-1)
	else
		arg_4_0._moveCount = arg_4_0._moveCount - 1

		local var_4_0 = arg_4_0._speed:Magnitude()

		arg_4_0._speedCross = arg_4_0._speedCross:Copy(var_0_4):Cross2(arg_4_0._speed):Mul(arg_4_0._crossAcc / var_4_0)
		arg_4_0._speed = arg_4_0._speed:Add(arg_4_0._speedCross)
		arg_4_0._hrz = arg_4_0._speed.x
		arg_4_0._vtc = arg_4_0._speed.z
	end
end

function var_0_3._stopTick(arg_5_0)
	if arg_5_0._stopCount <= 0 then
		arg_5_0:shiftTick(0, 10)
	else
		arg_5_0._stopCount = arg_5_0._stopCount - 1
	end
end

function var_0_3.shiftTick(arg_6_0, arg_6_1, arg_6_2)
	arg_6_0._stopWeight = arg_6_1 or arg_6_0._stopWeight
	arg_6_0._moveWeight = arg_6_2 or arg_6_0._moveWeight

	if math.random(arg_6_0._stopWeight, arg_6_0._moveWeight) >= 0 then
		arg_6_0._moveWeight = arg_6_0._moveWeight - 1
		arg_6_0._moveCount = math.random(var_0_3.MOVE_DURATION_MIN, var_0_3.MOVE_DURATION_MAX)
		arg_6_0._targetPoint = arg_6_0:generateTargetPoint()

		local var_6_0 = arg_6_0._motionVO:GetPos()
		local var_6_1, var_6_2 = arg_6_0.getDirection(var_6_0, arg_6_0._targetPoint)

		arg_6_0._speed.x = var_6_1
		arg_6_0._speed.z = var_6_2
		arg_6_0._crossAcc = math.random(-100, 100) / 10000
		arg_6_0.analysis = arg_6_0._moveTick
	else
		arg_6_0._stopCount = math.random(var_0_3.STOP_DURATION_MIN, var_0_3.STOP_DURATION_MAX)
		arg_6_0.analysis = var_0_3._stopTick
		arg_6_0._hrz = 0
		arg_6_0._vtc = 0
	end
end

function var_0_3.generateTargetPoint(arg_7_0)
	local var_7_0 = arg_7_0._fleetVO:GetLeaderPersonality()
	local var_7_1 = var_7_0.front_rate
	local var_7_2 = var_7_0.rear_rate

	if arg_7_0._fleetVO:GetIFF() == var_0_2.FRIENDLY_CODE then
		var_7_1 = 1 - var_7_1
		var_7_2 = 1 - var_7_2
	end

	local var_7_3 = arg_7_0._totalWidth * var_7_1 + arg_7_0._leftBound
	local var_7_4 = arg_7_0._totalWidth * var_7_2 + arg_7_0._leftBound
	local var_7_5 = arg_7_0._totalHeight * var_7_0.upper_rate + arg_7_0._lowerBound
	local var_7_6 = arg_7_0._totalHeight * var_7_0.lower_rate + arg_7_0._lowerBound
	local var_7_7
	local var_7_8 = math.random(var_7_4, var_7_3)
	local var_7_9 = math.random(var_7_6, var_7_5)

	return (Vector3(var_7_8, 0, var_7_9))
end
