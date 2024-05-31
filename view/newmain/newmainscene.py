local var_0_0 = class("NewMainScene", import("..base.BaseUI"))

var_0_0.THEME_CLASSIC = 1
var_0_0.THEME_MELLOW = 2
var_0_0.OPEN_LIVEAREA = "NewMainScene.OPEN_LIVEAREA"
var_0_0.FOLD = "NewMainScene.FOLD"
var_0_0.CHAT_STATE_CHANGE = "NewMainScene.CHAT_STATE_CHANGE"
var_0_0.ON_CHANGE_SKIN = "NewMainScene.ON_CHANGE_SKIN"
var_0_0.ON_BUFF_DESC = "NewMainScene.ON_BUFF_DESC"
var_0_0.ON_SKIN_FREEUSAGE_DESC = "NewMainScene.ON_SKIN_FREEUSAGE_DESC"
var_0_0.ENABLE_PAITING_MOVE = "NewMainScene.ENABLE_PAITING_MOVE"
var_0_0.ON_ENTER_DONE = "NewMainScene.ON_ENTER_DONE"
var_0_0.ENTER_SILENT_VIEW = "NewMainScene.ENTER_SILENT_VIEW"
var_0_0.EXIT_SILENT_VIEW = "NewMainScene.EXIT_SILENT_VIEW"
var_0_0.RESET_L2D = "NewMainScene.RESET_L2D"

def var_0_0.getUIName(arg_1_0):
	return "NewMainUI"

def var_0_0.needCache(arg_2_0):
	return True

def var_0_0.GetThemeStyle(arg_3_0):
	return getProxy(SettingsProxy).GetMainSceneThemeStyle()

def var_0_0.PlayBGM(arg_4_0):
	return

def var_0_0.GetFlagShip(arg_5_0):
	return (getProxy(PlayerProxy).getRawData().GetFlagShip())

def var_0_0.PlayBgm(arg_6_0, arg_6_1):
	local var_6_0

	if arg_6_1.IsBgmSkin() and getProxy(SettingsProxy).IsBGMEnable():
		var_6_0 = arg_6_1.GetSkinBgm()

	if not var_6_0:
		local var_6_1, var_6_2 = MainBGView.GetBgAndBgm()

		var_6_0 = var_6_2

	var_6_0 = var_6_0 or var_0_0.super.getBGM(arg_6_0)

	if var_6_0:
		pg.BgmMgr.GetInstance().Push(arg_6_0.__cname, var_6_0)

def var_0_0.ResUISettings(arg_7_0):
	return {
		showType = PlayerResUI.TYPE_ALL,
		anim = not arg_7_0.resAnimFlag,
		weight = LayerWeightConst.BASE_LAYER + 1
	}

def var_0_0.ShowOrHideResUI(arg_8_0, arg_8_1):
	if not arg_8_0.isInit:
		return

	var_0_0.super.ShowOrHideResUI(arg_8_0, arg_8_1)

def var_0_0.init(arg_9_0):
	arg_9_0.mainCG = GetOrAddComponent(arg_9_0._tf, typeof(CanvasGroup))
	arg_9_0.bgView = MainBGView.New(arg_9_0.findTF("Sea/bg"))
	arg_9_0.paintingView = MainPaintingView.New(arg_9_0.findTF("paint"), arg_9_0.findTF("paintBg"), arg_9_0.event)
	arg_9_0.effectView = MainEffectView.New(arg_9_0.findTF("paint/effect"))
	arg_9_0.buffDescPage = MainBuffDescPage.New(arg_9_0._tf, arg_9_0.event)
	arg_9_0.calibrationPage = MainCalibrationPage.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)
	arg_9_0.silentView = MainSilentView.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)
	arg_9_0.silentChecker = MainSilentChecker.New(arg_9_0.event)
	arg_9_0.skinExperienceDisplayPage = SkinExperienceDiplayPage.New(arg_9_0._tf, arg_9_0.event)

	if USE_OLD_MAIN_LIVE_AREA_UI:
		arg_9_0.liveAreaPage = MainLiveAreaOldPage.New(arg_9_0._tf, arg_9_0.event)
	else
		arg_9_0.liveAreaPage = MainLiveAreaPage.New(arg_9_0._tf, arg_9_0.event)

	pg.redDotHelper = MainReddotView.New()
	arg_9_0.sequenceView = MainSequenceView.New()
	arg_9_0.awakeSequenceView = MainAwakeSequenceView.New()
	arg_9_0.themes = {
		[var_0_0.THEME_CLASSIC] = NewMainClassicTheme.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData),
		[var_0_0.THEME_MELLOW] = NewMainMellowTheme.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)
	}

