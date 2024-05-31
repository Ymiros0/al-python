local var_0_0 = class("Chapter", import(".BaseVO"))

var_0_0.SelectFleet = 1
var_0_0.CustomFleet = 2
var_0_0.CHAPTER_STATE = {
	i18n("level_chapter_state_high_risk"),
	i18n("level_chapter_state_risk"),
	i18n("level_chapter_state_low_risk"),
	i18n("level_chapter_state_safety")
}

def var_0_0.bindConfigTable(arg_1_0):
	return pg.chapter_template

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.configId = arg_2_1.id
	arg_2_0.id = arg_2_0.configId
	arg_2_0.active = False
	arg_2_0.progress = defaultValue(arg_2_1.progress, 0)
	arg_2_0.defeatCount = arg_2_1.defeat_count or 0
	arg_2_0.passCount = arg_2_1.pass_count or 0
	arg_2_0.todayDefeatCount = arg_2_1.today_defeat_count or 0

	local var_2_0 = {
		defaultValue(arg_2_1.kill_boss_count, 0),
		defaultValue(arg_2_1.kill_enemy_count, 0),
		defaultValue(arg_2_1.take_box_count, 0)
	}

	arg_2_0.achieves = {}

	for iter_2_0 = 1, 3:
		local var_2_1 = arg_2_0.getConfig("star_require_" .. iter_2_0)

		if var_2_1 > 0:
			table.insert(arg_2_0.achieves, {
				type = var_2_1,
				config = arg_2_0.getConfig("num_" .. iter_2_0),
				count = var_2_0[iter_2_0]
			})

	arg_2_0.dropShipIdList = {}
	arg_2_0.eliteFleetList = {
		{},
		{},
		{}
	}
	arg_2_0.eliteCommanderList = {
		{},
		{},
		{}
	}
	arg_2_0.supportFleet = {}
	arg_2_0.loopFlag = 0

