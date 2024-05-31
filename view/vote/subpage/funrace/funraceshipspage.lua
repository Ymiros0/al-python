local var_0_0 = class("FunRaceShipsPage", import("..FinalsRece.VoteFinalsRaceShipsPage"))

function var_0_0.getUIName(arg_1_0)
	local var_1_0 = arg_1_0.contextData.voteGroup

	if var_1_0:IsFunMetaRace() then
		return "FinalsRaceShipsForMeta"
	elseif var_1_0:IsFunSireRace() then
		return "FinalsRaceShipsForSire"
	elseif var_1_0:IsFunKidRace() then
		return "FinalsRaceShipsForKid"
	else
		assert(false)
	end
end

return var_0_0
