local var_0_0 = class("VoteFunRaceShipsPageForRank", import("..FinalsRece.VoteFinalsRaceShipsPageForRank"))

def var_0_0.getUIName(arg_1_0):
	local var_1_0 = arg_1_0.contextData.voteGroup

	if var_1_0.IsFunMetaRace():
		return "FinalsRaceShipsRankForMeta"
	elif var_1_0.IsFunSireRace():
		return "FinalsRaceShipsRankForSire"
	elif var_1_0.IsFunKidRace():
		return "FinalsRaceShipsRankForKid"
	else
		assert(False)

return var_0_0
