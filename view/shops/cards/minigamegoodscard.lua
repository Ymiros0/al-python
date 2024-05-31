local var_0_0 = class("MiniGameGoodsCard", import(".BaseGoodsCard"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.go = arg_1_1
	arg_1_0.tr = tf(arg_1_1)
	arg_1_0.mask = arg_1_0.tr:Find("mask")
	arg_1_0.selloutTag = arg_1_0.tr:Find("mask/tag/sellout_tag")

	setActive(arg_1_0.selloutTag, true)
	setText(arg_1_0.selloutTag, i18n("common_sale_out"))

	arg_1_0.levelTag = arg_1_0.tr:Find("mask/tag/level_tag")

	setText(arg_1_0.levelTag, i18n("shop_charge_level_limit"))

	arg_1_0.levelTagText = arg_1_0.tr:Find("mask/tag/level_tag/Text")
	arg_1_0.stars = arg_1_0.tr:Find("item/icon_bg/stars")
	arg_1_0.itemTF = findTF(arg_1_0.tr, "item")
	arg_1_0.nameTxt = findTF(arg_1_0.tr, "item/name_mask/name")
	arg_1_0.discountTF = findTF(arg_1_0.tr, "item/discount")
	arg_1_0.discountTextTF = findTF(arg_1_0.discountTF, "Text"):GetComponent(typeof(Text))
	arg_1_0.countTF = findTF(arg_1_0.tr, "item/consume/contain/Text"):GetComponent(typeof(Text))
	arg_1_0.resIconTF = findTF(arg_1_0.tr, "item/consume/contain/icon"):GetComponent(typeof(Image))
	arg_1_0.itemIconTF = arg_1_0.itemTF:Find("icon_bg/icon"):GetComponent(typeof(Image))
	arg_1_0.itemCountTF = arg_1_0.itemTF:Find("icon_bg/count"):GetComponent(typeof(Text))
	arg_1_0.countContainTf = findTF(arg_1_0.tr, "item/count_contain/count")

	setText(findTF(arg_1_0.tr, "item/count_contain/label"), i18n("activity_shop_exchange_count"))

	arg_1_0.maskTip = i18n("buy_countLimit")

	setText(arg_1_0.tr:Find("mask/tag/sellout_tag"), i18n("word_sell_out"))
	onButton(arg_1_0, arg_1_0.mask, function()
		pg.TipsMgr.GetInstance():ShowTips(arg_1_0.maskTip)
	end, SFX_PANEL)
end

function var_0_0.setGroupMask(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_0.goodsVO:getConfig("group_limit")
	local var_3_1 = var_3_0 > 0 and var_3_0 <= arg_3_1

	if isActive(arg_3_0.mask) then
		return
	end

	setActive(arg_3_0.mask, var_3_1)

	if var_3_0 > 0 and var_3_0 <= arg_3_1 then
		setActive(arg_3_0.selloutTag, true)
		setActive(arg_3_0.levelTag, false)
	end
end

function var_0_0.setLevelMask(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0.goodsVO:getLevelLimit(arg_4_1)
	local var_4_1 = arg_4_0.goodsVO:isLevelLimit(arg_4_1)

	if isActive(arg_4_0.mask) then
		return
	end

	setActive(arg_4_0.mask, var_4_1)

	if var_4_1 then
		setText(arg_4_0.levelTagText, tostring(var_4_0))
		setActive(arg_4_0.levelTag, true)
		setActive(arg_4_0.selloutTag, false)

		arg_4_0.maskTip = i18n("charge_level_limit")
	end
end

function var_0_0.update(arg_5_0, arg_5_1)
	arg_5_0.goodsVO = arg_5_1

	local var_5_0 = arg_5_0.goodsVO:CanPurchase()

	setActive(arg_5_0.mask, not var_5_0)
	setActive(arg_5_0.stars, false)

	local var_5_1 = arg_5_1:GetDropInfo()

	updateDrop(arg_5_0.itemTF, var_5_1)

	local var_5_2 = var_5_1:getConfig("name") or ""

	setText(arg_5_0.nameTxt, shortenString(var_5_2, 6))

	local var_5_3 = ""
	local var_5_4 = arg_5_1:getConfig("price")
	local var_5_5 = arg_5_1:GetMaxCnt()
	local var_5_6 = arg_5_1:getConfig("goods_purchase_limit")

	setText(arg_5_0.countContainTf, var_5_5 .. "/" .. var_5_6)
	setActive(arg_5_0.discountTF, false)

	arg_5_0.countTF.text = math.ceil(var_5_4)

	GetSpriteFromAtlasAsync("ui/ShopsUI_atlas", "minigameRes", function(arg_6_0)
		arg_5_0.resIconTF:GetComponent(typeof(Image)).sprite = arg_6_0
	end)
end

function var_0_0.OnDispose(arg_7_0)
	arg_7_0.goodsVO = nil
end

return var_0_0
