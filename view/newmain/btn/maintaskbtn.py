local var_0_0 = class("MainTaskBtn", import(".MainBaseBtn"))

def var_0_0.OnClick(arg_1_0):
	arg_1_0.emit(NewMainMediator.GO_SCENE, SCENE.TASK)

return var_0_0
