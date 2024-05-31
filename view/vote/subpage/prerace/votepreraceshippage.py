local var_0_0 = class("VotePreRaceShipPage", import("....base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "PreRaceShips"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.scrollRect = arg_2_0._tf.GetComponent("LScrollRect")
	arg_2_0.voteItems = {}

	function arg_2_0.scrollRect.onInitItem(arg_3_0)
		arg_2_0.onInitItem(arg_3_0)

	function arg_2_0.scrollRect.onUpdateItem(arg_4_0, arg_4_1)
		arg_2_0.onUpdateItem(arg_4_0, arg_4_1)

	function arg_2_0.scrollRect.onReturnItem(arg_5_0, arg_5_1)
		arg_2_0.onReturnItem(arg_5_0, arg_5_1)

	arg_2_0._tf.SetAsFirstSibling()

def var_0_0.onInitItem(arg_6_0, arg_6_1):
	local var_6_0 = VoteShipItem.New(arg_6_1)

	onButton(arg_6_0, var_6_0.go, function()
		if arg_6_0.phase == VoteGroup.VOTE_STAGE:
			arg_6_0.CallBack(var_6_0), SFX_PANEL)

	arg_6_0.voteItems[arg_6_1] = var_6_0

def var_0_0.SetCallBack(arg_8_0, arg_8_1):
	arg_8_0.CallBack = arg_8_1

def var_0_0.onUpdateItem(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = arg_9_0.voteItems[arg_9_2]

	if not var_9_0:
		arg_9_0.onInitItem(arg_9_2)

		var_9_0 = arg_9_0.voteItems[arg_9_2]

	local var_9_1 = arg_9_0.displays[arg_9_1 + 1]

	arg_9_0.UpdateShip(arg_9_1, var_9_0, var_9_1)

def var_0_0.UpdateShip(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	if arg_10_0.phase != VoteGroup.VOTE_STAGE:
		local var_10_0 = arg_10_0.voteGroup.GetRank(arg_10_3)
		local var_10_1, var_10_2 = arg_10_0.voteGroup.CanRankToNextTurn(var_10_0)

		arg_10_2.update(arg_10_3, {
			rank = var_10_0,
			riseFlag = var_10_1,
			resurgenceFlag = var_10_2
		})
	else
		arg_10_2.update(arg_10_3, None)

def var_0_0.onReturnItem(arg_11_0, arg_11_1, arg_11_2):
	if arg_11_0.exited:
		return

	local var_11_0 = arg_11_0.voteItems[arg_11_2]

	if var_11_0:
		var_11_0.clear()

def var_0_0.Update(arg_12_0, arg_12_1, arg_12_2):
	arg_12_0.voteGroup = arg_12_1
	arg_12_0.phase = arg_12_1.GetStage()
	arg_12_0.displays = arg_12_2

	arg_12_0.UpdateShips()
	arg_12_0.Show()

def var_0_0.UpdateShips(arg_13_0):
	if arg_13_0.phase == VoteGroup.VOTE_STAGE:
		shuffle(arg_13_0.displays)

	arg_13_0.scrollRect.SetTotalCount(#arg_13_0.displays)

def var_0_0.OnDestroy(arg_14_0):
	return

return var_0_0
