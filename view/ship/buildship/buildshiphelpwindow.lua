local var_0_0 = class("BuildShipHelpWindow", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "BuildShipHelpWindowUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.shipListTF = arg_2_0:findTF("window/list/scrollview/list", arg_2_0._tf)
	arg_2_0.shipListTpl = arg_2_0:findTF("window/list/scrollview/item", arg_2_0._tf)

	setActive(arg_2_0.shipListTpl, false)

	arg_2_0.tipListTF = arg_2_0:findTF("window/rateList/scrollview/list", arg_2_0._tf)
	arg_2_0.tipListTpl = arg_2_0:findTF("window/rateList/scrollview/item", arg_2_0._tf)

	setText(arg_2_0:findTF("window/confirm_btn/Image/Image (1)"), i18n("text_confirm"))
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0:findTF("window/close_btn", arg_3_0._tf), function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0:findTF("window/confirm_btn", arg_3_0._tf), function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
end

function var_0_0.Show(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
	pg.UIMgr.GetInstance():BlurPanel(arg_7_0._tf, false, {
		weight = LayerWeightConst.TOP_LAYER
	})

	arg_7_0.isSupport = arg_7_2 == "support"

	if arg_7_0.isSupport then
		setText(arg_7_0:findTF("window/rateList/title/Text"), i18n("support_rate_title"))
	else
		setText(arg_7_0:findTF("window/rateList/title/Text"), i18n("build_rate_title"))
	end

	arg_7_0:OnShow(arg_7_1, arg_7_3)
	setActiveViaLayer(arg_7_0._tf, true)
end

function var_0_0.OnShow(arg_8_0, arg_8_1, arg_8_2)
	arg_8_0.showing = true

	local var_8_0 = arg_8_1
	local var_8_1 = arg_8_0.shipListTF.childCount

	for iter_8_0 = 1, var_8_1 do
		local var_8_2 = arg_8_0.shipListTF:GetChild(iter_8_0 - 1)

		if var_8_2 then
			setActive(var_8_2, false)
		end
	end

	local var_8_3 = arg_8_0.tipListTF.childCount

	for iter_8_1 = 1, var_8_3 do
		local var_8_4 = arg_8_0.tipListTF:GetChild(iter_8_1 - 1)

		if var_8_4 then
			setActive(var_8_4, false)
		end
	end

	local var_8_5 = getProxy(ActivityProxy)
	local var_8_6

	if not arg_8_0.isSupport then
		if arg_8_2 then
			var_8_6 = var_8_5:getBuildActivityCfgByID(var_8_0.id)
		else
			var_8_6 = var_8_5:getNoneActBuildActivityCfgByID(var_8_0.id)
		end
	end

	local var_8_7 = var_8_6 and var_8_6.rate_tip or var_8_0.rate_tip

	for iter_8_2 = 1, #var_8_7 do
		local var_8_8

		if iter_8_2 <= var_8_3 then
			var_8_8 = arg_8_0.tipListTF:GetChild(iter_8_2 - 1)
		else
			var_8_8 = cloneTplTo(arg_8_0.tipListTpl, arg_8_0.tipListTF)
		end

		if var_8_8 then
			setActive(var_8_8, true)
			setText(var_8_8, HXSet.hxLan(var_8_7[iter_8_2]))
		end
	end
end

function var_0_0.Hide(arg_9_0)
	arg_9_0.showing = false

	setActiveViaLayer(arg_9_0._tf, false)
	pg.UIMgr.GetInstance():UnblurPanel(arg_9_0._tf, arg_9_0._tf)
end

function var_0_0.isShowing(arg_10_0)
	return arg_10_0.showing
end

function var_0_0.OnDestroy(arg_11_0)
	return
end

return var_0_0
