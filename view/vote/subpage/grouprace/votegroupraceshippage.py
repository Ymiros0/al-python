local var_0_0 = class("VoteGroupRaceShipPage", import("..PreRace.VotePreRaceShipPage"))

def var_0_0.getUIName(arg_1_0):
	return "GroupRaceShips"

def var_0_0.onInitItem(arg_2_0, arg_2_1):
	var_0_0.super.onInitItem(arg_2_0, arg_2_1)

	local var_2_0 = arg_2_0.voteItems[arg_2_1]

	onButton(arg_2_0, var_2_0.go, function()
		if arg_2_0.CallBack and arg_2_0.phase == VoteGroup.VOTE_STAGE:
			arg_2_0.CallBack(var_2_0, var_2_0.voteShip.votes), SFX_PANEL)

def var_0_0.UpdateShips(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.scrollRect.SetTotalCount(#arg_4_0.displays)

def var_0_0.OnDestroy(arg_5_0):
	return

return var_0_0
