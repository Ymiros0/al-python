ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleCardPuzzleEvent

var_0_0.Battle.CardPuzzleMovePile = class("CardPuzzleMovePile")

local var_0_3 = var_0_0.Battle.CardPuzzleMovePile

var_0_3.__name = "CardPuzzleMovePile"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1

	arg_1_0.init()

def var_0_3.SetCardPuzzleComponent(arg_2_0, arg_2_1):
	arg_2_0._cardPuzzleInfo = arg_2_1
	arg_2_0._moveDeck = arg_2_0._cardPuzzleInfo.GetMoveDeck()

	arg_2_0._moveDeck.RegisterEventListener(arg_2_0, var_0_2.UPDATE_CARDS, arg_2_0.onUpdateMoveCards)
	arg_2_0.onUpdateMoveCards()

def var_0_3.onUpdateMoveCards(arg_3_0, arg_3_1):
	setText(arg_3_0._moveCountLabel, "X" .. arg_3_0._moveDeck.GetLength())

def var_0_3.Update(arg_4_0):
	return

def var_0_3.init(arg_5_0):
	var_0_0.EventListener.AttachEventListener(arg_5_0)

	arg_5_0._tf = arg_5_0._go.transform
	arg_5_0._btnTF = arg_5_0._tf.Find("card")
	arg_5_0._moveCountLabel = arg_5_0._btnTF.Find("count")
	arg_5_0._moveProgress = arg_5_0._btnTF.Find("progress").GetComponent(typeof(Image))
	arg_5_0._moveProgress.fillAmount = 1

def var_0_3.updateMoveProgress(arg_6_0):
	local var_6_0 = arg_6_0._moveDeck.GetGeneratePorcess()

	if var_6_0 != arg_6_0._progressCache:
		arg_6_0._moveProgress.fillAmount = var_6_0

	arg_6_0._progressCache = var_6_0

def var_0_3.Dispose(arg_7_0):
	arg_7_0._moveCountLabel = None
	arg_7_0._moveProgress = None
	arg_7_0._btnTF = None
	arg_7_0._tf = None
