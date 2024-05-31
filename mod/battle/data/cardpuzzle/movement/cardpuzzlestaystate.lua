ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.CardPuzzleStayState = class("CardPuzzleStayState", var_0_0.Battle.CardPuzzleIMoveState)

local var_0_1 = var_0_0.Battle.CardPuzzleStayState

var_0_1.__name = "CardPuzzleStayState"
var_0_1.STAY_DURATION = 5000

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.AddMoveToState(arg_2_0, arg_2_1)
	arg_2_1:OnMoveToState()
end

function var_0_1.AddRandomState(arg_3_0, arg_3_1)
	arg_3_1:OnRandomState()
end

function var_0_1.AddStayState(arg_4_0, arg_4_1)
	arg_4_1:OnStayState()
end

function var_0_1.IsFinish(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1:GetStateChangeTimeStamp()

	return arg_5_0._currentTime - var_5_0 > var_0_1.STAY_DURATION
end

function var_0_1.NextState(arg_6_0)
	return var_0_0.Battle.CardPuzzleMoveState.STATE_RANDOM
end
