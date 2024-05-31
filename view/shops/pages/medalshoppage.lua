local var_0_0 = class("MedalShopPage", import(".MilitaryShopPage"))

function var_0_0.getUIName(arg_1_0)
	return "MedalShop"
end

function var_0_0.CanOpen(arg_2_0)
	return true
end

function var_0_0.OnLoaded(arg_3_0)
	arg_3_0.exploitTF = arg_3_0._tf:Find("res_exploit/bg/Text"):GetComponent(typeof(Text))
	arg_3_0.timerTF = arg_3_0._tf:Find("time/day"):GetComponent(typeof(Text))

	setText(arg_3_0._tf:Find("time"), i18n("title_limit_time"))
	setText(arg_3_0._tf:Find("time/text"), i18n("shops_rest_day"))
	setText(arg_3_0._tf:Find("time/text_day"), i18n("word_date"))
end

function var_0_0.OnInit(arg_4_0)
	arg_4_0.purchaseWindow = MedalShopPurchasePanel.New(arg_4_0._tf, arg_4_0.event)
	arg_4_0.multiWindow = MedalShopMultiWindow.New(arg_4_0._tf, arg_4_0.event)
end

function var_0_0.UpdateShop(arg_5_0, ...)
	var_0_0.super.UpdateShop(arg_5_0, ...)

	if arg_5_0.purchaseWindow:isShowing() then
		arg_5_0.purchaseWindow:ExecuteAction("Hide")
	end

	if arg_5_0.multiWindow:isShowing() then
		arg_5_0.multiWindow:ExecuteAction("Hide")
	end
end

function var_0_0.OnUpdatePlayer(arg_6_0)
	return
end

function var_0_0.OnUpdateItems(arg_7_0)
	local var_7_0 = arg_7_0.items

	arg_7_0.exploitTF.text = var_7_0[ITEM_ID_SILVER_HOOK] and var_7_0[ITEM_ID_SILVER_HOOK].count or 0
end

function var_0_0.OnInitItem(arg_8_0, arg_8_1)
	local var_8_0 = MedalGoodsCard.New(arg_8_1)

	onButton(arg_8_0, var_8_0._go, function()
		if not var_8_0.goods:CanPurchase() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("buy_countLimit"))

			return
		end

		arg_8_0:OnCardClick(var_8_0)
	end, SFX_PANEL)

	arg_8_0.cards[arg_8_1] = var_8_0
end

function var_0_0.OnCardClick(arg_10_0, arg_10_1)
	if arg_10_1.goods:Selectable() then
		arg_10_0.purchaseWindow:ExecuteAction("Show", {
			id = arg_10_1.goods.id,
			count = arg_10_1.goods:GetMaxCnt(),
			type = arg_10_1.goods:getConfig("type"),
			price = arg_10_1.goods:getConfig("price"),
			displays = arg_10_1.goods:getConfig("goods"),
			num = arg_10_1.goods:getConfig("num")
		})
	elseif arg_10_1.goods:getConfig("goods_type") == 1 and arg_10_1.goods:GetLimit() > 1 then
		arg_10_0.multiWindow:ExecuteAction("Show", arg_10_1.goods, function(arg_11_0)
			if not arg_10_1.goods:CanPurchaseCnt(arg_11_0) then
				pg.TipsMgr.GetInstance():ShowTips(i18n("buy_countLimit"))

				return
			end

			local var_11_0 = {}
			local var_11_1 = arg_10_1.goods:getConfig("goods")[1]

			for iter_11_0 = 1, arg_11_0 do
				table.insert(var_11_0, var_11_1)
			end

			arg_10_0:emit(NewShopsMediator.ON_MEDAL_SHOPPING, arg_10_1.goods.id, var_11_0)
		end)
	else
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			yesText = "text_exchange",
			content = i18n("guild_shop_exchange_tip"),
			onYes = function()
				if not arg_10_1.goods:CanPurchase() then
					pg.TipsMgr.GetInstance():ShowTips(i18n("buy_countLimit"))

					return
				end

				arg_10_0:emit(NewShopsMediator.ON_MEDAL_SHOPPING, arg_10_1.goods.id, arg_10_1.goods:GetFirstDropId())
			end
		})
	end
end

function var_0_0.AddTimer(arg_13_0)
	local var_13_0 = arg_13_0.shop.nextTime + 1

	arg_13_0.timer = Timer.New(function()
		local var_14_0 = var_13_0 - pg.TimeMgr.GetInstance():GetServerTime()

		if var_14_0 <= 0 then
			arg_13_0:RemoveTimer()
			arg_13_0:OnTimeOut()
		elseif arg_13_0.timerTF.text ~= tostring(1 + math.floor((var_14_0 - 1) / 86400)) then
			arg_13_0.timerTF.text = string.format("%02d", 1 + math.floor((var_14_0 - 1) / 86400))
		end
	end, 1, -1)

	arg_13_0.timer:Start()
	arg_13_0.timer.func()
end

function var_0_0.OnTimeOut(arg_15_0)
	arg_15_0:emit(NewShopsMediator.REFRESH_MEDAL_SHOP, false)
end

function var_0_0.OnDestroy(arg_16_0)
	var_0_0.super.OnDestroy(arg_16_0)
	arg_16_0.purchaseWindow:Destroy()
	arg_16_0.multiWindow:Destroy()
end

return var_0_0
