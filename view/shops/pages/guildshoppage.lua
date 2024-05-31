local var_0_0 = class("GuildShopPage", import(".MilitaryShopPage"))

function var_0_0.getUIName(arg_1_0)
	return "GuildShop"
end

function var_0_0.CanOpen(arg_2_0)
	return true
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.refreshBtn, function()
		local var_4_0 = arg_3_0.shop:GetResetConsume()

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("guild_shop_refresh_all_tip", var_4_0, i18n("word_guildgold")),
			onYes = function()
				if arg_3_0.player:getResource(PlayerConst.ResGuildCoin) < var_4_0 then
					pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_resource"))

					return
				else
					arg_3_0:emit(NewShopsMediator.REFRESH_GUILD_SHOP, true)
				end
			end
		})
	end, SFX_PANEL)

	arg_3_0.purchaseWindow = GuildShopPurchasePanel.New(arg_3_0._tf, arg_3_0.event)
end

function var_0_0.UpdateShop(arg_6_0, ...)
	var_0_0.super.UpdateShop(arg_6_0, ...)

	if arg_6_0.purchaseWindow:isShowing() then
		arg_6_0.purchaseWindow:ExecuteAction("Hide")
	end
end

function var_0_0.OnUpdatePlayer(arg_7_0)
	local var_7_0 = arg_7_0.player

	arg_7_0.exploitTF.text = var_7_0:getResource(PlayerConst.ResGuildCoin)
end

function var_0_0.OnSetUp(arg_8_0)
	var_0_0.super.OnSetUp(arg_8_0)
	arg_8_0:UpdateRefreshBtn()
end

function var_0_0.UpdateRefreshBtn(arg_9_0)
	setButtonEnabled(arg_9_0.refreshBtn, arg_9_0.shop:CanRefresh())
end

function var_0_0.OnInitItem(arg_10_0, arg_10_1)
	local var_10_0 = GuildGoodsCard.New(arg_10_1)

	onButton(arg_10_0, var_10_0._go, function()
		if not var_10_0.goods:CanPurchase() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("buy_countLimit"))

			return
		end

		arg_10_0:OnCardClick(var_10_0)
	end, SFX_PANEL)

	arg_10_0.cards[arg_10_1] = var_10_0
end

function var_0_0.OnCardClick(arg_12_0, arg_12_1)
	if arg_12_1.goods:Selectable() then
		arg_12_0.purchaseWindow:ExecuteAction("Show", {
			id = arg_12_1.goods.id,
			count = arg_12_1.goods:GetMaxCnt(),
			type = arg_12_1.goods:getConfig("type"),
			price = arg_12_1.goods:getConfig("price"),
			displays = arg_12_1.goods:getConfig("goods"),
			num = arg_12_1.goods:getConfig("num")
		})
	else
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			yesText = "text_exchange",
			content = i18n("guild_shop_exchange_tip"),
			onYes = function()
				if not arg_12_1.goods:CanPurchase() then
					pg.TipsMgr.GetInstance():ShowTips(i18n("buy_countLimit"))

					return
				end

				arg_12_0:emit(NewShopsMediator.ON_GUILD_SHOPPING, arg_12_1.goods.id, arg_12_1.goods:GetFirstDropId())
			end
		})
	end
end

function var_0_0.OnTimeOut(arg_14_0)
	arg_14_0:emit(NewShopsMediator.REFRESH_GUILD_SHOP, false)
end

function var_0_0.OnDestroy(arg_15_0)
	var_0_0.super.OnDestroy(arg_15_0)
	arg_15_0.purchaseWindow:Destroy()
end

return var_0_0
