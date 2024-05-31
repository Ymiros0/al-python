﻿local var_0_0 = class("ChapterProxy", import(".NetProxy"))

var_0_0.CHAPTER_UPDATED = "ChapterProxy:CHAPTER_UPDATED"
var_0_0.CHAPTER_TIMESUP = "ChapterProxy:CHAPTER_TIMESUP"
var_0_0.CHAPTER_CELL_UPDATED = "ChapterProxy:CHAPTER_CELL_UPDATED"
var_0_0.CHAPTER_AUTO_FIGHT_FLAG_UPDATED = "CHAPTERPROXY:CHAPTER_AUTO_FIGHT_FLAG_UPDATED"
var_0_0.CHAPTER_SKIP_PRECOMBAT_UPDATED = "CHAPTERPROXY:CHAPTER_SKIP_PRECOMBAT_UPDATED"
var_0_0.CHAPTER_REMASTER_INFO_UPDATED = "CHAPTERPROXY:CHAPTER_REMASTER_INFO_UPDATED"
var_0_0.LAST_MAP_FOR_ACTIVITY = "last_map_for_activity"
var_0_0.LAST_MAP = "last_map"

function var_0_0.register(arg_1_0)
	arg_1_0:on(13001, function(arg_2_0)
		arg_1_0.mapEliteFleetCache = {}
		arg_1_0.mapEliteCommanderCache = {}
		arg_1_0.mapSupportFleetCache = {}

		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.fleet_list) do
			var_2_0[iter_2_1.map_id] = var_2_0[iter_2_1.map_id] or {}

			table.insert(var_2_0[iter_2_1.map_id], iter_2_1)
		end

		for iter_2_2, iter_2_3 in pairs(var_2_0) do
			arg_1_0.mapEliteFleetCache[iter_2_2], arg_1_0.mapEliteCommanderCache[iter_2_2], arg_1_0.mapSupportFleetCache[iter_2_2] = Chapter.BuildEliteFleetList(iter_2_3)
		end

		for iter_2_4, iter_2_5 in ipairs(arg_2_0.chapter_list) do
			if not pg.chapter_template[iter_2_5.id] then
				errorMsg("chapter_template not exist: " .. iter_2_5.id)
			else
				local var_2_1 = Chapter.New(iter_2_5)
				local var_2_2 = var_2_1:getConfig("formation")

				var_2_1:setEliteFleetList(Clone(arg_1_0.mapEliteFleetCache[var_2_2]) or {
					{},
					{},
					{}
				})
				var_2_1:setEliteCommanders(Clone(arg_1_0.mapEliteCommanderCache[var_2_2]) or {
					{},
					{},
					{}
				})
				var_2_1:setSupportFleetList(Clone(arg_1_0.mapSupportFleetCache[var_2_2]) or {
					{}
				})
				arg_1_0:updateChapter(var_2_1)
			end
		end

		if arg_2_0.current_chapter then
			local var_2_3 = arg_2_0.current_chapter.id

			if var_2_3 > 0 then
				local var_2_4 = arg_1_0:getChapterById(var_2_3, true)

				var_2_4:update(arg_2_0.current_chapter)
				arg_1_0:updateChapter(var_2_4)
			end
		end

		arg_1_0.repairTimes = arg_2_0.daily_repair_count

		if arg_2_0.react_chapter then
			arg_1_0.remasterTickets = arg_2_0.react_chapter.count
			arg_1_0.remasterDailyCount = arg_2_0.react_chapter.daily_count
			arg_1_0.remasterTip = not (arg_1_0.remasterDailyCount > 0)
		end

		Map.lastMap = arg_1_0:getLastMap(var_0_0.LAST_MAP)
		Map.lastMapForActivity = arg_1_0:getLastMap(var_0_0.LAST_MAP_FOR_ACTIVITY)

		pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inChapter")
		pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inElite")
		pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inSupport")
	end)

	arg_1_0.timers = {}
	arg_1_0.escortChallengeTimes = 0
	arg_1_0.chaptersExtend = {}
	arg_1_0.chapterStoryGroups = {}
	arg_1_0.continuousData = {}

	arg_1_0:buildMaps()
	arg_1_0:buildRemasterInfo()
end

function var_0_0.OnBattleFinished(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = arg_3_0:getActiveChapter()

	if var_3_0 then
		local var_3_1 = 0

		local function var_3_2()
			local var_4_0 = getProxy(ContextProxy)

			if not var_4_0 then
				return
			end

			if var_4_0:getCurrentContext().mediator == LevelMediator2 then
				var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyAttachment, ChapterConst.DirtyStrategy)

				arg_3_0:SetChapterAutoFlag(var_3_0.id, false)

				return
			end

			local var_4_1 = var_4_0:getContextByMediator(LevelMediator2)

			if not var_4_1 then
				return
			end

			var_4_1.data.StopAutoFightFlag = true
		end

		if _.any(arg_3_1.ai_list, function(arg_5_0)
			return arg_5_0.item_type == ChapterConst.AttachOni
		end) then
			var_3_0:onOniEnter()
			var_3_2()
		end

		if _.any(arg_3_1.map_update, function(arg_6_0)
			return arg_6_0.item_type == ChapterConst.AttachBomb_Enemy
		end) then
			var_3_0:onBombEnemyEnter()
			var_3_2()
		end

		if #arg_3_1.map_update > 0 then
			_.each(arg_3_1.map_update, function(arg_7_0)
				if arg_7_0.item_type == ChapterConst.AttachStory and arg_7_0.item_data == ChapterConst.StoryTrigger then
					local var_7_0 = ChapterCell.Line2Name(arg_7_0.pos.row, arg_7_0.pos.column)
					local var_7_1 = var_3_0:GetChapterCellAttachemnts()
					local var_7_2 = var_7_1[var_7_0]

					if var_7_2 then
						if var_7_2.flag == ChapterConst.CellFlagTriggerActive and arg_7_0.item_flag == ChapterConst.CellFlagTriggerDisabled then
							local var_7_3 = pg.map_event_template[var_7_2.attachmentId].gametip

							if var_7_3 ~= "" then
								pg.TipsMgr.GetInstance():ShowTips(i18n(var_7_3))
							end
						end

						var_7_2.attachment = arg_7_0.item_type
						var_7_2.attachmentId = arg_7_0.item_id
						var_7_2.flag = arg_7_0.item_flag
						var_7_2.data = arg_7_0.item_data
					else
						var_7_1[var_7_0] = ChapterCell.New(arg_7_0)
					end
				elseif arg_7_0.item_type ~= ChapterConst.AttachNone and arg_7_0.item_type ~= ChapterConst.AttachBorn and arg_7_0.item_type ~= ChapterConst.AttachBorn_Sub and arg_7_0.item_type ~= ChapterConst.AttachOni_Target and arg_7_0.item_type ~= ChapterConst.AttachOni then
					local var_7_4 = ChapterCell.New(arg_7_0)

					var_3_0:mergeChapterCell(var_7_4)
				end
			end)

			var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyAttachment, ChapterConst.DirtyAutoAction)
		end

		if #arg_3_1.ai_list > 0 then
			_.each(arg_3_1.ai_list, function(arg_8_0)
				local var_8_0 = ChapterChampionPackage.New(arg_8_0)

				var_3_0:mergeChampion(var_8_0)
			end)

			var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyChampion, ChapterConst.DirtyAutoAction)
		end

		if #arg_3_1.add_flag_list > 0 or #arg_3_1.del_flag_list > 0 then
			var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyFleet, ChapterConst.DirtyStrategy, ChapterConst.DirtyCellFlag, ChapterConst.DirtyFloatItems, ChapterConst.DirtyAttachment)

			arg_3_0:updateExtraFlag(var_3_0, arg_3_1.add_flag_list, arg_3_1.del_flag_list)
		end

		if #arg_3_1.buff_list > 0 then
			var_3_0:UpdateBuffList(arg_3_1.buff_list)
		end

		if #arg_3_1.cell_flag_list > 0 then
			_.each(arg_3_1.cell_flag_list, function(arg_9_0)
				local var_9_0 = var_3_0:getChapterCell(arg_9_0.pos.row, arg_9_0.pos.column)

				if var_9_0 then
					var_9_0:updateFlagList(arg_9_0)
				else
					var_9_0 = ChapterCell.New(arg_9_0)
				end

				var_3_0:updateChapterCell(var_9_0)
			end)

			var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyCellFlag)
		end

		arg_3_0:updateChapter(var_3_0, var_3_1)

		if arg_3_2 then
			arg_3_0:sendNotification(GAME.CHAPTER_OP_DONE, {
				type = ChapterConst.OpSkipBattle
			})
		end
	end
