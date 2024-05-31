local var_0_0 = class("ChapterProxy", import(".NetProxy"))

var_0_0.CHAPTER_UPDATED = "ChapterProxy.CHAPTER_UPDATED"
var_0_0.CHAPTER_TIMESUP = "ChapterProxy.CHAPTER_TIMESUP"
var_0_0.CHAPTER_CELL_UPDATED = "ChapterProxy.CHAPTER_CELL_UPDATED"
var_0_0.CHAPTER_AUTO_FIGHT_FLAG_UPDATED = "CHAPTERPROXY.CHAPTER_AUTO_FIGHT_FLAG_UPDATED"
var_0_0.CHAPTER_SKIP_PRECOMBAT_UPDATED = "CHAPTERPROXY.CHAPTER_SKIP_PRECOMBAT_UPDATED"
var_0_0.CHAPTER_REMASTER_INFO_UPDATED = "CHAPTERPROXY.CHAPTER_REMASTER_INFO_UPDATED"
var_0_0.LAST_MAP_FOR_ACTIVITY = "last_map_for_activity"
var_0_0.LAST_MAP = "last_map"

def var_0_0.register(arg_1_0):
	arg_1_0.on(13001, function(arg_2_0)
		arg_1_0.mapEliteFleetCache = {}
		arg_1_0.mapEliteCommanderCache = {}
		arg_1_0.mapSupportFleetCache = {}

		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.fleet_list):
			var_2_0[iter_2_1.map_id] = var_2_0[iter_2_1.map_id] or {}

			table.insert(var_2_0[iter_2_1.map_id], iter_2_1)

		for iter_2_2, iter_2_3 in pairs(var_2_0):
			arg_1_0.mapEliteFleetCache[iter_2_2], arg_1_0.mapEliteCommanderCache[iter_2_2], arg_1_0.mapSupportFleetCache[iter_2_2] = Chapter.BuildEliteFleetList(iter_2_3)

		for iter_2_4, iter_2_5 in ipairs(arg_2_0.chapter_list):
			if not pg.chapter_template[iter_2_5.id]:
				errorMsg("chapter_template not exist. " .. iter_2_5.id)
			else
				local var_2_1 = Chapter.New(iter_2_5)
				local var_2_2 = var_2_1.getConfig("formation")

				var_2_1.setEliteFleetList(Clone(arg_1_0.mapEliteFleetCache[var_2_2]) or {
					{},
					{},
					{}
				})
				var_2_1.setEliteCommanders(Clone(arg_1_0.mapEliteCommanderCache[var_2_2]) or {
					{},
					{},
					{}
				})
				var_2_1.setSupportFleetList(Clone(arg_1_0.mapSupportFleetCache[var_2_2]) or {
					{}
				})
				arg_1_0.updateChapter(var_2_1)

		if arg_2_0.current_chapter:
			local var_2_3 = arg_2_0.current_chapter.id

			if var_2_3 > 0:
				local var_2_4 = arg_1_0.getChapterById(var_2_3, True)

				var_2_4.update(arg_2_0.current_chapter)
				arg_1_0.updateChapter(var_2_4)

		arg_1_0.repairTimes = arg_2_0.daily_repair_count

		if arg_2_0.react_chapter:
			arg_1_0.remasterTickets = arg_2_0.react_chapter.count
			arg_1_0.remasterDailyCount = arg_2_0.react_chapter.daily_count
			arg_1_0.remasterTip = not (arg_1_0.remasterDailyCount > 0)

		Map.lastMap = arg_1_0.getLastMap(var_0_0.LAST_MAP)
		Map.lastMapForActivity = arg_1_0.getLastMap(var_0_0.LAST_MAP_FOR_ACTIVITY)

		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inChapter")
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inElite")
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inSupport"))

	arg_1_0.timers = {}
	arg_1_0.escortChallengeTimes = 0
	arg_1_0.chaptersExtend = {}
	arg_1_0.chapterStoryGroups = {}
	arg_1_0.continuousData = {}

	arg_1_0.buildMaps()
	arg_1_0.buildRemasterInfo()

def var_0_0.OnBattleFinished(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = arg_3_0.getActiveChapter()

	if var_3_0:
		local var_3_1 = 0

		local function var_3_2()
			local var_4_0 = getProxy(ContextProxy)

			if not var_4_0:
				return

			if var_4_0.getCurrentContext().mediator == LevelMediator2:
				var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyAttachment, ChapterConst.DirtyStrategy)

				arg_3_0.SetChapterAutoFlag(var_3_0.id, False)

				return

			local var_4_1 = var_4_0.getContextByMediator(LevelMediator2)

			if not var_4_1:
				return

			var_4_1.data.StopAutoFightFlag = True

		if _.any(arg_3_1.ai_list, function(arg_5_0)
			return arg_5_0.item_type == ChapterConst.AttachOni):
			var_3_0.onOniEnter()
			var_3_2()

		if _.any(arg_3_1.map_update, function(arg_6_0)
			return arg_6_0.item_type == ChapterConst.AttachBomb_Enemy):
			var_3_0.onBombEnemyEnter()
			var_3_2()

		if #arg_3_1.map_update > 0:
			_.each(arg_3_1.map_update, function(arg_7_0)
				if arg_7_0.item_type == ChapterConst.AttachStory and arg_7_0.item_data == ChapterConst.StoryTrigger:
					local var_7_0 = ChapterCell.Line2Name(arg_7_0.pos.row, arg_7_0.pos.column)
					local var_7_1 = var_3_0.GetChapterCellAttachemnts()
					local var_7_2 = var_7_1[var_7_0]

					if var_7_2:
						if var_7_2.flag == ChapterConst.CellFlagTriggerActive and arg_7_0.item_flag == ChapterConst.CellFlagTriggerDisabled:
							local var_7_3 = pg.map_event_template[var_7_2.attachmentId].gametip

							if var_7_3 != "":
								pg.TipsMgr.GetInstance().ShowTips(i18n(var_7_3))

						var_7_2.attachment = arg_7_0.item_type
						var_7_2.attachmentId = arg_7_0.item_id
						var_7_2.flag = arg_7_0.item_flag
						var_7_2.data = arg_7_0.item_data
					else
						var_7_1[var_7_0] = ChapterCell.New(arg_7_0)
				elif arg_7_0.item_type != ChapterConst.AttachNone and arg_7_0.item_type != ChapterConst.AttachBorn and arg_7_0.item_type != ChapterConst.AttachBorn_Sub and arg_7_0.item_type != ChapterConst.AttachOni_Target and arg_7_0.item_type != ChapterConst.AttachOni:
					local var_7_4 = ChapterCell.New(arg_7_0)

					var_3_0.mergeChapterCell(var_7_4))

			var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyAttachment, ChapterConst.DirtyAutoAction)

		if #arg_3_1.ai_list > 0:
			_.each(arg_3_1.ai_list, function(arg_8_0)
				local var_8_0 = ChapterChampionPackage.New(arg_8_0)

				var_3_0.mergeChampion(var_8_0))

			var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyChampion, ChapterConst.DirtyAutoAction)

		if #arg_3_1.add_flag_list > 0 or #arg_3_1.del_flag_list > 0:
			var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyFleet, ChapterConst.DirtyStrategy, ChapterConst.DirtyCellFlag, ChapterConst.DirtyFloatItems, ChapterConst.DirtyAttachment)

			arg_3_0.updateExtraFlag(var_3_0, arg_3_1.add_flag_list, arg_3_1.del_flag_list)

		if #arg_3_1.buff_list > 0:
			var_3_0.UpdateBuffList(arg_3_1.buff_list)

		if #arg_3_1.cell_flag_list > 0:
			_.each(arg_3_1.cell_flag_list, function(arg_9_0)
				local var_9_0 = var_3_0.getChapterCell(arg_9_0.pos.row, arg_9_0.pos.column)

				if var_9_0:
					var_9_0.updateFlagList(arg_9_0)
				else
					var_9_0 = ChapterCell.New(arg_9_0)

				var_3_0.updateChapterCell(var_9_0))

			var_3_1 = bit.bor(var_3_1, ChapterConst.DirtyCellFlag)

		arg_3_0.updateChapter(var_3_0, var_3_1)

		if arg_3_2:
			arg_3_0.sendNotification(GAME.CHAPTER_OP_DONE, {
				type = ChapterConst.OpSkipBattle
			})

