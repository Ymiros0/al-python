local var_0_0 = class("MainActTraingCampBtn", import(".MainBaseSpcailActBtn"))

def var_0_0.GetContainer(arg_1_0):
	return arg_1_0.root.parent.Find("link_top/layout")

def var_0_0.InShowTime(arg_2_0):
	local var_2_0 = TrainingCampScene.isNormalActOn()
	local var_2_1 = TrainingCampScene.isTecActOn()

	return var_2_0 or var_2_1

def var_0_0.GetUIName(arg_3_0):
	return "MainUIRecruitBtn"

def var_0_0.OnClick(arg_4_0):
	arg_4_0.event.emit(NewMainMediator.GO_SCENE, SCENE.TRAININGCAMP)

def var_0_0.OnRegister(arg_5_0):
	arg_5_0.redDot = EffectRedDotNode.New(arg_5_0._tf, {
		pg.RedDotMgr.TYPES.ACT_NEWBIE
	})

	pg.redDotHelper.AddNode(arg_5_0.redDot)

def var_0_0.OnClear(arg_6_0):
	if arg_6_0.redDot:
		pg.redDotHelper.RemoveNode(arg_6_0.redDot)

return var_0_0
