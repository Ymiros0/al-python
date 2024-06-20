local var_0_0 = class("PlayerVitaeSpineBtn", import(".PlayerVitaeBaseBtn"))

def var_0_0.GetBgName(arg_1_0):
	if arg_1_0.IsHrzType():
		return "share/btn_l2d_atlas", "spine_painting_bg"
	else
		return "AdmiralUI_atlas", "sp"

def var_0_0.IsActive(arg_2_0, arg_2_1):
	local var_2_0 = HXSet.autoHxShiftPath("spinepainting/" .. arg_2_1.getPainting())

	return (checkABExist(var_2_0))

def var_0_0.GetDefaultValue(arg_3_0):
	return getProxy(SettingsProxy).getCharacterSetting(arg_3_0.ship.id, SHIP_FLAG_SP)

def var_0_0.OnSwitch(arg_4_0, arg_4_1):
	getProxy(SettingsProxy).setCharacterSetting(arg_4_0.ship.id, SHIP_FLAG_SP, arg_4_1)

	return True

def var_0_0.Load(arg_5_0, arg_5_1):
	var_0_0.super.Load(arg_5_0, arg_5_1)

	if arg_5_0.IsHrzType():
		arg_5_1.gameObject.name = "spine"

return var_0_0