end

function var_0_0.setEliteCache(arg_10_0, arg_10_1)
	arg_10_0.mapEliteFleetCache = {}
	arg_10_0.mapEliteCommanderCache = {}
	arg_10_0.mapSupportFleetCache = {}

	local var_10_0 = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_1) do
		var_10_0[iter_10_1.map_id] = var_10_0[iter_10_1.map_id] or {}

		table.insert(var_10_0[iter_10_1.map_id], iter_10_1)
	end

	for iter_10_2, iter_10_3 in pairs(var_10_0) do
		arg_10_0.mapEliteFleetCache[iter_10_2], arg_10_0.mapEliteCommanderCache[iter_10_2], arg_10_0.mapSupportFleetCache[iter_10_2] = Chapter.BuildEliteFleetList(iter_10_3)
	end

	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inElite")
	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inSupport")

	for iter_10_4, iter_10_5 in pairs(arg_10_0.data) do
		local var_10_1 = iter_10_5:getConfig("formation")

		iter_10_5:setEliteFleetList(Clone(arg_10_0.mapEliteFleetCache[var_10_1]) or {
			{},
			{},
			{}
		})
		iter_10_5:setEliteCommanders(Clone(arg_10_0.mapEliteCommanderCache[var_10_1]) or {
			{},
			{},
			{}
		})
		iter_10_5:setSupportFleetList(Clone(arg_10_0.mapSupportFleetCache[var_10_1]) or {
			{},
			{},
			{}
		})
		arg_10_0:updateChapter(iter_10_5)
	end
end

function var_0_0.buildMaps(arg_11_0)
	arg_11_0:initChapters()
	arg_11_0:buildBaseMaps()
	arg_11_0:buildRemasterMaps()
end

function var_0_0.initChapters(arg_12_0)
	var_0_0.MapToChapters = table.shallowCopy(pg.chapter_template.get_id_list_by_map)

	for iter_12_0, iter_12_1 in pairs(pg.story_group.get_id_list_by_map) do
		var_0_0.MapToChapters[iter_12_0] = var_0_0.MapToChapters[iter_12_0] or {}
		var_0_0.MapToChapters[iter_12_0] = table.mergeArray(var_0_0.MapToChapters[iter_12_0], iter_12_1)
	end

	var_0_0.FormationToChapters = pg.chapter_template.get_id_list_by_formation
end

function var_0_0.buildBaseMaps(arg_13_0)
	var_0_0.ActToMaps = {}
	var_0_0.TypeToMaps = {}

	local var_13_0 = {}

	for iter_13_0, iter_13_1 in ipairs(pg.expedition_data_by_map.all) do
		local var_13_1 = Map.New({
			id = iter_13_1,
			chapterIds = var_0_0.MapToChapters[iter_13_1]
		})

		var_13_0[iter_13_1] = var_13_1

		local var_13_2 = var_13_1:getConfig("on_activity")

		if var_13_2 ~= 0 then
			var_0_0.ActToMaps[var_13_2] = var_0_0.ActToMaps[var_13_2] or {}

			table.insert(var_0_0.ActToMaps[var_13_2], var_13_1.id)
		end

		local var_13_3 = var_13_1:getMapType()

		var_0_0.TypeToMaps[var_13_3] = var_0_0.TypeToMaps[var_13_3] or {}

		table.insert(var_0_0.TypeToMaps[var_13_3], var_13_1.id)
	end

	arg_13_0.baseMaps = var_13_0
end

function var_0_0.buildRemasterMaps(arg_14_0)
	var_0_0.RemasterToMaps = {}

	local var_14_0 = {}

	_.each(pg.re_map_template.all, function(arg_15_0)
		local var_15_0 = pg.re_map_template[arg_15_0]

		_.each(var_15_0.config_data, function(arg_16_0)
			local var_16_0 = arg_14_0.baseMaps[pg.chapter_template[arg_16_0].map]

			assert(not var_14_0[var_16_0.id] or var_14_0[var_16_0.id] == arg_15_0, "remaster chapter error:" .. arg_16_0)

			if not var_14_0[var_16_0.id] then
				var_14_0[var_16_0.id] = arg_15_0

				var_16_0:setRemaster(arg_15_0)

				var_0_0.RemasterToMaps[arg_15_0] = var_0_0.RemasterToMaps[arg_15_0] or {}

				table.insert(var_0_0.RemasterToMaps[arg_15_0], var_16_0.id)
			end
		end)
	end)
end

function var_0_0.IsChapterInRemaster(arg_17_0, arg_17_1)
	return _.detect(pg.re_map_template.all, function(arg_18_0)
		local var_18_0 = pg.re_map_template[arg_18_0]

		return _.any(var_18_0.config_data, function(arg_19_0)
			return arg_19_0 == arg_17_1
		end)
	end)
end

