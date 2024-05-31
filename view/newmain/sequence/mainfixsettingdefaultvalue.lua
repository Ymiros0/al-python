local var_0_0 = class("MainFixSettingDefaultValue")

function var_0_0.Execute(arg_1_0, arg_1_1)
	local var_1_0 = pg.settings_other_template

	for iter_1_0, iter_1_1 in ipairs(var_1_0.all) do
		local var_1_1 = _G[var_1_0[iter_1_1].name]
		local var_1_2 = var_1_0[iter_1_1].default

		if var_1_1 ~= "" and not PlayerPrefs.HasKey(var_1_1) then
			PlayerPrefs.SetInt(var_1_1, var_1_2)
		end
	end

	PlayerPrefs.Save()
	arg_1_0:FixPlayerPrefsKey()
	arg_1_1()
end

function var_0_0.FixPlayerPrefsKey(arg_2_0)
	local var_2_0 = getProxy(PlayerProxy):getRawData()

	USAGE_NEW_MAINUI = "USAGE_NEW_MAINUI" .. var_2_0.id
end

return var_0_0
