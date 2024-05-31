local var_0_0 = class("SettingsMangaBtn", import(".SettingsDownloadableBtn"))

function var_0_0.GetDownloadGroup(arg_1_0)
	return "MANGA"
end

function var_0_0.GetLocaltion(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = ""

	if arg_2_1 == DownloadState.None then
		if arg_2_2 == 1 then
			var_2_0 = i18n("word_soundfiles_download_title")
		elseif arg_2_2 == 2 then
			var_2_0 = i18n("word_soundfiles_download")
		end
	elseif arg_2_1 == DownloadState.Checking then
		if arg_2_2 == 1 then
			var_2_0 = i18n("word_soundfiles_checking_title")
		elseif arg_2_2 == 2 then
			var_2_0 = i18n("word_soundfiles_checking")
		end
	elseif arg_2_1 == DownloadState.CheckToUpdate then
		if arg_2_2 == 1 then
			var_2_0 = i18n("word_soundfiles_checkend_title")
		elseif arg_2_2 == 2 then
			var_2_0 = i18n("word_soundfiles_checkend")
		end
	elseif arg_2_1 == DownloadState.CheckOver then
		if arg_2_2 == 1 then
			var_2_0 = i18n("word_soundfiles_checkend_title")
		elseif arg_2_2 == 2 then
			var_2_0 = i18n("word_soundfiles_noneedupdate")
		end
	elseif arg_2_1 == DownloadState.CheckFailure then
		if arg_2_2 == 1 then
			var_2_0 = i18n("word_soundfiles_checkfailed")
		elseif arg_2_2 == 2 then
			var_2_0 = i18n("word_soundfiles_retry")
		end
	elseif arg_2_1 == DownloadState.Updating then
		if arg_2_2 == 1 then
			var_2_0 = i18n("word_soundfiles_update")
		end
	elseif arg_2_1 == DownloadState.UpdateSuccess then
		if arg_2_2 == 1 then
			var_2_0 = i18n("word_soundfiles_update_end_title")
		elseif arg_2_2 == 2 then
			var_2_0 = i18n("word_soundfiles_update_end")
		end
	elseif arg_2_1 == DownloadState.UpdateFailure then
		if arg_2_2 == 1 then
			var_2_0 = i18n("word_soundfiles_update_failed")
		elseif arg_2_2 == 2 then
			var_2_0 = i18n("word_soundfiles_update_retry")
		end
	end

	return var_2_0
end

function var_0_0.GetTitle(arg_3_0)
	return i18n("setting_resdownload_title_manga")
end

return var_0_0
