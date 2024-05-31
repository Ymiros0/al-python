local var_0_0 = class("QuotaGoodsCard", import(".BaseGoodsCard"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.go = arg_1_1
	arg_1_0.tr = tf(arg_1_1)
	arg_1_0.itemTF = findTF(arg_1_0.tr, "item")
	arg_1_0.nameTxt = findTF(arg_1_0.tr, "item/name_mask/name")
	arg_1_0.resIconTF = findTF(arg_1_0.tr, "item/consume/contain/icon"):GetComponent(typeof(Image))
	arg_1_0.mask = arg_1_0.tr:Find("mask")
	arg_1_0.countTF = findTF(arg_1_0.tr, "item/consume/contain/Text"):GetComponent(typeof(Text))
	arg_1_0.discountTF = findTF(arg_1_0.tr, "item/discount")

	setActive(arg_1_0.discountTF, false)

	arg_1_0.limitCountTF = findTF(arg_1_0.tr, "item/count_contain/count"):GetComponent(typeof(Text))
	arg_1_0.limitCountLabelTF = findTF(arg_1_0.tr, "item/count_contain/label"):GetComponent(typeof(Text))
	arg_1_0.limitCountLabelTF.text = i18n("quota_shop_owned")
	arg_1_0.limitTag = arg_1_0.tr:Find("mask/tag/limit_tag")
end

function var_0_0.update(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4)
	arg_2_0.goodsVO = arg_2_1

	local var_2_0 = arg_2_0.goodsVO:canPurchase()

	setActive(arg_2_0.mask, not var_2_0)
	setActive(arg_2_0.limitTag, not var_2_0)
	onButton(arg_2_0, arg_2_0.mask, function()
		pg.TipsMgr.GetInstance():ShowTips(i18n("quota_shop_limit_error"))
	end, SFX_PANEL)

	local var_2_1 = arg_2_1:getConfig("commodity_type")
	local var_2_2 = arg_2_1:getConfig("commodity_id")
	local var_2_3 = Drop.New({
		type = var_2_1,
		id = var_2_2,
		count = arg_2_1:getConfig("num")
	})

	updateDrop(arg_2_0.itemTF, var_2_3)

	local var_2_4 = ""

	if var_2_1 == DROP_TYPE_SKIN then
		var_2_4 = pg.ship_skin_template[var_2_2].name or "??"
	else
		var_2_4 = var_2_3:getConfig("name") or "??"
	end

	arg_2_0.countTF.text = arg_2_1:getConfig("resource_num")

	if string.match(var_2_4, "(%d+)") then
		setText(arg_2_0.nameTxt, shortenString(var_2_4, 5))
	else
		setText(arg_2_0.nameTxt, shortenString(var_2_4, 6))
	end

	local var_2_5 = Drop.New({
		type = arg_2_1:getConfig("resource_category"),
		id = arg_2_1:getConfig("resource_type")
	}):getIcon()

	arg_2_0.resIconTF.sprite = GetSpriteFromAtlas(var_2_5, "")

	local var_2_6 = arg_2_1:GetLimitGoodCount()
	local var_2_7 = arg_2_1:GetPurchasableCnt()

	arg_2_0.limitCountTF.text = var_2_6 - var_2_7 .. "/" .. var_2_6
end

function var_0_0.setAsLastSibling(arg_4_0)
	arg_4_0.tr:SetAsLastSibling()
end

function var_0_0.OnDispose(arg_5_0)
	arg_5_0.goodsVO = nil
end

return var_0_0