def var_0_0.didEnter(arg_10_0):
	arg_10_0.bind(var_0_0.FOLD, function(arg_11_0, arg_11_1)
		arg_10_0.FoldPanels(arg_11_1)

		local var_11_0 = arg_10_0.paintingView.ship

		if not var_11_0:
			return

		arg_10_0.calibrationPage.ExecuteAction("ShowOrHide", arg_11_1, arg_10_0.bgView.ship, arg_10_0.theme.GetPaintingOffset(var_11_0), arg_10_0.theme.GetCalibrationBG()))
	arg_10_0.bind(var_0_0.ON_CHANGE_SKIN, function(arg_12_0)
		arg_10_0.SwitchToNextShip())
	arg_10_0.bind(var_0_0.ENTER_SILENT_VIEW, function()
		arg_10_0.ExitCalibrationView()
		arg_10_0.FoldPanels(True)
		arg_10_0.silentView.ExecuteAction("Show"))
	arg_10_0.bind(GAME.WILL_LOGOUT, function()
		arg_10_0.GameLogout())
	arg_10_0.bind(var_0_0.EXIT_SILENT_VIEW, function()
		arg_10_0.ExitSilentView()
		arg_10_0.SetUpSilentChecker()
		pg.redDotHelper._Refresh())
	arg_10_0.bind(var_0_0.ON_SKIN_FREEUSAGE_DESC, function(arg_16_0, arg_16_1)
		arg_10_0.skinExperienceDisplayPage.ExecuteAction("Show", arg_16_1))
	arg_10_0.bind(NewMainScene.OPEN_LIVEAREA, function(arg_17_0)
		arg_10_0.liveAreaPage.ExecuteAction("Show"))
	arg_10_0.SetUp()

def var_0_0.SetUp(arg_18_0, arg_18_1):
	arg_18_0.mainCG.blocksRaycasts = False
	arg_18_0.isInit = False
	arg_18_0.resAnimFlag = False

	local var_18_0

	seriesAsync({
		function(arg_19_0)
			arg_18_0.awakeSequenceView.Execute(arg_19_0),
		function(arg_20_0)
			var_18_0 = arg_18_0.GetFlagShip()

			arg_18_0.bgView.Init(var_18_0)
			onNextTick(arg_20_0),
		function(arg_21_0)
			arg_18_0.theme = arg_18_0.themes[arg_18_0.GetThemeStyle()]

			arg_18_0.theme.ExecuteAction("Show", arg_21_0),
		function(arg_22_0)
			onNextTick(arg_22_0),
		function(arg_23_0)
			arg_18_0.isInit = True

			arg_18_0.theme.PlayEnterAnimation(var_18_0, arg_23_0)

			local var_23_0 = arg_18_0.theme.GetPaintingOffset(var_18_0)

			arg_18_0.paintingView.Init(var_18_0, var_23_0, arg_18_1)

			arg_18_0.resAnimFlag = True,
		function(arg_24_0)
			arg_18_0.PlayBgm(var_18_0)
			arg_18_0.effectView.Init(var_18_0)
			arg_18_0.theme.init(var_18_0)
			onNextTick(arg_24_0),
		function(arg_25_0)
			arg_18_0.ShowOrHideResUI(arg_18_0.theme.ApplyDefaultResUI())
			arg_18_0.sequenceView.Execute(arg_25_0)
	}, function()
		arg_18_0.SetUpSilentChecker()
		arg_18_0.emit(var_0_0.ON_ENTER_DONE)

		arg_18_0.mainCG.blocksRaycasts = True)

