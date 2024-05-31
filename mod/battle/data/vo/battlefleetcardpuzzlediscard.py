ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = var_0_0.Battle.BattleCardPuzzleEvent
local var_0_4 = var_0_0.Battle.BattleFormulas
local var_0_5 = var_0_0.Battle.BattleConst
local var_0_6 = var_0_0.Battle.BattleConfig
local var_0_7 = var_0_0.Battle.BattleAttr
local var_0_8 = var_0_0.Battle.BattleDataFunction
local var_0_9 = var_0_0.Battle.BattleAttr
local var_0_10 = class("BattleFleetCardPuzzleDiscard")

var_0_0.Battle.BattleFleetCardPuzzleDiscard = var_0_10
var_0_10.__name = "BattleFleetCardPuzzleDiscard"

def var_0_10.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._cardPuzzleComponent = arg_1_1
	arg_1_0._indexID = arg_1_2

	arg_1_0.init()

def var_0_10.GetIndexID(arg_2_0):
	return arg_2_0._indexID

def var_0_10.Dispose(arg_3_0):
	return

def var_0_10.GetCardList(arg_4_0):
	return arg_4_0._discardList

def var_0_10.init(arg_5_0):
	arg_5_0._discardList = {}

	var_0_0.EventDispatcher.AttachEventDispatcher(arg_5_0)
	var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent.AttachCardManager(arg_5_0)
