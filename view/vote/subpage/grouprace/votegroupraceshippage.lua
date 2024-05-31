local var_0_0 = class("VoteGroupRaceShipPage", import("..PreRace.VotePreRaceShipPage"))

function var_0_0.getUIName(arg_1_0)
	return "GroupRaceShips"
end

function var_0_0.onInitItem(arg_2_0, arg_2_1)
	var_0_0.super.onInitItem(arg_2_0, arg_2_1)

	local var_2_0 = arg_2_0.voteItems[arg_2_1]

	onButton(arg_2_0, var_2_0.go, function()
		if arg_2_0.CallBack and arg_2_0.phase == VoteGroup.VOTE_STAGE then
			arg_2_0.CallBack(var_2_0, var_2_0.voteShip.votes)
		end
	end, SFX_PANEL)
end

function var_0_0.UpdateShips(arg_4_0, arg_4_1, arg_4_2)
	arg_4_0.scrollRect:SetTotalCount(#arg_4_0.displays)
end

function var_0_0.OnDestroy(arg_5_0)
	return
end

return var_0_0
