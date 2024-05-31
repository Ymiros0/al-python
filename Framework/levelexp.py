def prepareLevelExpConfig(arg_1_0, arg_1_1):
	arg_1_1 = arg_1_1 or "exp"

	local var_1_0

	for iter_1_0, iter_1_1 in ipairs(arg_1_0.all):
		local var_1_1 = arg_1_0[iter_1_1]

		var_1_1.level0 = iter_1_0 - 1
		var_1_1.level1 = iter_1_0

		if not var_1_0:
			var_1_1[arg_1_1 .. "_start"] = 0
		else
			var_1_1[arg_1_1 .. "_start"] = var_1_0[arg_1_1 .. "_start"] + var_1_0[arg_1_1 .. "_interval"]

		var_1_1[arg_1_1 .. "_interval"] = var_1_1[arg_1_1]
		var_1_1[arg_1_1 .. "_end"] = var_1_1[arg_1_1 .. "_start"] + var_1_1[arg_1_1] - 1
		var_1_0 = var_1_1

def getConfigFromTotalExp(arg_2_0, arg_2_1, arg_2_2):
	arg_2_2 = arg_2_2 or "exp"

	local var_2_0

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.all):
		var_2_0 = arg_2_0[iter_2_1]

		if arg_2_1 < var_2_0[arg_2_2 .. "_end"]:
			return var_2_0

	return var_2_0

def getConfigFromLevel0(arg_3_0, arg_3_1):
	return arg_3_0[arg_3_1 + 1] or arg_3_0[#arg_3_0]

def getConfigFromLevel1(arg_4_0, arg_4_1):
	return arg_4_0[arg_4_1] or arg_4_0[#arg_4_0]

def getExpByRarityFromLv1(arg_5_0, arg_5_1):
	local var_5_0 = getConfigFromLevel1(pg.ship_level, arg_5_1)

	if arg_5_0 >= ShipRarity.SSR:
		return var_5_0.exp_ur
	else
		return var_5_0.exp

prepareLevelExpConfig(pg.user_level)
prepareLevelExpConfig(pg.ship_level)
prepareLevelExpConfig(pg.ship_level, "exp_ur")
