local var_0_0 = class("CardPuzzleRelicDeckLayerCombat", CardPuzzleRelicDeckLayer)

def var_0_0.getUIName(arg_1_0):
	return "CardTowerGiftDeckCombat"

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)
	onButton(arg_2_0, arg_2_0.findTF("backBtn"), function()
		arg_2_0.OnBackward(), SFX_PANEL)

def var_0_0.OnBackward(arg_4_0):
	arg_4_0.emit(CardPuzzleCardDeckMediator.CLOSE_LAYER)

	return var_0_0.super.OnBackward(arg_4_0)

def var_0_0.willExit(arg_5_0):
	return

return var_0_0
