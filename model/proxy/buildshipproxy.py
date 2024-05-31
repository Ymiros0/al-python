local var_0_0 = class("BuildShipProxy", import(".NetProxy"))

var_0_0.ADDED = "BuildShipProxy ADDED"
var_0_0.TIMEUP = "BuildShipProxy TIMEUP"
var_0_0.UPDATED = "BuildShipProxy UPDATED"
var_0_0.REMOVED = "BuildShipProxy REMOVED"
var_0_0.DRAW_COUNT_UPDATE = "BuildShipProxy DRAW_COUNT_UPDATE"
var_0_0.REGULAR_BUILD_POOL_COUNT_UPDATE = "BuildShipProxy.REGULAR_BUILD_POOL_COUNT_UPDATE"

def var_0_0.register(arg_1_0):
	arg_1_0.on(12024, function(arg_2_0)
		arg_1_0.data = {}
		arg_1_0.workCount = arg_2_0.worklist_count
		arg_1_0.drawCount1 = arg_2_0.draw_count_1
		arg_1_0.drawCount10 = arg_2_0.draw_count_10

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.worklist_list):
			local var_2_0 = BuildShip.New(iter_2_1)

			var_2_0.setId(iter_2_0)
			table.insert(arg_1_0.data, var_2_0)

		arg_1_0.setBuildShipState()

		arg_1_0.regularExchangeCount = arg_2_0.exchange_count)

def var_0_0.GetPools(arg_3_0):
	local var_3_0 = {}
	local var_3_1 = getProxy(ActivityProxy)

	for iter_3_0, iter_3_1 in ipairs(var_3_1.getActivitiesByTypes({
		ActivityConst.ACTIVITY_TYPE_BUILDSHIP_1,
		ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD
	})):
		local var_3_2 = {}

		table.insert(var_3_2, function(arg_4_0)
			if iter_3_1 and not iter_3_1.isEnd():
				arg_4_0())
		table.insert(var_3_2, function(arg_5_0)
			local var_5_0 = pg.ship_data_create_exchange[iter_3_1.id] or {}

			if iter_3_1.getConfig("type") != ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD or iter_3_1.data2 < (var_5_0.exchange_available_times or 0):
				arg_5_0())
		seriesAsync(var_3_2, function()
			table.insert(var_3_0, BuildShipActivityPool.New({
				activityId = iter_3_1.id,
				id = iter_3_1.getConfig("config_id"),
				mark = BuildShipPool.BUILD_POOL_MARK_NEW
			})))

	table.insert(var_3_0, BuildShipPool.New({
		id = 2,
		mark = BuildShipPool.BUILD_POOL_MARK_LIGHT
	}))
	table.insert(var_3_0, BuildShipPool.New({
		id = 3,
		mark = BuildShipPool.BUILD_POOL_MARK_HEAVY
	}))
	table.insert(var_3_0, BuildShipPool.New({
		id = 1,
		mark = BuildShipPool.BUILD_POOL_MARK_SPECIAL
	}))

	return var_3_0

def var_0_0.GetPoolsWithoutNewServer(arg_7_0):
	local var_7_0 = arg_7_0.GetPools()

	return _.select(var_7_0, function(arg_8_0)
		return not (arg_8_0.IsActivity() and arg_8_0.IsNewServerBuild()))

def var_0_0.setBuildShipState(arg_9_0):
	arg_9_0.removeBuildTimer()

	arg_9_0.buildIndex = 0
	arg_9_0.buildTimers = {}

	local var_9_0 = 0

	for iter_9_0, iter_9_1 in ipairs(arg_9_0.data or {}):
		if var_9_0 == arg_9_0.getMaxWorkCount():
			break

		if not iter_9_1.isFinish():
			arg_9_0.buildIndex = iter_9_0
			var_9_0 = var_9_0 + 1

			arg_9_0.addBuildTimer()

		iter_9_1.state = iter_9_1.isFinish() and BuildShip.FINISH or BuildShip.ACTIVE