function var_0_0.getMaxEscortChallengeTimes(arg_20_0)
	return getProxy(ActivityProxy):getActivityParameter("escort_daily_count") or 0
end

function var_0_0.getEscortChapterIds(arg_21_0)
	return getProxy(ActivityProxy):getActivityParameter("escort_exp_id") or {}
end

function var_0_0.resetEscortChallengeTimes(arg_22_0)
	arg_22_0.escortChallengeTimes = 0
end

function var_0_0.addChapterListener(arg_23_0, arg_23_1)
	if not arg_23_1.dueTime or not arg_23_0.timers then
		return
	end

	if arg_23_0.timers[arg_23_1.id] then
		arg_23_0.timers[arg_23_1.id]:Stop()

		arg_23_0.timers[arg_23_1.id] = nil
	end

	local var_23_0 = arg_23_1.dueTime - pg.TimeMgr.GetInstance():GetServerTime()

	local function var_23_1()
		arg_23_0.data[arg_23_1.id].dueTime = nil

		arg_23_0.data[arg_23_1.id]:display("times'up")
		arg_23_0:sendNotification(var_0_0.CHAPTER_UPDATED, {
			dirty = 0,
			chapter = arg_23_0.data[arg_23_1.id]:clone()
		})
		arg_23_0:sendNotification(var_0_0.CHAPTER_TIMESUP)
	end

	if var_23_0 > 0 then
		arg_23_0.timers[arg_23_1.id] = Timer.New(function()
			var_23_1()
			arg_23_0.timers[arg_23_1.id]:Stop()

			arg_23_0.timers[arg_23_1.id] = nil
		end, var_23_0, 1)

		arg_23_0.timers[arg_23_1.id]:Start()
	else
		var_23_1()
	end
end

function var_0_0.removeChapterListener(arg_26_0, arg_26_1)
	if arg_26_0.timers[arg_26_1] then
		arg_26_0.timers[arg_26_1]:Stop()

		arg_26_0.timers[arg_26_1] = nil
	end
end

function var_0_0.remove(arg_27_0)
	for iter_27_0, iter_27_1 in pairs(arg_27_0.timers) do
		iter_27_1:Stop()
	end

	arg_27_0.timers = nil
end

function var_0_0.GetRawChapterById(arg_28_0, arg_28_1)
	return arg_28_0.data[arg_28_1]
end

function var_0_0.getChapterById(arg_29_0, arg_29_1, arg_29_2)
	local var_29_0 = arg_29_0.data[arg_29_1]

	if not var_29_0 then
		assert(pg.chapter_template[arg_29_1], "Not Exist Chapter ID: " .. (arg_29_1 or "NIL"))

		var_29_0 = Chapter.New({
			id = arg_29_1
		})

		local var_29_1 = var_29_0:getConfig("formation")

		if var_29_0:getConfig("type") == Chapter.CustomFleet then
			var_29_0:setEliteFleetList(Clone(arg_29_0.mapEliteFleetCache[var_29_1]) or {
				{},
				{},
				{}
			})
			var_29_0:setEliteCommanders(Clone(arg_29_0.mapEliteCommanderCache[var_29_1]) or {
				{},
				{},
				{}
			})
		elseif var_29_0:getConfig("type") == Chapter.SelectFleet then
			var_29_0:setSupportFleetList(Clone(arg_29_0.mapSupportFleetCache[var_29_1]) or {
				{},
				{},
				{}
			})
		end

		arg_29_0.data[arg_29_1] = var_29_0
	end

	return arg_29_2 and var_29_0 or var_29_0:clone()
end

function var_0_0.GetChapterItemById(arg_30_0, arg_30_1)
	if Chapter:bindConfigTable()[arg_30_1] then
		return arg_30_0:getChapterById(arg_30_1, true)
	elseif ChapterStoryGroup:bindConfigTable()[arg_30_1] then
		local var_30_0 = arg_30_0.chapterStoryGroups[arg_30_1]

		if not var_30_0 then
			var_30_0 = ChapterStoryGroup.New({
				configId = arg_30_1
			})
			arg_30_0.chapterStoryGroups[arg_30_1] = var_30_0
		end

		return var_30_0
	end
end

function var_0_0.updateChapter(arg_31_0, arg_31_1, arg_31_2)
	assert(isa(arg_31_1, Chapter), "should be an instance of Chapter")

	local var_31_0 = arg_31_0.data[arg_31_1.id]
	local var_31_1 = arg_31_1

	arg_31_0.data[arg_31_1.id] = var_31_1

	if var_31_0 then
		arg_31_0:removeChapterListener(var_31_0.id)
	end

	arg_31_0:addChapterListener(var_31_1)

	if getProxy(PlayerProxy):getInited() then
		arg_31_0.facade:sendNotification(var_0_0.CHAPTER_UPDATED, {
			chapter = var_31_1:clone(),
			dirty = defaultValue(arg_31_2, 0)
		})
	end

	if var_31_1.active and var_31_1.fleet then
		var_31_1.fleet:clearShipHpChange()
	end

	if tobool(checkExist(var_31_0, {
		"active"
	})) ~= tobool(var_31_1.active) then
		pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inChapter")
	end
end

function var_0_0.getMapById(arg_32_0, arg_32_1)
	return arg_32_0.baseMaps[arg_32_1]
end

function var_0_0.getNormalMaps(arg_33_0)
	local var_33_0 = {}

	for iter_33_0, iter_33_1 in ipairs(arg_33_0.baseMaps) do
		table.insert(var_33_0, iter_33_1)
	end

	return var_33_0
end

function var_0_0.getMapsByType(arg_34_0, arg_34_1)
	if var_0_0.TypeToMaps[arg_34_1] then
		return _.map(var_0_0.TypeToMaps[arg_34_1], function(arg_35_0)
			return arg_34_0:getMapById(arg_35_0)
		end)
	else
		return {}
	end
end

function var_0_0.getMapsByActId(arg_36_0, arg_36_1)
	if var_0_0.ActToMaps[arg_36_1] then
		return underscore.map(var_0_0.ActToMaps[arg_36_1], function(arg_37_0)
			return arg_36_0:getMapById(arg_37_0)
		end)
	else
		return {}
	end
end

function var_0_0.getRemasterMaps(arg_38_0, arg_38_1)
	if var_0_0.RemasterToMaps[arg_38_1] then
		return underscore.map(var_0_0.RemasterToMaps[arg_38_1], function(arg_39_0)
			return arg_38_0:getMapById(arg_39_0)
		end)
	else
		return {}
	end
end

function var_0_0.getMapsByActivities(arg_40_0)
	local var_40_0 = {}
	local var_40_1 = getProxy(ActivityProxy):getActivitiesByType(ActivityConst.ACTIVITY_TYPE_ZPROJECT)

	underscore.each(var_40_1, function(arg_41_0)
		if not arg_41_0:isEnd() then
			var_40_0 = table.mergeArray(var_40_0, arg_40_0:getMapsByActId(arg_41_0.id))
		end
	end)

	return var_40_0
