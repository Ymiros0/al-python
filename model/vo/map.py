local var_0_0 = class("Map", import(".BaseVO"))

var_0_0.INVALID = 0
var_0_0.SCENARIO = 1
var_0_0.ELITE = 2
var_0_0.EVENT = 3
var_0_0.ACTIVITY_EASY = 4
var_0_0.ACTIVITY_HARD = 5
var_0_0.ACT_EXTRA = 8
var_0_0.ESCORT = 9
var_0_0.SKIRMISH = 10
var_0_0.NORMAL_MAP = {
	var_0_0.INVALID,
	var_0_0.SCENARIO,
	var_0_0.ELITE,
	var_0_0.EVENT,
	var_0_0.ACTIVITY_EASY,
	var_0_0.ACTIVITY_HARD,
	var_0_0.ACT_EXTRA
}

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.configId = arg_1_1.id
	arg_1_0.id = arg_1_0.configId
	arg_1_0.chapterIds = arg_1_1.chapterIds

def var_0_0.bindConfigTable(arg_2_0):
	return pg.expedition_data_by_map

def var_0_0.isUnlock(arg_3_0):
	if getProxy(PlayerProxy).getRawData().level < arg_3_0.getConfig("level_limit"):
		return False, i18n("levelScene_chapter_unlock_tip", arg_3_0.getConfig("level_limit"))
	elif arg_3_0.isActivity():
		if arg_3_0.isRemaster():
			if arg_3_0.isAnyChapterUnlocked():
				return True
			else
				return False, i18n("battle_levelScene_lock")
		else
			local var_3_0 = getProxy(ActivityProxy).getActivityById(arg_3_0.getConfig("on_activity"))

			if not var_3_0 or var_3_0.isEnd():
				return False, i18n("common_activity_end")
			else
				local var_3_1, var_3_2 = arg_3_0.isAnyChapterUnlocked(True)

				if var_3_1:
					return True
				elif var_3_2:
					return False, i18n("battle_levelScene_close")
				elif ChapterConst.IsAtelierMap(arg_3_0) and arg_3_0.isHardMap():
					return False, i18n("battle_levelScene_ryza_lock")
				else
					return False, i18n("battle_levelScene_lock")
	elif arg_3_0.getMapType() == Map.SCENARIO:
		if arg_3_0.isAnyChapterUnlocked(False):
			return True
		else
			return False, i18n("battle_levelScene_lock")
	elif arg_3_0.getMapType() == Map.ELITE:
		if arg_3_0.isEliteEnabled():
			return True
		else
			return False, i18n("battle_levelScene_hard_lock")
	else
		return True

def var_0_0.setRemaster(arg_4_0, arg_4_1):
	arg_4_0.remasterId = arg_4_1

def var_0_0.isRemaster(arg_5_0):
	return arg_5_0.remasterId != None

def var_0_0.getRemaster(arg_6_0):
	return arg_6_0.remasterId

def var_0_0.getMapType(arg_7_0):
	return arg_7_0.getConfig("type")

def var_0_0.getMapTitleNumber(arg_8_0):
	return arg_8_0.getConfig("title")

def var_0_0.getBindMapId(arg_9_0):
	return arg_9_0.getConfig("bind_map")

def var_0_0.getBindMap(arg_10_0):
	return getProxy(ChapterProxy).getMapById(arg_10_0.getBindMapId())

def var_0_0.getChapters(arg_11_0):
	return _.filter(arg_11_0.GetChapterItems(), function(arg_12_0)
		return isa(arg_12_0, Chapter))

def var_0_0.GetChapterItems(arg_13_0):
	local var_13_0 = getProxy(ChapterProxy)

	return _.map(arg_13_0.GetChapterList(), function(arg_14_0)
		return var_13_0.GetChapterItemById(arg_14_0))

def var_0_0.getEscortConfig(arg_15_0):
	if arg_15_0.isEscort():
		return pg.escort_map_template[arg_15_0.id]

def var_0_0.getChapterTimeLimit(arg_16_0):
	if not arg_16_0.isActivity() or arg_16_0.isRemaster():
		return 0

	local var_16_0 = pg.TimeMgr.GetInstance()
	local var_16_1 = 0

	for iter_16_0, iter_16_1 in ipairs(arg_16_0.getChapters()):
		local var_16_2 = pg.activity_template[iter_16_1.GetBindActID()]

		if var_16_2 and var_16_2.time and #var_16_2.time == 3:
			local var_16_3 = var_16_0.parseTimeFromConfig(var_16_2.time[2]) - var_16_0.GetServerTime()

			if var_16_3 > 0:
				if var_16_1 == 0:
					var_16_1 = var_16_3
				else
					var_16_1 = math.min(var_16_1, var_16_3)

	return var_16_1

def var_0_0.isClear(arg_17_0):
	if arg_17_0.getMapType() == var_0_0.SCENARIO:
		return arg_17_0.isAllChaptersClear()
	elif arg_17_0.isActivity():
		return arg_17_0.isClearForActivity()
	else
		return True

