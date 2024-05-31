local var_0_0 = class("SettingsResUpdatePanel", import(".SettingsBasePanel"))

def var_0_0.GetUIName(arg_1_0):
	return "SettingsResUpdate"

def var_0_0.GetTitle(arg_2_0):
	return i18n("Settings_title_resUpdate")

def var_0_0.GetTitleEn(arg_3_0):
	return "  / DOWNLOAD"

def var_0_0.OnInit(arg_4_0):
	arg_4_0.tpl = arg_4_0._tf.Find("Tpl")
	arg_4_0.containerTF = arg_4_0._tf.Find("list")
	arg_4_0.iconTF = arg_4_0._tf.Find("Icon")

	local var_4_0 = arg_4_0._tf.Find("MainGroup")
	local var_4_1 = not GroupMainHelper.IsVerSameWithServer()

	setActive(var_4_0, var_4_1)

	if var_4_1:
		arg_4_0.mainGroupBtn = SettingsMainGroupBtn.New(var_4_0)

	arg_4_0.soundBtn = SettingsSoundBtn.New({
		tpl = arg_4_0.tpl,
		container = arg_4_0.containerTF,
		iconSP = getImageSprite(arg_4_0.iconTF.Find("CV"))
	})
	arg_4_0.live2dBtn = SettingsLive2DBtn.New({
		tpl = arg_4_0.tpl,
		container = arg_4_0.containerTF,
		iconSP = getImageSprite(arg_4_0.iconTF.Find("L2D"))
	})
	arg_4_0.galleryBtn = SettingsGalleryBtn.New({
		tpl = arg_4_0.tpl,
		container = arg_4_0.containerTF,
		iconSP = getImageSprite(arg_4_0.iconTF.Find("GALLERY_PIC"))
	})
	arg_4_0.musicBtn = SettingsMusicBtn.New({
		tpl = arg_4_0.tpl,
		container = arg_4_0.containerTF,
		iconSP = getImageSprite(arg_4_0.iconTF.Find("GALLERY_BGM"))
	})
	arg_4_0.mangaBtn = SettingsMangaBtn.New({
		tpl = arg_4_0.tpl,
		container = arg_4_0.containerTF,
		iconSP = getImageSprite(arg_4_0.iconTF.Find("MANGA"))
	})
	arg_4_0.repairBtn = SettingsResRepairBtn.New({
		tpl = arg_4_0.tpl,
		container = arg_4_0.containerTF,
		iconSP = getImageSprite(arg_4_0.iconTF.Find("REPAIR"))
	})

def var_0_0.Dispose(arg_5_0):
	var_0_0.super.Dispose(arg_5_0)

	if arg_5_0.IsLoaded():
		arg_5_0.repairBtn.Dispose()

		arg_5_0.repairBtn = None

		arg_5_0.live2dBtn.Dispose()

		arg_5_0.live2dBtn = None

		arg_5_0.galleryBtn.Dispose()

		arg_5_0.galleryBtn = None

		arg_5_0.soundBtn.Dispose()

		arg_5_0.soundBtn = None

		arg_5_0.musicBtn.Dispose()

		arg_5_0.musicBtn = None

		arg_5_0.mangaBtn.Dispose()

		arg_5_0.mangaBtn = None

		if arg_5_0.mainGroupBtn:
			arg_5_0.mainGroupBtn.Dispose()

			arg_5_0.mainGroupBtn = None

return var_0_0
