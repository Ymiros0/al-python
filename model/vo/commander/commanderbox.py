local var_0_0 = class("CommanderBox", import("..BaseVO"))

var_0_0.STATE_EMPTY = -1
var_0_0.STATE_WAITING = 0
var_0_0.STATE_STARTING = 1
var_0_0.STATE_FINISHED = 2

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.id = arg_1_1.id
	arg_1_0.index = arg_1_2 or 99
	arg_1_0.configId = arg_1_0.id
	arg_1_0.finishTime = arg_1_1.finish_time or 0
	arg_1_0.beginTime = arg_1_1.begin_time or 0

	local var_1_0 = arg_1_1.poolId or 0

	if var_1_0 and var_1_0 > 0:
		arg_1_0.pool = getProxy(CommanderProxy).getPoolById(var_1_0)

def var_0_0.getPool(arg_2_0):
	return arg_2_0.pool

def var_0_0.getFinishTime(arg_3_0):
	return arg_3_0.finishTime

def var_0_0.ReduceFinishTime(arg_4_0, arg_4_1):
	arg_4_0.finishTime = math.max(arg_4_0.beginTime, arg_4_0.finishTime - arg_4_1)

def var_0_0.costTime(arg_5_0):
	local var_5_0 = arg_5_0.getState()

	if var_5_0 == var_0_0.STATE_STARTING or var_5_0 == var_0_0.STATE_FINISHED:
		return arg_5_0.finishTime - arg_5_0.beginTime
	else
		return 0

def var_0_0.getState(arg_6_0):
	local var_6_0 = pg.TimeMgr.GetInstance().GetServerTime()

	if arg_6_0.finishTime == 0:
		return var_0_0.STATE_EMPTY
	elif var_6_0 >= arg_6_0.finishTime:
		return var_0_0.STATE_FINISHED
	elif arg_6_0.finishTime > 0 and var_6_0 < arg_6_0.beginTime:
		return var_0_0.STATE_WAITING
	elif arg_6_0.finishTime > 0 and var_6_0 < arg_6_0.finishTime:
		return var_0_0.STATE_STARTING

def var_0_0.finish(arg_7_0):
	arg_7_0.finishTime = 0
	arg_7_0.beginTime = 0

def var_0_0.getPrefab(arg_8_0):
	if not arg_8_0.rarity2Str:
		arg_8_0.rarity2Str = {
			"",
			"SR",
			"SSR"
		}

	if arg_8_0.pool:
		local var_8_0 = arg_8_0.rarity2Str[arg_8_0.pool.getRarity()]
		local var_8_1 = arg_8_0.getState()

		if var_8_1 == var_0_0.STATE_WAITING:
			return var_8_0 .. "NekoBox1"
		elif var_8_1 == var_0_0.STATE_STARTING:
			return var_8_0 .. "NekoBox2"
		elif var_8_1 == var_0_0.STATE_FINISHED:
			return var_8_0 .. "NekoBox3"
	else
		return None

def var_0_0.getFetchPrefab(arg_9_0):
	if not arg_9_0.rarity2Str:
		arg_9_0.rarity2Str = {
			"",
			"SR",
			"SSR"
		}

	assert(arg_9_0.pool)

	return arg_9_0.rarity2Str[arg_9_0.pool.getRarity()] .. "NekoBox4"

def var_0_0.IsSsr(arg_10_0):
	return arg_10_0.pool.getRarity() == 3

def var_0_0.IsSr(arg_11_0):
	return arg_11_0.pool.getRarity() == 2

def var_0_0.IsR(arg_12_0):
	return arg_12_0.pool.getRarity() == 1

return var_0_0
