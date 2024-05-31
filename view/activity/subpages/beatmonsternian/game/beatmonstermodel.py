local var_0_0 = class("BeatMonsterModel")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.controller = arg_1_1
	arg_1_0.fuShun = None
	arg_1_0.mosterNian = None
	arg_1_0.attackCnt = 0
	arg_1_0.actionStr = ""

def var_0_0.AddFuShun(arg_2_0):
	arg_2_0.fuShun = {}

def var_0_0.AddMonsterNian(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.mosterNian = {
		hp = arg_3_1,
		maxHp = arg_3_2
	}

def var_0_0.UpdateMonsterHp(arg_4_0, arg_4_1):
	arg_4_0.mosterNian.hp = arg_4_1

def var_0_0.UpdateData(arg_5_0, arg_5_1):
	arg_5_0.UpdateMonsterHp(arg_5_1.hp)

	arg_5_0.mosterNian.maxHp = arg_5_1.maxHp

	arg_5_0.SetAttackCnt(arg_5_1.leftCount)

def var_0_0.SetAttackCnt(arg_6_0, arg_6_1):
	arg_6_0.attackCnt = arg_6_1

def var_0_0.UpdateActionStr(arg_7_0, arg_7_1):
	if not arg_7_1 or arg_7_1 == "":
		arg_7_0.actionStr = ""
	else
		arg_7_0.actionStr = arg_7_0.actionStr .. arg_7_1

def var_0_0.SetStorys(arg_8_0, arg_8_1):
	arg_8_0.storys = arg_8_1

def var_0_0.GetPlayableStory(arg_9_0):
	local var_9_0 = arg_9_0.storys

	if not var_9_0 or type(var_9_0) != "table":
		return

	local var_9_1 = pg.NewStoryMgr.GetInstance()

	for iter_9_0, iter_9_1 in pairs(var_9_0):
		local var_9_2 = iter_9_1[1]
		local var_9_3 = iter_9_1[2]

		if var_9_2 >= arg_9_0.mosterNian.hp and not var_9_1.IsPlayed(var_9_3):
			return var_9_3

def var_0_0.GetActionStr(arg_10_0):
	return arg_10_0.actionStr

def var_0_0.IsMatchAction(arg_11_0):
	return BeatMonsterNianConst.MatchAction(arg_11_0.actionStr)

def var_0_0.GetMatchAction(arg_12_0):
	return BeatMonsterNianConst.GetMatchAction(arg_12_0.actionStr)

def var_0_0.GetMonsterAction(arg_13_0):
	return BeatMonsterNianConst.GetMonsterAction(arg_13_0.actionStr)

def var_0_0.RandomDamage(arg_14_0):
	local var_14_0 = math.random(1, 2)

	return math.max(arg_14_0.mosterNian.hp - var_14_0, 0)

def var_0_0.GetMonsterMaxHp(arg_15_0):
	return arg_15_0.mosterNian.maxHp

def var_0_0.GetAttackCount(arg_16_0):
	return arg_16_0.attackCnt

def var_0_0.Dispose(arg_17_0):
	return

return var_0_0
