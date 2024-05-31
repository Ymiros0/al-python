ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = class("BattleCardPuzzleSkillMoveTo", var_0_0.Battle.BattleCardPuzzleSkillEffect)

var_0_0.Battle.BattleCardPuzzleSkillMoveTo = var_0_3
var_0_3.__name = "BattleCardPuzzleSkillMoveTo"

function var_0_3.Ctor(arg_1_0, arg_1_1)
	var_0_3.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_3.HoldForInput(arg_2_0)
	return false
end

function var_0_3.SkillEffectHandler(arg_3_0)
	local var_3_0 = arg_3_0._card:GetInputPoint()
	local var_3_1 = arg_3_0:GetCardPuzzleComponent():TakeoverMovecontroller(var_3_0, function()
		arg_3_0:Finale()
	end)
end

function var_0_3.Finale(arg_5_0)
	var_0_3.super.Finale(arg_5_0)
	arg_5_0:GetCardPuzzleComponent():ReturnMovecontroller()
end
