ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = var_0_0.Battle.BattleAttr

var_0_0.Battle.BattleBuffSmokeAimBias = class("BattleBuffSmokeAimBias", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffSmokeAimBias.__name = "BattleBuffSmokeAimBias"

local var_0_4 = var_0_0.Battle.BattleBuffSmokeAimBias
local var_0_5 = var_0_0.Battle.BattleAttr

var_0_4.ATTR_SMOKE = "smoke_aim_bias"

function var_0_4.Ctor(arg_1_0, arg_1_1)
	var_0_4.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_4.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	return
end

function var_0_4.onAttach(arg_3_0, arg_3_1, arg_3_2)
	var_0_5.SetCurrent(arg_3_1, var_0_4.ATTR_SMOKE, 1)
	var_0_1.AttachSmoke(arg_3_1)

	if BATTLE_ENEMY_AIMBIAS_RANGE then
		var_0_0.Battle.BattleDataProxy.GetInstance():DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleEvent.ADD_AIM_BIAS, {
			aimBias = arg_3_1:GetAimBias()
		}))
	end
end

function var_0_4.onUpdate(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	local var_4_0 = {
		[var_0_2.FRIENDLY_CODE] = 0,
		[var_0_2.FOE_CODE] = 0
	}
	local var_4_1 = {
		[var_0_2.FRIENDLY_CODE] = 0,
		[var_0_2.FOE_CODE] = 0
	}
	local var_4_2 = var_0_0.Battle.BattleDataProxy.GetInstance():GetUnitList()

	for iter_4_0, iter_4_1 in pairs(var_4_2) do
		local var_4_3 = iter_4_1:GetIFF()
		local var_4_4 = var_4_0[var_4_3]
		local var_4_5 = var_0_3.GetCurrent(iter_4_1, "attackRating")
		local var_4_6 = var_0_3.GetCurrent(iter_4_1, "aimBiasExtraACC")

		var_4_0[var_4_3] = math.max(var_4_4, var_4_5)
		var_4_1[var_4_3] = var_4_1[var_4_3] + var_4_6
	end

	local var_4_7 = arg_4_1:GetAimBias()

	var_4_7:SetDecayFactor(var_4_0[var_0_2.FRIENDLY_CODE], var_4_1[var_0_2.FRIENDLY_CODE])

	local var_4_8 = arg_4_3.timeStamp

	var_4_7:Update(var_4_8)
end

function var_0_4.onRemove(arg_5_0, arg_5_1, arg_5_2)
	if BATTLE_ENEMY_AIMBIAS_RANGE then
		var_0_0.Battle.BattleDataProxy.GetInstance():DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleEvent.REMOVE_AIM_BIAS, {
			aimBias = arg_5_1:GetAimBias()
		}))
	end

	var_0_5.SetCurrent(arg_5_1, var_0_4.ATTR_SMOKE, 0)
	arg_5_1:ExitSmokeArea()
end
