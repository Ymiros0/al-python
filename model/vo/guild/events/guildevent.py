local var_0_0 = class("GuildEvent", import("...BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.active = False
	arg_1_0.startTime = 0
	arg_1_0.clueCount = 0
	arg_1_0.missions = {}
	arg_1_0.boss = None
	arg_1_0.durTime = pg.guildset.operation_duration_time.key_value

def var_0_0.bindConfigTable(arg_2_0):
	return pg.guild_operation_template

def var_0_0.GetConsume(arg_3_0):
	return arg_3_0.getConfig("consume")

def var_0_0.Active(arg_4_0, arg_4_1):
	arg_4_0.Deactivate()

	arg_4_0.startTime = arg_4_1.start_time
	arg_4_0.endTime = arg_4_0.durTime + arg_4_0.startTime
	arg_4_0.clueCount = arg_4_1.clue_count
	arg_4_0.joinCnt = arg_4_1.join_times
	arg_4_0.isParticipant = arg_4_1.is_participant

	local var_4_0 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_1.perfs):
		var_4_0[iter_4_1.event_id] = iter_4_1.index

	local var_4_1 = {}

	for iter_4_2, iter_4_3 in ipairs(arg_4_1.formation_time):
		var_4_1[iter_4_3.key] = iter_4_3.value

	local var_4_2 = 0

	local function var_4_3(arg_5_0)
		local var_5_0 = GuildMission.New(arg_5_0)
		local var_5_1 = var_5_0.GetPosition()

		if var_5_1 > var_4_2:
			var_4_2 = var_5_1

		if not arg_4_0.missions[var_5_1]:
			arg_4_0.missions[var_5_1] = {}

		if var_4_0[var_5_0.id]:
			var_5_0.UpdateNodeAnimFlagIndex(var_4_0[var_5_0.id])

		if var_4_1[var_5_0.id]:
			var_5_0.UpdateFormationTime(var_4_1[var_5_0.id])

		table.insert(arg_4_0.missions[var_5_1], var_5_0)

	for iter_4_4, iter_4_5 in ipairs(arg_4_1.base_events):
		var_4_3(iter_4_5)

	for iter_4_6, iter_4_7 in ipairs(arg_4_1.completed_events):
		var_4_3(GuildMission.CompleteData2FullData(iter_4_7))

	arg_4_0.boss = GuildBossMission.New(var_4_2 + 1, arg_4_1.daily_count, arg_4_1.fleets)

	if arg_4_1.boss_event and arg_4_1.boss_event.boss_id != 0:
		arg_4_0.boss.Flush(arg_4_1.boss_event)

	arg_4_0.active = True

def var_0_0.IsParticipant(arg_6_0):
	return arg_6_0.isParticipant > 0

def var_0_0.GetJoinCnt(arg_7_0):
	return arg_7_0.joinCnt

def var_0_0.IncreaseJoinCnt(arg_8_0):
	arg_8_0.isParticipant = 1

	if arg_8_0.joinCnt < arg_8_0.GetMaxJoinCnt():
		arg_8_0.joinCnt = arg_8_0.joinCnt + 1
	else
		getProxy(GuildProxy).getRawData().ReduceExtraBattleCnt(1)

def var_0_0.GetExtraJoinCnt(arg_9_0):
	return getProxy(GuildProxy).getRawData().GetExtraBattleCnt()

def var_0_0.IsLimitedJoin(arg_10_0):
	local var_10_0 = arg_10_0.GetJoinCnt()
	local var_10_1 = arg_10_0.GetMaxJoinCnt()
	local var_10_2 = arg_10_0.GetExtraJoinCnt()

	return not (var_10_0 < var_10_1 or var_10_2 > 0)

def var_0_0.GetMaxJoinCnt(arg_11_0):
	return pg.guildset.efficiency_param_times.key_value

def var_0_0.GetBossMission(arg_12_0):
	return arg_12_0.boss

def var_0_0.GetMissions(arg_13_0):
	return arg_13_0.missions

def var_0_0.Deactivate(arg_14_0):
	arg_14_0.startTime = 0
	arg_14_0.clueCount = 0
	arg_14_0.missions = {}
	arg_14_0.boss = None
	arg_14_0.active = False
	arg_14_0.isParticipant = 0

def var_0_0.IsExpired(arg_15_0):
	return pg.TimeMgr.GetInstance().GetServerTime() >= arg_15_0.endTime

def var_0_0.IsActive(arg_16_0):
	return arg_16_0.active == True

def var_0_0.GetDesc(arg_17_0):
	return arg_17_0.getConfig("profile")

def var_0_0.GetName(arg_18_0):
	return arg_18_0.getConfig("name")

def var_0_0.GetScaleDesc(arg_19_0):
	return arg_19_0.getConfig("scale")

def var_0_0.GetDisplayMission(arg_20_0):
	return arg_20_0.getConfig("event_type_list")

def var_0_0.GetDisplayAward(arg_21_0):
	return arg_21_0.getConfig("award_display")

def var_0_0.IsUnlock(arg_22_0, arg_22_1):
	return arg_22_1 >= arg_22_0.getConfig("unlock_guild_level")

def var_0_0.GetTheme(arg_23_0):
	return arg_23_0.getConfig("theme")

def var_0_0.GetJoinShips(arg_24_0):
	local var_24_0 = {}

	for iter_24_0, iter_24_1 in ipairs(arg_24_0.missions):
		for iter_24_2, iter_24_3 in ipairs(iter_24_1):
			if not iter_24_3.IsFinish():
				local var_24_1 = iter_24_3.GetMyShips()

				for iter_24_4, iter_24_5 in ipairs(var_24_1):
					table.insert(var_24_0, iter_24_5)

	return var_24_0

def var_0_0.GetMissionById(arg_25_0, arg_25_1):
	for iter_25_0, iter_25_1 in pairs(arg_25_0.missions):
		for iter_25_2, iter_25_3 in ipairs(iter_25_1):
			if iter_25_3.id == arg_25_1:
				return iter_25_3

	assert(False)

def var_0_0.GetJoinShipCnt(arg_26_0):
	local var_26_0 = 0

	for iter_26_0, iter_26_1 in pairs(arg_26_0.missions):
		for iter_26_2, iter_26_3 in ipairs(iter_26_1):
			var_26_0 = var_26_0 + iter_26_3.GetJoinCnt()

	return var_26_0

def var_0_0.GetBossShipIds(arg_27_0):
	local var_27_0 = {}

	if arg_27_0.boss and arg_27_0.boss.IsActive():
		local var_27_1 = arg_27_0.boss.GetMyShipIds()

		for iter_27_0, iter_27_1 in ipairs(var_27_1):
			table.insert(var_27_0, iter_27_1)

	return var_27_0

def var_0_0.GetMissionCnt(arg_28_0):
	local var_28_0 = 0

	for iter_28_0, iter_28_1 in pairs(arg_28_0.missions):
		for iter_28_2, iter_28_3 in ipairs(iter_28_1):
			var_28_0 = var_28_0 + 1

	return var_28_0

def var_0_0.GetMainMissionCntAndFinishCnt(arg_29_0):
	local var_29_0 = 0
	local var_29_1 = 0

	for iter_29_0, iter_29_1 in pairs(arg_29_0.missions):
		for iter_29_2, iter_29_3 in ipairs(iter_29_1):
			if iter_29_3.IsMain():
				var_29_0 = var_29_0 + 1

			if iter_29_3.IsMain() and iter_29_3.IsFinish():
				var_29_1 = var_29_1 + 1

	return var_29_0, var_29_1

def var_0_0.GetMissionFinishCnt(arg_30_0):
	local var_30_0 = 0

	for iter_30_0, iter_30_1 in pairs(arg_30_0.missions):
		for iter_30_2, iter_30_3 in ipairs(iter_30_1):
			if iter_30_3.IsFinish():
				var_30_0 = var_30_0 + 1

	return var_30_0

def var_0_0.GetCanFormationMisstions(arg_31_0):
	local function var_31_0(arg_32_0)
		if arg_32_0.IsFinish():
			return False

		local var_32_0 = arg_32_0.GetPosition()
		local var_32_1 = arg_31_0.missions[var_32_0 - 1]

		if var_32_1:
			for iter_32_0, iter_32_1 in pairs(var_32_1):
				if iter_32_1.IsMain() and iter_32_1.IsFinish():
					return True
		else
			return True

		return False

	local var_31_1 = {}

	for iter_31_0, iter_31_1 in pairs(arg_31_0.missions):
		for iter_31_2, iter_31_3 in ipairs(iter_31_1):
			if var_31_0(iter_31_3) and iter_31_3.CanFormation() and not iter_31_3.IsFinish():
				table.insert(var_31_1, iter_31_3)

	return var_31_1

def var_0_0.AnyMissionCanFormation(arg_33_0):
	return #arg_33_0.GetCanFormationMisstions() > 0

def var_0_0.AnyMissionFirstFleetCanFroamtion(arg_34_0):
	local var_34_0 = arg_34_0.GetCanFormationMisstions()
	local var_34_1 = _.detect(var_34_0, function(arg_35_0)
		return arg_35_0.FirstFleetCanFormation() or arg_35_0.IsFinish() and not arg_35_0.IsFinishedByServer())

	return var_34_1 != None, var_34_1

def var_0_0.GetUnlockMission(arg_36_0):
	local var_36_0 = 0

	for iter_36_0, iter_36_1 in pairs(arg_36_0.missions):
		for iter_36_2, iter_36_3 in ipairs(iter_36_1):
			if iter_36_3.IsMain() and (iter_36_3.IsFinishedByServer() or iter_36_3.IsFinish()):
				var_36_0 = iter_36_0

	local var_36_1 = arg_36_0.missions[var_36_0 + 1]

	for iter_36_4, iter_36_5 in ipairs(var_36_1 or {}):
		if iter_36_5.IsMain():
			return iter_36_5

	return None

def var_0_0.GetLeftTime(arg_37_0):
	local var_37_0 = pg.TimeMgr.GetInstance().GetServerTime()

	return arg_37_0.endTime - var_37_0

return var_0_0
