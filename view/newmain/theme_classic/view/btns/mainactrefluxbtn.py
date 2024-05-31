local var_0_0 = class("MainActRefluxBtn", import(".MainBaseSpcailActBtn"))

def var_0_0.GetContainer(arg_1_0):
	return arg_1_0.root.parent.Find("link_top/layout")

def var_0_0.InShowTime(arg_2_0):
	return getProxy(RefluxProxy).isActive()

def var_0_0.GetUIName(arg_3_0):
	return "MainUIReturnBtn"

def var_0_0.OnClick(arg_4_0):
	arg_4_0.event.emit(NewMainMediator.GO_SCENE, SCENE.REFLUX)

def var_0_0.OnRegister(arg_5_0):
	arg_5_0.redDot = EffectRedDotNode.New(arg_5_0._tf, {
		pg.RedDotMgr.TYPES.ACT_RETURN
	})

	pg.redDotHelper.AddNode(arg_5_0.redDot)

def var_0_0.OnClear(arg_6_0):
	if arg_6_0.redDot:
		pg.redDotHelper.RemoveNode(arg_6_0.redDot)

return var_0_0
