local var_0_0 = class("MainActNewServerBtn", import(".MainBaseSpcailActBtn"))

function var_0_0.GetContainer(arg_1_0)
	return arg_1_0.root.parent:Find("link_top/layout")
end

function var_0_0.InShowTime(arg_2_0)
	return NewServerCarnivalScene.isShow()
end

function var_0_0.GetUIName(arg_3_0)
	return "MainUINewServerBtn"
end

function var_0_0.OnClick(arg_4_0)
	arg_4_0.event:emit(NewMainMediator.GO_SCENE, SCENE.NEW_SERVER_CARNIVAL)
end

function var_0_0.OnRegister(arg_5_0)
	arg_5_0.redDot = EffectRedDotNode.New(arg_5_0._tf, {
		pg.RedDotMgr.TYPES.NEW_SERVER
	})

	pg.redDotHelper:AddNode(arg_5_0.redDot)
end

function var_0_0.OnClear(arg_6_0)
	if arg_6_0.redDot then
		pg.redDotHelper:RemoveNode(arg_6_0.redDot)
	end
end

return var_0_0
