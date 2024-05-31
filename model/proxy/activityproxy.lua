local var_0_0 = class("ActivityProxy", import(".NetProxy"))

var_0_0.ACTIVITY_ADDED = "ActivityProxy ACTIVITY_ADDED"
var_0_0.ACTIVITY_UPDATED = "ActivityProxy ACTIVITY_UPDATED"
var_0_0.ACTIVITY_DELETED = "ActivityProxy ACTIVITY_DELETED"
var_0_0.ACTIVITY_OPERATION_DONE = "ActivityProxy ACTIVITY_OPERATION_DONE"
var_0_0.ACTIVITY_SHOW_AWARDS = "ActivityProxy ACTIVITY_SHOW_AWARDS"
var_0_0.ACTIVITY_SHOP_SHOW_AWARDS = "ActivityProxy ACTIVITY_SHOP_SHOW_AWARDS"
var_0_0.ACTIVITY_SHOW_BB_RESULT = "ActivityProxy ACTIVITY_SHOW_BB_RESULT"
var_0_0.ACTIVITY_LOTTERY_SHOW_AWARDS = "ActivityProxy ACTIVITY_LOTTERY_SHOW_AWARDS"
var_0_0.ACTIVITY_HITMONSTER_SHOW_AWARDS = "ActivityProxy ACTIVITY_HITMONSTER_SHOW_AWARDS"
var_0_0.ACTIVITY_SHOW_REFLUX_AWARDS = "ActivityProxy ACTIVITY_SHOW_REFLUX_AWARDS"
var_0_0.ACTIVITY_OPERATION_ERRO = "ActivityProxy ACTIVITY_OPERATION_ERRO"
var_0_0.ACTIVITY_SHOW_LOTTERY_AWARD_RESULT = "ActivityProxy ACTIVITY_SHOW_LOTTERY_AWARD_RESULT"
var_0_0.ACTIVITY_SHOW_RED_PACKET_AWARDS = "ActivityProxy ACTIVITY_SHOW_RED_PACKET_AWARDS"
var_0_0.ACTIVITY_SHOW_SHAKE_BEADS_RESULT = "ActivityProxy ACTIVITY_SHOW_SHAKE_BEADS_RESULT"
var_0_0.ACTIVITY_PT_ID = 110

