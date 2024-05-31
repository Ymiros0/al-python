local var_0_0 = class("Dorm3dLevelLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "Dorm3dLevelUI"

def var_0_0.init(arg_2_0):
	local var_2_0 = arg_2_0._tf.Find("btn_back")

	onButton(arg_2_0, var_2_0, function()
		arg_2_0.closeView(), SFX_CANCEL)

	arg_2_0.rtLevelPanel = arg_2_0._tf.Find("panel")

	local var_2_1 = arg_2_0.rtLevelPanel.Find("view/container")

	arg_2_0.levelItemList = UIItemList.New(var_2_1, var_2_1.Find("tpl"))

	arg_2_0.levelItemList.make(function(arg_4_0, arg_4_1, arg_4_2)
		arg_4_1 = arg_4_1 + 1

		if arg_4_0 == UIItemList.EventUpdate:
			local var_4_0 = arg_4_1 <= arg_2_0.apartment.level

			setActive(arg_4_2.Find("unlock"), var_4_0)
			setActive(arg_4_2.Find("lock"), not var_4_0)

			local var_4_1 = arg_4_2.Find(var_4_0 and "unlock" or "lock")

			setText(var_4_1.Find("level"), arg_4_1)
			setText(var_4_1.Find("Text"), arg_2_0.apartment.getFavorConfig("levelup_desc", arg_4_1)))
	onButton(arg_2_0, arg_2_0.rtLevelPanel.Find("bottom/btn_time"), function()
		local var_5_0, var_5_1 = arg_2_0.apartment.checkUnlockConfig(getDorm3dGameset("drom3d_clothing_unlock")[2])

		if not var_5_0:
			pg.TipsMgr.GetInstance().ShowTips(var_5_1)

			return

		arg_2_0.ShowTimeSelectWindow(), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.rtLevelPanel.Find("bottom/btn_skin"), function()
		if #arg_2_0.apartment.skinList < 2:
			pg.TipsMgr.GetInstance().ShowTips("without unlock skin")

			return

		local var_6_0, var_6_1 = arg_2_0.apartment.checkUnlockConfig(getDorm3dGameset("drom3d_clothing_unlock")[2])

		if not var_6_0:
			pg.TipsMgr.GetInstance().ShowTips(var_6_1)

			return

		arg_2_0.ShowSkinSelectWindow(), SFX_PANEL)

	arg_2_0.rtTimeSelectWindow = arg_2_0._tf.Find("TimeSelectWindow")

	onButton(arg_2_0, arg_2_0.rtTimeSelectWindow.Find("bg"), function()
		setActive(arg_2_0.rtTimeSelectWindow, False)
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_2_0.rtTimeSelectWindow, arg_2_0._tf), SFX_CANCEL)

	arg_2_0.rtSkinSelectWindow = arg_2_0._tf.Find("SkinSelectWindow")

	onButton(arg_2_0, arg_2_0.rtSkinSelectWindow.Find("bg"), function()
		setActive(arg_2_0.rtSkinSelectWindow, False)
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_2_0.rtSkinSelectWindow, arg_2_0._tf), SFX_CANCEL)
	pg.UIMgr.GetInstance().OverlayPanelPB(arg_2_0._tf, {
		weight = LayerWeightConst.SECOND_LAYER,
		groupName = LayerWeightConst.GROUP_DORM3D
	})

def var_0_0.SetApartment(arg_9_0, arg_9_1):
	arg_9_0.apartment = arg_9_1

