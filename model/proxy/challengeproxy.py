local var_0_0 = class("ChallengeProxy", import(".NetProxy"))

var_0_0.MODE_CASUAL = 0
var_0_0.MODE_INFINITE = 1

def var_0_0.register(arg_1_0):
	arg_1_0._curMode = var_0_0.MODE_CASUAL
	arg_1_0._challengeInfo = None
	arg_1_0._userChallengeList = {}

	arg_1_0.on(24010, function(arg_2_0)
		arg_1_0.updateCombatScore(arg_2_0.score))

def var_0_0.userSeaonExpire(arg_3_0, arg_3_1):
	if arg_3_0._challengeInfo.getSeasonID() != arg_3_0._userChallengeList[arg_3_1].getSeasonID():
		return True
	else
		return False

def var_0_0.updateCombatScore(arg_4_0, arg_4_1):
	arg_4_0.getUserChallengeInfo(arg_4_0._curMode).updateCombatScore(arg_4_1)

def var_0_0.updateSeasonChallenge(arg_5_0, arg_5_1):
	if not arg_5_0._challengeInfo:
		arg_5_0._challengeInfo = ChallengeInfo.New(arg_5_1)
	else
		arg_5_0._challengeInfo.UpdateChallengeInfo(arg_5_1)

def var_0_0.updateCurrentChallenge(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.mode
	local var_6_1 = arg_6_0._userChallengeList[var_6_0]

	if var_6_1 == None:
		arg_6_0._userChallengeList[var_6_0] = UserChallengeInfo.New(arg_6_1)
	else
		var_6_1.UpdateChallengeInfo(arg_6_1)

def var_0_0.GetCurrentChallenge(arg_7_0, arg_7_1):
	return arg_7_0._userChallengeList

def var_0_0.getCurMode(arg_8_0):
	return arg_8_0._curMode

def var_0_0.setCurMode(arg_9_0, arg_9_1):
	if arg_9_1 == var_0_0.MODE_CASUAL:
		arg_9_0._curMode = var_0_0.MODE_CASUAL
	elif arg_9_1 == var_0_0.MODE_INFINITE:
		arg_9_0._curMode = var_0_0.MODE_INFINITE
	else
		assert(False, "challenge mode undefined")

def var_0_0.getChallengeInfo(arg_10_0):
	return arg_10_0._challengeInfo

def var_0_0.getUserChallengeInfoList(arg_11_0):
	return arg_11_0._userChallengeList

def var_0_0.getUserChallengeInfo(arg_12_0, arg_12_1):
	return arg_12_0._userChallengeList[arg_12_1]

def var_0_0.WriteBackOnExitBattleResult(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = arg_13_0.getUserChallengeInfo(arg_13_2)

	if arg_13_1 < ys.Battle.BattleConst.BattleScore.S:
		arg_13_0.sendNotification(GAME.CHALLENGE2_RESET, {
			mode = arg_13_2
		})
	else
		local var_13_1 = var_13_0.IsFinish()

		var_13_0.updateLevelForward()

		if var_13_0.getMode() == ChallengeProxy.MODE_INFINITE and var_13_1:
			var_13_0.setInfiniteDungeonIDListByLevel()

	local var_13_2 = arg_13_0.getChallengeInfo()

	if not arg_13_0.userSeaonExpire(var_13_0.getMode()):
		var_13_2.checkRecord(var_13_0)

return var_0_0