function var_0_0.register(arg_1_0)
	arg_1_0:on(11200, function(arg_2_0)
		arg_1_0.data = {}
		arg_1_0.params = {}
		arg_1_0.hxList = {}
		arg_1_0.buffActs = {}

		if arg_2_0.hx_list then
			for iter_2_0, iter_2_1 in ipairs(arg_2_0.hx_list) do
				table.insert(arg_1_0.hxList, iter_2_1)
			end
		end

		for iter_2_2, iter_2_3 in ipairs(arg_2_0.activity_list) do
			if not pg.activity_template[iter_2_3.id] then
				Debugger.LogError("活动acvitity_template不存在: " .. iter_2_3.id)
			else
				local var_2_0 = Activity.Create(iter_2_3)
				local var_2_1 = var_2_0:getConfig("type")

				if var_2_1 == ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2 then
					if var_2_0:checkBattleTimeInBossAct() then
						arg_1_0:InitActtivityFleet(var_2_0, iter_2_3)
					end
				elseif var_2_1 == ActivityConst.ACTIVITY_TYPE_CHALLENGE then
					arg_1_0:InitActtivityFleet(var_2_0, iter_2_3)
				elseif var_2_1 == ActivityConst.ACTIVITY_TYPE_PARAMETER then
					arg_1_0:addActivityParameter(var_2_0)
				elseif var_2_1 == ActivityConst.ACTIVITY_TYPE_BUFF then
					table.insert(arg_1_0.buffActs, var_2_0.id)
				elseif var_2_1 == ActivityConst.ACTIVITY_TYPE_BOSSRUSH then
					arg_1_0:InitActtivityFleet(var_2_0, iter_2_3)
				elseif var_2_1 == ActivityConst.ACTIVITY_TYPE_BOSSSINGLE then
					arg_1_0:InitActtivityFleet(var_2_0, iter_2_3)
				elseif var_2_1 == ActivityConst.ACTIVITY_TYPE_EVENT_SINGLE then
					arg_1_0:CheckDailyEventRequest(var_2_0)
				end

				arg_1_0.data[iter_2_3.id] = var_2_0
			end
		end

		arg_1_0:refreshActivityBuffs()

		for iter_2_4, iter_2_5 in pairs(arg_1_0.data) do
			arg_1_0:sendNotification(GAME.ACTIVITY_BE_UPDATED, {
				isInit = true,
				activity = iter_2_5
			})
		end

		if arg_1_0.data[ActivityConst.MILITARY_EXERCISE_ACTIVITY_ID] then
			getProxy(MilitaryExerciseProxy):addSeasonOverTimer()
		end

		local var_2_2 = arg_1_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_CHALLENGE)

		if var_2_2 and not var_2_2:isEnd() then
			arg_1_0:sendNotification(GAME.CHALLENGE2_INFO, {})
		end

		local var_2_3 = arg_1_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_TASK_LIST_MONITOR)

		if var_2_3 and not var_2_3:isEnd() and var_2_3.data1 == 0 then
			arg_1_0:monitorTaskList(var_2_3)
		end

		local var_2_4 = arg_1_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

		if var_2_4 and not var_2_4:isEnd() then
			local var_2_5 = arg_1_0.data[var_2_4.id]

			arg_1_0:InitActivityBossData(var_2_5)
		end

		pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inElite")
		;(function()
			local var_3_0 = arg_1_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

			if not var_3_0 then
				return
			end

			arg_1_0:sendNotification(GAME.REQUEST_ATELIER, var_3_0.id)
		end)()
	end)
	arg_1_0:on(11201, function(arg_4_0)
		local var_4_0 = Activity.Create(arg_4_0.activity_info)

		assert(var_4_0.id, "should exist activity")

		local var_4_1 = var_4_0:getConfig("type")

		if var_4_1 == ActivityConst.ACTIVITY_TYPE_PARAMETER then
			arg_1_0:addActivityParameter(var_4_0)
		end

		if not arg_1_0.data[var_4_0.id] then
			arg_1_0:addActivity(var_4_0)
		else
			arg_1_0:updateActivity(var_4_0)
		end

		if var_4_1 == ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2 then
			arg_1_0:InitActtivityFleet(var_4_0, arg_4_0.activity_info)
			arg_1_0:InitActivityBossData(var_4_0)
		end

		arg_1_0:sendNotification(GAME.ACTIVITY_BE_UPDATED, {
			activity = var_4_0
		})
	end)
	arg_1_0:on(40009, function(arg_5_0)
		local var_5_0 = arg_1_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSSRUSH)
		local var_5_1

		if var_5_0 then
			var_5_1 = var_5_0:GetSeriesData()
		end

		local var_5_2 = BossRushSettlementCommand.ConcludeEXP(arg_5_0, var_5_0, var_5_1 and var_5_1:GetBattleStatistics())

		;(function()
			getProxy(ActivityProxy):GetBossRushRuntime(var_5_0.id).settlementData = var_5_2
		end)()
	end)
	arg_1_0:on(24100, function(arg_7_0)
		(function()
			local var_8_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_EXTRA_BOSSRUSH_RANK)

			if not var_8_0 then
				return
			end

			var_8_0:Record(arg_7_0.score)
			arg_1_0:updateActivity(var_8_0)
		end)()

		local var_7_0 = arg_1_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSSRUSH)

		if not var_7_0 then
			return
		end

		local var_7_1 = var_7_0:GetSeriesData()

		if not var_7_1 then
			return
		end

		var_7_1:AddEXScore(arg_7_0)
		arg_1_0:updateActivity(var_7_0)
	end)
	arg_1_0:on(11028, function(arg_9_0)
		print("接受到问卷状态", arg_9_0.result)

		if arg_9_0.result == 0 then
			arg_1_0:setSurveyState(arg_9_0.result)
		elseif arg_9_0.result > 0 then
			arg_1_0:setSurveyState(arg_9_0.result)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_9_0.result))
		end
	end)
	arg_1_0:on(26033, function(arg_10_0)
		local var_10_0 = arg_1_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

		if not var_10_0 then
			return
		end

		local var_10_1 = arg_10_0.point
		local var_10_2 = var_10_0:UpdateHighestScore(var_10_1)

		arg_1_0:GetActivityBossRuntime(var_10_0.id).spScore = {
			score = var_10_1,
			new = var_10_2
		}

		arg_1_0:updateActivity(var_10_0)
	end)

	arg_1_0.requestTime = {}
	arg_1_0.extraDatas = {}
end

function var_0_0.getAliveActivityByType(arg_11_0, arg_11_1)
	for iter_11_0, iter_11_1 in pairs(arg_11_0.data) do
		if iter_11_1:getConfig("type") == arg_11_1 and not iter_11_1:isEnd() then
			return iter_11_1
		end
	end
end

function var_0_0.getActivityByType(arg_12_0, arg_12_1)
	for iter_12_0, iter_12_1 in pairs(arg_12_0.data) do
		if iter_12_1:getConfig("type") == arg_12_1 then
			return iter_12_1
		end
	end
end

function var_0_0.getActivitiesByType(arg_13_0, arg_13_1)
	local var_13_0 = {}

	for iter_13_0, iter_13_1 in pairs(arg_13_0.data) do
		if iter_13_1:getConfig("type") == arg_13_1 then
			table.insert(var_13_0, iter_13_1)
		end
	end

	return var_13_0
end

