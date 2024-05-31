ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.CardPuzzleMoveToState = class("CardPuzzleMoveToState", var_0_0.Battle.CardPuzzleIMoveState)

local var_0_1 = var_0_0.Battle.CardPuzzleMoveToState

var_0_1.__name = "CardPuzzleMoveToState"
var_0_1.VALVE = 0.5

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

def var_0_1.AddMoveToState(arg_2_0, arg_2_1):
	arg_2_1.OnMoveToState()

def var_0_1.AddRandomState(arg_3_0, arg_3_1):
	arg_3_1.OnRandomState()

def var_0_1.AddStayState(arg_4_0, arg_4_1):
	arg_4_1.OnStayState()

def var_0_1.IsFinish(arg_5_0, arg_5_1):
	return (arg_5_0._referencePoint - arg_5_1.GetFleetPosition()).magnitude < var_0_1.VALVE

def var_0_1.GetOutput(arg_6_0, arg_6_1):
	local var_6_0 = (arg_6_0._referencePoint - arg_6_1.GetFleetPosition()).normalized

	return var_6_0.x, var_6_0.z

def var_0_1.NextState(arg_7_0):
	return var_0_0.Battle.CardPuzzleMoveState.STATE_STAY
