local var_0_0 = class("NewServerGoodsCard")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0._tr = arg_1_1.transform
	arg_1_0.itemTF = arg_1_0._tr.Find("item")
	arg_1_0.itemIconBgTF = arg_1_0.itemTF.Find("icon_bg")
	arg_1_0.itemIconFrameTF = arg_1_0.itemTF.Find("icon_bg/frame")
	arg_1_0.itemIconTF = arg_1_0.itemTF.Find("icon_bg/icon")
	arg_1_0.itemCountTF = arg_1_0.itemTF.Find("icon_bg/count").GetComponent(typeof(Text))
	arg_1_0.discountTF = arg_1_0._tr.Find("item/discount")
	arg_1_0.nameTF = arg_1_0._tr.Find("item/name_mask/name").GetComponent(typeof(Text))
	arg_1_0.consumeIconTF = arg_1_0._tr.Find("item/consume/contain/icon")
	arg_1_0.consumeTxtTF = arg_1_0._tr.Find("item/consume/contain/Text").GetComponent(typeof(Text))
	arg_1_0.sellOutMaskTF = arg_1_0._tr.Find("selloutmask")
	arg_1_0.levelMaskTF = arg_1_0._tr.Find("levelmask")
	arg_1_0.cntTxt = arg_1_0._tr.Find("item/count_contain/count").GetComponent(typeof(Text))

	setActive(arg_1_0.discountTF, False)
	setText(arg_1_0.sellOutMaskTF.Find("ch"), i18n("word_sell_out"))
	setText(arg_1_0.levelMaskTF.Find("ch"), i18n("word_sell_lock"))
	setText(arg_1_0._tr.Find("item/count_contain/label"), i18n("activity_shop_exchange_count"))

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.shop = arg_2_2

	if arg_2_1 != arg_2_0.commodity:
		arg_2_0.commodity = arg_2_1

		arg_2_0.Init()
		arg_2_0.Flush()
	else
		arg_2_0.commodity = arg_2_1

		arg_2_0.Flush()

def var_0_0.Flush(arg_3_0):
	arg_3_0.cntTxt.text = arg_3_0.commodity.GetCanPurchaseCnt() .. "/" .. arg_3_0.commodity.GetCanPurchaseMaxCnt()

	setActive(arg_3_0.sellOutMaskTF, not arg_3_0.commodity.CanPurchase())
	setActive(arg_3_0.levelMaskTF, not arg_3_0.commodity.IsOpening(arg_3_0.shop.GetStartTime()))

def var_0_0.Init(arg_4_0):
	local var_4_0 = arg_4_0.commodity.GetDesc()
	local var_4_1 = var_4_0.name

	if string.match(var_4_1, "(%d+)"):
		setText(arg_4_0.nameTF, shortenString(var_4_1, 5))
	else
		setText(arg_4_0.nameTF, shortenString(var_4_1, 6))

	local var_4_2 = arg_4_0.commodity.GetConsume()

	arg_4_0.consumeTxtTF.text = var_4_2.count

	GetImageSpriteFromAtlasAsync(var_4_2.getConfig("icon"), "", arg_4_0.consumeIconTF)

	arg_4_0.itemCountTF.text = arg_4_0.commodity.GetDropCnt()

	GetImageSpriteFromAtlasAsync(var_4_0.icon, "", arg_4_0.itemIconTF)

	local var_4_3 = var_4_0.rarity or ItemRarity.Gray

	setImageSprite(arg_4_0.itemIconBgTF, GetSpriteFromAtlas("weaponframes", "bg" .. ItemRarity.Rarity2Print(var_4_3)))
	setImageColor(arg_4_0.itemIconFrameTF, Color.NewHex(ItemRarity.Rarity2FrameHexColor(var_4_3)))

def var_0_0.Dispose(arg_5_0):
	return

return var_0_0
