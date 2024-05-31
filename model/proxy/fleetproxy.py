local var_0_0 = class("FleetProxy", import(".NetProxy"))

var_0_0.FLEET_ADDED = "fleet added"
var_0_0.FLEET_UPDATED = "fleet updated"
var_0_0.FLEET_RENAMED = "fleet renamed"
var_0_0.PVP_FLEET_ID = 101
var_0_0.CHALLENGE_FLEET_ID = 102
var_0_0.CHALLENGE_SUB_FLEET_ID = 103

def var_0_0.register(arg_1_0):
	arg_1_0.extraFleets = {}
	arg_1_0.activityFleetData = {}

	arg_1_0.on(12101, function(arg_2_0)
		arg_1_0.data = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.group_list):
			local var_2_0 = var_0_0.CreateFleet(iter_2_1)

			var_2_0.display("loaded")

			arg_1_0.data[var_2_0.id] = var_2_0

		for iter_2_2 = 1, FormationUI.MAX_FLEET_NUM:
			if not arg_1_0.data[iter_2_2]:
				arg_1_0.data[iter_2_2] = var_0_0.CreateFleet({
					name = "",
					id = iter_2_2,
					ship_list = {},
					commanders = {}
				})

		for iter_2_3, iter_2_4 in pairs({
			[var_0_0.PVP_FLEET_ID] = "",
			[var_0_0.CHALLENGE_FLEET_ID] = "",
			[var_0_0.CHALLENGE_SUB_FLEET_ID] = ""
		}):
			if not arg_1_0.data[iter_2_3]:
				arg_1_0.data[iter_2_3] = var_0_0.CreateFleet({
					id = iter_2_3,
					name = iter_2_4,
					ship_list = {},
					commanders = {}
				})

		for iter_2_5, iter_2_6 in ipairs({
			var_0_0.CHALLENGE_FLEET_ID,
			var_0_0.CHALLENGE_SUB_FLEET_ID
		}):
			arg_1_0.extraFleets[iter_2_6] = arg_1_0.data[iter_2_6]
			arg_1_0.data[iter_2_6] = None

		if LOCK_SUBMARINE:
			for iter_2_7, iter_2_8 in pairs(arg_1_0.data):
				if iter_2_8.id == 11 or iter_2_8.id == 12:
					arg_1_0.data[iter_2_7] = None

		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inFleet")
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inPvP")
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inChallenge"))
	arg_1_0.on(12106, function(arg_3_0)
		local var_3_0 = var_0_0.CreateFleet(arg_3_0.group)

		if arg_1_0.data[var_3_0.id]:
			arg_1_0.updateFleet(var_3_0)
		else
			arg_1_0.addFleet(var_3_0))

def var_0_0.CreateFleet(arg_4_0):
	local var_4_0 = arg_4_0.id
	local var_4_1 = CreateShell(arg_4_0)

	var_4_1.fleetType = FleetType.Normal

	if var_4_0 >= Fleet.REGULAR_FLEET_ID and var_4_0 < Fleet.REGULAR_FLEET_ID + Fleet.REGULAR_FLEET_NUMS:
		if var_4_0 == Fleet.REGULAR_FLEET_ID:
			var_4_1.saveLastShipFlag = True
	elif var_4_0 >= Fleet.SUBMARINE_FLEET_ID and var_4_0 < Fleet.SUBMARINE_FLEET_ID + Fleet.SUBMARINE_FLEET_NUMS:
		var_4_1.fleetType = FleetType.Submarine
	elif var_4_0 == FleetProxy.PVP_FLEET_ID:
		var_4_1.saveLastShipFlag = True
	elif var_4_0 == FleetProxy.CHALLENGE_FLEET_ID:
		-- block empty
	elif var_4_0 == FleetProxy.CHALLENGE_SUB_FLEET_ID:
		var_4_1.fleetType = FleetType.Submarine

	return (TypedFleet.New(var_4_1))

def var_0_0.addFleet(arg_5_0, arg_5_1):
	assert(isa(arg_5_1, Fleet), "should be an instance of Fleet")
	assert(arg_5_0.data[arg_5_1.id] == None, "fleet already exist, use updateFleet() instead")

	arg_5_0.data[arg_5_1.id] = arg_5_1.clone()

	arg_5_0.data[arg_5_1.id].display("added")
	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inFleet")
	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inPvP")
	arg_5_0.facade.sendNotification(var_0_0.FLEET_ADDED, arg_5_1.clone())

