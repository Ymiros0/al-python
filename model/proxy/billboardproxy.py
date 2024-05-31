local var_0_0 = class("BillboardProxy", import(".NetProxy"))

var_0_0.FETCH_LIST_DONE = "BillboardProxy.FETCH_LIST_DONE"
var_0_0.NONTIMER = {}

def var_0_0.register(arg_1_0):
	var_0_0.NONTIMER = {
		PowerRank.TYPE_MILITARY_RANK,
		PowerRank.TYPE_BOSSRUSH
	}
	arg_1_0.data = {}
	arg_1_0.playerData = {}
	arg_1_0.timeStamps = {}
	arg_1_0.hashList = {}
	arg_1_0.hashCount = 0

def var_0_0.setPlayerRankData(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	local var_2_0 = arg_2_0.getHashId(arg_2_1, arg_2_2)

	if table.contains(var_0_0.NONTIMER, arg_2_1):
		return

	arg_2_0.playerData[var_2_0] = arg_2_3

def var_0_0.getPlayerRankData(arg_3_0, arg_3_1, arg_3_2):
	return arg_3_0.playerData[arg_3_0.getHashId(arg_3_1, arg_3_2)]

def var_0_0.setRankList(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	local var_4_0 = arg_4_0.getHashId(arg_4_1, arg_4_2)

	if table.contains(var_0_0.NONTIMER, arg_4_1):
		return

	arg_4_0.data[var_4_0] = arg_4_3
	arg_4_0.timeStamps[var_4_0] = GetHalfHour()

def var_0_0.getRankList(arg_5_0, arg_5_1, arg_5_2):
	return arg_5_0.data[arg_5_0.getHashId(arg_5_1, arg_5_2)]

def var_0_0.canFetch(arg_6_0, arg_6_1, arg_6_2):
	if table.contains(var_0_0.NONTIMER, arg_6_1):
		return True

	local var_6_0 = arg_6_0.getHashId(arg_6_1, arg_6_2)

	if not arg_6_0.timeStamps[var_6_0] or pg.TimeMgr.GetInstance().GetServerTime() > arg_6_0.timeStamps[var_6_0]:
		return True

	return False

def var_0_0.getHashId(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0

	if arg_7_2:
		arg_7_0.hashList[arg_7_1] = arg_7_0.hashList[arg_7_1] or {}
		var_7_0 = arg_7_0.hashList[arg_7_1][arg_7_2]
	else
		var_7_0 = arg_7_0.hashList[arg_7_1]

	if var_7_0:
		return var_7_0
	else
		arg_7_0.hashCount = arg_7_0.hashCount + 1

		if arg_7_2:
			arg_7_0.hashList[arg_7_1][arg_7_2] = arg_7_0.hashCount
		else
			arg_7_0.hashList[arg_7_1] = arg_7_0.hashCount

		return arg_7_0.hashCount

return var_0_0
