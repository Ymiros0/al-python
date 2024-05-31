local var_0_0 = class("VoteFunRaceRankPage", import("..FinalsRece.VoteFinalsRaceRankPage"))

def var_0_0.getUIName(arg_1_0):
	local var_1_0 = arg_1_0.contextData.voteGroup

	if var_1_0.IsFunMetaRace():
		return "FinalsRaceRankForMeta"
	elif var_1_0.IsFunSireRace():
		return "FinalsRaceRankForSire"
	elif var_1_0.IsFunKidRace():
		return "FinalsRaceRankForKid"
	else
		assert(False)

return var_0_0
