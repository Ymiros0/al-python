﻿local var_0_0 = class("NewNavalTacticsUnlockSlotPage", import("....base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "NewNavalTacticsUnlockSlotPage"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.contentTxt = arg_2_0:findTF("content/Text"):GetComponent(typeof(Text))
	arg_2_0.discountDateTxt = arg_2_0:findTF("content/discountDate"):GetComponent(typeof(Text))
	arg_2_0.discountTxt = arg_2_0:findTF("content/discountInfo/Text"):GetComponent(typeof(Text))
	arg_2_0.confirmBtn = arg_2_0:findTF("content/confirm_btn")
	arg_2_0.cancelBtn = arg_2_0:findTF("content/cancel_btn")
	arg_2_0.closeBtn = arg_2_0:findTF("content/btnBack")

	setText(arg_2_0.confirmBtn:Find("pic"), i18n("word_ok"))
	setText(arg_2_0.cancelBtn:Find("pic"), i18n("word_cancel"))
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if arg_3_0.callback then
			arg_3_0.callback()
		end

		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
end

function var_0_0.Show(arg_8_0, arg_8_1, arg_8_2)
	var_0_0.super.Show(arg_8_0)

	arg_8_0.callback = arg_8_2

	local var_8_0 = CommonCommodity.New({
		id = arg_8_1
	}, Goods.TYPE_SHOPSTREET)

	arg_8_0:Flush(var_8_0)

	arg_8_0.commodity = var_8_0
end

function var_0_0.Flush(arg_9_0, arg_9_1)
	arg_9_0:RemoveTimer()

	local var_9_0 = arg_9_1:isDisCount()

	if var_9_0 then
		arg_9_0:UpdateDiscountView(arg_9_1)
	else
		local var_9_1 = arg_9_1:GetPrice()

		arg_9_0.contentTxt.text = i18n("open_skill_pos", var_9_1)
	end

	setActive(arg_9_0.discountDateTxt.gameObject, var_9_0)
	setActive(arg_9_0.discountTxt.gameObject.transform.parent, var_9_0)
end

function var_0_0.UpdateDiscountView(arg_10_0, arg_10_1)
	local var_10_0, var_10_1 = arg_10_1:GetPrice()
	local var_10_2 = arg_10_1:GetDiscountEndTime()

	arg_10_0:AddTimer(var_10_2)

	arg_10_0.discountTxt.text = var_10_1 .. "%"

	local var_10_3 = arg_10_1:getConfig("resource_num")

	arg_10_0.contentTxt.text = i18n("open_skill_pos_discount", var_10_3, var_10_0)

	onNextTick(function()
		local var_11_0 = arg_10_0.contentTxt.gameObject.transform
		local var_11_1 = var_11_0:GetChild(var_11_0.childCount - 1)

		if not IsNil(var_11_1) then
			setAnchoredPosition(var_11_1, {
				y = var_11_1.anchoredPosition.y + 15
			})
		end
	end)
end

function var_0_0.AddTimer(arg_12_0, arg_12_1)
	arg_12_0.timer = Timer.New(function()
		local var_13_0 = pg.TimeMgr.GetInstance():GetServerTime()
		local var_13_1 = arg_12_1 - var_13_0

		if var_13_1 <= 0 then
			arg_12_0.discountDateTxt.text = ""

			arg_12_0:Flush(arg_12_0.commodity)
		else
			local var_13_2 = i18n("discount_time", arg_12_0:WarpDateTip(var_13_1) .. i18n("word_date"))

			if var_13_2 ~= arg_12_0.str then
				arg_12_0.discountDateTxt.text = var_13_2
				arg_12_0.str = var_13_2
			end
		end
	end, 1, -1)

	arg_12_0.timer:Start()
	arg_12_0.timer.func()
end

function var_0_0.WarpDateTip(arg_14_0, arg_14_1)
	local var_14_0 = ""

	if arg_14_1 >= 86400 then
		var_14_0 = math.floor(arg_14_1 / 86400)
	elseif arg_14_1 >= 3600 then
		var_14_0 = math.floor(arg_14_1 / 3600)
	else
		var_14_0 = math.floor(arg_14_1 / 60)
	end

	return var_14_0
end

function var_0_0.RemoveTimer(arg_15_0)
	if arg_15_0.timer then
		arg_15_0.timer:Stop()

		arg_15_0.timer = nil
	end
end

function var_0_0.Hide(arg_16_0)
	arg_16_0:RemoveTimer()
	var_0_0.super.Hide(arg_16_0)

	arg_16_0.callback = nil
	arg_16_0.commodity = nil
end

function var_0_0.OnDestroy(arg_17_0)
	arg_17_0:Hide()
end

return var_0_0
