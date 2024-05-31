local var_0_0 = class("ActivityGoodsCard", import(".BaseGoodsCard"))

var_0_0.Color = {}
var_0_0.DefaultColor = {
	0.8745098039215686,
	0.9294117647058824,
	1
}

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.go = arg_1_1
	arg_1_0.tr = tf(arg_1_1)
	arg_1_0.itemTF = findTF(arg_1_0.tr, "item")
	arg_1_0.nameTxt = findTF(arg_1_0.tr, "item/name_mask/name")
	arg_1_0.resIconTF = findTF(arg_1_0.tr, "item/consume/contain/icon"):GetComponent(typeof(Image))
	arg_1_0.mask = arg_1_0.tr:Find("mask")
	arg_1_0.selloutTag = arg_1_0.tr:Find("mask/tag/sellout_tag")
	arg_1_0.sellEndTag = arg_1_0.tr:Find("mask/tag/sellend_tag")

	setActive(arg_1_0.sellEndTag, false)

	arg_1_0.unexchangeTag = arg_1_0.tr:Find("mask/tag/unexchange_tag")
	arg_1_0.countTF = findTF(arg_1_0.tr, "item/consume/contain/Text"):GetComponent(typeof(Text))
	arg_1_0.discountTF = findTF(arg_1_0.tr, "item/discount")

	setActive(arg_1_0.discountTF, false)

	arg_1_0.limitTimeSellTF = findTF(arg_1_0.tr, "item/limit_time_sell")

	setActive(arg_1_0.limitTimeSellTF, false)

	arg_1_0.limitCountTF = findTF(arg_1_0.tr, "item/count_contain/count"):GetComponent(typeof(Text))
	arg_1_0.limitCountLabelTF = findTF(arg_1_0.tr, "item/count_contain/label"):GetComponent(typeof(Text))
	arg_1_0.limitCountLabelTF.text = i18n("activity_shop_exchange_count")
	arg_1_0.tagImg = arg_1_0.tr:Find("mask/tag"):GetComponent(typeof(Image))
	arg_1_0.limitPassTag = arg_1_0.tr:Find("mask/tag/pass_tag")
end

function var_0_0.update(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4)
	arg_2_0.goodsVO = arg_2_1

	local var_2_0 = arg_2_0.goodsVO:CheckCntLimit()
	local var_2_1 = var_2_0 and not arg_2_0.goodsVO:CheckArgLimit()

	setActive(arg_2_0.mask, not var_2_0 or var_2_1)
	setActive(arg_2_0.selloutTag, not var_2_0)

	if arg_2_0.limitPassTag then
		setActive(arg_2_0.limitPassTag, false)
	end

	removeOnButton(arg_2_0.mask)

	if var_2_1 then
		local var_2_2, var_2_3, var_2_4 = arg_2_0.goodsVO:CheckArgLimit()

		if var_2_3 == "pass" then
			setActive(arg_2_0.limitPassTag, true)
			setText(findTF(arg_2_0.limitPassTag, "Text"), i18n("eventshop_unlock_info", var_2_4))
			onButton(arg_2_0, arg_2_0.mask, function()
				pg.TipsMgr.GetInstance():ShowTips(i18n("eventshop_unlock_hint", var_2_4))
			end, SFX_PANEL)
		elseif var_2_3 == 1 or var_2_3 == 2 then
			setText(arg_2_0.unexchangeTag, var_2_4)

			local var_2_5 = ""

			if var_2_3 == 1 then
				var_2_5 = "LIMIT"
			end

			if var_2_3 == 2 then
				var_2_5 = "LOCK"
			end

			setText(arg_2_0.unexchangeTag:Find("sellout_tag_en"), var_2_5)
			setActive(arg_2_0.unexchangeTag, true)
		end
	end

	local var_2_6 = Drop.New({
		type = arg_2_1:getConfig("commodity_type"),
		id = arg_2_1:getConfig("commodity_id"),
		count = arg_2_1:getConfig("num")
	})

	updateDrop(arg_2_0.itemTF, var_2_6)
	setActive(arg_2_0.limitTimeSellTF, false)

	if var_2_0 then
		local var_2_7, var_2_8, var_2_9 = arg_2_0.goodsVO:CheckTimeLimit()

		setActive(arg_2_0.limitTimeSellTF, var_2_7 and var_2_8)

		if var_2_7 and not var_2_8 then
			setActive(arg_2_0.mask, true)
			setActive(arg_2_0.sellEndTag, true)
			removeOnButton(arg_2_0.mask)
			onButton(arg_2_0, arg_2_0.mask, function()
				if var_2_9 then
					pg.TipsMgr.GetInstance():ShowTips(i18n("tip_build_ticket_exchange_expired", var_2_6:getName()))
				end
			end, SFX_PANEL)
		end
	end

	GetSpriteFromAtlasAsync(Drop.New({
		type = arg_2_1:getConfig("resource_category"),
		id = arg_2_1:getConfig("resource_type")
	}):getIcon(), "", function(arg_5_0)
		arg_2_0.resIconTF.sprite = arg_5_0
	end)

	arg_2_0.countTF.text = arg_2_1:getConfig("resource_num")

	local var_2_10 = var_2_6:getName() or "??"

	if string.match(var_2_10, "(%d+)") then
		setText(arg_2_0.nameTxt, shortenString(var_2_10, 5))
	else
		setText(arg_2_0.nameTxt, shortenString(var_2_10, 6))
	end

	local var_2_11 = arg_2_1:getConfig("num_limit")

	if var_2_11 == 0 then
		arg_2_0.limitCountTF.text = i18n("common_no_limit")
	else
		local var_2_12 = arg_2_1:GetPurchasableCnt()

		arg_2_0.limitCountTF.text = math.max(var_2_12, 0) .. "/" .. var_2_11
	end

	local var_2_13 = var_0_0.Color[arg_2_2] or var_0_0.DefaultColor

	arg_2_0.limitCountTF.color = arg_2_3 or Color.New(unpack(var_2_13))
	arg_2_0.limitCountLabelTF.color = arg_2_3 or Color.New(unpack(var_2_13))
	arg_2_4 = arg_2_4 or Color.New(0, 0, 0, 1)

	if GetComponent(arg_2_0.limitCountTF, typeof(Outline)) then
		setOutlineColor(arg_2_0.limitCountTF, arg_2_4)
	end

	if GetComponent(arg_2_0.limitCountLabelTF, typeof(Outline)) then
		setOutlineColor(arg_2_0.limitCountLabelTF, arg_2_4)
	end
