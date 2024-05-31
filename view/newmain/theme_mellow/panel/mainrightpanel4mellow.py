local var_0_0 = class("MainRightPanel4Mellow", import("...base.MainBasePanel"))

def var_0_0.GetBtns(arg_1_0):
	return {
		MainMemoryBtn.New(findTF(arg_1_0._tf, "2/menor"), arg_1_0.event),
		MainCollectionBtn.New(findTF(arg_1_0._tf, "2/collection"), arg_1_0.event),
		MainRankBtn4Mellow.New(findTF(arg_1_0._tf, "2/rank"), arg_1_0.event),
		MainFriendBtn.New(findTF(arg_1_0._tf, "2/friend"), arg_1_0.event),
		MainFormationBtn.New(findTF(arg_1_0._tf, "1/formation"), arg_1_0.event),
		MainBattleBtn.New(findTF(arg_1_0._tf, "1/battle"), arg_1_0.event)
	}

def var_0_0.GetDirection(arg_2_0):
	return Vector2(1, 0)

return var_0_0
