﻿local var_0_0 = class("AiriUSTracker")

var_0_0.DEV_TOKEN = "2KtJzaeLzGnPUhtOY4-LYw"
var_0_0.ANDROID_LINK_ID = "DE31AE06D3CE21EE3A9E1A1BCEB506E1"
var_0_0.IOS_LINK_ID = "F7FE029D3F957A107D358D2BB93CA7E2"

function var_0_0.Ctor(arg_1_0)
	arg_1_0.mapping = {}
	arg_1_0.mapping[TRACKING_ROLE_CREATE] = "role_create"
	arg_1_0.mapping[TRACKING_ROLE_LOGIN] = "role_login"
	arg_1_0.mapping[TRACKING_TUTORIAL_COMPLETE_1] = "tutorial_complete_1"
	arg_1_0.mapping[TRACKING_TUTORIAL_COMPLETE_2] = "tutorial_complete_2"
	arg_1_0.mapping[TRACKING_TUTORIAL_COMPLETE_3] = "tutorial_complete_3"
	arg_1_0.mapping[TRACKING_TUTORIAL_COMPLETE_4] = "tutorial_complete_4"
	arg_1_0.mapping[TRACKING_USER_LEVELUP] = "user_levelup"
	arg_1_0.mapping[TRACKING_ROLE_LOGOUT] = "role_logout"
	arg_1_0.mapping[TRACKING_PURCHASE_FIRST] = "purchase_first"
	arg_1_0.mapping[TRACKING_PURCHASE_CLICK] = "purchase_click"
	arg_1_0.mapping[TRACKING_PURCHASE_CLICK_MONTHLYCARD] = "purchase_click_monthlycard"
	arg_1_0.mapping[TRACKING_PURCHASE_CLICK_GIFTBAG] = "purchase_click_giftbag"
	arg_1_0.mapping[TRACKING_PURCHASE_CLICK_DIAMOND] = "purchase_click_diamond"
	arg_1_0.mapping[TRACKING_PURCHASE] = "purchase"
	arg_1_0.mapping[TRACKING_2D_RETENTION] = "2d_retention"
	arg_1_0.mapping[TRACKING_7D_RETENTION] = "7d_retention"
end

