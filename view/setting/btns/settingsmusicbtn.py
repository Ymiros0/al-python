local var_0_0 = class("SettingsMusicBtn", import(".SettingsDownloadableBtn"))

def var_0_0.GetDownloadGroup(arg_1_0):
	return "GALLERY_BGM"

def var_0_0.GetLocaltion(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = ""

	if arg_2_1 == DownloadState.None:
		if arg_2_2 == 1:
			var_2_0 = i18n("word_soundfiles_download_title")
		elif arg_2_2 == 2:
			var_2_0 = i18n("word_soundfiles_download")
	elif arg_2_1 == DownloadState.Checking:
		if arg_2_2 == 1:
			var_2_0 = i18n("word_soundfiles_checking_title")
		elif arg_2_2 == 2:
			var_2_0 = i18n("word_soundfiles_checking")
	elif arg_2_1 == DownloadState.CheckToUpdate:
		if arg_2_2 == 1:
			var_2_0 = i18n("word_soundfiles_checkend_title")
		elif arg_2_2 == 2:
			var_2_0 = i18n("word_soundfiles_checkend")
	elif arg_2_1 == DownloadState.CheckOver:
		if arg_2_2 == 1:
			var_2_0 = i18n("word_soundfiles_checkend_title")
		elif arg_2_2 == 2:
			var_2_0 = i18n("word_soundfiles_noneedupdate")
	elif arg_2_1 == DownloadState.CheckFailure:
		if arg_2_2 == 1:
			var_2_0 = i18n("word_soundfiles_checkfailed")
		elif arg_2_2 == 2:
			var_2_0 = i18n("word_soundfiles_retry")
	elif arg_2_1 == DownloadState.Updating:
		if arg_2_2 == 1:
			var_2_0 = i18n("word_soundfiles_update")
	elif arg_2_1 == DownloadState.UpdateSuccess:
		if arg_2_2 == 1:
			var_2_0 = i18n("word_soundfiles_update_end_title")
		elif arg_2_2 == 2:
			var_2_0 = i18n("word_soundfiles_update_end")
	elif arg_2_1 == DownloadState.UpdateFailure:
		if arg_2_2 == 1:
			var_2_0 = i18n("word_soundfiles_update_failed")
		elif arg_2_2 == 2:
			var_2_0 = i18n("word_soundfiles_update_retry")

	return var_2_0

def var_0_0.GetTitle(arg_3_0):
	return i18n("setting_resdownload_title_music")

return var_0_0
