local var_0_0 = class("CheckHotfixCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().mediatorName

	if var_1_0 and (string.find(var_1_0, "Combat") or string.find(var_1_0, "Battle")):
		return

	local var_1_1 = getProxy(SettingsProxy)

	if PLATFORM_CODE == PLATFORM_US and VersionMgr.Inst.OnProxyUsing():
		return

	local var_1_2 = BundleWizard.Inst.GetGroupMgr("DEFAULT_RES")

	if var_1_2.CurrentVersion.Major > 0 and (not var_1_1.lastRequestVersionTime or Time.realtimeSinceStartup - var_1_1.lastRequestVersionTime > 1800):
		var_1_1.lastRequestVersionTime = Time.realtimeSinceStartup

		pg.UIMgr.GetInstance().LoadingOn()

		local var_1_3 = True

		VersionMgr.Inst.FetchVersion(function(arg_2_0)
			pg.UIMgr.GetInstance().LoadingOff()

			var_1_3 = False

			if arg_2_0.Major > var_1_2.CurrentVersion.Major or arg_2_0.Major == var_1_2.CurrentVersion.Major and arg_2_0.Minor > var_1_2.CurrentVersion.Minor or arg_2_0.Major == var_1_2.CurrentVersion.Major and arg_2_0.Minor == var_1_2.CurrentVersion.Minor and arg_2_0.Build > var_1_2.CurrentVersion.Build:
				nowWorld().forceLock = True

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					modal = True,
					locked = True,
					hideNo = True,
					content = i18n("new_version_tip"),
					weight = LayerWeightConst.TOP_LAYER,
					def onYes:()
						Application.Quit(),
					def onClose:()
						Application.Quit()
				}))
		LeanTween.delayedCall(3, System.Action(function()
			if var_1_3:
				pg.UIMgr.GetInstance().LoadingOff()))

	if var_1_0 and string.find(var_1_0, "LoginMediator"):
		var_1_1.lastRequestVersionTime = None

return var_0_0
