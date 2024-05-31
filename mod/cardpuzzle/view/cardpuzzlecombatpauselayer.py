local var_0_0 = class("CardPuzzleCombatPauseLayer", BaseUI)

def var_0_0.getUIName(arg_1_0):
	return "CardTowerCombatPause"

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)
	onButton(arg_2_0, arg_2_0.findTF("btn_quit"), function()
		arg_2_0.emit(CardPuzzleCombatPauseMediator.QUIT_COMBAT, {}), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.findTF("btn_resume"), function()
		arg_2_0.OnBackward(), SFX_PANEL)

def var_0_0.OnBackward(arg_5_0):
	arg_5_0.emit(CardPuzzleCombatPauseMediator.RESUME_COMBAT)
	arg_5_0.closeView()

	return True

def var_0_0.willExit(arg_6_0):
	return

return var_0_0