def var_0_0.setEliteCache(arg_10_0, arg_10_1):
	arg_10_0.mapEliteFleetCache = {}
	arg_10_0.mapEliteCommanderCache = {}
	arg_10_0.mapSupportFleetCache = {}

	local var_10_0 = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_1):
		var_10_0[iter_10_1.map_id] = var_10_0[iter_10_1.map_id] or {}

		table.insert(var_10_0[iter_10_1.map_id], iter_10_1)

	for iter_10_2, iter_10_3 in pairs(var_10_0):
		arg_10_0.mapEliteFleetCache[iter_10_2], arg_10_0.mapEliteCommanderCache[iter_10_2], arg_10_0.mapSupportFleetCache[iter_10_2] = Chapter.BuildEliteFleetList(iter_10_3)

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inElite")
	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inSupport")

	for iter_10_4, iter_10_5 in pairs(arg_10_0.data):
		local var_10_1 = iter_10_5.getConfig("formation")

		iter_10_5.setEliteFleetList(Clone(arg_10_0.mapEliteFleetCache[var_10_1]) or {
			{},
			{},
			{}
		})
		iter_10_5.setEliteCommanders(Clone(arg_10_0.mapEliteCommanderCache[var_10_1]) or {
			{},
			{},
			{}
		})
		iter_10_5.setSupportFleetList(Clone(arg_10_0.mapSupportFleetCache[var_10_1]) or {
			{},
			{},
			{}
		})
		arg_10_0.updateChapter(iter_10_5)

def var_0_0.buildMaps(arg_11_0):
	arg_11_0.initChapters()
	arg_11_0.buildBaseMaps()
	arg_11_0.buildRemasterMaps()

def var_0_0.initChapters(arg_12_0):
	var_0_0.MapToChapters = table.shallowCopy(pg.chapter_template.get_id_list_by_map)

	for iter_12_0, iter_12_1 in pairs(pg.story_group.get_id_list_by_map):
		var_0_0.MapToChapters[iter_12_0] = var_0_0.MapToChapters[iter_12_0] or {}
		var_0_0.MapToChapters[iter_12_0] = table.mergeArray(var_0_0.MapToChapters[iter_12_0], iter_12_1)

	var_0_0.FormationToChapters = pg.chapter_template.get_id_list_by_formation

def var_0_0.buildBaseMaps(arg_13_0):
	var_0_0.ActToMaps = {}
	var_0_0.TypeToMaps = {}

	local var_13_0 = {}

	for iter_13_0, iter_13_1 in ipairs(pg.expedition_data_by_map.all):
		local var_13_1 = Map.New({
			id = iter_13_1,
			chapterIds = var_0_0.MapToChapters[iter_13_1]
		})

		var_13_0[iter_13_1] = var_13_1

		local var_13_2 = var_13_1.getConfig("on_activity")

		if var_13_2 != 0:
			var_0_0.ActToMaps[var_13_2] = var_0_0.ActToMaps[var_13_2] or {}

			table.insert(var_0_0.ActToMaps[var_13_2], var_13_1.id)

		local var_13_3 = var_13_1.getMapType()

		var_0_0.TypeToMaps[var_13_3] = var_0_0.TypeToMaps[var_13_3] or {}

		table.insert(var_0_0.TypeToMaps[var_13_3], var_13_1.id)

	arg_13_0.baseMaps = var_13_0

def var_0_0.buildRemasterMaps(arg_14_0):
	var_0_0.RemasterToMaps = {}

	local var_14_0 = {}

	_.each(pg.re_map_template.all, function(arg_15_0)
		local var_15_0 = pg.re_map_template[arg_15_0]

		_.each(var_15_0.config_data, function(arg_16_0)
			local var_16_0 = arg_14_0.baseMaps[pg.chapter_template[arg_16_0].map]

			assert(not var_14_0[var_16_0.id] or var_14_0[var_16_0.id] == arg_15_0, "remaster chapter error." .. arg_16_0)

			if not var_14_0[var_16_0.id]:
				var_14_0[var_16_0.id] = arg_15_0

				var_16_0.setRemaster(arg_15_0)

				var_0_0.RemasterToMaps[arg_15_0] = var_0_0.RemasterToMaps[arg_15_0] or {}

				table.insert(var_0_0.RemasterToMaps[arg_15_0], var_16_0.id)))

