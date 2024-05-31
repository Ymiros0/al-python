local var_0_0 = class("MainHideBtn", import(".MainBaseBtn"))

function var_0_0.OnClick(arg_1_0)
	arg_1_0:emit(NewMainScene.FOLD, true)
end

return var_0_0