function var_0_0.getActivitiesByTypes(arg_14_0, arg_14_1)
	local var_14_0 = {}

	for iter_14_0, iter_14_1 in pairs(arg_14_0.data) do
		if table.contains(arg_14_1, iter_14_1:getConfig("type")) then
			table.insert(var_14_0, iter_14_1)
		end
	end

	return var_14_0
end

function var_0_0.GetEarliestActByType(arg_15_0, arg_15_1)
	local var_15_0 = arg_15_0:getActivitiesByType(arg_15_1)
	local var_15_1 = _.select(var_15_0, function(arg_16_0)
		return not arg_16_0:isEnd()
	end)

	table.sort(var_15_1, function(arg_17_0, arg_17_1)
		return arg_17_0.id < arg_17_1.id
	end)

	return var_15_1[1]
end

function var_0_0.getMilitaryExerciseActivity(arg_18_0)
	local var_18_0

	for iter_18_0, iter_18_1 in pairs(arg_18_0.data) do
		if iter_18_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_MILITARY_EXERCISE then
			var_18_0 = iter_18_1

			break
		end
	end

	return Clone(var_18_0)
end

function var_0_0.getPanelActivities(arg_19_0)
	local function var_19_0(arg_20_0)
		local var_20_0 = arg_20_0:getConfig("type")
		local var_20_1 = arg_20_0:isShow() and not arg_20_0:isAfterShow()

		if var_20_1 then
			if var_20_0 == ActivityConst.ACTIVITY_TYPE_CHARGEAWARD then
				var_20_1 = arg_20_0.data2 == 0
			elseif var_20_0 == ActivityConst.ACTIVITY_TYPE_PROGRESSLOGIN then
				var_20_1 = arg_20_0.data1 < 7 or not arg_20_0.achieved
			end
		end

		return var_20_1 and not arg_20_0:isEnd()
	end

	local var_19_1 = {}

	for iter_19_0, iter_19_1 in pairs(arg_19_0.data) do
		if var_19_0(iter_19_1) then
			table.insert(var_19_1, iter_19_1)
		end
	end

	table.sort(var_19_1, function(arg_21_0, arg_21_1)
		local var_21_0 = arg_21_0:getConfig("login_pop")
		local var_21_1 = arg_21_1:getConfig("login_pop")

		if var_21_0 == var_21_1 then
			return arg_21_0.id < arg_21_1.id
		else
			return var_21_1 < var_21_0
		end
	end)

	return var_19_1
end

function var_0_0.checkHxActivity(arg_22_0, arg_22_1)
	if arg_22_0.hxList and #arg_22_0.hxList > 0 then
		for iter_22_0 = 1, #arg_22_0.hxList do
			if arg_22_0.hxList[iter_22_0] == arg_22_1 then
				return true
			end
		end
	end

	return false
end

function var_0_0.getBannerDisplays(arg_23_0)
	return _(pg.activity_banner.all):chain():map(function(arg_24_0)
		return pg.activity_banner[arg_24_0]
	end):filter(function(arg_25_0)
		return pg.TimeMgr.GetInstance():inTime(arg_25_0.time) and arg_25_0.type ~= GAMEUI_BANNER_9 and arg_25_0.type ~= GAMEUI_BANNER_11 and arg_25_0.type ~= GAMEUI_BANNER_10 and arg_25_0.type ~= GAMEUI_BANNER_12 and arg_25_0.type ~= GAMEUI_BANNER_13
	end):value()
end

function var_0_0.getActiveBannerByType(arg_26_0, arg_26_1)
	local var_26_0 = pg.activity_banner.get_id_list_by_type[arg_26_1]

	if not var_26_0 then
		return nil
	end

	for iter_26_0, iter_26_1 in ipairs(var_26_0) do
		local var_26_1 = pg.activity_banner[iter_26_1]

		if pg.TimeMgr.GetInstance():inTime(var_26_1.time) then
			return var_26_1
		end
	end

	return nil
end

function var_0_0.getNoticeBannerDisplays(arg_27_0)
	return _.map(pg.activity_banner_notice.all, function(arg_28_0)
		return pg.activity_banner_notice[arg_28_0]
	end)
end

