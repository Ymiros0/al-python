local var_0_0 = class("SettingsAgreementPanle", import(".SettingsBasePanel"))

def var_0_0.GetUIName(arg_1_0):
	return "SettingsAgreement"

def var_0_0.GetTitle(arg_2_0):
	return i18n("Settings_title_agreement")

def var_0_0.GetTitleEn(arg_3_0):
	return "  / VIEW AGREEMENT"

def var_0_0.OnInit(arg_4_0):
	onButton(arg_4_0, arg_4_0._tf.Find("private"), function()
		pg.SdkMgr.GetInstance().ShowPrivate(), SFX_PANEL)
	onButton(arg_4_0, arg_4_0._tf.Find("licence"), function()
		pg.SdkMgr.GetInstance().ShowLicence(), SFX_PANEL)

def var_0_0.OnUpdate(arg_7_0):
	return

return var_0_0
