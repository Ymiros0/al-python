﻿ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattleFormulas
local var_0_4 = var_0_0.Battle.BattleAttr
local var_0_5 = var_0_0.Battle.BattleConfig
local var_0_6 = var_0_0.Battle.BattleUnitEvent
local var_0_7 = class("BattleBossUnit", var_0_0.Battle.BattleEnemyUnit)

var_0_0.Battle.BattleBossUnit = var_0_7
var_0_7.__name = "BattleBossUnit"

function var_0_7.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_7.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._isBoss = true
end

function var_0_7.IsBoss(arg_2_0)
	return true
end

function var_0_7.BarrierStateChange(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = {
		barrierDurability = arg_3_1,
		barrierDuration = arg_3_2
	}

	arg_3_0:DispatchEvent(var_0_0.Event.New(var_0_6.BARRIER_STATE_CHANGE, var_3_0))
end

function var_0_7.UpdateHP(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4)
	local var_4_0 = var_0_7.super.UpdateHP(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4) or 0

	if var_4_0 < 0 then
		for iter_4_0, iter_4_1 in ipairs(arg_4_0._autoWeaponList) do
			iter_4_1:UpdatePrecastArmor(var_4_0)
		end
	end

	return var_4_0
end