def var_0_0.getNextBuildShip(arg_10_0):
	local var_10_0
	local var_10_1 = arg_10_0.data[arg_10_0.buildIndex + 1]

	if var_10_1 and var_10_1.state == BuildShip.INACTIVE:
		arg_10_0.buildIndex = arg_10_0.buildIndex + 1
		var_10_0 = var_10_1

	return var_10_0

def var_0_0.activeNextBuild(arg_11_0):
	local var_11_0 = arg_11_0.getNextBuildShip()

	if var_11_0:
		var_11_0.active()
		arg_11_0.updateBuildShip(arg_11_0.buildIndex, var_11_0)
		arg_11_0.addBuildTimer()

def var_0_0.addBuildTimer(arg_12_0):
	local var_12_0 = arg_12_0.buildIndex

	if arg_12_0.buildTimers[var_12_0]:
		arg_12_0.buildTimers[var_12_0].Stop()

		arg_12_0.buildTimers[var_12_0] = None

	local function var_12_1()
		arg_12_0.activeNextBuild()
		arg_12_0.data[var_12_0].finish()
		arg_12_0.data[var_12_0].display("- build finish -")
		arg_12_0.updateBuildShip(var_12_0, arg_12_0.data[var_12_0])

	local var_12_2 = arg_12_0.data[var_12_0].finishTime - pg.TimeMgr.GetInstance().GetServerTime()

	if var_12_2 > 0:
		arg_12_0.buildTimers[var_12_0] = Timer.New(function()
			arg_12_0.buildTimers[var_12_0].Stop()

			arg_12_0.buildTimers[var_12_0] = None

			var_12_1(), var_12_2, 1)

		arg_12_0.buildTimers[var_12_0].Start()
	else
		var_12_1()

def var_0_0.getMaxWorkCount(arg_15_0):
	return arg_15_0.workCount

def var_0_0.getBuildShipCount(arg_16_0):
	return table.getCount(arg_16_0.data)

def var_0_0.removeBuildTimer(arg_17_0):
	for iter_17_0, iter_17_1 in pairs(arg_17_0.buildTimers or {}):
		iter_17_1.Stop()

	arg_17_0.buildTimers = None

def var_0_0.remove(arg_18_0):
	arg_18_0.removeBuildTimer()

	if arg_18_0.exchangeItemTimer:
		arg_18_0.exchangeItemTimer.Stop()

		arg_18_0.exchangeItemTimer = None

def var_0_0.getBuildShip(arg_19_0, arg_19_1):
	return Clone(arg_19_0.data[arg_19_1])

def var_0_0.getFinishCount(arg_20_0):
	local var_20_0 = 0

	for iter_20_0, iter_20_1 in pairs(arg_20_0.data):
		if iter_20_1.state == BuildShip.FINISH:
			var_20_0 = var_20_0 + 1

	return var_20_0

def var_0_0.getNeedFinishCount(arg_21_0):
	return table.getCount(arg_21_0.data) - arg_21_0.getFinishCount()

def var_0_0.getActiveCount(arg_22_0):
	local var_22_0 = 0

	for iter_22_0, iter_22_1 in pairs(arg_22_0.data):
		if iter_22_1.state == BuildShip.ACTIVE:
			var_22_0 = var_22_0 + 1

	return var_22_0

def var_0_0.getFinishedIndex(arg_23_0):
	for iter_23_0, iter_23_1 in ipairs(arg_23_0.data):
		if iter_23_1.state == BuildShip.FINISH:
			return iter_23_0

