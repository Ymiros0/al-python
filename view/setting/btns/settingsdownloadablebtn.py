local var_0_0 = class("SettingsDownloadableBtn")

def var_0_0.InitTpl(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.tpl
	local var_1_1 = arg_1_1.container
	local var_1_2 = arg_1_1.iconSP

	arg_1_0._tf = cloneTplTo(var_1_0, var_1_1, arg_1_0.GetDownloadGroup())
	arg_1_0._go = arg_1_0._tf.gameObject

	setImageSprite(arg_1_0._tf.Find("icon"), var_1_2)

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.InitTpl(arg_2_1)
	pg.DelegateInfo.New(arg_2_0)

	arg_2_0.loadProgress = findTF(arg_2_0._tf, "progress")
	arg_2_0.loadProgressHandle = findTF(arg_2_0._tf, "progress/handle")
	arg_2_0.loadInfo1 = findTF(arg_2_0._tf, "status")
	arg_2_0.loadInfo2 = findTF(arg_2_0._tf, "version")
	arg_2_0.loadLabelNew = findTF(arg_2_0._tf, "version/new")
	arg_2_0.loadDot = findTF(arg_2_0._tf, "new")
	arg_2_0.loadLoading = findTF(arg_2_0._tf, "loading")

	setText(arg_2_0._tf.Find("title"), arg_2_0.GetTitle())
	arg_2_0.Init()
	arg_2_0.InitPrefsBar()

def var_0_0.Init(arg_3_0):
	setSlider(arg_3_0.loadProgress, 0, 1, 0)
	setActive(arg_3_0.loadDot, False)
	setActive(arg_3_0.loadLoading, False)
	arg_3_0.Check()

def var_0_0.InitPrefsBar(arg_4_0):
	arg_4_0.prefsBar = findTF(arg_4_0._tf, "PrefsBar")

	setText(findTF(arg_4_0.prefsBar, "Text"), i18n("setting_group_prefs_tip"))
	setActive(arg_4_0.prefsBar, True)

	local var_4_0 = arg_4_0.GetDownloadGroup()

	arg_4_0.hideTip = True

	onToggle(arg_4_0, arg_4_0.prefsBar, function(arg_5_0)
		if arg_5_0 == True:
			GroupHelper.SetGroupPrefsByName(var_4_0, DMFileChecker.Prefs.Max)
		else
			GroupHelper.SetGroupPrefsByName(var_4_0, DMFileChecker.Prefs.Min)

		if not arg_4_0.hideTip:
			pg.TipsMgr.GetInstance().ShowTips(i18n("group_prefs_switch_tip")), SFX_PANEL)
	triggerToggle(arg_4_0.prefsBar, GroupHelper.GetGroupPrefsByName(var_4_0) == DMFileChecker.Prefs.Max)

	arg_4_0.hideTip = False

def var_0_0.Check(arg_6_0):
	local var_6_0 = arg_6_0.GetDownloadGroup()
	local var_6_1 = BundleWizard.Inst.GetGroupMgr(var_6_0)

	arg_6_0.timer = Timer.New(function()
		arg_6_0.UpdateDownLoadState(), 0.5, -1)

	arg_6_0.timer.Start()
	arg_6_0.UpdateDownLoadState()

	if var_6_1.state == DownloadState.None:
		var_6_1.CheckD()

	onButton(arg_6_0, arg_6_0._tf, function()
		local var_8_0 = var_6_1.state

		if var_8_0 == DownloadState.CheckFailure:
			var_6_1.CheckD()
		elif var_8_0 == DownloadState.CheckToUpdate or var_8_0 == DownloadState.UpdateFailure:
			VersionMgr.Inst.RequestUIForUpdateD(var_6_0, True), SFX_PANEL)

def var_0_0.UpdateDownLoadState(arg_9_0):
	local var_9_0 = arg_9_0.GetDownloadGroup()
	local var_9_1 = BundleWizard.Inst.GetGroupMgr(var_9_0)
	local var_9_2 = var_9_1.state
	local var_9_3
	local var_9_4
	local var_9_5
	local var_9_6
	local var_9_7
	local var_9_8 = False

	if var_9_2 == DownloadState.None:
		local var_9_9 = arg_9_0.GetLocaltion(var_9_2, 1)

		var_9_4 = arg_9_0.GetLocaltion(var_9_2, 2)
		var_9_5 = "DOWNLOAD"
		var_9_6 = 0
		var_9_7 = False
	elif var_9_2 == DownloadState.Checking:
		local var_9_10 = arg_9_0.GetLocaltion(var_9_2, 1)

		var_9_4 = arg_9_0.GetLocaltion(var_9_2, 2)
		var_9_5 = "CHECKING"
		var_9_6 = 0
		var_9_7 = False
	elif var_9_2 == DownloadState.CheckToUpdate:
		local var_9_11 = arg_9_0.GetLocaltion(var_9_2, 1)

		var_9_4 = arg_9_0.GetLocaltion(var_9_2, 2)
		var_9_5 = string.format("V.%d > V.%d", var_9_1.localVersion.Build, var_9_1.serverVersion.Build)
		var_9_6 = 0
		var_9_7 = True
	elif var_9_2 == DownloadState.CheckOver:
		local var_9_12 = arg_9_0.GetLocaltion(var_9_2, 1)

		var_9_4 = arg_9_0.GetLocaltion(var_9_2, 2)
		var_9_5 = "V." .. var_9_1.CurrentVersion.Build
		var_9_6 = 1
		var_9_7 = False
	elif var_9_2 == DownloadState.CheckFailure:
		local var_9_13 = arg_9_0.GetLocaltion(var_9_2, 1)

		var_9_4 = arg_9_0.GetLocaltion(var_9_2, 2)
		var_9_5 = string.format("ERROR(CODE.%d)", var_9_1.errorCode)
		var_9_6 = 0
		var_9_7 = False
	elif var_9_2 == DownloadState.Updating:
		local var_9_14 = arg_9_0.GetLocaltion(var_9_2, 1)

		var_9_4 = string.format("(%d/%d)", var_9_1.downloadCount, var_9_1.downloadTotal)
		var_9_5 = var_9_1.downPath
		var_9_6 = var_9_1.downloadCount / math.max(var_9_1.downloadTotal, 1)
		var_9_7 = False
		var_9_8 = True
	elif var_9_2 == DownloadState.UpdateSuccess:
		local var_9_15 = arg_9_0.GetLocaltion(var_9_2, 1)

		var_9_4 = arg_9_0.GetLocaltion(var_9_2, 2)
		var_9_5 = "V." .. var_9_1.CurrentVersion.Build
		var_9_6 = 1
		var_9_7 = False
	elif var_9_2 == DownloadState.UpdateFailure:
		local var_9_16 = arg_9_0.GetLocaltion(var_9_2, 1)

		var_9_4 = arg_9_0.GetLocaltion(var_9_2, 2)
		var_9_5 = string.format("ERROR(CODE.%d)", var_9_1.errorCode)
		var_9_6 = var_9_1.downloadCount / math.max(var_9_1.downloadTotal, 1)
		var_9_7 = True

	if var_9_5.len() > 15:
		var_9_5 = var_9_5.sub(1, 12) .. "..."

	setText(arg_9_0.loadInfo1, var_9_4)
	setText(arg_9_0.loadInfo2, var_9_5)
	setSlider(arg_9_0.loadProgress, 0, 1, var_9_6)
	setActive(arg_9_0.loadProgressHandle, var_9_6 != 0 and var_9_6 != 1)
	setActive(arg_9_0.loadDot, var_9_7)
	setActive(arg_9_0.loadLoading, var_9_8)
	setActive(arg_9_0.loadLabelNew, var_9_2 == DownloadState.CheckToUpdate)

def var_0_0.Dispose(arg_10_0):
	pg.DelegateInfo.Dispose(arg_10_0)

	if arg_10_0.timer:
		arg_10_0.timer.Stop()

		arg_10_0.timer = None

def var_0_0.GetDownloadGroup(arg_11_0):
	assert(False, "overwrite me !!!")

def var_0_0.GetLocaltion(arg_12_0, arg_12_1, arg_12_2):
	assert(False, "overwrite me !!!")

def var_0_0.GetTitle(arg_13_0):
	assert(False, "overwrite me !!!")

return var_0_0