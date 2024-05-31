local var_0_0 = class("VoteGroupRaceRankPage", import("....base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "GroupRaceRank"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.cards = {}
	arg_2_0.title1 = arg_2_0.findTF("stages/title1")
	arg_2_0.title2 = arg_2_0.findTF("stages/title2")
	arg_2_0.scrollRect = arg_2_0.findTF("scrollrect").GetComponent("LScrollRect")

	function arg_2_0.scrollRect.onInitItem(arg_3_0)
		arg_2_0.OnInitItem(arg_3_0)

	function arg_2_0.scrollRect.onUpdateItem(arg_4_0, arg_4_1)
		arg_2_0.OnUpdateItem(arg_4_0, arg_4_1)

	setText(arg_2_0.findTF("titles/rank_title"), i18n("vote_label_rank"))
	setText(arg_2_0.findTF("titles/votes"), i18n("word_votes"))
	setText(arg_2_0.findTF("tip"), i18n("vote_label_rank_fresh_time_tip"))

def var_0_0.Update(arg_5_0, arg_5_1):
	arg_5_0.voteGroup = arg_5_1
	arg_5_0.phase = arg_5_1.GetStage()

	setActive(arg_5_0.title1, arg_5_0.phase == VoteGroup.VOTE_STAGE)
	setActive(arg_5_0.title2, arg_5_0.phase != VoteGroup.VOTE_STAGE)
	setActive(arg_5_0.findTF("tip"), arg_5_0.phase == VoteGroup.VOTE_STAGE)
	arg_5_0.UpdateList()

def var_0_0.UpdateList(arg_6_0):
	arg_6_0.displays = arg_6_0.voteGroup.GetRankList()

	arg_6_0.scrollRect.SetTotalCount(#arg_6_0.displays)

def var_0_0.OnInitItem(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.NewCard(arg_7_1)

	arg_7_0.cards[arg_7_1] = var_7_0

def var_0_0.OnUpdateItem(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = arg_8_0.cards[arg_8_2]
	local var_8_1 = arg_8_0.displays[arg_8_1 + 1]
	local var_8_2 = arg_8_0.voteGroup.GetVotes(var_8_1)
	local var_8_3 = arg_8_1 + 1
	local var_8_4 = arg_8_0.voteGroup.GetRiseColor(var_8_3)

	var_8_0.Update(var_8_1, var_8_3, var_8_2, var_8_4)

def var_0_0.NewCard(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.transform

	return {
		def Update:(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
			setText(var_9_0.Find("number"), setColorStr(arg_10_1, arg_10_3))
			setText(var_9_0.Find("name"), setColorStr(shortenString(arg_10_0.getShipName(), 6), arg_10_3))
			setText(var_9_0.Find("Text"), setColorStr(arg_10_2, arg_10_3))
	}

def var_0_0.OnDestroy(arg_11_0):
	return

return var_0_0
