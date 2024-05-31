local var_0_0 = class("PlayerVitaeAddCard", import(".PlayerVitaeBaseCard"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.line1 = arg_1_0._tf.Find("line1")
	arg_1_0.line2 = arg_1_0._tf.Find("line2")
	arg_1_0.txt = arg_1_0._tf.Find("Text")

	onButton(arg_1_0, arg_1_0._tf, function()
		if arg_1_0.inEdit:
			return

		if not arg_1_0.canCilick:
			return

		arg_1_0.emit(PlayerVitaeMediator.CHANGE_PAINT, None), SFX_PANEL)

def var_0_0.OnUpdate(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
	local var_3_0 = arg_3_4 == PlayerVitaeShipsPage.RANDOM_FLAG_SHIP_PAGE

	arg_3_0.canCilick = not var_3_0

	setActive(arg_3_0.line1, not var_3_0)
	setActive(arg_3_0.line2, not var_3_0)
	setActive(arg_3_0.txt, not var_3_0)

def var_0_0.EditCard(arg_4_0, arg_4_1):
	arg_4_0.inEdit = arg_4_1

	setActive(arg_4_0.mask, arg_4_1)

def var_0_0.Disable(arg_5_0):
	var_0_0.super.Disable(arg_5_0)
	arg_5_0.EditCard(False)

def var_0_0.OnDispose(arg_6_0):
	arg_6_0.Disable()

return var_0_0
