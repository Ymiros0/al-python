﻿local var_0_0 = class("MiniGameData", import(".BaseVO"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_1.id
	arg_1_0.configCsv = arg_1_0:getConfig("config_csv")
	arg_1_0.configCsvKey = arg_1_0:getConfig("config_csv_key")
	arg_1_0.runtimeData = {}
	arg_1_0.exData = nil
	arg_1_0.rank = {}
	arg_1_0._rankCd = 0
end

function var_0_0.bindConfigTable(arg_2_0)
	return pg.mini_game
end

function var_0_0.GetSimpleValue(arg_3_0, arg_3_1)
	return arg_3_0:getConfig("simple_config_data")[arg_3_1]
end

function var_0_0.GetConfigCsvValue(arg_4_0, arg_4_1)
	return pg[arg_4_0.configCsv][arg_4_0.configCsvKey][arg_4_1]
end

function var_0_0.GetConfigCsvLine(arg_5_0, arg_5_1)
	return pg[arg_5_0.configCsv][arg_5_1]
end

function var_0_0.SetRuntimeData(arg_6_0, arg_6_1, arg_6_2)
	arg_6_0.runtimeData[arg_6_1] = arg_6_2
end

function var_0_0.GetRuntimeData(arg_7_0, arg_7_1)
	return arg_7_0.runtimeData[arg_7_1]
end

function var_0_0.CheckInTime(arg_8_0)
	local var_8_0 = getProxy(MiniGameProxy)
	local var_8_1 = arg_8_0:getConfig("hub_id")

	if var_8_0:CheckHasHub(var_8_1) then
		return var_8_0:GetHubByHubId(var_8_1):CheckInTime()
	else
		return false
	end
end

function var_0_0.GetRank(arg_9_0)
	return arg_9_0.rank
end

function var_0_0.SetRank(arg_10_0, arg_10_1)
	arg_10_0._rankCd = GetHalfHour()
	arg_10_0.rank = arg_10_1
end

function var_0_0.CanFetchRank(arg_11_0)
	return pg.TimeMgr.GetInstance():GetServerTime() > arg_11_0._rankCd
end

return var_0_0