def var_0_0.updateFleet(arg_6_0, arg_6_1):
	assert(isa(arg_6_1, Fleet), "should be an instance of Fleet")

	if arg_6_0.data[arg_6_1.id] != None:
		arg_6_0.data[arg_6_1.id] = arg_6_1.clone()

		arg_6_0.data[arg_6_1.id].display("updated")
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inFleet")
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inPvP")
	elif arg_6_0.extraFleets[arg_6_1.id] != None:
		arg_6_0.extraFleets[arg_6_1.id] = arg_6_1

		arg_6_0.extraFleets[arg_6_1.id].display("updated")
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inChallenge")
	else
		assert(False, "fleet should exist")

	arg_6_0.facade.sendNotification(var_0_0.FLEET_UPDATED, arg_6_1.id)

def var_0_0.saveEdittingFleet(arg_7_0):
	if arg_7_0.editSrcCache == None:
		arg_7_0.editSrcCache = Clone(arg_7_0.data)

	if arg_7_0.EdittingFleet != None:
		arg_7_0.data[arg_7_0.EdittingFleet.id] = arg_7_0.EdittingFleet

		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inFleet")
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inPvP")

def var_0_0.commitEdittingFleet(arg_8_0, arg_8_1):
	local var_8_0 = {}

	if arg_8_0.EdittingFleet != None:
		table.insert(var_8_0, function(arg_9_0)
			arg_8_0.facade.sendNotification(GAME.UPDATE_FLEET, {
				fleet = arg_8_0.EdittingFleet,
				def callback:()
					arg_8_0.editSrcCache = None
					arg_8_0.EdittingFleet = None

					arg_9_0()
			}))

	seriesAsync(var_8_0, function()
		if arg_8_1:
			arg_8_1())

def var_0_0.abortEditting(arg_12_0):
	if arg_12_0.editSrcCache:
		arg_12_0.data = arg_12_0.editSrcCache
		arg_12_0.editSrcCache = None

	arg_12_0.EdittingFleet = None

def var_0_0.syncFleet(arg_13_0):
	for iter_13_0, iter_13_1 in ipairs(arg_13_0.data):
		arg_13_0.facade.sendNotification(GAME.UPDATE_FLEET, {
			fleet = iter_13_1
		})

def var_0_0.getCount(arg_14_0):
	return table.getCount(arg_14_0.data)

def var_0_0.getFleetById(arg_15_0, arg_15_1):
	if arg_15_0.data[arg_15_1] != None:
		return arg_15_0.data[arg_15_1].clone()

	if arg_15_0.extraFleets[arg_15_1]:
		return arg_15_0.extraFleets[arg_15_1]

	return None

def var_0_0.getAllShipIds(arg_16_0, arg_16_1):
	local var_16_0 = {}

	for iter_16_0, iter_16_1 in pairs(arg_16_0.data):
		if arg_16_1 and not iter_16_1.isRegularFleet():
			-- block empty
		else
			for iter_16_2, iter_16_3 in ipairs(iter_16_1.ships):
				table.insert(var_16_0, iter_16_3)

	return var_16_0

def var_0_0.getFirstFleetShipCount(arg_17_0):
	local var_17_0 = 0

	for iter_17_0, iter_17_1 in ipairs(arg_17_0.data[1].ships):
		var_17_0 = var_17_0 + 1

	return var_17_0

def var_0_0.GetRegularFleets(arg_18_0):
	local var_18_0 = {}

	for iter_18_0, iter_18_1 in pairs(arg_18_0.data):
		if iter_18_1.isRegularFleet():
			var_18_0[iter_18_0] = Clone(iter_18_1)

	return var_18_0

def var_0_0.inPvPFleet(arg_19_0, arg_19_1):
	if arg_19_0.data[FleetProxy.PVP_FLEET_ID].containShip(arg_19_1):
		return True

	return False

def var_0_0.GetRegularFleetByShip(arg_20_0, arg_20_1):
	assert(isa(arg_20_1, Ship), "should be an instance of Ship")

	for iter_20_0, iter_20_1 in pairs(arg_20_0.data):
		if iter_20_1.isRegularFleet() and iter_20_1.containShip(arg_20_1):
			return iter_20_1.clone()

	return None

def var_0_0.renameFleet(arg_21_0, arg_21_1, arg_21_2):
	local var_21_0 = arg_21_0.getFleetById(arg_21_1)

	assert(var_21_0 != None, "fleet should exist")

	var_21_0.name = arg_21_2

	arg_21_0.updateFleet(var_21_0)
	arg_21_0.facade.sendNotification(var_0_0.FLEET_RENAMED, var_21_0.clone())

