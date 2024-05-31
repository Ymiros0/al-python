local var_0_0 = class("SixthAnniversaryIslandFlowerWindowLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "SixthAnniversaryIslandFlowerWindow"

def var_0_0.init(arg_2_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf)
	setText(arg_2_0._tf.Find("content/title/Text"), i18n("islandnode_tips7", arg_2_0.contextData.name))

	local var_2_0 = arg_2_0._tf.Find("content/main/content")

	arg_2_0.itemList = UIItemList.New(var_2_0, var_2_0.Find("icon"))

	arg_2_0.itemList.make(function(arg_3_0, arg_3_1, arg_3_2)
		arg_3_1 = arg_3_1 + 1

		if arg_3_0 == UIItemList.EventUpdate:
			updateDrop(arg_3_2.Find("IconTpl"), arg_2_0.contextData.awards[arg_3_1]))
	arg_2_0.itemList.align(#arg_2_0.contextData.awards)
	onButton(arg_2_0, arg_2_0._tf.Find("content/bottom/btn"), function()
		arg_2_0.closeView(), SFX_CANCEL)

def var_0_0.didEnter(arg_5_0):
	return

def var_0_0.willExit(arg_6_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_6_0._tf)

return var_0_0