function var_0_0.findNextAutoActivity(arg_29_0)
	local var_29_0
	local var_29_1 = pg.TimeMgr.GetInstance()
	local var_29_2 = var_29_1:GetServerTime()

	for iter_29_0, iter_29_1 in ipairs(arg_29_0:getPanelActivities()) do
		if iter_29_1:isShow() and not iter_29_1.autoActionForbidden then
			local var_29_3 = iter_29_1:getConfig("type")

			if var_29_3 == ActivityConst.ACTIVITY_TYPE_7DAYSLOGIN then
				local var_29_4 = iter_29_1:getConfig("config_id")
				local var_29_5 = pg.activity_7_day_sign[var_29_4].front_drops

				if iter_29_1.data1 < #var_29_5 and not var_29_1:IsSameDay(var_29_2, iter_29_1.data2) and var_29_2 > iter_29_1.data2 then
					var_29_0 = iter_29_1

					break
				end
			elseif var_29_3 == ActivityConst.ACTIVITY_TYPE_PROGRESSLOGIN then
				local var_29_6 = getProxy(ChapterProxy)

				if iter_29_1.data1 < 7 and not var_29_1:IsSameDay(var_29_2, iter_29_1.data2) or iter_29_1.data1 == 7 and not iter_29_1.achieved and var_29_6:isClear(204) then
					var_29_0 = iter_29_1

					break
				end
			elseif var_29_3 == ActivityConst.ACTIVITY_TYPE_MONTHSIGN then
				local var_29_7 = pg.TimeMgr.GetInstance():STimeDescS(var_29_2, "*t")

				iter_29_1:setSpecialData("reMonthSignDay", nil)

				if var_29_7.year ~= iter_29_1.data1 or var_29_7.month ~= iter_29_1.data2 then
					iter_29_1.data1 = var_29_7.year
					iter_29_1.data2 = var_29_7.month
					iter_29_1.data1_list = {}
					var_29_0 = iter_29_1

					break
				elseif not table.contains(iter_29_1.data1_list, var_29_7.day) then
					var_29_0 = iter_29_1

					break
				elseif var_29_7.day > #iter_29_1.data1_list and pg.activity_month_sign[iter_29_1.data2].resign_count > iter_29_1.data3 then
					for iter_29_2 = var_29_7.day, 1, -1 do
						if not table.contains(iter_29_1.data1_list, iter_29_2) then
							iter_29_1:setSpecialData("reMonthSignDay", iter_29_2)

							break
						end
					end

					var_29_0 = iter_29_1
				end
			elseif iter_29_1.id == ActivityConst.SHADOW_PLAY_ID and iter_29_1.clientData1 == 0 then
				local var_29_8 = iter_29_1:getConfig("config_data")[1]
				local var_29_9 = getProxy(TaskProxy)
				local var_29_10 = var_29_9:getTaskById(var_29_8) or var_29_9:getFinishTaskById(var_29_8)

				if var_29_10 and not var_29_10:isReceive() then
					var_29_0 = iter_29_1

					break
				end
			end
		end
	end

	if not var_29_0 then
		for iter_29_3, iter_29_4 in pairs(arg_29_0.data) do
			if not iter_29_4:isShow() and iter_29_4:getConfig("type") == ActivityConst.ACTIVITY_TYPE_7DAYSLOGIN then
				local var_29_11 = iter_29_4:getConfig("config_id")
				local var_29_12 = pg.activity_7_day_sign[var_29_11].front_drops

				if iter_29_4.data1 < #var_29_12 and not var_29_1:IsSameDay(var_29_2, iter_29_4.data2) and var_29_2 > iter_29_4.data2 then
					var_29_0 = iter_29_4

					break
				end
			end
		end
	end

	return var_29_0
end

function var_0_0.findRefluxAutoActivity(arg_30_0)
	local var_30_0 = arg_30_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_REFLUX)

	if var_30_0 and not var_30_0:isEnd() and not var_30_0.autoActionForbidden then
		local var_30_1 = pg.TimeMgr.GetInstance()

		if var_30_0.data1_list[2] < #pg.return_sign_template.all and not var_30_1:IsSameDay(var_30_1:GetServerTime(), var_30_0.data1_list[1]) then
			return 1
		end
	end
end

function var_0_0.existRefluxAwards(arg_31_0)
	local var_31_0 = arg_31_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_REFLUX)

	if var_31_0 and not var_31_0:isEnd() then
		local var_31_1 = pg.return_pt_template

		for iter_31_0 = #var_31_1.all, 1, -1 do
			local var_31_2 = var_31_1.all[iter_31_0]
			local var_31_3 = var_31_1[var_31_2]

			if var_31_0.data3 >= var_31_3.pt_require and var_31_2 > var_31_0.data4 then
				return true
			end
		end

		local var_31_4 = getProxy(TaskProxy)
		local var_31_5 = _(var_31_0:getConfig("config_data")[7]):chain():map(function(arg_32_0)
			return arg_32_0[2]
		end):flatten():map(function(arg_33_0)
			return var_31_4:getTaskById(arg_33_0) or var_31_4:getFinishTaskById(arg_33_0) or false
		end):filter(function(arg_34_0)
			return not not arg_34_0
		end):value()

		if _.any(var_31_5, function(arg_35_0)
			return arg_35_0:getTaskStatus() == 1
		end) then
			return true
		end
	end
end

function var_0_0.getActivityById(arg_36_0, arg_36_1)
	return Clone(arg_36_0.data[arg_36_1])
end