def var_0_0.getCommandersInFleet(arg_22_0):
	local var_22_0 = {}

	for iter_22_0, iter_22_1 in pairs(arg_22_0.data):
		if iter_22_1.isRegularFleet():
			for iter_22_2, iter_22_3 in pairs(iter_22_1.getCommanders()):
				table.insert(var_22_0, iter_22_3.id)

	return var_22_0

def var_0_0.getCommanders(arg_23_0):
	local var_23_0 = {}

	for iter_23_0, iter_23_1 in pairs(arg_23_0.data):
		if iter_23_1.isRegularFleet():
			for iter_23_2, iter_23_3 in pairs(iter_23_1.getCommanders()):
				table.insert(var_23_0, {
					fleetId = iter_23_1.id,
					pos = iter_23_2,
					commanderId = iter_23_3.id
				})

	return var_23_0

def var_0_0.GetExtraCommanders(arg_24_0):
	local var_24_0 = {}

	for iter_24_0, iter_24_1 in pairs(arg_24_0.extraFleets):
		for iter_24_2, iter_24_3 in pairs(iter_24_1.getCommanders()):
			table.insert(var_24_0, {
				fleetId = iter_24_1.id,
				pos = iter_24_2,
				commanderId = iter_24_3.id
			})

	return var_24_0

def var_0_0.getActivityFleets(arg_25_0):
	return arg_25_0.activityFleetData

def var_0_0.addActivityFleet(arg_26_0, arg_26_1, arg_26_2):
	local var_26_0 = arg_26_1.id

	if not arg_26_0.activityFleetData[var_26_0]:
		arg_26_0.activityFleetData[var_26_0] = {}

	local var_26_1 = arg_26_0.activityFleetData[var_26_0]
	local var_26_2 = getProxy(BayProxy)
	local var_26_3
	local var_26_4

	local function var_26_5()
		if var_26_4:
			return var_26_4

		local var_27_0 = arg_26_1.GetActiveSeriesIds()

		var_26_4 = _.map(var_27_0, function(arg_28_0)
			return table.lastof(BossRushSeriesData.New({
				id = arg_28_0,
				actId = arg_26_1.id
			}).GetFleetIds()))

		return var_26_4

	local var_26_6 = pg.activity_template[var_26_0]

	for iter_26_0, iter_26_1 in ipairs(arg_26_2):
		local var_26_7 = CreateShell(iter_26_1)

		if var_26_6.type == ActivityConst.ACTIVITY_TYPE_BOSSRUSH:
			var_26_7.fleetType = table.contains(var_26_5(), iter_26_1.id) and FleetType.Submarine or FleetType.Normal
		elif var_26_6.type == ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2:
			var_26_7.fleetType = iter_26_1.id >= Fleet.SUBMARINE_FLEET_ID and FleetType.Submarine or FleetType.Normal
		elif var_26_6.type == ActivityConst.ACTIVITY_TYPE_BOSSSINGLE:
			var_26_7.fleetType = iter_26_1.id >= Fleet.SUBMARINE_FLEET_ID and FleetType.Submarine or FleetType.Normal
		else
			local var_26_8 = {
				id = iter_26_1.id
			}

			var_26_7.fleetType = Fleet.isSubmarineFleet(var_26_8) and FleetType.Submarine or FleetType.Normal

		local var_26_9 = TypedFleet.New(var_26_7)

		var_26_1[var_26_9.id] = var_26_9

		for iter_26_2, iter_26_3 in ipairs(iter_26_1.ship_list):
			if not var_26_2.RawGetShipById(iter_26_3):
				var_26_3 = True

				break

	if var_26_3:
		arg_26_0.commitActivityFleet(var_26_0)

	local var_26_10
	local var_26_11

	if var_26_6.type == ActivityConst.ACTIVITY_TYPE_CHALLENGE:
		var_26_10 = 2
		var_26_11 = 2
	elif var_26_6.type == ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2:
		var_26_10 = 0
		var_26_11 = 0
	elif var_26_6.type == ActivityConst.ACTIVITY_TYPE_BOSSRUSH:
		var_26_10 = 0
		var_26_11 = 0
	elif var_26_6.type == ActivityConst.ACTIVITY_TYPE_BOSSSINGLE:
		var_26_10 = 0
		var_26_11 = 0

	local var_26_12 = 0

	while var_26_12 < var_26_10:
		var_26_12 = var_26_12 + 1

		if var_26_1[var_26_12] == None:
			var_26_1[var_26_12] = TypedFleet.New({
				id = var_26_12,
				ship_list = {},
				fleetType = FleetType.Normal
			})

	local var_26_13 = 0

	while var_26_13 < var_26_11:
		local var_26_14 = Fleet.SUBMARINE_FLEET_ID + var_26_13

		if var_26_1[var_26_14] == None:
			var_26_1[var_26_14] = TypedFleet.New({
				id = var_26_14,
				ship_list = {},
				fleetType = FleetType.Submarine
			})

		var_26_13 = var_26_13 + 1

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inActivity")

