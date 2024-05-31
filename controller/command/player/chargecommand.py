local var_0_0 = class("ChargeCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	if (PLATFORM_CODE == PLATFORM_US or PLATFORM_CODE == PLATFORM_JP) and not pg.SdkMgr.GetInstance().CheckAiriCanBuy():
		originalPrint("wait for a second, Do not click quickly~")

		return

	local var_1_0 = arg_1_1.getBody().shopId
	local var_1_1 = getProxy(ShopsProxy)
	local var_1_2 = var_1_1.getFirstChargeList() or {}

	if not var_1_0:
		return

	local var_1_3 = not table.contains(var_1_2, var_1_0)
	local var_1_4 = Goods.Create({
		shop_id = var_1_0
	}, Goods.TYPE_CHARGE)

	pg.TrackerMgr.GetInstance().Tracking(TRACKING_PURCHASE_CLICK, var_1_0)
	print("=================ChargeCommand test======================")
	print(tostring(PLATFORM))
	pg.ConnectionMgr.GetInstance().Send(11501, {
		shop_id = var_1_0,
		device = PLATFORM
	}, 11502, function(arg_2_0)
		if arg_2_0.result == 0:
			if var_1_1.tradeNoPrev != arg_2_0.pay_id:
				if (PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US) and pg.SdkMgr.GetInstance().GetIsPlatform():
					if pg.SdkMgr.GetInstance().CheckAudit():
						originalPrint("serverTag.audit 请求购买物品")
						pg.SdkMgr.GetInstance().AiriBuy(var_1_4.getConfig("airijp_id"), "audit", arg_2_0.pay_id)
					elif pg.SdkMgr.GetInstance().CheckPreAudit():
						originalPrint("serverTag.preAudit 请求购买物品")
						pg.SdkMgr.GetInstance().AiriBuy(var_1_4.getConfig("airijp_id"), "preAudit", arg_2_0.pay_id)
					elif pg.SdkMgr.GetInstance().CheckPretest():
						originalPrint("serverTag.preTest 请求购买物品")
						pg.SdkMgr.GetInstance().AiriBuy(var_1_4.getConfig("airijp_id"), "preAudit", arg_2_0.pay_id)
					elif pg.SdkMgr.GetInstance().CheckGoogleSimulator():
						originalPrint("serverTag.test 请求购买物品")
						pg.SdkMgr.GetInstance().AiriBuy(var_1_4.getConfig("airijp_id"), "test", arg_2_0.pay_id)
					else
						originalPrint("serverTag.production 请求购买物品")
						pg.SdkMgr.GetInstance().AiriBuy(var_1_4.getConfig("airijp_id"), "production", arg_2_0.pay_id)

					originalPrint("请求购买的airijp_id为：" .. var_1_4.getConfig("airijp_id"))
					originalPrint("请求购买的id为：" .. arg_2_0.pay_id)
				else
					local var_2_0 = var_1_4.firstPayDouble() and var_1_3
					local var_2_1 = getProxy(PlayerProxy).getData()
					local var_2_2 = var_1_4.RawGetConfig("money") * 100
					local var_2_3 = var_1_4.getConfig("name")

					if PLATFORM_CODE == PLATFORM_CH and pg.SdkMgr.GetInstance().GetChannelUID() == "21" and var_1_0 == 1001:
						var_2_3 = "特许巡游凭证(202111)"

					local var_2_4 = 0

					if var_2_0:
						var_2_4 = var_1_4.getConfig("gem") * 2
					else
						var_2_4 = var_1_4.getConfig("gem") + var_1_4.getConfig("extra_gem")

					local var_2_5 = arg_2_0.pay_id
					local var_2_6 = var_1_4.getConfig("subject")
					local var_2_7 = "-" .. var_2_1.id .. "-" .. var_2_5
					local var_2_8 = arg_2_0.url or ""
					local var_2_9 = arg_2_0.order_sign or ""

					pg.SdkMgr.GetInstance().SdkPay(var_1_4.getConfig("id_str"), var_2_2, var_2_3, var_2_4, var_2_5, var_2_6, var_2_7, var_2_1.name, var_2_8, var_2_9)

				var_1_1.tradeNoPrev = arg_2_0.pay_id

				pg.TrackerMgr.GetInstance().Tracking(TRACKING_PURCHASE, var_1_0)
				getProxy(ShopsProxy).addWaitTimer()
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("charge_trade_no_error"))
		elif arg_2_0.result == 6:
			pg.TipsMgr.GetInstance().ShowTips(i18n("charge_error_count_limit"))
		elif arg_2_0.result == 5002:
			pg.TipsMgr.GetInstance().ShowTips(i18n("charge_error_disable"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("charge", arg_2_0.result)))

return var_0_0
