﻿ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = class("BattleFleetBound")

var_0_0.Battle.BattleFleetBound = var_0_2
var_0_2.__name = "BattleFleetBound"

function var_0_2.Ctor(arg_1_0, arg_1_1)
	arg_1_0._iff = arg_1_1
end

function var_0_2.Dispose(arg_2_0)
	arg_2_0._iff = nil
end

function var_0_2.GetBound(arg_3_0)
	return arg_3_0._upperBound, arg_3_0._lowerBound, arg_3_0._absoluteLeft, arg_3_0._absoluteRight, arg_3_0._bufferLeft, arg_3_0._bufferRight
end

function var_0_2.GetAbsoluteRight(arg_4_0)
	return arg_4_0._absoluteRight
end

function var_0_2.ConfigAreaData(arg_5_0, arg_5_1, arg_5_2)
	arg_5_0._totalArea = setmetatable({}, {
		__index = arg_5_1
	})
	arg_5_0._playerArea = setmetatable({}, {
		__index = arg_5_2
	})
	arg_5_0._totalLeftBound = arg_5_0._totalArea[1]
	arg_5_0._totalRightBound = arg_5_0._totalArea[1] + arg_5_0._totalArea[3]
	arg_5_0._totalUpperBound = arg_5_0._totalArea[2] + arg_5_0._totalArea[4]
	arg_5_0._totalLowerBound = arg_5_0._totalArea[2]
	arg_5_0._upperBound = arg_5_0._playerArea[2] + arg_5_0._playerArea[4]
	arg_5_0._lowerBound = arg_5_0._playerArea[2]
	arg_5_0._middleLine = arg_5_0._playerArea[1] + arg_5_0._playerArea[3]
end

function var_0_2.SwtichCommon(arg_6_0)
	if arg_6_0._iff == var_0_1.FRIENDLY_CODE then
		arg_6_0._absoluteLeft = arg_6_0._playerArea[1]
		arg_6_0._absoluteRight = var_0_1.MaxRight
		arg_6_0._bufferLeft = var_0_1.MaxLeft
		arg_6_0._bufferRight = arg_6_0._middleLine
	elseif arg_6_0._iff == var_0_1.FOE_CODE then
		arg_6_0._absoluteLeft = arg_6_0._middleLine
		arg_6_0._absoluteRight = arg_6_0._totalRightBound
		arg_6_0._bufferLeft = arg_6_0._middleLine
		arg_6_0._bufferRight = var_0_1.MaxRight
	end
end

function var_0_2.SwtichDuelAggressive(arg_7_0)
	if arg_7_0._iff == var_0_1.FRIENDLY_CODE then
		arg_7_0._absoluteLeft = arg_7_0._middleLine
		arg_7_0._absoluteRight = arg_7_0._totalRightBound
		arg_7_0._bufferLeft = arg_7_0._middleLine
		arg_7_0._bufferRight = var_0_1.MaxRight
	elseif arg_7_0._iff == var_0_1.FOE_CODE then
		arg_7_0._absoluteLeft = arg_7_0._playerArea[1]
		arg_7_0._absoluteRight = var_0_1.MaxRight
		arg_7_0._bufferLeft = var_0_1.MaxLeft
		arg_7_0._bufferRight = arg_7_0._middleLine
	end
end

function var_0_2.SwtichDBRGL(arg_8_0)
	if arg_8_0._iff == var_0_1.FRIENDLY_CODE then
		arg_8_0._absoluteLeft = arg_8_0._playerArea[1]
		arg_8_0._absoluteRight = arg_8_0._middleLine
		arg_8_0._bufferLeft = var_0_1.MaxLeft
		arg_8_0._bufferRight = var_0_1.MaxRight
	elseif arg_8_0._iff == var_0_1.FOE_CODE then
		arg_8_0._absoluteLeft = arg_8_0._middleLine
		arg_8_0._absoluteRight = arg_8_0._totalRightBound
		arg_8_0._bufferLeft = arg_8_0._middleLine
		arg_8_0._bufferRight = var_0_1.MaxRight
	end
end

function var_0_2.FixCardPuzzleInput(arg_9_0, arg_9_1)
	local var_9_0 = math.clamp(arg_9_1.x, arg_9_0._absoluteLeft, arg_9_0._absoluteRight)
	local var_9_1 = math.clamp(arg_9_1.z, arg_9_0._lowerBound, arg_9_0._upperBound)

	arg_9_1:Set(var_9_0, 0, var_9_1)
end
