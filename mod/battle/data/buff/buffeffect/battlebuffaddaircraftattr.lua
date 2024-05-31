﻿ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffAddAircraftAttr = class("BattleBuffAddAircraftAttr", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffAddAircraftAttr.__name = "BattleBuffAddAircraftAttr"

local var_0_1 = var_0_0.Battle.BattleBuffAddAircraftAttr

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._attr = arg_2_0._tempData.arg_list.attr
	arg_2_0._number = arg_2_0._tempData.arg_list.number
	arg_2_0._numberBase = arg_2_0._number
end

function var_0_1.onStack(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0._number = arg_3_0._numberBase * arg_3_2._stack
end

function var_0_1.onAircraftCreate(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	if not arg_4_0:equipIndexRequire(arg_4_3.equipIndex) then
		return
	end

	arg_4_0:calcAircraftAttr(arg_4_3.aircraft)
end

function var_0_1.calcAircraftAttr(arg_5_0, arg_5_1)
	var_0_0.Battle.BattleAttr.Increase(arg_5_1, arg_5_0._attr, arg_5_0._number)
end
