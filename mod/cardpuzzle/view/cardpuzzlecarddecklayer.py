local var_0_0 = class("CardPuzzleCardDeckLayer", BaseUI)

def var_0_0.getUIName(arg_1_0):
	return "CardTowerCardDeckUI"

def var_0_0.isLayer(arg_2_0):
	return False

def var_0_0.init(arg_3_0):
	arg_3_0.cardListRect = arg_3_0.findTF("Container")
	arg_3_0.cardListComp = arg_3_0.cardListRect.GetComponent("LScrollRect")

	function arg_3_0.cardListComp.onUpdateItem(arg_4_0, arg_4_1)
		local var_4_0 = tf(arg_4_1).GetChild(0)
		local var_4_1 = CardPuzzleCardView.New(var_4_0)

		var_4_1.SetData(arg_3_0.cards[arg_4_0 + 1])
		var_4_1.UpdateView()
		onButton(arg_3_0, arg_4_1, function()
			arg_3_0.ShowCardDetail(arg_4_0), SFX_PANEL)

def var_0_0.ShowCardDetail(arg_6_0, arg_6_1):
	arg_6_0.emit(CardPuzzleCardDeckMediator.SHOW_CARD, {
		cardData = arg_6_0.cards[arg_6_1 + 1]
	})

def var_0_0.SetCards(arg_7_0, arg_7_1):
	arg_7_0.cards = arg_7_1

def var_0_0.didEnter(arg_8_0):
	arg_8_0.RefreshCards()

def var_0_0.RefreshCards(arg_9_0):
	arg_9_0.cardListComp.SetTotalCount(#arg_9_0.cards)

def var_0_0.OnBackward(arg_10_0):
	arg_10_0.closeView()

	return True

def var_0_0.willExit(arg_11_0):
	pg.m02.sendNotification(CardTowerStageMediator.CARDTOWER_STAGE_REMOVE_SUBVIEW, arg_11_0._tf)

return var_0_0
