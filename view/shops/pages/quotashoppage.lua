local var_0_0 = class("QuotaShopPage", import(".BaseShopPage"))

function var_0_0.getUIName(arg_1_0)
	return "QuotaShop"
end

function var_0_0.GetPaintingCommodityUpdateVoice(arg_2_0)
	return
end

function var_0_0.CanOpen(arg_3_0, arg_3_1, arg_3_2)
	return pg.SystemOpenMgr.GetInstance():isOpenSystem(arg_3_2.level, "QuotaShop")
end

function var_0_0.OnLoaded(arg_4_0)
	arg_4_0.nanoTxt = arg_4_0:findTF("res_nano/Text"):GetComponent(typeof(Text))
end

function var_0_0.OnInit(arg_5_0)
	setText(arg_5_0._tf:Find("title/tip"), i18n("quota_shop_description"))
end

function var_0_0.OnUpdateItems(arg_6_0)
	local var_6_0 = arg_6_0.items[ChapterConst.ShamMoneyItem]

	if not var_6_0 then
		arg_6_0.nanoTxt.text = 0
	else
		arg_6_0.nanoTxt.text = var_6_0.count
	end
end

function var_0_0.OnUpdateCommodity(arg_7_0, arg_7_1)
	local var_7_0

	for iter_7_0, iter_7_1 in pairs(arg_7_0.cards) do
		if iter_7_1.goodsVO.id == arg_7_1.id then
			var_7_0 = iter_7_1

			break
		end
	end

	if var_7_0 then
		var_7_0:update(arg_7_1)
	end
end

function var_0_0.OnInitItem(arg_8_0, arg_8_1)
	local var_8_0 = QuotaGoodsCard.New(arg_8_1)

	onButton(arg_8_0, var_8_0.tr, function()
		if not var_8_0.goodsVO:canPurchase() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("buy_countLimit"))

			return
		end

		arg_8_0:OnClickCommodity(var_8_0.goodsVO, function(arg_10_0, arg_10_1)
			arg_8_0:OnPurchase(arg_10_0, arg_10_1)
		end)
	end, SFX_PANEL)

	arg_8_0.cards[arg_8_1] = var_8_0
end

function var_0_0.OnUpdateItem(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = arg_11_0.cards[arg_11_2]

	if not var_11_0 then
		arg_11_0:OnInitItem(arg_11_2)

		var_11_0 = arg_11_0.cards[arg_11_2]
	end

	local var_11_1 = arg_11_0.displays[arg_11_1 + 1]

	var_11_0:update(var_11_1)
end

function var_0_0.OnUpdateAll(arg_12_0)
	arg_12_0:InitCommodities()
end

function var_0_0.OnPurchase(arg_13_0, arg_13_1, arg_13_2)
	arg_13_0:emit(NewShopsMediator.ON_QUOTA_SHOPPING, arg_13_1.id, arg_13_2)
end

function var_0_0.OnDestroy(arg_14_0)
	return
end

return var_0_0
