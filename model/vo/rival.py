local var_0_0 = class("Rival", import(".PlayerAttire"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.id = arg_1_1.id
	arg_1_0.level = arg_1_1.level
	arg_1_0.name = arg_1_1.name
	arg_1_0.score = arg_1_1.score or 0
	arg_1_0.rank = arg_1_1.rank
	arg_1_0.vanguardShips = {}
	arg_1_0.mainShips = {}

	local function var_1_0(arg_2_0)
		if arg_2_0.getTeamType() == TeamType.Vanguard:
			table.insert(arg_1_0.vanguardShips, arg_2_0)
		elif arg_2_0.getTeamType() == TeamType.Main:
			table.insert(arg_1_0.mainShips, arg_2_0)

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.vanguard_ship_list):
		local var_1_1 = RivalShip.New(iter_1_1)

		var_1_1.isRival = True

		var_1_0(var_1_1)

	for iter_1_2, iter_1_3 in ipairs(arg_1_1.main_ship_list):
		local var_1_2 = RivalShip.New(iter_1_3)

		var_1_2.isRival = True

		var_1_0(var_1_2)

	arg_1_0.score = arg_1_0.score + SeasonInfo.INIT_POINT

def var_0_0.getPainting(arg_3_0):
	local var_3_0 = pg.ship_skin_template[arg_3_0.skinId]

	return var_3_0 and var_3_0.painting or "unknown"

def var_0_0.getShips(arg_4_0):
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.vanguardShips):
		table.insert(var_4_0, iter_4_1)

	for iter_4_2, iter_4_3 in ipairs(arg_4_0.mainShips):
		table.insert(var_4_0, iter_4_3)

	return var_4_0

def var_0_0.GetGearScoreSum(arg_5_0, arg_5_1):
	local var_5_0

	if arg_5_1 == "main":
		var_5_0 = arg_5_0.mainShips
	elif arg_5_1 == "vanguard":
		var_5_0 = arg_5_0.vanguardShips

	local var_5_1 = 0

	for iter_5_0, iter_5_1 in ipairs(var_5_0):
		var_5_1 = var_5_1 + iter_5_1.getShipCombatPower()

	return var_5_1

return var_0_0
