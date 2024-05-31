local var_0_0 = class("Challenge2Fleet", import(".Fleet"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id

	arg_1_0.updateShips(arg_1_1.ships)

	arg_1_0.commanderList = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.commanders or {}):
		arg_1_0.commanderList[iter_1_1.pos] = Commander.New(iter_1_1.commanderinfo)

	arg_1_0.skills = {}

	arg_1_0.updateCommanderSkills()

def var_0_0.getShipsByTeam(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0[arg_2_1]):
		if iter_2_1.hpRant > 0:
			var_2_0[#var_2_0 + 1] = iter_2_1

	if arg_2_2:
		for iter_2_2, iter_2_3 in ipairs(arg_2_0[arg_2_1]):
			if iter_2_3.hpRant <= 0:
				var_2_0[#var_2_0 + 1] = iter_2_3

	return var_2_0

def var_0_0.getTeamByName(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0[arg_3_1]
	local var_3_1 = {}

	for iter_3_0, iter_3_1 in pairs(var_3_0):
		table.insert(var_3_1, iter_3_1.id)

	return var_3_1

def var_0_0.getFleetType(arg_4_0):
	for iter_4_0, iter_4_1 in pairs(arg_4_0.ships):
		if iter_4_1.getTeamType() == TeamType.Submarine:
			return FleetType.Submarine

	return FleetType.Normal

def var_0_0.getShips(arg_5_0, arg_5_1):
	local var_5_0 = {}
	local var_5_1 = arg_5_0.getFleetType()

	if var_5_1 == FleetType.Normal:
		_.each(arg_5_0.getShipsByTeam(TeamType.Main, arg_5_1), function(arg_6_0)
			table.insert(var_5_0, arg_6_0))
		_.each(arg_5_0.getShipsByTeam(TeamType.Vanguard, arg_5_1), function(arg_7_0)
			table.insert(var_5_0, arg_7_0))
	elif var_5_1 == FleetType.Submarine:
		_.each(arg_5_0.getShipsByTeam(TeamType.Submarine, arg_5_1), function(arg_8_0)
			table.insert(var_5_0, arg_8_0))

	return var_5_0

def var_0_0.updateShips(arg_9_0, arg_9_1):
	arg_9_0[TeamType.Vanguard] = {}
	arg_9_0[TeamType.Main] = {}
	arg_9_0[TeamType.Submarine] = {}
	arg_9_0.ships = {}

	_.each(arg_9_1 or {}, function(arg_10_0)
		local var_10_0 = Ship.New(arg_10_0.ship_info)

		var_10_0.hpRant = arg_10_0.hp_rant
		arg_9_0.ships[var_10_0.id] = var_10_0

		table.insert(arg_9_0[var_10_0.getTeamType()], var_10_0))

def var_0_0.updateShipsHP(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0 = arg_11_0.ships[arg_11_1]

	if var_11_0:
		var_11_0.hpRant = arg_11_2

		return True
	else
		return False

def var_0_0.getCommanders(arg_12_0):
	return arg_12_0.commanderList

def var_0_0.switchShip(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	local var_13_0 = arg_13_0.getShipsByTeam(arg_13_1, False)
	local var_13_1 = var_13_0[arg_13_2].id
	local var_13_2 = var_13_0[arg_13_3].id
	local var_13_3
	local var_13_4
	local var_13_5
	local var_13_6

	for iter_13_0, iter_13_1 in pairs(arg_13_0.ships):
		if iter_13_0 == var_13_1:
			var_13_3 = iter_13_1.getTeamType()
			var_13_4 = table.indexof(arg_13_0[var_13_3], iter_13_1)

		if iter_13_0 == var_13_2:
			var_13_5 = iter_13_1.getTeamType()
			var_13_6 = table.indexof(arg_13_0[var_13_5], iter_13_1)

	if var_13_3 == var_13_5 and var_13_4 != var_13_6:
		arg_13_0[var_13_3][var_13_4], arg_13_0[var_13_5][var_13_6] = arg_13_0[var_13_5][var_13_6], arg_13_0[var_13_3][var_13_4]

def var_0_0.buildBattleBuffList(arg_14_0):
	local var_14_0 = {}
	local var_14_1, var_14_2 = FleetSkill.triggerMirrorSkill(arg_14_0, FleetSkill.TypeBattleBuff)

	if var_14_1 and #var_14_1 > 0:
		local var_14_3 = {}

		for iter_14_0, iter_14_1 in ipairs(var_14_1):
			local var_14_4 = var_14_2[iter_14_0]
			local var_14_5 = arg_14_0.findCommanderBySkillId(var_14_4.id)

			var_14_3[var_14_5] = var_14_3[var_14_5] or {}

			table.insert(var_14_3[var_14_5], iter_14_1)

		for iter_14_2, iter_14_3 in pairs(var_14_3):
			table.insert(var_14_0, {
				iter_14_2,
				iter_14_3
			})

	local var_14_6 = arg_14_0.getCommanders()

	for iter_14_4, iter_14_5 in pairs(var_14_6):
		local var_14_7 = iter_14_5.getTalents()

		for iter_14_6, iter_14_7 in ipairs(var_14_7):
			local var_14_8 = iter_14_7.getBuffsAddition()

			if #var_14_8 > 0:
				local var_14_9

				for iter_14_8, iter_14_9 in ipairs(var_14_0):
					if iter_14_9[1] == iter_14_5:
						var_14_9 = iter_14_9[2]

						break

				if not var_14_9:
					var_14_9 = {}

					table.insert(var_14_0, {
						iter_14_5,
						var_14_9
					})

				for iter_14_10, iter_14_11 in ipairs(var_14_8):
					table.insert(var_14_9, iter_14_11)

	return var_14_0

return var_0_0
