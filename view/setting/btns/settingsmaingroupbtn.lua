local var_0_0 = class("SettingsMainGroupBtn")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	pg.DelegateInfo.New(arg_1_0)
	arg_1_0:initData()
	arg_1_0:findUI(arg_1_1)
	arg_1_0:addListener()
	arg_1_0:check()
end

function var_0_0.Dispose(arg_2_0)
	pg.DelegateInfo.Dispose(arg_2_0)

	if arg_2_0.timer then
		arg_2_0.timer:Stop()

		arg_2_0.timer = nil
	end
end

function var_0_0.initData(arg_3_0)
	arg_3_0.mgr = pg.MainGroupMgr:GetInstance()
end

function var_0_0.findUI(arg_4_0, arg_4_1)
	arg_4_0._tf = arg_4_1

	local var_4_0 = findTF(arg_4_0._tf, "Content")

	arg_4_0.titleText = findTF(var_4_0, "Title")
	arg_4_0.progressBar = findTF(var_4_0, "Progress")
	arg_4_0.btn = findTF(var_4_0, "Btn")
	arg_4_0.btnText = findTF(arg_4_0.btn, "Text")
	arg_4_0.loadingIcon = findTF(var_4_0, "Status/Loading")
	arg_4_0.newIcon = findTF(var_4_0, "Status/New")
	arg_4_0.finishIcon = findTF(var_4_0, "Status/Finish")

	setText(arg_4_0.titleText, i18n("setting_resdownload_title_main_group"))
end

function var_0_0.addListener(arg_5_0)
	onButton(arg_5_0, arg_5_0._tf, function()
		local var_6_0 = arg_5_0.mgr:GetState()

		if var_6_0 == DownloadState.CheckFailure then
			arg_5_0.mgr:StartCheckD()
		elseif var_6_0 == DownloadState.CheckToUpdate or var_6_0 == DownloadState.UpdateFailure then
			local var_6_1 = arg_5_0.mgr:GetTotalSize()
			local var_6_2 = HashUtil.BytesToString(var_6_1)

			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				type = MSGBOX_TYPE_NORMAL,
				content = string.format(i18n("main_group_msgbox_content", var_6_2)),
				onYes = function()
					GroupMainHelper.SavePrefs(DMFileChecker.Prefs.Max)
					arg_5_0.mgr:StartUpdateD()
				end
			})
		end
	end, SFX_PANEL)
end

function var_0_0.check(arg_8_0)
	if arg_8_0.mgr:GetState() == DownloadState.None then
		arg_8_0.mgr:StartCheckD()
	end

	arg_8_0.timer = Timer.New(function()
		arg_8_0:updateUI()
	end, 0.5, -1)

	arg_8_0.timer:Start()
	arg_8_0:updateUI()
end

function var_0_0.updateUI(arg_10_0)
	local var_10_0 = arg_10_0.mgr:GetState()

	if var_10_0 == DownloadState.None then
		setText(arg_10_0.btnText, "无状态")
		setActive(arg_10_0.loadingIcon, false)
		setActive(arg_10_0.newIcon, false)
		setActive(arg_10_0.finishIcon, false)
	elseif var_10_0 == DownloadState.Checking then
		setText(arg_10_0.btnText, i18n("word_maingroup_checking"))
		setActive(arg_10_0.loadingIcon, false)
		setActive(arg_10_0.newIcon, false)
		setActive(arg_10_0.finishIcon, false)
	elseif var_10_0 == DownloadState.CheckToUpdate then
		setText(arg_10_0.btnText, i18n("word_maingroup_checktoupdate"))
		setActive(arg_10_0.loadingIcon, false)
		setActive(arg_10_0.newIcon, true)
		setActive(arg_10_0.finishIcon, false)
	elseif var_10_0 == DownloadState.CheckOver then
		setText(arg_10_0.btnText, "无需更新")
		setActive(arg_10_0.loadingIcon, false)
		setActive(arg_10_0.newIcon, false)
		setActive(arg_10_0.finishIcon, false)
	elseif var_10_0 == DownloadState.CheckFailure then
		setText(arg_10_0.btnText, i18n("word_maingroup_checkfailure"))
		setActive(arg_10_0.loadingIcon, false)
		setActive(arg_10_0.newIcon, false)
		setActive(arg_10_0.finishIcon, false)
	elseif var_10_0 == DownloadState.Updating then
		setText(arg_10_0.btnText, i18n("word_maingroup_updating"))
		setActive(arg_10_0.loadingIcon, true)
		setActive(arg_10_0.newIcon, false)
		setActive(arg_10_0.finishIcon, false)

		local var_10_1, var_10_2 = arg_10_0.mgr:GetCountProgress()

		setSlider(arg_10_0.progressBar, 0, var_10_2, var_10_1)
		setText(arg_10_0.btnText, var_10_1 .. "/" .. var_10_2)
	elseif var_10_0 == DownloadState.UpdateSuccess then
		setText(arg_10_0.btnText, i18n("word_maingroup_updatesuccess"))
		setActive(arg_10_0.loadingIcon, false)
		setActive(arg_10_0.newIcon, false)
		setActive(arg_10_0.finishIcon, true)
	elseif var_10_0 == DownloadState.UpdateFailure then
		setText(arg_10_0.btnText, i18n("word_maingroup_updatefailure"))
		setActive(arg_10_0.loadingIcon, false)
		setActive(arg_10_0.newIcon, false)
		setActive(arg_10_0.finishIcon, false)
	end
end

return var_0_0
