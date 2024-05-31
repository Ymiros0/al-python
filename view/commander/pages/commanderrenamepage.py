local var_0_0 = class("CommanderRenamePage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CommandeRenameUI"

def var_0_0.OnInit(arg_2_0):
	onButton(arg_2_0, arg_2_0._tf.Find("frame/close_btn"), function()
		arg_2_0.Hide(), SFX_PANEL)
	onButton(arg_2_0, arg_2_0._tf, function()
		arg_2_0.Hide(), SFX_PANEL)
	onButton(arg_2_0, arg_2_0._tf.Find("frame/cancel_btn"), function()
		arg_2_0.Hide(), SFX_PANEL)

	arg_2_0.input = findTF(arg_2_0._tf, "frame/bg/content/input")
	arg_2_0.confirmBtn = arg_2_0._tf.Find("frame/confirm_btn")

	setText(arg_2_0.findTF("frame/bg/content/label"), i18n("commander_rename_tip"))

def var_0_0.Show(arg_6_0, arg_6_1):
	arg_6_0.isShowMsgBox = True

	setActive(arg_6_0._tf, True)
	arg_6_0._tf.SetAsLastSibling()
	setInputText(arg_6_0.input, "")
	onButton(arg_6_0, arg_6_0.confirmBtn, function()
		local var_7_0 = getInputText(arg_6_0.input)

		if not var_7_0 or var_7_0 == "":
			return

		arg_6_0.emit(CommanderCatMediator.RENAME, arg_6_1.id, var_7_0)
		arg_6_0.Hide(), SFX_PANEL)
	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf, False, {
		weight = LayerWeightConst.SECOND_LAYER
	})

def var_0_0.Hide(arg_8_0):
	arg_8_0.isShowMsgBox = None

	setActive(arg_8_0._tf, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_8_0._tf, arg_8_0._parentTf)

def var_0_0.OnDestroy(arg_9_0):
	if arg_9_0.isShowMsgBox:
		arg_9_0.Hide()

return var_0_0
