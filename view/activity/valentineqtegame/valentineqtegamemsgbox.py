local var_0_0 = class("ValentineQteGameMsgBox")

var_0_0.EXIT_TXT = 1
var_0_0.PAUSE_TXT = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._tf = arg_1_1

	arg_1_0.OnInit()
	arg_1_0.OnRegister()

def var_0_0.OnInit(arg_2_0):
	arg_2_0.confirmBtn = arg_2_0._tf.Find("frame/btns/confirm_btn")
	arg_2_0.cancelBtn = arg_2_0._tf.Find("frame/btns/cancel_btn")
	arg_2_0.texts = {
		[var_0_0.EXIT_TXT] = arg_2_0._tf.Find("frame/exit"),
		[var_0_0.PAUSE_TXT] = arg_2_0._tf.Find("frame/puase")
	}

def var_0_0.OnRegister(arg_3_0):
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if arg_3_0.settings.onYes:
			arg_3_0.settings.onYes()

		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		if arg_3_0.settings.onNo:
			arg_3_0.settings.onNo()

		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_6_0, arg_6_1):
	arg_6_0.settings = arg_6_1

	setActive(arg_6_0._tf, True)

	for iter_6_0, iter_6_1 in pairs(arg_6_0.texts):
		setActive(iter_6_1, False)

	if arg_6_0.texts[arg_6_1.content]:
		setActive(arg_6_0.texts[arg_6_1.content], True)

	setActive(arg_6_0.cancelBtn, not arg_6_1.noNo)

def var_0_0.Hide(arg_7_0):
	setActive(arg_7_0._tf, False)

	arg_7_0.settings = None

def var_0_0.Destroy(arg_8_0):
	pg.DelegateInfo.Dispose(arg_8_0)
	arg_8_0.Hide()

return var_0_0