end

function var_0_0.getLastUnlockMap(arg_42_0)
	local var_42_0

	for iter_42_0, iter_42_1 in ipairs(arg_42_0:getNormalMaps()) do
		if not iter_42_1:isUnlock() then
			break
		end

		var_42_0 = iter_42_1
	end

	return var_42_0
end

function var_0_0.updateExtraFlag(arg_43_0, arg_43_1, arg_43_2, arg_43_3, arg_43_4)
	local var_43_0 = arg_43_1:updateExtraFlags(arg_43_2, arg_43_3)

	if not arg_43_4 and not var_43_0 then
		return
	end

	local var_43_1 = {}

	for iter_43_0, iter_43_1 in ipairs(arg_43_2) do
		table.insert(var_43_1, iter_43_1)
	end

	arg_43_0:SetExtendChapterData(arg_43_1.id, "extraFlagUpdate", var_43_1)

	return true
end

function var_0_0.extraFlagUpdated(arg_44_0, arg_44_1)
	arg_44_0:RemoveExtendChapterData(arg_44_1, "extraFlagUpdate")
end

function var_0_0.getUpdatedExtraFlags(arg_45_0, arg_45_1)
	return arg_45_0:GetExtendChapterData(arg_45_1, "extraFlagUpdate")
end

function var_0_0.SetExtendChapterData(arg_46_0, arg_46_1, arg_46_2, arg_46_3)
	assert(arg_46_1, "Missing Chapter ID")

	arg_46_0.chaptersExtend[arg_46_1] = arg_46_0.chaptersExtend[arg_46_1] or {}
	arg_46_0.chaptersExtend[arg_46_1][arg_46_2] = arg_46_3
end

function var_0_0.AddExtendChapterDataArray(arg_47_0, arg_47_1, arg_47_2, arg_47_3, arg_47_4)
	assert(arg_47_1, "Missing Chapter ID")

	arg_47_0.chaptersExtend[arg_47_1] = arg_47_0.chaptersExtend[arg_47_1] or {}

	if type(arg_47_0.chaptersExtend[arg_47_1][arg_47_2]) ~= "table" then
		assert(arg_47_0.chaptersExtend[arg_47_1][arg_47_2] == nil, "Changing NonEmpty ExtendData " .. arg_47_2 .. " to Table ID: " .. arg_47_1)

		arg_47_0.chaptersExtend[arg_47_1][arg_47_2] = {}
	end

	arg_47_4 = arg_47_4 or #arg_47_0.chaptersExtend[arg_47_1][arg_47_2] + 1
	arg_47_0.chaptersExtend[arg_47_1][arg_47_2][arg_47_4] = arg_47_3
end

function var_0_0.AddExtendChapterDataTable(arg_48_0, arg_48_1, arg_48_2, arg_48_3, arg_48_4)
	assert(arg_48_1, "Missing Chapter ID")

	arg_48_0.chaptersExtend[arg_48_1] = arg_48_0.chaptersExtend[arg_48_1] or {}

	if type(arg_48_0.chaptersExtend[arg_48_1][arg_48_2]) ~= "table" then
		assert(arg_48_0.chaptersExtend[arg_48_1][arg_48_2] == nil, "Changing NonEmpty ExtendData " .. arg_48_2 .. " to Table ID: " .. arg_48_1)

		arg_48_0.chaptersExtend[arg_48_1][arg_48_2] = {}
	end

	assert(arg_48_3, "Missing Index on Set HashData")

	arg_48_0.chaptersExtend[arg_48_1][arg_48_2][arg_48_3] = arg_48_4
end

function var_0_0.GetExtendChapterData(arg_49_0, arg_49_1, arg_49_2)
	assert(arg_49_1, "Missing Chapter ID")
	assert(arg_49_2, "Requesting Empty key")

	if not arg_49_2 or not arg_49_0.chaptersExtend[arg_49_1] then
		return
	end

	return arg_49_0.chaptersExtend[arg_49_1][arg_49_2]
end

function var_0_0.RemoveExtendChapterData(arg_50_0, arg_50_1, arg_50_2)
	assert(arg_50_1, "Missing Chapter ID")

	if not arg_50_2 or not arg_50_0.chaptersExtend[arg_50_1] then
		return
	end

	arg_50_0.chaptersExtend[arg_50_1][arg_50_2] = nil

	if next(arg_50_0.chaptersExtend[arg_50_1]) then
		return
	end

	arg_50_0:RemoveExtendChapter(arg_50_1)
end

function var_0_0.GetExtendChapter(arg_51_0, arg_51_1)
	assert(arg_51_1, "Missing Chapter ID")

	return arg_51_0.chaptersExtend[arg_51_1]
end

function var_0_0.RemoveExtendChapter(arg_52_0, arg_52_1)
	assert(arg_52_1, "Missing Chapter ID")

	if not arg_52_0.chaptersExtend[arg_52_1] then
		return
	end

	arg_52_0.chaptersExtend[arg_52_1] = nil
end

function var_0_0.duplicateEliteFleet(arg_53_0, arg_53_1)
	if arg_53_1:getConfig("type") ~= Chapter.CustomFleet then
		return
	end

	local var_53_0 = arg_53_1:getEliteFleetList()
	local var_53_1 = arg_53_1:getEliteFleetCommanders()
	local var_53_2 = arg_53_1:getConfig("formation")

	arg_53_0.mapEliteFleetCache[var_53_2] = Clone(var_53_0)
	arg_53_0.mapEliteCommanderCache[var_53_2] = Clone(var_53_1)

	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inElite")

	for iter_53_0, iter_53_1 in ipairs(var_0_0.FormationToChapters[var_53_2]) do
		local var_53_3 = arg_53_0:getChapterById(iter_53_1, true)

		if var_53_3.configId ~= arg_53_1.configId then
			var_53_3:setEliteFleetList(Clone(var_53_0))
			var_53_3:setEliteCommanders(Clone(var_53_1))
			arg_53_0:updateChapter(var_53_3)
		end
	end
end

function var_0_0.duplicateSupportFleet(arg_54_0, arg_54_1)
	local var_54_0 = arg_54_1:getSupportFleet()
	local var_54_1 = arg_54_1:getConfig("formation")

	arg_54_0.mapSupportFleetCache[var_54_1] = {
		Clone(var_54_0)
	}

	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inSupport")

	for iter_54_0, iter_54_1 in ipairs(var_0_0.FormationToChapters[var_54_1]) do
		local var_54_2 = arg_54_0:getChapterById(iter_54_1, true)

		if var_54_2.configId ~= arg_54_1.configId then
			var_54_2:setSupportFleetList({
				Clone(var_54_0)
			})
			arg_54_0:updateChapter(var_54_2)
		end
	end
