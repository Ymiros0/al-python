local var_0_0 = class("AttireExpireDisplayPage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "AttireOverDueUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.uilist = UIItemList.New(arg_2_0.findTF("window/sliders/scrollrect/content"), arg_2_0.findTF("window/sliders/scrollrect/content/tpl"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("window/confirm_btn"), function()
		arg_3_0.Hide(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("window/top/btnBack"), function()
		arg_3_0.Hide(), SFX_CANCEL)

def var_0_0.Show(arg_7_0, arg_7_1):
	var_0_0.super.Show(arg_7_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_7_0._tf, False, {
		weight = LayerWeightConst.SECOND_LAYER
	})
	arg_7_0.Display(arg_7_1)

def var_0_0.Display(arg_8_0, arg_8_1):
	arg_8_0.uilist.make(function(arg_9_0, arg_9_1, arg_9_2)
		if arg_9_0 == UIItemList.EventUpdate:
			local var_9_0 = arg_8_1[arg_9_1 + 1]

			updateDrop(arg_9_2, {
				count = 1,
				id = var_9_0.getConfig("id"),
				type = var_9_0.getDropType()
			}))
	arg_8_0.uilist.align(#arg_8_1)

def var_0_0.OnDestroy(arg_10_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_10_0._tf, pg.UIMgr.GetInstance()._normalUIMain)

return var_0_0
