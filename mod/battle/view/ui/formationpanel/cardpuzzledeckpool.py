ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleCardPuzzleEvent

var_0_0.Battle.CardPuzzleDeckPool = class("CardPuzzleDeckPool")

local var_0_3 = var_0_0.Battle.CardPuzzleDeckPool

var_0_3.__name = "CardPuzzleDeckPool"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1

	arg_1_0.init()

def var_0_3.SetCardPuzzleComponent(arg_2_0, arg_2_1):
	arg_2_0._cardPuzzleInfo = arg_2_1
	arg_2_0._deck = arg_2_0._cardPuzzleInfo.GetDeck()

	arg_2_0._deck.RegisterEventListener(arg_2_0, var_0_2.UPDATE_CARDS, arg_2_0.onUpdateDeckCard)
	arg_2_0.onUpdateDeckCard()

def var_0_3.onUpdateDeckCard(arg_3_0, arg_3_1):
	setText(arg_3_0._deckCountLabel, arg_3_0._deck.GetLength())

def var_0_3.init(arg_4_0):
	var_0_0.EventListener.AttachEventListener(arg_4_0)

	arg_4_0._tf = arg_4_0._go.transform
	arg_4_0._deckCountLabel = arg_4_0._tf.Find("count/text")

	setText(arg_4_0._tf.Find("label"), i18n("card_puzzle_deck"))

def var_0_3.Dispose(arg_5_0):
	arg_5_0._deckCountLabel = None
	arg_5_0._tf = None
