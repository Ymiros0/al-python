ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.CardPuzzleRandomState = class("CardPuzzleRandomState", var_0_0.Battle.CardPuzzleIMoveState)

local var_0_1 = var_0_0.Battle.CardPuzzleRandomState

var_0_1.__name = "CardPuzzleRandomState"
var_0_1.VALVE = 0.5
var_0_1.RANDOM_RANGE = 10

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

def var_0_1.AddMoveToState(arg_2_0, arg_2_1):
	arg_2_1.OnMoveToState()

def var_0_1.AddRandomState(arg_3_0, arg_3_1):
	return

def var_0_1.AddStayState(arg_4_0, arg_4_1):
	arg_4_1.OnStayState()

def var_0_1.IntputReferencePoint(arg_5_0, arg_5_1):
	local var_5_0 = {
		X1 = arg_5_1.x - var_0_1.RANDOM_RANGE,
		X2 = arg_5_1.x + var_0_1.RANDOM_RANGE,
		Z1 = arg_5_1.z - var_0_1.RANDOM_RANGE,
		Z2 = arg_5_1.z + var_0_1.RANDOM_RANGE
	}

	arg_5_0._referencePoint = var_0_0.Battle.BattleFormulas.RandomPos(var_5_0)

def var_0_1.IsFinish(arg_6_0, arg_6_1):
	return (arg_6_0._referencePoint - arg_6_1.GetFleetPosition()).magnitude < var_0_1.VALVE

def var_0_1.GetOutput(arg_7_0, arg_7_1):
	local var_7_0 = (arg_7_0._referencePoint - arg_7_1.GetFleetPosition()).normalized

	return var_7_0.x, var_7_0.z

def var_0_1.NextState(arg_8_0):
	return var_0_0.Battle.CardPuzzleMoveState.STATE_STAY
