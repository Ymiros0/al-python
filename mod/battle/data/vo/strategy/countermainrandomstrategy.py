ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = var_0_0.Battle.BattleConfig

var_0_0.Battle.CounterMainRandomStrategy = class("CounterMainRandomStrategy", var_0_0.Battle.RandomStrategy)

local var_0_3 = var_0_0.Battle.CounterMainRandomStrategy

var_0_3.__name = "CounterMainRandomStrategy"
var_0_3.FIX_FRONT = 0.5

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_3.super.Ctor(arg_1_0, arg_1_1)

def var_0_3.GetStrategyType(arg_2_0):
	return var_0_0.Battle.BattleJoyStickAutoBot.COUNTER_MAIN

def var_0_3.generateTargetPoint(arg_3_0):
	local var_3_0 = arg_3_0._upperBound
	local var_3_1 = arg_3_0._lowerBound

	for iter_3_0, iter_3_1 in pairs(arg_3_0._foeShipList):
		local var_3_2 = iter_3_1.GetPosition().z

		var_3_0 = math.min(var_3_2, var_3_0)
		var_3_1 = math.max(var_3_2, var_3_1)

	local var_3_3 = arg_3_0._fleetVO.GetLeaderPersonality()
	local var_3_4 = var_0_3.FIX_FRONT
	local var_3_5 = var_3_3.rear_rate

	if arg_3_0._fleetVO.GetIFF() == var_0_2.FRIENDLY_CODE:
		var_3_4 = 1 - var_3_4
		var_3_5 = 1 - var_3_5

	local var_3_6 = arg_3_0._totalWidth * var_3_4 + arg_3_0._leftBound
	local var_3_7 = arg_3_0._totalWidth * var_3_5 + arg_3_0._leftBound
	local var_3_8 = arg_3_0._totalHeight * var_3_3.upper_rate + arg_3_0._lowerBound
	local var_3_9 = arg_3_0._totalHeight * var_3_3.lower_rate + arg_3_0._lowerBound
	local var_3_10 = math.min(var_3_0, var_3_8)
	local var_3_11 = math.max(var_3_1, var_3_9)
	local var_3_12
	local var_3_13 = math.random(var_3_7, var_3_6)
	local var_3_14 = math.random(var_3_11, var_3_10)

	return (Vector3(var_3_13, 0, var_3_14))
