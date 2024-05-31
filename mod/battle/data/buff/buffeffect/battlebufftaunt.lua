﻿ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleAttr
local var_0_2 = class("BattleBuffTaunt", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffTaunt = var_0_2
var_0_2.__name = "BattleBuffTaunt"

function var_0_2.Ctor(arg_1_0, arg_1_1)
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._tauntActive = false
end

function var_0_2.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._guardTargetFilter = arg_2_0._tempData.arg_list.guardTarget
	arg_2_0._handleCloak = arg_2_1:GetCloak() ~= nil
end

function var_0_2.onTrigger(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	if not arg_3_0._handleCloak then
		return
	end

	local var_3_0 = arg_3_0:getTargetList(arg_3_1, arg_3_0._guardTargetFilter, arg_3_0._tempData.arg_list)
	local var_3_1 = true

	for iter_3_0, iter_3_1 in ipairs(var_3_0) do
		var_3_1 = var_3_1 and var_0_1.IsCloak(iter_3_1)
	end

	if not var_3_1 and not arg_3_0._tauntActive then
		arg_3_0:forceToExpose(arg_3_1)
	elseif var_3_1 and arg_3_0._tauntActive then
		arg_3_0:releaseExpose(arg_3_1)
	end
end

function var_0_2.onRemove(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	arg_4_0:releaseExpose(arg_4_1)
end

function var_0_2.forceToExpose(arg_5_0, arg_5_1)
	if not arg_5_0._handleCloak then
		return
	end

	arg_5_0._tauntActive = true

	local var_5_0 = arg_5_1:GetCloak()

	var_5_0:ForceToMax()
	var_5_0:UpdateTauntExpose(true)
end

function var_0_2.releaseExpose(arg_6_0, arg_6_1)
	if not arg_6_0._handleCloak then
		return
	end

	arg_6_0._tauntActive = false

	arg_6_1:GetCloak():UpdateTauntExpose(false)
end
