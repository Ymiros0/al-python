﻿ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleEnvironmentBehaviourPlayFX", var_0_0.Battle.BattleEnvironmentBehaviour)

var_0_0.Battle.BattleEnvironmentBehaviourPlayFX = var_0_3
var_0_3.__name = "BattleEnvironmentBehaviourPlayFX"

function var_0_3.Ctor(arg_1_0)
	var_0_3.super.Ctor(arg_1_0)
end

function var_0_3.SetTemplate(arg_2_0, arg_2_1)
	var_0_3.super.SetTemplate(arg_2_0, arg_2_1)

	arg_2_0._FXID = arg_2_0._tmpData.FX_ID
	arg_2_0._offset = arg_2_0._tmpData.offset and Vector3(unpack(arg_2_0._tmpData.offset)) or Vector3.zero
end

function var_0_3.doBehaviour(arg_3_0)
	local var_3_0 = 1

	if arg_3_0._tmpData.scaleRate then
		local var_3_1 = arg_3_0._unit:GetAOEData()
		local var_3_2 = var_3_1:GetAreaType()
		local var_3_3

		if var_3_2 == var_0_1.AreaType.CUBE then
			var_3_3 = var_3_1:GetWidth()
		elseif var_3_2 == var_0_1.AreaType.COLUMN then
			var_3_3 = var_3_1:GetRange()
		end

		var_3_0 = arg_3_0._tmpData.scaleRate * var_3_3
	elseif arg_3_0._tmpData.scale then
		var_3_0 = arg_3_0._tmpData.scale
	end

	local var_3_4 = arg_3_0._unit:GetAOEData():GetPosition() + arg_3_0._offset

	var_0_0.Battle.BattleDataProxy.GetInstance():SpawnEffect(arg_3_0._FXID, var_3_4, var_3_0)
	var_0_3.super.doBehaviour(arg_3_0)
end