def var_0_0.IsChapterInRemaster(arg_17_0, arg_17_1):
	return _.detect(pg.re_map_template.all, function(arg_18_0)
		local var_18_0 = pg.re_map_template[arg_18_0]

		return _.any(var_18_0.config_data, function(arg_19_0)
			return arg_19_0 == arg_17_1))

def var_0_0.getMaxEscortChallengeTimes(arg_20_0):
	return getProxy(ActivityProxy).getActivityParameter("escort_daily_count") or 0

def var_0_0.getEscortChapterIds(arg_21_0):
	return getProxy(ActivityProxy).getActivityParameter("escort_exp_id") or {}

def var_0_0.resetEscortChallengeTimes(arg_22_0):
	arg_22_0.escortChallengeTimes = 0

def var_0_0.addChapterListener(arg_23_0, arg_23_1):
	if not arg_23_1.dueTime or not arg_23_0.timers:
		return

	if arg_23_0.timers[arg_23_1.id]:
		arg_23_0.timers[arg_23_1.id].Stop()

		arg_23_0.timers[arg_23_1.id] = None

	local var_23_0 = arg_23_1.dueTime - pg.TimeMgr.GetInstance().GetServerTime()

	local function var_23_1()
		arg_23_0.data[arg_23_1.id].dueTime = None

		arg_23_0.data[arg_23_1.id].display("times'up")
		arg_23_0.sendNotification(var_0_0.CHAPTER_UPDATED, {
			dirty = 0,
			chapter = arg_23_0.data[arg_23_1.id].clone()
		})
		arg_23_0.sendNotification(var_0_0.CHAPTER_TIMESUP)

	if var_23_0 > 0:
		arg_23_0.timers[arg_23_1.id] = Timer.New(function()
			var_23_1()
			arg_23_0.timers[arg_23_1.id].Stop()

			arg_23_0.timers[arg_23_1.id] = None, var_23_0, 1)

		arg_23_0.timers[arg_23_1.id].Start()
	else
		var_23_1()

def var_0_0.removeChapterListener(arg_26_0, arg_26_1):
	if arg_26_0.timers[arg_26_1]:
		arg_26_0.timers[arg_26_1].Stop()

		arg_26_0.timers[arg_26_1] = None

def var_0_0.remove(arg_27_0):
	for iter_27_0, iter_27_1 in pairs(arg_27_0.timers):
		iter_27_1.Stop()

	arg_27_0.timers = None

def var_0_0.GetRawChapterById(arg_28_0, arg_28_1):
	return arg_28_0.data[arg_28_1]

def var_0_0.getChapterById(arg_29_0, arg_29_1, arg_29_2):
	local var_29_0 = arg_29_0.data[arg_29_1]

	if not var_29_0:
		assert(pg.chapter_template[arg_29_1], "Not Exist Chapter ID. " .. (arg_29_1 or "NIL"))

		var_29_0 = Chapter.New({
			id = arg_29_1
		})

		local var_29_1 = var_29_0.getConfig("formation")

		if var_29_0.getConfig("type") == Chapter.CustomFleet:
			var_29_0.setEliteFleetList(Clone(arg_29_0.mapEliteFleetCache[var_29_1]) or {
				{},
				{},
				{}
			})
			var_29_0.setEliteCommanders(Clone(arg_29_0.mapEliteCommanderCache[var_29_1]) or {
				{},
				{},
				{}
			})
		elif var_29_0.getConfig("type") == Chapter.SelectFleet:
			var_29_0.setSupportFleetList(Clone(arg_29_0.mapSupportFleetCache[var_29_1]) or {
				{},
				{},
				{}
			})

		arg_29_0.data[arg_29_1] = var_29_0

	return arg_29_2 and var_29_0 or var_29_0.clone()

def var_0_0.GetChapterItemById(arg_30_0, arg_30_1):
	if Chapter.bindConfigTable()[arg_30_1]:
		return arg_30_0.getChapterById(arg_30_1, True)
	elif ChapterStoryGroup.bindConfigTable()[arg_30_1]:
		local var_30_0 = arg_30_0.chapterStoryGroups[arg_30_1]

		if not var_30_0:
			var_30_0 = ChapterStoryGroup.New({
				configId = arg_30_1
			})
			arg_30_0.chapterStoryGroups[arg_30_1] = var_30_0

		return var_30_0

def var_0_0.updateChapter(arg_31_0, arg_31_1, arg_31_2):
	assert(isa(arg_31_1, Chapter), "should be an instance of Chapter")

	local var_31_0 = arg_31_0.data[arg_31_1.id]
	local var_31_1 = arg_31_1

	arg_31_0.data[arg_31_1.id] = var_31_1

	if var_31_0:
		arg_31_0.removeChapterListener(var_31_0.id)

	arg_31_0.addChapterListener(var_31_1)

	if getProxy(PlayerProxy).getInited():
		arg_31_0.facade.sendNotification(var_0_0.CHAPTER_UPDATED, {
			chapter = var_31_1.clone(),
			dirty = defaultValue(arg_31_2, 0)
		})

	if var_31_1.active and var_31_1.fleet:
		var_31_1.fleet.clearShipHpChange()

	if tobool(checkExist(var_31_0, {
		"active"
	})) != tobool(var_31_1.active):
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inChapter")

def var_0_0.getMapById(arg_32_0, arg_32_1):
	return arg_32_0.baseMaps[arg_32_1]

def var_0_0.getNormalMaps(arg_33_0):
	local var_33_0 = {}

	for iter_33_0, iter_33_1 in ipairs(arg_33_0.baseMaps):
		table.insert(var_33_0, iter_33_1)

	return var_33_0

def var_0_0.getMapsByType(arg_34_0, arg_34_1):
	if var_0_0.TypeToMaps[arg_34_1]:
		return _.map(var_0_0.TypeToMaps[arg_34_1], function(arg_35_0)
			return arg_34_0.getMapById(arg_35_0))
	else
		return {}

def var_0_0.getMapsByActId(arg_36_0, arg_36_1):
	if var_0_0.ActToMaps[arg_36_1]:
		return underscore.map(var_0_0.ActToMaps[arg_36_1], function(arg_37_0)
			return arg_36_0.getMapById(arg_37_0))
	else
		return {}

def var_0_0.getRemasterMaps(arg_38_0, arg_38_1):
	if var_0_0.RemasterToMaps[arg_38_1]:
		return underscore.map(var_0_0.RemasterToMaps[arg_38_1], function(arg_39_0)
			return arg_38_0.getMapById(arg_39_0))
	else
		return {}

