local var_0_0 = class("SeasonInfo", import(".BaseVO"))

var_0_0.RECOVER_UP_COUNT = 5
var_0_0.MAX_FIGHTCOUNT = 10
var_0_0.RECOVER_UP_SIX_HOUR = 6
var_0_0.RECOVER_UP_TWELVE_HOUR = 12
var_0_0.INIT_POINT = pg.arena_data_rank[1].point
var_0_0.ONE_SEASON_TIME = 1209600
var_0_0.preRivals = {}

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.score = arg_1_1.score or 0
	arg_1_0.rank = arg_1_1.rank
	arg_1_0.fightCount = arg_1_1.fight_count
	arg_1_0.resetTime = arg_1_1.fight_count_reset_time
	arg_1_0.flashTargetCount = arg_1_1.flash_target_count + 1
	arg_1_0.score = arg_1_0.score + var_0_0.INIT_POINT

	local var_1_0 = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.vanguard_ship_id_list):
		table.insert(var_1_0, iter_1_1)

	for iter_1_2, iter_1_3 in ipairs(arg_1_1.main_ship_id_list):
		table.insert(var_1_0, iter_1_3)

	arg_1_0.fleet = TypedFleet.New({
		saveLastShipFlag = True,
		ship_list = var_1_0,
		fleetType = FleetType.Normal
	})
	arg_1_0.rivals = {}

	for iter_1_4, iter_1_5 in ipairs(arg_1_1.target_list):
		local var_1_1 = Rival.New(iter_1_5)

		table.insert(arg_1_0.rivals, var_1_1)

		var_0_0.preRivals[var_1_1.id] = var_1_1

def var_0_0.getFlashCount(arg_2_0):
	return arg_2_0.flashTargetCount

def var_0_0.increaseFlashCount(arg_3_0):
	arg_3_0.flashTargetCount = arg_3_0.flashTargetCount + 1

def var_0_0.resetFlashCount(arg_4_0):
	arg_4_0.flashTargetCount = 0

def var_0_0.getconsumeGem(arg_5_0):
	local var_5_0 = arg_5_0.getMilitaryRank(arg_5_0.score, arg_5_0.rank)

	return var_5_0.refresh_price[arg_5_0.flashTargetCount] or var_5_0.refresh_price[#var_5_0.refresh_price]

def var_0_0.updateRank(arg_6_0, arg_6_1):
	arg_6_0.rank = arg_6_1

def var_0_0.updateScore(arg_7_0, arg_7_1):
	arg_7_0.score = arg_7_1

def var_0_0.getRivals(arg_8_0):
	return Clone(arg_8_0.rivals)

def var_0_0.updateRivals(arg_9_0, arg_9_1):
	for iter_9_0, iter_9_1 in pairs(arg_9_0.rivals):
		var_0_0.preRivals[iter_9_1.id] = iter_9_1

	arg_9_0.rivals = arg_9_1

def var_0_0.GetPreRivals(arg_10_0):
	return var_0_0.preRivals

def var_0_0.updateFleet(arg_11_0, arg_11_1):
	arg_11_0.fleet = arg_11_1

def var_0_0.canExercise(arg_12_0):
	return arg_12_0.fightCount > 0

def var_0_0.reduceExerciseCount(arg_13_0):
	assert(arg_13_0.fightCount > 0, "演习次数必须大于0")

	arg_13_0.fightCount = arg_13_0.fightCount - 1

def var_0_0.updateExerciseCount(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_0.fightCount + arg_14_1

	arg_14_0.fightCount = math.min(var_14_0, var_0_0.MAX_FIGHTCOUNT)

def var_0_0.setExerciseCount(arg_15_0, arg_15_1):
	arg_15_0.fightCount = arg_15_1

def var_0_0.updateResetTime(arg_16_0, arg_16_1):
	arg_16_0.resetTime = arg_16_1

def var_0_0.getMilitaryRank(arg_17_0, arg_17_1):
	local var_17_0
	local var_17_1 = pg.arena_data_rank

	for iter_17_0 = #var_17_1.all, 1, -1:
		local var_17_2 = var_17_1.all[iter_17_0]
		local var_17_3 = var_17_1[var_17_2].point
		local var_17_4 = var_17_1[var_17_2].order

		if var_17_1[var_17_2].order != 0:
			if arg_17_1 <= var_17_4 and var_17_3 <= arg_17_0:
				var_17_0 = var_17_1[var_17_2]

				break
		elif var_17_3 <= arg_17_0:
			var_17_0 = var_17_1[var_17_2]

			break

	var_17_0 = var_17_0 or var_17_1[var_17_1.all[1]]

	return var_17_0

def var_0_0.getNextMilitaryRank(arg_18_0, arg_18_1):
	local var_18_0 = var_0_0.getMilitaryRank(arg_18_0, arg_18_1)
	local var_18_1 = pg.arena_data_rank[var_18_0.id + 1] or pg.arena_data_rank[#pg.arena_data_rank.all]

	return var_18_1.name, var_18_1.point, var_18_1.order

def var_0_0.maxRankScore():
	local var_19_0 = pg.arena_data_rank
	local var_19_1 = var_19_0[var_19_0.all[#var_19_0.all]]

	return var_19_1.name, var_19_1.point

def var_0_0.getEmblem(arg_20_0, arg_20_1):
	local var_20_0 = var_0_0.getMilitaryRank(arg_20_0, arg_20_1)

	return math.min(math.max(var_20_0.id, 1), 14)

def var_0_0.getMainShipIds(arg_21_0):
	return arg_21_0.fleet.mainShips

def var_0_0.getVanguardShipIds(arg_22_0):
	return arg_22_0.fleet.vanguardShips

def var_0_0.getMainFleetShipCount(arg_23_0):
	return table.getCount(arg_23_0.mainShips)

def var_0_0.getVanguardShipsShipCount(arg_24_0):
	return table.getCount(arg_24_0.vanguardShips)

return var_0_0