def var_0_0.SetUpSilentChecker(arg_27_0):
	local var_27_0 = getProxy(SettingsProxy).GetMainSceneScreenSleepTime()

	arg_27_0.defaultSleepTimeout = Screen.sleepTimeout
	Screen.sleepTimeout = var_27_0

	arg_27_0.silentChecker.SetUp()

def var_0_0.RevertSleepTimeout(arg_28_0):
	if arg_28_0.defaultSleepTimeout and Screen.sleepTimeout != arg_28_0.defaultSleepTimeout:
		Screen.sleepTimeout = arg_28_0.defaultSleepTimeout

	arg_28_0.defaultSleepTimeout = None

def var_0_0.FoldPanels(arg_29_0, arg_29_1):
	if not arg_29_0.theme:
		return

	arg_29_0.theme.OnFoldPanels(arg_29_1)
	arg_29_0.paintingView.Fold(arg_29_1, 0.5)
	pg.playerResUI.Fold(arg_29_1, 0.5)

def var_0_0.SwitchToNextShip(arg_30_0):
	if arg_30_0.paintingView.IsLoading() or arg_30_0.bgView.IsLoading() or not arg_30_0.theme:
		return

	local var_30_0 = getProxy(PlayerProxy).getRawData().GetNextFlagShip()

	if arg_30_0.bgView.ship.skinId != var_30_0.skinId or arg_30_0.bgView.ship.id != var_30_0.id:
		arg_30_0.bgView.Refresh(var_30_0)
		arg_30_0.PlayBgm(var_30_0)
		arg_30_0.paintingView.Refresh(var_30_0, arg_30_0.theme.GetPaintingOffset(var_30_0))
		arg_30_0.effectView.Refresh(var_30_0)
		arg_30_0.theme.OnSwitchToNextShip(var_30_0)

def var_0_0.OnVisible(arg_31_0):
	local var_31_0 = arg_31_0.themes[arg_31_0.GetThemeStyle()]

	if not (not arg_31_0.theme or var_31_0 != arg_31_0.theme):
		arg_31_0.Refresh()
	else
		arg_31_0.UnloadTheme()
		arg_31_0.SetUp(True)

def var_0_0.Refresh(arg_32_0):
	arg_32_0.mainCG.blocksRaycasts = False

	seriesAsync({
		function(arg_33_0)
			arg_32_0.awakeSequenceView.Execute(arg_33_0),
		function(arg_34_0)
			arg_32_0.isInit = True

			arg_32_0.ShowOrHideResUI(arg_32_0.theme.ApplyDefaultResUI())

			local var_34_0 = arg_32_0.GetFlagShip()

			arg_32_0.bgView.Refresh(var_34_0)
			arg_32_0.paintingView.Refresh(var_34_0, arg_32_0.theme.GetPaintingOffset(var_34_0))
			arg_32_0.effectView.Refresh(var_34_0)
			arg_32_0.theme.Refresh(var_34_0)
			arg_32_0.PlayBgm(var_34_0)
			pg.redDotHelper.Refresh()
			arg_34_0(),
		function(arg_35_0)
			arg_32_0.sequenceView.Execute(arg_35_0)
	}, function()
		arg_32_0.SetUpSilentChecker()
		arg_32_0.emit(var_0_0.ON_ENTER_DONE)

		arg_32_0.mainCG.blocksRaycasts = True)

