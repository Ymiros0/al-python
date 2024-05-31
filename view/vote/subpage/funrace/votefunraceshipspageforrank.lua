local var_0_0 = class("VoteFunRaceShipsPageForRank", import("..FinalsRece.VoteFinalsRaceShipsPageForRank"))

function var_0_0.getUIName(arg_1_0)
	local var_1_0 = arg_1_0.contextData.voteGroup

	if var_1_0:IsFunMetaRace() then
		return "FinalsRaceShipsRankForMeta"
	elseif var_1_0:IsFunSireRace() then
		return "FinalsRaceShipsRankForSire"
	elseif var_1_0:IsFunKidRace() then
		return "FinalsRaceShipsRankForKid"
	else
		assert(false)
	end
end

return var_0_0
