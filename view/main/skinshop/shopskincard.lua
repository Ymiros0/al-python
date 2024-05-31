local var_0_0 = class("ShopSkinCard")
local var_0_1 = pg.ship_data_group
local var_0_2 = pg.shop_template
local var_0_3 = pg.skin_page_template
local var_0_4 = pg.ship_skin_template

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.view = arg_1_2
	arg_1_0._go = arg_1_1
	arg_1_0._tf = tf(arg_1_1)
	arg_1_0._content = arg_1_0._tf:Find("ship/content")
	arg_1_0._mask = arg_1_0._tf:Find("ship/mask")
	arg_1_0._icon = arg_1_0._tf:Find("ship/content/main/bg/icon"):GetComponent(typeof(Image))
	arg_1_0._priceTF = arg_1_0._tf:Find("ship/content/main/bg/price")

	setActive(arg_1_0._priceTF, false)

	arg_1_0._priceIcon = arg_1_0._priceTF:Find("gem"):GetComponent(typeof(Image))
	arg_1_0._priceTxt = arg_1_0._priceTF:Find("gem/Text"):GetComponent(typeof(Text))
	arg_1_0._opriceTxt = arg_1_0._priceTF:Find("originalprice"):GetComponent(typeof(Text))
	arg_1_0._tagTFs = {
		arg_1_0._tf:Find("ship/content/top/tags/tag_hot"),
		arg_1_0._tf:Find("ship/content/top/tags/tag_new"),
		arg_1_0._tf:Find("ship/content/top/tags/tag_advice"),
		arg_1_0._tf:Find("ship/content/top/tags/tag_activity"),
		arg_1_0._tf:Find("ship/content/top/tags/tag_discount"),
		arg_1_0._tf:Find("ship/content/top/tags/tag_nothing"),
		arg_1_0._tf:Find("ship/content/top/tags/tag_bought"),
		arg_1_0._tf:Find("ship/content/top/tags/tag_limit"),
		arg_1_0._tf:Find("ship/content/top/tags/tag_timelimit"),
		arg_1_0._tf:Find("ship/content/top/tags/tag_return")
	}

	onButton(nil, arg_1_0._go, function()
		arg_1_0.view:emit(SkinShopScene.EVENT_ON_CARD_CLICK, arg_1_0)
	end, SFX_PANEL)
end

function var_0_0.update(arg_3_0, arg_3_1)
	arg_3_0.goodsVO = arg_3_1

	local var_3_0 = arg_3_1:getSkinId()

	arg_3_0.shipSkinConfig = var_0_4[var_3_0]

	local var_3_1 = var_0_4[var_3_0].prefab

	arg_3_0._icon.sprite = nil

	LoadSpriteAsync("shipYardIcon/" .. var_3_1, function(arg_4_0)
		if not IsNil(arg_3_0._icon) then
			arg_3_0._icon.sprite = arg_4_0
		end
	end)

	for iter_3_0, iter_3_1 in pairs(arg_3_0._tagTFs) do
		setActive(iter_3_1, false)
	end

	if arg_3_0.goodsVO.type == Goods.TYPE_SKIN then
		local var_3_2 = arg_3_1:getConfig("resource_type")

		arg_3_0._priceIcon.sprite = LoadSprite(Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = var_3_2
		}):getIcon())

		local var_3_3 = arg_3_1:getConfig("resource_num")
		local var_3_4 = arg_3_1:isDisCount()
		local var_3_5, var_3_6 = arg_3_1:GetPrice()

		arg_3_0._priceTxt.text = var_3_5
		arg_3_0._opriceTxt.text = var_3_3

		setActive(go(arg_3_0._opriceTxt), var_3_4 and var_3_6 > 0)

		local var_3_7 = arg_3_1.buyCount == 0
		local var_3_8 = arg_3_1:getConfig("genre") == ShopArgs.SkinShopTimeLimit

		if arg_3_0.view.encoreSkinMap[arg_3_1.id] and var_3_7 then
			setActive(arg_3_0._tagTFs[10], true)
		elseif var_3_8 then
			setActive(arg_3_0._tagTFs[9], true)
		elseif var_3_7 then
			local var_3_9 = arg_3_0.goodsVO:getConfig("tag")

			if var_3_4 or var_3_9 == 5 then
				local var_3_10 = arg_3_0._tagTFs[5]

				setText(var_3_10:Find("Text"), string.format("%0.2f", var_3_6) .. "%")
				setActive(arg_3_0._tagTFs[5], true)
			elseif arg_3_0._tagTFs[var_3_9] then
				setActive(arg_3_0._tagTFs[var_3_9], true)
			else
				setActive(arg_3_0._tagTFs[6], true)
			end
		else
			setActive(arg_3_0._tagTFs[7], true)
		end
	end

	local var_3_11 = 0

	if var_3_0 == 302053 then
		var_3_11 = 39
	elseif var_3_0 == 502052 then
		var_3_11 = 60
	end

	setAnchoredPosition(arg_3_0._icon.gameObject, {
		y = var_3_11
	})
end

function var_0_0.updateSelected(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1 and -26 or -126

	arg_5_0._content.localPosition = Vector3(0, var_5_0, 0)

	local var_5_1 = arg_5_0.goodsVO.type == Goods.TYPE_SKIN

	setActive(arg_5_0._priceTF, arg_5_1 and var_5_1)
	setActive(arg_5_0._mask, not arg_5_1)
end

function var_0_0.Dispose(arg_6_0)
	removeOnButton(arg_6_0._go)

	arg_6_0._go = nil
	arg_6_0._tf = nil
	arg_6_0._tagTFs = nil
end

return var_0_0
