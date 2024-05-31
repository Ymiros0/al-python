local var_0_0 = class("VoteFinalsRaceShipsPage", import("....base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "FinalsRaceShips"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.num1TF = arg_2_0.findTF("content/head/num1")
	arg_2_0.num2TF = arg_2_0.findTF("content/head/num2")
	arg_2_0.num3TF = arg_2_0.findTF("content/head/num3")
	arg_2_0.UIlist = UIItemList.New(arg_2_0.findTF("content/ships"), arg_2_0.findTF("content/ships/ship_tpl"))

def var_0_0.SetCallBack(arg_3_0, arg_3_1):
	arg_3_0.CallBack = arg_3_1

def var_0_0.Update(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	arg_4_0.voteGroup = arg_4_1
	arg_4_0.count = arg_4_3
	arg_4_0.phase = arg_4_1.GetStage()
	arg_4_0.displays = {}
	arg_4_0.topList = {}

	local var_4_0 = arg_4_1.GetRankList()

	for iter_4_0, iter_4_1 in ipairs(arg_4_2):
		if iter_4_1.group == var_4_0[1].group or iter_4_1.group == var_4_0[2].group or iter_4_1.group == var_4_0[3].group:
			table.insert(arg_4_0.topList, iter_4_1)
		else
			table.insert(arg_4_0.displays, iter_4_1)

	arg_4_0.UpdateTop3(var_4_0[1], var_4_0[2], var_4_0[3])
	arg_4_0.UpdateShips()
	arg_4_0.Show()

def var_0_0.UpdateTop3(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	arg_5_0.UpdateVoteShip(arg_5_0.num1TF, arg_5_1)
	arg_5_0.UpdateVoteShip(arg_5_0.num2TF, arg_5_2)
	arg_5_0.UpdateVoteShip(arg_5_0.num3TF, arg_5_3)
	setActive(arg_5_0.num1TF, _.any(arg_5_0.topList, function(arg_6_0)
		return arg_6_0.group == arg_5_1.group))
	setActive(arg_5_0.num2TF, _.any(arg_5_0.topList, function(arg_7_0)
		return arg_7_0.group == arg_5_2.group))
	setActive(arg_5_0.num3TF, _.any(arg_5_0.topList, function(arg_8_0)
		return arg_8_0.group == arg_5_3.group))

def var_0_0.UpdateShips(arg_9_0):
	arg_9_0.UIlist.make(function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0 == UIItemList.EventUpdate:
			local var_10_0 = arg_9_0.displays[arg_10_1 + 1]
			local var_10_1 = VoteShipItem.New(arg_10_2)

			var_10_1.update(var_10_0)
			onButton(arg_9_0, var_10_1.go, function()
				if arg_9_0.CallBack and arg_9_0.phase == VoteGroup.VOTE_STAGE:
					arg_9_0.CallBack(var_10_1, var_10_1.voteShip.votes), SFX_PANEL))
	arg_9_0.UIlist.align(math.max(#arg_9_0.displays, 0))

def var_0_0.contains(arg_12_0, arg_12_1, arg_12_2):
	return _.any(arg_12_1, function(arg_13_0)
		return arg_13_0.group == arg_12_2.group)

def var_0_0.UpdateVoteShip(arg_14_0, arg_14_1, arg_14_2):
	if not arg_14_2:
		setActive(arg_14_1, False)

		return

	setText(arg_14_1.Find("name"), shortenString(arg_14_2.getShipName(), 5))

	local var_14_0 = arg_14_2.getPainting()

	arg_14_0.LoadPainting(arg_14_1.Find("mask"), var_14_0)
	onButton(arg_14_0, arg_14_1, function()
		if arg_14_0.CallBack and arg_14_0.phase == VoteGroup.VOTE_STAGE:
			arg_14_0.CallBack({
				voteShip = arg_14_2
			}, arg_14_2.votes), SFX_PANEL)

def var_0_0.LoadPainting(arg_16_0, arg_16_1, arg_16_2):
	LoadSpriteAsync("VoteShips/" .. arg_16_2, function(arg_17_0)
		setImageSprite(arg_16_1.Find("icon"), arg_17_0, False))

def var_0_0.OnDestroy(arg_18_0):
	return

return var_0_0
