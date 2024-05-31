local var_0_0 = class("BayProxy", import(".NetProxy"))

var_0_0.SHIP_ADDED = "ship added"
var_0_0.SHIP_REMOVED = "ship removed"
var_0_0.SHIP_UPDATED = "ship updated"
var_0_0.SHIP_EQUIPMENT_ADDED = "ship equipment added"
var_0_0.SHIP_EQUIPMENT_REMOVED = "ship equipment removed"

def var_0_0.register(arg_1_0):
	arg_1_0.on(12001, function(arg_2_0)
		arg_1_0.data = {}
		arg_1_0.activityNpcShipIds = {}
		arg_1_0.metaShipIDList = {}
		arg_1_0.equipCountDic = {}
		arg_1_0.equipSkinCountDic = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.shiplist):
			local var_2_0 = Ship.New(iter_2_1)

			var_2_0.display("loaded")

			arg_1_0.shipHighestLevel = math.max(arg_1_0.shipHighestLevel, var_2_0.level)

			if var_2_0.getConfigTable():
				arg_1_0.data[var_2_0.id] = var_2_0

				if var_2_0.isActivityNpc():
					table.insert(arg_1_0.activityNpcShipIds, var_2_0.id)
				elif var_2_0.isMetaShip() and not table.contains(arg_1_0.metaShipIDList, var_2_0.id):
					table.insert(arg_1_0.metaShipIDList, var_2_0.id)

				var_0_0.recordShipLevelVertify(var_2_0)
				arg_1_0.UpdateShipEquipAndSkinCount(var_2_0, True)
			else
				warning("不存在的角色. " .. var_2_0.id)

		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("isActivityNpc"))
	arg_1_0.on(12031, function(arg_3_0)
		arg_1_0.energyRecoverTime = arg_3_0.energy_auto_increase_time + Ship.ENERGY_RECOVER_TIME

		local var_3_0 = arg_1_0.energyRecoverTime - pg.TimeMgr.GetInstance().GetServerTime()

		arg_1_0.addEnergyListener(var_3_0))
	arg_1_0.on(12010, function(arg_4_0)
		for iter_4_0, iter_4_1 in ipairs(arg_4_0.ship_list):
			local var_4_0 = Ship.New(iter_4_1)

			var_4_0.display("loaded")

			arg_1_0.shipHighestLevel = math.max(arg_1_0.shipHighestLevel, var_4_0.level)

			if var_4_0.getConfigTable():
				arg_1_0.data[var_4_0.id] = var_4_0

				if var_4_0.isActivityNpc():
					table.insert(arg_1_0.activityNpcShipIds, var_4_0.id)
				elif var_4_0.isMetaShip() and not table.contains(arg_1_0.metaShipIDList, var_4_0.id):
					table.insert(arg_1_0.metaShipIDList, var_4_0.id)

				var_0_0.recordShipLevelVertify(var_4_0)
				arg_1_0.UpdateShipEquipAndSkinCount(var_4_0, True)
			else
				warning("不存在的角色. " .. var_4_0.id)

		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("isActivityNpc"))
	arg_1_0.on(12042, function(arg_5_0)
		local var_5_0 = getProxy(PlayerProxy).getInited()
		local var_5_1 = 0

		arg_1_0.newShipList = {}

		for iter_5_0, iter_5_1 in ipairs(arg_5_0.ship_list):
			local var_5_2 = Ship.New(iter_5_1)

			if var_5_2.getConfigTable() and var_5_2.id > 0:
				arg_1_0.addShip(var_5_2, False)

				if var_5_0:
					var_5_1 = var_5_1 + 1

				arg_1_0.newShipList[#arg_1_0.newShipList + 1] = var_5_2
			else
				warning("不存在的角色. " .. var_5_2.id)

		if var_5_1 > 0:
			arg_1_0.countShip(var_5_1)

		arg_1_0.metaTransItemMap = {})

	local var_1_0 = getProxy(PlayerProxy)

	arg_1_0.on(12019, function(arg_6_0)
		local var_6_0 = var_1_0.getData()
		local var_6_1 = arg_1_0.getShipById(var_6_0.character)

		var_6_1.setLikability(arg_6_0.intimacy)
		arg_1_0.updateShip(var_6_1))

	arg_1_0.shipHighestLevel = 0

def var_0_0.recoverAllShipEnergy(arg_7_0):
	local var_7_0 = pg.energy_template[3].upper_bound - 1
	local var_7_1 = pg.energy_template[4].upper_bound
	local var_7_2 = {}
	local var_7_3 = getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING)

	table.insertto(var_7_3, getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING_2))
	table.Foreach(var_7_3, function(arg_8_0, arg_8_1)
		if arg_8_1 and not arg_8_1.isEnd():
			local var_8_0 = arg_8_1.GetEnergyRecoverAddition()

			_.each(arg_8_1.getData1List(), function(arg_9_0)
				var_7_2[arg_9_0] = (var_7_2[arg_9_0] or 0) + var_8_0))

	for iter_7_0, iter_7_1 in pairs(arg_7_0.data):
		local var_7_4 = iter_7_1.getRecoverEnergyPoint()
		local var_7_5 = 0
		local var_7_6 = var_7_0

		if iter_7_1.state == Ship.STATE_REST or iter_7_1.state == Ship.STATE_TRAIN:
			if iter_7_1.state == Ship.STATE_TRAIN:
				var_7_5 = var_7_5 + Ship.BACKYARD_1F_ENERGY_ADDITION
			elif iter_7_1.state == Ship.STATE_REST:
				var_7_5 = var_7_5 + Ship.BACKYARD_2F_ENERGY_ADDITION

			for iter_7_2, iter_7_3 in ipairs(getProxy(ActivityProxy).getBackyardEnergyActivityBuffs()):
				var_7_5 = var_7_5 + tonumber(iter_7_3.getConfig("benefit_effect"))

			var_7_6 = var_7_1

		if var_7_2[iter_7_1.id]:
			var_7_5 = var_7_5 + var_7_2[iter_7_1.id]
			var_7_6 = var_7_1

		local var_7_7 = math.max(math.min(var_7_4, var_7_6 - iter_7_1.getEnergy()), 0)
		local var_7_8 = math.min(iter_7_1.getEnergy() + var_7_7 + var_7_5, var_7_1)

		iter_7_1.setEnergy(var_7_8)
		arg_7_0.updateShip(iter_7_1)

