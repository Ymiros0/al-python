local var_0_0 = class("SettingsMsgBosPage", import("..base.BaseSubView"))

var_0_0.ALIGN_CENTER = 0
var_0_0.ALIGN_LEFT = 1

def var_0_0.getUIName(arg_1_0):
	return "SetttingMsgbox"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.closeBtn = arg_2_0.findTF("window/top/btnBack")
	arg_2_0.textTr = arg_2_0.findTF("window/view/content/Text")
	arg_2_0.text = arg_2_0.textTr.GetComponent(typeof(Text))
	arg_2_0.scrollrect = arg_2_0.findTF("window/view/content")

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_6_0, arg_6_1, arg_6_2):
	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf)
	var_0_0.super.Show(arg_6_0)

	arg_6_0.text.text = arg_6_1

	arg_6_0.UpdateLayout(arg_6_2 or var_0_0.ALIGN_CENTER)

	arg_6_0.scrollrect.GetComponent(typeof(ScrollRect)).verticalNormalizedPosition = 1

	arg_6_0._tf.SetAsLastSibling()

def var_0_0.UpdateLayout(arg_7_0, arg_7_1):
	local var_7_0 = Vector2(0.5, 0.5)
	local var_7_1 = TextAnchor.MiddleCenter

	if arg_7_1 == var_0_0.ALIGN_LEFT:
		var_7_0 = Vector2(0, 1)
		var_7_1 = TextAnchor.UpperLeft

	arg_7_0.textTr.pivot = var_7_0
	arg_7_0.text.alignment = var_7_1

	local var_7_2 = arg_7_0.textTr.GetComponent(typeof(LayoutElement)).preferredWidth

	setAnchoredPosition(arg_7_0.textTr, {
		x = var_7_2 * (var_7_0.x - 0.5)
	})

def var_0_0.Hide(arg_8_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_8_0._tf, arg_8_0._parentTf)
	var_0_0.super.Hide(arg_8_0)

	arg_8_0.text.text = ""

def var_0_0.OnDestroy(arg_9_0):
	arg_9_0.Hide()

return var_0_0
