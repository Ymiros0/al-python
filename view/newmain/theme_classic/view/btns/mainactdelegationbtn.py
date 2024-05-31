local var_0_0 = class("MainActDelegationBtn", import(".MainBaseSpcailActBtn"))

def var_0_0.GetContainer(arg_1_0):
	return arg_1_0.root.parent.Find("eventPanel")

def var_0_0.InShowTime(arg_2_0):
	local var_2_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.RYZA_TASK)

	return var_2_0 and not var_2_0.isEnd()

def var_0_0.GetUIName(arg_3_0):
	return "MainActDelegationBtn"

def var_0_0.OnClick(arg_4_0):
	arg_4_0.event.emit(NewMainMediator.GO_SCENE, SCENE.RYZA_TASK)

def var_0_0.OnInit(arg_5_0):
	setAnchoredPosition(arg_5_0._tf, {
		x = 200,
		y = 220
	})

def var_0_0.OnRegister(arg_6_0):
	arg_6_0.redDot = RedDotNode.New(arg_6_0._tf.Find("tip"), {
		pg.RedDotMgr.TYPES.RYZA_TASK
	})

	pg.redDotHelper.AddNode(arg_6_0.redDot)

def var_0_0.OnClear(arg_7_0):
	if arg_7_0.redDot:
		pg.redDotHelper.RemoveNode(arg_7_0.redDot)

return var_0_0
