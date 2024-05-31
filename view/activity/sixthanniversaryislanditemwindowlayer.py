local var_0_0 = class("SixthAnniversaryIslandItemWindowLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "SixthAnniversaryIslandItemWindow"

def var_0_0.init(arg_2_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf)
	setText(arg_2_0._tf.Find("content/bottom/Text"), arg_2_0.contextData.text)
	onButton(arg_2_0, arg_2_0._tf.Find("bg"), function()
		arg_2_0.closeView(), SFX_CANCEL)

def var_0_0.didEnter(arg_4_0):
	local var_4_0 = arg_4_0.contextData.drop
	local var_4_1 = arg_4_0._tf.Find("content/main")
	local var_4_2 = var_4_0.count and {
		var_4_0.count,
		True
	} or {
		var_4_0.getOwnedCount()
	}
	local var_4_3, var_4_4 = unpack(var_4_2)

	setActive(var_4_1.Find("owner"), var_4_4)

	if var_4_4:
		setText(var_4_1.Find("owner"), i18n("word_own1") .. var_4_3)

	var_4_0.count = None

	updateDrop(var_4_1.Find("icon/IconTpl"), var_4_0)
	setText(var_4_1.Find("line/name"), var_4_0.getConfig("name"))
	setText(var_4_1.Find("line/content/Text"), var_4_0.desc or var_4_0.getConfig("desc"))

def var_0_0.willExit(arg_5_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_5_0._tf)

return var_0_0