def var_0_0.didEnter(arg_10_0):
	local var_10_0 = arg_10_0.apartment.favor
	local var_10_1 = arg_10_0.apartment.getNextExp()

	setText(arg_10_0.rtLevelPanel.Find("title/level"), arg_10_0.apartment.level)
	setText(arg_10_0.rtLevelPanel.Find("title/Text"), i18n("dorm3d_favor_level") .. string.format("%d/%d", var_10_0, var_10_1))
	setSlider(arg_10_0.rtLevelPanel.Find("title/slider"), 0, var_10_1, var_10_0)
	arg_10_0.levelItemList.align(getDorm3dGameset("favor_level")[1])
	setImageAlpha(arg_10_0.rtLevelPanel.Find("bottom/btn_time/Image"), 1)
	setActive(arg_10_0.rtLevelPanel.Find("bottom/btn_time/lock"), False)
	setImageAlpha(arg_10_0.rtLevelPanel.Find("bottom/btn_skin/Image"), #arg_10_0.apartment.skinList < 2 and 0.2 or 1)
	setActive(arg_10_0.rtLevelPanel.Find("bottom/btn_skin/lock"), #arg_10_0.apartment.skinList < 2)

def var_0_0.ShowTimeSelectWindow(arg_11_0):
	local var_11_0 = arg_11_0.rtTimeSelectWindow.Find("panel")

	setText(var_11_0.Find("title"), i18n("dorm3d_time_choose"))

	for iter_11_0, iter_11_1 in ipairs({
		"day",
		"twilight",
		"night"
	}):
		local var_11_1 = var_11_0.Find("content/" .. iter_11_1)

		setText(var_11_1.Find("now/Text"), i18n("dorm3d_now_time"))
		setActive(var_11_1.Find("now"), iter_11_0 == arg_11_0.contextData.timeIndex)
		onToggle(arg_11_0, var_11_1, function(arg_12_0)
			if arg_12_0 == True:
				arg_11_0.selectTimeIndex = iter_11_0, SFX_PANEL)
		triggerToggle(var_11_1, iter_11_0 == arg_11_0.contextData.timeIndex)

	setText(var_11_0.Find("bottom/toggle_lock/Text"), i18n("dorm3d_is_auto_time"))
	onToggle(arg_11_0, var_11_0.Find("bottom/toggle_lock"), function(arg_13_0)
		if arg_13_0:
			PlayerPrefs.SetInt("DORM3D_SCENE_LOCK_TIME", 0)
		else
			PlayerPrefs.SetInt("DORM3D_SCENE_LOCK_TIME", arg_11_0.contextData.timeIndex), SFX_PANEL)
	triggerToggle(var_11_0.Find("bottom/toggle_lock"), PlayerPrefs.GetInt("DORM3D_SCENE_LOCK_TIME", 0) == 0)
	onButton(arg_11_0, var_11_0.Find("bottom/btn_confirm"), function()
		warning(arg_11_0.contextData.timeIndex, arg_11_0.selectTimeIndex)

		if arg_11_0.contextData.timeIndex == arg_11_0.selectTimeIndex:
			return
		else
			if PlayerPrefs.GetInt("DORM3D_SCENE_LOCK_TIME", 0) != 0:
				PlayerPrefs.SetInt("DORM3D_SCENE_LOCK_TIME", arg_11_0.selectTimeIndex)

			triggerButton(arg_11_0.rtTimeSelectWindow.Find("bg"))
			arg_11_0.emit(Dorm3dLevelMediator.CHAMGE_TIME, arg_11_0.selectTimeIndex), SFX_CONFIRM)
	setActive(arg_11_0.rtTimeSelectWindow, True)
	pg.UIMgr.GetInstance().OverlayPanel(arg_11_0.rtTimeSelectWindow, {
		weight = LayerWeightConst.SECOND_LAYER,
		groupName = LayerWeightConst.GROUP_DORM3D
	})

def var_0_0.ShowSkinSelectWindow(arg_15_0):
	local var_15_0 = arg_15_0.rtSkinSelectWindow.Find("panel")

	setText(var_15_0.Find("title"), i18n("dorm3d_clothing_choose"))
	UIItemList.StaticAlign(var_15_0.Find("content"), var_15_0.Find("content/tpl"), #arg_15_0.apartment.skinList, function(arg_16_0, arg_16_1, arg_16_2)
		arg_16_1 = arg_16_1 + 1

		if arg_16_0 == UIItemList.EventUpdate:
			local var_16_0 = arg_15_0.apartment.skinList[arg_16_1]

			if var_16_0 == 0:
				var_16_0 = arg_15_0.apartment.getConfig("skin_model")

			GetImageSpriteFromAtlasAsync(string.format("dorm3dselect/%d_skin", var_16_0), "", arg_16_2.Find("Image"))
			GetImageSpriteFromAtlasAsync(string.format("dorm3dselect/%s_name", pg.dorm3d_resource[var_16_0].picture), "", arg_16_2.Find("name"))
			setText(arg_16_2.Find("select/now/Text"), i18n("dorm3d_now_clothing"))
			setActive(arg_16_2.Find("select/now"), arg_15_0.apartment.getSkinId() == var_16_0)
			onToggle(arg_15_0, arg_16_2, function(arg_17_0)
				if arg_17_0 == True:
					arg_15_0.selectSkinId = var_16_0, SFX_PANEL)
			triggerToggle(arg_16_2, arg_15_0.apartment.getSkinId() == var_16_0))
	setText(var_15_0.Find("bottom/btn_confirm/Text"), i18n("word_ok"))
	onButton(arg_15_0, var_15_0.Find("bottom/btn_confirm"), function()
		if arg_15_0.apartment.getSkinId() == arg_15_0.selectSkinId:
			pg.TipsMgr.GetInstance().ShowTips("this skin is allready dress")
		else
			triggerButton(arg_15_0.rtSkinSelectWindow.Find("bg"))
			arg_15_0.emit(Dorm3dLevelMediator.CHANGE_SKIN, arg_15_0.apartment.configId, arg_15_0.selectSkinId), SFX_CONFIRM)
	setActive(arg_15_0.rtSkinSelectWindow, True)
	pg.UIMgr.GetInstance().OverlayPanel(arg_15_0.rtSkinSelectWindow, {
		weight = LayerWeightConst.SECOND_LAYER,
		groupName = LayerWeightConst.GROUP_DORM3D
	})

def var_0_0.onBackPressed(arg_19_0):
	if isActive(arg_19_0.rtSkinSelectWindow):
		triggerButton(arg_19_0.rtSkinSelectWindow.Find("bg"))
	elif isActive(arg_19_0.rtTimeSelectWindow):
		triggerButton(arg_19_0.rtTimeSelectWindow.Find("bg"))
	else
		var_0_0.super.onBackPressed(arg_19_0)

def var_0_0.willExit(arg_20_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_20_0._tf)

return var_0_0