def var_0_0.addEnergyListener(arg_10_0, arg_10_1):
	if arg_10_1 <= 0:
		arg_10_0.recoverAllShipEnergy()
		arg_10_0.addEnergyListener(Ship.ENERGY_RECOVER_TIME)

		return

	if arg_10_0.energyTimer:
		arg_10_0.energyTimer.Stop()

		arg_10_0.energyTimer = None

	arg_10_0.energyTimer = Timer.New(function()
		arg_10_0.recoverAllShipEnergy()
		arg_10_0.addEnergyListener(Ship.ENERGY_RECOVER_TIME), arg_10_1, 1)

	arg_10_0.energyTimer.Start()

def var_0_0.remove(arg_12_0):
	if arg_12_0.energyTimer:
		arg_12_0.energyTimer.Stop()

		arg_12_0.energyTimer = None

def var_0_0.recordShipLevelVertify(arg_13_0):
	if arg_13_0:
		ys.BattleShipLevelVertify[arg_13_0.id] = var_0_0.generateLevelVertify(arg_13_0.level)

def var_0_0.checkShiplevelVertify(arg_14_0):
	if var_0_0.generateLevelVertify(arg_14_0.level) == ys.BattleShipLevelVertify[arg_14_0.id]:
		return True
	else
		return False

def var_0_0.generateLevelVertify(arg_15_0):
	return (arg_15_0 + 1114) * 824

def var_0_0.addShip(arg_16_0, arg_16_1, arg_16_2):
	assert(isa(arg_16_1, Ship), "should be an instance of Ship")
	assert(arg_16_0.data[arg_16_1.id] == None, "ship already exist, use updateShip() instead")

	arg_16_0.data[arg_16_1.id] = arg_16_1

	var_0_0.recordShipLevelVertify(arg_16_1)
	arg_16_0.UpdateShipEquipAndSkinCount(arg_16_1, True)

	arg_16_2 = defaultValue(arg_16_2, True)

	if arg_16_2:
		arg_16_0.countShip()

	arg_16_0.shipHighestLevel = math.max(arg_16_0.shipHighestLevel, arg_16_1.level)

	if arg_16_1.isActivityNpc():
		table.insert(arg_16_0.activityNpcShipIds, arg_16_1.id)
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("isActivityNpc")
	else
		if arg_16_1.isMetaShip() and not table.contains(arg_16_0.metaShipIDList, arg_16_1.id):
			table.insert(arg_16_0.metaShipIDList, arg_16_1.id)
			getProxy(MetaCharacterProxy).requestMetaTacticsInfo({
				arg_16_1.id
			})

		local var_16_0 = getProxy(CollectionProxy)

		if var_16_0:
			var_16_0.flushCollection(arg_16_1)

	if getProxy(PlayerProxy).getInited():
		arg_16_0.facade.sendNotification(var_0_0.SHIP_ADDED, arg_16_1.clone())

def var_0_0.countShip(arg_17_0, arg_17_1):
	local var_17_0 = getProxy(PlayerProxy)
	local var_17_1 = var_17_0.getData()

	var_17_1.increaseShipCount(arg_17_1)
	var_17_0.updatePlayer(var_17_1)

