local var_0_0 = class("MainActTraingCampBtnMellowAdapt", import(".MainDifferentStyleSpActBtnAdapt"))

def var_0_0.GetContainer(arg_1_0):
	return arg_1_0.root.Find("left/list")

def var_0_0.OnRegister(arg_2_0):
	arg_2_0.redDot = RedDotNode.New(arg_2_0._tf.Find("tip"), {
		pg.RedDotMgr.TYPES.ACT_NEWBIE
	})

	pg.redDotHelper.AddNode(arg_2_0.redDot)
	arg_2_0._tf.SetAsFirstSibling()

return var_0_0
