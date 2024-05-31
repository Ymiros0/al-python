local var_0_0 = class("ShipAtlasBgBtn", import("....PlayerVitae.btns.PlayerVitaeBGBtn"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.event = arg_1_3
	arg_1_0.value = arg_1_4

def var_0_0.emit(arg_2_0, ...):
	arg_2_0.event.emit(...)

def var_0_0.GetDefaultValue(arg_3_0):
	return arg_3_0.value

def var_0_0.OnSwitch(arg_4_0, arg_4_1):
	return True

def var_0_0.OnSwitchDone(arg_5_0):
	arg_5_0.emit(SkinAtlasPreviewPage.ON_BG_SWITCH_DONE, arg_5_0.flag)

return var_0_0
