local var_0_0 = class("MainFriendBtn", import(".MainBaseBtn"))

function var_0_0.OnClick(arg_1_0)
	arg_1_0:emit(NewMainMediator.GO_SCENE, SCENE.FRIEND)
end

return var_0_0
