local var_0_0 = class("MainSettingsBtn", import(".MainBaseBtn"))

def var_0_0.OnClick(arg_1_0):
	SettingsRedDotNode.CanUpdateCV = False

	arg_1_0.emit(NewMainMediator.GO_SCENE, SCENE.SETTINGS)

return var_0_0
