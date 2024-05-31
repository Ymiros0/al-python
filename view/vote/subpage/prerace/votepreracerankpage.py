local var_0_0 = class("VotePreRaceRankPage", import("....base.BaseSubView"))

var_0_0.RANK_DISPLAY_COUNT = 15

def var_0_0.getUIName(arg_1_0):
	return "PreRaceRank"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.uiitemlist = UIItemList.New(arg_2_0.findTF("content"), arg_2_0.findTF("content/tpl"))
	arg_2_0.prevBtn = arg_2_0.findTF("prev")
	arg_2_0.nextBtn = arg_2_0.findTF("next")
	arg_2_0.tip = arg_2_0.findTF("tip")
	arg_2_0.title1 = arg_2_0.findTF("stages/title1")
	arg_2_0.title2 = arg_2_0.findTF("stages/title2")
	arg_2_0.rankTitle = arg_2_0.findTF("titles/rank_title")

	onButton(arg_2_0, arg_2_0.nextBtn, function()
		local var_3_0 = arg_2_0.page + 1

		if var_3_0 > arg_2_0.maxPage:
			var_3_0 = 1

		arg_2_0.page = var_3_0

		arg_2_0.initRank(arg_2_0.page), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.prevBtn, function()
		local var_4_0 = arg_2_0.page - 1

		if var_4_0 <= 0:
			var_4_0 = arg_2_0.maxPage

		arg_2_0.page = var_4_0

		arg_2_0.initRank(arg_2_0.page), SFX_PANEL)
	setText(arg_2_0.findTF("titles/rank_title"), i18n("vote_label_rank"))
	setText(arg_2_0.findTF("tip"), i18n("vote_label_rank_fresh_time_tip"))

def var_0_0.initRank(arg_5_0, arg_5_1):
	local var_5_0 = (arg_5_1 - 1) * var_0_0.RANK_DISPLAY_COUNT
	local var_5_1 = arg_5_0.voteShips

	arg_5_0.uiitemlist.make(function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_0 == UIItemList.EventUpdate:
			local var_6_0 = var_5_0 + arg_6_1 + 1
			local var_6_1 = var_5_1[var_6_0]

			if var_6_1:
				arg_5_0.UpdateShipInfo(arg_6_2, var_6_1.getShipName(), var_6_0)

			setActive(arg_6_2, var_6_1))
	arg_5_0.uiitemlist.align(var_0_0.RANK_DISPLAY_COUNT)
	arg_5_0.UpdateTitle()

def var_0_0.UpdateShipInfo(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	local var_7_0 = arg_7_0.voteGroup.GetRiseColor(arg_7_3)

	setText(arg_7_1.Find("Text"), setColorStr(shortenString(arg_7_2, 9), var_7_0))
	setText(arg_7_1.Find("number"), setColorStr(arg_7_3, var_7_0))

def var_0_0.UpdateTitle(arg_8_0):
	local var_8_0 = arg_8_0.voteGroup.getConfig("next_round_number")

	setActive(arg_8_0.rankTitle, True)

def var_0_0.Update(arg_9_0, arg_9_1):
	arg_9_0.voteGroup = arg_9_1
	arg_9_0.voteShips = arg_9_1.getList()
	arg_9_0.page = 1
	arg_9_0.maxPage = math.ceil(#arg_9_0.voteShips / var_0_0.RANK_DISPLAY_COUNT)
	arg_9_0.phase = arg_9_1.GetStage()

	setActive(arg_9_0.title1, arg_9_0.phase == VoteGroup.VOTE_STAGE)
	setActive(arg_9_0.title2, arg_9_0.phase != VoteGroup.VOTE_STAGE)
	setActive(arg_9_0.tip, arg_9_0.phase == VoteGroup.VOTE_STAGE)
	arg_9_0.UpdateTitle()
	arg_9_0.initRank(arg_9_0.page)
	arg_9_0.Show()

def var_0_0.OnDestroy(arg_10_0):
	return

return var_0_0
