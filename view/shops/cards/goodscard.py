local var_0_0 = class("GoodsCard", import(".BaseGoodsCard"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.go = arg_1_1
	arg_1_0.tr = tf(arg_1_1)
	arg_1_0.mask = arg_1_0.tr.Find("mask")
	arg_1_0.selloutTag = arg_1_0.tr.Find("mask/tag/sellout_tag")

	setText(arg_1_0.selloutTag, i18n("common_sale_out"))

	arg_1_0.levelTag = arg_1_0.tr.Find("mask/tag/level_tag")

	setText(arg_1_0.levelTag, i18n("shop_charge_level_limit"))

	arg_1_0.levelTagText = arg_1_0.tr.Find("mask/tag/level_tag/Text")
	arg_1_0.stars = arg_1_0.tr.Find("item/icon_bg/stars")
	arg_1_0.itemTF = findTF(arg_1_0.tr, "item")
	arg_1_0.nameTxt = findTF(arg_1_0.tr, "item/name_mask/name")
	arg_1_0.discountTF = findTF(arg_1_0.tr, "item/discount")
	arg_1_0.discountTextTF = findTF(arg_1_0.discountTF, "Text").GetComponent(typeof(Text))
	arg_1_0.countTF = findTF(arg_1_0.tr, "item/consume/contain/Text").GetComponent(typeof(Text))
	arg_1_0.resIconTF = findTF(arg_1_0.tr, "item/consume/contain/icon").GetComponent(typeof(Image))
	arg_1_0.itemIconTF = arg_1_0.itemTF.Find("icon_bg/icon").GetComponent(typeof(Image))
	arg_1_0.itemCountTF = arg_1_0.itemTF.Find("icon_bg/count").GetComponent(typeof(Text))
	arg_1_0.maskTip = i18n("buy_countLimit")

	onButton(arg_1_0, arg_1_0.mask, function()
		pg.TipsMgr.GetInstance().ShowTips(arg_1_0.maskTip), SFX_PANEL)

def var_0_0.setGroupMask(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.goodsVO.getConfig("group_limit")
	local var_3_1 = var_3_0 > 0 and var_3_0 <= arg_3_1

	if isActive(arg_3_0.mask):
		return

	setActive(arg_3_0.mask, var_3_1)

	if var_3_0 > 0 and var_3_0 <= arg_3_1:
		setActive(arg_3_0.selloutTag, True)
		setActive(arg_3_0.levelTag, False)

def var_0_0.setLevelMask(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.goodsVO.getLevelLimit(arg_4_1)
	local var_4_1 = arg_4_0.goodsVO.isLevelLimit(arg_4_1)

	if isActive(arg_4_0.mask):
		return

	setActive(arg_4_0.mask, var_4_1)

	if var_4_1:
		setText(arg_4_0.levelTagText, tostring(var_4_0))
		setActive(arg_4_0.levelTag, True)
		setActive(arg_4_0.selloutTag, False)

		arg_4_0.maskTip = i18n("charge_level_limit")

def var_0_0.update(arg_5_0, arg_5_1):
	arg_5_0.goodsVO = arg_5_1

	local var_5_0 = arg_5_0.goodsVO.canPurchase()

	setActive(arg_5_0.mask, not var_5_0)
	setActive(arg_5_0.selloutTag, not var_5_0)
	setActive(arg_5_0.stars, False)

	local var_5_1 = arg_5_1.getDropInfo()

	updateDrop(arg_5_0.itemTF, var_5_1)

	local var_5_2 = var_5_1.getConfig("name") or ""

	setText(arg_5_0.nameTxt, shortenString(var_5_2, 6))

	local var_5_3 = ""
	local var_5_4 = arg_5_1.getConfig("resource_num")

	if arg_5_1.getConfig("genre") == ShopArgs.ShoppingStreetLimit:
		var_5_3 = 100 - arg_5_1.discount .. "%OFF"
		var_5_4 = var_5_4 * (arg_5_1.discount / 100)

	setActive(arg_5_0.discountTF, False)

	arg_5_0.discountTF = arg_5_1.activityDiscount and findTF(arg_5_0.tr, "item/discount_activity") or findTF(arg_5_0.tr, "item/discount")
	arg_5_0.discountTextTF = findTF(arg_5_0.discountTF, "Text").GetComponent(typeof(Text))

	setActive(arg_5_0.discountTF, arg_5_1.hasDiscount())

	arg_5_0.discountTextTF.text = var_5_3
	arg_5_0.countTF.text = math.ceil(var_5_4)

	GetImageSpriteFromAtlasAsync(Drop.New({
		type = DROP_TYPE_RESOURCE,
		id = arg_5_1.getConfig("resource_type")
	}).getIcon(), "", tf(arg_5_0.resIconTF))

def var_0_0.OnDispose(arg_6_0):
	arg_6_0.goodsVO = None

return var_0_0
