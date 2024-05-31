local var_0_0 = class("ZeroHourCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0, var_1_1 = pcall(arg_1_0.mainHandler, arg_1_0)

	if not var_1_0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("zero_hour_command_error"))
		error(var_1_1)
	end
end

function var_0_0.mainHandler(arg_2_0, arg_2_1)
	local var_2_0 = getProxy(PlayerProxy)
	local var_2_1 = var_2_0:getData()

	var_2_1:resetBuyOilCount()

	for iter_2_0, iter_2_1 in pairs(var_2_1.vipCards) do
		if iter_2_1:isExpire() then
			var_2_1.vipCards[iter_2_1.id] = nil
		end
	end

	var_2_0:updatePlayer(var_2_1)

	local var_2_2 = getProxy(ShopsProxy)
	local var_2_3 = var_2_2:getShopStreet()

	if var_2_3 then
		var_2_3:resetflashCount()
		var_2_2:setShopStreet(var_2_3)
	end

	var_2_2.refreshChargeList = true

	getProxy(CollectionProxy):resetEvaCount()

	local var_2_4 = getProxy(MilitaryExerciseProxy)
	local var_2_5 = var_2_4:getSeasonInfo()

	if var_2_5 then
		var_2_5:resetFlashCount()
		var_2_4:updateSeasonInfo(var_2_5)
	end

	getProxy(DailyLevelProxy):resetDailyCount()

	local var_2_6 = getProxy(ChapterProxy)

	var_2_6:resetRepairTimes()
	var_2_6:resetEscortChallengeTimes()

	local var_2_7 = var_2_6:getData()

	for iter_2_2, iter_2_3 in pairs(var_2_7) do
		if iter_2_3.todayDefeatCount > 0 then
			iter_2_3.todayDefeatCount = 0

			var_2_6:updateChapter(iter_2_3)
		end
	end

	var_2_6:resetDailyCount()
	;(function()
		local var_3_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSSRUSH)

		if not var_3_0 then
			return
		end

		local var_3_1 = var_3_0:GetUsedBonus()

		table.Foreach(var_3_1, function(arg_4_0, arg_4_1)
			var_3_1[arg_4_0] = 0
		end)
		getProxy(ActivityProxy):updateActivity(var_3_0)
	end)()
	getProxy(DailyLevelProxy):clearChaptersDefeatCount()

	local var_2_8 = pg.TimeMgr.GetInstance():STimeDescS(pg.TimeMgr.GetInstance():GetServerTime(), "*t")

	if var_2_8.day == 1 then
		var_2_2.shamShop:update(var_2_8.month, {})
		var_2_2:AddShamShop(var_2_2.shamShop)
		var_2_2.fragmentShop:Reset(var_2_8.month)
		var_2_2:AddFragmentShop(var_2_2.fragmentShop)

		if not LOCK_UR_SHIP then
			local var_2_9 = pg.gameset.urpt_chapter_max.description[1]

			getProxy(BagProxy):ClearLimitCnt(var_2_9)
		end
	end

	local var_2_10 = getProxy(ShopsProxy):getMiniShop()

	if var_2_10 and var_2_10:checkShopFlash() then
		pg.m02:sendNotification(GAME.MINI_GAME_SHOP_FLUSH)
	end

	local var_2_11 = getProxy(ActivityProxy)

	for iter_2_4, iter_2_5 in ipairs(var_2_11:getPanelActivities()) do
		if (function()
			local var_5_0 = {
				ActivityConst.ACTIVITY_TYPE_7DAYSLOGIN,
				ActivityConst.ACTIVITY_TYPE_PROGRESSLOGIN,
				ActivityConst.ACTIVITY_TYPE_MONTHSIGN,
				ActivityConst.ACTIVITY_TYPE_REFLUX,
				ActivityConst.ACTIVITY_TYPE_HITMONSTERNIAN,
				ActivityConst.ACTIVITY_TYPE_BB,
				ActivityConst.ACTIVITY_TYPE_LOTTERY_AWARD
			}

			iter_2_5.autoActionForbidden = false

			if iter_2_5:getConfig("type") == ActivityConst.ACTIVITY_TYPE_BB then
				iter_2_5.data2 = 0
			elseif iter_2_5:getConfig("type") == ActivityConst.ACTIVITY_TYPE_LOTTERY_AWARD then
				iter_2_5.data2 = 0
			end

			return table.contains(var_5_0, iter_2_5:getConfig("type"))
		end)() then
			var_2_11:updateActivity(iter_2_5)
		end
	end

	getProxy(RefluxProxy):setAutoActionForbidden(false)

	local var_2_12 = var_2_11:getActivityByType(ActivityConst.ACTIVITY_TYPE_MANUAL_SIGN)

	if var_2_12 and not var_2_12:isEnd() then
		pg.m02:sendNotification(GAME.ACT_MANUAL_SIGN, {
			activity_id = var_2_12.id,
			cmd = ManualSignActivity.OP_SIGN
		})
	end

	local var_2_13 = var_2_11:getActivityByType(ActivityConst.ACTIVITY_TYPE_REFLUX)

	if var_2_13 and not var_2_13:isEnd() then
		var_2_13.data1KeyValueList = {
			{}
		}

		var_2_11:updateActivity(var_2_13)
	end

	local var_2_14 = var_2_11:getActivityByType(ActivityConst.ACTIVITY_TYPE_TURNTABLE)

	if var_2_14 and not var_2_14:isEnd() then
		local var_2_15 = var_2_14:getConfig("config_id")
		local var_2_16 = pg.activity_event_turning[var_2_15]

		if var_2_16.total_num <= var_2_14.data3 then
			return
		end

		local var_2_17 = var_2_16.task_table[var_2_14.data4]
		local var_2_18 = getProxy(TaskProxy)

		for iter_2_6, iter_2_7 in ipairs(var_2_17) do
			if (var_2_18:getTaskById(iter_2_7) or var_2_18:getFinishTaskById(iter_2_7)):getTaskStatus() ~= 2 then
				return
			end
		end

		arg_2_0:sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 2,
			activity_id = var_2_14.id
		})
	end

	local var_2_19 = getProxy(NavalAcademyProxy)

	var_2_19:setCourse(var_2_19.course)
	arg_2_0:sendNotification(GAME.CLASS_FORCE_UPDATE)
	getProxy(TechnologyProxy):updateRefreshFlag(0)
	arg_2_0:sendNotification(GAME.ACCEPT_ACTIVITY_TASK)
	getProxy(CommanderProxy):resetBoxUseCnt()

	local var_2_20 = getProxy(CommanderProxy):GetCommanderHome()

	if var_2_20 then
		var_2_20:ResetCatteryOP()
		var_2_20:ReduceClean()
	end

	local var_2_21 = var_2_11:getActivityByType(ActivityConst.ACTIVITY_TYPE_MONOPOLY)

	if var_2_21 and not var_2_21:isEnd() then
		var_2_11:updateActivity(var_2_21)
	end

	local var_2_22 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_CHALLENGE)

	if var_2_22 and not var_2_22:isEnd() then
		arg_2_0:sendNotification(GAME.CHALLENGE2_INFO, {})
	end

	LimitChallengeConst.RequestInfo()
	arg_2_0:sendNotification(GAME.REQUEST_MINI_GAME, {
		type = MiniGameRequestCommand.REQUEST_HUB_DATA
	})

	local var_2_23 = getProxy(MiniGameProxy)
	local var_2_24 = var_2_23:GetMiniGameDataByType(MiniGameConst.MG_TYPE_5)

	if var_2_24 then
		local var_2_25 = var_2_24.id
		local var_2_26 = var_2_23:GetHubByGameId(var_2_25).id

		arg_2_0:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_2_26,
			cmd = MiniGameOPCommand.CMD_SPECIAL_GAME,
			args1 = {
				var_2_25,
				1
			}
		})
	end

	arg_2_0:sendNotification(GAME.REFLUX_REQUEST_DATA)

	local var_2_27 = nowWorld()

	if pg.TimeMgr.GetInstance():GetServerWeek() == 1 then
		var_2_27.staminaMgr.staminaExchangeTimes = 0
	end

	if var_2_27 then
		local var_2_28 = var_2_27:GetBossProxy()

		var_2_28:increasePt()
		var_2_28:ClearSummonPtDailyAcc()
		var_2_28:ClearSummonPtOldAcc()
	end

	local var_2_29 = var_2_11:getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

	if var_2_29 and not var_2_29:isEnd() then
		local var_2_30 = var_2_29.data1KeyValueList[1]
		local var_2_31 = pg.activity_event_worldboss[var_2_29:getConfig("config_id")]

		if var_2_31 then
			for iter_2_8, iter_2_9 in ipairs(var_2_31.normal_expedition_drop_num or {}) do
				for iter_2_10, iter_2_11 in ipairs(iter_2_9[1]) do
					var_2_30[iter_2_11] = iter_2_9[2] or 0
				end
			end
		end

		var_2_11:updateActivity(var_2_29)
	end

	local var_2_32 = getProxy(ActivityProxy)
	local var_2_33 = var_2_32:getActivityByType(ActivityConst.ACTIVITY_TYPE_COLLECTION_EVENT)

	if var_2_33 and not var_2_33:isEnd() then
		local var_2_34, var_2_35 = getProxy(EventProxy):GetEventByActivityId(var_2_33.id)

		if not var_2_34 or var_2_34 and not var_2_34:IsStarting() then
			if var_2_34 and var_2_35 then
				table.remove(getProxy(EventProxy).eventList, var_2_35)
			end

			local var_2_36 = var_2_33:getConfig("config_data")
			local var_2_37 = var_2_33:getDayIndex()

			if var_2_37 > 0 and var_2_37 <= #var_2_36 then
				getProxy(EventProxy):AddActivityEvent(EventInfo.New({
					finish_time = 0,
					over_time = 0,
					id = var_2_36[var_2_37],
					ship_id_list = {},
					activity_id = var_2_33.id
				}))
			end

			pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inEvent")
			arg_2_0:sendNotification(GAME.EVENT_LIST_UPDATE)
		end
	end

	local var_2_38 = getProxy(GuildProxy)
	local var_2_39 = var_2_38:getRawData()

	if var_2_39 then
		var_2_39:ResetTechCancelCnt()

		local var_2_40 = var_2_39:getWeeklyTask()

		if var_2_40 and var_2_40:isExpire() then
			local var_2_41 = var_2_40:GetPresonTaskId()

			getProxy(TaskProxy):removeTaskById(var_2_41)

			var_2_39.weeklyTaskFlag = 0
		end

		local var_2_42 = var_2_39:GetActiveEvent()

		if var_2_42 then
			var_2_42:GetBossMission():ResetDailyCnt()
		end

		if var_2_8.day == 1 then
			var_2_39:ResetActiveEventCnt()
		end

		var_2_38:updateGuild(var_2_39)
	end

	if var_2_38:GetPublicGuild() then
		local var_2_43 = math.random(2, 5)
		local var_2_44

		var_2_44 = Timer.New(function()
			var_2_44:Stop()
			arg_2_0:sendNotification(GAME.GET_PUBLIC_GUILD_USER_DATA, {
				flag = true
			})
		end, var_2_43, 1)

		var_2_44:Start()
	end

	getProxy(NavalAcademyProxy):resetUsedDailyFinishCnt()
	getProxy(AvatarFrameProxy):clearTimeOut()
	arg_2_0:sendNotification(GAME.ZERO_HOUR_OP_DONE)
	MainRequestActDataSequence.New():RequestRandomDailyTask()
	;(function()
		local var_7_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSSSINGLE)

		if not var_7_0 or var_7_0:isEnd() then
			return
		end

		local var_7_1 = var_7_0:GetDailyCounts()

		table.Foreach(var_7_1, function(arg_8_0, arg_8_1)
			var_7_1[arg_8_0] = 0
		end)
		getProxy(ActivityProxy):updateActivity(var_7_0)
	end)()
	;(function()
		local var_9_0 = var_2_32:getActivityByType(ActivityConst.ACTIVITY_TYPE_EVENT_SINGLE)

		if not var_9_0 or var_9_0:isEnd() then
			return
		end

		arg_2_0:sendNotification(GAME.SINGLE_EVENT_REFRESH, {
			actId = var_9_0.id
		})
	end)()
end

return var_0_0
