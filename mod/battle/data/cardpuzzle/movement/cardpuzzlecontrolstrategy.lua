ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = var_0_0.Battle.BattleConfig

var_0_0.Battle.CardPuzzleControlStrategy = class("CardPuzzleControlStrategy", var_0_0.Battle.BattleJoyStickBotBaseStrategy)

local var_0_3 = var_0_0.Battle.CardPuzzleControlStrategy

var_0_3.__name = "CardPuzzleControlStrategy"

function var_0_3.Ctor(arg_1_0, arg_1_1)
	var_0_3.super.Ctor(arg_1_0, arg_1_1)
	arg_1_0._fleetVO:GetCardPuzzleComponent():AttachMoveController(arg_1_0)

	arg_1_0._moveState = var_0_0.Battle.CardPuzzleMoveState.New(arg_1_0._fleetVO)
end

function var_0_3.GetStrategyType(arg_2_0)
	return var_0_0.Battle.BattleJoyStickAutoBot.CARD_PUZZLE_CONTROL
end

function var_0_3.InputTargetPoint(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0._moveState:SetReferencePoint(arg_3_1)
	arg_3_0._moveState:FinishCallback(arg_3_2)
	arg_3_0._moveState:ChangeState(arg_3_0._moveState.STATE_MOVE)
end

function var_0_3.analysis(arg_4_0)
	local var_4_0, var_4_1 = arg_4_0._moveState:GetDirection()

	arg_4_0._hrz = var_4_0
	arg_4_0._vtc = var_4_1
end

function var_0_3.Output(arg_5_0)
	arg_5_0._moveState:Update()
	arg_5_0:analysis()

	return arg_5_0._hrz, arg_5_0._vtc
end
