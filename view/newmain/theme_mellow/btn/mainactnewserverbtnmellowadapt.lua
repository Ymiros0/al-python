local var_0_0 = class("MainActNewServerBtnMellowAdapt", import(".MainDifferentStyleSpActBtnAdapt"))

function var_0_0.GetContainer(arg_1_0)
	return arg_1_0.root:Find("left/list")
end

function var_0_0.OnRegister(arg_2_0)
	arg_2_0.redDot = RedDotNode.New(arg_2_0._tf:Find("tip"), {
		pg.RedDotMgr.TYPES.NEW_SERVER
	})

	pg.redDotHelper:AddNode(arg_2_0.redDot)
end

return var_0_0
