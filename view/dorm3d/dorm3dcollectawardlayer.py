local var_0_0 = class("Dorm3dCollectAwardLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "Dorm3dCollectAwardUI"

def var_0_0.preload(arg_2_0, arg_2_1):
	local var_2_0 = pg.dorm3d_collection_template[arg_2_0.contextData.itemId]

	GetSpriteFromAtlasAsync("dorm3dcollection/" .. var_2_0.model, "", function(arg_3_0)
		arg_2_0.iconSprite = arg_3_0

		arg_2_1())

def var_0_0.init(arg_4_0):
	onButton(arg_4_0, arg_4_0._tf.Find("bg"), function()
		arg_4_0.closeView(), SFX_CANCEL)
	pg.UIMgr.GetInstance().BlurPanel(arg_4_0._tf, False, {
		weight = LayerWeightConst.THIRD_LAYER
	})

def var_0_0.didEnter(arg_6_0):
	local var_6_0 = pg.dorm3d_collection_template[arg_6_0.contextData.itemId]

	setText(arg_6_0._tf.Find("panel/name/Text"), var_6_0.name)
	setText(arg_6_0._tf.Find("panel/desc"), var_6_0.desc)

	local var_6_1 = pg.dorm3d_favor_trigger[var_6_0.award].num

	setText(arg_6_0._tf.Find("panel/favor/Image/Text"), string.format("favor plus.%d", var_6_1))
	setImageSprite(arg_6_0._tf.Find("panel/icon"), arg_6_0.iconSprite, True)

def var_0_0.willExit(arg_7_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_7_0._tf)

return var_0_0
