﻿local var_0_0 = class("SettingsOtherPage", import(".SettingsOptionPage"))

function var_0_0.OnShowTranscode(arg_1_0, arg_1_1)
	if PLATFORM_CODE == PLATFORM_JP then
		arg_1_0:GetPanel(SettingsAccountJPPanle):showTranscode(arg_1_1)
	end
end

function var_0_0.OnCheckAllAccountState(arg_2_0)
	if PLATFORM_CODE == PLATFORM_JP then
		arg_2_0:GetPanel(SettingsAccountJPPanle):checkAllAccountState()
	elseif PLATFORM_CODE == PLATFORM_US then
		arg_2_0:GetPanel(SettingsAccountUSPanle):checkAllAccountState_US()
	end
end

function var_0_0.OnClearExchangeCode(arg_3_0)
	local var_3_0 = arg_3_0:GetPanel(SettingsRedeemPanel)

	if var_3_0 then
		var_3_0:ClearExchangeCode()
	end
end

function var_0_0.OnSecondPwdStateChange(arg_4_0)
	local var_4_0 = arg_4_0:GetPanel(SettingsSecondPwLimitedOpPanle)

	if var_4_0 then
		var_4_0:UpdateBtnsState()
	end
end

function var_0_0.GetPanels(arg_5_0)
	local var_5_0 = {
		SettingsSecondPasswordPanle,
		SettingsSecondPwLimitedOpPanle
	}

	if arg_5_0:NeedRedeem() then
		table.insert(var_5_0, 1, SettingsRedeemPanel)
	end

	if PLATFORM_CODE == PLATFORM_JP then
		table.insert(var_5_0, 1, SettingsAccountJPPanle)
	end

	if PLATFORM_CODE == PLATFORM_US then
		table.insert(var_5_0, 1, SettingsAccountUSPanle)
	end

	if PLATFORM_CODE == PLATFORM_CHT then
		table.insert(var_5_0, 1, SettingsAccountTwPanle)

		if CSharpVersion >= 50 then
			table.insert(var_5_0, SettingsAccountCHTPanle)
		end

		table.insert(var_5_0, SettingsAgreementCHTPanle)
	end

	if PLATFORM_CODE == PLATFORM_CH then
		table.insert(var_5_0, SettingsAgreementPanle)

		local var_5_1 = LuaHelper.GetCHPackageType()

		if var_5_1 == 1 and CSharpVersion >= 50 and not LOCK_SDK_SERVIVE then
			table.insert(var_5_0, SettingsServicePanle)
		end

		if var_5_1 == 1 or var_5_1 == 3 and pg.SdkMgr.GetInstance():IsHuaweiPackage() then
			table.insert(var_5_0, SettingsAccountCHPanle)
		end

		if var_5_1 == 1 and OPEN_EXCEPTION_TEST then
			table.insert(var_5_0, SettingsTestUploadExceptionPanle)
		end
	end

	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US then
		table.insert(var_5_0, SettingsAccountSpecialPanel)
	end

	return var_5_0
end

function var_0_0.NeedRedeem(arg_6_0)
	local var_6_0 = true

	if PLATFORM_CODE == PLATFORM_CH or PLATFORM_CODE == PLATFORM_KR then
		if PLATFORM == PLATFORM_IPHONEPLAYER then
			var_6_0 = false
		end
	elseif PLATFORM_CODE == PLATFORM_JP then
		if PLATFORM == PLATFORM_IPHONEPLAYER then
			var_6_0 = false
		end
	elseif PLATFORM_CODE == PLATFORM_US then
		var_6_0 = false
	elseif PLATFORM_CODE == PLATFORM_CHT and PLATFORM == PLATFORM_IPHONEPLAYER then
		var_6_0 = false
	end

	return var_6_0
end

function var_0_0.OnInitPanle(arg_7_0)
	if PlayerPrefs.GetFloat("firstIntoOtherPanel") == 0 then
		local var_7_0 = arg_7_0:GetPanel(SettingsSecondPasswordPanle)

		arg_7_0:ScrollToPanel(var_7_0)
		PlayerPrefs.SetFloat("firstIntoOtherPanel", 1)
		PlayerPrefs.Save()
	end
end

return var_0_0
