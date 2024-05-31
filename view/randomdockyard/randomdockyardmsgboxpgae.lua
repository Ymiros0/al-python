﻿local var_0_0 = class("RandomDockYardMsgBoxPgae", import("view.base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "RandomDockYardMsgBoxUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.closeBtn = arg_2_0:findTF("frame/top/btnBack")
	arg_2_0.cancelBtn = arg_2_0:findTF("frame/cancel_button")
	arg_2_0.confirmBtn = arg_2_0:findTF("frame/confirm_button")
	arg_2_0.scrollrect = arg_2_0:findTF("frame/sliders"):GetComponent("LScrollRect")
	arg_2_0.titleTxt = arg_2_0:findTF("frame/top/title_list/infomation/title"):GetComponent(typeof(Text))
	arg_2_0.titleEnTxt = arg_2_0:findTF("frame/top/title_list/infomation/title_en"):GetComponent(typeof(Text))
	arg_2_0.subTitleTxt = arg_2_0:findTF("frame/label/Text"):GetComponent(typeof(Text))

	setText(arg_2_0:findTF("frame/confirm_button/pic"), i18n("text_confirm"))
	setText(arg_2_0:findTF("frame/cancel_button/pic"), i18n("text_cancel"))
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if arg_3_0.callback then
			arg_3_0.callback()
		end

		arg_3_0:Hide()
	end, SFX_PANEL)

	arg_3_0.cards = {}

	function arg_3_0.scrollrect.onUpdateItem(arg_8_0, arg_8_1)
		arg_3_0:OnUpdateItem(arg_8_0, arg_8_1)
	end

	function arg_3_0.scrollrect.onInitItem(arg_9_0)
		arg_3_0:OnInitItem(arg_9_0)
	end
end

function var_0_0.OnInitItem(arg_10_0, arg_10_1)
	local var_10_0 = RandomDockYardCard.New(arg_10_1)

	arg_10_0.cards[arg_10_1] = var_10_0
end

function var_0_0.OnUpdateItem(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = arg_11_0.cards[arg_11_2]

	if not var_11_0 then
		arg_11_0:OnInitItem(arg_11_2)

		var_11_0 = arg_11_0.cards[arg_11_2]
	end

	local var_11_1 = getProxy(BayProxy):RawGetShipById(arg_11_0.shipIds[arg_11_1 + 1])

	var_11_0:Update(var_11_1, false)
end

function var_0_0.Flush(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4)
	arg_12_0:Show()
	arg_12_0:UpdateTitle(arg_12_1)
	arg_12_0:UpdateSubTitle(arg_12_2)
	arg_12_0:UpdateList(arg_12_3)

	arg_12_0.callback = arg_12_4
end

function var_0_0.UpdateTitle(arg_13_0, arg_13_1)
	arg_13_0.titleTxt.text = arg_13_1.cn
	arg_13_0.titleEnTxt.text = arg_13_1.en
end

function var_0_0.UpdateSubTitle(arg_14_0, arg_14_1)
	arg_14_0.subTitleTxt.text = arg_14_1
end

function var_0_0.UpdateList(arg_15_0, arg_15_1)
	arg_15_0.shipIds = arg_15_1

	arg_15_0.scrollrect:SetTotalCount(#arg_15_0.shipIds)
end

function var_0_0.Show(arg_16_0)
	var_0_0.super.Show(arg_16_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_16_0._tf)
end

function var_0_0.Hide(arg_17_0)
	arg_17_0.callback = nil
	arg_17_0.shipIds = nil

	for iter_17_0, iter_17_1 in pairs(arg_17_0.cards) do
		iter_17_1:Dispose()
	end

	arg_17_0.cards = {}

	var_0_0.super.Hide(arg_17_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_17_0._tf, arg_17_0._parentTf)
end

function var_0_0.OnDestroy(arg_18_0)
	arg_18_0:Hide()
end

return var_0_0
