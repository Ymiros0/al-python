local var_0_0 = class("CommanderMsgBoxPage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CommanderMsgBoxUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.cancelBtn = arg_2_0._tf.Find("frame/cancel_btn")
	arg_2_0.text = arg_2_0._tf.Find("frame/bg/content/Text")
	arg_2_0.text1 = arg_2_0._tf.Find("frame/bg/content/Text1")
	arg_2_0.text2 = arg_2_0._tf.Find("frame/bg/content/Text2")
	arg_2_0.confirmBtn = arg_2_0._tf.Find("frame/confirm_btn")
	arg_2_0.closeBtn = arg_2_0._tf.Find("frame/close_btn")

	onButton(arg_2_0, arg_2_0._tf, function()
		arg_2_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_4_0, arg_4_1):
	var_0_0.super.Show(arg_4_0)

	if arg_4_1.content1:
		setText(arg_4_0.text1, arg_4_1.content)
		setText(arg_4_0.text2, arg_4_1.content1)
	elif arg_4_1.content:
		setText(arg_4_0.text, setColorStr(arg_4_1.content, "#847D7B"))

	arg_4_0.layer = arg_4_1.layer

	onButton(arg_4_0, arg_4_0.cancelBtn, function()
		arg_4_0.Hide()

		if arg_4_1.onNo:
			arg_4_1.onNo(), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.confirmBtn, function()
		arg_4_0.Hide()

		if arg_4_1.onYes:
			arg_4_1.onYes(), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.closeBtn, function()
		arg_4_0.Hide()

		if arg_4_1.onClose:
			arg_4_1.onClose(), SFX_PANEL)

	if arg_4_1.onShow:
		arg_4_1.onShow()

	arg_4_0._tf.SetAsLastSibling()
	pg.UIMgr.GetInstance().BlurPanel(arg_4_0._tf, False, {
		weight = arg_4_0.layer or LayerWeightConst.SECOND_LAYER
	})

def var_0_0.Hide(arg_8_0):
	var_0_0.super.Hide(arg_8_0)
	setText(arg_8_0.text, "")
	setText(arg_8_0.text1, "")
	setText(arg_8_0.text2, "")
	pg.UIMgr.GetInstance().UnblurPanel(arg_8_0._tf, arg_8_0._parentTf)

def var_0_0.OnDestroy(arg_9_0):
	arg_9_0.Hide()

return var_0_0
