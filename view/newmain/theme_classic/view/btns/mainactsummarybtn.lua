﻿local var_0_0 = class("MainActSummaryBtn", import(".MainBaseActivityBtn"))

function var_0_0.GetEventName(arg_1_0)
	return "event_all"
end

function var_0_0.GetTipImage(arg_2_0)
	return "tip_1920"
end

function var_0_0.GetActivityID(arg_3_0)
	return nil
end

function var_0_0.OnInit(arg_4_0)
	arg_4_0:PickPriortyActAsyn(function(arg_5_0, arg_5_1)
		arg_4_0.priority = arg_5_0

		if arg_5_1 > 0 then
			arg_4_0.tipTxt.text = arg_5_1
		end

		setActive(arg_4_0.tipTr.gameObject, arg_5_1 > 0)
	end)
end

function var_0_0.PickPriortyActAsyn(arg_6_0, arg_6_1)
	local var_6_0 = {}
	local var_6_1 = 0
	local var_6_2

	table.insert(var_6_0, function(arg_7_0)
		local var_7_0, var_7_1 = arg_6_0:CollectActivity()

		var_6_2 = var_7_1
		var_6_1 = var_6_1 + var_7_0

		onNextTick(arg_7_0)
	end)
	table.insert(var_6_0, function(arg_8_0)
		local var_8_0 = arg_6_0:CollectActEntrance()

		var_6_1 = var_6_1 + var_8_0

		onNextTick(arg_8_0)
	end)
	seriesAsync(var_6_0, function()
		arg_6_1(var_6_2, var_6_1)
	end)
end

function var_0_0.CollectActivity(arg_10_0)
	local var_10_0 = 0
	local var_10_1
	local var_10_2 = getProxy(ActivityProxy):getRawData()

	for iter_10_0, iter_10_1 in pairs(var_10_2) do
		if not iter_10_1:isEnd() and iter_10_1:isShow() and iter_10_1:readyToAchieve() then
			var_10_0 = var_10_0 + 1

			if not var_10_1 or var_10_1 and var_10_1.id > iter_10_1.id then
				var_10_1 = iter_10_1
			end
		end
	end

	return var_10_0, var_10_1
end

function var_0_0.CollectActEntrance(arg_11_0)
	local var_11_0 = 0
	local var_11_1 = ActivityMainScene.GetOnShowEntranceData()

	return #_.filter(var_11_1, function(arg_12_0)
		return arg_12_0.isTip and arg_12_0.isTip()
	end)
end

function var_0_0.CustomOnClick(arg_13_0)
	pg.m02:sendNotification(GAME.GO_SCENE, SCENE.CARD_TOWER_MODE_SELECT)
end

return var_0_0
