﻿ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("IPilot")

var_0_0.Battle.IPilot = var_0_1
var_0_1.__name = "IPilot"

function var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._index = arg_1_1
	arg_1_0._pilot = arg_1_2
end

function var_0_1.SetParameter(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._paramList = arg_2_1
	arg_2_0._valve = arg_2_1.valve or var_0_0.Battle.AutoPilot.PILOT_VALVE
	arg_2_0._toIndex = arg_2_2
	arg_2_0._duration = arg_2_1.duration or -1
end

function var_0_1.GetIndex(arg_3_0)
	return arg_3_0._index
end

function var_0_1.GetToIndex(arg_4_0)
	return arg_4_0._toIndex
end

function var_0_1.Active(arg_5_0, arg_5_1)
	arg_5_0._startTime = pg.TimeMgr.GetInstance():GetCombatTime()
end

function var_0_1.IsExpired(arg_6_0)
	if arg_6_0._duration > 0 and pg.TimeMgr.GetInstance():GetCombatTime() - arg_6_0._startTime > arg_6_0._duration then
		return true
	else
		return false
	end
end

function var_0_1.GetDirection(arg_7_0, arg_7_1)
	return
end

function var_0_1.Finish(arg_8_0)
	arg_8_0._pilot:NextStep()
end