def var_0_0.updateActivityFleet(arg_29_0, arg_29_1, arg_29_2, arg_29_3):
	arg_29_0.activityFleetData[arg_29_1][arg_29_2] = arg_29_3

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inActivity")

def var_0_0.commitActivityFleet(arg_30_0, arg_30_1):
	arg_30_0.editSrcCache = None
	arg_30_0.EdittingFleet = None

	arg_30_0.facade.sendNotification(GAME.EDIT_ACTIVITY_FLEET, {
		actID = arg_30_1,
		fleets = arg_30_0.activityFleetData[arg_30_1]
	})

def var_0_0.checkActivityFleet(arg_31_0, arg_31_1):
	local var_31_0 = arg_31_0.activityFleetData[arg_31_1]

	for iter_31_0, iter_31_1 in pairs(var_31_0):
		if iter_31_0 < Fleet.SUBMARINE_FLEET_ID and iter_31_1.isLegalToFight() == True:
			return True

	return False

def var_0_0.removeActivityFleetCommander(arg_32_0, arg_32_1):
	for iter_32_0, iter_32_1 in pairs(arg_32_0.activityFleetData):
		for iter_32_2, iter_32_3 in pairs(iter_32_1):
			local var_32_0 = False
			local var_32_1 = iter_32_3.GetRawCommanderIds()

			for iter_32_4, iter_32_5 in pairs(var_32_1):
				if arg_32_1 == iter_32_5:
					iter_32_3.updateCommanderByPos(iter_32_4, None)
					iter_32_3.updateCommanderSkills()
					arg_32_0.updateActivityFleet(iter_32_0, iter_32_2, iter_32_3)
					arg_32_0.commitActivityFleet(iter_32_0)

					var_32_0 = True

					break

			if var_32_0:
				break

def var_0_0.recommendActivityFleet(arg_33_0, arg_33_1, arg_33_2):
	local var_33_0 = arg_33_0.getActivityFleets()[arg_33_1][arg_33_2]
	local var_33_1 = getProxy(BayProxy)

	local function var_33_2(arg_34_0, arg_34_1)
		local var_34_0 = TeamType.GetShipTypeListFromTeam(arg_34_0)
		local var_34_1 = var_33_1.getActivityRecommendShips(var_34_0, var_33_0.ships, arg_34_1, arg_33_1)

		for iter_34_0, iter_34_1 in ipairs(var_34_1):
			var_33_0.insertShip(iter_34_1, None, arg_34_0)

	if arg_33_2 >= Fleet.SUBMARINE_FLEET_ID:
		if not var_33_0.isFull():
			var_33_2(TeamType.Submarine, TeamType.SubmarineMax - #var_33_0.subShips)
	else
		local var_33_3 = TeamType.VanguardMax - #var_33_0.vanguardShips
		local var_33_4 = TeamType.MainMax - #var_33_0.mainShips

		if var_33_3 > 0:
			var_33_2(TeamType.Vanguard, var_33_3)

		if var_33_4 > 0:
			var_33_2(TeamType.Main, var_33_4)

	arg_33_0.updateActivityFleet(arg_33_1, arg_33_2, var_33_0)

def var_0_0.GetBossRushFleets(arg_35_0, arg_35_1, arg_35_2):
	local var_35_0 = {}
	local var_35_1 = arg_35_0.getActivityFleets()[arg_35_1]

	table.Foreach(arg_35_2, function(arg_36_0, arg_36_1)
		local var_36_0 = arg_36_0 == #arg_35_2

		if not var_35_1[arg_36_1]:
			local var_36_1 = var_36_0 and FleetType.Submarine or FleetType.Normal

			var_35_1[arg_36_1] = TypedFleet.New({
				id = arg_36_1,
				ship_list = {},
				fleetType = var_36_1
			})

		local var_36_2 = var_35_1[arg_36_1]

		var_36_2.RemoveUnusedItems()

		var_35_0[arg_36_0] = var_36_2)

	return var_35_0

return var_0_0