def var_0_0.BuildEliteFleetList(arg_3_0):
	local var_3_0 = {
		{},
		{},
		{}
	}
	local var_3_1 = {
		{},
		{},
		{}
	}
	local var_3_2 = {
		{}
	}

	for iter_3_0, iter_3_1 in ipairs(arg_3_0 or {}):
		local var_3_3 = {}

		for iter_3_2, iter_3_3 in ipairs(iter_3_1.main_id):
			var_3_3[#var_3_3 + 1] = iter_3_3

		if iter_3_0 == 4:
			var_3_2[1] = var_3_3
		else
			var_3_0[iter_3_0] = var_3_3

		local var_3_4 = {}

		for iter_3_4, iter_3_5 in ipairs(iter_3_1.commanders):
			local var_3_5 = iter_3_5.id
			local var_3_6 = iter_3_5.pos

			if getProxy(CommanderProxy).getCommanderById(var_3_5) and Commander.canEquipToFleetList(var_3_1, iter_3_0, var_3_6, var_3_5):
				var_3_4[var_3_6] = var_3_5

		var_3_1[iter_3_0] = var_3_4

	return var_3_0, var_3_1, var_3_2

def var_0_0.getMaxCount(arg_4_0):
	local var_4_0 = arg_4_0.getConfig("risk_levels")

	if #var_4_0 == 0:
		return 0

	return var_4_0[1][1]

def var_0_0.hasMitigation(arg_5_0):
	if not LOCK_MITIGATION:
		return arg_5_0.getConfig("mitigation_level") > 0
	else
		return False

def var_0_0.getRemainPassCount(arg_6_0):
	local var_6_0 = arg_6_0.getMaxCount()

	return math.max(var_6_0 - arg_6_0.passCount, 0)

def var_0_0.getRiskLevel(arg_7_0):
	local var_7_0 = arg_7_0.getRemainPassCount()
	local var_7_1 = arg_7_0.getConfig("risk_levels")

	for iter_7_0, iter_7_1 in ipairs(var_7_1):
		if var_7_0 <= iter_7_1[1] and var_7_0 >= iter_7_1[2]:
			return iter_7_0

	assert(False, "index can not be None")

def var_0_0.getMitigationRate(arg_8_0):
	local var_8_0 = arg_8_0.getMaxCount()
	local var_8_1 = LOCK_MITIGATION and 0 or arg_8_0.getConfig("mitigation_rate")

	return math.min(arg_8_0.passCount, var_8_0) * var_8_1

def var_0_0.getRepressInfo(arg_9_0):
	return {
		repressMax = arg_9_0.getMaxCount(),
		repressCount = arg_9_0.passCount,
		repressReduce = arg_9_0.getMitigationRate(),
		repressLevel = LOCK_MITIGATION and 0 or arg_9_0.getRemainPassCount() > 0 and 0 or arg_9_0.getConfig("mitigation_level") or 0,
		repressEnemyHpRant = 1 - arg_9_0.getStageCell(arg_9_0.fleet.line.row, arg_9_0.fleet.line.column).data / 10000
	}

def var_0_0.getChapterState(arg_10_0):
	local var_10_0 = arg_10_0.getRiskLevel()

	assert(var_0_0.CHAPTER_STATE[var_10_0], "state desc is None")

	return var_0_0.CHAPTER_STATE[var_10_0]

def var_0_0.getPlayType(arg_11_0):
	return arg_11_0.getConfig("model")

def var_0_0.isTypeDefence(arg_12_0):
	return arg_12_0.getPlayType() == ChapterConst.TypeDefence

def var_0_0.IsSpChapter(arg_13_0):
	return getProxy(ChapterProxy).getMapById(arg_13_0.getConfig("map")).getMapType() == Map.ACT_EXTRA and arg_13_0.getPlayType() == ChapterConst.TypeRange

def var_0_0.getConfig(arg_14_0, arg_14_1):
	if arg_14_0.isLoop():
		local var_14_0 = pg.chapter_template_loop[arg_14_0.id]

		assert(var_14_0, "chapter_template_loop not exist. " .. arg_14_0.id)

		if var_14_0[arg_14_1] != None and var_14_0[arg_14_1] != "&&":
			return var_14_0[arg_14_1]

		if (arg_14_1 == "air_dominance" or arg_14_1 == "best_air_dominance") and var_14_0.air_dominance_loop_rate != None:
			local var_14_1 = arg_14_0.getConfigTable()
			local var_14_2 = var_14_0.air_dominance_loop_rate * 0.01

			return math.floor(var_14_1[arg_14_1] * var_14_2)

	return var_0_0.super.getConfig(arg_14_0, arg_14_1)

def var_0_0.existLoop(arg_15_0):
	return pg.chapter_template_loop[arg_15_0.id] != None

def var_0_0.canActivateLoop(arg_16_0):
	return arg_16_0.progress == 100

def var_0_0.isLoop(arg_17_0):
	return arg_17_0.loopFlag == 1

def var_0_0.existAmbush(arg_18_0):
	return arg_18_0.getConfig("is_ambush") == 1 or arg_18_0.getConfig("is_air_attack") == 1

def var_0_0.isUnlock(arg_19_0):
	return arg_19_0.IsCleanPrevChapter() and arg_19_0.IsCleanPrevStory()

def var_0_0.IsCleanPrevChapter(arg_20_0):
	local var_20_0 = arg_20_0.getConfig("pre_chapter")

	if var_20_0 == 0:
		return True

	return getProxy(ChapterProxy).GetChapterItemById(var_20_0).isClear()

def var_0_0.IsCleanPrevStory(arg_21_0):
	local var_21_0 = arg_21_0.getConfig("pre_story")

	if var_21_0 == 0:
		return True

	return getProxy(ChapterProxy).GetChapterItemById(var_21_0).isClear()

def var_0_0.isPlayerLVUnlock(arg_22_0):
	return getProxy(PlayerProxy).getRawData().level >= arg_22_0.getConfig("unlocklevel")

def var_0_0.isClear(arg_23_0):
	return arg_23_0.progress >= 100

def var_0_0.ifNeedHide(arg_24_0):
	if table.contains(pg.chapter_setting.all, arg_24_0.id) and pg.chapter_setting[arg_24_0.id].hide == 1:
		return arg_24_0.isClear()

def var_0_0.existAchieve(arg_25_0):
	return #arg_25_0.achieves > 0

def var_0_0.isAllAchieve(arg_26_0):
	return _.all(arg_26_0.achieves, function(arg_27_0)
		return ChapterConst.IsAchieved(arg_27_0))

def var_0_0.clearEliterFleetByIndex(arg_28_0, arg_28_1):
	if arg_28_1 > #arg_28_0.eliteFleetList:
		return

	arg_28_0.eliteFleetList[arg_28_1] = {}

def var_0_0.wrapEliteFleet(arg_29_0, arg_29_1):
	local var_29_0 = {}
	local var_29_1 = arg_29_1 > 2 and FleetType.Submarine or FleetType.Normal
	local var_29_2 = _.flatten(arg_29_0.getEliteFleetList()[arg_29_1])

	for iter_29_0, iter_29_1 in pairs(arg_29_0.getEliteFleetCommanders()[arg_29_1]):
		table.insert(var_29_0, {
			pos = iter_29_0,
			id = iter_29_1
		})

	return TypedFleet.New({
		id = arg_29_1,
		fleetType = var_29_1,
		ship_list = var_29_2,
		commanders = var_29_0
	})

def var_0_0.setEliteCommanders(arg_30_0, arg_30_1):
	arg_30_0.eliteCommanderList = arg_30_1

def var_0_0.getEliteFleetCommanders(arg_31_0):
	return arg_31_0.eliteCommanderList

def var_0_0.updateCommander(arg_32_0, arg_32_1, arg_32_2, arg_32_3):
	arg_32_0.eliteCommanderList[arg_32_1][arg_32_2] = arg_32_3

def var_0_0.getEliteFleetList(arg_33_0):
	arg_33_0.EliteShipTypeFilter()

	return arg_33_0.eliteFleetList

def var_0_0.setEliteFleetList(arg_34_0, arg_34_1):
	arg_34_0.eliteFleetList = arg_34_1

def var_0_0.IsEliteFleetLegal(arg_35_0):
	local var_35_0 = 0
	local var_35_1 = 0
	local var_35_2 = 0
	local var_35_3 = 0
	local var_35_4
	local var_35_5

	for iter_35_0 = 1, #arg_35_0.eliteFleetList:
		local var_35_6, var_35_7 = arg_35_0.singleEliteFleetVertify(iter_35_0)

		if not var_35_6:
			if not var_35_7:
				if iter_35_0 >= 3:
					var_35_2 = var_35_2 + 1
				else
					var_35_0 = var_35_0 + 1
			else
				var_35_4 = var_35_7
				var_35_5 = iter_35_0
		elif iter_35_0 >= 3:
			var_35_3 = var_35_3 + 1
		else
			var_35_1 = var_35_1 + 1

	if var_35_0 == 2:
		return False, i18n("elite_disable_no_fleet")
	elif var_35_1 == 0:
		return False, var_35_4
	elif var_35_2 + var_35_3 < arg_35_0.getConfig("submarine_num"):
		return False, var_35_4

	local var_35_8 = arg_35_0.IsPropertyLimitationSatisfy()
	local var_35_9 = 1

	for iter_35_1, iter_35_2 in ipairs(var_35_8):
		var_35_9 = var_35_9 * iter_35_2

	if var_35_9 != 1:
		return False, i18n("elite_disable_property_unsatisfied")

	return True, var_35_5

def var_0_0.IsPropertyLimitationSatisfy(arg_36_0):
	local var_36_0 = getProxy(BayProxy).getRawData()
	local var_36_1 = arg_36_0.getConfig("property_limitation")
	local var_36_2 = {}

	for iter_36_0, iter_36_1 in ipairs(var_36_1):
		var_36_2[iter_36_1[1]] = 0

	local var_36_3 = arg_36_0.getEliteFleetList()
	local var_36_4 = 0

	for iter_36_2 = 1, 2:
		if not arg_36_0.singleEliteFleetVertify(iter_36_2):
			-- block empty
		else
			local var_36_5 = {}
			local var_36_6 = {}

			for iter_36_3, iter_36_4 in ipairs(var_36_1):
				local var_36_7, var_36_8, var_36_9, var_36_10 = unpack(iter_36_4)

				if string.sub(var_36_7, 1, 5) == "fleet":
					var_36_5[var_36_7] = 0
					var_36_6[var_36_7] = var_36_10

			local var_36_11 = var_36_3[iter_36_2]

			for iter_36_5, iter_36_6 in ipairs(var_36_11):
				local var_36_12 = var_36_0[iter_36_6]

				var_36_4 = var_36_4 + 1

				local var_36_13 = intProperties(var_36_12.getProperties())

				for iter_36_7, iter_36_8 in pairs(var_36_2):
					if string.sub(iter_36_7, 1, 5) == "fleet":
						if iter_36_7 == "fleet_totle_level":
							var_36_5[iter_36_7] = var_36_5[iter_36_7] + var_36_12.level
					elif iter_36_7 == "level":
						var_36_2[iter_36_7] = iter_36_8 + var_36_12.level
					else
						var_36_2[iter_36_7] = iter_36_8 + var_36_13[iter_36_7]

			for iter_36_9, iter_36_10 in pairs(var_36_5):
				if iter_36_9 == "fleet_totle_level" and iter_36_10 > var_36_6[iter_36_9]:
					var_36_2[iter_36_9] = var_36_2[iter_36_9] + 1

	local var_36_14 = {}

	for iter_36_11, iter_36_12 in ipairs(var_36_1):
		local var_36_15, var_36_16, var_36_17 = unpack(iter_36_12)

		if var_36_15 == "level" and var_36_4 > 0:
			var_36_2[var_36_15] = math.ceil(var_36_2[var_36_15] / var_36_4)

		var_36_14[iter_36_11] = AttributeType.EliteConditionCompare(var_36_16, var_36_2[var_36_15], var_36_17) and 1 or 0

	return var_36_14, var_36_2

def var_0_0.GetNomralFleetMaxCount(arg_37_0):
	return arg_37_0.getConfig("group_num")

def var_0_0.GetSubmarineFleetMaxCount(arg_38_0):
	return arg_38_0.getConfig("submarine_num")

def var_0_0.GetSupportFleetMaxCount(arg_39_0):
	return arg_39_0.getConfig("support_group_num")

def var_0_0.EliteShipTypeFilter(arg_40_0):
	if arg_40_0.getConfig("type") == Chapter.SelectFleet:
		local var_40_0 = {
			1,
			2,
			3
		}

		for iter_40_0, iter_40_1 in ipairs(var_40_0):
			table.clear(arg_40_0.eliteFleetList[iter_40_1])
			table.clear(arg_40_0.eliteCommanderList[iter_40_1])
	else
		for iter_40_2 = arg_40_0.GetNomralFleetMaxCount() + 1, 2:
			table.clear(arg_40_0.eliteFleetList[iter_40_2])
			table.clear(arg_40_0.eliteCommanderList[iter_40_2])

		for iter_40_3 = arg_40_0.GetSubmarineFleetMaxCount() + 2 + 1, 3:
			table.clear(arg_40_0.eliteFleetList[iter_40_3])
			table.clear(arg_40_0.eliteCommanderList[iter_40_3])

	local var_40_1 = getProxy(BayProxy).getRawData()

	for iter_40_4, iter_40_5 in ipairs(arg_40_0.eliteFleetList):
		for iter_40_6 = #iter_40_5, 1, -1:
			if var_40_1[iter_40_5[iter_40_6]] == None:
				table.remove(iter_40_5, iter_40_6)

	local function var_40_2(arg_41_0, arg_41_1, arg_41_2)
		arg_41_1 = Clone(arg_41_1)

		ChapterProxy.SortRecommendLimitation(arg_41_1)

		for iter_41_0, iter_41_1 in ipairs(arg_41_2):
			local var_41_0
			local var_41_1 = var_40_1[iter_41_1].getShipType()

			for iter_41_2, iter_41_3 in ipairs(arg_41_1):
				if ShipType.ContainInLimitBundle(iter_41_3, var_41_1):
					var_41_0 = iter_41_2

					break

			if var_41_0:
				table.remove(arg_41_1, var_41_0)
			else
				table.removebyvalue(arg_41_0, iter_41_1)

	for iter_40_7, iter_40_8 in ipairs(arg_40_0.getConfig("limitation")):
		local var_40_3 = arg_40_0.eliteFleetList[iter_40_7]
		local var_40_4 = {}
		local var_40_5 = {}
		local var_40_6 = {}

		for iter_40_9, iter_40_10 in ipairs(var_40_3):
			local var_40_7 = var_40_1[iter_40_10].getTeamType()

			if var_40_7 == TeamType.Main:
				table.insert(var_40_4, iter_40_10)
			elif var_40_7 == TeamType.Vanguard:
				table.insert(var_40_5, iter_40_10)
			elif var_40_7 == TeamType.Submarine:
				table.insert(var_40_6, iter_40_10)

		var_40_2(var_40_3, iter_40_8[1], var_40_4)
		var_40_2(var_40_3, iter_40_8[2], var_40_5)
		var_40_2(var_40_3, {
			0,
			0,
			0
		}, var_40_6)

def var_0_0.singleEliteFleetVertify(arg_42_0, arg_42_1):
	local var_42_0 = getProxy(BayProxy).getRawData()
	local var_42_1 = arg_42_0.getEliteFleetList()[arg_42_1]

	if not var_42_1 or #var_42_1 == 0:
		return False

	if arg_42_1 >= 3:
		return True

	if arg_42_0.getConfig("type") != Chapter.CustomFleet:
		return True

	local var_42_2 = 0
	local var_42_3 = 0
	local var_42_4 = {}

	for iter_42_0, iter_42_1 in ipairs(var_42_1):
		local var_42_5 = var_42_0[iter_42_1]

		if var_42_5:
			if var_42_5.getFlag("inEvent"):
				return False, i18n("elite_disable_ship_escort")

			local var_42_6 = var_42_5.getTeamType()

			if var_42_6 == TeamType.Main:
				var_42_2 = var_42_2 + 1
			elif var_42_6 == TeamType.Vanguard:
				var_42_3 = var_42_3 + 1

			var_42_4[#var_42_4 + 1] = var_42_5.getShipType()

	if var_42_2 * var_42_3 == 0 and var_42_2 + var_42_3 != 0:
		return False

	local var_42_7 = checkExist(arg_42_0.getConfig("limitation"), {
		arg_42_1
	})
	local var_42_8 = 1

	for iter_42_2, iter_42_3 in ipairs(var_42_7 or {}):
		local var_42_9 = 0
		local var_42_10 = 0

		for iter_42_4, iter_42_5 in ipairs(iter_42_3):
			if iter_42_5 != 0:
				var_42_9 = var_42_9 + 1

				if underscore.any(var_42_4, function(arg_43_0)
					return ShipType.ContainInLimitBundle(iter_42_5, arg_43_0)):
					var_42_10 = 1

					break

		if var_42_9 == 0:
			var_42_10 = 1

		var_42_8 = var_42_8 * var_42_10

	if var_42_8 == 0:
		return False, i18n("elite_disable_formation_unsatisfied")

	return True

def var_0_0.ClearSupportFleetList(arg_44_0, arg_44_1):
	arg_44_0.supportFleet = {}

def var_0_0.setSupportFleetList(arg_45_0, arg_45_1):
	arg_45_0.supportFleet = arg_45_1[1]

def var_0_0.getSupportFleet(arg_46_0):
	arg_46_0.SupportShipTypeFilter()

	return arg_46_0.supportFleet

def var_0_0.SupportShipTypeFilter(arg_47_0):
	if arg_47_0.GetSupportFleetMaxCount() < 1:
		table.clear(arg_47_0.supportFleet)

	local var_47_0 = getProxy(BayProxy).getRawData()
	local var_47_1 = arg_47_0.supportFleet

	for iter_47_0 = #var_47_1, 1, -1:
		if var_47_0[var_47_1[iter_47_0]] == None:
			table.remove(var_47_1, iter_47_0)

def var_0_0.activeAlways(arg_48_0):
	if getProxy(ChapterProxy).getMapById(arg_48_0.getConfig("map")).isActivity():
		local var_48_0 = arg_48_0.GetBindActID()
		local var_48_1 = pg.activity_template[var_48_0]

		if type(var_48_1.config_client) == "table":
			local var_48_2 = var_48_1.config_client.prevs or {}

			return table.contains(var_48_2, arg_48_0.id)

	return False

def var_0_0.getPrevChapterName(arg_49_0):
	local var_49_0 = ""
	local var_49_1 = arg_49_0.getConfig("pre_chapter")

	if var_49_1 != 0:
		var_49_0 = arg_49_0.bindConfigTable()[var_49_1].chapter_name

	return var_49_0

def var_0_0.CanQuickPlay(arg_50_0):
	local var_50_0 = pg.chapter_setting[arg_50_0.id]

	return var_50_0 and var_50_0.expedite > 0

def var_0_0.GetQuickPlayFlag(arg_51_0):
	return PlayerPrefs.GetInt("chapter_quickPlay_flag_" .. arg_51_0.id, 0) == 1

def var_0_0.writeDrops(arg_52_0, arg_52_1):
	_.each(arg_52_1, function(arg_53_0)
		if arg_53_0.type == DROP_TYPE_SHIP and not table.contains(arg_52_0.dropShipIdList, arg_53_0.id):
			table.insert(arg_52_0.dropShipIdList, arg_53_0.id))

def var_0_0.UpdateDropShipList(arg_54_0, arg_54_1):
	for iter_54_0, iter_54_1 in ipairs(arg_54_1):
		if not table.contains(arg_54_0.dropShipIdList, iter_54_1):
			table.insert(arg_54_0.dropShipIdList, iter_54_1)

def var_0_0.GetDropShipList(arg_55_0):
	return arg_55_0.dropShipIdList

def var_0_0.getOniChapterInfo(arg_56_0):
	return pg.chapter_capture[arg_56_0.id]

def var_0_0.getBombChapterInfo(arg_57_0):
	return pg.chapter_boom[arg_57_0.id]

def var_0_0.getNpcShipByType(arg_58_0, arg_58_1):
	local var_58_0 = {}
	local var_58_1 = getProxy(TaskProxy)

	local function var_58_2(arg_59_0)
		if arg_59_0 == 0:
			return True

		local var_59_0 = var_58_1.getTaskVO(arg_59_0)

		return var_59_0 and not var_59_0.isFinish()

	for iter_58_0, iter_58_1 in ipairs(arg_58_0.getConfig("npc_data")):
		local var_58_3 = pg.npc_squad_template[iter_58_1]

		if not arg_58_1 or arg_58_1 == var_58_3.type and var_58_2(var_58_3.task_id):
			for iter_58_2, iter_58_3 in ipairs({
				"vanguard_list",
				"main_list"
			}):
				for iter_58_4, iter_58_5 in ipairs(var_58_3[iter_58_3]):
					table.insert(var_58_0, NpcShip.New({
						id = iter_58_5[1],
						configId = iter_58_5[1],
						level = iter_58_5[2]
					}))

	return var_58_0

def var_0_0.getTodayDefeatCount(arg_60_0):
	return getProxy(DailyLevelProxy).getChapterDefeatCount(arg_60_0.configId)

def var_0_0.isTriesLimit(arg_61_0):
	local var_61_0 = arg_61_0.getConfig("count")

	return var_61_0 and var_61_0 > 0

def var_0_0.updateTodayDefeatCount(arg_62_0):
	getProxy(DailyLevelProxy).updateChapterDefeatCount(arg_62_0.configId)

def var_0_0.enoughTimes2Start(arg_63_0):
	if arg_63_0.isTriesLimit():
		return arg_63_0.getTodayDefeatCount() < arg_63_0.getConfig("count")
	else
		return True

def var_0_0.GetRestDailyBonus(arg_64_0):
	local var_64_0 = 0

	if arg_64_0.IsRemaster():
		return var_64_0

	local var_64_1 = arg_64_0.getConfig("boss_expedition_id")

	for iter_64_0, iter_64_1 in ipairs(var_64_1):
		local var_64_2 = pg.expedition_activity_template[iter_64_1]

		var_64_0 = math.max(var_64_0, var_64_2 and var_64_2.bonus_time or 0)

	local var_64_3 = pg.chapter_defense[arg_64_0.id]

	if var_64_3:
		var_64_0 = math.max(var_64_0, var_64_3.bonus_time or 0)

	return (math.max(var_64_0 - arg_64_0.todayDefeatCount, 0))

def var_0_0.GetDailyBonusQuota(arg_65_0):
	return arg_65_0.GetRestDailyBonus() > 0

var_0_0.OPERATION_BUFF_TYPE_COST = "more_oil"
var_0_0.OPERATION_BUFF_TYPE_REWARD = "extra_drop"
var_0_0.OPERATION_BUFF_TYPE_EXP = "chapter_up"
var_0_0.OPERATION_BUFF_TYPE_DESC = "desc"

def var_0_0.GetSPOperationItemCacheKey(arg_66_0):
	return "specialOPItem_" .. arg_66_0

def var_0_0.GetSpItems(arg_67_0):
	local var_67_0 = {}
	local var_67_1 = getProxy(BagProxy).getItemsByType(Item.SPECIAL_OPERATION_TICKET)
	local var_67_2 = arg_67_0.getConfig("special_operation_list")

	if var_67_2 and #var_67_2 == 0:
		return var_67_0

	for iter_67_0, iter_67_1 in ipairs(pg.benefit_buff_template.all):
		local var_67_3 = pg.benefit_buff_template[iter_67_1]

		if var_67_3.benefit_type == Chapter.OPERATION_BUFF_TYPE_DESC and table.contains(var_67_2, var_67_3.id):
			local var_67_4 = tonumber(var_67_3.benefit_condition)

			for iter_67_2, iter_67_3 in ipairs(var_67_1):
				if var_67_4 == iter_67_3.configId:
					table.insert(var_67_0, iter_67_3)

					break

	return var_67_0

def var_0_0.GetSPBuffByItem(arg_68_0):
	for iter_68_0, iter_68_1 in ipairs(pg.benefit_buff_template.all):
		buffConfig = pg.benefit_buff_template[iter_68_1]

		if buffConfig.benefit_type == Chapter.OPERATION_BUFF_TYPE_DESC and tonumber(buffConfig.benefit_condition) == arg_68_0:
			return buffConfig.id

def var_0_0.GetActiveSPItemID(arg_69_0):
	local var_69_0 = Chapter.GetSPOperationItemCacheKey(arg_69_0.id)
	local var_69_1 = PlayerPrefs.GetInt(var_69_0, 0)

	if var_69_1 == 0:
		return 0

	if arg_69_0.GetRestDailyBonus() > 0:
		return 0

	local var_69_2 = arg_69_0.GetSpItems()

	if _.detect(var_69_2, function(arg_70_0)
		return arg_70_0.GetConfigID() == var_69_1):
		return var_69_1

	return 0

def var_0_0.GetLimitOilCost(arg_71_0, arg_71_1, arg_71_2):
	if not arg_71_0.isLoop():
		return 9999

	local var_71_0
	local var_71_1

	if arg_71_1:
		var_71_1 = 3
	else
		local var_71_2 = pg.expedition_data_template[arg_71_2]

		var_71_1 = (var_71_2.type == ChapterConst.ExpeditionTypeBoss or var_71_2.type == ChapterConst.ExpeditionTypeMulBoss) and 2 or 1

	return arg_71_0.getConfig("use_oil_limit")[var_71_1] or 9999

def var_0_0.IsRemaster(arg_72_0):
	local var_72_0 = getProxy(ChapterProxy).getMapById(arg_72_0.getConfig("map"))

	return var_72_0 and var_72_0.isRemaster()

def var_0_0.GetBindActID(arg_73_0):
	return arg_73_0.getConfig("act_id")

def var_0_0.GetMaxBattleCount(arg_74_0):
	local var_74_0 = 0
	local var_74_1 = getProxy(ChapterProxy).getMapById(arg_74_0.getConfig("map"))

	if var_74_1.getMapType() == Map.ELITE:
		var_74_0 = pg.gameset.hard_level_multiple_sorties_times.key_value
		var_74_0 = math.clamp(var_74_0, 0, getProxy(DailyLevelProxy).GetRestEliteCount())
	elif var_74_1.isRemaster():
		var_74_0 = pg.gameset.archives_level_multiple_sorties_times.key_value
		var_74_0 = math.clamp(var_74_0, 0, getProxy(ChapterProxy).remasterTickets)
	elif var_74_1.isActivity():
		var_74_0 = pg.gameset.activity_level_multiple_sorties_times.key_value
	else
		var_74_0 = pg.gameset.main_level_multiple_sorties_times.key_value

	if arg_74_0.isTriesLimit():
		local var_74_2 = arg_74_0.getConfig("count") - arg_74_0.getTodayDefeatCount()

		var_74_0 = math.clamp(var_74_0, 0, var_74_2)

	return var_74_0

return var_0_0
