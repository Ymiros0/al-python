﻿local var_0_0 = class("SkinVoucherMsgBox", import(".SkinCouponMsgBox"))

function var_0_0.getUIName(arg_1_0)
	return "SkinVoucherMsgBoxUI"
end

function var_0_0.OnLoaded(arg_2_0)
	var_0_0.super.OnLoaded(arg_2_0)
	setActive(arg_2_0.confirmBtn, false)

	arg_2_0.realPriceBtn = arg_2_0:findTF("window/button_container/real_price")
	arg_2_0.discountPriceBtn = arg_2_0:findTF("window/button_container/discount_price")

	setText(arg_2_0._tf:Find("window/top/bg/infomation/title"), i18n("title_info"))
end

function var_0_0.RegisterBtn(arg_3_0, arg_3_1)
	onButton(arg_3_0, arg_3_0.discountPriceBtn, function()
		if not arg_3_0.prevSelId then
			return
		end

		if arg_3_1.onYes then
			arg_3_1.onYes(arg_3_0.prevSelId)
		end

		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.realPriceBtn, function()
		if arg_3_1.onYes then
			arg_3_1.onYes()
		end

		arg_3_0:Hide()
	end, SFX_PANEL)
end

function var_0_0.UpdateContent(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_1.skinName
	local var_6_1 = arg_6_1.price

	if arg_6_0.prevSelId then
		local var_6_2 = pg.item_data_statistics[arg_6_0.prevSelId]
		local var_6_3 = var_6_2.usage_arg[2]
		local var_6_4 = math.max(0, var_6_1 - var_6_3)

		arg_6_0.label1.text = i18n(var_6_4 > 0 and "skin_purchase_confirm" or "skin_purchase_over_price", var_6_2.name, var_6_4, var_6_0)
	else
		arg_6_0.label1.text = i18n("charge_scene_buy_confirm", var_6_1, var_6_0)
	end

	setActive(arg_6_0.realPriceBtn, not arg_6_0.prevSelId)
	setActive(arg_6_0.discountPriceBtn, arg_6_0.prevSelId)
end

function var_0_0.UpdateItem(arg_7_0, arg_7_1)
	arg_7_0.itemTrs = {}

	local var_7_0 = table.mergeArray({
		0
	}, arg_7_1.itemList or {})

	UIItemList.StaticAlign(arg_7_0:findTF("window/frame/list"), arg_7_0:findTF("window/frame/left"), #var_7_0, function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate then
			arg_7_0:FlushItem(var_7_0[arg_8_1 + 1], arg_8_2)
		end
	end)
	triggerToggle(arg_7_0:findTF("window/frame/list/none"), true)
end

function var_0_0.FlushItem(arg_9_0, arg_9_1, arg_9_2)
	if arg_9_1 == 0 then
		setText(arg_9_2:Find("name_bg/Text"), i18n("not_use_ticket_to_buy_skin"))
	else
		updateDrop(arg_9_2, {
			count = 1,
			type = DROP_TYPE_ITEM,
			id = arg_9_1
		})

		local var_9_0 = pg.item_data_statistics[arg_9_1].name

		setText(arg_9_2:Find("name_bg/Text"), var_9_0)
	end

	onToggle(arg_9_0, arg_9_2, function(arg_10_0)
		if arg_10_0 then
			if arg_9_1 == 0 then
				arg_9_0.prevSelId = nil

				arg_9_0:UpdateContent(arg_9_0.settings)
			else
				arg_9_0:ClearPrevSel()

				arg_9_0.prevSelId = arg_9_1

				arg_9_0:UpdateContent(arg_9_0.settings)
			end
		end
	end, SFX_PANEL)

	arg_9_0.itemTrs[arg_9_1] = arg_9_2
end

function var_0_0.ClearPrevSel(arg_11_0)
	arg_11_0.prevSelId = nil
end

function var_0_0.Hide(arg_12_0)
	arg_12_0.settings = nil

	setActive(arg_12_0._tf, false)
	arg_12_0:ClearPrevSel()

	for iter_12_0, iter_12_1 in pairs(arg_12_0.itemTrs) do
		removeOnToggle(iter_12_1)
		triggerToggle(iter_12_1, false)
	end
end

return var_0_0
