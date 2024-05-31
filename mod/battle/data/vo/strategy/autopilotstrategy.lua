ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = var_0_0.Battle.BattleConfig

var_0_0.Battle.AutoPilotStrategy = class("AutoPilotStrategy", var_0_0.Battle.BattleJoyStickBotBaseStrategy)

local var_0_3 = var_0_0.Battle.AutoPilotStrategy

var_0_3.__name = "AutoPilotStrategy"
var_0_3.FIX_FRONT = 0.5

function var_0_3.Ctor(arg_1_0, arg_1_1)
	var_0_3.super.Ctor(arg_1_0, arg_1_1)

	local var_1_0 = arg_1_1:GetMotionReferenceUnit()
	local var_1_1 = arg_1_1:GetAutoBotAIID()
	local var_1_2 = var_0_0.Battle.BattleDataFunction.GetAITmpDataFromID(var_1_1)

	arg_1_0._autoPilot = var_0_0.Battle.AutoPilot.New(var_1_0, var_1_2)
end

function var_0_3.GetStrategyType(arg_2_0)
	return var_0_0.Battle.BattleJoyStickAutoBot.AUTO_PILOT
end

function var_0_3.analysis(arg_3_0)
	local var_3_0 = arg_3_0._autoPilot:GetDirection()

	arg_3_0._hrz = var_3_0.x
	arg_3_0._vtc = var_3_0.z
end