def var_0_0.getMapsByActivities(arg_40_0):
	local var_40_0 = {}
	local var_40_1 = getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_ZPROJECT)

	underscore.each(var_40_1, function(arg_41_0)
		if not arg_41_0.isEnd():
			var_40_0 = table.mergeArray(var_40_0, arg_40_0.getMapsByActId(arg_41_0.id)))

	return var_40_0

def var_0_0.getLastUnlockMap(arg_42_0):
	local var_42_0

	for iter_42_0, iter_42_1 in ipairs(arg_42_0.getNormalMaps()):
		if not iter_42_1.isUnlock():
			break

		var_42_0 = iter_42_1

	return var_42_0

def var_0_0.updateExtraFlag(arg_43_0, arg_43_1, arg_43_2, arg_43_3, arg_43_4):
	local var_43_0 = arg_43_1.updateExtraFlags(arg_43_2, arg_43_3)

	if not arg_43_4 and not var_43_0:
		return

	local var_43_1 = {}

	for iter_43_0, iter_43_1 in ipairs(arg_43_2):
		table.insert(var_43_1, iter_43_1)

	arg_43_0.SetExtendChapterData(arg_43_1.id, "extraFlagUpdate", var_43_1)

	return True

def var_0_0.extraFlagUpdated(arg_44_0, arg_44_1):
	arg_44_0.RemoveExtendChapterData(arg_44_1, "extraFlagUpdate")

def var_0_0.getUpdatedExtraFlags(arg_45_0, arg_45_1):
	return arg_45_0.GetExtendChapterData(arg_45_1, "extraFlagUpdate")

def var_0_0.SetExtendChapterData(arg_46_0, arg_46_1, arg_46_2, arg_46_3):
	assert(arg_46_1, "Missing Chapter ID")

	arg_46_0.chaptersExtend[arg_46_1] = arg_46_0.chaptersExtend[arg_46_1] or {}
	arg_46_0.chaptersExtend[arg_46_1][arg_46_2] = arg_46_3

def var_0_0.AddExtendChapterDataArray(arg_47_0, arg_47_1, arg_47_2, arg_47_3, arg_47_4):
	assert(arg_47_1, "Missing Chapter ID")

	arg_47_0.chaptersExtend[arg_47_1] = arg_47_0.chaptersExtend[arg_47_1] or {}

	if type(arg_47_0.chaptersExtend[arg_47_1][arg_47_2]) != "table":
		assert(arg_47_0.chaptersExtend[arg_47_1][arg_47_2] == None, "Changing NonEmpty ExtendData " .. arg_47_2 .. " to Table ID. " .. arg_47_1)

		arg_47_0.chaptersExtend[arg_47_1][arg_47_2] = {}

	arg_47_4 = arg_47_4 or #arg_47_0.chaptersExtend[arg_47_1][arg_47_2] + 1
	arg_47_0.chaptersExtend[arg_47_1][arg_47_2][arg_47_4] = arg_47_3

def var_0_0.AddExtendChapterDataTable(arg_48_0, arg_48_1, arg_48_2, arg_48_3, arg_48_4):
	assert(arg_48_1, "Missing Chapter ID")

	arg_48_0.chaptersExtend[arg_48_1] = arg_48_0.chaptersExtend[arg_48_1] or {}

	if type(arg_48_0.chaptersExtend[arg_48_1][arg_48_2]) != "table":
		assert(arg_48_0.chaptersExtend[arg_48_1][arg_48_2] == None, "Changing NonEmpty ExtendData " .. arg_48_2 .. " to Table ID. " .. arg_48_1)

		arg_48_0.chaptersExtend[arg_48_1][arg_48_2] = {}

	assert(arg_48_3, "Missing Index on Set HashData")

	arg_48_0.chaptersExtend[arg_48_1][arg_48_2][arg_48_3] = arg_48_4

def var_0_0.GetExtendChapterData(arg_49_0, arg_49_1, arg_49_2):
	assert(arg_49_1, "Missing Chapter ID")
	assert(arg_49_2, "Requesting Empty key")

	if not arg_49_2 or not arg_49_0.chaptersExtend[arg_49_1]:
		return

	return arg_49_0.chaptersExtend[arg_49_1][arg_49_2]

def var_0_0.RemoveExtendChapterData(arg_50_0, arg_50_1, arg_50_2):
	assert(arg_50_1, "Missing Chapter ID")

	if not arg_50_2 or not arg_50_0.chaptersExtend[arg_50_1]:
		return

	arg_50_0.chaptersExtend[arg_50_1][arg_50_2] = None

	if next(arg_50_0.chaptersExtend[arg_50_1]):
		return

	arg_50_0.RemoveExtendChapter(arg_50_1)

def var_0_0.GetExtendChapter(arg_51_0, arg_51_1):
	assert(arg_51_1, "Missing Chapter ID")

	return arg_51_0.chaptersExtend[arg_51_1]

def var_0_0.RemoveExtendChapter(arg_52_0, arg_52_1):
	assert(arg_52_1, "Missing Chapter ID")

	if not arg_52_0.chaptersExtend[arg_52_1]:
		return

	arg_52_0.chaptersExtend[arg_52_1] = None

def var_0_0.duplicateEliteFleet(arg_53_0, arg_53_1):
	if arg_53_1.getConfig("type") != Chapter.CustomFleet:
		return

	local var_53_0 = arg_53_1.getEliteFleetList()
	local var_53_1 = arg_53_1.getEliteFleetCommanders()
	local var_53_2 = arg_53_1.getConfig("formation")

	arg_53_0.mapEliteFleetCache[var_53_2] = Clone(var_53_0)
	arg_53_0.mapEliteCommanderCache[var_53_2] = Clone(var_53_1)

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inElite")

	for iter_53_0, iter_53_1 in ipairs(var_0_0.FormationToChapters[var_53_2]):
		local var_53_3 = arg_53_0.getChapterById(iter_53_1, True)

		if var_53_3.configId != arg_53_1.configId:
			var_53_3.setEliteFleetList(Clone(var_53_0))
			var_53_3.setEliteCommanders(Clone(var_53_1))
			arg_53_0.updateChapter(var_53_3)

