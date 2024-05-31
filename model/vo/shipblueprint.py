local var_0_0 = class("ShipBluePrint", import(".BaseVO"))

var_0_0.STATE_LOCK = 1
var_0_0.STATE_DEV = 2
var_0_0.STATE_DEV_FINISHED = 3
var_0_0.STATE_UNLOCK = 4
var_0_0.TASK_STATE_LOCK = 1
var_0_0.TASK_STATE_OPENING = 2
var_0_0.TASK_STATE_WAIT = 3
var_0_0.TASK_STATE_START = 4
var_0_0.TASK_STATE_ACHIEVED = 5
var_0_0.TASK_STATE_FINISHED = 6
var_0_0.TASK_STATE_PAUSE = 7
var_0_0.STRENGTHEN_TYPE_ATTR = "attr"
var_0_0.STRENGTHEN_TYPE_DIALOGUE = "dialog"
var_0_0.STRENGTHEN_TYPE_SKILL = "skill"
var_0_0.STRENGTHEN_TYPE_CHANGE_SKILL = "change_skill"
var_0_0.STRENGTHEN_TYPE_BASE_LIST = "base"
var_0_0.STRENGTHEN_TYPE_SKIN = "skin"
var_0_0.STRENGTHEN_TYPE_BREAKOUT = "breakout"
var_0_0.STRENGTHEN_TYPE_PRLOAD_COUNT = "preload"
var_0_0.STRENGTHEN_TYPE_EQUIPMENTPROFICIENCY = "equipmentproficiency"

local var_0_1 = pg.ship_data_blueprint
local var_0_2 = pg.ship_strengthen_blueprint
local var_0_3 = False

def var_0_0.print(...):
	if var_0_3:
		print(...)

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.configId = arg_2_1.id
	arg_2_0.id = arg_2_0.configId
	arg_2_0.state = var_0_0.STATE_LOCK
	arg_2_0.startTime = 0
	arg_2_0.shipId = 0
	arg_2_0.duration = 0
	arg_2_0.level = 0
	arg_2_0.fateLevel = -1
	arg_2_0.exp = 0
	arg_2_0.strengthenConfig = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.getConfig("strengthen_effect")):
		local var_2_0 = Clone(var_0_2[iter_2_1])

		if var_2_0.special == 1:
			arg_2_0.warpspecialEffect(var_2_0)

		arg_2_0.strengthenConfig[iter_2_0] = var_2_0

	arg_2_0.fateStrengthenConfig = {}

	for iter_2_2, iter_2_3 in ipairs(arg_2_0.getConfig("fate_strengthen")):
		local var_2_1 = Clone(var_0_2[iter_2_3])

		if var_2_1.special == 1:
			arg_2_0.warpspecialEffect(var_2_1)

		arg_2_0.fateStrengthenConfig[iter_2_2] = var_2_1

