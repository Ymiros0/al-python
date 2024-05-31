local var_0_0 = class("BuffHelper")

local function var_0_1(arg_1_0, arg_1_1)
	if arg_1_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUFF:
		if arg_1_1 and not arg_1_1.isEnd():
			local var_1_0 = arg_1_1.getConfig("config_id")
			local var_1_1 = {}

			if var_1_0 == 0:
				var_1_1 = arg_1_1.getConfig("config_data")
			else
				table.insert(var_1_1, var_1_0)

			for iter_1_0, iter_1_1 in ipairs(var_1_1):
				local var_1_2 = ActivityBuff.New(arg_1_1.id, iter_1_1)

				if var_1_2.isActivate():
					table.insert(arg_1_0, var_1_2)
	elif arg_1_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF or arg_1_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2:
		if arg_1_1 and not arg_1_1.isEnd():
			local var_1_3 = arg_1_1.GetBuildingIds()

			for iter_1_2, iter_1_3 in pairs(var_1_3):
				local var_1_4 = pg.activity_event_building[iter_1_3]

				if var_1_4:
					_.each(var_1_4.buff, function(arg_2_0)
						local var_2_0 = ActivityBuff.New(arg_1_1.id, arg_2_0)

						if var_2_0.isActivate():
							table.insert(arg_1_0, var_2_0))

			if arg_1_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2:
				local var_1_5 = arg_1_1.GetSceneBuildingId()

				if var_1_5 > 0:
					local var_1_6 = pg.activity_event_building[var_1_5]

					if var_1_6:
						_.each(var_1_6.buff, function(arg_3_0)
							local var_3_0 = ActivityBuff.New(arg_1_1.id, arg_3_0)

							if var_3_0.isActivate():
								table.insert(arg_1_0, var_3_0))
	elif arg_1_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_PT_BUFF:
		if arg_1_1:
			local var_1_7 = ActivityPtData.New(arg_1_1)

			if not arg_1_1.isEnd() and var_1_7.isInBuffTime():
				local var_1_8 = arg_1_1.data3_list

				for iter_1_4, iter_1_5 in pairs(var_1_8):
					table.insert(arg_1_0, ActivityBuff.New(arg_1_1.id, iter_1_5))
	elif arg_1_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_ATELIER_LINK and arg_1_1:
		local var_1_9 = arg_1_1.GetSlots()

		for iter_1_6, iter_1_7 in ipairs(var_1_9):
			local var_1_10 = iter_1_7[1]
			local var_1_11 = iter_1_7[2]

			if var_1_10 > 0 and var_1_11 > 0:
				table.insert(arg_1_0, ActivityBuff.New(arg_1_1.id, AtelierMaterial.New({
					configId = var_1_10
				}).GetBuffs()[var_1_11]))

	for iter_1_8, iter_1_9 in pairs(arg_1_1.GetBuffList()):
		table.insert(arg_1_0, iter_1_9)

def var_0_0.GetAllBuff(arg_4_0):
	local var_4_0 = {}
	local var_4_1 = getProxy(PlayerProxy).getRawData()

	for iter_4_0, iter_4_1 in ipairs(var_4_1.GetBuffs()):
		table.insert(var_4_0, CommonBuff.New(iter_4_1))

	local var_4_2 = getProxy(ActivityProxy).getRawData()

	for iter_4_2, iter_4_3 in pairs(var_4_2):
		if (function()
			if arg_4_0 and arg_4_0.system and arg_4_0.system == SYSTEM_SCENARIO and iter_4_3.getConfig("type") == ActivityConst.ACTIVITY_TYPE_ATELIER_LINK:
				local var_5_0 = getProxy(ChapterProxy).getActiveChapter(True)
				local var_5_1 = var_5_0 and getProxy(ChapterProxy).getMapById(var_5_0.getConfig("map")) or None

				if var_5_1 and not AtelierActivity.IsActivityBuffMap(var_5_1):
					return False

			return True)():
			var_0_1(var_4_0, iter_4_3)

	return var_4_0

def var_0_0.GetBackYardExpBuffs():
	local var_6_0 = {}
	local var_6_1 = var_0_0.GetAllBuff()

	for iter_6_0, iter_6_1 in ipairs(var_6_1):
		if iter_6_1.BackYardExpUsage():
			table.insert(var_6_0, iter_6_1)

	return var_6_0

