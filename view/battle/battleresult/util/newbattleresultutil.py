local var_0_0 = class("NewBattleResultUtil")

def var_0_0.Score2Grade(arg_1_0, arg_1_1):
	local var_1_0 = {
		"d",
		"c",
		"b",
		"a",
		"s"
	}
	local var_1_1
	local var_1_2
	local var_1_3

	if arg_1_0 > 0:
		var_1_3 = var_1_0[arg_1_0 + 1]
		var_1_1 = "battlescore/battle_score_" .. var_1_3 .. "/letter_" .. var_1_3
		var_1_2 = "battlescore/battle_score_" .. var_1_3 .. "/label_" .. var_1_3
	else
		local var_1_4

		if arg_1_1 == ys.Battle.BattleConst.DEAD_FLAG:
			var_1_3 = var_1_0[2]
			var_1_4 = "flag_destroy"
		else
			var_1_3 = var_1_0[1]

		var_1_1 = "battlescore/battle_score_" .. var_1_3 .. "/letter_" .. var_1_3
		var_1_2 = "battlescore/battle_score_" .. var_1_3 .. "/label_" .. (var_1_4 or var_1_3)

	return var_1_1, var_1_2

def var_0_0.Score2Bg(arg_2_0):
	return arg_2_0 > 1 and "Victory" or "Failed"

def var_0_0.GetChapterName(arg_3_0):
	local var_3_0 = pg.expedition_data_template[arg_3_0.stageId]

	return var_3_0 and var_3_0.name or ""

local function var_0_1(arg_4_0, arg_4_1)
	if arg_4_0 == 1 or arg_4_0 == 4 or arg_4_0 == 8:
		return arg_4_1.score > 1
	elif arg_4_0 == 2 or arg_4_0 == 3:
		return not arg_4_1.statistics._deadUnit
	elif arg_4_0 == 6:
		return arg_4_1.statistics._boss_destruct < 1
	elif arg_4_0 == 5:
		return not arg_4_1.statistics._badTime
	elif arg_4_0 == 7:
		return True

	return None

local function var_0_2(arg_5_0)
	return ({
		"battle_result_victory",
		"battle_result_undefeated",
		"battle_result_sink_limit",
		"battle_preCombatLayer_time_hold",
		"battle_result_time_limit",
		"battle_result_boss_destruct",
		"battle_preCombatLayer_damage_before_end",
		"battle_result_defeat_all_enemys"
	})[arg_5_0]

def var_0_0.ColorObjective(arg_6_0):
	local var_6_0
	local var_6_1
	local var_6_2

	if arg_6_0 == None:
		var_6_0 = "check_mark"
		var_6_2 = "#FFFFFFFF"
	elif arg_6_0 == True:
		var_6_0 = "jiesuan_bg22"
		var_6_2 = "#FFFFFFFF"
	else
		var_6_0 = "jiesuan_bg23"
		var_6_2 = "#FFFFFF80"

	return var_6_0, var_6_2

def var_0_0.GetObjectives(arg_7_0):
	local var_7_0 = {}
	local var_7_1 = pg.expedition_data_template[arg_7_0.stageId]

	local function var_7_2(arg_8_0)
		if not arg_8_0 or type(arg_8_0) != "table":
			return

		local var_8_0 = i18n(var_0_2(arg_8_0[1]), arg_8_0[2])
		local var_8_1 = var_0_1(arg_8_0[1], arg_7_0)
		local var_8_2, var_8_3 = var_0_0.ColorObjective(var_8_1)

		table.insert(var_7_0, {
			text = setColorStr(var_8_0, var_8_3),
			icon = var_8_2
		})

	for iter_7_0 = 1, 3:
		var_7_2(var_7_1["objective_" .. iter_7_0])

	return var_7_0

def var_0_0.IsOpBonus(arg_9_0):
	for iter_9_0, iter_9_1 in ipairs(arg_9_0):
		if pg.benefit_buff_template[iter_9_1].benefit_type == Chapter.OPERATION_BUFF_TYPE_EXP:
			return True

	return False