function var_0_0.RawGetActivityById(arg_37_0, arg_37_1)
	return arg_37_0.data[arg_37_1]
end

function var_0_0.updateActivity(arg_38_0, arg_38_1)
	assert(arg_38_0.data[arg_38_1.id], "activity should exist" .. arg_38_1.id)
	assert(isa(arg_38_1, Activity), "activity should instance of Activity")

	if arg_38_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_PT_CRUSING then
		local var_38_0 = pg.battlepass_event_pt[arg_38_1.id].target

		if arg_38_0.data[arg_38_1.id].data1 < var_38_0[#var_38_0] and arg_38_1.data1 - arg_38_0.data[arg_38_1.id].data1 > 0 then
			pg.ToastMgr.GetInstance():ShowToast(pg.ToastMgr.TYPE_CRUSING, {
				ptId = pg.battlepass_event_pt[arg_38_1.id].pt,
				ptCount = arg_38_1.data1 - arg_38_0.data[arg_38_1.id].data1
			})
		end
	end

	arg_38_0.data[arg_38_1.id] = arg_38_1

	arg_38_0.facade:sendNotification(var_0_0.ACTIVITY_UPDATED, arg_38_1:clone())
	arg_38_0.facade:sendNotification(GAME.SYN_GRAFTING_ACTIVITY, {
		id = arg_38_1.id
	})
end

function var_0_0.addActivity(arg_39_0, arg_39_1)
	assert(arg_39_0.data[arg_39_1.id] == nil, "activity already exist" .. arg_39_1.id)
	assert(isa(arg_39_1, Activity), "activity should instance of Activity")

	arg_39_0.data[arg_39_1.id] = arg_39_1

	arg_39_0.facade:sendNotification(var_0_0.ACTIVITY_ADDED, arg_39_1:clone())

	if arg_39_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUFF then
		table.insert(arg_39_0.buffActs, arg_39_1.id)
		arg_39_0:refreshActivityBuffs()
	end
end

function var_0_0.deleteActivityById(arg_40_0, arg_40_1)
	assert(arg_40_0.data[arg_40_1], "activity should exist" .. arg_40_1)

	arg_40_0.data[arg_40_1] = nil

	arg_40_0.facade:sendNotification(var_0_0.ACTIVITY_DELETED, arg_40_1)
end

function var_0_0.IsActivityNotEnd(arg_41_0, arg_41_1)
	return arg_41_0.data[arg_41_1] and not arg_41_0.data[arg_41_1]:isEnd()
end

function var_0_0.readyToAchieveByType(arg_42_0, arg_42_1)
	local var_42_0 = false
	local var_42_1 = arg_42_0:getActivitiesByType(arg_42_1)

	for iter_42_0, iter_42_1 in ipairs(var_42_1) do
		if iter_42_1:readyToAchieve() then
			var_42_0 = true

			break
		end
	end

	return var_42_0
end

function var_0_0.getBuildActivityCfgByID(arg_43_0, arg_43_1)
	local var_43_0 = arg_43_0:getActivitiesByTypes({
		ActivityConst.ACTIVITY_TYPE_BUILDSHIP_1,
		ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD
	})

	for iter_43_0, iter_43_1 in ipairs(var_43_0) do
		if not iter_43_1:isEnd() then
			local var_43_1 = iter_43_1:getConfig("config_client")

			if var_43_1 and var_43_1.id == arg_43_1 then
				return var_43_1
			end
		end
	end

	return nil
end

function var_0_0.getNoneActBuildActivityCfgByID(arg_44_0, arg_44_1)
	local var_44_0 = arg_44_0:getActivitiesByTypes({
		ActivityConst.ACTIVITY_TYPE_BUILD
	})

	for iter_44_0, iter_44_1 in ipairs(var_44_0) do
		if not iter_44_1:isEnd() then
			local var_44_1 = iter_44_1:getConfig("config_client")

			if var_44_1 and var_44_1.id == arg_44_1 then
				return var_44_1
			end
		end
	end

	return nil
end

function var_0_0.getBuffShipList(arg_45_0)
	local var_45_0 = {}
	local var_45_1 = arg_45_0:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_SHIP_BUFF)

	_.each(var_45_1, function(arg_46_0)
		if arg_46_0 and not arg_46_0:isEnd() then
			local var_46_0 = arg_46_0:getConfig("config_id")
			local var_46_1 = pg.activity_expup_ship[var_46_0]

			if not var_46_1 then
				return
			end

			local var_46_2 = var_46_1.expup

			for iter_46_0, iter_46_1 in pairs(var_46_2) do
				var_45_0[iter_46_1[1]] = iter_46_1[2]
			end
		end
	end)

	return var_45_0
end

function var_0_0.getVirtualItemNumber(arg_47_0, arg_47_1)
	local var_47_0 = arg_47_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

	if var_47_0 and not var_47_0:isEnd() then
		return var_47_0.data1KeyValueList[1][arg_47_1] and var_47_0.data1KeyValueList[1][arg_47_1] or 0
	end

	return 0
