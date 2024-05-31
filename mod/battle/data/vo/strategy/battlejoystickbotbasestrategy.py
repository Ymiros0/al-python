ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleJoyStickBotBaseStrategy = class("BattleJoyStickBotBaseStrategy")

local var_0_1 = var_0_0.Battle.BattleJoyStickBotBaseStrategy

var_0_1.__name = "BattleJoyStickBotBaseStrategy"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	arg_1_0._hrz = 0
	arg_1_0._vtc = 0
	arg_1_0._fleetVO = arg_1_1
	arg_1_0._motionVO = arg_1_1.GetMotion()

def var_0_1.GetStrategyType(arg_2_0):
	return None

def var_0_1.SetBoardBound(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
	arg_3_0._upperBound = arg_3_1
	arg_3_0._lowerBound = arg_3_2
	arg_3_0._leftBound = arg_3_3
	arg_3_0._rightBound = arg_3_4
	arg_3_0._totalWidth = arg_3_4 - arg_3_3
	arg_3_0._totalHeight = arg_3_1 - arg_3_2

def var_0_1.Input(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0._foeShipList = arg_4_1
	arg_4_0._foeAircraftList = arg_4_2

def var_0_1.Output(arg_5_0):
	arg_5_0.analysis()

	return arg_5_0._hrz, arg_5_0._vtc

def var_0_1.Dispose(arg_6_0):
	arg_6_0._foeShipList = None
	arg_6_0._foeAircraftList = None
	arg_6_0._motionVO = None

def var_0_1.analysis(arg_7_0):
	return

def var_0_1.getDirection(arg_8_0, arg_8_1):
	local var_8_0 = (arg_8_1 - arg_8_0).normalized

	return var_8_0.x, var_8_0.z
