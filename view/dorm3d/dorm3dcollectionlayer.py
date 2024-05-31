local var_0_0 = class("Dorm3dCollectionLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "Dorm3dCollectionUI"

def var_0_0.SetApartment(arg_2_0, arg_2_1):
	arg_2_0.contextData.apartment = arg_2_1

def var_0_0.init(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf.Find("bg"), function()
		arg_3_0.closeView(), SFX_PANEL)

	local var_3_0 = arg_3_0._tf.Find("window")

	eachChild(var_3_0.Find("toggles"), function(arg_5_0)
		onToggle(arg_3_0, arg_5_0, function(arg_6_0)
			if arg_6_0:
				arg_3_0.SetPage(arg_5_0.name), SFX_PANEL))

	local var_3_1 = var_3_0.Find("content")

	arg_3_0.memoryView = Dorm3dMemorySubView.New(None, arg_3_0.event, arg_3_0.contextData)

	arg_3_0.memoryView.SetExtra(var_3_1.Find("memory"))

	arg_3_0.collectItemView = Dorm3dCollectionItemSubView.New(None, arg_3_0.event, arg_3_0.contextData)

	arg_3_0.collectItemView.SetExtra(var_3_1.Find("item"))
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf, False, {
		weight = LayerWeightConst.SECOND_LAYER
	})

def var_0_0.SetPage(arg_7_0, arg_7_1):
	for iter_7_0, iter_7_1 in pairs({
		memory = arg_7_0.memoryView,
		item = arg_7_0.collectItemView
	}):
		if iter_7_0 == arg_7_1:
			iter_7_1.ExecuteAction("Show")
		elif iter_7_1.isShowing():
			iter_7_1.Hide()

def var_0_0.didEnter(arg_8_0):
	triggerToggle(arg_8_0._tf.Find("window/toggles/memory"), True)

def var_0_0.onBackPressed(arg_9_0):
	var_0_0.super.onBackPressed(arg_9_0)

def var_0_0.willExit(arg_10_0):
	arg_10_0.memoryView.Destroy()
	arg_10_0.collectItemView.Destroy()
	pg.UIMgr.GetInstance().UnblurPanel(arg_10_0._tf)

return var_0_0