def var_0_0.OnDisVisible(arg_37_0):
	arg_37_0.FoldPanels(False)
	arg_37_0.paintingView.Disable()
	arg_37_0.bgView.Disable()
	arg_37_0.sequenceView.Disable()
	arg_37_0.awakeSequenceView.Disable()
	arg_37_0.theme.Disable()
	pg.redDotHelper.Disable()
	arg_37_0.buffDescPage.Disable()
	arg_37_0.silentChecker.Disable()
	arg_37_0.calibrationPage.Destroy()
	arg_37_0.calibrationPage.Reset()
	arg_37_0.skinExperienceDisplayPage.Destroy()
	arg_37_0.skinExperienceDisplayPage.Reset()
	arg_37_0.liveAreaPage.Destroy()
	arg_37_0.liveAreaPage.Reset()

	arg_37_0.isInit = False

	arg_37_0.RevertSleepTimeout()

def var_0_0.UnloadTheme(arg_38_0):
	if arg_38_0.theme:
		arg_38_0.theme.Destroy()
		arg_38_0.theme.Reset()

		arg_38_0.theme = None

def var_0_0.ExitCalibrationView(arg_39_0):
	if arg_39_0.calibrationPage and arg_39_0.calibrationPage.GetLoaded() and arg_39_0.calibrationPage.isShowing():
		triggerButton(arg_39_0.calibrationPage.backBtn)

def var_0_0.ExitSilentView(arg_40_0):
	if arg_40_0.silentView and arg_40_0.silentView.GetLoaded() and arg_40_0.silentView.isShowing():
		arg_40_0.FoldPanels(False)
		arg_40_0.silentView.Destroy()
		arg_40_0.silentView.Reset()

def var_0_0.GameLogout(arg_41_0):
	arg_41_0.ExitCalibrationView()
	arg_41_0.ExitSilentView()

def var_0_0.onBackPressed(arg_42_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	if arg_42_0.silentView and arg_42_0.silentView.GetLoaded() and arg_42_0.silentView.isShowing():
		arg_42_0.ExitSilentView()

		return

	if arg_42_0.liveAreaPage and arg_42_0.liveAreaPage.GetLoaded() and arg_42_0.liveAreaPage.isShowing():
		arg_42_0.liveAreaPage.Hide()

		return

	if arg_42_0.calibrationPage and arg_42_0.calibrationPage.GetLoaded() and arg_42_0.calibrationPage.isShowing():
		triggerButton(arg_42_0.calibrationPage._parentTf)

		return

	pg.SdkMgr.GetInstance().OnAndoridBackPress()
	pg.PushNotificationMgr.GetInstance().PushAll()

def var_0_0.willExit(arg_43_0):
	arg_43_0.bgView.Dispose()

	arg_43_0.bgView = None

	if arg_43_0.calibrationPage:
		arg_43_0.calibrationPage.Destroy()

		arg_43_0.calibrationPage = None

	if arg_43_0.silentView:
		arg_43_0.silentView.Destroy()

		arg_43_0.silentView = None

	arg_43_0.paintingView.Dispose()

	arg_43_0.paintingView = None

	arg_43_0.liveAreaPage.Destroy()

	arg_43_0.liveAreaPage = None

	arg_43_0.sequenceView.Dispose()

	arg_43_0.sequenceView = None

	arg_43_0.awakeSequenceView.Dispose()

	arg_43_0.awakeSequenceView = None

	arg_43_0.effectView.Dispose()

	arg_43_0.effectView = None

	pg.redDotHelper.Dispose()

	pg.redDotHelper = None

	arg_43_0.buffDescPage.Destroy()

	arg_43_0.buffDescPage = None

	arg_43_0.silentChecker.Dispose()

	arg_43_0.silentChecker = None

	arg_43_0.skinExperienceDisplayPage.Destroy()

	arg_43_0.skinExperienceDisplayPage = None

	arg_43_0.UnloadTheme()
	arg_43_0.RevertSleepTimeout()

return var_0_0
