local var_0_0 = class("BackYardThemeTemplateMsgBox", import("....base.BaseSubView"))

var_0_0.TYPE_TEXT = 1
var_0_0.TYPE_IMAGE = 2

def var_0_0.getUIName(arg_1_0):
	return "BackYardThemeTemplateMsgBox"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.frame = arg_2_0.findTF("window1")
	arg_2_0.content = arg_2_0.findTF("window1/content").GetComponent(typeof(Text))
	arg_2_0.frame1 = arg_2_0.findTF("window2")
	arg_2_0.content1 = arg_2_0.findTF("window2/content").GetComponent(typeof(Text))
	arg_2_0.icon = arg_2_0.findTF("window2/mask/Icon").GetComponent(typeof(RawImage))
	arg_2_0.cancelBtn = arg_2_0.findTF("btns/cancel")
	arg_2_0.cancelBtnTxt = arg_2_0.findTF("btns/cancel/Text").GetComponent(typeof(Text))
	arg_2_0.confirmBtn = arg_2_0.findTF("btns/confirm")
	arg_2_0.confirmBtnTxt = arg_2_0.findTF("btns/confirm/Text").GetComponent(typeof(Text))
	arg_2_0._parentTF = arg_2_0._tf.parent

	setText(arg_2_0.findTF("title"), i18n("words_information"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0.Hide()

		if arg_3_0.onCancel:
			arg_3_0.onCancel(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		arg_3_0.Hide()

		if arg_3_0.onYes:
			arg_3_0.onYes(), SFX_PANEL)

def var_0_0.SetUp(arg_7_0, arg_7_1):
	arg_7_0.onYes = arg_7_1.onYes
	arg_7_0.onCancel = arg_7_1.onCancel
	arg_7_0.cancelBtnTxt.text = arg_7_1.cancelTxt or i18n("word_cancel")
	arg_7_0.confirmBtnTxt.text = arg_7_1.confirmTxt or i18n("word_ok")

	local var_7_0 = arg_7_1.type or var_0_0.TYPE_TEXT

	if var_7_0 == var_0_0.TYPE_TEXT:
		arg_7_0.content.text = arg_7_1.content
	elif var_7_0 == var_0_0.TYPE_IMAGE:
		arg_7_0.content1.text = arg_7_1.content

		BackYardThemeTempalteUtil.GetNonCacheTexture(arg_7_1.srpiteName, arg_7_1.md5, function(arg_8_0)
			if not IsNil(arg_7_0.icon) and arg_8_0:
				arg_7_0.icon.texture = arg_8_0)

	setActive(arg_7_0.frame, var_7_0 == var_0_0.TYPE_TEXT)
	setActive(arg_7_0.frame1, var_7_0 == var_0_0.TYPE_IMAGE)
	setActive(arg_7_0.cancelBtn, not arg_7_1.hideNo)
	arg_7_0.Show()

def var_0_0.Show(arg_9_0):
	var_0_0.super.Show(arg_9_0)
	SetParent(arg_9_0._tf, pg.UIMgr.GetInstance().OverlayMain)

def var_0_0.Hide(arg_10_0):
	if not IsNil(arg_10_0.icon.texture):
		Object.Destroy(arg_10_0.icon.texture)

		arg_10_0.icon.texture = None

	var_0_0.super.Hide(arg_10_0)
	SetParent(arg_10_0._tf, arg_10_0._parentTF)

def var_0_0.OnDestroy(arg_11_0):
	arg_11_0.Hide()

return var_0_0
