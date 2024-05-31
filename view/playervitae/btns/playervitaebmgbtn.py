local var_0_0 = class("PlayerVitaeBMGBtn", import(".PlayerVitaeBaseBtn"))

def var_0_0.GetBgName(arg_1_0):
	return "AdmiralUI_atlas", "bgm"

def var_0_0.IsActive(arg_2_0, arg_2_1):
	return arg_2_1.IsBgmSkin()

def var_0_0.GetDefaultValue(arg_3_0):
	return getProxy(SettingsProxy).IsBGMEnable()

def var_0_0.OnSwitch(arg_4_0, arg_4_1):
	getProxy(SettingsProxy).SetBgmFlag(arg_4_1)

	local var_4_0

	if arg_4_1:
		var_4_0 = arg_4_0.ship.GetSkinBgm()
	else
		var_4_0 = "main"

	pg.BgmMgr.GetInstance().Push(PlayerVitaeScene.__cname, var_4_0)

	return True

def var_0_0.Load(arg_5_0, arg_5_1):
	var_0_0.super.Load(arg_5_0, arg_5_1)

	if arg_5_0.IsHrzType():
		arg_5_1.gameObject.name = "bmg"

return var_0_0
