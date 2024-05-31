local var_0_0 = class("BuildShipHelpWindow", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "BuildShipHelpWindowUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.shipListTF = arg_2_0.findTF("window/list/scrollview/list", arg_2_0._tf)
	arg_2_0.shipListTpl = arg_2_0.findTF("window/list/scrollview/item", arg_2_0._tf)

	setActive(arg_2_0.shipListTpl, False)

	arg_2_0.tipListTF = arg_2_0.findTF("window/rateList/scrollview/list", arg_2_0._tf)
	arg_2_0.tipListTpl = arg_2_0.findTF("window/rateList/scrollview/item", arg_2_0._tf)

	setText(arg_2_0.findTF("window/confirm_btn/Image/Image (1)"), i18n("text_confirm"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("window/close_btn", arg_3_0._tf), function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("window/confirm_btn", arg_3_0._tf), function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	pg.UIMgr.GetInstance().BlurPanel(arg_7_0._tf, False, {
		weight = LayerWeightConst.TOP_LAYER
	})

	arg_7_0.isSupport = arg_7_2 == "support"

	if arg_7_0.isSupport:
		setText(arg_7_0.findTF("window/rateList/title/Text"), i18n("support_rate_title"))
	else
		setText(arg_7_0.findTF("window/rateList/title/Text"), i18n("build_rate_title"))

	arg_7_0.OnShow(arg_7_1, arg_7_3)
	setActiveViaLayer(arg_7_0._tf, True)

def var_0_0.OnShow(arg_8_0, arg_8_1, arg_8_2):
	arg_8_0.showing = True

	local var_8_0 = arg_8_1
	local var_8_1 = arg_8_0.shipListTF.childCount

	for iter_8_0 = 1, var_8_1:
		local var_8_2 = arg_8_0.shipListTF.GetChild(iter_8_0 - 1)

		if var_8_2:
			setActive(var_8_2, False)

	local var_8_3 = arg_8_0.tipListTF.childCount

	for iter_8_1 = 1, var_8_3:
		local var_8_4 = arg_8_0.tipListTF.GetChild(iter_8_1 - 1)

		if var_8_4:
			setActive(var_8_4, False)

	local var_8_5 = getProxy(ActivityProxy)
	local var_8_6

	if not arg_8_0.isSupport:
		if arg_8_2:
			var_8_6 = var_8_5.getBuildActivityCfgByID(var_8_0.id)
		else
			var_8_6 = var_8_5.getNoneActBuildActivityCfgByID(var_8_0.id)

	local var_8_7 = var_8_6 and var_8_6.rate_tip or var_8_0.rate_tip

	for iter_8_2 = 1, #var_8_7:
		local var_8_8

		if iter_8_2 <= var_8_3:
			var_8_8 = arg_8_0.tipListTF.GetChild(iter_8_2 - 1)
		else
			var_8_8 = cloneTplTo(arg_8_0.tipListTpl, arg_8_0.tipListTF)

		if var_8_8:
			setActive(var_8_8, True)
			setText(var_8_8, HXSet.hxLan(var_8_7[iter_8_2]))

def var_0_0.Hide(arg_9_0):
	arg_9_0.showing = False

	setActiveViaLayer(arg_9_0._tf, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_9_0._tf, arg_9_0._tf)

def var_0_0.isShowing(arg_10_0):
	return arg_10_0.showing

def var_0_0.OnDestroy(arg_11_0):
	return

return var_0_0
