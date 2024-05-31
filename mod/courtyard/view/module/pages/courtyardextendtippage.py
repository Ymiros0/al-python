local var_0_0 = class("CourtYardExtendTipPage", import(".CourtYardBaseSubPage"))

def var_0_0.getUIName(arg_1_0):
	return "CourtYardExtendTipUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.valueTxt = findTF(arg_2_0._tf, "frame/tip_2/value_bg/Text")
	arg_2_0.text1 = findTF(arg_2_0._tf, "frame/tip_1/text_1")
	arg_2_0.text2 = findTF(arg_2_0._tf, "frame/tip_1/value_bg/Text")
	arg_2_0.text3 = findTF(arg_2_0._tf, "frame/tip_1/text_2")
	arg_2_0.text4 = findTF(arg_2_0._tf, "frame/tip_2/text_1")
	arg_2_0.text5 = findTF(arg_2_0._tf, "frame/tip_2/text_2")
	arg_2_0.itemTF = findTF(arg_2_0._tf, "frame")
	arg_2_0.okBtn = findTF(arg_2_0._tf, "frame/ok_btn")
	arg_2_0.cancelBtn = findTF(arg_2_0._tf, "frame/cancel_btn")
	arg_2_0.closeBtn = findTF(arg_2_0._tf, "frame/close")
	arg_2_0._parent = arg_2_0._tf.parent

	setText(arg_2_0.okBtn.Find("Text"), i18n("word_ok"))
	setText(arg_2_0.cancelBtn.Find("Text"), i18n("word_cancel"))
	setText(arg_2_0.findTF("frame/tip_1/text_1"), i18n("backyard_extend_tip_1"))
	setText(arg_2_0.findTF("frame/tip_1/text_2"), i18n("backyard_extend_tip_2"))
	setText(arg_2_0.findTF("frame/tip_2/text_1"), i18n("backyard_extend_tip_3"))
	setText(arg_2_0.findTF("frame/tip_2/text_2"), i18n("backyard_extend_tip_4"))
	setText(arg_2_0.findTF("frame/title"), i18n("words_information"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.okBtn, function()
		arg_3_0.Emit("Extend")
		arg_3_0.Hide(), SFX_CONFIRM)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0.Hide(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_CANCEL)

def var_0_0.Show(arg_8_0):
	local var_8_0 = getProxy(BagProxy).getItemById(ITEM_BACKYARD_AREA_EXTEND) or Item.New({
		count = 0,
		id = ITEM_BACKYARD_AREA_EXTEND
	})
	local var_8_1 = i18n("backyard_extendArea_tip", 1, var_8_0.count)
	local var_8_2 = {}

	for iter_8_0, iter_8_1 in ipairs(string.split(var_8_1, "||")):
		var_8_2["text" .. iter_8_0] = iter_8_1

	setActive(arg_8_0._tf, True)

	local var_8_3 = {
		type = DROP_TYPE_ITEM,
		id = var_8_0.id
	}

	setText(arg_8_0.text1, var_8_2.text1)
	setText(arg_8_0.text2, setColorStr(var_8_2.text2, "#72bc42"))
	setText(arg_8_0.text3, var_8_2.text3)
	setText(arg_8_0.text4, var_8_2.text4)

	local var_8_4 = tonumber(var_8_0.count) <= 0 and setColorStr(var_8_0.count, COLOR_RED) or setColorStr(var_8_0.count, "#72bc42")

	setText(arg_8_0.valueTxt, var_8_4)
	setText(arg_8_0.text5, var_8_2.text6)
	updateDrop(arg_8_0.itemTF, var_8_3)
	pg.UIMgr.GetInstance().OverlayPanel(arg_8_0._tf)

	arg_8_0.showing = True

def var_0_0.Hide(arg_9_0):
	if arg_9_0.showing == True:
		arg_9_0.showing = False

		setActive(arg_9_0._tf, False)
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_9_0._tf, arg_9_0._parent)

def var_0_0.OnDestroy(arg_10_0):
	arg_10_0.Hide()

return var_0_0