end

function var_0_0.CheckUnitInSupportFleet(arg_55_0, arg_55_1)
	local var_55_0 = {}
	local var_55_1 = arg_55_1.id

	for iter_55_0, iter_55_1 in pairs(arg_55_0.mapSupportFleetCache) do
		for iter_55_2, iter_55_3 in ipairs(iter_55_1) do
			if table.contains(iter_55_3, var_55_1) then
				var_55_0[iter_55_0] = true

				break
			end
		end
	end

	return next(var_55_0), var_55_0
end

function var_0_0.RemoveUnitFromSupportFleet(arg_56_0, arg_56_1)
	arg_56_0:sendNotification(GAME.REMOVE_ELITE_TARGET_SHIP, {
		shipId = arg_56_1.id,
		callback = next
	})
end

function var_0_0.getActiveChapter(arg_57_0, arg_57_1)
	for iter_57_0, iter_57_1 in pairs(arg_57_0.data) do
		if iter_57_1.active then
			return arg_57_1 and iter_57_1 or iter_57_1:clone()
		end
	end
end

function var_0_0.getLastMapForActivity(arg_58_0)
	local var_58_0
	local var_58_1
	local var_58_2 = arg_58_0:getActiveChapter()

	if var_58_2 then
		local var_58_3 = arg_58_0:getMapById(var_58_2:getConfig("map"))

		if var_58_3:isActivity() and not var_58_3:isRemaster() then
			return var_58_3.id, var_58_2.id
		end
	end

	local var_58_4 = Map.lastMapForActivity and arg_58_0:getMapById(Map.lastMapForActivity)

	if var_58_4 and not var_58_4:isRemaster() and var_58_4:isUnlock() then
		return Map.lastMapForActivity
	end

	if Map.lastMapForActivity then
		Map.lastMapForActivity = nil

		arg_58_0:recordLastMap(var_0_0.LAST_MAP_FOR_ACTIVITY, 0)
	end

	local var_58_5 = arg_58_0:getMapsByActivities()

	table.sort(var_58_5, function(arg_59_0, arg_59_1)
		return arg_59_0.id > arg_59_1.id
	end)

	local var_58_6 = {}

	if _.all(var_58_5, function(arg_60_0)
		return arg_60_0:getConfig("type") == Map.EVENT
	end) then
		var_58_6 = var_58_5
	else
		for iter_58_0, iter_58_1 in ipairs({
			Map.ACTIVITY_EASY,
			Map.ACTIVITY_HARD
		}) do
			local var_58_7 = underscore.filter(var_58_5, function(arg_61_0)
				return arg_61_0:getMapType() == iter_58_1
			end)

			if #var_58_7 > 0 then
				var_58_6 = var_58_7

				if underscore.any(var_58_6, function(arg_62_0)
					return not arg_62_0:isClearForActivity()
				end) then
					break
				end
			end
		end
	end

	for iter_58_2 = #var_58_6, 1, -1 do
		local var_58_8 = var_58_6[iter_58_2]

		if var_58_8:isUnlock() then
			return var_58_8.id
		end
	end

	if #var_58_5 > 0 then
		return var_58_5[1].id
	end
end

function var_0_0.updateActiveChapterShips(arg_63_0)
	local var_63_0 = arg_63_0:getActiveChapter(true)

	if var_63_0 then
		_.each(var_63_0.fleets, function(arg_64_0)
			arg_64_0:flushShips()
		end)
		arg_63_0:updateChapter(var_63_0, ChapterConst.DirtyFleet)
	end
end

function var_0_0.resetRepairTimes(arg_65_0)
	arg_65_0.repairTimes = 0
end

