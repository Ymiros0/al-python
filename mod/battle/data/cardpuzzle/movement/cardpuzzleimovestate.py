ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.CardPuzzleMoveState

var_0_0.Battle.CardPuzzleIMoveState = class("CardPuzzleIMoveState")

local var_0_2 = var_0_0.Battle.CardPuzzleIMoveState

var_0_2.__name = "CardPuzzleIMoveState"
var_0_2.ADD_STATE_TABLE = {
	[var_0_1.STATE_STAY] = "AddStayState",
	[var_0_1.STATE_RANDOM] = "AddRandomState",
	[var_0_1.STATE_MOVE] = "AddMoveToState"
}

def var_0_2.Ctor(arg_1_0):
	arg_1_0._hrz = 0
	arg_1_0._vtc = 0
	arg_1_0._timeStamp = 0

def var_0_2.AddMoveToState(arg_2_0, arg_2_1):
	return

def var_0_2.AddRandomState(arg_3_0, arg_3_1):
	return

def var_0_2.AddStayState(arg_4_0, arg_4_1):
	return

def var_0_2.IsFinish(arg_5_0, arg_5_1):
	return

def var_0_2.Update(arg_6_0):
	arg_6_0._currentTime = pg.TimeMgr.GetInstance().GetCombatTime()

def var_0_2.GetOutput(arg_7_0, arg_7_1):
	return arg_7_0._hrz, arg_7_0._vtc

def var_0_2.IntputReferencePoint(arg_8_0, arg_8_1):
	arg_8_0._referencePoint = arg_8_1

def var_0_2.NextState(arg_9_0):
	return
