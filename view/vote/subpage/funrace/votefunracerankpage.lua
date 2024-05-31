local var_0_0 = class("VoteFunRaceRankPage", import("..FinalsRece.VoteFinalsRaceRankPage"))

function var_0_0.getUIName(arg_1_0)
	local var_1_0 = arg_1_0.contextData.voteGroup

	if var_1_0:IsFunMetaRace() then
		return "FinalsRaceRankForMeta"
	elseif var_1_0:IsFunSireRace() then
		return "FinalsRaceRankForSire"
	elseif var_1_0:IsFunKidRace() then
		return "FinalsRaceRankForKid"
	else
		assert(false)
	end
end

return var_0_0
