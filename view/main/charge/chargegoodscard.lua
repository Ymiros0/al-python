local var_0_0 = class("ChargeGoodsCard", import("...shops.cards.GoodsCard"))

function var_0_0.update(arg_1_0, arg_1_1)
	arg_1_0.goodsVO = arg_1_1

	local var_1_0 = arg_1_0.goodsVO:canPurchase()

	setActive(arg_1_0.mask, not var_1_0)
	setActive(arg_1_0.stars, false)

	local var_1_1 = arg_1_1:getDropInfo()

	updateDrop(arg_1_0.itemTF, var_1_1)

	local var_1_2 = var_1_1:getConfig("name") or ""

	setText(arg_1_0.nameTxt, shortenString(var_1_2, 6))

	local var_1_3 = arg_1_1:GetPrice()

	arg_1_0.discountTextTF = findTF(arg_1_0.discountTF, "Text"):GetComponent(typeof(Text))

	local var_1_4 = arg_1_1:getConfig("discount")

	setActive(arg_1_0.discountTF, arg_1_1:isDisCount())

	arg_1_0.discountTextTF.text = var_1_4 .. "%OFF"
	arg_1_0.countTF.text = math.ceil(var_1_3)

	GetImageSpriteFromAtlasAsync(Drop.New({
		type = DROP_TYPE_RESOURCE,
		id = arg_1_1:getConfig("resource_type")
	}):getIcon(), "", tf(arg_1_0.resIconTF))
end

return var_0_0
