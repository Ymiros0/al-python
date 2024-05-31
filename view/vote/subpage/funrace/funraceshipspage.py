local var_0_0 = class("FunRaceShipsPage", import("..FinalsRece.VoteFinalsRaceShipsPage"))

def var_0_0.getUIName(arg_1_0):
	local var_1_0 = arg_1_0.contextData.voteGroup

	if var_1_0.IsFunMetaRace():
		return "FinalsRaceShipsForMeta"
	elif var_1_0.IsFunSireRace():
		return "FinalsRaceShipsForSire"
	elif var_1_0.IsFunKidRace():
		return "FinalsRaceShipsForKid"
	else
		assert(False)

return var_0_0