def var_0_0.GetShipModExpBuff():
	return getProxy(ActivityProxy).getShipModExpActivity()

def var_0_0.GetBackYardPlayerBuffs():
	local var_8_0 = {}
	local var_8_1 = getProxy(PlayerProxy).getRawData()

	for iter_8_0, iter_8_1 in ipairs(var_8_1.GetBuffs()):
		local var_8_2 = CommonBuff.New(iter_8_1)

		if var_8_2.BackYardExpUsage():
			table.insert(var_8_0, var_8_2)

	return var_8_0

def var_0_0.GetBattleBuffs(arg_9_0):
	local var_9_0 = {}
	local var_9_1 = var_0_0.GetAllBuff({
		system = arg_9_0
	})

	for iter_9_0, iter_9_1 in ipairs(var_9_1):
		if iter_9_1.BattleUsage():
			table.insert(var_9_0, iter_9_1)

	return var_9_0

def var_0_0.GetBuffsByActivityType(arg_10_0):
	local var_10_0 = {}
	local var_10_1 = getProxy(ActivityProxy).getActivitiesByType(arg_10_0)

	_.each(var_10_1, function(arg_11_0)
		var_0_1(var_10_0, arg_11_0))

	return var_10_0

def var_0_0.GetBuffsForMainUI():
	local var_12_0 = getProxy(ActivityProxy)
	local var_12_1 = var_0_0.GetBuffsByActivityType(ActivityConst.ACTIVITY_TYPE_BUFF)

	for iter_12_0 = #var_12_1, 1, -1:
		if not var_12_1[iter_12_0].checkShow():
			table.remove(var_12_1, iter_12_0)

	local var_12_2 = var_12_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_MINIGAME)

	if var_12_2 and not var_12_2.isEnd():
		local var_12_3 = var_12_2.getConfig("config_client").bufflist
		local var_12_4 = getProxy(PlayerProxy).getRawData()

		for iter_12_1, iter_12_2 in pairs(var_12_4.buff_list):
			if pg.TimeMgr.GetInstance().GetServerTime() < iter_12_2.timestamp and table.contains(var_12_3, iter_12_2.id):
				local var_12_5 = ActivityBuff.New(var_12_2.id, iter_12_2.id, iter_12_2.timestamp)

				if var_12_5.checkShow():
					table.insert(var_12_1, var_12_5)

	local var_12_6 = getProxy(MiniGameProxy).GetMiniGameDataByType(MiniGameConst.MG_TYPE_3)

	if var_12_6:
		local var_12_7 = getProxy(PlayerProxy).getRawData()
		local var_12_8 = var_12_6.getConfig("config_data")[2]
		local var_12_9

		for iter_12_3, iter_12_4 in ipairs(var_12_7.buff_list):
			if table.indexof(var_12_8, iter_12_4.id, 1):
				if pg.TimeMgr.GetInstance().GetServerTime() < iter_12_4.timestamp:
					local var_12_10 = var_12_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_MINIGAME)
					local var_12_11 = ActivityBuff.New(var_12_10.id, iter_12_4.id, iter_12_4.timestamp)

					if var_12_11.checkShow():
						table.insert(var_12_1, var_12_11)

				break

	local var_12_12 = getProxy(MiniGameProxy).GetMiniGameDataByType(MiniGameConst.MG_TYPE_5)

	if var_12_12:
		local var_12_13 = getProxy(PlayerProxy).getRawData()
		local var_12_14 = var_12_12.getConfig("config_data")[2]
		local var_12_15

		for iter_12_5, iter_12_6 in ipairs(var_12_13.buff_list):
			if table.indexof(var_12_14, iter_12_6.id, 1):
				if pg.TimeMgr.GetInstance().GetServerTime() < iter_12_6.timestamp:
					local var_12_16 = var_12_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_MINIGAME)
					local var_12_17 = ActivityBuff.New(var_12_16.id, iter_12_6.id, iter_12_6.timestamp)

					if var_12_17.checkShow():
						table.insert(var_12_1, var_12_17)

				break

	return var_12_1

return var_0_0
