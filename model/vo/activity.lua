local var_0_0 = class("Activity", import(".BaseVO"))
local var_0_1

function var_0_0.GetType2Class()
	if var_0_1 then
		return var_0_1
	end

	var_0_1 = {
		[ActivityConst.ACTIVITY_TYPE_INSTAGRAM] = InstagramActivity,
		[ActivityConst.ACTIVITY_TYPE_HITMONSTERNIAN] = BeatMonterNianActivity,
		[ActivityConst.ACTIVITY_TYPE_COLLECTION_EVENT] = CollectionEventActivity,
		[ActivityConst.ACTIVITY_TYPE_RETURN_AWARD] = ReturnerActivity,
		[ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF] = BuildingBuffActivity,
		[ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2] = BuildingBuff2Activity,
		[ActivityConst.ACTIVITY_TYPE_ATELIER_LINK] = AtelierActivity,
		[ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2] = ActivityBossActivity,
		[ActivityConst.ACTIVITY_TYPE_BOSSRUSH] = BossRushActivity,
		[ActivityConst.ACTIVITY_TYPE_EXTRA_BOSSRUSH_RANK] = BossRushRankActivity,
		[ActivityConst.ACTIVITY_TYPE_WORKBENCH] = WorkBenchActivity,
		[ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG] = VirtualBagActivity,
		[ActivityConst.ACTIVITY_TYPE_SCULPTURE] = SculptureActivity,
		[ActivityConst.ACTIVITY_TYPE_HOTSPRING] = SpringActivity,
		[ActivityConst.ACTIVITY_TYPE_HOTSPRING_2] = Spring2Activity,
		[ActivityConst.ACTIVITY_TYPE_TASK_RYZA] = ActivityTaskActivity,
		[ActivityConst.ACTIVITY_TYPE_PUZZLA] = PuzzleActivity,
		[ActivityConst.ACTIVITY_TYPE_SKIN_COUPON] = SkinCouponActivity,
		[ActivityConst.ACTIVITY_TYPE_MANUAL_SIGN] = ManualSignActivity,
		[ActivityConst.ACTIVITY_TYPE_BOSSSINGLE] = BossSingleActivity,
		[ActivityConst.ACTIVITY_TYPE_EVENT_SINGLE] = SingleEventActivity,
		[ActivityConst.ACTIVITY_TYPE_LINER] = LinerActivity
	}

	return var_0_1
end

function var_0_0.Create(arg_2_0)
	local var_2_0 = pg.activity_template[arg_2_0.id]

	return (var_0_0.GetType2Class()[var_2_0.type] or Activity).New(arg_2_0)
end

function var_0_0.Ctor(arg_3_0, arg_3_1)
	arg_3_0.id = arg_3_1.id
	arg_3_0.configId = arg_3_0.id
	arg_3_0.stopTime = arg_3_1.stop_time
	arg_3_0.data1 = defaultValue(arg_3_1.data1, 0)
	arg_3_0.data2 = defaultValue(arg_3_1.data2, 0)
	arg_3_0.data3 = defaultValue(arg_3_1.data3, 0)
	arg_3_0.data4 = defaultValue(arg_3_1.data4, 0)
	arg_3_0.str_data1 = defaultValue(arg_3_1.str_data1, "")
	arg_3_0.data1_list = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_1.data1_list or {}) do
		table.insert(arg_3_0.data1_list, iter_3_1)
	end

	arg_3_0.data2_list = {}

	for iter_3_2, iter_3_3 in ipairs(arg_3_1.data2_list or {}) do
		table.insert(arg_3_0.data2_list, iter_3_3)
	end

	arg_3_0.data3_list = {}

	for iter_3_4, iter_3_5 in ipairs(arg_3_1.data3_list or {}) do
		table.insert(arg_3_0.data3_list, iter_3_5)
	end

	arg_3_0.data4_list = {}

	for iter_3_6, iter_3_7 in ipairs(arg_3_1.data4_list or {}) do
		table.insert(arg_3_0.data4_list, iter_3_7)
	end

	arg_3_0.data1KeyValueList = {}

	for iter_3_8, iter_3_9 in ipairs(arg_3_1.date1_key_value_list or {}) do
		arg_3_0.data1KeyValueList[iter_3_9.key] = {}

		for iter_3_10, iter_3_11 in ipairs(iter_3_9.value_list or {}) do
			arg_3_0.data1KeyValueList[iter_3_9.key][iter_3_11.key] = iter_3_11.value
		end
	end

	arg_3_0.buffList = {}

	for iter_3_12, iter_3_13 in ipairs(arg_3_1.buff_list or {}) do
		table.insert(arg_3_0.buffList, ActivityBuff.New(arg_3_0.id, iter_3_13.id, iter_3_13.timestamp))
	end

	if arg_3_0:getConfig("type") == ActivityConst.ACTIVITY_TYPE_NEWSERVER_SHOP then
		arg_3_0.data2KeyValueList = {}

		for iter_3_14, iter_3_15 in ipairs(arg_3_1.date1_key_value_list or {}) do
			local var_3_0 = iter_3_15.key
			local var_3_1 = iter_3_15.value

			arg_3_0.data2KeyValueList[var_3_0] = {}
			arg_3_0.data2KeyValueList[var_3_0].value = var_3_1
			arg_3_0.data2KeyValueList[var_3_0].dataMap = {}

			for iter_3_16, iter_3_17 in ipairs(iter_3_15.value_list or {}) do
				local var_3_2 = iter_3_17.key
				local var_3_3 = iter_3_17.value

				arg_3_0.data2KeyValueList[var_3_0].dataMap[var_3_2] = var_3_3
			end
		end
	end

	arg_3_0.clientData1 = 0
	arg_3_0.clientList = {}
end

function var_0_0.GetBuffList(arg_4_0)
	return arg_4_0.buffList
end

function var_0_0.AddBuff(arg_5_0, arg_5_1)
	assert(isa(arg_5_1, ActivityBuff), "activityBuff should instance of ActivityBuff")
	table.insert(arg_5_0.buffList, arg_5_1)