def var_0_0.duplicateSupportFleet(arg_54_0, arg_54_1):
	local var_54_0 = arg_54_1.getSupportFleet()
	local var_54_1 = arg_54_1.getConfig("formation")

	arg_54_0.mapSupportFleetCache[var_54_1] = {
		Clone(var_54_0)
	}

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inSupport")

	for iter_54_0, iter_54_1 in ipairs(var_0_0.FormationToChapters[var_54_1]):
		local var_54_2 = arg_54_0.getChapterById(iter_54_1, True)

		if var_54_2.configId != arg_54_1.configId:
			var_54_2.setSupportFleetList({
				Clone(var_54_0)
			})
			arg_54_0.updateChapter(var_54_2)

def var_0_0.CheckUnitInSupportFleet(arg_55_0, arg_55_1):
	local var_55_0 = {}
	local var_55_1 = arg_55_1.id

	for iter_55_0, iter_55_1 in pairs(arg_55_0.mapSupportFleetCache):
		for iter_55_2, iter_55_3 in ipairs(iter_55_1):
			if table.contains(iter_55_3, var_55_1):
				var_55_0[iter_55_0] = True

				break

	return next(var_55_0), var_55_0

def var_0_0.RemoveUnitFromSupportFleet(arg_56_0, arg_56_1):
	arg_56_0.sendNotification(GAME.REMOVE_ELITE_TARGET_SHIP, {
		shipId = arg_56_1.id,
		callback = next
	})

def var_0_0.getActiveChapter(arg_57_0, arg_57_1):
	for iter_57_0, iter_57_1 in pairs(arg_57_0.data):
		if iter_57_1.active:
			return arg_57_1 and iter_57_1 or iter_57_1.clone()

def var_0_0.getLastMapForActivity(arg_58_0):
	local var_58_0
	local var_58_1
	local var_58_2 = arg_58_0.getActiveChapter()

	if var_58_2:
		local var_58_3 = arg_58_0.getMapById(var_58_2.getConfig("map"))

		if var_58_3.isActivity() and not var_58_3.isRemaster():
			return var_58_3.id, var_58_2.id

	local var_58_4 = Map.lastMapForActivity and arg_58_0.getMapById(Map.lastMapForActivity)

	if var_58_4 and not var_58_4.isRemaster() and var_58_4.isUnlock():
		return Map.lastMapForActivity

	if Map.lastMapForActivity:
		Map.lastMapForActivity = None

		arg_58_0.recordLastMap(var_0_0.LAST_MAP_FOR_ACTIVITY, 0)

	local var_58_5 = arg_58_0.getMapsByActivities()

	table.sort(var_58_5, function(arg_59_0, arg_59_1)
		return arg_59_0.id > arg_59_1.id)

	local var_58_6 = {}

	if _.all(var_58_5, function(arg_60_0)
		return arg_60_0.getConfig("type") == Map.EVENT):
		var_58_6 = var_58_5
	else
		for iter_58_0, iter_58_1 in ipairs({
			Map.ACTIVITY_EASY,
			Map.ACTIVITY_HARD
		}):
			local var_58_7 = underscore.filter(var_58_5, function(arg_61_0)
				return arg_61_0.getMapType() == iter_58_1)

			if #var_58_7 > 0:
				var_58_6 = var_58_7

				if underscore.any(var_58_6, function(arg_62_0)
					return not arg_62_0.isClearForActivity()):
					break

	for iter_58_2 = #var_58_6, 1, -1:
		local var_58_8 = var_58_6[iter_58_2]

		if var_58_8.isUnlock():
			return var_58_8.id

	if #var_58_5 > 0:
		return var_58_5[1].id

def var_0_0.updateActiveChapterShips(arg_63_0):
	local var_63_0 = arg_63_0.getActiveChapter(True)

	if var_63_0:
		_.each(var_63_0.fleets, function(arg_64_0)
			arg_64_0.flushShips())
		arg_63_0.updateChapter(var_63_0, ChapterConst.DirtyFleet)

def var_0_0.resetRepairTimes(arg_65_0):
	arg_65_0.repairTimes = 0

