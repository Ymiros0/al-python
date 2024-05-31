local var_0_0 = class("FragmentShopPage", import(".ShamShopPage"))

function var_0_0.getUIName(arg_1_0)
	return "FragmentShop"
end

function var_0_0.GetPaintingCommodityUpdateVoice(arg_2_0)
	return
end

function var_0_0.CanOpen(arg_3_0, arg_3_1, arg_3_2)
	return pg.SystemOpenMgr.GetInstance():isOpenSystem(arg_3_2.level, "FragmentShop")
end

function var_0_0.OnLoaded(arg_4_0)
	arg_4_0.dayTxt = arg_4_0:findTF("time/day"):GetComponent(typeof(Text))
	arg_4_0.fragment = arg_4_0:findTF("res_fragment/count"):GetComponent(typeof(Text))
	arg_4_0.resolveBtn = arg_4_0:findTF("res_fragment/resolve")
	arg_4_0.urRes = arg_4_0:findTF("res_ur/count"):GetComponent(typeof(Text))
end

function var_0_0.OnInit(arg_5_0)
	var_0_0.super.OnInit(arg_5_0)
	onButton(arg_5_0, arg_5_0.resolveBtn, function()
		if not arg_5_0.resolvePanel then
			arg_5_0.resolvePanel = FragResolvePanel.New(arg_5_0)

			arg_5_0.resolvePanel:Load()
		end

		arg_5_0.resolvePanel.buffer:Reset()
		arg_5_0.resolvePanel.buffer:Trigger("control")
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0:findTF("res_fragment"), function()
		arg_5_0:emit(BaseUI.ON_ITEM, id2ItemId(PlayerConst.ResBlueprintFragment))
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0:findTF("res_ur"), function()
		local var_8_0 = pg.gameset.urpt_chapter_max.description[1]

		arg_5_0:emit(BaseUI.ON_ITEM, var_8_0)
	end, SFX_PANEL)
end

function var_0_0.OnUpdatePlayer(arg_9_0)
	local var_9_0 = arg_9_0.player
	local var_9_1 = arg_9_0.player:getResource(PlayerConst.ResBlueprintFragment)

	arg_9_0.fragment.text = var_9_1
end

function var_0_0.OnFragmentSellUpdate(arg_10_0)
	if arg_10_0.resolvePanel then
		arg_10_0.resolvePanel.buffer:Reset()
		arg_10_0.resolvePanel.buffer:Trigger("control")
	end
end

function var_0_0.OnUpdateItems(arg_11_0)
	if not LOCK_UR_SHIP then
		local var_11_0 = pg.gameset.urpt_chapter_max.description[1]
		local var_11_1 = arg_11_0.items[var_11_0] or {
			count = 0
		}

		arg_11_0.urRes.text = var_11_1.count
	else
		setActive(arg_11_0:findTF("res_ur"), false)
		setAnchoredPosition(arg_11_0:findTF("res_fragment"), {
			x = 938.5
		})
	end
end

function var_0_0.OnUpdateCommodity(arg_12_0, arg_12_1)
	local var_12_0

	for iter_12_0, iter_12_1 in pairs(arg_12_0.cards) do
		if iter_12_1.goodsVO.id == arg_12_1.id then
			var_12_0 = iter_12_1

			break
		end
	end

	if var_12_0 then
		var_12_0.goodsVO = arg_12_1

		ActivityGoodsCard.StaticUpdate(var_12_0.tr, arg_12_1, var_0_0.TYPE_FRAGMENT)
	end
end

function var_0_0.OnInitItem(arg_13_0, arg_13_1)
	local var_13_0 = ActivityGoodsCard.New(arg_13_1)

	onButton(arg_13_0, var_13_0.tr, function()
		if not var_13_0.goodsVO:canPurchase() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("buy_countLimit"))

			return
		end

		arg_13_0:OnClickCommodity(var_13_0.goodsVO, function(arg_15_0, arg_15_1)
			arg_13_0:OnPurchase(arg_15_0, arg_15_1)
		end)
	end, SFX_PANEL)

	arg_13_0.cards[arg_13_1] = var_13_0
end

function var_0_0.OnUpdateItem(arg_16_0, arg_16_1, arg_16_2)
	local var_16_0 = arg_16_0.cards[arg_16_2]

	if not var_16_0 then
		arg_16_0:OnInitItem(arg_16_2)

		var_16_0 = arg_16_0.cards[arg_16_2]
	end

	local var_16_1 = arg_16_0.displays[arg_16_1 + 1]

	var_16_0.goodsVO = var_16_1

	ActivityGoodsCard.StaticUpdate(var_16_0.tr, var_16_1, var_0_0.TYPE_FRAGMENT)
end

function var_0_0.OnPurchase(arg_17_0, arg_17_1, arg_17_2)
	arg_17_0:emit(NewShopsMediator.ON_FRAGMENT_SHOPPING, arg_17_1.id, arg_17_2)
end

function var_0_0.OnDestroy(arg_18_0)
	var_0_0.super.OnDestroy(arg_18_0)

	if arg_18_0.resolvePanel then
		arg_18_0.resolvePanel:Destroy()

		arg_18_0.resolvePanel = nil
	end
end

return var_0_0
