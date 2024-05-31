def GetBattleCheck():
	return 0

def GetBattleCheckResult(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = 2621
	local var_2_1 = 3527
	local var_2_2 = GetBattleCheck()

	arg_2_0 = math.floor(arg_2_0 % var_2_0 * (arg_2_1 % var_2_0) % var_2_0 + arg_2_2)

	local var_2_3 = tostring(math.floor(var_2_2 % var_2_1 * (arg_2_1 % var_2_1) % (var_2_1 + arg_2_0)))

	return arg_2_0, var_2_3

ys.BattleShipLevelVertify = {}
