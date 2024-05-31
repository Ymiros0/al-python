local var_0_0 = class("MainEquipBtn", import(".MainBaseBtn"))

def var_0_0.OnClick(arg_1_0):
	arg_1_0.emit(NewMainMediator.GO_SCENE, SCENE.EQUIPSCENE)

return var_0_0
