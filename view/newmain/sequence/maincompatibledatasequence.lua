local var_0_0 = class("MainCompatibleDataSequence")

function var_0_0.Execute(arg_1_0, arg_1_1)
	seriesAsync({
		function(arg_2_0)
			getProxy(IslandProxy):CheckAndRequest(arg_2_0)
		end,
		function(arg_3_0)
			arg_1_0:CheckSpecialDayForEducateChar(arg_3_0)
		end
	}, arg_1_1)
end

function var_0_0.CheckSpecialDayForEducateChar(arg_4_0, arg_4_1)
	if LOCK_EDUCATE_SYSTEM then
		arg_4_1()

		return
	end

	local var_4_0 = pg.TimeMgr.GetInstance():GetServerTime()
	local var_4_1, var_4_2, var_4_3 = ChineseCalendar.GetCurrYearMonthDay(var_4_0)
	local var_4_4 = getProxy(PlayerProxy):getRawData():ExistEducateChar()
	local var_4_5 = getProxy(SettingsProxy)

	if var_4_4 and var_4_5:GetFlagShipDisplayMode() ~= FlAG_SHIP_DISPLAY_ONLY_SHIP and not var_4_5:IsTipDay(var_4_1, var_4_2, var_4_3) and ChineseCalendar.AnySpecialDay(var_4_1, var_4_2, var_4_3) then
		local var_4_6, var_4_7 = PlayerVitaeShipsPage.GetSlotMaxCnt()
		local var_4_8 = var_4_7 + 1

		if var_4_8 and var_4_8 > 0 then
			var_4_5:setCurrentSecretaryIndex(var_4_8)
		end
	end

	arg_4_1()
end

return var_0_0