function var_0_0.getUseableEliteMap(arg_66_0)
	local var_66_0 = {}

	for iter_66_0, iter_66_1 in ipairs(arg_66_0:getMapsByType(Map.ELITE)) do
		if iter_66_1:isEliteEnabled() then
			var_66_0[#var_66_0 + 1] = iter_66_1
		end
	end

	return var_66_0
end

function var_0_0.getUseableMaxEliteMap(arg_67_0)
	local var_67_0 = arg_67_0:getUseableEliteMap()

	if #var_67_0 == 0 then
		return false
	else
		local var_67_1

		for iter_67_0, iter_67_1 in ipairs(var_67_0) do
			if not var_67_1 or var_67_1.id < iter_67_1.id then
				var_67_1 = iter_67_1
			end
		end

		return var_67_1
	end
end

function var_0_0.getHigestClearChapterAndMap(arg_68_0)
	local var_68_0 = arg_68_0.baseMaps[1]

	for iter_68_0, iter_68_1 in ipairs(arg_68_0:getNormalMaps()) do
		if not iter_68_1:isAnyChapterClear() then
			break
		end

		var_68_0 = iter_68_1
	end

	local var_68_1 = arg_68_0:getChapterById(var_68_0.chapterIds[1])

	for iter_68_2, iter_68_3 in ipairs(var_68_0:getChapters()) do
		if not iter_68_3:isClear() then
			break
		end

		var_68_1 = iter_68_3
	end

	return var_68_1, var_68_0
end

function var_0_0.SortRecommendLimitation(arg_69_0)
	table.sort(arg_69_0, CompareFuncs({
		function(arg_70_0)
			if type(arg_70_0) == "number" then
				if arg_70_0 == 0 then
					return 1
				else
					return -arg_70_0
				end
			elseif type(arg_70_0) == "string" then
				return 0
			else
				assert(false)
			end
		end
	}))
end

function var_0_0.eliteFleetRecommend(arg_71_0, arg_71_1, arg_71_2)
	local var_71_0 = arg_71_1:getEliteFleetList()[arg_71_2]
	local var_71_1 = arg_71_1:getConfig("limitation")[arg_71_2]
	local var_71_2 = var_71_1 and Clone(var_71_1[1]) or {
		0,
		0,
		0
	}
	local var_71_3 = var_71_1 and Clone(var_71_1[2]) or {
		0,
		0,
		0
	}
	local var_71_4 = {
		0,
		0,
		0
	}

	var_0_0.SortRecommendLimitation(var_71_2)
	var_0_0.SortRecommendLimitation(var_71_3)
	var_0_0.SortRecommendLimitation(var_71_4)

	local var_71_5 = {}

	for iter_71_0, iter_71_1 in ipairs(arg_71_1:getEliteFleetList()) do
		for iter_71_2, iter_71_3 in ipairs(iter_71_1) do
			var_71_5[#var_71_5 + 1] = iter_71_3
		end
	end

	local var_71_6

	if arg_71_2 > 2 then
		var_71_6 = {
			[TeamType.Submarine] = var_71_4
		}
	else
		var_71_6 = {
			[TeamType.Main] = var_71_2,
			[TeamType.Vanguard] = var_71_3
		}
	end

	local var_71_7 = arg_71_0:FleetRecommend(var_71_0, var_71_5, var_71_6, function(arg_72_0)
		return ShipStatus.ShipStatusCheck("inElite", arg_72_0, nil, {
			inElite = arg_71_1:getConfig("formation")
		})
	end)

	table.clean(var_71_0)
	table.insertto(var_71_0, var_71_7)
end

function var_0_0.SupportFleetRecommend(arg_73_0, arg_73_1, arg_73_2)
	local var_73_0 = arg_73_1:getSupportFleet()
	local var_73_1 = {
		[TeamType.Main] = {
			"hang",
			"hang",
			"hang"
		}
	}
	local var_73_2 = table.shallowCopy(var_73_0)
	local var_73_3 = arg_73_0:FleetRecommend(var_73_0, var_73_2, var_73_1, function(arg_74_0)
		return ShipStatus.ShipStatusCheck("inSupport", arg_74_0, nil, {
			inSupport = arg_73_1:getConfig("formation")
		})
	end)

	table.clean(var_73_0)
	table.insertto(var_73_0, var_73_3)
end

function var_0_0.FleetRecommend(arg_75_0, arg_75_1, arg_75_2, arg_75_3, arg_75_4)
	arg_75_1 = table.shallowCopy(arg_75_1)
	arg_75_2 = table.shallowCopy(arg_75_2)

	local var_75_0 = getProxy(BayProxy)
	local var_75_1 = getProxy(BayProxy):getRawData()

	for iter_75_0, iter_75_1 in ipairs(arg_75_1) do
		local var_75_2 = var_75_1[iter_75_1]:getShipType()
		local var_75_3 = TeamType.GetTeamFromShipType(var_75_2)
		local var_75_4 = 0
		local var_75_5 = arg_75_3[var_75_3]

		for iter_75_2, iter_75_3 in ipairs(var_75_5) do
			if ShipType.ContainInLimitBundle(iter_75_3, var_75_2) then
				var_75_4 = iter_75_3

				break
			end
		end

		for iter_75_4, iter_75_5 in ipairs(var_75_5) do
			if iter_75_5 == var_75_4 then
				table.remove(var_75_5, iter_75_4)

				break
			end
		end
	end

	local function var_75_6(arg_76_0, arg_76_1)
		local var_76_0 = underscore.filter(TeamType.GetShipTypeListFromTeam(arg_76_1), function(arg_77_0)
			return ShipType.ContainInLimitBundle(arg_76_0, arg_77_0)
		end)
		local var_76_1 = var_75_0:GetRecommendShip(var_76_0, arg_75_2, arg_75_4)

		if var_76_1 then
			local var_76_2 = var_76_1.id

			arg_75_2[#arg_75_2 + 1] = var_76_2
			arg_75_1[#arg_75_1 + 1] = var_76_2
		end
	end

	for iter_75_6, iter_75_7 in pairs(arg_75_3) do
		for iter_75_8, iter_75_9 in ipairs(iter_75_7) do
			var_75_6(iter_75_9, iter_75_6)
		end
	end

	return arg_75_1
end

function var_0_0.isClear(arg_78_0, arg_78_1)
	local var_78_0 = arg_78_0:GetChapterItemById(arg_78_1)

	if not var_78_0 then
		return false
	end

	return var_78_0:isClear()
end

function var_0_0.getEscortShop(arg_79_0)
	return Clone(arg_79_0.escortShop)
end

function var_0_0.updateEscortShop(arg_80_0, arg_80_1)
	arg_80_0.escortShop = arg_80_1
end

function var_0_0.recordLastMap(arg_81_0, arg_81_1, arg_81_2)
	local var_81_0 = false

	if arg_81_1 == var_0_0.LAST_MAP_FOR_ACTIVITY then
		Map.lastMapForActivity = arg_81_2
		var_81_0 = true
	elseif arg_81_1 == var_0_0.LAST_MAP and arg_81_2 ~= Map.lastMap then
		Map.lastMap = arg_81_2
		var_81_0 = true
	end

	if var_81_0 then
		local var_81_1 = getProxy(PlayerProxy):getRawData()

		PlayerPrefs.SetInt(arg_81_1 .. var_81_1.id, arg_81_2)
		PlayerPrefs.Save()
	end
end

function var_0_0.getLastMap(arg_82_0, arg_82_1)
	local var_82_0 = getProxy(PlayerProxy):getRawData()
	local var_82_1 = PlayerPrefs.GetInt(arg_82_1 .. var_82_0.id)

	if var_82_1 ~= 0 then
		return var_82_1
	end
end

function var_0_0.IsActivitySPChapterActive(arg_83_0)
	local var_83_0 = arg_83_0:getMapsByActivities()
	local var_83_1 = _.select(var_83_0, function(arg_84_0)
		return arg_84_0:getMapType() == Map.ACT_EXTRA
	end)
	local var_83_2 = _.reduce(var_83_1, {}, function(arg_85_0, arg_85_1)
		local var_85_0 = _.select(arg_85_1:getChapters(true), function(arg_86_0)
			return arg_86_0:getPlayType() == ChapterConst.TypeRange
		end)

		return table.mergeArray(arg_85_0, var_85_0)
	end)

	return _.any(var_83_2, function(arg_87_0)
		return arg_87_0:isUnlock() and arg_87_0:isPlayerLVUnlock() and arg_87_0:enoughTimes2Start()
	end)
end

function var_0_0.getSubAidFlag(arg_88_0, arg_88_1)
	local var_88_0 = ys.Battle.BattleConst.SubAidFlag
	local var_88_1 = arg_88_0.fleet
	local var_88_2 = false
	local var_88_3 = _.detect(arg_88_0.fleets, function(arg_89_0)
		return arg_89_0:getFleetType() == FleetType.Submarine and arg_89_0:isValid()
	end)

	if var_88_3 then
		if var_88_3:inHuntingRange(var_88_1.line.row, var_88_1.line.column) then
			var_88_2 = true
		else
			local var_88_4 = var_88_3:getStrategies()
			local var_88_5 = _.detect(var_88_4, function(arg_90_0)
				return arg_90_0.id == ChapterConst.StrategyCallSubOutofRange
			end)

			if var_88_5 and var_88_5.count > 0 then
				var_88_2 = true
			end
		end
	end

	if var_88_2 then
		local var_88_6 = getProxy(PlayerProxy):getRawData()
		local var_88_7, var_88_8 = arg_88_0:getFleetCost(var_88_1, arg_88_1)
		local var_88_9, var_88_10 = arg_88_0:getFleetAmmo(var_88_3)
		local var_88_11 = 0

		for iter_88_0, iter_88_1 in ipairs({
			arg_88_0:getFleetCost(var_88_3, arg_88_1)
		}) do
			var_88_11 = var_88_11 + iter_88_1.oil
		end

		if var_88_10 <= 0 then
			return var_88_0.AMMO_EMPTY
		elseif var_88_11 + var_88_8.oil >= var_88_6.oil then
			return var_88_0.OIL_EMPTY
		else
			return true, var_88_3
		end
	else
		return var_88_0.AID_EMPTY
	end
end

function var_0_0.GetChapterAuraBuffs(arg_91_0)
	local var_91_0 = {}

	for iter_91_0, iter_91_1 in ipairs(arg_91_0.fleets) do
		if iter_91_1:getFleetType() ~= FleetType.Support then
			local var_91_1 = iter_91_1:getMapAura()

			for iter_91_2, iter_91_3 in ipairs(var_91_1) do
				table.insert(var_91_0, iter_91_3)
			end
		end
	end

	return var_91_0
end

function var_0_0.GetChapterAidBuffs(arg_92_0)
	local var_92_0 = {}

	for iter_92_0, iter_92_1 in ipairs(arg_92_0.fleets) do
		if iter_92_1 ~= arg_92_0.fleet and iter_92_1:getFleetType() ~= FleetType.Support then
			local var_92_1 = iter_92_1:getMapAid()

			for iter_92_2, iter_92_3 in pairs(var_92_1) do
				var_92_0[iter_92_2] = iter_92_3
			end
		end
	end

	return var_92_0
end

function var_0_0.RecordComboHistory(arg_93_0, arg_93_1, arg_93_2)
	if arg_93_2 ~= nil then
		arg_93_0:SetExtendChapterData(arg_93_1, "comboHistoryBuffer", arg_93_2)
	else
		arg_93_0:RemoveExtendChapterData(arg_93_1, "comboHistoryBuffer")
	end
end

function var_0_0.GetComboHistory(arg_94_0, arg_94_1)
	return arg_94_0:GetExtendChapterData(arg_94_1, "comboHistoryBuffer")
end

function var_0_0.RecordJustClearChapters(arg_95_0, arg_95_1, arg_95_2)
	if arg_95_2 ~= nil then
		arg_95_0:SetExtendChapterData(arg_95_1, "justClearChapters", arg_95_2)
	else
		arg_95_0:RemoveExtendChapterData(arg_95_1, "justClearChapters")
	end
end

function var_0_0.GetJustClearChapters(arg_96_0, arg_96_1)
	return arg_96_0:GetExtendChapterData(arg_96_1, "justClearChapters")
end

function var_0_0.RecordLastDefeatedEnemy(arg_97_0, arg_97_1, arg_97_2)
	if arg_97_2 ~= nil then
		arg_97_0:SetExtendChapterData(arg_97_1, "defeatedEnemiesBuffer", arg_97_2)
	else
		arg_97_0:RemoveExtendChapterData(arg_97_1, "defeatedEnemiesBuffer")
	end
end

function var_0_0.GetLastDefeatedEnemy(arg_98_0, arg_98_1)
	return arg_98_0:GetExtendChapterData(arg_98_1, "defeatedEnemiesBuffer")
end

function var_0_0.ifShowRemasterTip(arg_99_0)
	return arg_99_0.remasterTip
end

function var_0_0.setRemasterTip(arg_100_0, arg_100_1)
	arg_100_0.remasterTip = arg_100_1
end

function var_0_0.updateRemasterTicketsNum(arg_101_0, arg_101_1)
	arg_101_0.remasterTickets = arg_101_1
end

function var_0_0.resetDailyCount(arg_102_0)
	arg_102_0.remasterDailyCount = 0
end

function var_0_0.updateDailyCount(arg_103_0)
	arg_103_0.remasterDailyCount = arg_103_0.remasterDailyCount + pg.gameset.reactivity_ticket_daily.key_value
end

function var_0_0.GetSkipPrecombat(arg_104_0)
	if arg_104_0.skipPrecombat == nil then
		arg_104_0.skipPrecombat = PlayerPrefs.GetInt("chapter_skip_precombat", 0)
	end

	return arg_104_0.skipPrecombat > 0
end

function var_0_0.UpdateSkipPrecombat(arg_105_0, arg_105_1)
	arg_105_1 = tobool(arg_105_1) and 1 or 0

	if arg_105_1 ~= arg_105_0:GetSkipPrecombat() then
		PlayerPrefs.SetInt("chapter_skip_precombat", arg_105_1)

		arg_105_0.skipPrecombat = arg_105_1

		arg_105_0:sendNotification(var_0_0.CHAPTER_SKIP_PRECOMBAT_UPDATED, arg_105_1)
	end
end

function var_0_0.GetChapterAutoFlag(arg_106_0, arg_106_1)
	return arg_106_0:GetExtendChapterData(arg_106_1, "AutoFightFlag")
end

function var_0_0.SetChapterAutoFlag(arg_107_0, arg_107_1, arg_107_2, arg_107_3)
	arg_107_2 = tobool(arg_107_2)

	if arg_107_2 == (arg_107_0:GetChapterAutoFlag(arg_107_1) == 1) then
		return
	end

	arg_107_0:SetExtendChapterData(arg_107_1, "AutoFightFlag", arg_107_2 and 1 or 0)

	if arg_107_2 then
		arg_107_0:UpdateSkipPrecombat(true)

		if AutoBotCommand.autoBotSatisfied() then
			PlayerPrefs.SetInt("autoBotIsAcitve" .. AutoBotCommand.GetAutoBotMark(), 1)
		end

		getProxy(MetaCharacterProxy):setMetaTacticsInfoOnStart()
		pg.BrightnessMgr.GetInstance():SetScreenNeverSleep(true)

		if not LOCK_BATTERY_SAVEMODE and PlayerPrefs.GetInt(AUTOFIGHT_BATTERY_SAVEMODE, 0) == 1 and pg.BrightnessMgr.GetInstance():IsPermissionGranted() then
			pg.BrightnessMgr.GetInstance():EnterManualMode()

			if PlayerPrefs.GetInt(AUTOFIGHT_DOWN_FRAME, 0) == 1 then
				getProxy(SettingsProxy):RecordFrameRate()

				Application.targetFrameRate = 30
			end
		end
	else
		arg_107_0:StopContinuousOperation(SYSTEM_SCENARIO, arg_107_3)
		pg.BrightnessMgr.GetInstance():SetScreenNeverSleep(false)

		if not LOCK_BATTERY_SAVEMODE then
			pg.BrightnessMgr.GetInstance():ExitManualMode()
			getProxy(SettingsProxy):RestoreFrameRate()
		end
	end

	arg_107_0.facade:sendNotification(var_0_0.CHAPTER_AUTO_FIGHT_FLAG_UPDATED, arg_107_2 and 1 or 0)
	arg_107_0.facade:sendNotification(PlayerResUI.CHANGE_TOUCH_ABLE, not arg_107_2)
end

function var_0_0.StopAutoFight(arg_108_0, arg_108_1)
	local var_108_0 = arg_108_0:getActiveChapter(true)

	if not var_108_0 then
		return
	end

	arg_108_0:SetChapterAutoFlag(var_108_0.id, false, arg_108_1)
end

function var_0_0.FinishAutoFight(arg_109_0, arg_109_1)
	if arg_109_0:GetChapterAutoFlag(arg_109_1) == 1 then
		pg.BrightnessMgr.GetInstance():SetScreenNeverSleep(false)

		if not LOCK_BATTERY_SAVEMODE then
			pg.BrightnessMgr.GetInstance():ExitManualMode()
			getProxy(SettingsProxy):RestoreFrameRate()
		end

		arg_109_0.facade:sendNotification(PlayerResUI.CHANGE_TOUCH_ABLE, true)
	end

	local var_109_0 = arg_109_0:GetExtendChapter(arg_109_1)

	arg_109_0:RemoveExtendChapter(arg_109_1)

	return var_109_0
end

function var_0_0.buildRemasterInfo(arg_110_0)
	arg_110_0.remasterInfo = {}

	for iter_110_0, iter_110_1 in ipairs(pg.re_map_template.all) do
		for iter_110_2, iter_110_3 in ipairs(pg.re_map_template[iter_110_1].drop_gain) do
			if #iter_110_3 > 0 then
				local var_110_0, var_110_1, var_110_2, var_110_3 = unpack(iter_110_3)

				arg_110_0.remasterInfo[var_110_0] = defaultValue(arg_110_0.remasterInfo[var_110_0], {})
				arg_110_0.remasterInfo[var_110_0][iter_110_2] = {
					count = 0,
					receive = false,
					max = var_110_3
				}
			end
		end
	end
end

function var_0_0.checkRemasterInfomation(arg_111_0)
	if not arg_111_0.checkRemaster then
		arg_111_0.checkRemaster = true

		arg_111_0:sendNotification(GAME.CHAPTER_REMASTER_INFO_REQUEST)
	end
end

function var_0_0.addRemasterPassCount(arg_112_0, arg_112_1)
	if not arg_112_0.remasterInfo[arg_112_1] then
		return
	end

	local var_112_0

	for iter_112_0, iter_112_1 in pairs(arg_112_0.remasterInfo[arg_112_1]) do
		if iter_112_1.count < iter_112_1.max then
			iter_112_1.count = iter_112_1.count + 1
			var_112_0 = true
		end
	end

	if var_112_0 then
		arg_112_0:sendNotification(var_0_0.CHAPTER_REMASTER_INFO_UPDATED)
	end
end

function var_0_0.markRemasterPassReceive(arg_113_0, arg_113_1, arg_113_2)
	local var_113_0 = arg_113_0.remasterInfo[arg_113_1][arg_113_2]

	if not arg_113_0.remasterInfo[arg_113_1][arg_113_2] then
		return
	end

	if not var_113_0.receive then
		var_113_0.receive = true

		arg_113_0:sendNotification(var_0_0.CHAPTER_REMASTER_INFO_UPDATED)
	end
end

function var_0_0.anyRemasterAwardCanReceive(arg_114_0)
	for iter_114_0, iter_114_1 in pairs(arg_114_0.remasterInfo) do
		for iter_114_2, iter_114_3 in pairs(iter_114_1) do
			if not iter_114_3.receive and iter_114_3.count >= iter_114_3.max then
				return true
			end
		end
	end

	return false
end

function var_0_0.AddActBossRewards(arg_115_0, arg_115_1)
	arg_115_0.actBossItems = arg_115_0.actBossItems or {}

	table.insertto(arg_115_0.actBossItems, arg_115_1)
end

function var_0_0.PopActBossRewards(arg_116_0)
	local var_116_0 = arg_116_0.actBossItems or {}

	arg_116_0.actBossItems = nil

	return var_116_0
end

function var_0_0.AddBossSingleRewards(arg_117_0, arg_117_1)
	arg_117_0.bossSingleItems = arg_117_0.bossSingleItems or {}

	table.insertto(arg_117_0.bossSingleItems, arg_117_1)
end

function var_0_0.PopBossSingleRewards(arg_118_0)
	local var_118_0 = arg_118_0.bossSingleItems or {}

	arg_118_0.bossSingleItems = nil

	return var_118_0
end

function var_0_0.WriteBackOnExitBattleResult(arg_119_0)
	local var_119_0 = arg_119_0:getActiveChapter()

	if var_119_0 then
		if var_119_0:existOni() then
			var_119_0:clearSubmarineFleet()
			arg_119_0:updateChapter(var_119_0)
		elseif var_119_0:isPlayingWithBombEnemy() then
			var_119_0.fleets = {
				var_119_0.fleet
			}
			var_119_0.findex = 1

			arg_119_0:updateChapter(var_119_0)
		end
	end
end

function var_0_0.GetContinuousData(arg_120_0, arg_120_1)
	return arg_120_0.continuousData[arg_120_1]
end

function var_0_0.InitContinuousTime(arg_121_0, arg_121_1, arg_121_2)
	local var_121_0 = ContinuousOperationRuntimeData.New({
		system = arg_121_1,
		totalBattleTime = arg_121_2,
		battleTime = arg_121_2
	})

	arg_121_0.continuousData[arg_121_1] = var_121_0
end

function var_0_0.StopContinuousOperation(arg_122_0, arg_122_1, arg_122_2)
	local var_122_0 = arg_122_0:GetContinuousData(arg_122_1)

	if not var_122_0 or not var_122_0:IsActive() then
		return
	end

	if arg_122_2 == ChapterConst.AUTOFIGHT_STOP_REASON.MANUAL and arg_122_1 == SYSTEM_SCENARIO then
		pg.TipsMgr.GetInstance():ShowTips(i18n("multiple_sorties_stop"))
	end

	var_122_0:Stop(arg_122_2)
end

function var_0_0.PopContinuousData(arg_123_0, arg_123_1)
	local var_123_0 = arg_123_0.continuousData[arg_123_1]

	arg_123_0.continuousData[arg_123_1] = nil

	return var_123_0
end

function var_0_0.SetLastFleetIndex(arg_124_0, arg_124_1, arg_124_2)
	if arg_124_2 and arg_124_0.lastFleetIndex then
		return
	end

	arg_124_0.lastFleetIndex = arg_124_1
end

function var_0_0.GetLastFleetIndex(arg_125_0)
	return arg_125_0.lastFleetIndex
end

return var_0_0