def var_0_0.GetPlayerExpOffset(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_0
	local var_10_1 = var_10_0.level
	local var_10_2 = arg_10_1.level
	local var_10_3 = arg_10_1.exp - var_10_0.exp

	while var_10_1 < var_10_2:
		var_10_3 = var_10_3 + pg.user_level[var_10_1].exp
		var_10_1 = var_10_1 + 1

	if var_10_1 == pg.user_level[#pg.user_level].level:
		var_10_3 = 0

	return var_10_3

def var_0_0.HasSubShip(arg_11_0):
	for iter_11_0, iter_11_1 in ipairs(arg_11_0):
		local var_11_0 = ys.Battle.BattleDataFunction.GetPlayerShipTmpDataFromID(iter_11_1.configId).type

		if table.contains(TeamType.SubShipType, var_11_0):
			return True

	return False

def var_0_0.HasSurfaceShip(arg_12_0):
	for iter_12_0, iter_12_1 in ipairs(arg_12_0):
		local var_12_0 = ys.Battle.BattleDataFunction.GetPlayerShipTmpDataFromID(iter_12_1.configId).type

		if not table.contains(TeamType.SubShipType, var_12_0):
			return True

	return False

def var_0_0.SeparateSurfaceAndSubShips(arg_13_0):
	local var_13_0 = {}
	local var_13_1 = {}

	for iter_13_0, iter_13_1 in ipairs(arg_13_0):
		local var_13_2 = ys.Battle.BattleDataFunction.GetPlayerShipTmpDataFromID(iter_13_1.configId).type

		if table.contains(TeamType.SubShipType, var_13_2):
			table.insert(var_13_1, iter_13_1)
		else
			table.insert(var_13_0, iter_13_1)

	return var_13_0, var_13_1

def var_0_0.SeparateMvpShip(arg_14_0, arg_14_1, arg_14_2):
	if not arg_14_1 or arg_14_1 == 0:
		arg_14_1 = arg_14_2

	local var_14_0
	local var_14_1 = {}
	local var_14_2 = {}
	local var_14_3 = {}

	for iter_14_0, iter_14_1 in ipairs(arg_14_0):
		if iter_14_1.id != arg_14_1:
			local var_14_4 = ys.Battle.BattleDataFunction.GetPlayerShipTmpDataFromID(iter_14_1.configId).type
			local var_14_5 = TeamType.GetTeamFromShipType(var_14_4)

			if var_14_5 == TeamType.Vanguard:
				table.insert(var_14_1, iter_14_1)
			elif var_14_5 == TeamType.Main:
				table.insert(var_14_2, iter_14_1)
			elif var_14_5 == TeamType.Submarine:
				table.insert(var_14_3, iter_14_1)
		else
			var_14_0 = iter_14_1

	return var_14_1, var_14_2, var_14_3, var_14_0

def var_0_0.SpecialInsertItem(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4):
	for iter_15_0, iter_15_1 in ipairs(arg_15_1):
		table.insert(arg_15_0, iter_15_1)

	for iter_15_2, iter_15_3 in ipairs(arg_15_2):
		table.insert(arg_15_0, iter_15_3)

	for iter_15_4, iter_15_5 in ipairs(arg_15_3):
		table.insert(arg_15_0, iter_15_5)

	table.insert(arg_15_0, #arg_15_0, arg_15_4)

def var_0_0.GetShipExpOffset(arg_16_0, arg_16_1):
	assert(arg_16_1, arg_16_0.getConfig("name"))

	if arg_16_0.level < arg_16_1.level:
		local var_16_0 = arg_16_0.getConfig("rarity")
		local var_16_1 = 0

		for iter_16_0 = arg_16_0.level, arg_16_1.level - 1:
			var_16_1 = var_16_1 + getExpByRarityFromLv1(var_16_0, iter_16_0)

		return var_16_1 + arg_16_1.getExp() - arg_16_0.getExp()
	else
		return math.ceil(arg_16_1.getExp() - arg_16_0.getExp())

def var_0_0.GetSeasonScoreOffset(arg_17_0, arg_17_1):
	return arg_17_1.score - arg_17_0.score

def var_0_0.GetMaxOutput(arg_18_0, arg_18_1):
	local var_18_0 = 0

	if arg_18_1.mvpShipID == -1:
		for iter_18_0, iter_18_1 in ipairs(arg_18_0):
			local var_18_1 = arg_18_1[iter_18_1.id] or {}

			var_18_0 = math.max(var_18_1.output or 0, var_18_0)
	elif arg_18_1.mvpShipID and arg_18_1.mvpShipID != 0:
		var_18_0 = (arg_18_1[arg_18_1.mvpShipID] or {}).output or 0

	return var_18_0

def var_0_0.RemoveNonStatisticShips(arg_19_0, arg_19_1):
	local var_19_0 = {}

	for iter_19_0, iter_19_1 in ipairs(arg_19_0):
		if arg_19_1[iter_19_1.id]:
			table.insert(var_19_0, iter_19_1)

	return var_19_0

return var_0_0
