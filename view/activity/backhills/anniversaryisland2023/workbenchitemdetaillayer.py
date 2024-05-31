local var_0_0 = class("WorkBenchItemDetailLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "WorkBenchItemDetailLayer"

def var_0_0.init(arg_2_0):
	arg_2_0.loader = AutoLoader.New()

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf.Find("BG"), function()
		arg_3_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0._tf.Find("Window/Close"), function()
		arg_3_0.onBackPressed(), SFX_CANCEL)
	arg_3_0.UpdateItemDetail()
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf, None, {
		weight = LayerWeightConst.SECOND_LAYER
	})

def var_0_0.UpdateItemDetail(arg_6_0):
	local var_6_0 = arg_6_0.contextData.material

	arg_6_0.UpdateItem(arg_6_0._tf.Find("Window/IconBG"), var_6_0)
	setText(arg_6_0._tf.Find("Window/Name"), var_6_0.GetName())
	setText(arg_6_0._tf.Find("Window/Description/Text"), var_6_0.GetDesc())

	local var_6_1 = var_6_0.GetSource()

	setText(arg_6_0._tf.Find("Window/Source"), var_6_1[1] or "")
	onButton(arg_6_0, arg_6_0._tf.Find("Window/Go"), function()
		arg_6_0.emit(GAME.WORKBENCH_ITEM_GO, var_6_0.GetConfigID()), SFX_PANEL)
	setActive(arg_6_0._tf.Find("Window/Go"), table.getCount(var_6_0.GetSource()) > 1)

local var_0_1 = "ui/AtelierCommonUI_atlas"

def var_0_0.UpdateItem(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = "icon_frame_" .. arg_8_2.GetRarity()

	arg_8_0.loader.GetSpriteQuiet(var_0_1, var_8_0, arg_8_1)
	arg_8_0.loader.GetSpriteQuiet(arg_8_2.GetIconPath(), "", arg_8_1.Find("Icon"))

	if not IsNil(arg_8_1.Find("Text")):
		setText(arg_8_1.Find("Text"), arg_8_2.count)

def var_0_0.willExit(arg_9_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_9_0._tf)
	arg_9_0.loader.Clear()

return var_0_0