end

function var_0_0.setAsLastSibling(arg_6_0)
	arg_6_0.tr:SetAsLastSibling()
end

function var_0_0.StaticUpdate(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
	local var_7_0 = tf(arg_7_0)
	local var_7_1 = findTF(var_7_0, "item")
	local var_7_2 = findTF(var_7_0, "item/name_mask/name")
	local var_7_3 = findTF(var_7_0, "item/consume/contain/icon"):GetComponent(typeof(Image))
	local var_7_4 = var_7_0:Find("mask")
	local var_7_5 = var_7_0:Find("mask/tag/sellout_tag")
	local var_7_6 = findTF(var_7_0, "item/consume/contain/Text"):GetComponent(typeof(Text))
	local var_7_7 = findTF(var_7_0, "item/discount")

	setActive(var_7_7, false)

	local var_7_8 = findTF(var_7_0, "item/count_contain/count"):GetComponent(typeof(Text))
	local var_7_9 = findTF(var_7_0, "item/count_contain/label"):GetComponent(typeof(Text))
	local var_7_10, var_7_11 = arg_7_1:canPurchase()

	setActive(var_7_4, not var_7_10)
	setActive(var_7_5, not var_7_10)

	local var_7_12 = Drop.New({
		type = arg_7_1:getConfig("commodity_type"),
		id = arg_7_1:getConfig("commodity_id"),
		count = arg_7_1:getConfig("num")
	})

	updateDrop(var_7_1, var_7_12)

	local var_7_13 = var_7_12:getConfig("name") or "??"

	var_7_6.text = arg_7_1:getConfig("resource_num")

	if string.match(var_7_13, "(%d+)") then
		setText(var_7_2, shortenString(var_7_13, 5))
	else
		setText(var_7_2, shortenString(var_7_13, 6))
	end

	var_7_3.sprite = GetSpriteFromAtlas(Drop.New({
		type = arg_7_1:getConfig("resource_category"),
		id = arg_7_1:getConfig("resource_type")
	}):getIcon(), "")

	if arg_7_1:getConfig("num_limit") == 0 then
		var_7_8.text = i18n("common_no_limit")
	else
		local var_7_14 = arg_7_1:getConfig("num_limit")

		if var_7_12.type == DROP_TYPE_SKIN and not var_7_10 then
			var_7_8.text = "0/" .. var_7_14
		else
			var_7_8.text = var_7_14 - arg_7_1.buyCount .. "/" .. var_7_14
		end
	end

	local var_7_15 = var_0_0.Color[arg_7_2] or var_0_0.DefaultColor

	var_7_8.color = arg_7_3 or Color.New(var_7_15[1], var_7_15[2], var_7_15[3], 1)
	var_7_9.color = arg_7_3 or Color.New(var_7_15[1], var_7_15[2], var_7_15[3], 1)

	if arg_7_1:getConfig("num_limit") >= 99 then
		var_7_9.text = i18n("shop_label_unlimt_cnt")
		var_7_8.text = ""
	end
end

function var_0_0.OnDispose(arg_8_0)
	arg_8_0.goodsVO = nil
end

return var_0_0
