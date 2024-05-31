local var_0_0 = class("SettingsOtherPage", import(".SettingsOptionPage"))

def var_0_0.OnShowTranscode(arg_1_0, arg_1_1):
	if PLATFORM_CODE == PLATFORM_JP:
		arg_1_0.GetPanel(SettingsAccountJPPanle).showTranscode(arg_1_1)

def var_0_0.OnCheckAllAccountState(arg_2_0):
	if PLATFORM_CODE == PLATFORM_JP:
		arg_2_0.GetPanel(SettingsAccountJPPanle).checkAllAccountState()
	elif PLATFORM_CODE == PLATFORM_US:
		arg_2_0.GetPanel(SettingsAccountUSPanle).checkAllAccountState_US()

def var_0_0.OnClearExchangeCode(arg_3_0):
	local var_3_0 = arg_3_0.GetPanel(SettingsRedeemPanel)

	if var_3_0:
		var_3_0.ClearExchangeCode()

def var_0_0.OnSecondPwdStateChange(arg_4_0):
	local var_4_0 = arg_4_0.GetPanel(SettingsSecondPwLimitedOpPanle)

	if var_4_0:
		var_4_0.UpdateBtnsState()

def var_0_0.GetPanels(arg_5_0):
	local var_5_0 = {
		SettingsSecondPasswordPanle,
		SettingsSecondPwLimitedOpPanle
	}

	if arg_5_0.NeedRedeem():
		table.insert(var_5_0, 1, SettingsRedeemPanel)

	if PLATFORM_CODE == PLATFORM_JP:
		table.insert(var_5_0, 1, SettingsAccountJPPanle)

	if PLATFORM_CODE == PLATFORM_US:
		table.insert(var_5_0, 1, SettingsAccountUSPanle)

	if PLATFORM_CODE == PLATFORM_CHT:
		table.insert(var_5_0, 1, SettingsAccountTwPanle)

		if CSharpVersion >= 50:
			table.insert(var_5_0, SettingsAccountCHTPanle)

		table.insert(var_5_0, SettingsAgreementCHTPanle)

	if PLATFORM_CODE == PLATFORM_CH:
		table.insert(var_5_0, SettingsAgreementPanle)

		local var_5_1 = LuaHelper.GetCHPackageType()

		if var_5_1 == 1 and CSharpVersion >= 50 and not LOCK_SDK_SERVIVE:
			table.insert(var_5_0, SettingsServicePanle)

		if var_5_1 == 1 or var_5_1 == 3 and pg.SdkMgr.GetInstance().IsHuaweiPackage():
			table.insert(var_5_0, SettingsAccountCHPanle)

		if var_5_1 == 1 and OPEN_EXCEPTION_TEST:
			table.insert(var_5_0, SettingsTestUploadExceptionPanle)

	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
		table.insert(var_5_0, SettingsAccountSpecialPanel)

	return var_5_0

def var_0_0.NeedRedeem(arg_6_0):
	local var_6_0 = True

	if PLATFORM_CODE == PLATFORM_CH or PLATFORM_CODE == PLATFORM_KR:
		if PLATFORM == PLATFORM_IPHONEPLAYER:
			var_6_0 = False
	elif PLATFORM_CODE == PLATFORM_JP:
		if PLATFORM == PLATFORM_IPHONEPLAYER:
			var_6_0 = False
	elif PLATFORM_CODE == PLATFORM_US:
		var_6_0 = False
	elif PLATFORM_CODE == PLATFORM_CHT and PLATFORM == PLATFORM_IPHONEPLAYER:
		var_6_0 = False

	return var_6_0

def var_0_0.OnInitPanle(arg_7_0):
	if PlayerPrefs.GetFloat("firstIntoOtherPanel") == 0:
		local var_7_0 = arg_7_0.GetPanel(SettingsSecondPasswordPanle)

		arg_7_0.ScrollToPanel(var_7_0)
		PlayerPrefs.SetFloat("firstIntoOtherPanel", 1)
		PlayerPrefs.Save()

return var_0_0