end

function var_0_0.removeVitemById(arg_48_0, arg_48_1, arg_48_2)
	local var_48_0 = arg_48_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

	assert(var_48_0, "vbagType invalid")

	if var_48_0 and not var_48_0:isEnd() then
		var_48_0.data1KeyValueList[1][arg_48_1] = var_48_0.data1KeyValueList[1][arg_48_1] - arg_48_2
	end

	arg_48_0:updateActivity(var_48_0)
end

function var_0_0.addVitemById(arg_49_0, arg_49_1, arg_49_2)
	local var_49_0 = arg_49_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

	assert(var_49_0, "vbagType invalid")

	if var_49_0 and not var_49_0:isEnd() then
		if not var_49_0.data1KeyValueList[1][arg_49_1] then
			var_49_0.data1KeyValueList[1][arg_49_1] = 0
		end

		var_49_0.data1KeyValueList[1][arg_49_1] = var_49_0.data1KeyValueList[1][arg_49_1] + arg_49_2
	end

	arg_49_0:updateActivity(var_49_0)

	local var_49_1 = Item.getConfigData(arg_49_1).link_id

	if var_49_1 ~= 0 then
		local var_49_2 = arg_49_0:getActivityById(var_49_1)

		if var_49_2 and not var_49_2:isEnd() then
			PlayerResChangeCommand.UpdateActivity(var_49_2, arg_49_2)
		end
	end
end

function var_0_0.monitorTaskList(arg_50_0, arg_50_1)
	if arg_50_1 and not arg_50_1:isEnd() and arg_50_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_TASK_LIST_MONITOR then
		local var_50_0 = arg_50_1:getConfig("config_data")[1] or {}

		if getProxy(TaskProxy):isReceiveTasks(var_50_0) then
			pg.m02:sendNotification(GAME.ACTIVITY_OPERATION, {
				cmd = 1,
				activity_id = arg_50_1.id
			})
		end
	end
end

function var_0_0.InitActtivityFleet(arg_51_0, arg_51_1, arg_51_2)
	getProxy(FleetProxy):addActivityFleet(arg_51_1, arg_51_2.group_list)
end

function var_0_0.InitActivityBossData(arg_52_0, arg_52_1)
	local var_52_0 = pg.activity_event_worldboss[arg_52_1:getConfig("config_id")]

	if not var_52_0 then
		return
	end

	local var_52_1 = arg_52_1.data1KeyValueList

	for iter_52_0, iter_52_1 in pairs(var_52_0.normal_expedition_drop_num or {}) do
		for iter_52_2, iter_52_3 in pairs(iter_52_1[1]) do
			local var_52_2 = iter_52_1[2]
			local var_52_3 = var_52_1[1][iter_52_3] or 0

			var_52_1[1][iter_52_3] = math.max(var_52_2 - var_52_3, 0)
			var_52_1[2][iter_52_3] = var_52_1[2][iter_52_3] or 0
		end
	end
end

function var_0_0.AddInstagramTimer(arg_53_0, arg_53_1)
	arg_53_0:RemoveInstagramTimer()

	local var_53_0, var_53_1 = arg_53_0.data[arg_53_1]:GetNextPushTime()

	if var_53_0 then
		local var_53_2 = var_53_0 - pg.TimeMgr.GetInstance():GetServerTime()

		local function var_53_3()
			arg_53_0:sendNotification(GAME.ACT_INSTAGRAM_OP, {
				arg2 = 0,
				activity_id = arg_53_1,
				cmd = ActivityConst.INSTAGRAM_OP_ACTIVE,
				arg1 = var_53_1
			})
		end

		if var_53_2 <= 0 then
			var_53_3()
		else
			arg_53_0.instagramTimer = Timer.New(function()
				var_53_3()
				arg_53_0:RemoveInstagramTimer()
			end, var_53_2, 1)

			arg_53_0.instagramTimer:Start()
		end
	end
end

function var_0_0.RemoveInstagramTimer(arg_56_0)
	if arg_56_0.instagramTimer then
		arg_56_0.instagramTimer:Stop()

		arg_56_0.instagramTimer = nil
	end
end

function var_0_0.RegisterRequestTime(arg_57_0, arg_57_1, arg_57_2)
	if not arg_57_1 or arg_57_1 <= 0 then
		return
	end

	arg_57_0.requestTime[arg_57_1] = arg_57_2
end

function var_0_0.remove(arg_58_0)
	arg_58_0:RemoveInstagramTimer()
end

function var_0_0.addActivityParameter(arg_59_0, arg_59_1)
	local var_59_0 = arg_59_1:getConfig("config_data")
	local var_59_1 = arg_59_1.stopTime

	for iter_59_0, iter_59_1 in ipairs(var_59_0) do
		arg_59_0.params[iter_59_1[1]] = {
			iter_59_1[2],
			var_59_1
		}
	end