def var_0_0.isClearForActivity(arg_18_0):
	local var_18_0 = arg_18_0.GetChapterItems()

	for iter_18_0, iter_18_1 in ipairs(var_18_0):
		if iter_18_0 > 1 and iter_18_1.id - var_18_0[iter_18_0 - 1].id > 1:
			break
		elif not iter_18_1.isClear():
			return False

	return True

def var_0_0.isEliteEnabled(arg_19_0):
	local var_19_0

	if arg_19_0.getMapType() == var_0_0.ELITE:
		var_19_0 = getProxy(ChapterProxy).getMapById(arg_19_0.getBindMapId())
	else
		var_19_0 = arg_19_0

	return var_19_0.isAllChaptersClear() and var_19_0.isAllChaptersAchieve()

def var_0_0.isAnyChapterUnlocked(arg_20_0, arg_20_1):
	local var_20_0 = False

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.GetChapterItems()):
		if iter_20_1.isUnlock():
			if not arg_20_1 or iter_20_1.inActTime():
				return True
			else
				var_20_0 = True

	return False, var_20_0

def var_0_0.isAnyChapterClear(arg_21_0):
	return underscore.any(arg_21_0.GetChapterItems(), function(arg_22_0)
		return arg_22_0.isClear())

def var_0_0.isAllChaptersClear(arg_23_0):
	for iter_23_0, iter_23_1 in ipairs(arg_23_0.GetChapterItems()):
		if not iter_23_1.isClear():
			return False

	return True

def var_0_0.isAllChaptersAchieve(arg_24_0):
	for iter_24_0, iter_24_1 in ipairs(arg_24_0.getChapters()):
		if not iter_24_1.isAllAchieve():
			return False

	return True

def var_0_0.getLastUnlockChapterName(arg_25_0):
	local var_25_0

	for iter_25_0, iter_25_1 in ipairs(arg_25_0.getChapters()):
		if not iter_25_1.isUnlock():
			break

		var_25_0 = iter_25_1

	return var_25_0.getConfig("chapter_name")

def var_0_0.GetChapterInProgress(arg_26_0):
	return underscore.detect(arg_26_0.GetChapterItems(), function(arg_27_0)
		return arg_27_0.isUnlock() and not arg_27_0.isClear())

def var_0_0.GetChapterList(arg_28_0):
	return arg_28_0.chapterIds

def var_0_0.GetRearChaptersOfRemaster(arg_29_0):
	if not arg_29_0 or arg_29_0 == 0:
		return

	local var_29_0 = getProxy(ChapterProxy)
	local var_29_1 = _.reduce(pg.re_map_template[arg_29_0].config_data, {}, function(arg_30_0, arg_30_1)
		local var_30_0 = var_29_0.getChapterById(arg_30_1, True).getConfig("map")
		local var_30_1 = var_29_0.getMapById(var_30_0).getConfig("type")

		arg_30_0[var_30_1] = arg_30_0[var_30_1] or {}

		table.insert(arg_30_0[var_30_1], arg_30_1)

		return arg_30_0)
	local var_29_2 = {}

	table.Foreach(var_29_1, function(arg_31_0, arg_31_1)
		local var_31_0 = _.reduce(arg_31_1, {}, function(arg_32_0, arg_32_1)
			arg_32_0[var_29_0.getChapterById(arg_32_1, True).getConfig("pre_chapter")] = arg_32_1

			return arg_32_0)
		local var_31_1 = _.filter(arg_31_1, function(arg_33_0)
			return not var_31_0[arg_33_0])

		table.insert(var_29_2, _.max(var_31_1)))

	return var_29_2

def var_0_0.isActivity(arg_34_0):
	local var_34_0 = arg_34_0.getMapType()

	if var_34_0 == Map.EVENT:
		return True, False
	elif var_34_0 == Map.ACTIVITY_EASY or var_34_0 == Map.ACTIVITY_HARD or var_34_0 == Map.ACT_EXTRA:
		return True, True
	else
		return False

def var_0_0.isHardMap(arg_35_0):
	local var_35_0 = arg_35_0.getMapType()

	return var_35_0 == Map.ELITE or var_35_0 == Map.ACTIVITY_HARD

def var_0_0.isActExtra(arg_36_0):
	return arg_36_0.getMapType() == Map.ACT_EXTRA

def var_0_0.isEscort(arg_37_0):
	return arg_37_0.getMapType() == Map.ESCORT

def var_0_0.isSkirmish(arg_38_0):
	return arg_38_0.getMapType() == Map.SKIRMISH

def var_0_0.isNormalMap(arg_39_0):
	return table.contains(Map.NORMAL_MAP, arg_39_0.getMapType())

def var_0_0.NeedRecordMap(arg_40_0):
	local var_40_0 = arg_40_0.getMapType()

	return var_40_0 == var_0_0.INVALID or var_40_0 == var_0_0.SCENARIO or var_40_0 == var_0_0.ELITE

return var_0_0
