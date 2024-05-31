local var_0_0 = class("ColoringProxy", import(".NetProxy"))

def var_0_0.register(arg_1_0):
	arg_1_0.colorGroups = {}
	arg_1_0.colorItems = {}

def var_0_0.netUpdateData(arg_2_0, arg_2_1):
	arg_2_0.startTime = arg_2_1.start_time

	local var_2_0 = {}

	_.each(arg_2_1.award_list, function(arg_3_0)
		var_2_0[arg_3_0.id] = _.map(arg_3_0.award_list, function(arg_4_0)
			return {
				type = arg_4_0.type,
				id = arg_4_0.id,
				count = arg_4_0.number
			}))

	local var_2_1 = {}
	local var_2_2 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_COLORING_ALPHA)

	if var_2_2 and not var_2_2.isEnd():
		var_2_1 = var_2_2.getConfig("config_data")

	arg_2_0.colorGroups = {}

	_.each(var_2_1, function(arg_5_0)
		local var_5_0 = arg_5_0[1]
		local var_5_1 = arg_5_0[2]
		local var_5_2 = ColorGroup.New(var_5_0)

		if var_5_2.canBeCustomised() and COLORING_ACTIVITY_CUSTOMIZED_BANNED:
			return

		var_5_2.setHasAward(var_5_1 > 0)

		if var_5_0 == arg_2_1.id:
			_.each(arg_2_1.cell_list, function(arg_6_0)
				var_5_2.setFill(arg_6_0.row, arg_6_0.column, arg_6_0.color))

		local var_5_3 = var_2_0[var_5_0] or {}

		var_5_2.setDrops(var_5_3)

		if var_5_1 > 0 and #var_5_3 > 0:
			var_5_2.setState(ColorGroup.StateAchieved)
		elif var_5_0 < arg_2_1.id or var_5_2.isAllFill():
			var_5_2.setState(ColorGroup.StateFinish)

		table.insert(arg_2_0.colorGroups, var_5_2))

	local var_2_3 = 0

	for iter_2_0 = #arg_2_0.colorGroups, 1, -1:
		local var_2_4 = arg_2_0.colorGroups[iter_2_0].getState()

		if var_2_4 == ColorGroup.StateFinish or var_2_4 == ColorGroup.StateAchieved:
			var_2_3 = iter_2_0

			break

	for iter_2_1 = var_2_3 - 1, 1, -1:
		local var_2_5 = arg_2_0.colorGroups[iter_2_1]

		if not var_2_5.getState():
			var_2_5.setState(ColorGroup.StateFinish)

	if var_2_3 + 1 <= #arg_2_0.colorGroups:
		arg_2_0.colorGroups[var_2_3 + 1].setState(var_2_3 == 0 and ColorGroup.StateColoring or ColorGroup.StateLock)

	for iter_2_2 = var_2_3 + 2, #arg_2_0.colorGroups:
		local var_2_6 = arg_2_0.colorGroups[iter_2_2]

		if not var_2_6.getState():
			var_2_6.setState(ColorGroup.StateLock)

	arg_2_0.checkState()

	arg_2_0.colorItems = {}

	for iter_2_3, iter_2_4 in ipairs(arg_2_1.color_list):
		arg_2_0.colorItems[iter_2_4.id] = iter_2_4.number

def var_0_0.getColorItems(arg_7_0):
	return arg_7_0.colorItems

def var_0_0.getColorGroups(arg_8_0):
	return arg_8_0.colorGroups

def var_0_0.getColorGroup(arg_9_0, arg_9_1):
	return _.detect(arg_9_0.colorGroups, function(arg_10_0)
		return arg_10_0.id == arg_9_1)

def var_0_0.checkState(arg_11_0):
	local var_11_0 = False
	local var_11_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_COLORING_ALPHA)

	if var_11_1 and not var_11_1.isEnd():
		local var_11_2 = pg.TimeMgr.GetInstance()
		local var_11_3 = var_11_2.DiffDay(arg_11_0.startTime, var_11_2.GetServerTime()) + 1

		for iter_11_0, iter_11_1 in ipairs(arg_11_0.colorGroups):
			if iter_11_1.getState() == ColorGroup.StateColoring and iter_11_1.isAllFill():
				iter_11_1.setState(ColorGroup.StateFinish)

				var_11_0 = True

				break
			elif iter_11_0 < var_11_3 and iter_11_1.getState() == ColorGroup.StateAchieved:
				local var_11_4 = arg_11_0.colorGroups[iter_11_0 + 1]

				if var_11_4 and var_11_4.getState() == ColorGroup.StateLock:
					var_11_4.setState(ColorGroup.StateColoring)

					var_11_0 = True

					break

	return var_11_0

def var_0_0.CheckTodayTip(arg_12_0):
	local var_12_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_COLORING_ALPHA)

	if var_12_0 and not var_12_0.isEnd() and arg_12_0.startTime:
		local var_12_1 = pg.TimeMgr.GetInstance()
		local var_12_2 = math.min(var_12_1.DiffDay(arg_12_0.startTime, var_12_1.GetServerTime()) + 1, #arg_12_0.colorGroups)
		local var_12_3 = arg_12_0.GetViewedPage()

		for iter_12_0, iter_12_1 in ipairs(arg_12_0.colorGroups):
			if var_12_2 < iter_12_0:
				break

			if iter_12_1.getState() == ColorGroup.StateLock:
				break

			if iter_12_1.getState() != ColorGroup.StateAchieved and not iter_12_1.canBeCustomised():
				if var_12_3 < iter_12_0:
					return True

				if iter_12_1.getState() == ColorGroup.StateFinish or iter_12_1.HasEnoughItem2FillAll(arg_12_0.getColorItems()):
					return True

				break

def var_0_0.IsALLAchieve(arg_13_0):
	if #arg_13_0.colorGroups == 0:
		return False

	return _.all(arg_13_0.colorGroups, function(arg_14_0)
		return arg_14_0.canBeCustomised() or arg_14_0.getState() == ColorGroup.StateAchieved)

def var_0_0.GetViewedPage(arg_15_0):
	local var_15_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_COLORING_ALPHA)

	if not var_15_0 or var_15_0.isEnd():
		return 0

	local var_15_1 = getProxy(PlayerProxy).getRawData()

	return PlayerPrefs.GetInt("pixelDraw_maxPage_" .. var_15_0.id .. "_" .. var_15_1.id, 0)

def var_0_0.SetViewedPage(arg_16_0, arg_16_1):
	local var_16_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_COLORING_ALPHA)

	if not var_16_0 or var_16_0.isEnd():
		return

	if arg_16_1 <= arg_16_0.GetViewedPage():
		return

	local var_16_1 = getProxy(PlayerProxy).getRawData()

	return PlayerPrefs.SetInt("pixelDraw_maxPage_" .. var_16_0.id .. "_" .. var_16_1.id, arg_16_1)

return var_0_0