def var_0_0.getNewShip(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_0.newShipList or {}

	if arg_18_1:
		arg_18_0.newShipList = None

	return var_18_0

def var_0_0.getMetaTransItemMap(arg_19_0, arg_19_1):
	local var_19_0

	if arg_19_0.metaTransItemMap and arg_19_0.metaTransItemMap[arg_19_1] and #arg_19_0.metaTransItemMap[arg_19_1] > 0:
		var_19_0 = arg_19_0.metaTransItemMap[arg_19_1][1]

		table.remove(arg_19_0.metaTransItemMap[arg_19_1], 1)

	return var_19_0

def var_0_0.addMetaTransItemMap(arg_20_0, arg_20_1, arg_20_2):
	if not arg_20_0.metaTransItemMap:
		arg_20_0.metaTransItemMap = {}

	if not arg_20_0.metaTransItemMap[arg_20_1]:
		arg_20_0.metaTransItemMap[arg_20_1] = {}

	table.insert(arg_20_0.metaTransItemMap[arg_20_1], arg_20_2)

def var_0_0.getShipsByFleet(arg_21_0, arg_21_1):
	assert(isa(arg_21_1, Fleet), "should be an instance of Fleet")

	local var_21_0 = {}

	for iter_21_0, iter_21_1 in ipairs(arg_21_1.getShipIds()):
		table.insert(var_21_0, arg_21_0.data[iter_21_1])

	return var_21_0

def var_0_0.getSortShipsByFleet(arg_22_0, arg_22_1):
	assert(isa(arg_22_1, Fleet), "should be an instance of Fleet")

	local var_22_0 = {}

	for iter_22_0, iter_22_1 in ipairs(arg_22_1.mainShips):
		table.insert(var_22_0, arg_22_0.data[iter_22_1])

	for iter_22_2, iter_22_3 in ipairs(arg_22_1.vanguardShips):
		table.insert(var_22_0, arg_22_0.data[iter_22_3])

	for iter_22_4, iter_22_5 in ipairs(arg_22_1.subShips):
		table.insert(var_22_0, arg_22_0.data[iter_22_5])

	return var_22_0

def var_0_0.getShipByTeam(arg_23_0, arg_23_1, arg_23_2):
	assert(isa(arg_23_1, Fleet), "should be an instance of Fleet")

	local var_23_0 = {}

	if arg_23_2 == TeamType.Vanguard:
		for iter_23_0, iter_23_1 in ipairs(arg_23_1.vanguardShips):
			table.insert(var_23_0, arg_23_0.data[iter_23_1])
	elif arg_23_2 == TeamType.Main:
		for iter_23_2, iter_23_3 in ipairs(arg_23_1.mainShips):
			table.insert(var_23_0, arg_23_0.data[iter_23_3])
	elif arg_23_2 == TeamType.Submarine:
		for iter_23_4, iter_23_5 in ipairs(arg_23_1.subShips):
			table.insert(var_23_0, arg_23_0.data[iter_23_5])

	return Clone(var_23_0)

def var_0_0.getShipsByTypes(arg_24_0, arg_24_1):
	local var_24_0 = {}

	for iter_24_0, iter_24_1 in pairs(arg_24_0.data):
		if table.contains(arg_24_1, iter_24_1.getShipType()):
			table.insert(var_24_0, iter_24_1)

	return var_24_0

def var_0_0.getShipsByStatus(arg_25_0, arg_25_1):
	local var_25_0 = {}

	for iter_25_0, iter_25_1 in pairs(arg_25_0.data):
		if iter_25_1.status == arg_25_1:
			table.insert(var_25_0, iter_25_1)

	return var_25_0

def var_0_0.getShipsByTeamType(arg_26_0, arg_26_1):
	local var_26_0 = {}

	for iter_26_0, iter_26_1 in pairs(arg_26_0.data):
		if iter_26_1.getTeamType() == arg_26_1:
			table.insert(var_26_0, iter_26_1)

	return var_26_0

def var_0_0.getConfigShipCount(arg_27_0, arg_27_1):
	local var_27_0 = 0

	for iter_27_0, iter_27_1 in pairs(arg_27_0.data):
		if iter_27_1.configId == arg_27_1:
			var_27_0 = var_27_0 + 1

	return var_27_0

def var_0_0.getShips(arg_28_0):
	local var_28_0 = {}

	for iter_28_0, iter_28_1 in pairs(arg_28_0.data):
		table.insert(var_28_0, iter_28_1)

	return var_28_0

def var_0_0.getRawShipCount(arg_29_0):
	local var_29_0 = 0

	for iter_29_0, iter_29_1 in pairs(arg_29_0.data):
		var_29_0 = var_29_0 + 1

	return var_29_0

def var_0_0.getShipCount(arg_30_0):
	local var_30_0 = {}

	for iter_30_0, iter_30_1 in ipairs(getGameset("unoccupied_ship_nationality")[2]):
		var_30_0[iter_30_1] = True

	local var_30_1 = 0
	local var_30_2 = 0

	for iter_30_2, iter_30_3 in pairs(arg_30_0.data):
		if var_30_0[iter_30_3.getNation()]:
			var_30_2 = var_30_2 + 1
		else
			var_30_1 = var_30_1 + 1

	return var_30_1, var_30_2

def var_0_0.getShipById(arg_31_0, arg_31_1):
	if arg_31_0.data[arg_31_1] != None:
		return arg_31_0.data[arg_31_1].clone()

def var_0_0.RawGetShipById(arg_32_0, arg_32_1):
	return arg_32_0.data[arg_32_1]

def var_0_0.getMetaShipByGroupId(arg_33_0, arg_33_1):
	for iter_33_0, iter_33_1 in pairs(arg_33_0.data):
		if iter_33_1.isMetaShip() and iter_33_1.metaCharacter.id == arg_33_1:
			return iter_33_1

def var_0_0.getMetaShipIDList(arg_34_0):
	return arg_34_0.metaShipIDList

def var_0_0.updateShip(arg_35_0, arg_35_1):
	if arg_35_1.isNpc:
		return

	assert(isa(arg_35_1, Ship), "should be an instance of Ship")
	assert(arg_35_0.data[arg_35_1.id] != None, "ship should exist")

	if arg_35_1.level > arg_35_0.shipHighestLevel:
		arg_35_0.shipHighestLevel = arg_35_1.level

		pg.TrackerMgr.GetInstance().Tracking(TRACKING_SHIP_HIGHEST_LEVEL, arg_35_0.shipHighestLevel)

	local var_35_0 = arg_35_0.data[arg_35_1.id]

	arg_35_0.UpdateShipEquipAndSkinCount(var_35_0, False)

	arg_35_0.data[arg_35_1.id] = arg_35_1

	var_0_0.recordShipLevelVertify(arg_35_1)
	arg_35_0.UpdateShipEquipAndSkinCount(arg_35_1, True)

	if var_35_0.isActivityNpc() and not arg_35_1.isActivityNpc():
		table.removebyvalue(arg_35_0.activityNpcShipIds, arg_35_1.id)
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("isActivityNpc")

	if var_35_0.level < arg_35_1.level:
		pg.TrackerMgr.GetInstance().Tracking(TRACKING_SHIP_LEVEL_UP, arg_35_1.level - var_35_0.level)

	if var_35_0.getStar() < arg_35_1.getStar() or var_35_0.intimacy < arg_35_1.intimacy or var_35_0.level < arg_35_1.level or not var_35_0.propose and arg_35_1.propose:
		local var_35_1 = getProxy(CollectionProxy)

		if var_35_1 and not arg_35_1.isActivityNpc():
			var_35_1.flushCollection(arg_35_1)

	arg_35_0.facade.sendNotification(var_0_0.SHIP_UPDATED, arg_35_1.clone())

def var_0_0.removeShip(arg_36_0, arg_36_1):
	assert(isa(arg_36_1, Ship), "should be an instance of Ship")
	arg_36_0.removeShipById(arg_36_1.id)

def var_0_0.getEquipment2ByflagShip(arg_37_0):
	local var_37_0 = getProxy(PlayerProxy).getData()
	local var_37_1 = arg_37_0.getShipById(var_37_0.character)

	assert(var_37_1, "ship is None")

	return var_37_1.getEquip(2)

def var_0_0.removeShipById(arg_38_0, arg_38_1):
	local var_38_0 = arg_38_0.data[arg_38_1]

	assert(var_38_0 != None, "ship should exist")

	if var_38_0.isActivityNpc():
		table.removebyvalue(arg_38_0.activityNpcShipIds, var_38_0.id)
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("isActivityNpc")

	arg_38_0.data[var_38_0.id] = None

	var_38_0.display("removed")
	arg_38_0.UpdateShipEquipAndSkinCount(var_38_0, False)
	arg_38_0.facade.sendNotification(var_0_0.SHIP_REMOVED, var_38_0)

def var_0_0.findShipByGroup(arg_39_0, arg_39_1):
	for iter_39_0, iter_39_1 in pairs(arg_39_0.data):
		if iter_39_1.groupId == arg_39_1:
			return iter_39_1

	return None

def var_0_0.findShipsByGroup(arg_40_0, arg_40_1):
	local var_40_0 = {}

	for iter_40_0, iter_40_1 in pairs(arg_40_0.data):
		if iter_40_1.groupId == arg_40_1:
			table.insert(var_40_0, iter_40_1)

	return var_40_0

def var_0_0._findShipsByGroup(arg_41_0, arg_41_1, arg_41_2, arg_41_3):
	local function var_41_0(arg_42_0)
		if arg_41_2:
			return arg_42_0.isRemoulded()
		else
			return True

	local function var_41_1(arg_43_0)
		if arg_41_3:
			return arg_43_0.propose
		else
			return True

	local var_41_2 = {}

	for iter_41_0, iter_41_1 in pairs(arg_41_0.data):
		if iter_41_1.groupId == arg_41_1 and var_41_0(iter_41_1) and var_41_1(iter_41_1):
			table.insert(var_41_2, iter_41_1)

	return var_41_2

def var_0_0.ExistGroupShip(arg_44_0, arg_44_1):
	for iter_44_0, iter_44_1 in pairs(arg_44_0.data):
		if iter_44_1.groupId == arg_44_1:
			return True

	return False

def var_0_0._ExistGroupShip(arg_45_0, arg_45_1, arg_45_2, arg_45_3):
	local function var_45_0(arg_46_0)
		if arg_45_2:
			return arg_46_0.isRemoulded()
		else
			return True

	local function var_45_1(arg_47_0)
		if arg_45_3:
			return arg_47_0.propose
		else
			return True

	for iter_45_0, iter_45_1 in pairs(arg_45_0.data):
		if iter_45_1.groupId == arg_45_1 and var_45_0(iter_45_1) and var_45_1(iter_45_1):
			return True

	return False

def var_0_0.getSameGroupShipCount(arg_48_0, arg_48_1):
	local var_48_0 = 0

	for iter_48_0, iter_48_1 in pairs(arg_48_0.data):
		if iter_48_1.groupId == arg_48_1:
			var_48_0 = var_48_0 + 1

	return var_48_0

def var_0_0.getUpgradeShips(arg_49_0, arg_49_1):
	local var_49_0 = arg_49_1.getConfig("rarity")
	local var_49_1 = arg_49_1.groupId
	local var_49_2 = {}

	for iter_49_0, iter_49_1 in pairs(arg_49_0.data):
		if iter_49_1.groupId == var_49_1 or iter_49_1.isTestShip() and iter_49_1.canUseTestShip(var_49_0):
			table.insert(var_49_2, iter_49_1)

	return var_49_2

def var_0_0.getBayPower(arg_50_0):
	local var_50_0 = {}
	local var_50_1 = 0

	for iter_50_0, iter_50_1 in pairs(arg_50_0.data):
		local var_50_2 = iter_50_1.configId
		local var_50_3 = iter_50_1.getShipCombatPower()

		if ShipGroup.GetGroupConfig(iter_50_1.getGroupId()).handbook_type != 1 and (not var_50_0[var_50_2] or var_50_3 > var_50_0[var_50_2]):
			var_50_1 = var_50_1 - defaultValue(var_50_0[var_50_2], 0)
			var_50_0[var_50_2] = var_50_3
			var_50_1 = var_50_1 + var_50_3

	return var_50_1

def var_0_0.GetBayPowerRootedAsyn(arg_51_0, arg_51_1):
	local var_51_0

	var_51_0 = coroutine.wrap(function()
		local var_52_0 = {}
		local var_52_1 = 0
		local var_52_2 = 0

		for iter_52_0, iter_52_1 in pairs(arg_51_0.data):
			local var_52_3 = iter_52_1.configId
			local var_52_4 = iter_52_1.getShipCombatPower()

			if ShipGroup.GetGroupConfig(iter_52_1.getGroupId()).handbook_type != 1 and (not var_52_0[var_52_3] or var_52_4 > var_52_0[var_52_3]):
				var_52_1 = var_52_1 - defaultValue(var_52_0[var_52_3], 0)
				var_52_0[var_52_3] = var_52_4
				var_52_1 = var_52_1 + var_52_4

			var_52_2 = var_52_2 + 1

			if var_52_2 == 1 or var_52_2 % 50 == 0:
				onNextTick(var_51_0)
				coroutine.yield()

		arg_51_1(var_52_1^0.667))

	var_51_0()

def var_0_0.getBayPowerRooted(arg_53_0):
	return arg_53_0.getBayPower()^0.667

def var_0_0.getEquipsInShips(arg_54_0, arg_54_1):
	local var_54_0 = {}

	for iter_54_0, iter_54_1 in pairs(arg_54_0.data):
		for iter_54_2, iter_54_3 in pairs(iter_54_1.equipments):
			if iter_54_3 and (not arg_54_1 or arg_54_1(iter_54_3, iter_54_1.id)):
				table.insert(var_54_0, setmetatable({
					shipId = iter_54_1.id,
					shipPos = iter_54_2
				}, {
					__index = iter_54_3
				}))

	return var_54_0

def var_0_0.UpdateShipEquipAndSkinCount(arg_55_0, arg_55_1, arg_55_2):
	if not arg_55_1:
		return

	local var_55_0 = arg_55_2 and 1 or -1

	for iter_55_0, iter_55_1 in pairs(arg_55_1.equipments):
		if iter_55_1:
			arg_55_0.equipCountDic[iter_55_1.id] = defaultValue(arg_55_0.equipCountDic[iter_55_1.id], 0) + var_55_0

			assert(arg_55_0.equipCountDic[iter_55_1.id] >= 0)

	for iter_55_2, iter_55_3 in pairs(arg_55_1.equipmentSkins):
		if iter_55_3 > 0:
			arg_55_0.equipSkinCountDic[iter_55_3] = defaultValue(arg_55_0.equipSkinCountDic[iter_55_3], 0) + var_55_0

			assert(arg_55_0.equipSkinCountDic[iter_55_3] >= 0)

def var_0_0.GetEquipCountInShips(arg_56_0, arg_56_1):
	return arg_56_0.equipCountDic[arg_56_1] or 0

def var_0_0.GetEquipSkinCountInShips(arg_57_0, arg_57_1):
	return arg_57_0.equipSkinCountDic[arg_57_1] or 0

def var_0_0.GetEquipsInShipsRaw(arg_58_0):
	local function var_58_0(arg_59_0, arg_59_1, arg_59_2)
		local var_59_0 = CreateShell(arg_59_0)

		var_59_0.shipId = arg_59_1
		var_59_0.shipPos = arg_59_2

		return var_59_0

	local var_58_1 = {}

	for iter_58_0, iter_58_1 in pairs(arg_58_0.data):
		for iter_58_2, iter_58_3 in pairs(iter_58_1.equipments):
			if iter_58_3:
				table.insert(var_58_1, var_58_0(iter_58_3, iter_58_1.id, iter_58_2))

	return var_58_1

def var_0_0.getEquipmentSkinInShips(arg_60_0, arg_60_1, arg_60_2):
	local function var_60_0(arg_61_0)
		local var_61_0 = False

		if arg_61_0 and arg_61_0 > 0:
			local var_61_1 = pg.equip_skin_template[arg_61_0]

			var_61_0 = _.any(var_61_1.equip_type, function(arg_62_0)
				return not arg_60_2 or table.contains(arg_60_2, arg_62_0))

		return var_61_0

	local var_60_1 = {}

	for iter_60_0, iter_60_1 in pairs(arg_60_0.data):
		if not arg_60_1 or arg_60_1.id != iter_60_1.id:
			for iter_60_2, iter_60_3 in pairs(iter_60_1.getEquipSkins()):
				local var_60_2 = var_60_0(iter_60_3)

				if iter_60_3 and var_60_2:
					table.insert(var_60_1, {
						id = iter_60_3,
						shipId = iter_60_1.id,
						shipPos = iter_60_2
					})

	return var_60_1

def var_0_0.GetSpWeaponsInShips(arg_63_0, arg_63_1):
	local var_63_0 = {}

	for iter_63_0, iter_63_1 in pairs(arg_63_0.data):
		if not arg_63_1 or arg_63_1.id != iter_63_1.id:
			local var_63_1 = iter_63_1.GetSpWeapon()

			if var_63_1 and (not arg_63_1 or not arg_63_1.IsSpWeaponForbidden(var_63_1)):
				table.insert(var_63_0, var_63_1)

	return var_63_0

def var_0_0.getProposeGroupList(arg_64_0):
	local var_64_0 = {}

	for iter_64_0, iter_64_1 in pairs(arg_64_0.data):
		if iter_64_1.ShowPropose():
			var_64_0[iter_64_1.groupId] = True

	return var_64_0

def var_0_0.GetRecommendShip(arg_65_0, arg_65_1, arg_65_2, arg_65_3):
	assert(arg_65_3)

	local var_65_0 = arg_65_0.getShipsByTypes(arg_65_1)
	local var_65_1 = {}

	for iter_65_0, iter_65_1 in ipairs(var_65_0):
		var_65_1[iter_65_1] = iter_65_1.getShipCombatPower()

	table.sort(var_65_0, function(arg_66_0, arg_66_1)
		return var_65_1[arg_66_0] < var_65_1[arg_66_1])

	local var_65_2 = {}

	for iter_65_2, iter_65_3 in ipairs(arg_65_2):
		var_65_2[#var_65_2 + 1] = arg_65_0.data[iter_65_3].getGroupId()

	local var_65_3 = #var_65_0
	local var_65_4

	while var_65_3 > 0:
		local var_65_5 = var_65_0[var_65_3]
		local var_65_6 = var_65_5.id
		local var_65_7 = var_65_5.getGroupId()

		if not table.contains(arg_65_2, var_65_6) and not table.contains(var_65_2, var_65_7) and arg_65_3(var_65_5):
			var_65_4 = var_65_5

			break
		else
			var_65_3 = var_65_3 - 1

	return var_65_4

def var_0_0.getActivityRecommendShips(arg_67_0, arg_67_1, arg_67_2, arg_67_3, arg_67_4):
	local var_67_0 = arg_67_0.getShipsByTypes(arg_67_1)
	local var_67_1 = {}

	for iter_67_0, iter_67_1 in ipairs(var_67_0):
		var_67_1[iter_67_1] = iter_67_1.getShipCombatPower()

	table.sort(var_67_0, function(arg_68_0, arg_68_1)
		return var_67_1[arg_68_0] < var_67_1[arg_68_1])

	local var_67_2 = {}

	for iter_67_2, iter_67_3 in ipairs(arg_67_2):
		local var_67_3 = arg_67_0.data[iter_67_3]

		var_67_2[#var_67_2 + 1] = var_67_3.getGroupId()

	local var_67_4 = #var_67_0
	local var_67_5 = {}

	while var_67_4 > 0 and arg_67_3 > 0:
		local var_67_6 = var_67_0[var_67_4]
		local var_67_7 = var_67_6.id
		local var_67_8 = var_67_6.getGroupId()

		if not table.contains(arg_67_2, var_67_7) and not table.contains(var_67_2, var_67_8) and ShipStatus.ShipStatusCheck("inActivity", var_67_6, None, {
			inActivity = arg_67_4
		}):
			table.insert(var_67_5, var_67_6)
			table.insert(var_67_2, var_67_8)

			arg_67_3 = arg_67_3 - 1

		var_67_4 = var_67_4 - 1

	return var_67_5

def var_0_0.getDelegationRecommendShips(arg_69_0, arg_69_1):
	local var_69_0 = 6 - #arg_69_1.shipIds
	local var_69_1 = arg_69_1.template.ship_type
	local var_69_2 = arg_69_1.template.ship_lv
	local var_69_3 = math.max(var_69_2, 2)
	local var_69_4 = Clone(arg_69_1.shipIds)
	local var_69_5 = arg_69_0.getShipsByTypes(var_69_1)

	table.sort(var_69_5, function(arg_70_0, arg_70_1)
		return arg_70_0.level > arg_70_1.level)

	local var_69_6 = {}
	local var_69_7 = False

	for iter_69_0, iter_69_1 in ipairs(var_69_4):
		local var_69_8 = arg_69_0.data[iter_69_1]

		if var_69_3 <= var_69_8.level:
			var_69_7 = True

		var_69_6[#var_69_6 + 1] = var_69_8.getGroupId()

	if var_69_7:
		var_69_3 = 2

	local var_69_9 = {}
	local var_69_10 = #var_69_5

	while var_69_10 > 0:
		if var_69_0 <= 0:
			break

		local var_69_11 = var_69_5[var_69_10]
		local var_69_12 = var_69_11.id
		local var_69_13 = var_69_11.getGroupId()

		if var_69_3 <= var_69_11.level and var_69_11.lockState != Ship.LOCK_STATE_UNLOCK and not table.contains(var_69_4, var_69_12) and not table.contains(var_69_6, var_69_13) and not table.contains(var_69_9, var_69_12) and not var_69_11.getFlag("inElite") and not var_69_11.getFlag("inActivity") and ShipStatus.ShipStatusCheck("inEvent", var_69_11):
			table.insert(var_69_6, var_69_13)
			table.insert(var_69_9, var_69_12)

			var_69_0 = var_69_0 - 1

			if var_69_7 == False:
				var_69_7 = True
				var_69_3 = 2
				var_69_10 = #var_69_5
		else
			var_69_10 = var_69_10 - 1

	return var_69_9

def var_0_0.getDelegationRecommendShipsLV1(arg_71_0, arg_71_1):
	local var_71_0 = 6 - #arg_71_1.shipIds
	local var_71_1 = arg_71_1.template.ship_type
	local var_71_2 = Clone(arg_71_1.shipIds)
	local var_71_3 = arg_71_0.getShipsByTypes(var_71_1)
	local var_71_4 = _.select(var_71_3, function(arg_72_0)
		return arg_72_0.level == 1)

	table.sort(var_71_4, CompareFuncs({
		function(arg_73_0)
			return arg_73_0.lockState == arg_73_0.LOCK_STATE_UNLOCK and 0 or 1
	}))

	local var_71_5 = {}

	for iter_71_0, iter_71_1 in ipairs(var_71_2):
		local var_71_6 = arg_71_0.data[iter_71_1]

		var_71_5[#var_71_5 + 1] = var_71_6.getGroupId()

	local var_71_7 = {}
	local var_71_8 = #var_71_4

	while var_71_8 > 0:
		if var_71_0 <= 0:
			break

		local var_71_9 = var_71_4[var_71_8]
		local var_71_10 = var_71_9.id
		local var_71_11 = var_71_9.getGroupId()

		if not table.contains(var_71_2, var_71_10) and not table.contains(var_71_5, var_71_11) and not table.contains(var_71_7, var_71_10) and not var_71_9.getFlag("inElite") and not var_71_9.getFlag("inActivity") and ShipStatus.ShipStatusCheck("inEvent", var_71_9):
			table.insert(var_71_5, var_71_11)
			table.insert(var_71_7, var_71_10)

			var_71_0 = var_71_0 - 1
		else
			var_71_8 = var_71_8 - 1

	return var_71_7

def var_0_0.getWorldRecommendShip(arg_74_0, arg_74_1, arg_74_2):
	local var_74_0 = arg_74_0.getShipsByTeamType(arg_74_1)
	local var_74_1 = {}

	for iter_74_0, iter_74_1 in ipairs(var_74_0):
		var_74_1[iter_74_1] = iter_74_1.getShipCombatPower()

	table.sort(var_74_0, function(arg_75_0, arg_75_1)
		return var_74_1[arg_75_0] < var_74_1[arg_75_1])

	local var_74_2 = {}

	for iter_74_2, iter_74_3 in ipairs(arg_74_2):
		var_74_2[#var_74_2 + 1] = arg_74_0.data[iter_74_3].getGroupId()

	local var_74_3 = #var_74_0
	local var_74_4

	while var_74_3 > 0:
		local var_74_5 = var_74_0[var_74_3]
		local var_74_6 = var_74_5.id
		local var_74_7 = var_74_5.getGroupId()

		if not table.contains(arg_74_2, var_74_6) and not table.contains(var_74_2, var_74_7) and ShipStatus.ShipStatusCheck("inWorld", var_74_5):
			var_74_4 = var_74_5

			break
		else
			var_74_3 = var_74_3 - 1

	return var_74_4

def var_0_0.getModRecommendShip(arg_76_0, arg_76_1, arg_76_2):
	local var_76_0 = underscore.map(arg_76_2, function(arg_77_0)
		return arg_76_0.data[arg_77_0])
	local var_76_1 = Clone(arg_76_1)

	for iter_76_0, iter_76_1 in pairs(ShipModLayer.getModExpAdditions(var_76_1, var_76_0)):
		var_76_1.addModAttrExp(iter_76_0, iter_76_1)

	local var_76_2 = var_76_1.getNeedModExp()
	local var_76_3 = 0

	for iter_76_2, iter_76_3 in pairs(var_76_2):
		var_76_3 = var_76_3 + iter_76_3

	local var_76_4 = {}

	for iter_76_4, iter_76_5 in pairs(arg_76_0.data):
		if iter_76_5.isSameKind(arg_76_1):
			var_76_4.sameKind = var_76_4.sameKind or {}

			table.insert(var_76_4.sameKind, iter_76_5)
		else
			local var_76_5 = iter_76_5.getShipType()

			var_76_4[var_76_5] = var_76_4[var_76_5] or {}

			table.insert(var_76_4[var_76_5], iter_76_5)

	local var_76_6 = arg_76_1.getConfig("type")

	for iter_76_6, iter_76_7 in ipairs(table.mergeArray({
		"sameKind"
	}, pg.ship_data_by_type[var_76_6].strengthen_choose_type)):
		if #var_76_0 == 12 or var_76_3 == 0:
			break

		local var_76_7 = var_76_4[iter_76_7] or {}
		local var_76_8 = {}

		for iter_76_8, iter_76_9 in ipairs(pg.ShipFlagMgr.GetInstance().FilterShips(ShipStatus.FILTER_SHIPS_FLAGS_2, underscore.map(var_76_7, function(arg_78_0)
			return arg_78_0.id))):
			var_76_8[iter_76_9] = True

		local var_76_9 = underscore.filter(var_76_7, function(arg_79_0)
			return arg_79_0.level == 1 and arg_79_0.getRarity() <= ShipRarity.Gray and arg_79_0.GetLockState() != Ship.LOCK_STATE_LOCK and not table.contains(arg_76_2, arg_79_0.id) and arg_76_1.id != arg_79_0.id and not var_76_8[arg_79_0.id])

		for iter_76_10, iter_76_11 in ipairs(var_76_9):
			if #var_76_0 == 12 or var_76_3 == 0:
				break

			local var_76_10 = ShipModLayer.getModExpAdditions(var_76_1, {
				iter_76_11
			})
			local var_76_11 = False

			for iter_76_12, iter_76_13 in pairs(var_76_10):
				if iter_76_13 > 0 and var_76_2[iter_76_12] > 0:
					var_76_11 = True
					var_76_3 = var_76_3 - math.min(var_76_2[iter_76_12], iter_76_13)
					var_76_2[iter_76_12] = math.max(var_76_2[iter_76_12] - iter_76_13, 0)

			if var_76_11:
				table.insert(var_76_0, iter_76_11)

	return underscore.map(var_76_0, function(arg_80_0)
		return arg_80_0.id)

def var_0_0.getUpgradeRecommendShip(arg_81_0, arg_81_1, arg_81_2, arg_81_3):
	local var_81_0 = arg_81_0.getUpgradeShips(arg_81_1)
	local var_81_1 = pg.ShipFlagMgr.GetInstance().FilterShips(ShipStatus.FILTER_SHIPS_FLAGS_4, underscore.keys(arg_81_0.data))

	local function var_81_2(arg_82_0)
		return arg_82_0.level == 1 and arg_82_0.GetLockState() != Ship.LOCK_STATE_LOCK and not table.contains(arg_81_2, arg_82_0.id) and arg_81_1.id != arg_82_0.id and not table.contains(var_81_1, arg_82_0.id)

	local var_81_3 = {}

	for iter_81_0, iter_81_1 in ipairs(var_81_0):
		if var_81_2(iter_81_1):
			table.insert(var_81_3, iter_81_1)

	local var_81_4 = {
		function(arg_83_0)
			return arg_83_0.isSameKind(arg_81_1) and 0 or 1
	}

	table.sort(var_81_3, CompareFuncs(var_81_4))

	local var_81_5 = {}

	for iter_81_2, iter_81_3 in pairs(arg_81_2):
		table.insert(var_81_5, arg_81_0.data[iter_81_3])

	for iter_81_4, iter_81_5 in ipairs(var_81_3):
		if #var_81_5 == arg_81_3:
			break

		table.insert(var_81_5, iter_81_5)

	return underscore.map(var_81_5, function(arg_84_0)
		return arg_84_0.id)

def var_0_0.getGroupPropose(arg_85_0, arg_85_1):
	local var_85_0 = False

	if arg_85_0.data:
		for iter_85_0, iter_85_1 in ipairs(arg_85_0.data):
			if pg.ship_data_template[iter_85_1.configId].group_type == arg_85_1 and iter_85_1.propose:
				return True

	return var_85_0

def var_0_0.CanUseShareSkinShips(arg_86_0, arg_86_1):
	local var_86_0 = pg.ship_skin_template[arg_86_1].ship_group
	local var_86_1 = pg.ship_data_group.get_id_list_by_group_type[var_86_0][1]
	local var_86_2 = pg.ship_data_group[var_86_1].share_group_id
	local var_86_3 = {}
	local var_86_4 = arg_86_0.getRawData()

	for iter_86_0, iter_86_1 in pairs(var_86_4):
		if table.contains(var_86_2, iter_86_1.groupId) and math.floor(iter_86_1.getIntimacy() / 100) >= iter_86_1.GetNoProposeIntimacyMax():
			table.insert(var_86_3, iter_86_1)

	return var_86_3

return var_0_0
