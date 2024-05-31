﻿local var_0_0 = class("CatterySettlementPage", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "CatterySettlementPage"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.painting = arg_2_0:findTF("painting")
	arg_2_0.uilist = UIItemList.New(arg_2_0:findTF("frame/commanders"), arg_2_0:findTF("frame/commanders/tpl"))

	setText(arg_2_0:findTF("dialogue/label/Text1"), i18n("cattery_settlement_dialogue_1"))
	setText(arg_2_0:findTF("dialogue/label/Text3"), i18n("cattery_settlement_dialogue_2"))
	setText(arg_2_0:findTF("dialogue/label1/Text1"), i18n("cattery_settlement_dialogue_3"))
	setText(arg_2_0:findTF("dialogue/label1/Text3"), i18n("cattery_settlement_dialogue_4"))

	arg_2_0.timeTxt = arg_2_0:findTF("dialogue/label/Text2"):GetComponent(typeof(Text))
	arg_2_0.expTxt = arg_2_0:findTF("dialogue/label1/Text2"):GetComponent(typeof(Text))
	arg_2_0.confirmBtn = arg_2_0:findTF("comfirm")
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		arg_3_0:Destroy()
	end, SFX_PANEL)

	arg_3_0.cards = {}

	arg_3_0.uilist:make(function(arg_5_0, arg_5_1, arg_5_2)
		if arg_5_0 == UIItemList.EventUpdate then
			local var_5_0 = arg_3_0.displays[arg_5_1 + 1]

			arg_3_0:UpdateCommander(arg_5_2, var_5_0)
		end
	end)
end

function var_0_0.Show(arg_6_0, arg_6_1)
	var_0_0.super.Show(arg_6_0)

	arg_6_0.home = arg_6_1

	arg_6_0:SetPainting()
	arg_6_0:UpdateCommanders()
	arg_6_0:UpdateDialogue()

	arg_6_0.UIMgr = pg.UIMgr.GetInstance()

	arg_6_0.UIMgr:BlurPanel(arg_6_0._tf)
end

function var_0_0.Hide(arg_7_0)
	var_0_0.super.Hide(arg_7_0)
	arg_7_0.UIMgr:UnblurPanel(arg_7_0._tf, arg_7_0.UIMgr._normalUIMain)
end

function var_0_0.GetCurrentFlagship(arg_8_0)
	return Ship.New({
		id = 999,
		configId = 312011
	})
end

function var_0_0.SetPainting(arg_9_0)
	arg_9_0:ReturnPainting()

	local var_9_0 = arg_9_0:GetCurrentFlagship():getPainting()

	arg_9_0.paintingName = var_9_0

	setPaintingPrefabAsync(arg_9_0.painting, var_9_0, "jiesuan")
end

function var_0_0.UpdateCommanders(arg_10_0)
	local var_10_0 = arg_10_0.home:GetCatteries()

	arg_10_0.displays = {}

	for iter_10_0, iter_10_1 in pairs(var_10_0) do
		table.insert(arg_10_0.displays, iter_10_1)
	end

	table.sort(arg_10_0.displays, function(arg_11_0, arg_11_1)
		return arg_11_0:GetCommanderId() > arg_11_1:GetCommanderId()
	end)
	arg_10_0.uilist:align(#arg_10_0.displays)
end

function var_0_0.UpdateCommander(arg_12_0, arg_12_1, arg_12_2)
	local var_12_0 = arg_12_0.cards[arg_12_1]

	if not var_12_0 then
		var_12_0 = CatterySettlementCard.New(arg_12_1)
		arg_12_0.cards[arg_12_1] = var_12_0
	end

	var_12_0:Update(arg_12_2, arg_12_2:GetCacheExp())
	var_12_0:Action(function()
		return
	end)
end

function var_0_0.UpdateDialogue(arg_14_0)
	local var_14_0 = arg_14_0.home:GetCatteries()
	local var_14_1 = 0
	local var_14_2 = 0

	for iter_14_0, iter_14_1 in pairs(var_14_0) do
		var_14_1 = var_14_1 + iter_14_1:GetCacheExp()

		local var_14_3 = iter_14_1:GetCacheExpTime()

		if var_14_2 < var_14_3 then
			var_14_2 = var_14_3
		end
	end

	arg_14_0.timeTxt.text = pg.TimeMgr.GetInstance():DescCDTime(var_14_2)
	arg_14_0.expTxt.text = var_14_1
end

function var_0_0.ReturnPainting(arg_15_0)
	if arg_15_0.paintingName then
		retPaintingPrefab(arg_15_0.painting, arg_15_0.paintingName)

		arg_15_0.paintingName = nil
	end
end

function var_0_0.OnDestroy(arg_16_0)
	arg_16_0:ReturnPainting()

	for iter_16_0, iter_16_1 in pairs(arg_16_0.cards) do
		iter_16_1:Dispose()
	end

	arg_16_0:Hide()

	arg_16_0.cards = nil
end

return var_0_0
