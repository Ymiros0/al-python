local var_0_0 = class("PipeGamingUI")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	var_0_1 = PipeGameVo
	arg_1_0._gameUI = findTF(arg_1_0._tf, "ui/gamingUI")
	arg_1_0.btnBack = findTF(arg_1_0._gameUI, "back")
	arg_1_0.btnPause = findTF(arg_1_0._gameUI, "pause")
	arg_1_0.gameTime = findTF(arg_1_0._gameUI, "time")

	onButton(arg_1_0._event, arg_1_0.btnBack, function()
		if not var_0_1.startSettlement:
			arg_1_0._event.emit(PipeGameEvent.PAUSE_GAME, True)
			arg_1_0._event.emit(PipeGameEvent.OPEN_LEVEL_UI), SFX_CONFIRM)
	onButton(arg_1_0._event, arg_1_0.btnPause, function()
		if not var_0_1.startSettlement:
			arg_1_0._event.emit(PipeGameEvent.PAUSE_GAME, True)
			arg_1_0._event.emit(PipeGameEvent.OPEN_PAUSE_UI), SFX_CONFIRM)

def var_0_0.show(arg_4_0, arg_4_1):
	setActive(arg_4_0._gameUI, arg_4_1)

def var_0_0.update(arg_5_0):
	return

def var_0_0.start(arg_6_0):
	arg_6_0.subGameStepTime = 0

	arg_6_0.show(True)

def var_0_0.addScore(arg_7_0, arg_7_1):
	return

def var_0_0.step(arg_8_0, arg_8_1):
	local var_8_0 = var_0_1.gameDragTime

	setText(arg_8_0.gameTime, math.floor(var_8_0))

	if var_8_0 <= 0:
		arg_8_0.show(False)
	elif var_0_1.startSettlement and isActive(arg_8_0._gameUI):
		arg_8_0.show(False)

def var_0_0.press(arg_9_0, arg_9_1, arg_9_2):
	return

return var_0_0