def var_0_0.warpspecialEffect(arg_3_0, arg_3_1):
	local var_3_0 = {}
	local var_3_1 = string.split(arg_3_1.effect_desc, "|")
	local var_3_2 = 0

	if type(arg_3_1.effect_attr) == "table":
		for iter_3_0, iter_3_1 in ipairs(arg_3_1.effect_attr):
			var_3_2 = var_3_2 + 1

			table.insert(var_3_0, {
				var_0_0.STRENGTHEN_TYPE_ATTR,
				iter_3_1,
				var_3_1[var_3_2] or ""
			})

		arg_3_1.effect_attr = None

	if arg_3_1.effect_breakout != 0:
		var_3_2 = var_3_2 + 1

		table.insert(var_3_0, {
			var_0_0.STRENGTHEN_TYPE_BREAKOUT,
			arg_3_1.effect_breakout,
			var_3_1[var_3_2] or ""
		})

		arg_3_1.effect_breakout = None

	if type(arg_3_1.effect_skill) == "table":
		var_3_2 = var_3_2 + 1

		table.insert(var_3_0, {
			var_0_0.STRENGTHEN_TYPE_SKILL,
			arg_3_1.effect_skill,
			var_3_1[var_3_2] or ""
		})

		arg_3_1.effect_skill = None

	if type(arg_3_1.change_skill) == "table":
		var_3_2 = var_3_2 + 1

		table.insert(var_3_0, {
			var_0_0.STRENGTHEN_TYPE_CHANGE_SKILL,
			arg_3_1.change_skill,
			var_3_1[var_3_2] or ""
		})

		arg_3_1.change_skill = None

	if type(arg_3_1.effect_base) == "table":
		var_3_2 = var_3_2 + 1

		table.insert(var_3_0, {
			var_0_0.STRENGTHEN_TYPE_BASE_LIST,
			arg_3_1.effect_base,
			var_3_1[var_3_2] or ""
		})

		arg_3_1.effect_base = None

	if type(arg_3_1.effect_preload) == "table":
		var_3_2 = var_3_2 + 1

		table.insert(var_3_0, {
			var_0_0.STRENGTHEN_TYPE_PRLOAD_COUNT,
			arg_3_1.effect_preload,
			var_3_1[var_3_2] or ""
		})

		arg_3_1.effect_preload = None

	if type(arg_3_1.effect_dialog) == "table":
		var_3_2 = var_3_2 + 1

		table.insert(var_3_0, {
			var_0_0.STRENGTHEN_TYPE_DIALOGUE,
			arg_3_1.effect_dialog,
			var_3_1[var_3_2] or ""
		})

		arg_3_1.effect_dialog = None

	if arg_3_1.effect_skin != 0:
		var_3_2 = var_3_2 + 1

		table.insert(var_3_0, {
			var_0_0.STRENGTHEN_TYPE_SKIN,
			arg_3_1.effect_skin,
			var_3_1[var_3_2] or ""
		})

		arg_3_1.effect_skin = None

	if type(arg_3_1.effect_equipment_proficiency) == "table":
		local var_3_3 = var_3_2 + 1

		table.insert(var_3_0, {
			var_0_0.STRENGTHEN_TYPE_EQUIPMENTPROFICIENCY,
			arg_3_1.effect_equipment_proficiency,
			var_3_1[var_3_3] or ""
		})

	arg_3_1.special_effect = var_3_0

def var_0_0.updateInfo(arg_4_0, arg_4_1):
	arg_4_0.startTime = arg_4_1.start_time or 0
	arg_4_0.shipId = arg_4_1.ship_id or 0
	arg_4_0.level = arg_4_1.blue_print_level and math.min(arg_4_1.blue_print_level, arg_4_0.getMaxLevel()) or 0
	arg_4_0.fateLevel = arg_4_0.level == arg_4_0.getMaxLevel() and arg_4_1.blue_print_level - arg_4_0.getMaxLevel() or -1
	arg_4_0.exp = arg_4_1.exp or 0
	arg_4_0.duration = arg_4_1.start_duration or 0

	arg_4_0.updateState()

def var_0_0.updateStartUpTime(arg_5_0, arg_5_1):
	arg_5_0.duration = arg_5_1

def var_0_0.updateState(arg_6_0):
	if arg_6_0.isFetched():
		arg_6_0.state = var_0_0.STATE_UNLOCK
	elif arg_6_0.startTime == 0:
		arg_6_0.state = var_0_0.STATE_LOCK
	elif arg_6_0.isFinishedAllTasks():
		arg_6_0.state = var_0_0.STATE_DEV_FINISHED
	else
		arg_6_0.state = var_0_0.STATE_DEV

def var_0_0.addExp(arg_7_0, arg_7_1):
	assert(arg_7_1, "exp can not be None")

	arg_7_0.exp = arg_7_0.exp + arg_7_1

	local var_7_0 = arg_7_0.getMaxLevel()

	if var_7_0 > arg_7_0.level:
		while arg_7_0.canLevelUp():
			local var_7_1 = arg_7_0.getNextLevelExp()

			arg_7_0.exp = arg_7_0.exp - var_7_1
			arg_7_0.level = math.min(arg_7_0.level + 1, var_7_0)

		if arg_7_0.level == var_7_0:
			arg_7_0.fateLevel = 0

	if arg_7_0.canFateSimulation():
		local var_7_2 = arg_7_0.getMaxFateLevel()

		while arg_7_0.canFateLevelUp():
			local var_7_3 = arg_7_0.getNextFateLevelExp()

			arg_7_0.exp = arg_7_0.exp - var_7_3
			arg_7_0.fateLevel = math.min(arg_7_0.fateLevel + 1, var_7_2)

