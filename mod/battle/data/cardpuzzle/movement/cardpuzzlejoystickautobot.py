ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.CardPuzzleJoyStickAutoBot = class("CardPuzzleJoyStickAutoBot")

local var_0_1 = var_0_0.Battle.CardPuzzleJoyStickAutoBot

var_0_1.__name = "CardPuzzleJoyStickAutoBot"
var_0_1.RANDOM = "RandomStrategy"
var_0_1.MOVE_TO = "RandomStrategy"
var_0_1.CARD_PUZZLE_CONTROL = "CardPuzzleControlStrategy"

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._dataProxy = arg_1_1
	arg_1_0._fleetVO = arg_1_2

	arg_1_0.init()

def var_0_1.UpdateFleetArea(arg_2_0):
	if arg_2_0._strategy:
		arg_2_0._strategy.SetBoardBound(arg_2_0._fleetVO.GetFleetBound())

def var_0_1.FleetFormationUpdate(arg_3_0):
	return

def var_0_1.SetActive(arg_4_0, arg_4_1):
	arg_4_0._active = arg_4_1

	if arg_4_1:
		local function var_4_0()
			return arg_4_0._strategy.Output()

		arg_4_0._fleetVO.SetMotionSource(var_4_0)
	else
		arg_4_0._fleetVO.SetMotionSource()

def var_0_1.SwitchStrategy(arg_6_0, arg_6_1):
	if arg_6_0._strategy:
		arg_6_0._strategy.Dispose()

	arg_6_1 = arg_6_1 or var_0_1.CARD_PUZZLE_CONTROL
	arg_6_0._strategy = var_0_0.Battle[arg_6_1].New(arg_6_0._fleetVO)

	arg_6_0.UpdateFleetArea()
	arg_6_0._strategy.Input(arg_6_0._dataProxy.GetFoeShipList(), arg_6_0._dataProxy.GetFoeAircraftList())

def var_0_1.init(arg_7_0):
	arg_7_0.SwitchStrategy()

def var_0_1.Dispose(arg_8_0):
	if arg_8_0._strategy:
		arg_8_0._strategy.Dispose()

	arg_8_0._dataProxy = None
