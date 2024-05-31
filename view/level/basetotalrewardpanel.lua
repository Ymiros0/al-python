﻿local var_0_0 = class("BaseTotalRewardPanel", import("view.base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "BaseTotalRewardPanel"
end

function var_0_0.init(arg_2_0)
	arg_2_0.window = arg_2_0._tf:Find("Window")
	arg_2_0.boxView = arg_2_0.window:Find("Layout/Box/ScrollView")
	arg_2_0.emptyTip = arg_2_0.window:Find("Layout/Box/EmptyTip")

	setText(arg_2_0.emptyTip, i18n("autofight_rewards_none"))
	setText(arg_2_0.window:Find("Fixed/top/bg/obtain/title"), arg_2_0.contextData.title)
	setText(arg_2_0.window:Find("Fixed/top/bg/obtain/title/title_en"), arg_2_0.contextData.subTitle)
	setText(arg_2_0.window:Find("Fixed/ButtonGO/pic"), i18n("autofight_onceagain"))
	setText(arg_2_0.window:Find("Fixed/ButtonExit/pic"), i18n("autofight_leave"))
end

function var_0_0.didEnter(arg_3_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_3_0._tf)
	arg_3_0:UpdateView()
end

function var_0_0.willExit(arg_4_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_4_0._tf)
end

function var_0_0.UpdateView(arg_5_0)
	local var_5_0 = arg_5_0.contextData

	onButton(arg_5_0, arg_5_0._tf:Find("BG"), function()
		existCall(var_5_0.onClose)
		arg_5_0:closeView()
	end)
end

function var_0_0.CloneIconTpl(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_0:GetComponent(typeof(ItemList))

	assert(var_7_0, "Need a Itemlist Component for " .. (arg_7_0 and arg_7_0.name or "NIL"))

	local var_7_1 = Instantiate(var_7_0.prefabItem[0])

	if arg_7_1 then
		var_7_1.name = arg_7_1
	end

	setParent(var_7_1, arg_7_0)

	return var_7_1
end

function var_0_0.HandleShowMsgBox(arg_8_0, arg_8_1)
	pg.MsgboxMgr.GetInstance():ShowMsgBox(arg_8_1)
end

return var_0_0