def var_0_0.getNextLevelExp(arg_8_0):
	if arg_8_0.level == arg_8_0.getMaxLevel():
		return -1
	else
		local var_8_0 = arg_8_0.level + 1

		return arg_8_0.strengthenConfig[var_8_0].need_exp

def var_0_0.getNextFateLevelExp(arg_9_0):
	if arg_9_0.fateLevel == arg_9_0.getMaxFateLevel():
		return -1
	else
		local var_9_0 = arg_9_0.fateLevel + 1

		return arg_9_0.fateStrengthenConfig[var_9_0].need_exp

def var_0_0.canLevelUp(arg_10_0):
	if arg_10_0.level == arg_10_0.getMaxLevel():
		return False

	if arg_10_0.getNextLevelExp() <= arg_10_0.exp:
		return True

	return False

def var_0_0.canFateSimulation(arg_11_0):
	return #arg_11_0.fateStrengthenConfig > 0 and arg_11_0.fateLevel >= 0

def var_0_0.canFateLevelUp(arg_12_0):
	if arg_12_0.fateLevel == arg_12_0.getMaxFateLevel():
		return False

	if arg_12_0.getNextFateLevelExp() <= arg_12_0.exp:
		return True

	return False

def var_0_0.getMaxLevel(arg_13_0):
	return arg_13_0.strengthenConfig[#arg_13_0.strengthenConfig].lv

def var_0_0.getMaxFateLevel(arg_14_0):
	return arg_14_0.fateStrengthenConfig[#arg_14_0.fateStrengthenConfig].lv - 30

def var_0_0.isMaxLevel(arg_15_0):
	return arg_15_0.level == arg_15_0.getMaxLevel()

def var_0_0.isMaxFateLevel(arg_16_0):
	return arg_16_0.fateLevel == arg_16_0.getMaxFateLevel()

def var_0_0.isMaxIntensifyLevel(arg_17_0):
	if #arg_17_0.getConfig("fate_strengthen") > 0:
		return arg_17_0.isMaxFateLevel()
	else
		return arg_17_0.isMaxLevel()

def var_0_0.getBluePrintAddition(arg_18_0, arg_18_1):
	local var_18_0 = table.indexof(ShipModAttr.BLUEPRINT_ATTRS, arg_18_1)
	local var_18_1 = arg_18_0.getConfig("attr_exp")[var_18_0]

	if var_18_1:
		local var_18_2 = 0

		for iter_18_0 = 1, arg_18_0.level:
			var_18_2 = var_18_2 + arg_18_0.strengthenConfig[iter_18_0].effect[var_18_0]

		local var_18_3 = 0

		if not arg_18_0.isMaxLevel():
			local var_18_4 = arg_18_0.getNextLevelExp()

			var_18_3 = arg_18_0.exp / var_18_4 * arg_18_0.strengthenConfig[arg_18_0.level + 1].effect[var_18_0]

		local var_18_5 = (var_18_2 + var_18_3) / var_18_1
		local var_18_6 = (var_18_2 + var_18_3) % var_18_1

		return var_18_5, var_18_6
	else
		return 0, 0

def var_0_0.getShipVO(arg_19_0):
	return Ship.New({
		configId = tonumber(arg_19_0.id .. "1")
	})

def var_0_0.isFetched(arg_20_0):
	return arg_20_0.shipId != 0

def var_0_0.getState(arg_21_0):
	return arg_21_0.state

def var_0_0.start(arg_22_0, arg_22_1):
	arg_22_0.state = var_0_0.STATE_DEV
	arg_22_0.startTime = arg_22_1
	arg_22_0.duration = 0

def var_0_0.reset(arg_23_0):
	arg_23_0.state = var_0_0.STATE_LOCK
	arg_23_0.startTime = 0

def var_0_0.isLock(arg_24_0):
	return arg_24_0.state == var_0_0.STATE_LOCK

def var_0_0.isDeving(arg_25_0):
	return arg_25_0.state == var_0_0.STATE_DEV

def var_0_0.isFinished(arg_26_0):
	return arg_26_0.state == var_0_0.STATE_DEV_FINISHED

def var_0_0.finish(arg_27_0):
	arg_27_0.state = var_0_0.STATE_DEV_FINISHED

def var_0_0.unlock(arg_28_0, arg_28_1):
	arg_28_0.shipId = arg_28_1
	arg_28_0.state = var_0_0.STATE_UNLOCK
	arg_28_0.duration = 0

def var_0_0.isUnlock(arg_29_0):
	return arg_29_0.state == var_0_0.STATE_UNLOCK

def var_0_0.getItemId(arg_30_0):
	return arg_30_0.getConfig("strengthen_item")

def var_0_0.bindConfigTable(arg_31_0):
	return pg.ship_data_blueprint

def var_0_0.getTaskIds(arg_32_0):
	return _.map(arg_32_0.getConfig("unlock_task"), function(arg_33_0)
		return arg_33_0[1])

def var_0_0.getTaskOpenTimeStamp(arg_34_0, arg_34_1):
	local var_34_0 = table.indexof(arg_34_0.getTaskIds(), arg_34_1)

	return arg_34_0.getConfig("unlock_task")[var_34_0][2] + arg_34_0.startTime + 1

def var_0_0.isFinishedAllTasks(arg_35_0):
	local var_35_0 = getProxy(TaskProxy)

	return _.all(arg_35_0.getTaskIds(), function(arg_36_0)
		return arg_35_0.getTaskStateById(arg_36_0) == var_0_0.TASK_STATE_FINISHED)

def var_0_0.getTaskStateById(arg_37_0, arg_37_1):
	if arg_37_0.isLock():
		if arg_37_0.duration > 0:
			return var_0_0.TASK_STATE_PAUSE
		else
			return var_0_0.TASK_STATE_LOCK
	elif arg_37_0.getTaskOpenTimeStamp(arg_37_1) > pg.TimeMgr.GetInstance().GetServerTime():
		return var_0_0.TASK_STATE_WAIT
	else
		local var_37_0 = getProxy(TaskProxy).getTaskVO(arg_37_1)

		if var_37_0 and var_37_0.isReceive():
			return var_0_0.TASK_STATE_FINISHED
		elif var_37_0 and var_37_0.isFinish():
			return var_0_0.TASK_STATE_ACHIEVED
		elif var_37_0:
			return var_0_0.TASK_STATE_START
		else
			return var_0_0.TASK_STATE_OPENING

def var_0_0.getExpRetio(arg_38_0, arg_38_1):
	local var_38_0 = arg_38_0.getConfig("attr_exp")

	assert(arg_38_1 > 0 and arg_38_1 <= #var_38_0, "invalid index" .. arg_38_1)

	return var_38_0[arg_38_1]

def var_0_0.specialStrengthens(arg_39_0):
	local var_39_0 = {}

	for iter_39_0, iter_39_1 in ipairs(arg_39_0.strengthenConfig):
		if iter_39_1.special == 1:
			table.insert(var_39_0, {
				des = iter_39_1.special_effect,
				extraDes = iter_39_1.extra_desc,
				level = iter_39_1.lv
			})

	return var_39_0

def var_0_0.getSpecials(arg_40_0):
	return arg_40_0.strengthenConfig[arg_40_0.level].special_effect

def var_0_0.getTopLimitAttrValue(arg_41_0, arg_41_1):
	if arg_41_0.level == 0:
		return 0
	else
		local var_41_0 = arg_41_0.strengthenConfig[arg_41_0.level].effect
		local var_41_1 = var_41_0[arg_41_1]

		assert(var_41_0[arg_41_1], "strengthen config effect" .. arg_41_1)

		local var_41_2 = arg_41_0.getConfig("attr_exp")[arg_41_1]

		return math.floor(var_41_1 / var_41_2)

def var_0_0.getItemExp(arg_42_0):
	local var_42_0 = arg_42_0.getConfig("strengthen_item")

	return Item.getConfigData(var_42_0).usage_arg[1]

def var_0_0.getShipProperties(arg_43_0, arg_43_1, arg_43_2):
	assert(arg_43_1, "shipVO can not be None" .. arg_43_0.shipId)

	local var_43_0 = arg_43_1.getBaseProperties()

	arg_43_2 = defaultValue(arg_43_2, True)

	local var_43_1 = arg_43_0.getTotalAdditions()

	for iter_43_0, iter_43_1 in pairs(var_43_0):
		var_43_0[iter_43_0] = var_43_0[iter_43_0] + (var_43_1[iter_43_0] or 0)

	if arg_43_1.getIntimacyLevel() > 0 and arg_43_2:
		local var_43_2 = pg.intimacy_template[arg_43_1.getIntimacyLevel()].attr_bonus * 0.0001

		for iter_43_2, iter_43_3 in pairs(var_43_0):
			if iter_43_2 == AttributeType.Durability or iter_43_2 == AttributeType.Cannon or iter_43_2 == AttributeType.Torpedo or iter_43_2 == AttributeType.AntiAircraft or iter_43_2 == AttributeType.Air or iter_43_2 == AttributeType.Reload or iter_43_2 == AttributeType.Hit or iter_43_2 == AttributeType.AntiSub or iter_43_2 == AttributeType.Dodge:
				var_43_0[iter_43_2] = var_43_0[iter_43_2] * (var_43_2 + 1)

	return var_43_0

def var_0_0.getTotalAdditions(arg_44_0):
	local var_44_0 = {}
	local var_44_1 = arg_44_0.attrSpecialAddition()

	for iter_44_0, iter_44_1 in ipairs(Ship.PROPERTIES):
		local var_44_2, var_44_3 = arg_44_0.getBluePrintAddition(iter_44_1)

		var_44_0[iter_44_1] = var_44_2 + (var_44_1[iter_44_1] or 0)

	return var_44_0

def var_0_0.attrSpecialAddition(arg_45_0):
	local var_45_0 = {}

	for iter_45_0 = 1, arg_45_0.level:
		local var_45_1 = arg_45_0.strengthenConfig[iter_45_0]

		if var_45_1.special == 1 and type(var_45_1.special_effect) == "table":
			for iter_45_1, iter_45_2 in ipairs(var_45_1.special_effect):
				if iter_45_2[1] == var_0_0.STRENGTHEN_TYPE_ATTR:
					local var_45_2 = iter_45_2[2]

					var_45_0[var_45_2[1]] = (var_45_0[var_45_2[1]] or 0) + var_45_2[2]

	for iter_45_3 = 1, arg_45_0.fateLevel:
		local var_45_3 = arg_45_0.fateStrengthenConfig[iter_45_3]

		if var_45_3.special == 1 and type(var_45_3.special_effect) == "table":
			for iter_45_4, iter_45_5 in ipairs(var_45_3.special_effect):
				if iter_45_5[1] == var_0_0.STRENGTHEN_TYPE_ATTR:
					local var_45_4 = iter_45_5[2]

					var_45_0[var_45_4[1]] = (var_45_0[var_45_4[1]] or 0) + var_45_4[2]

	return var_45_0

def var_0_0.getUseageMaxItem(arg_46_0):
	local var_46_0 = 0

	for iter_46_0 = arg_46_0.level + 1, arg_46_0.getMaxLevel():
		assert(arg_46_0.strengthenConfig[iter_46_0], "strengthen config >> " .. iter_46_0)

		var_46_0 = var_46_0 + arg_46_0.strengthenConfig[iter_46_0].need_exp

	return math.max(math.ceil((var_46_0 - arg_46_0.exp) / arg_46_0.getItemExp()), 0)

def var_0_0.getFateUseageMaxItem(arg_47_0):
	local var_47_0 = 0

	for iter_47_0 = arg_47_0.fateLevel + 1, arg_47_0.getMaxFateLevel():
		assert(arg_47_0.fateStrengthenConfig[iter_47_0], "strengthen config >> " .. iter_47_0)

		var_47_0 = var_47_0 + arg_47_0.fateStrengthenConfig[iter_47_0].need_exp

	return math.max(math.ceil((var_47_0 - arg_47_0.exp) / arg_47_0.getItemExp()), 0)

def var_0_0.getOpenTaskList(arg_48_0):
	return arg_48_0.getConfig("unlock_task_open_condition")

def var_0_0.getStrengthenConfig(arg_49_0, arg_49_1):
	return arg_49_0.strengthenConfig[arg_49_1]

def var_0_0.getFateStrengthenConfig(arg_50_0, arg_50_1):
	return arg_50_0.fateStrengthenConfig[arg_50_1]

def var_0_0.getUnlockVoices(arg_51_0):
	local var_51_0 = {}

	for iter_51_0 = 1, arg_51_0.level:
		local var_51_1 = arg_51_0.getStrengthenConfig(iter_51_0)

		if var_51_1.special == 1:
			local var_51_2 = var_51_1.special_effect

			if type(var_51_2) == "table":
				for iter_51_1, iter_51_2 in ipairs(var_51_2):
					if iter_51_2[1] == var_0_0.STRENGTHEN_TYPE_DIALOGUE:
						for iter_51_3, iter_51_4 in ipairs(iter_51_2[2]):
							table.insert(var_51_0, iter_51_4)

	return var_51_0

def var_0_0.getUnlockLevel(arg_52_0, arg_52_1):
	local var_52_0 = arg_52_0.getMaxLevel()

	for iter_52_0 = 1, var_52_0:
		local var_52_1 = arg_52_0.getStrengthenConfig(iter_52_0).special_effect

		if type(var_52_1) == "table":
			for iter_52_1, iter_52_2 in ipairs(var_52_1):
				if iter_52_2[1] == var_0_0.STRENGTHEN_TYPE_DIALOGUE:
					for iter_52_3, iter_52_4 in ipairs(iter_52_2[2]):
						if arg_52_1 == iter_52_4:
							return iter_52_0

	return 0

def var_0_0.getBaseList(arg_53_0, arg_53_1):
	assert(arg_53_1, "shipVO can not be None" .. arg_53_0.shipId)

	for iter_53_0 = arg_53_0.level, 1, -1:
		local var_53_0 = arg_53_0.getStrengthenConfig(iter_53_0)

		if var_53_0.special == 1:
			local var_53_1 = var_53_0.special_effect

			for iter_53_1, iter_53_2 in ipairs(var_53_1):
				if iter_53_2[1] == var_0_0.STRENGTHEN_TYPE_BASE_LIST:
					return iter_53_2[2]

	return arg_53_1.getConfig("base_list")

def var_0_0.getPreLoadCount(arg_54_0, arg_54_1):
	assert(arg_54_1, "shipVO can not be None" .. arg_54_0.shipId)

	for iter_54_0 = arg_54_0.level, 1, -1:
		local var_54_0 = arg_54_0.getStrengthenConfig(iter_54_0)

		if var_54_0.special == 1:
			local var_54_1 = var_54_0.special_effect

			for iter_54_1, iter_54_2 in ipairs(var_54_1):
				if iter_54_2[1] == var_0_0.STRENGTHEN_TYPE_PRLOAD_COUNT:
					return iter_54_2[2]

	return arg_54_1.getConfig("preload_count")

def var_0_0.getEquipProficiencyList(arg_55_0, arg_55_1):
	assert(arg_55_1, "shipVO can not be None" .. arg_55_0.shipId)

	local var_55_0 = {}

	for iter_55_0 = 1, arg_55_0.level:
		local var_55_1 = arg_55_0.getStrengthenConfig(iter_55_0)

		if var_55_1.special == 1:
			local var_55_2 = var_55_1.special_effect

			for iter_55_1, iter_55_2 in ipairs(var_55_2):
				if iter_55_2[1] == var_0_0.STRENGTHEN_TYPE_EQUIPMENTPROFICIENCY:
					local var_55_3 = iter_55_2[2][1]
					local var_55_4 = iter_55_2[2][2]

					var_55_0[var_55_3] = (var_55_0[var_55_3] or 0) + var_55_4

	local var_55_5 = Clone(arg_55_1.getConfig("equipment_proficiency"))

	for iter_55_3, iter_55_4 in pairs(var_55_0):
		var_55_5[iter_55_3] = var_55_5[iter_55_3] + iter_55_4

	return var_55_5

def var_0_0.isFinishPrevTask(arg_56_0):
	local var_56_0 = True
	local var_56_1 = True

	for iter_56_0, iter_56_1 in ipairs(arg_56_0.getOpenTaskList()):
		local var_56_2 = getProxy(TaskProxy).getTaskVO(iter_56_1)

		if not var_56_2 or not var_56_2.isFinish():
			return False, False
		else
			var_56_1 = (var_56_2.isReceive() or False) and var_56_1

	return var_56_0, var_56_1

def var_0_0.isShipModMaxLevel(arg_57_0, arg_57_1):
	assert(arg_57_1, "shipVO can not be None" .. arg_57_0.shipId)

	local var_57_0 = arg_57_0.getStrengthenConfig(math.min(arg_57_0.level + 1, arg_57_0.getMaxLevel()))

	if not arg_57_0.isMaxLevel() and arg_57_1.level < var_57_0.need_lv:
		return True, var_57_0.need_lv
	else
		return False

def var_0_0.isShipModMaxFateLevel(arg_58_0, arg_58_1):
	assert(arg_58_1, "shipVO can not be None" .. arg_58_0.shipId)

	local var_58_0 = arg_58_0.getFateStrengthenConfig(math.min(arg_58_0.fateLevel + 1, arg_58_0.getMaxFateLevel()))

	if not arg_58_0.isMaxFateLevel() and arg_58_1.level < var_58_0.need_lv:
		return True, var_58_0.need_lv
	else
		return False

def var_0_0.isShipModMaxIntensifyLevel(arg_59_0, arg_59_1):
	if arg_59_0.canFateSimulation():
		return arg_59_0.isShipModMaxFateLevel(arg_59_1)
	else
		return arg_59_0.isShipModMaxLevel(arg_59_1)

def var_0_0.getChangeSkillList(arg_60_0):
	return arg_60_0.getConfig("change_skill")

def var_0_0.isRarityUR(arg_61_0):
	return arg_61_0.getShipVO().getRarity() >= ShipRarity.SSR

def var_0_0.getFateMaxLeftOver(arg_62_0):
	local var_62_0 = arg_62_0.isRarityUR() and pg.gameset.fate_sim_ur.key_value or pg.gameset.fate_sim_ssr.key_value
	local var_62_1 = var_62_0 - arg_62_0.getFateUseNum()

	return var_62_1 < 0 and var_62_0 or var_62_1

def var_0_0.getFateUseNum(arg_63_0):
	local var_63_0 = 0

	if arg_63_0.isMaxLevel():
		local var_63_1 = 0

		for iter_63_0, iter_63_1 in ipairs(arg_63_0.fateStrengthenConfig):
			if iter_63_1.lv <= 30 + arg_63_0.fateLevel:
				var_63_1 = var_63_1 + iter_63_1.need_exp

		local var_63_2 = var_63_1 + arg_63_0.exp
		local var_63_3 = arg_63_0.getItemExp()

		var_63_0 = math.floor(var_63_2 / var_63_3)

	return var_63_0

def var_0_0.isPursuing(arg_64_0):
	return arg_64_0.getConfig("is_pursuing") == 1

def var_0_0.getPursuingPrice(arg_65_0, arg_65_1):
	arg_65_1 = arg_65_1 or 100

	return arg_65_0.getConfig("price") * arg_65_1 / 100

def var_0_0.getUnlockItem(arg_66_0):
	local var_66_0 = getProxy(BagProxy)

	for iter_66_0, iter_66_1 in ipairs(arg_66_0.getConfig("gain_item_id")):
		if var_66_0.getItemCountById(iter_66_1) > 0:
			return iter_66_1

def var_0_0.isPursuingCostTip(arg_67_0):
	return arg_67_0.isPursuing() and arg_67_0.isUnlock() and not arg_67_0.isMaxIntensifyLevel() and not arg_67_0.isShipModMaxIntensifyLevel(getProxy(BayProxy).getShipById(arg_67_0.shipId)) and getProxy(TechnologyProxy).calcPursuingCost(arg_67_0, 1) == 0

return var_0_0
