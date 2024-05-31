local var_0_0 = class("CrusingWindowLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "CrusingWindowUI"

def var_0_0.preload(arg_2_0, arg_2_1):
	local var_2_0 = getProxy(ActivityProxy).getAliveActivityByType(ActivityConst.ACTIVITY_TYPE_PT_CRUSING)

	GetSpriteFromAtlasAsync("crusingwindow/" .. var_2_0.getConfig("config_client").map_name, "", function(arg_3_0)
		arg_2_0.windowSprite = arg_3_0

		arg_2_1())

def var_0_0.init(arg_4_0):
	setImageSprite(arg_4_0._tf.Find("panel"), arg_4_0.windowSprite, True)

	arg_4_0.rtBg = arg_4_0._tf.Find("bg")
	arg_4_0.btnBack = arg_4_0._tf.Find("panel/btn_back")
	arg_4_0.btnGo = arg_4_0._tf.Find("panel/btn_go")
	arg_4_0.itemContent = arg_4_0._tf.Find("panel/content")

	local var_4_0 = getProxy(ActivityProxy).getAliveActivityByType(ActivityConst.ACTIVITY_TYPE_PT_CRUSING).getConfig("config_client").equip_skin or {}

	arg_4_0.itemList = UIItemList.New(arg_4_0.itemContent, arg_4_0.itemContent.GetChild(0))

	arg_4_0.itemList.make(function(arg_5_0, arg_5_1, arg_5_2)
		arg_5_1 = arg_5_1 + 1

		if arg_5_0 == UIItemList.EventUpdate:
			local var_5_0 = {}

			var_5_0.type, var_5_0.id, var_5_0.count = unpack(var_4_0[arg_5_1])

			updateDrop(arg_5_2, var_5_0)
			onButton(arg_4_0, arg_5_2, function()
				arg_4_0.emit(var_0_0.ON_DROP, var_5_0), SFX_PANEL))
	arg_4_0.itemList.align(#var_4_0)

def var_0_0.didEnter(arg_7_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_7_0._tf, False, {
		weight = LayerWeightConst.TOP_LAYER
	})
	onButton(arg_7_0, arg_7_0.rtBg, function()
		arg_7_0.closeView(), SFX_CANCEL)
	onButton(arg_7_0, arg_7_0.btnBack, function()
		arg_7_0.closeView(), SFX_CANCEL)
	onButton(arg_7_0, arg_7_0.btnGo, function()
		arg_7_0.emit(CrusingWindowMediator.GO_CRUSING), SFX_CONFIRM)

def var_0_0.willExit(arg_11_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_11_0._tf)

return var_0_0
