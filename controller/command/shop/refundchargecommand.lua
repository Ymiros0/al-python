﻿local var_0_0 = class("RefundChargeCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	if (PLATFORM_CODE == PLATFORM_US or PLATFORM_CODE == PLATFORM_JP) and not pg.SdkMgr.GetInstance():CheckAiriCanBuy() then
		print("wait for a second, Do not click quickly~")

		return
	end

	local var_1_0 = arg_1_1:getBody().shopId
	local var_1_1 = getProxy(ShopsProxy)
	local var_1_2 = var_1_1:getFirstChargeList() or {}

	if not var_1_0 then
		return
	end

	local var_1_3 = not table.contains(var_1_2, var_1_0)
	local var_1_4 = Goods.Create({
		shop_id = var_1_0
	}, Goods.TYPE_CHARGE)

	pg.TrackerMgr.GetInstance():Tracking(TRACKING_PURCHASE_CLICK, var_1_0)
	pg.ConnectionMgr.GetInstance():Send(11513, {
		shop_id = var_1_0,
		device = PLATFORM
	}, 11514, function(arg_2_0)
		if arg_2_0.result == 0 then
			if var_1_1.tradeNoPrev ~= arg_2_0.pay_id then
				if (PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US) and pg.SdkMgr.GetInstance():GetIsPlatform() then
					if pg.SdkMgr.GetInstance():CheckAudit() then
						originalPrint("serverTag:audit 请求购买物品")
						pg.SdkMgr.GetInstance():AiriBuy(var_1_4:getConfig("airijp_id"), "audit", arg_2_0.pay_id)
					elseif pg.SdkMgr.GetInstance():CheckPreAudit() then
						originalPrint("serverTag:preAudit 请求购买物品")
						pg.SdkMgr.GetInstance():AiriBuy(var_1_4:getConfig("airijp_id"), "preAudit", arg_2_0.pay_id)
					elseif pg.SdkMgr.GetInstance():CheckPretest() then
						originalPrint("serverTag:preTest 请求购买物品")
						pg.SdkMgr.GetInstance():AiriBuy(var_1_4:getConfig("airijp_id"), "preAudit", arg_2_0.pay_id)
					elseif pg.SdkMgr.GetInstance():CheckGoogleSimulator() then
						originalPrint("serverTag:test 请求购买物品")
						pg.SdkMgr.GetInstance():AiriBuy(var_1_4:getConfig("airijp_id"), "test", arg_2_0.pay_id)
					else
						originalPrint("serverTag:production 请求购买物品")
						pg.SdkMgr.GetInstance():AiriBuy(var_1_4:getConfig("airijp_id"), "production", arg_2_0.pay_id)
					end

					originalPrint("请求购买的airijp_id为：" .. var_1_4:getConfig("airijp_id"))
					originalPrint("请求购买的id为：" .. arg_2_0.pay_id)
				else
					local var_2_0 = var_1_4:firstPayDouble() and var_1_3
					local var_2_1 = getProxy(PlayerProxy):getData()
					local var_2_2 = var_1_4:getConfig("money") * 100
					local var_2_3 = var_1_4:getConfig("name")
					local var_2_4 = 0

					if var_2_0 then
						var_2_4 = var_1_4:getConfig("gem") * 2
					else
						var_2_4 = var_1_4:getConfig("gem") + var_1_4:getConfig("extra_gem")
					end

					local var_2_5 = arg_2_0.pay_id
					local var_2_6 = var_1_4:getConfig("subject")
					local var_2_7 = "-" .. var_2_1.id .. "-" .. var_2_5
					local var_2_8 = arg_2_0.url or ""
					local var_2_9 = arg_2_0.order_sign or ""

					pg.SdkMgr.GetInstance():SdkPay(var_1_4:getConfig("id_str"), var_2_2, var_2_3, var_2_4, var_2_5, var_2_6, var_2_7, var_2_1.name, var_2_8, var_2_9)
				end

				var_1_1.tradeNoPrev = arg_2_0.pay_id

				pg.TrackerMgr.GetInstance():Tracking(TRACKING_PURCHASE, var_1_0)
				getProxy(ShopsProxy):addWaitTimer()
			else
				pg.TipsMgr.GetInstance():ShowTips(i18n("charge_trade_no_error"))
			end
		elseif arg_2_0.result == 6 then
			-- block empty
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("charge", arg_2_0.result))
		end
	end)
end

return var_0_0