function var_0_0.Tracking(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	local var_2_0 = arg_2_0.mapping[arg_2_1]

	if var_2_0 == nil then
		return
	end

	if arg_2_1 == TRACKING_USER_LEVELUP then
		originalPrint("tracking lvl:" .. arg_2_3)

		local var_2_1 = AiriUserEvent.New(var_2_0)

		var_2_1:AddParam("lvl", arg_2_3)
		var_2_1:AddParam("user_id", arg_2_2)
		pg.SdkMgr.GetInstance():UserEventUpload(var_2_1)
	elseif arg_2_1 == TRACKING_PURCHASE_CLICK then
		local var_2_2 = AiriUserEvent.New(var_2_0)

		var_2_2:AddParam("user_id", arg_2_2)
		pg.SdkMgr.GetInstance():UserEventUpload(var_2_2)
	elseif arg_2_1 == TRACKING_PURCHASE_FIRST then
		originalPrint("order id : " .. arg_2_3)

		local var_2_3 = AiriUserEvent.New(var_2_0)

		var_2_3:AddParam("user_id", arg_2_2)
		var_2_3:AddParam("order_id", arg_2_3)
		pg.SdkMgr.GetInstance():UserEventUpload(var_2_3)
	elseif arg_2_1 == TRACKING_2D_RETENTION or arg_2_1 == TRACKING_7D_RETENTION then
		local var_2_4 = AiriUserEvent.New(var_2_0)

		var_2_4:AddParam("user_id", arg_2_2)
		pg.SdkMgr.GetInstance():UserEventUpload(var_2_4)
	elseif arg_2_1 ~= TRACKING_PURCHASE then
		local var_2_5 = AiriUserEvent.New(var_2_0)

		var_2_5:AddParam("user_id", arg_2_2)
		pg.SdkMgr.GetInstance():UserEventUpload(var_2_5)
	end

	if pg.SdkMgr.GetInstance():GetChannelUID() == "0" then
		if arg_2_1 == TRACKING_PURCHASE_CLICK then
			local var_2_6 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

			arg_2_0:YS_S2S(var_0_0.DEV_TOKEN, "DE31AE06D3CE21EE3A9E1A1BCEB506E1", "Azur Lane (Android) S2S_purchase_click", "", tostring(var_2_6), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
		elseif arg_2_1 == TRACKING_PURCHASE_CLICK_MONTHLYCARD then
			local var_2_7 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

			arg_2_0:YS_S2S(var_0_0.DEV_TOKEN, "DE31AE06D3CE21EE3A9E1A1BCEB506E1", "Azur Lane (Android) S2S_purchase_click_monthlycard", "", tostring(var_2_7), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
		elseif arg_2_1 == TRACKING_PURCHASE_CLICK_DIAMOND then
			local var_2_8 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

			arg_2_0:YS_S2S(var_0_0.DEV_TOKEN, "DE31AE06D3CE21EE3A9E1A1BCEB506E1", "Azur Lane (Android) S2S_purchase_click_diamond", "", tostring(var_2_8), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
		elseif arg_2_1 == TRACKING_PURCHASE_CLICK_GIFTBAG then
			local var_2_9 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

			arg_2_0:YS_S2S(var_0_0.DEV_TOKEN, "DE31AE06D3CE21EE3A9E1A1BCEB506E1", "Azur Lane (Android) S2S_purchase_click_giftbag", "", tostring(var_2_9), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
		elseif arg_2_1 == TRACKING_PURCHASE then
			local var_2_10 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

			arg_2_0:YS_S2S(var_0_0.DEV_TOKEN, "DE31AE06D3CE21EE3A9E1A1BCEB506E1", "Azur Lane (Android) S2S_purchase", "", tostring(var_2_10), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
		end
	elseif arg_2_1 == TRACKING_PURCHASE_CLICK then
		local var_2_11 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

		YS2S.S2S(var_0_0.DEV_TOKEN, "F7FE029D3F957A107D358D2BB93CA7E2", "Azur Lane (iOS) S2S_purchase_click", "", tostring(var_2_11), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
	elseif arg_2_1 == TRACKING_PURCHASE_CLICK_MONTHLYCARD then
		local var_2_12 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

		YS2S.S2S(var_0_0.DEV_TOKEN, "F7FE029D3F957A107D358D2BB93CA7E2", "Azur Lane (iOS) S2S_purchase_click_monthlycard", "", tostring(var_2_12), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
	elseif arg_2_1 == TRACKING_PURCHASE_CLICK_DIAMOND then
		local var_2_13 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

		YS2S.S2S(var_0_0.DEV_TOKEN, "F7FE029D3F957A107D358D2BB93CA7E2", "Azur Lane (iOS) S2S_purchase_click_diamond", "", tostring(var_2_13), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
	elseif arg_2_1 == TRACKING_PURCHASE_CLICK_GIFTBAG then
		local var_2_14 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

		YS2S.S2S(var_0_0.DEV_TOKEN, "F7FE029D3F957A107D358D2BB93CA7E2", "Azur Lane (iOS) S2S_purchase_click_giftbag", "", tostring(var_2_14), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
	elseif arg_2_1 == TRACKING_PURCHASE then
		local var_2_15 = arg_2_0:transMoney(pg.pay_data_display[arg_2_3].money)

		YS2S.S2S(var_0_0.DEV_TOKEN, "F7FE029D3F957A107D358D2BB93CA7E2", "Azur Lane (iOS) S2S_purchase", "", tostring(var_2_15), pg.SdkMgr.GetInstance():GetDeviceId(), tostring(pg.TimeMgr.GetInstance():GetServerTime()))
	end

	originalPrint("track done.")
end

function var_0_0.YS_S2S(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5, arg_3_6, arg_3_7)
	local var_3_0 = pg.SdkMgr.GetInstance():GetChannelUID() == "0"
	local var_3_1 = "https://www.googleadservices.com/pagead/conversion/app/1.0?"
	local var_3_2 = {
		dev_token = arg_3_1,
		link_id = arg_3_2
	}

	var_3_2.app_event_type = "custom"
	var_3_2.app_event_name = arg_3_3

	if arg_3_4 then
		var_3_2.app_event_data = arg_3_4
	end

	var_3_2.rdid = arg_3_6

	if var_3_0 then
		var_3_2.id_type = "advertisingid"
	else
		var_3_2.id_type = "idfa"
	end

	var_3_2.lat = "0"
	var_3_2.app_version = Application.version
	var_3_2.os_version = SystemInfo.operatingSystem
	var_3_2.sdk_version = "1.9.5r6"
	var_3_2.timestamp = arg_3_7 .. ".000001"
	var_3_2.value = arg_3_5
	var_3_2.currency_code = "USD"

	for iter_3_0, iter_3_1 in pairs(var_3_2) do
		var_3_1 = var_3_1 .. iter_3_0 .. "=" .. iter_3_1 .. "&"
	end

	local var_3_3 = string.sub(var_3_1, 1, -2)

	originalPrint(var_3_1)
	VersionMgr.Inst:WebRequest(var_3_3, function(arg_4_0, arg_4_1)
		originalPrint("code:" .. arg_4_0 .. " content:" .. arg_4_1)
	end)
end

function var_0_0.transMoney(arg_5_0, arg_5_1)
	return string.format("%.2f", arg_5_1 / 100)
end

return var_0_0