end

function var_0_0.getActivityParameter(arg_60_0, arg_60_1)
	if arg_60_0.params[arg_60_1] then
		local var_60_0, var_60_1 = unpack(arg_60_0.params[arg_60_1])

		if not (var_60_1 > 0) or not (var_60_1 <= pg.TimeMgr.GetInstance():GetServerTime()) then
			return var_60_0
		end
	end
end

function var_0_0.IsShowFreeBuildMark(arg_61_0, arg_61_1)
	for iter_61_0, iter_61_1 in ipairs(arg_61_0:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_BUILD_FREE)) do
		if iter_61_1 and not iter_61_1:isEnd() and iter_61_1.data1 > 0 and iter_61_1.stopTime - pg.TimeMgr.GetInstance():GetServerTime() < 259200 and tobool(arg_61_1) == (PlayerPrefs.GetString("Free_Build_Ticket_" .. iter_61_1.id, "") == pg.TimeMgr.GetInstance():CurrentSTimeDesc("%Y/%m/%d")) then
			return iter_61_1
		end
	end

	return false
end

function var_0_0.getBuildFreeActivityByBuildId(arg_62_0, arg_62_1)
	for iter_62_0, iter_62_1 in ipairs(arg_62_0:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_BUILD_FREE)) do
		if underscore.any(iter_62_1:getConfig("config_data"), function(arg_63_0)
			return arg_63_0 == arg_62_1
		end) then
			return iter_62_1
		end
	end
end

function var_0_0.getBuildPoolActivity(arg_64_0, arg_64_1)
	if arg_64_1:IsActivity() then
		return arg_64_0:getActivityById(arg_64_1.activityId)
	end
end

function var_0_0.getEnterReadyActivity(arg_65_0)
	local var_65_0 = {
		[ActivityConst.ACTIVITY_TYPE_ZPROJECT] = false,
		[ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2] = function(arg_66_0)
			return not arg_66_0:checkBattleTimeInBossAct()
		end,
		[ActivityConst.ACTIVITY_TYPE_BOSSRUSH] = false,
		[ActivityConst.ACTIVITY_TYPE_BOSSSINGLE] = false
	}
	local var_65_1 = _.keys(var_65_0)
	local var_65_2 = {}

	for iter_65_0, iter_65_1 in ipairs(var_65_1) do
		var_65_2[iter_65_1] = 0
	end

	for iter_65_2, iter_65_3 in pairs(arg_65_0.data) do
		local var_65_3 = iter_65_3:getConfig("type")

		if var_65_2[var_65_3] and not iter_65_3:isEnd() and not existCall(var_65_0[var_65_3], iter_65_3) then
			var_65_2[var_65_3] = math.max(var_65_2[var_65_3], iter_65_2)
		end
	end

	table.sort(var_65_1)

	for iter_65_4, iter_65_5 in ipairs(var_65_1) do
		if var_65_2[iter_65_5] > 0 then
			return arg_65_0.data[var_65_2[iter_65_5]]
		end
	end
end

function var_0_0.AtelierActivityAllSlotIsEmpty(arg_67_0)
	local var_67_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

	if not var_67_0 or var_67_0:isEnd() then
		return false
	end

	local var_67_1 = var_67_0:GetSlots()

	for iter_67_0, iter_67_1 in pairs(var_67_1) do
		if iter_67_1[1] ~= 0 then
			return false
		end
	end

	return true
end

function var_0_0.OwnAtelierActivityItemCnt(arg_68_0, arg_68_1, arg_68_2)
	local var_68_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

	if not var_68_0 or var_68_0:isEnd() then
		return false
	end

	local var_68_1 = var_68_0:GetItems()[arg_68_1]

	return var_68_1 and arg_68_2 <= var_68_1.count
end

function var_0_0.refreshActivityBuffs(arg_69_0)
	arg_69_0.actBuffs = {}

	local var_69_0 = 1

	while var_69_0 <= #arg_69_0.buffActs do
		local var_69_1 = arg_69_0.data[arg_69_0.buffActs[var_69_0]]

		if not var_69_1 or var_69_1:isEnd() then
			table.remove(arg_69_0.buffActs, var_69_0)
		else
			var_69_0 = var_69_0 + 1

			local var_69_2 = {
				var_69_1:getConfig("config_id")
			}

			if var_69_2[1] == 0 then
				var_69_2 = var_69_1:getConfig("config_data")
			end

			for iter_69_0, iter_69_1 in ipairs(var_69_2) do
				local var_69_3 = ActivityBuff.New(var_69_1.id, iter_69_1)

				if var_69_3:isActivate() then
					table.insert(arg_69_0.actBuffs, var_69_3)
				end
			end
		end
	end
end

