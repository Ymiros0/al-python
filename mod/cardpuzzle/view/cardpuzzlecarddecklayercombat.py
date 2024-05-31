local var_0_0 = class("CardTowerCardDeckLayerCombat", CardPuzzleCardDeckLayer)

def var_0_0.getUIName(arg_1_0):
	return "CardTowerCardDeckCombat"

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)

	arg_2_0.labelCH = arg_2_0.findTF("label/ch")
	arg_2_0.labelEN = arg_2_0.findTF("label/en")

	setText(arg_2_0.labelEN, i18n("card_battle_card details"))

	arg_2_0.switchToggle = arg_2_0.findTF("switch_toggle/toggle")

	setText(arg_2_0.findTF("switch_toggle/toggle/hand"), i18n("card_battle_card details_switchto_deck"))
	setText(arg_2_0.findTF("switch_toggle/toggle/deck"), i18n("card_battle_card details_switchto_hand"))
	onToggle(arg_2_0, arg_2_0.switchToggle, function(arg_3_0)
		if arg_3_0:
			arg_2_0.showHand()
		else
			arg_2_0.showDeck())

	arg_2_0.empty = arg_2_0.findTF("empty")

	setText(arg_2_0.findTF("empty/label_en"), i18n("card_battle_card_empty_en"))
	setText(arg_2_0.findTF("empty/label_ch"), i18n("card_battle_card_empty_ch"))
	onButton(arg_2_0, arg_2_0.findTF("backBtn"), function()
		arg_2_0.OnBackward(), SFX_PANEL)

def var_0_0.showHand(arg_5_0):
	setText(arg_5_0.labelCH, i18n("card_battle_card details_hand"))

	arg_5_0.cards = arg_5_0.hand

	arg_5_0.RefreshCards()

def var_0_0.showDeck(arg_6_0):
	setText(arg_6_0.labelCH, i18n("card_battle_card details_deck"))

	arg_6_0.cards = arg_6_0.deck

	arg_6_0.RefreshCards()

def var_0_0.didEnter(arg_7_0):
	triggerToggle(arg_7_0.switchToggle, False)

def var_0_0.SetCards(arg_8_0, arg_8_1, arg_8_2):
	arg_8_0.deck = arg_8_1
	arg_8_0.hand = arg_8_2

def var_0_0.RefreshCards(arg_9_0):
	setActive(arg_9_0.empty, #arg_9_0.cards == 0)
	arg_9_0.cardListComp.SetTotalCount(#arg_9_0.cards)

def var_0_0.OnBackward(arg_10_0):
	arg_10_0.emit(CardPuzzleCardDeckMediator.CLOSE_LAYER)

	return var_0_0.super.OnBackward(arg_10_0)

def var_0_0.willExit(arg_11_0):
	return

return var_0_0
