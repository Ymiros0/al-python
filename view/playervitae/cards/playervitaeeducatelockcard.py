local var_0_0 = class("PlayerVitaeEducateLockCard", import(".PlayerVitaeEducateBaseCard"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
	setText(arg_1_1.Find("desc/Text"), i18n("flagship_educate_slot_lock_tip"))
	onButton(arg_1_0, arg_1_1.Find("go"), function()
		arg_1_0.emit(PlayerVitaeMediator.GO_SCENE, SCENE.EDUCATE), SFX_PANEL)

return var_0_0