end

function var_0_0.setClientList(arg_6_0, arg_6_1)
	arg_6_0.clientList = arg_6_1
end

function var_0_0.getClientList(arg_7_0)
	return arg_7_0.clientList
end

function var_0_0.updateDataList(arg_8_0, arg_8_1)
	table.insert(arg_8_0.data1_list, arg_8_1)
end

function var_0_0.setDataList(arg_9_0, arg_9_1)
	arg_9_0.data1_list = arg_9_1
end

function var_0_0.updateKVPList(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	if not arg_10_0.data1KeyValueList[arg_10_1] then
		arg_10_0.data1KeyValueList[arg_10_1] = {}
	end

	arg_10_0.data1KeyValueList[arg_10_1][arg_10_2] = arg_10_3
end

function var_0_0.getKVPList(arg_11_0, arg_11_1, arg_11_2)
	if not arg_11_0.data1KeyValueList[arg_11_1] then
		arg_11_0.data1KeyValueList[arg_11_1] = {}
	end

	return arg_11_0.data1KeyValueList[arg_11_1][arg_11_2] or 0
end

function var_0_0.getData1(arg_12_0)
	return arg_12_0.data1
end

function var_0_0.getStrData1(arg_13_0)
	return arg_13_0.str_data1
end

function var_0_0.getData3(arg_14_0)
	return arg_14_0.data3
end

function var_0_0.getData1List(arg_15_0)
	return arg_15_0.data1_list
end

function var_0_0.bindConfigTable(arg_16_0)
	return pg.activity_template
end

function var_0_0.getDataConfigTable(arg_17_0)
	local var_17_0 = arg_17_0:getConfig("type")
	local var_17_1 = arg_17_0:getConfig("config_id")

	if var_17_0 == ActivityConst.ACTIVITY_TYPE_MONOPOLY then
		return pg.activity_event_monopoly[tonumber(var_17_1)]
	elseif var_17_0 == ActivityConst.ACTIVITY_TYPE_PIZZA_PT or var_17_0 == ActivityConst.ACTIVITY_TYPE_PT_BUFF then
		return pg.activity_event_pt[tonumber(var_17_1)]
	elseif var_17_0 == ActivityConst.ACTIVITY_TYPE_VOTE then
		return pg.activity_vote[tonumber(var_17_1)]
	end
end

function var_0_0.getDataConfig(arg_18_0, arg_18_1)
	local var_18_0 = arg_18_0:getDataConfigTable()

	assert(var_18_0, "miss config : " .. arg_18_0.id)

	return var_18_0 and var_18_0[arg_18_1]
end

function var_0_0.isEnd(arg_19_0)
	return arg_19_0.stopTime > 0 and pg.TimeMgr.GetInstance():GetServerTime() >= arg_19_0.stopTime
end

function var_0_0.increaseUsedCount(arg_20_0, arg_20_1)
	if arg_20_1 == 1 then
		arg_20_0.data1 = arg_20_0.data1 + 1
	elseif arg_20_1 == 2 then
		arg_20_0.data2 = arg_20_0.data2 + 1
	end
end

function var_0_0.readyToAchieve(arg_21_0)
	local var_21_0, var_21_1 = arg_21_0:IsShowTipById()

	if var_21_0 then
		return var_21_1
	end

	var_0_0.readyToAchieveDic = var_0_0.readyToAchieveDic or {
		[ActivityConst.ACTIVITY_TYPE_CARD_PAIRS] = function(arg_22_0)
			local var_22_0 = os.difftime(pg.TimeMgr.GetInstance():GetServerTime(), arg_22_0.data3)

			return math.ceil(var_22_0 / 86400) > arg_22_0.data2 and arg_22_0.data2 < arg_22_0:getConfig("config_data")[4]
		end,
		[ActivityConst.ACTIVITY_TYPE_LEVELAWARD] = function(arg_23_0)
			local var_23_0 = getProxy(PlayerProxy):getRawData()
			local var_23_1 = pg.activity_level_award[arg_23_0:getConfig("config_id")]

			for iter_23_0 = 1, #var_23_1.front_drops do
				local var_23_2 = var_23_1.front_drops[iter_23_0][1]

				if var_23_2 <= var_23_0.level and not _.include(arg_23_0.data1_list, var_23_2) then
					return true
				end
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_STORY_AWARD] = function(arg_24_0)
			local var_24_0 = getProxy(PlayerProxy):getRawData()
			local var_24_1 = pg.activity_event_chapter_award[arg_24_0:getConfig("config_id")]

			for iter_24_0 = 1, #var_24_1.chapter do
				local var_24_2 = var_24_1.chapter[iter_24_0]

				if getProxy(ChapterProxy):isClear(var_24_2) and not _.include(arg_24_0.data1_list, var_24_2) then
					return true
				end
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_TASKS] = function(arg_25_0)
			local var_25_0 = getProxy(TaskProxy)
			local var_25_1 = _.flatten(arg_25_0:getConfig("config_data"))

			if _.any(var_25_1, function(arg_26_0)
				local var_26_0 = var_25_0:getTaskById(arg_26_0)

				return var_26_0 and var_26_0:isFinish() and not var_26_0:isReceive()
			end) then
				return true
			end

			local var_25_2 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_WORLDINPICTURE)

			if var_25_2 and not var_25_2:isEnd() and var_25_2:getConfig("config_client").linkActID == arg_25_0.id and var_25_2:readyToAchieve() then
				return true
			end

			if arg_25_0:getConfig("config_client") and arg_25_0:getConfig("config_client").decodeGameId then
				local var_25_3 = arg_25_0:getConfig("config_client").decodeGameId
				local var_25_4 = getProxy(MiniGameProxy):GetHubByGameId(var_25_3)

				if var_25_4 then
					local var_25_5 = arg_25_0:getConfig("config_data")
					local var_25_6 = var_25_5[#var_25_5]
					local var_25_7 = _.all(var_25_6, function(arg_27_0)
						return getProxy(TaskProxy):getFinishTaskById(arg_27_0) ~= nil
					end)

					if var_25_4.ultimate <= 0 and var_25_7 then
						return true
					end
				end
			end

			if arg_25_0:getConfig("config_client") and arg_25_0:getConfig("config_client").linkTaskPoolAct then
				local var_25_8 = arg_25_0:getConfig("config_client").linkTaskPoolAct
				local var_25_9 = getProxy(ActivityProxy):getActivityById(var_25_8)

				if var_25_9 and var_25_9:readyToAchieve() then
					return true
				end
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_TASK_LIST] = function(...)
			return var_0_0.readyToAchieveDic[ActivityConst.ACTIVITY_TYPE_TASKS](...)
		end,
		[ActivityConst.ACTIVITY_TYPE_HITMONSTERNIAN] = function(arg_29_0)
			local var_29_0 = arg_29_0:GetCountForHitMonster()

			return not (arg_29_0:GetDataConfig("hp") <= arg_29_0.data3) and var_29_0 > 0
		end,
		[ActivityConst.ACTIVITY_TYPE_DODGEM] = function(arg_30_0)
			local var_30_0 = pg.TimeMgr.GetInstance()
			local var_30_1 = var_30_0:DiffDay(arg_30_0.data1, var_30_0:GetServerTime()) + 1
			local var_30_2 = arg_30_0:getConfig("config_id")

			if var_30_2 == 1 then
				return arg_30_0.data4 == 0 and arg_30_0.data2 >= 7 or defaultValue(arg_30_0.data2_list[1], 0) > 0 or defaultValue(arg_30_0.data2_list[2], 0) > 0 or arg_30_0.data2 < math.min(var_30_1, 7) or var_30_1 > arg_30_0.data3
			elseif var_30_2 == 2 then
				return arg_30_0.data4 == 0 and arg_30_0.data2 >= 7 or defaultValue(arg_30_0.data2_list[1], 0) > 0 or defaultValue(arg_30_0.data2_list[2], 0) > 0 or arg_30_0.data2 < math.min(var_30_1, 7)
			end
		end,
		[ActivityConst.ACTIVITY_TYPE_MONOPOLY] = function(arg_31_0)
			local var_31_0 = arg_31_0.data1
			local var_31_1 = arg_31_0.data1_list[1]
			local var_31_2 = arg_31_0.data1_list[2]
			local var_31_3 = arg_31_0.data2_list[1]
			local var_31_4 = arg_31_0.data2_list[2]
			local var_31_5 = pg.TimeMgr.GetInstance():GetServerTime()
			local var_31_6 = math.ceil((var_31_5 - var_31_0) / 86400) * arg_31_0:getDataConfig("daily_time") + var_31_1 - var_31_2
			local var_31_7 = var_31_3 - var_31_4

			return var_31_6 > 0
		end,
		[ActivityConst.ACTIVITY_TYPE_PIZZA_PT] = function(arg_32_0)
			local var_32_0 = ActivityPtData.New(arg_32_0):CanGetAward()
			local var_32_1 = true

			if arg_32_0:getConfig("config_client") then
				local var_32_2 = arg_32_0:getConfig("config_client").task_act_id

				if var_32_2 and var_32_2 ~= 0 and pg.activity_template[var_32_2] then
					local var_32_3 = pg.activity_template[var_32_2]
					local var_32_4 = _.flatten(var_32_3.config_data)

					if var_32_4 and #var_32_4 > 0 then
						local var_32_5 = getProxy(TaskProxy)

						for iter_32_0 = 1, #var_32_4 do
							local var_32_6 = var_32_5:getTaskById(var_32_4[iter_32_0])

							if var_32_6 and var_32_6:isFinish() then
								return true
							end
						end
					end
				end
			end

			local var_32_7 = false
			local var_32_8 = arg_32_0:getConfig("config_client").fireworkActID

			if var_32_8 and var_32_8 ~= 0 then
				local var_32_9 = getProxy(ActivityProxy):getActivityById(var_32_8)

				var_32_7 = var_32_9 and var_32_9:readyToAchieve() or false
			end

			local var_32_10 = arg_32_0:getConfig("config_client")[2]
			local var_32_11 = type(var_32_10) == "number" and ManualSignActivity.IsManualSignActAndAnyAwardCanGet(var_32_10)

			return var_32_0 and var_32_1 or var_32_7 or var_32_11
		end,
		[ActivityConst.ACTIVITY_TYPE_PT_BUFF] = function(...)
			return var_0_0.readyToAchieveDic[ActivityConst.ACTIVITY_TYPE_PIZZA_PT](...)
		end,
		[ActivityConst.ACTIVITY_TYPE_RETURN_AWARD] = function(arg_34_0)
			local var_34_0 = arg_34_0.data1

			if var_34_0 == 1 then
				local var_34_1 = pg.activity_template_headhunting[arg_34_0.id]
				local var_34_2 = var_34_1.target
				local var_34_3 = 0

				for iter_34_0, iter_34_1 in ipairs(arg_34_0:getClientList()) do
					var_34_3 = var_34_3 + iter_34_1:getPt()
				end

				local var_34_4 = 0

				for iter_34_2 = #var_34_2, 1, -1 do
					if table.contains(arg_34_0.data1_list, var_34_2[iter_34_2]) then
						var_34_4 = iter_34_2

						break
					end
				end

				local var_34_5 = var_34_1.drop_client
				local var_34_6 = math.min(var_34_4 + 1, #var_34_5)
				local var_34_7 = _.any(var_34_1.tasklist, function(arg_35_0)
					local var_35_0 = getProxy(TaskProxy):getTaskById(arg_35_0)

					return var_35_0 and var_35_0:isFinish() and not var_35_0:isReceive()
				end)

				return var_34_3 >= var_34_2[var_34_6] and var_34_4 ~= #var_34_5 or var_34_7
			elseif var_34_0 == 2 then
				local var_34_8 = getProxy(TaskProxy)
				local var_34_9 = pg.activity_template_returnner[arg_34_0.id]

				return _.any(_.flatten(var_34_9.task_list), function(arg_36_0)
					local var_36_0 = var_34_8:getTaskById(arg_36_0)

					return var_36_0 and var_36_0:isFinish()
				end)
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_MINIGAME] = function(arg_37_0)
			local var_37_0 = getProxy(MiniGameProxy):GetHubByHubId(arg_37_0:getConfig("config_id"))

			if var_37_0.count > 0 then
				return true
			end

			if var_37_0:getConfig("reward") ~= 0 and var_37_0.usedtime >= var_37_0:getConfig("reward_need") and var_37_0.ultimate == 0 then
				return true
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_TURNTABLE] = function(arg_38_0)
			local var_38_0 = pg.activity_event_turning[arg_38_0:getConfig("config_id")]
			local var_38_1 = arg_38_0.data4

			if var_38_1 ~= 0 then
				local var_38_2 = var_38_0.task_table[var_38_1]
				local var_38_3 = getProxy(TaskProxy)

				for iter_38_0, iter_38_1 in ipairs(var_38_2) do
					if (var_38_3:getTaskById(iter_38_1) or var_38_3:getFinishTaskById(iter_38_1)):getTaskStatus() == 1 then
						return true
					end
				end

				local var_38_4 = pg.TimeMgr.GetInstance():DiffDay(arg_38_0.data1, pg.TimeMgr.GetInstance():GetServerTime()) + 1

				if math.clamp(var_38_4, 1, pg.activity_event_turning[arg_38_0:getConfig("config_id")].total_num) > arg_38_0.data3 then
					for iter_38_2, iter_38_3 in ipairs(var_38_2) do
						if (var_38_3:getTaskById(iter_38_3) or var_38_3:getFinishTaskById(iter_38_3)):getTaskStatus() ~= 2 then
							return false
						end
					end

					return true
				end
			elseif var_38_1 == 0 then
				local var_38_5 = pg.TimeMgr.GetInstance():DiffDay(arg_38_0.data1, pg.TimeMgr.GetInstance():GetServerTime()) + 1

				if math.clamp(var_38_5, 1, pg.activity_event_turning[arg_38_0:getConfig("config_id")].total_num) > arg_38_0.data3 then
					return true
				end
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_LOTTERY_AWARD] = function(arg_39_0)
			return not (arg_39_0.data2 > 0)
		end,
		[ActivityConst.ACTIVITY_TYPE_SHRINE] = function(arg_40_0)
			local var_40_0 = arg_40_0:getConfig("config_client").story
			local var_40_1 = var_40_0 and #var_40_0 or 7
			local var_40_2 = pg.TimeMgr.GetInstance():DiffDay(arg_40_0.data3, pg.TimeMgr.GetInstance():GetServerTime()) + 1
			local var_40_3 = math.clamp(var_40_2, 1, var_40_1)
			local var_40_4 = pg.NewStoryMgr.GetInstance()
			local var_40_5 = math.clamp(arg_40_0.data2, 0, var_40_1)

			for iter_40_0 = 1, var_40_3 do
				local var_40_6 = var_40_0[iter_40_0][1]

				if var_40_6 and iter_40_0 <= var_40_5 and not var_40_4:IsPlayed(var_40_6) then
					return true
				end
			end

			if var_40_1 <= var_40_3 and var_40_1 <= arg_40_0.data2 and not (arg_40_0.data1 > 0) then
				return true
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_LINK_LINK] = function(arg_41_0)
			local var_41_0 = arg_41_0:getConfig("config_client")[3]
			local var_41_1 = pg.TimeMgr.GetInstance()
			local var_41_2 = var_41_1:DiffDay(arg_41_0.data3, var_41_1:GetServerTime()) + 1 - arg_41_0.data2

			return math.clamp(var_41_2, 0, #var_41_0 - arg_41_0.data2) > 0
		end,
		[ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF] = function(arg_42_0)
			local var_42_0 = arg_42_0:GetBuildingIds()

			for iter_42_0, iter_42_1 in ipairs(var_42_0) do
				local var_42_1 = arg_42_0:GetBuildingLevel(iter_42_1)
				local var_42_2 = pg.activity_event_building[iter_42_1]

				if var_42_2 and var_42_1 < #var_42_2.buff then
					local var_42_3 = var_42_2.material[var_42_1]

					if underscore.all(var_42_3, function(arg_43_0)
						local var_43_0 = arg_43_0[1]
						local var_43_1 = arg_43_0[2]
						local var_43_2 = arg_43_0[3]
						local var_43_3 = 0

						if var_43_0 == DROP_TYPE_VITEM then
							local var_43_4 = AcessWithinNull(Item.getConfigData(var_43_1), "link_id")

							assert(var_43_4 == arg_42_0.id)

							var_43_3 = arg_42_0:GetMaterialCount(var_43_1)
						elseif var_43_0 > DROP_TYPE_USE_ACTIVITY_DROP then
							local var_43_5 = AcessWithinNull(pg.activity_drop_type[var_43_0], "activity_id")

							assert(var_43_5)

							bagAct = getProxy(ActivityProxy):getActivityById(var_43_5)
							var_43_3 = bagAct:getVitemNumber(var_43_1)
						end

						return var_43_2 <= var_43_3
					end) then
						return true
					end
				end
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2] = function(arg_44_0, ...)
			return var_0_0.readyToAchieveDic[ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF](arg_44_0, ...) or arg_44_0:CanRequest()
		end,
		[ActivityConst.ACTIVITY_TYPE_EXPEDITION] = function(arg_45_0)
			if arg_45_0.data3 > 0 and arg_45_0.data1 ~= 0 then
				return true
			else
				for iter_45_0 = 1, #arg_45_0.data1_list do
					if not bit.band(arg_45_0.data1_list[iter_45_0], ActivityConst.EXPEDITION_TYPE_GOT) ~= 0 then
						if bit.band(arg_45_0.data1_list[iter_45_0], ActivityConst.EXPEDITION_TYPE_OPEN) ~= 0 then
							return true
						elseif bit.band(arg_45_0.data1_list[iter_45_0], ActivityConst.EXPEDITION_TYPE_BAOXIANG) ~= 0 then
							return true
						elseif bit.band(arg_45_0.data1_list[iter_45_0], ActivityConst.EXPEDITION_TYPE_BOSS) ~= 0 then
							return true
						end
					end
				end
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_CLIENT_DISPLAY] = function(arg_46_0)
			local var_46_0 = arg_46_0:getConfig("config_client")

			if var_46_0 and var_46_0.linkGameHubID then
				local var_46_1 = getProxy(MiniGameProxy):GetHubByHubId(var_46_0.linkGameHubID)

				if var_46_1 then
					if var_46_0.trimRed then
						if var_46_1.ultimate == 1 then
							return false
						end

						if var_46_1.usedtime == var_46_1:getConfig("reward_need") then
							return true
						end
					end

					return var_46_1.count > 0
				end
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_BB] = function(arg_47_0)
			return arg_47_0.data2 > 0
		end,
		[ActivityConst.ACTIVITY_TYPE_PUZZLA] = function(arg_48_0)
			local var_48_0 = arg_48_0.data1_list
			local var_48_1 = arg_48_0.data2_list
			local var_48_2 = arg_48_0:GetPicturePuzzleIds()
			local var_48_3 = arg_48_0:getConfig("config_client").linkActID

			if var_48_3 then
				local var_48_4 = getProxy(ActivityProxy):getActivityById(var_48_3)

				if var_48_4 and var_48_4:readyToAchieve() then
					return true
				end
			end

			if _.any(var_48_2, function(arg_49_0)
				local var_49_0 = table.contains(var_48_1, arg_49_0)
				local var_49_1 = table.contains(var_48_0, arg_49_0)

				return not var_49_0 and var_49_1
			end) then
				return true
			end

			local var_48_5 = pg.activity_event_picturepuzzle[arg_48_0.id]

			if var_48_5 and var_48_5.chapter > 0 and arg_48_0.data1 < 1 then
				return true
			end

			if var_48_5 and #var_48_5.auto_finish_args > 0 and arg_48_0.data1 == 1 then
				return true
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_WORLDINPICTURE] = function(arg_50_0)
			local var_50_0 = WorldInPictureActiviyData.New(arg_50_0)

			return not var_50_0:IsTravelAll() and var_50_0:GetTravelPoint() > 0 or var_50_0:GetDrawPoint() > 0 and var_50_0:AnyAreaCanDraw()
		end,
		[ActivityConst.ACTIVITY_TYPE_APRIL_REWARD] = function(arg_51_0)
			if arg_51_0.data1 == 0 then
				local var_51_0 = arg_51_0:getStartTime()
				local var_51_1 = pg.TimeMgr.GetInstance():GetServerTime()

				if arg_51_0:getConfig("config_client").autounlock <= var_51_1 - var_51_0 then
					return true
				end
			elseif arg_51_0.data1 ~= 0 and arg_51_0.data2 == 0 then
				return true
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_TASK_POOL] = function(arg_52_0)
			local var_52_0 = arg_52_0:getConfig("config_data")
			local var_52_1 = getProxy(TaskProxy)

			if arg_52_0.data1 >= #var_52_0 then
				return false
			end

			local var_52_2 = pg.TimeMgr.GetInstance()
			local var_52_3 = (var_52_2:DiffDay(arg_52_0:getStartTime(), var_52_2:GetServerTime()) + 1) * arg_52_0:getConfig("config_id")

			var_52_3 = var_52_3 > #var_52_0 and #var_52_0 or var_52_3

			local var_52_4 = _.any(var_52_0, function(arg_53_0)
				local var_53_0 = var_52_1:getTaskById(arg_53_0)

				return var_53_0 and var_53_0:isFinish()
			end)

			return var_52_3 - arg_52_0.data1 > 0 and var_52_4
		end,
		[ActivityConst.ACTIVITY_TYPE_EVENT] = function(arg_54_0)
			local var_54_0 = getProxy(PlayerProxy):getData().id

			return PlayerPrefs.GetInt("ACTIVITY_TYPE_EVENT_" .. arg_54_0.id .. "_" .. var_54_0) == 0
		end,
		[ActivityConst.ACTIVITY_TYPE_PT_OTHER] = function(arg_55_0)
			if arg_55_0.data2 and arg_55_0.data2 <= 0 and arg_55_0.data1 >= pg.activity_event_avatarframe[arg_55_0:getConfig("config_id")].target then
				return true
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_HOTSPRING] = function(arg_56_0)
			local var_56_0, var_56_1 = arg_56_0:GetUpgradeCost()

			if arg_56_0:GetSlotCount() < arg_56_0:GetTotalSlotCount() and var_56_1 <= arg_56_0:GetCoins() then
				return true
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_FIREWORK] = function(arg_57_0)
			local var_57_0 = arg_57_0:getConfig("config_data")[2][1]
			local var_57_1 = arg_57_0:getConfig("config_data")[2][2]
			local var_57_2 = getProxy(PlayerProxy):getRawData():getResource(var_57_0)

			if arg_57_0.data1 > 0 and var_57_1 <= var_57_2 then
				return true
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_FLOWER_FIELD] = function(arg_58_0)
			local var_58_0 = pg.TimeMgr.GetInstance()

			return var_58_0:GetServerTime() >= var_58_0:GetTimeToNextTime(math.max(arg_58_0.data1, arg_58_0.data2))
		end,
		[ActivityConst.ACTIVITY_TYPE_ISLAND] = function(arg_59_0)
			for iter_59_0, iter_59_1 in pairs(getProxy(IslandProxy):GetNodeDic()) do
				if iter_59_1:IsVisual() and iter_59_1:RedDotHint() then
					return true
				end
			end

			return false
		end,
		[ActivityConst.ACTIVITY_TYPE_HOTSPRING_2] = function(arg_60_0)
			return Spring2Activity.readyToAchieve(arg_60_0)
		end,
		[ActivityConst.ACTIVITY_TYPE_CARD_PUZZLE] = function(arg_61_0)
			local var_61_0 = #arg_61_0.data2_list
			local var_61_1 = arg_61_0:getData1List()
			local var_61_2 = arg_61_0:getConfig("config_data")[2]

			if #var_61_1 == #var_61_2 then
				return false
			end

			local function var_61_3()
				for iter_62_0, iter_62_1 in ipairs(var_61_2) do
					if not table.contains(var_61_1, iter_62_1[1]) and var_61_0 >= iter_62_1[1] then
						return true
					end
				end

				return false
			end

			local function var_61_4()
				local var_63_0 = getProxy(PlayerProxy):getData().id

				return PlayerPrefs.GetInt("DAY_TIP_" .. arg_61_0.id .. "_" .. var_63_0 .. "_" .. arg_61_0:getDayIndex()) == 0
			end

			return var_61_3() or var_61_4()
		end,
		[ActivityConst.ACTIVITY_TYPE_SURVEY] = function(arg_64_0)
			local var_64_0, var_64_1 = getProxy(ActivityProxy):isSurveyOpen()

			return var_64_0 and not SurveyPage.IsEverEnter(var_64_1)
		end,
		[ActivityConst.ACTIVITY_TYPE_ZUMA] = function(arg_65_0)
			return LaunchBallActivityMgr.GetInvitationAble(arg_65_0.id)
		end,
		[ActivityConst.ACTIVITY_TYPE_GIFT_UP] = function(arg_66_0)
			local var_66_0 = arg_66_0:getConfig("config_client").gifts[2]
			local var_66_1 = math.min(#var_66_0, arg_66_0:getNDay())

			return underscore(var_66_0):chain():first(var_66_1):any(function(arg_67_0)
				local var_67_0 = getProxy(ShopsProxy):GetGiftCommodity(arg_67_0, Goods.TYPE_GIFT_PACKAGE)

				return var_67_0:canPurchase() and var_67_0:inTime() and not var_67_0:IsGroupLimit()
			end):value()
		end,
		[ActivityConst.ACTIVITY_TYPE_UR_EXCHANGE] = function(arg_68_0)
			if getProxy(ShopsProxy):getActivityShops() == nil then
				return false
			end

			local var_68_0 = arg_68_0:getConfig("config_client")
			local var_68_1 = getProxy(PlayerProxy):getData():getResource(var_68_0.uPtId)
			local var_68_2 = #var_68_0.goodsId + 1
			local var_68_3 = var_68_2 - _.reduce(var_68_0.goodsId, 0, function(arg_69_0, arg_69_1)
				return arg_69_0 + getProxy(ShopsProxy):getActivityShopById(var_68_0.shopId):GetCommodityById(arg_69_1):GetPurchasableCnt()
			end)
			local var_68_4 = var_68_3 < var_68_2 and pg.activity_shop_template[var_68_0.goodsId[var_68_3]] or nil

			return var_68_3 < var_68_2 and var_68_1 >= var_68_4.resource_num
		end
	}

	return switch(arg_21_0:getConfig("type"), var_0_0.readyToAchieveDic, nil, arg_21_0)
