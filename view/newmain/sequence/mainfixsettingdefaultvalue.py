local var_0_0 = class("MainFixSettingDefaultValue")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = pg.settings_other_template

	for iter_1_0, iter_1_1 in ipairs(var_1_0.all):
		local var_1_1 = _G[var_1_0[iter_1_1].name]
		local var_1_2 = var_1_0[iter_1_1].default

		if var_1_1 != "" and not PlayerPrefs.HasKey(var_1_1):
			PlayerPrefs.SetInt(var_1_1, var_1_2)

	PlayerPrefs.Save()
	arg_1_0.FixPlayerPrefsKey()
	arg_1_1()

def var_0_0.FixPlayerPrefsKey(arg_2_0):
	local var_2_0 = getProxy(PlayerProxy).getRawData()

	USAGE_NEW_MAINUI = "USAGE_NEW_MAINUI" .. var_2_0.id

return var_0_0