def var_0_0.canBuildShip(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_0.getActiveCount()
	local var_24_1 = pg.ship_data_create_material[arg_24_1]
	local var_24_2 = getProxy(BagProxy).getItemById(var_24_1.use_item)

	if var_24_2 and var_24_2.count >= var_24_1.number_1:
		return getProxy(PlayerProxy).getData().gold >= var_24_1.use_gold and var_24_0 == 0

def var_0_0.getActiveOrFinishedCount(arg_25_0):
	local var_25_0 = 0

	for iter_25_0, iter_25_1 in pairs(arg_25_0.data):
		if iter_25_1.state == BuildShip.ACTIVE or iter_25_1.state == BuildShip.FINISH:
			var_25_0 = var_25_0 + 1

	return var_25_0

def var_0_0.getDrawCount(arg_26_0):
	return {
		drawCount1 = arg_26_0.drawCount1,
		drawCount10 = arg_26_0.drawCount10
	}

def var_0_0.increaseDrawCount(arg_27_0, arg_27_1):
	if arg_27_1 == 1:
		arg_27_0.drawCount1 = arg_27_0.drawCount1 + 1
	elif arg_27_1 == 10:
		arg_27_0.drawCount10 = arg_27_0.drawCount10 + 1

	arg_27_0.sendNotification(var_0_0.DRAW_COUNT_UPDATE, arg_27_0.getDrawCount())

def var_0_0.addBuildShip(arg_28_0, arg_28_1):
	assert(isa(arg_28_1, BuildShip), "should be an instance of BuildShip")
	table.insert(arg_28_0.data, arg_28_1)

	local var_28_0 = arg_28_0.getActiveCount()
	local var_28_1 = arg_28_0.getMaxWorkCount()

	if var_28_0 < var_28_1:
		arg_28_1.setState(BuildShip.ACTIVE)

		arg_28_0.buildIndex = #arg_28_0.data

		arg_28_0.addBuildTimer()
	elif var_28_0 == var_28_1:
		arg_28_1.setState(BuildShip.INACTIVE)
	else
		assert(False, "激活的建船数量大于最大数量")

	arg_28_0.sendNotification(var_0_0.ADDED, arg_28_1.clone())

def var_0_0.finishBuildShip(arg_29_0, arg_29_1):
	if arg_29_0.buildTimers[arg_29_1]:
		arg_29_0.buildTimers[arg_29_1].func()

def var_0_0.updateBuildShip(arg_30_0, arg_30_1, arg_30_2):
	assert(isa(arg_30_2, BuildShip), "should be an instance of BuildShip")

	arg_30_0.data[arg_30_1] = arg_30_2.clone()

	arg_30_0.sendNotification(var_0_0.UPDATED, {
		index = arg_30_1,
		buildShip = arg_30_2.clone()
	})

def var_0_0.removeBuildShipByIndex(arg_31_0, arg_31_1):
	local var_31_0 = arg_31_0.data[arg_31_1].clone()

	assert(var_31_0 != None, "buildShip should exist")

	arg_31_0.lastPoolType = arg_31_0.data[arg_31_1].type

	table.remove(arg_31_0.data, arg_31_1)
	arg_31_0.sendNotification(var_0_0.REMOVED, {
		index = arg_31_1,
		buildShip = var_31_0
	})

def var_0_0.getSkipBatchBuildFlag(arg_32_0):
	return arg_32_0.skipBatchFlag or False

def var_0_0.setSkipBatchBuildFlag(arg_33_0, arg_33_1):
	arg_33_0.skipBatchFlag = arg_33_1

def var_0_0.getLastBuildShipPoolType(arg_34_0):
	return arg_34_0.lastPoolType or 0

def var_0_0.getSupportShipCost(arg_35_0):
	return pg.gameset.supports_config.description[1]

def var_0_0.changeRegularExchangeCount(arg_36_0, arg_36_1):
	arg_36_0.regularExchangeCount = math.clamp(arg_36_0.regularExchangeCount + arg_36_1, 0, pg.ship_data_create_exchange[REGULAR_BUILD_POOL_EXCHANGE_ID].exchange_request)

	arg_36_0.sendNotification(var_0_0.REGULAR_BUILD_POOL_COUNT_UPDATE)

def var_0_0.getRegularExchangeCount(arg_37_0):
	return arg_37_0.regularExchangeCount

return var_0_0
