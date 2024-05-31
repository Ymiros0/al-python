﻿local var_0_0 = class("GuildRequestLayer", import("..base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "GuildRequestUI"
end

function var_0_0.setRequest(arg_2_0, arg_2_1)
	arg_2_0.requestVOs = arg_2_1
end

function var_0_0.init(arg_3_0)
	arg_3_0.viewRect = arg_3_0:findTF("request_panel/view")
	arg_3_0.listEmptyTF = arg_3_0:findTF("main/frame/empty")
	arg_3_0.listEmptyTF = arg_3_0:findTF("empty")

	setActive(arg_3_0.listEmptyTF, false)

	arg_3_0.listEmptyTxt = arg_3_0:findTF("Text", arg_3_0.listEmptyTF)

	setText(arg_3_0.listEmptyTxt, i18n("list_empty_tip_guildrequestui"))

	arg_3_0.scrollRect = arg_3_0.viewRect:GetComponent("LScrollRect")
end

function var_0_0.didEnter(arg_4_0)
	pg.GuildPaintingMgr:GetInstance():Hide()
end

function var_0_0.initRequests(arg_5_0)
	arg_5_0.requestCards = {}

	function arg_5_0.scrollRect.onInitItem(arg_6_0)
		arg_5_0:onInitItem(arg_6_0)
	end

	function arg_5_0.scrollRect.onUpdateItem(arg_7_0, arg_7_1)
		arg_5_0:onUpdateItem(arg_7_0, arg_7_1)
	end

	arg_5_0:SetTotalCount()
end

function var_0_0.onInitItem(arg_8_0, arg_8_1)
	local var_8_0 = GuildRequestCard.New(arg_8_1)

	onButton(arg_8_0, var_8_0.accpetBtn, function()
		arg_8_0:emit(GuildRequestMediator.ACCPET, var_8_0.requestVO.player.id)
	end, SFX_PANEL)
	onButton(arg_8_0, var_8_0.rejectBtn, function()
		arg_8_0:emit(GuildRequestMediator.REJECT, var_8_0.requestVO.player.id)
	end, SFX_PANEL)

	arg_8_0.requestCards[arg_8_1] = var_8_0
end

function var_0_0.onUpdateItem(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = arg_11_0.requestCards[arg_11_2]

	if not var_11_0 then
		arg_11_0:onInitItem(arg_11_2)

		var_11_0 = arg_11_0.requestCards[arg_11_2]
	end

	local var_11_1 = arg_11_0.requestVOs[arg_11_1 + 1]

	var_11_0:Update(var_11_1)
end

function var_0_0.SetTotalCount(arg_12_0)
	table.sort(arg_12_0.requestVOs, function(arg_13_0, arg_13_1)
		return arg_13_0.timestamp < arg_13_1.timestamp
	end)
	arg_12_0.scrollRect:SetTotalCount(#arg_12_0.requestVOs, 0)
	setActive(arg_12_0.listEmptyTF, #arg_12_0.requestVOs <= 0)
end

function var_0_0.addRequest(arg_14_0, arg_14_1)
	table.insert(arg_14_0.requestVOs, arg_14_1)
	arg_14_0:SetTotalCount()
end

function var_0_0.deleteRequest(arg_15_0, arg_15_1)
	for iter_15_0, iter_15_1 in ipairs(arg_15_0.requestVOs) do
		if iter_15_1.player.id == arg_15_1 then
			table.remove(arg_15_0.requestVOs, iter_15_0)

			break
		end
	end

	arg_15_0:SetTotalCount()
end

function var_0_0.onBackPressed(arg_16_0)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
	arg_16_0:emit(var_0_0.ON_BACK)
end

function var_0_0.willExit(arg_17_0)
	for iter_17_0, iter_17_1 in pairs(arg_17_0.requestCards) do
		iter_17_1:Dispose()
	end
end

return var_0_0
