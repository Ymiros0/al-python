local var_0_0 = class("MedalGoodsCard", import(".BaseGoodsCard"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._go = arg_1_1
	arg_1_0._tr = tf(arg_1_1)
	arg_1_0.itemTF = arg_1_0._tr:Find("item")
	arg_1_0.itemIconBgTF = arg_1_0.itemTF:Find("icon_bg")
	arg_1_0.itemIconFrameTF = arg_1_0.itemTF:Find("icon_bg/frame")
	arg_1_0.itemIconTF = arg_1_0.itemTF:Find("icon_bg/icon")
	arg_1_0.itemCountTF = arg_1_0.itemTF:Find("icon_bg/count"):GetComponent(typeof(Text))
	arg_1_0.discountTF = arg_1_0._tr:Find("item/discount")
	arg_1_0.nameTF = arg_1_0._tr:Find("item/name_mask/name"):GetComponent(typeof(Text))
	arg_1_0.consumeIconTF = arg_1_0._tr:Find("item/consume/contain/icon")
	arg_1_0.consumeTxtTF = arg_1_0._tr:Find("item/consume/contain/Text"):GetComponent(typeof(Text))
	arg_1_0.maskTF = arg_1_0._tr:Find("mask")
	arg_1_0.cntTxt = arg_1_0._tr:Find("item/count_contain/count"):GetComponent(typeof(Text))
	arg_1_0.groupMark = arg_1_0._tr:Find("item/group_locked")
	arg_1_0.limitCountLabelTF = findTF(arg_1_0._tr, "item/count_contain/label"):GetComponent(typeof(Text))
	arg_1_0.limitCountLabelTF.text = i18n("activity_shop_exchange_count")

	setActive(arg_1_0.discountTF, false)

	arg_1_0.selloutTag = arg_1_0._tr:Find("mask/tag/sellout_tag")
end

function var_0_0.update(arg_2_0, arg_2_1)
	if arg_2_0.goods ~= arg_2_1 then
		arg_2_0.goods = arg_2_1

		arg_2_0:Init()
	else
		arg_2_0.goods = arg_2_1
	end

	arg_2_0.cntTxt.text = arg_2_0.goods.count .. "/" .. arg_2_0.goods:GetLimit()

	local var_2_0 = arg_2_0.goods:CanPurchase()

	setActive(arg_2_0.maskTF, not var_2_0)
	setActive(arg_2_0.selloutTag, not var_2_0)
end

function var_0_0.Init(arg_3_0)
	local var_3_0 = arg_3_0.goods:getConfig("goods_name")

	if string.match(var_3_0, "(%d+)") then
		setText(arg_3_0.nameTF, shortenString(var_3_0, 5))
	else
		setText(arg_3_0.nameTF, shortenString(var_3_0, 6))
	end

	arg_3_0.consumeTxtTF.text = arg_3_0.goods:getConfig("price")

	GetImageSpriteFromAtlasAsync("props/medal", "", arg_3_0.consumeIconTF)
	GetImageSpriteFromAtlasAsync(arg_3_0.goods:getConfig("goods_icon"), "", arg_3_0.itemIconTF)

	arg_3_0.itemCountTF.text = arg_3_0.goods:getConfig("num")

	local var_3_1 = arg_3_0.goods:getConfig("goods_rarity") or ItemRarity.Gray

	setImageSprite(arg_3_0.itemIconBgTF, GetSpriteFromAtlas("weaponframes", "bg" .. ItemRarity.Rarity2Print(var_3_1)))
	setImageColor(arg_3_0.itemIconFrameTF, Color.NewHex(ItemRarity.Rarity2FrameHexColor(var_3_1)))

	local var_3_2 = arg_3_0.goods:getConfig("is_ship")
	local var_3_3 = arg_3_0.goods:getConfig("goods")

	if arg_3_0.groupMark and var_3_2 == 1 and #var_3_3 == 1 then
		local var_3_4 = var_3_3[1]
		local var_3_5 = pg.ship_data_template[var_3_4].group_type

		if var_3_5 and var_3_5 > 0 then
			setActive(arg_3_0.groupMark, not getProxy(CollectionProxy):getShipGroup(var_3_5))
		else
			setActive(arg_3_0.groupMark, false)
		end
	else
		setActive(arg_3_0.groupMark, false)
	end
end

function var_0_0.OnDispose(arg_4_0)
	arg_4_0.goods = nil
end

return var_0_0