function var_0_0.getActivityBuffs(arg_70_0)
	if underscore.any(arg_70_0.buffActs, function(arg_71_0)
		return not arg_70_0.data[arg_71_0] or arg_70_0.data[arg_71_0]:isEnd()
	end) or underscore.any(arg_70_0.actBuffs, function(arg_72_0)
		return not arg_72_0:isActivate()
	end) then
		arg_70_0:refreshActivityBuffs()
	end

	return arg_70_0.actBuffs
end

function var_0_0.getShipModExpActivity(arg_73_0)
	return underscore.select(arg_73_0:getActivityBuffs(), function(arg_74_0)
		return arg_74_0:ShipModExpUsage()
	end)
end

function var_0_0.getBackyardEnergyActivityBuffs(arg_75_0)
	return underscore.select(arg_75_0:getActivityBuffs(), function(arg_76_0)
		return arg_76_0:BackyardEnergyUsage()
	end)
end

function var_0_0.InitContinuousTime(arg_77_0, arg_77_1)
	arg_77_0.continuousOpeartionTime = arg_77_1
	arg_77_0.continuousOpeartionTotalTime = arg_77_1
end

function var_0_0.UseContinuousTime(arg_78_0)
	if not arg_78_0.continuousOpeartionTime then
		return
	end

	arg_78_0.continuousOpeartionTime = arg_78_0.continuousOpeartionTime - 1
end

function var_0_0.GetContinuousTime(arg_79_0)
	return arg_79_0.continuousOpeartionTime, arg_79_0.continuousOpeartionTotalTime
end

function var_0_0.AddBossRushAwards(arg_80_0, arg_80_1)
	arg_80_0.bossrushAwards = arg_80_0.bossrushAwards or {}

	table.insertto(arg_80_0.bossrushAwards, arg_80_1)
end

function var_0_0.PopBossRushAwards(arg_81_0)
	local var_81_0 = arg_81_0.bossrushAwards or {}

	arg_81_0.bossrushAwards = nil

	return var_81_0
end

function var_0_0.GetBossRushRuntime(arg_82_0, arg_82_1)
	if not arg_82_0.extraDatas[arg_82_1] then
		arg_82_0.extraDatas[arg_82_1] = {
			record = 0
		}
	end

	return arg_82_0.extraDatas[arg_82_1]
end

function var_0_0.GetActivityBossRuntime(arg_83_0, arg_83_1)
	if not arg_83_0.extraDatas[arg_83_1] then
		arg_83_0.extraDatas[arg_83_1] = {
			buffIds = {},
			spScore = {
				score = 0
			}
		}
	end

	return arg_83_0.extraDatas[arg_83_1]
end

function var_0_0.GetTaskActivities(arg_84_0)
	local var_84_0 = {}

	table.Foreach(Activity.GetType2Class(), function(arg_85_0, arg_85_1)
		if not isa(arg_85_1, ITaskActivity) then
			return
		end

		table.insertto(var_84_0, arg_84_0:getActivitiesByType(arg_85_0))
	end)

	return var_84_0
end

function var_0_0.setSurveyState(arg_86_0, arg_86_1)
	local var_86_0 = arg_86_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_SURVEY)

	if var_86_0 and not var_86_0:isEnd() then
		arg_86_0.surveyState = arg_86_1
	end
end

function var_0_0.isSurveyDone(arg_87_0)
	local var_87_0 = arg_87_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_SURVEY)

	if var_87_0 and not var_87_0:isEnd() then
		return arg_87_0.surveyState and arg_87_0.surveyState > 0
	end
end

function var_0_0.isSurveyOpen(arg_88_0)
	local var_88_0 = arg_88_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_SURVEY)

	if var_88_0 and not var_88_0:isEnd() then
		local var_88_1 = var_88_0:getConfig("config_data")
		local var_88_2 = var_88_1[1]
		local var_88_3 = var_88_1[2]

		if var_88_2 == 1 then
			local var_88_4 = var_88_3 <= getProxy(PlayerProxy):getData().level
			local var_88_5 = var_88_0:getConfig("config_id")

			return var_88_4, var_88_5
		end
	end
end

function var_0_0.GetActBossLinkPTActID(arg_89_0, arg_89_1)
	local var_89_0 = table.Find(arg_89_0.data, function(arg_90_0, arg_90_1)
		if arg_90_1:getConfig("type") ~= ActivityConst.ACTIVITY_TYPE_PT_BUFF then
			return
		end

		return arg_90_1:getDataConfig("link_id") == arg_89_1
	end)

	return var_89_0 and var_89_0.id
end

function var_0_0.CheckDailyEventRequest(arg_91_0, arg_91_1)
	if arg_91_1:CheckDailyEventRequest() then
		arg_91_0:sendNotification(GAME.SINGLE_EVENT_REFRESH, {
			actId = arg_91_1.id
		})
	end
end

return var_0_0
