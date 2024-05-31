local var_0_0 = class("CardPuzzleRelicDetailLayer", BaseUI)

def var_0_0.getUIName(arg_1_0):
	return "CardTowerGiftDetailUI"

def var_0_0.init(arg_2_0):
	return

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("BG"), function()
		arg_3_0.closeView(), SFX_CANCEL)

	local var_3_0 = arg_3_0.contextData.giftData

	setImageSprite(arg_3_0._tf.Find("Gift/Icon"), LoadSprite(var_3_0.GetIconPath(), ""))
	setText(arg_3_0._tf.Find("Gift/Name"), var_3_0.GetName())
	setText(arg_3_0._tf.Find("Gift/Desc"), var_3_0.GetDesc())
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf, None, {})

def var_0_0.willExit(arg_5_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_5_0._tf)

return var_0_0