def var_0_0.getUseableEliteMap(arg_66_0):
	local var_66_0 = {}

	for iter_66_0, iter_66_1 in ipairs(arg_66_0.getMapsByType(Map.ELITE)):
		if iter_66_1.isEliteEnabled():
			var_66_0[#var_66_0 + 1] = iter_66_1

	return var_66_0

def var_0_0.getUseableMaxEliteMap(arg_67_0):
	local var_67_0 = arg_67_0.getUseableEliteMap()

	if #var_67_0 == 0:
		return False
	else
		local var_67_1

		for iter_67_0, iter_67_1 in ipairs(var_67_0):
			if not var_67_1 or var_67_1.id < iter_67_1.id:
				var_67_1 = iter_67_1

		return var_67_1

def var_0_0.getHigestClearChapterAndMap(arg_68_0):
	local var_68_0 = arg_68_0.baseMaps[1]

	for iter_68_0, iter_68_1 in ipairs(arg_68_0.getNormalMaps()):
		if not iter_68_1.isAnyChapterClear():
			break

		var_68_0 = iter_68_1

	local var_68_1 = arg_68_0.getChapterById(var_68_0.chapterIds[1])

	for iter_68_2, iter_68_3 in ipairs(var_68_0.getChapters()):
		if not iter_68_3.isClear():
			break

		var_68_1 = iter_68_3

	return var_68_1, var_68_0

def var_0_0.SortRecommendLimitation(arg_69_0):
	table.sort(arg_69_0, CompareFuncs({
		function(arg_70_0)
			if type(arg_70_0) == "number":
				if arg_70_0 == 0:
					return 1
				else
					return -arg_70_0
			elif type(arg_70_0) == "string":
				return 0
			else
				assert(False)
	}))

def var_0_0.eliteFleetRecommend(arg_71_0, arg_71_1, arg_71_2):
	local var_71_0 = arg_71_1.getEliteFleetList()[arg_71_2]
	local var_71_1 = arg_71_1.getConfig("limitation")[arg_71_2]
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

	for iter_71_0, iter_71_1 in ipairs(arg_71_1.getEliteFleetList()):
		for iter_71_2, iter_71_3 in ipairs(iter_71_1):
			var_71_5[#var_71_5 + 1] = iter_71_3

	local var_71_6

	if arg_71_2 > 2:
		var_71_6 = {
			[TeamType.Submarine] = var_71_4
		}
	else
		var_71_6 = {
			[TeamType.Main] = var_71_2,
			[TeamType.Vanguard] = var_71_3
		}

	local var_71_7 = arg_71_0.FleetRecommend(var_71_0, var_71_5, var_71_6, function(arg_72_0)
		return ShipStatus.ShipStatusCheck("inElite", arg_72_0, None, {
			inElite = arg_71_1.getConfig("formation")
		}))

	table.clean(var_71_0)
	table.insertto(var_71_0, var_71_7)

def var_0_0.SupportFleetRecommend(arg_73_0, arg_73_1, arg_73_2):
	local var_73_0 = arg_73_1.getSupportFleet()
	local var_73_1 = {
		[TeamType.Main] = {
			"hang",
			"hang",
			"hang"
		}
	}
	local var_73_2 = table.shallowCopy(var_73_0)
	local var_73_3 = arg_73_0.FleetRecommend(var_73_0, var_73_2, var_73_1, function(arg_74_0)
		return ShipStatus.ShipStatusCheck("inSupport", arg_74_0, None, {
			inSupport = arg_73_1.getConfig("formation")
		}))

	table.clean(var_73_0)
	table.insertto(var_73_0, var_73_3)

def var_0_0.FleetRecommend(arg_75_0, arg_75_1, arg_75_2, arg_75_3, arg_75_4):
	arg_75_1 = table.shallowCopy(arg_75_1)
	arg_75_2 = table.shallowCopy(arg_75_2)

	local var_75_0 = getProxy(BayProxy)
	local var_75_1 = getProxy(BayProxy).getRawData()

	for iter_75_0, iter_75_1 in ipairs(arg_75_1):
		local var_75_2 = var_75_1[iter_75_1].getShipType()
		local var_75_3 = TeamType.GetTeamFromShipType(var_75_2)
		local var_75_4 = 0
		local var_75_5 = arg_75_3[var_75_3]

		for iter_75_2, iter_75_3 in ipairs(var_75_5):
			if ShipType.ContainInLimitBundle(iter_75_3, var_75_2):
				var_75_4 = iter_75_3

				break

		for iter_75_4, iter_75_5 in ipairs(var_75_5):
			if iter_75_5 == var_75_4:
				table.remove(var_75_5, iter_75_4)

				break

	local function var_75_6(arg_76_0, arg_76_1)
		local var_76_0 = underscore.filter(TeamType.GetShipTypeListFromTeam(arg_76_1), function(arg_77_0)
			return ShipType.ContainInLimitBundle(arg_76_0, arg_77_0))
		local var_76_1 = var_75_0.GetRecommendShip(var_76_0, arg_75_2, arg_75_4)

		if var_76_1:
			local var_76_2 = var_76_1.id

			arg_75_2[#arg_75_2 + 1] = var_76_2
			arg_75_1[#arg_75_1 + 1] = var_76_2

	for iter_75_6, iter_75_7 in pairs(arg_75_3):
		for iter_75_8, iter_75_9 in ipairs(iter_75_7):
			var_75_6(iter_75_9, iter_75_6)

	return arg_75_1

def var_0_0.isClear(arg_78_0, arg_78_1):
	local var_78_0 = arg_78_0.GetChapterItemById(arg_78_1)

	if not var_78_0:
		return False

	return var_78_0.isClear()

def var_0_0.getEscortShop(arg_79_0):
	return Clone(arg_79_0.escortShop)

def var_0_0.updateEscortShop(arg_80_0, arg_80_1):
	arg_80_0.escortShop = arg_80_1

def var_0_0.recordLastMap(arg_81_0, arg_81_1, arg_81_2):
	local var_81_0 = False

	if arg_81_1 == var_0_0.LAST_MAP_FOR_ACTIVITY:
		Map.lastMapForActivity = arg_81_2
		var_81_0 = True
	elif arg_81_1 == var_0_0.LAST_MAP and arg_81_2 != Map.lastMap:
		Map.lastMap = arg_81_2
		var_81_0 = True

	if var_81_0:
		local var_81_1 = getProxy(PlayerProxy).getRawData()

		PlayerPrefs.SetInt(arg_81_1 .. var_81_1.id, arg_81_2)
		PlayerPrefs.Save()

def var_0_0.getLastMap(arg_82_0, arg_82_1):
	local var_82_0 = getProxy(PlayerProxy).getRawData()
	local var_82_1 = PlayerPrefs.GetInt(arg_82_1 .. var_82_0.id)

	if var_82_1 != 0:
		return var_82_1

def var_0_0.IsActivitySPChapterActive(arg_83_0):
	local var_83_0 = arg_83_0.getMapsByActivities()
	local var_83_1 = _.select(var_83_0, function(arg_84_0)
		return arg_84_0.getMapType() == Map.ACT_EXTRA)
	local var_83_2 = _.reduce(var_83_1, {}, function(arg_85_0, arg_85_1)
		local var_85_0 = _.select(arg_85_1.getChapters(True), function(arg_86_0)
			return arg_86_0.getPlayType() == ChapterConst.TypeRange)

		return table.mergeArray(arg_85_0, var_85_0))

	return _.any(var_83_2, function(arg_87_0)
		return arg_87_0.isUnlock() and arg_87_0.isPlayerLVUnlock() and arg_87_0.enoughTimes2Start())

def var_0_0.getSubAidFlag(arg_88_0, arg_88_1):
	local var_88_0 = ys.Battle.BattleConst.SubAidFlag
	local var_88_1 = arg_88_0.fleet
	local var_88_2 = False
	local var_88_3 = _.detect(arg_88_0.fleets, function(arg_89_0)
		return arg_89_0.getFleetType() == FleetType.Submarine and arg_89_0.isValid())

	if var_88_3:
		if var_88_3.inHuntingRange(var_88_1.line.row, var_88_1.line.column):
			var_88_2 = True
		else
			local var_88_4 = var_88_3.getStrategies()
			local var_88_5 = _.detect(var_88_4, function(arg_90_0)
				return arg_90_0.id == ChapterConst.StrategyCallSubOutofRange)

			if var_88_5 and var_88_5.count > 0:
				var_88_2 = True

	if var_88_2:
		local var_88_6 = getProxy(PlayerProxy).getRawData()
		local var_88_7, var_88_8 = arg_88_0.getFleetCost(var_88_1, arg_88_1)
		local var_88_9, var_88_10 = arg_88_0.getFleetAmmo(var_88_3)
		local var_88_11 = 0

		for iter_88_0, iter_88_1 in ipairs({
			arg_88_0.getFleetCost(var_88_3, arg_88_1)
		}):
			var_88_11 = var_88_11 + iter_88_1.oil

		if var_88_10 <= 0:
			return var_88_0.AMMO_EMPTY
		elif var_88_11 + var_88_8.oil >= var_88_6.oil:
			return var_88_0.OIL_EMPTY
		else
			return True, var_88_3
	else
		return var_88_0.AID_EMPTY

def var_0_0.GetChapterAuraBuffs(arg_91_0):
	local var_91_0 = {}

	for iter_91_0, iter_91_1 in ipairs(arg_91_0.fleets):
		if iter_91_1.getFleetType() != FleetType.Support:
			local var_91_1 = iter_91_1.getMapAura()

			for iter_91_2, iter_91_3 in ipairs(var_91_1):
				table.insert(var_91_0, iter_91_3)

	return var_91_0

def var_0_0.GetChapterAidBuffs(arg_92_0):
	local var_92_0 = {}

	for iter_92_0, iter_92_1 in ipairs(arg_92_0.fleets):
		if iter_92_1 != arg_92_0.fleet and iter_92_1.getFleetType() != FleetType.Support:
			local var_92_1 = iter_92_1.getMapAid()

			for iter_92_2, iter_92_3 in pairs(var_92_1):
				var_92_0[iter_92_2] = iter_92_3

	return var_92_0

def var_0_0.RecordComboHistory(arg_93_0, arg_93_1, arg_93_2):
	if arg_93_2 != None:
		arg_93_0.SetExtendChapterData(arg_93_1, "comboHistoryBuffer", arg_93_2)
	else
		arg_93_0.RemoveExtendChapterData(arg_93_1, "comboHistoryBuffer")

def var_0_0.GetComboHistory(arg_94_0, arg_94_1):
	return arg_94_0.GetExtendChapterData(arg_94_1, "comboHistoryBuffer")

def var_0_0.RecordJustClearChapters(arg_95_0, arg_95_1, arg_95_2):
	if arg_95_2 != None:
		arg_95_0.SetExtendChapterData(arg_95_1, "justClearChapters", arg_95_2)
	else
		arg_95_0.RemoveExtendChapterData(arg_95_1, "justClearChapters")

def var_0_0.GetJustClearChapters(arg_96_0, arg_96_1):
	return arg_96_0.GetExtendChapterData(arg_96_1, "justClearChapters")

def var_0_0.RecordLastDefeatedEnemy(arg_97_0, arg_97_1, arg_97_2):
	if arg_97_2 != None:
		arg_97_0.SetExtendChapterData(arg_97_1, "defeatedEnemiesBuffer", arg_97_2)
	else
		arg_97_0.RemoveExtendChapterData(arg_97_1, "defeatedEnemiesBuffer")

def var_0_0.GetLastDefeatedEnemy(arg_98_0, arg_98_1):
	return arg_98_0.GetExtendChapterData(arg_98_1, "defeatedEnemiesBuffer")

def var_0_0.ifShowRemasterTip(arg_99_0):
	return arg_99_0.remasterTip

def var_0_0.setRemasterTip(arg_100_0, arg_100_1):
	arg_100_0.remasterTip = arg_100_1

def var_0_0.updateRemasterTicketsNum(arg_101_0, arg_101_1):
	arg_101_0.remasterTickets = arg_101_1

def var_0_0.resetDailyCount(arg_102_0):
	arg_102_0.remasterDailyCount = 0

def var_0_0.updateDailyCount(arg_103_0):
	arg_103_0.remasterDailyCount = arg_103_0.remasterDailyCount + pg.gameset.reactivity_ticket_daily.key_value

def var_0_0.GetSkipPrecombat(arg_104_0):
	if arg_104_0.skipPrecombat == None:
		arg_104_0.skipPrecombat = PlayerPrefs.GetInt("chapter_skip_precombat", 0)

	return arg_104_0.skipPrecombat > 0

def var_0_0.UpdateSkipPrecombat(arg_105_0, arg_105_1):
	arg_105_1 = tobool(arg_105_1) and 1 or 0

	if arg_105_1 != arg_105_0.GetSkipPrecombat():
		PlayerPrefs.SetInt("chapter_skip_precombat", arg_105_1)

		arg_105_0.skipPrecombat = arg_105_1

		arg_105_0.sendNotification(var_0_0.CHAPTER_SKIP_PRECOMBAT_UPDATED, arg_105_1)

def var_0_0.GetChapterAutoFlag(arg_106_0, arg_106_1):
	return arg_106_0.GetExtendChapterData(arg_106_1, "AutoFightFlag")

def var_0_0.SetChapterAutoFlag(arg_107_0, arg_107_1, arg_107_2, arg_107_3):
	arg_107_2 = tobool(arg_107_2)

	if arg_107_2 == (arg_107_0.GetChapterAutoFlag(arg_107_1) == 1):
		return

	arg_107_0.SetExtendChapterData(arg_107_1, "AutoFightFlag", arg_107_2 and 1 or 0)

	if arg_107_2:
		arg_107_0.UpdateSkipPrecombat(True)

		if AutoBotCommand.autoBotSatisfied():
			PlayerPrefs.SetInt("autoBotIsAcitve" .. AutoBotCommand.GetAutoBotMark(), 1)

		getProxy(MetaCharacterProxy).setMetaTacticsInfoOnStart()
		pg.BrightnessMgr.GetInstance().SetScreenNeverSleep(True)

		if not LOCK_BATTERY_SAVEMODE and PlayerPrefs.GetInt(AUTOFIGHT_BATTERY_SAVEMODE, 0) == 1 and pg.BrightnessMgr.GetInstance().IsPermissionGranted():
			pg.BrightnessMgr.GetInstance().EnterManualMode()

			if PlayerPrefs.GetInt(AUTOFIGHT_DOWN_FRAME, 0) == 1:
				getProxy(SettingsProxy).RecordFrameRate()

				Application.targetFrameRate = 30
	else
		arg_107_0.StopContinuousOperation(SYSTEM_SCENARIO, arg_107_3)
		pg.BrightnessMgr.GetInstance().SetScreenNeverSleep(False)

		if not LOCK_BATTERY_SAVEMODE:
			pg.BrightnessMgr.GetInstance().ExitManualMode()
			getProxy(SettingsProxy).RestoreFrameRate()

	arg_107_0.facade.sendNotification(var_0_0.CHAPTER_AUTO_FIGHT_FLAG_UPDATED, arg_107_2 and 1 or 0)
	arg_107_0.facade.sendNotification(PlayerResUI.CHANGE_TOUCH_ABLE, not arg_107_2)

def var_0_0.StopAutoFight(arg_108_0, arg_108_1):
	local var_108_0 = arg_108_0.getActiveChapter(True)

	if not var_108_0:
		return

	arg_108_0.SetChapterAutoFlag(var_108_0.id, False, arg_108_1)

def var_0_0.FinishAutoFight(arg_109_0, arg_109_1):
	if arg_109_0.GetChapterAutoFlag(arg_109_1) == 1:
		pg.BrightnessMgr.GetInstance().SetScreenNeverSleep(False)

		if not LOCK_BATTERY_SAVEMODE:
			pg.BrightnessMgr.GetInstance().ExitManualMode()
			getProxy(SettingsProxy).RestoreFrameRate()

		arg_109_0.facade.sendNotification(PlayerResUI.CHANGE_TOUCH_ABLE, True)

	local var_109_0 = arg_109_0.GetExtendChapter(arg_109_1)

	arg_109_0.RemoveExtendChapter(arg_109_1)

	return var_109_0

def var_0_0.buildRemasterInfo(arg_110_0):
	arg_110_0.remasterInfo = {}

	for iter_110_0, iter_110_1 in ipairs(pg.re_map_template.all):
		for iter_110_2, iter_110_3 in ipairs(pg.re_map_template[iter_110_1].drop_gain):
			if #iter_110_3 > 0:
				local var_110_0, var_110_1, var_110_2, var_110_3 = unpack(iter_110_3)

				arg_110_0.remasterInfo[var_110_0] = defaultValue(arg_110_0.remasterInfo[var_110_0], {})
				arg_110_0.remasterInfo[var_110_0][iter_110_2] = {
					count = 0,
					receive = False,
					max = var_110_3
				}

def var_0_0.checkRemasterInfomation(arg_111_0):
	if not arg_111_0.checkRemaster:
		arg_111_0.checkRemaster = True

		arg_111_0.sendNotification(GAME.CHAPTER_REMASTER_INFO_REQUEST)

def var_0_0.addRemasterPassCount(arg_112_0, arg_112_1):
	if not arg_112_0.remasterInfo[arg_112_1]:
		return

	local var_112_0

	for iter_112_0, iter_112_1 in pairs(arg_112_0.remasterInfo[arg_112_1]):
		if iter_112_1.count < iter_112_1.max:
			iter_112_1.count = iter_112_1.count + 1
			var_112_0 = True

	if var_112_0:
		arg_112_0.sendNotification(var_0_0.CHAPTER_REMASTER_INFO_UPDATED)

def var_0_0.markRemasterPassReceive(arg_113_0, arg_113_1, arg_113_2):
	local var_113_0 = arg_113_0.remasterInfo[arg_113_1][arg_113_2]

	if not arg_113_0.remasterInfo[arg_113_1][arg_113_2]:
		return

	if not var_113_0.receive:
		var_113_0.receive = True

		arg_113_0.sendNotification(var_0_0.CHAPTER_REMASTER_INFO_UPDATED)

def var_0_0.anyRemasterAwardCanReceive(arg_114_0):
	for iter_114_0, iter_114_1 in pairs(arg_114_0.remasterInfo):
		for iter_114_2, iter_114_3 in pairs(iter_114_1):
			if not iter_114_3.receive and iter_114_3.count >= iter_114_3.max:
				return True

	return False

def var_0_0.AddActBossRewards(arg_115_0, arg_115_1):
	arg_115_0.actBossItems = arg_115_0.actBossItems or {}

	table.insertto(arg_115_0.actBossItems, arg_115_1)

def var_0_0.PopActBossRewards(arg_116_0):
	local var_116_0 = arg_116_0.actBossItems or {}

	arg_116_0.actBossItems = None

	return var_116_0

def var_0_0.AddBossSingleRewards(arg_117_0, arg_117_1):
	arg_117_0.bossSingleItems = arg_117_0.bossSingleItems or {}

	table.insertto(arg_117_0.bossSingleItems, arg_117_1)

def var_0_0.PopBossSingleRewards(arg_118_0):
	local var_118_0 = arg_118_0.bossSingleItems or {}

	arg_118_0.bossSingleItems = None

	return var_118_0

def var_0_0.WriteBackOnExitBattleResult(arg_119_0):
	local var_119_0 = arg_119_0.getActiveChapter()

	if var_119_0:
		if var_119_0.existOni():
			var_119_0.clearSubmarineFleet()
			arg_119_0.updateChapter(var_119_0)
		elif var_119_0.isPlayingWithBombEnemy():
			var_119_0.fleets = {
				var_119_0.fleet
			}
			var_119_0.findex = 1

			arg_119_0.updateChapter(var_119_0)

def var_0_0.GetContinuousData(arg_120_0, arg_120_1):
	return arg_120_0.continuousData[arg_120_1]

def var_0_0.InitContinuousTime(arg_121_0, arg_121_1, arg_121_2):
	local var_121_0 = ContinuousOperationRuntimeData.New({
		system = arg_121_1,
		totalBattleTime = arg_121_2,
		battleTime = arg_121_2
	})

	arg_121_0.continuousData[arg_121_1] = var_121_0

def var_0_0.StopContinuousOperation(arg_122_0, arg_122_1, arg_122_2):
	local var_122_0 = arg_122_0.GetContinuousData(arg_122_1)

	if not var_122_0 or not var_122_0.IsActive():
		return

	if arg_122_2 == ChapterConst.AUTOFIGHT_STOP_REASON.MANUAL and arg_122_1 == SYSTEM_SCENARIO:
		pg.TipsMgr.GetInstance().ShowTips(i18n("multiple_sorties_stop"))

	var_122_0.Stop(arg_122_2)

def var_0_0.PopContinuousData(arg_123_0, arg_123_1):
	local var_123_0 = arg_123_0.continuousData[arg_123_1]

	arg_123_0.continuousData[arg_123_1] = None

	return var_123_0

def var_0_0.SetLastFleetIndex(arg_124_0, arg_124_1, arg_124_2):
	if arg_124_2 and arg_124_0.lastFleetIndex:
		return

	arg_124_0.lastFleetIndex = arg_124_1

def var_0_0.GetLastFleetIndex(arg_125_0):
	return arg_125_0.lastFleetIndex

return var_0_0