end

function var_0_0.IsShowTipById(arg_70_0)
	var_0_0.ShowTipTableById = var_0_0.ShowTipTableById or {
		[ActivityConst.ACTIVITY_ID_US_SKIRMISH_RE] = function()
			local var_71_0 = getProxy(SkirmishProxy)

			var_71_0:UpdateSkirmishProgress()

			local var_71_1 = var_71_0:getRawData()
			local var_71_2 = 0
			local var_71_3 = 0

			for iter_71_0, iter_71_1 in ipairs(var_71_1) do
				local var_71_4 = iter_71_1:GetState()

				var_71_2 = var_71_4 > SkirmishVO.StateInactive and var_71_2 + 1 or var_71_2
				var_71_3 = var_71_4 == SkirmishVO.StateClear and var_71_3 + 1 or var_71_3
			end

			return var_71_3 < var_71_2
		end,
		[ActivityConst.POCKY_SKIN_LOGIN] = function()
			local var_72_0 = arg_70_0:getConfig("config_client").linkids
			local var_72_1 = getProxy(TaskProxy)
			local var_72_2 = getProxy(ActivityProxy)
			local var_72_3 = var_72_2:getActivityById(var_72_0[1])
			local var_72_4 = var_72_2:getActivityById(var_72_0[2])
			local var_72_5 = var_72_2:getActivityById(var_72_0[3])

			assert(var_72_3 and var_72_4 and var_72_5)

			local function var_72_6()
				return var_72_3 and var_72_3:readyToAchieve()
			end

			local function var_72_7()
				return var_72_4 and var_72_4:readyToAchieve()
			end

			local function var_72_8()
				local var_75_0 = _.flatten(arg_70_0:getConfig("config_data"))

				for iter_75_0 = 1, math.min(#var_75_0, var_72_4.data3) do
					local var_75_1 = var_75_0[iter_75_0]
					local var_75_2 = var_72_1:getTaskById(var_75_1)

					if var_75_2 and var_75_2:isFinish() and not var_75_2:isReceive() then
						return true
					end
				end
			end

			local function var_72_9()
				if not (var_72_5 and var_72_5:readyToAchieve()) or not var_72_3 then
					return false
				end

				local var_76_0 = ActivityPtData.New(var_72_3)

				return var_76_0.level >= #var_76_0.targets
			end

			return var_72_8() or var_72_6() or var_72_7() or var_72_9()
		end,
		[ActivityConst.TOWERCLIMBING_SIGN] = function()
			local var_77_0 = getProxy(MiniGameProxy):GetHubByHubId(9)
			local var_77_1 = var_77_0.ultimate
			local var_77_2 = var_77_0:getConfig("reward_need")
			local var_77_3 = var_77_0.usedtime

			return var_77_1 == 0 and var_77_2 <= var_77_3
		end,
		[pg.activity_const.NEWYEAR_SNACK_PAGE_ID.act_id] = NewYearSnackPage.IsTip,
		[ActivityConst.WWF_TASK_ID] = WWFPtPage.IsShowRed,
		[ActivityConst.NEWMEIXIV4_SKIRMISH_ID] = NewMeixiV4SkirmishPage.IsShowRed,
		[ActivityConst.JIUJIU_YOYO_ID] = JiujiuYoyoPage.IsShowRed,
		[ActivityConst.SENRANKAGURA_TRAIN_ACT_ID] = SenrankaguraTrainScene.IsShowRed
	}

	local var_70_0 = var_0_0.ShowTipTableById[arg_70_0.id]

	return tobool(var_70_0), var_70_0 and var_70_0()
end

function var_0_0.isShow(arg_78_0)
	if arg_78_0:getConfig("is_show") <= 0 then
		return false
	end

	if arg_78_0:getConfig("type") == ActivityConst.ACTIVITY_TYPE_RETURN_AWARD then
		return arg_78_0.data1 ~= 0
	elseif arg_78_0:getConfig("type") == ActivityConst.ACTIVITY_TYPE_CLIENT_DISPLAY then
		local var_78_0 = arg_78_0:getConfig("config_client").display_link

		if var_78_0 then
			return underscore.any(var_78_0, function(arg_79_0)
				return arg_79_0[2] == 0 or pg.TimeMgr.GetInstance():inTime(pg.shop_template[arg_79_0[2]].time)
			end)
		end
	elseif arg_78_0:getConfig("type") == ActivityConst.ACTIVITY_TYPE_SURVEY then
		local var_78_1 = getProxy(ActivityProxy)
		local var_78_2 = var_78_1:isSurveyOpen()
		local var_78_3 = var_78_1:isSurveyDone()

		return var_78_2 and not var_78_3
	elseif arg_78_0:getConfig("type") == ActivityConst.ACTIVITY_TYPE_UR_EXCHANGE then
		if getProxy(ShopsProxy):getActivityShops() == nil then
			return false
		end

		local var_78_4 = arg_78_0:getConfig("config_client")
		local var_78_5 = getProxy(PlayerProxy):getData():getResource(var_78_4.uPtId)
		local var_78_6 = #var_78_4.goodsId + 1

		return var_78_6 > var_78_6 - _.reduce(var_78_4.goodsId, 0, function(arg_80_0, arg_80_1)
			return arg_80_0 + getProxy(ShopsProxy):getActivityShopById(var_78_4.shopId):GetCommodityById(arg_80_1):GetPurchasableCnt()
		end)
	end

	return true
end

function var_0_0.isAfterShow(arg_81_0)
	if arg_81_0.configId == ActivityConst.UR_TASK_ACT_ID or arg_81_0.configId == ActivityConst.SPECIAL_WEAPON_ACT_ID then
		local var_81_0 = getProxy(TaskProxy)

		return underscore.all(arg_81_0:getConfig("config_data")[1], function(arg_82_0)
			local var_82_0 = var_81_0:getTaskVO(arg_82_0)

			return var_82_0 and var_82_0:isReceive()
		end)
	end

	return false
end

function var_0_0.getShowPriority(arg_83_0)
	return arg_83_0:getConfig("is_show")
end

function var_0_0.left4Day(arg_84_0)
	if arg_84_0.stopTime - pg.TimeMgr.GetInstance():GetServerTime() < 345600 then
		return true
	end

	return false
end

function var_0_0.getAwardInfos(arg_85_0)
	return arg_85_0.data1KeyValueList or {}
end

function var_0_0.updateData(arg_86_0, arg_86_1, arg_86_2)
	if arg_86_0:getConfig("type") == ActivityConst.ACTIVITY_TYPE_LOTTERY then
		if not arg_86_0:getAwardInfos()[arg_86_1] then
			arg_86_0.data1KeyValueList[arg_86_1] = {}
		end

		for iter_86_0, iter_86_1 in ipairs(arg_86_2) do
			if arg_86_0.data1KeyValueList[arg_86_1][iter_86_1] then
				arg_86_0.data1KeyValueList[arg_86_1][iter_86_1] = arg_86_0.data1KeyValueList[arg_86_1][iter_86_1] + 1
			else
				arg_86_0.data1KeyValueList[arg_86_1][iter_86_1] = 1
			end
		end
	end
end

function var_0_0.getTaskShip(arg_87_0)
	return arg_87_0:getConfig("config_client")[1]
end

function var_0_0.getNotificationMsg(arg_88_0)
	local var_88_0 = arg_88_0:getConfig("type")
	local var_88_1 = ActivityProxy.ACTIVITY_SHOW_AWARDS

	if var_88_0 == ActivityConst.ACTIVITY_TYPE_SHOP then
		var_88_1 = ActivityProxy.ACTIVITY_SHOP_SHOW_AWARDS
	elseif var_88_0 == ActivityConst.ACTIVITY_TYPE_LOTTERY then
		var_88_1 = ActivityProxy.ACTIVITY_LOTTERY_SHOW_AWARDS
	elseif var_88_0 == ActivityConst.ACTIVITY_TYPE_REFLUX then
		var_88_1 = ActivityProxy.ACTIVITY_SHOW_REFLUX_AWARDS
	elseif var_88_0 == ActivityConst.ACTIVITY_TYPE_RED_PACKETS or var_88_0 == ActivityConst.ACTIVITY_TYPE_RED_PACKET_LOTTER then
		var_88_1 = ActivityProxy.ACTIVITY_SHOW_RED_PACKET_AWARDS
	end

	return var_88_1
end

function var_0_0.getDayIndex(arg_89_0)
	local var_89_0 = arg_89_0:getStartTime()
	local var_89_1 = pg.TimeMgr.GetInstance()
	local var_89_2 = var_89_1:GetServerTime()

	return var_89_1:DiffDay(var_89_0, var_89_2) + 1
end

function var_0_0.getStartTime(arg_90_0)
	local var_90_0, var_90_1 = parseTimeConfig(arg_90_0:getConfig("time"))

	if var_90_1 and var_90_1[1] == "newuser" then
		return arg_90_0.stopTime - var_90_1[3] * 86400
	else
		return pg.TimeMgr.GetInstance():parseTimeFromConfig(var_90_0[2])
	end
end

function var_0_0.getNDay(arg_91_0, arg_91_1)
	arg_91_1 = arg_91_1 or arg_91_0:getStartTime()

	local var_91_0 = pg.TimeMgr.GetInstance()

	return var_91_0:DiffDay(arg_91_1, var_91_0:GetServerTime()) + 1
end

function var_0_0.isVariableTime(arg_92_0)
	local var_92_0, var_92_1 = parseTimeConfig(arg_92_0:getConfig("time"))

	return var_92_1 and var_92_1[1] == "newuser"
end

function var_0_0.setSpecialData(arg_93_0, arg_93_1, arg_93_2)
	arg_93_0.speciaData = arg_93_0.speciaData and arg_93_0.speciaData or {}
	arg_93_0.speciaData[arg_93_1] = arg_93_2
end

function var_0_0.getSpecialData(arg_94_0, arg_94_1)
	return arg_94_0.speciaData and arg_94_0.speciaData[arg_94_1] and arg_94_0.speciaData[arg_94_1] or nil
end

function var_0_0.canPermanentFinish(arg_95_0)
	local var_95_0 = arg_95_0:getConfig("type")

	if var_95_0 == ActivityConst.ACTIVITY_TYPE_TASK_LIST then
		local var_95_1 = arg_95_0:getConfig("config_data")
		local var_95_2 = getProxy(TaskProxy)

		return underscore.all(underscore.flatten({
			var_95_1[#var_95_1]
		}), function(arg_96_0)
			return var_95_2:getFinishTaskById(arg_96_0) ~= nil
		end)
	elseif var_95_0 == ActivityConst.ACTIVITY_TYPE_PT_BUFF then
		local var_95_3 = ActivityPtData.New(arg_95_0)

		return var_95_3.level >= #var_95_3.targets
	end

	return false
end

function var_0_0.GetShopTime(arg_97_0)
	local var_97_0 = pg.TimeMgr.GetInstance()
	local var_97_1 = arg_97_0:getStartTime()
	local var_97_2 = arg_97_0.stopTime

	return var_97_0:STimeDescS(var_97_1, "%y.%m.%d") .. " - " .. var_97_0:STimeDescS(var_97_2, "%y.%m.%d")
end

function var_0_0.GetCrusingUnreceiveAward(arg_98_0)
	assert(arg_98_0:getConfig("type") == ActivityConst.ACTIVITY_TYPE_PT_CRUSING, "type error")

	local var_98_0 = pg.battlepass_event_pt[arg_98_0.id]
	local var_98_1 = {}
	local var_98_2 = {}

	for iter_98_0, iter_98_1 in ipairs(arg_98_0.data1_list) do
		var_98_2[iter_98_1] = true
	end

	for iter_98_2, iter_98_3 in ipairs(var_98_0.target) do
		if iter_98_3 > arg_98_0.data1 then
			break
		elseif not var_98_2[iter_98_3] then
			table.insert(var_98_1, Drop.Create(var_98_0.drop_client[iter_98_2]))
		end
	end

	if arg_98_0.data2 ~= 1 then
		return PlayerConst.MergePassItemDrop(var_98_1)
	end

	local var_98_3 = {}

	for iter_98_4, iter_98_5 in ipairs(arg_98_0.data2_list) do
		var_98_3[iter_98_5] = true
	end

	for iter_98_6, iter_98_7 in ipairs(var_98_0.target) do
		if iter_98_7 > arg_98_0.data1 then
			break
		elseif not var_98_3[iter_98_7] then
			table.insert(var_98_1, Drop.Create(var_98_0.drop_client_pay[iter_98_6]))
		end
	end

	return PlayerConst.MergePassItemDrop(var_98_1)
end

function var_0_0.GetCrusingInfo(arg_99_0)
	assert(arg_99_0:getConfig("type") == ActivityConst.ACTIVITY_TYPE_PT_CRUSING, "type error")

	local var_99_0 = pg.battlepass_event_pt[arg_99_0.id]
	local var_99_1 = var_99_0.pt
	local var_99_2 = {}
	local var_99_3 = {}

	for iter_99_0, iter_99_1 in ipairs(var_99_0.key_point_display) do
		var_99_3[iter_99_1] = true
	end

	for iter_99_2, iter_99_3 in ipairs(var_99_0.target) do
		table.insert(var_99_2, {
			id = iter_99_2,
			pt = iter_99_3,
			award = var_99_0.drop_client[iter_99_2],
			award_pay = var_99_0.drop_client_pay[iter_99_2],
			isImportent = var_99_3[iter_99_2]
		})
	end

	local var_99_4 = arg_99_0.data1
	local var_99_5 = arg_99_0.data2 == 1
	local var_99_6 = {}

	for iter_99_4, iter_99_5 in ipairs(arg_99_0.data1_list) do
		var_99_6[iter_99_5] = true
	end

	local var_99_7 = {}

	for iter_99_6, iter_99_7 in ipairs(arg_99_0.data2_list) do
		var_99_7[iter_99_7] = true
	end

	local var_99_8 = 0

	for iter_99_8, iter_99_9 in ipairs(var_99_2) do
		if var_99_4 < iter_99_9.pt then
			break
		else
			var_99_8 = iter_99_8
		end
	end

	return {
		ptId = var_99_1,
		awardList = var_99_2,
		pt = var_99_4,
		isPay = var_99_5,
		awardDic = var_99_6,
		awardPayDic = var_99_7,
		phase = var_99_8
	}
end

function var_0_0.IsActivityReady(arg_100_0)
	return arg_100_0 and not arg_100_0:isEnd() and arg_100_0:readyToAchieve()
end

function var_0_0.GetEndTimeStrByConfig(arg_101_0)
	local var_101_0 = arg_101_0:getConfig("time")

	if type(var_101_0) == "table" then
		local var_101_1 = var_101_0[3]
		local var_101_2 = var_101_1[1][2]
		local var_101_3 = var_101_1[1][3]

		return var_101_2 .. "." .. var_101_3
	else
		return ""
	end
end

return var_0_0
