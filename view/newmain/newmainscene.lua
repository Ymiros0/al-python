local var_0_0 = class("NewMainScene", import("..base.BaseUI"))

var_0_0.THEME_CLASSIC = 1
var_0_0.THEME_MELLOW = 2
var_0_0.OPEN_LIVEAREA = "NewMainScene:OPEN_LIVEAREA"
var_0_0.FOLD = "NewMainScene:FOLD"
var_0_0.CHAT_STATE_CHANGE = "NewMainScene:CHAT_STATE_CHANGE"
var_0_0.ON_CHANGE_SKIN = "NewMainScene:ON_CHANGE_SKIN"
var_0_0.ON_BUFF_DESC = "NewMainScene:ON_BUFF_DESC"
var_0_0.ON_SKIN_FREEUSAGE_DESC = "NewMainScene:ON_SKIN_FREEUSAGE_DESC"
var_0_0.ENABLE_PAITING_MOVE = "NewMainScene:ENABLE_PAITING_MOVE"
var_0_0.ON_ENTER_DONE = "NewMainScene:ON_ENTER_DONE"
var_0_0.ENTER_SILENT_VIEW = "NewMainScene:ENTER_SILENT_VIEW"
var_0_0.EXIT_SILENT_VIEW = "NewMainScene:EXIT_SILENT_VIEW"
var_0_0.RESET_L2D = "NewMainScene:RESET_L2D"

function var_0_0.getUIName(arg_1_0)
	return "NewMainUI"
end

function var_0_0.needCache(arg_2_0)
	return true
end

function var_0_0.GetThemeStyle(arg_3_0)
	return getProxy(SettingsProxy):GetMainSceneThemeStyle()
end

function var_0_0.PlayBGM(arg_4_0)
	return
end

function var_0_0.GetFlagShip(arg_5_0)
	return (getProxy(PlayerProxy):getRawData():GetFlagShip())
end

function var_0_0.PlayBgm(arg_6_0, arg_6_1)
	local var_6_0

	if arg_6_1:IsBgmSkin() and getProxy(SettingsProxy):IsBGMEnable() then
		var_6_0 = arg_6_1:GetSkinBgm()
	end

	if not var_6_0 then
		local var_6_1, var_6_2 = MainBGView.GetBgAndBgm()

		var_6_0 = var_6_2
	end

	var_6_0 = var_6_0 or var_0_0.super.getBGM(arg_6_0)

	if var_6_0 then
		pg.BgmMgr.GetInstance():Push(arg_6_0.__cname, var_6_0)
	end
end

function var_0_0.ResUISettings(arg_7_0)
	return {
		showType = PlayerResUI.TYPE_ALL,
		anim = not arg_7_0.resAnimFlag,
		weight = LayerWeightConst.BASE_LAYER + 1
	}
end

function var_0_0.ShowOrHideResUI(arg_8_0, arg_8_1)
	if not arg_8_0.isInit then
		return
	end

	var_0_0.super.ShowOrHideResUI(arg_8_0, arg_8_1)
end

function var_0_0.init(arg_9_0)
	arg_9_0.mainCG = GetOrAddComponent(arg_9_0._tf, typeof(CanvasGroup))
	arg_9_0.bgView = MainBGView.New(arg_9_0:findTF("Sea/bg"))
	arg_9_0.paintingView = MainPaintingView.New(arg_9_0:findTF("paint"), arg_9_0:findTF("paintBg"), arg_9_0.event)
	arg_9_0.effectView = MainEffectView.New(arg_9_0:findTF("paint/effect"))
	arg_9_0.buffDescPage = MainBuffDescPage.New(arg_9_0._tf, arg_9_0.event)
	arg_9_0.calibrationPage = MainCalibrationPage.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)
	arg_9_0.silentView = MainSilentView.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)
	arg_9_0.silentChecker = MainSilentChecker.New(arg_9_0.event)
	arg_9_0.skinExperienceDisplayPage = SkinExperienceDiplayPage.New(arg_9_0._tf, arg_9_0.event)

	if USE_OLD_MAIN_LIVE_AREA_UI then
		arg_9_0.liveAreaPage = MainLiveAreaOldPage.New(arg_9_0._tf, arg_9_0.event)
	else
		arg_9_0.liveAreaPage = MainLiveAreaPage.New(arg_9_0._tf, arg_9_0.event)
	end

	pg.redDotHelper = MainReddotView.New()
	arg_9_0.sequenceView = MainSequenceView.New()
	arg_9_0.awakeSequenceView = MainAwakeSequenceView.New()
	arg_9_0.themes = {
		[var_0_0.THEME_CLASSIC] = NewMainClassicTheme.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData),
		[var_0_0.THEME_MELLOW] = NewMainMellowTheme.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)
	}
end

function var_0_0.didEnter(arg_10_0)
	arg_10_0:bind(var_0_0.FOLD, function(arg_11_0, arg_11_1)
		arg_10_0:FoldPanels(arg_11_1)

		local var_11_0 = arg_10_0.paintingView.ship

		if not var_11_0 then
			return
		end

		arg_10_0.calibrationPage:ExecuteAction("ShowOrHide", arg_11_1, arg_10_0.bgView.ship, arg_10_0.theme:GetPaintingOffset(var_11_0), arg_10_0.theme:GetCalibrationBG())
	end)
	arg_10_0:bind(var_0_0.ON_CHANGE_SKIN, function(arg_12_0)
		arg_10_0:SwitchToNextShip()
	end)
	arg_10_0:bind(var_0_0.ENTER_SILENT_VIEW, function()
		arg_10_0:ExitCalibrationView()
		arg_10_0:FoldPanels(true)
		arg_10_0.silentView:ExecuteAction("Show")
	end)
	arg_10_0:bind(GAME.WILL_LOGOUT, function()
		arg_10_0:GameLogout()
	end)
	arg_10_0:bind(var_0_0.EXIT_SILENT_VIEW, function()
		arg_10_0:ExitSilentView()
		arg_10_0:SetUpSilentChecker()
		pg.redDotHelper:_Refresh()
	end)
	arg_10_0:bind(var_0_0.ON_SKIN_FREEUSAGE_DESC, function(arg_16_0, arg_16_1)
		arg_10_0.skinExperienceDisplayPage:ExecuteAction("Show", arg_16_1)
	end)
	arg_10_0:bind(NewMainScene.OPEN_LIVEAREA, function(arg_17_0)
		arg_10_0.liveAreaPage:ExecuteAction("Show")
	end)
	arg_10_0:SetUp()
end

function var_0_0.SetUp(arg_18_0, arg_18_1)
	arg_18_0.mainCG.blocksRaycasts = false
	arg_18_0.isInit = false
	arg_18_0.resAnimFlag = false

	local var_18_0

	seriesAsync({
		function(arg_19_0)
			arg_18_0.awakeSequenceView:Execute(arg_19_0)
		end,
		function(arg_20_0)
			var_18_0 = arg_18_0:GetFlagShip()

			arg_18_0.bgView:Init(var_18_0)
			onNextTick(arg_20_0)
		end,
		function(arg_21_0)
			arg_18_0.theme = arg_18_0.themes[arg_18_0:GetThemeStyle()]

			arg_18_0.theme:ExecuteAction("Show", arg_21_0)
		end,
		function(arg_22_0)
			onNextTick(arg_22_0)
		end,
		function(arg_23_0)
			arg_18_0.isInit = true

			arg_18_0.theme:PlayEnterAnimation(var_18_0, arg_23_0)

			local var_23_0 = arg_18_0.theme:GetPaintingOffset(var_18_0)

			arg_18_0.paintingView:Init(var_18_0, var_23_0, arg_18_1)

			arg_18_0.resAnimFlag = true
		end,
		function(arg_24_0)
			arg_18_0:PlayBgm(var_18_0)
			arg_18_0.effectView:Init(var_18_0)
			arg_18_0.theme:init(var_18_0)
			onNextTick(arg_24_0)
		end,
		function(arg_25_0)
			arg_18_0:ShowOrHideResUI(arg_18_0.theme:ApplyDefaultResUI())
			arg_18_0.sequenceView:Execute(arg_25_0)
		end
	}, function()
		arg_18_0:SetUpSilentChecker()
		arg_18_0:emit(var_0_0.ON_ENTER_DONE)

		arg_18_0.mainCG.blocksRaycasts = true
	end)
end

function var_0_0.SetUpSilentChecker(arg_27_0)
	local var_27_0 = getProxy(SettingsProxy):GetMainSceneScreenSleepTime()

	arg_27_0.defaultSleepTimeout = Screen.sleepTimeout
	Screen.sleepTimeout = var_27_0

	arg_27_0.silentChecker:SetUp()
end

function var_0_0.RevertSleepTimeout(arg_28_0)
	if arg_28_0.defaultSleepTimeout and Screen.sleepTimeout ~= arg_28_0.defaultSleepTimeout then
		Screen.sleepTimeout = arg_28_0.defaultSleepTimeout
	end

	arg_28_0.defaultSleepTimeout = nil
end

function var_0_0.FoldPanels(arg_29_0, arg_29_1)
	if not arg_29_0.theme then
		return
	end

	arg_29_0.theme:OnFoldPanels(arg_29_1)
	arg_29_0.paintingView:Fold(arg_29_1, 0.5)
	pg.playerResUI:Fold(arg_29_1, 0.5)
end

function var_0_0.SwitchToNextShip(arg_30_0)
	if arg_30_0.paintingView:IsLoading() or arg_30_0.bgView:IsLoading() or not arg_30_0.theme then
		return
	end

	local var_30_0 = getProxy(PlayerProxy):getRawData():GetNextFlagShip()

	if arg_30_0.bgView.ship.skinId ~= var_30_0.skinId or arg_30_0.bgView.ship.id ~= var_30_0.id then
		arg_30_0.bgView:Refresh(var_30_0)
		arg_30_0:PlayBgm(var_30_0)
		arg_30_0.paintingView:Refresh(var_30_0, arg_30_0.theme:GetPaintingOffset(var_30_0))
		arg_30_0.effectView:Refresh(var_30_0)
		arg_30_0.theme:OnSwitchToNextShip(var_30_0)
	end
end

function var_0_0.OnVisible(arg_31_0)
	local var_31_0 = arg_31_0.themes[arg_31_0:GetThemeStyle()]

	if not (not arg_31_0.theme or var_31_0 ~= arg_31_0.theme) then
		arg_31_0:Refresh()
	else
		arg_31_0:UnloadTheme()
		arg_31_0:SetUp(true)
	end
end

function var_0_0.Refresh(arg_32_0)
	arg_32_0.mainCG.blocksRaycasts = false

	seriesAsync({
		function(arg_33_0)
			arg_32_0.awakeSequenceView:Execute(arg_33_0)
		end,
		function(arg_34_0)
			arg_32_0.isInit = true

			arg_32_0:ShowOrHideResUI(arg_32_0.theme:ApplyDefaultResUI())

			local var_34_0 = arg_32_0:GetFlagShip()

			arg_32_0.bgView:Refresh(var_34_0)
			arg_32_0.paintingView:Refresh(var_34_0, arg_32_0.theme:GetPaintingOffset(var_34_0))
			arg_32_0.effectView:Refresh(var_34_0)
			arg_32_0.theme:Refresh(var_34_0)
			arg_32_0:PlayBgm(var_34_0)
			pg.redDotHelper:Refresh()
			arg_34_0()
		end,
		function(arg_35_0)
			arg_32_0.sequenceView:Execute(arg_35_0)
		end
	}, function()
		arg_32_0:SetUpSilentChecker()
		arg_32_0:emit(var_0_0.ON_ENTER_DONE)

		arg_32_0.mainCG.blocksRaycasts = true
	end)
end

function var_0_0.OnDisVisible(arg_37_0)
	arg_37_0:FoldPanels(false)
	arg_37_0.paintingView:Disable()
	arg_37_0.bgView:Disable()
	arg_37_0.sequenceView:Disable()
	arg_37_0.awakeSequenceView:Disable()
	arg_37_0.theme:Disable()
	pg.redDotHelper:Disable()
	arg_37_0.buffDescPage:Disable()
	arg_37_0.silentChecker:Disable()
	arg_37_0.calibrationPage:Destroy()
	arg_37_0.calibrationPage:Reset()
	arg_37_0.skinExperienceDisplayPage:Destroy()
	arg_37_0.skinExperienceDisplayPage:Reset()
	arg_37_0.liveAreaPage:Destroy()
	arg_37_0.liveAreaPage:Reset()

	arg_37_0.isInit = false

	arg_37_0:RevertSleepTimeout()
end

function var_0_0.UnloadTheme(arg_38_0)
	if arg_38_0.theme then
		arg_38_0.theme:Destroy()
		arg_38_0.theme:Reset()

		arg_38_0.theme = nil
	end
end

function var_0_0.ExitCalibrationView(arg_39_0)
	if arg_39_0.calibrationPage and arg_39_0.calibrationPage:GetLoaded() and arg_39_0.calibrationPage:isShowing() then
		triggerButton(arg_39_0.calibrationPage.backBtn)
	end
end

function var_0_0.ExitSilentView(arg_40_0)
	if arg_40_0.silentView and arg_40_0.silentView:GetLoaded() and arg_40_0.silentView:isShowing() then
		arg_40_0:FoldPanels(false)
		arg_40_0.silentView:Destroy()
		arg_40_0.silentView:Reset()
	end
end

function var_0_0.GameLogout(arg_41_0)
	arg_41_0:ExitCalibrationView()
	arg_41_0:ExitSilentView()
end

function var_0_0.onBackPressed(arg_42_0)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)

	if arg_42_0.silentView and arg_42_0.silentView:GetLoaded() and arg_42_0.silentView:isShowing() then
		arg_42_0:ExitSilentView()

		return
	end

	if arg_42_0.liveAreaPage and arg_42_0.liveAreaPage:GetLoaded() and arg_42_0.liveAreaPage:isShowing() then
		arg_42_0.liveAreaPage:Hide()

		return
	end

	if arg_42_0.calibrationPage and arg_42_0.calibrationPage:GetLoaded() and arg_42_0.calibrationPage:isShowing() then
		triggerButton(arg_42_0.calibrationPage._parentTf)

		return
	end

	pg.SdkMgr.GetInstance():OnAndoridBackPress()
	pg.PushNotificationMgr.GetInstance():PushAll()
end

function var_0_0.willExit(arg_43_0)
	arg_43_0.bgView:Dispose()

	arg_43_0.bgView = nil

	if arg_43_0.calibrationPage then
		arg_43_0.calibrationPage:Destroy()

		arg_43_0.calibrationPage = nil
	end

	if arg_43_0.silentView then
		arg_43_0.silentView:Destroy()

		arg_43_0.silentView = nil
	end

	arg_43_0.paintingView:Dispose()

	arg_43_0.paintingView = nil

	arg_43_0.liveAreaPage:Destroy()

	arg_43_0.liveAreaPage = nil

	arg_43_0.sequenceView:Dispose()

	arg_43_0.sequenceView = nil

	arg_43_0.awakeSequenceView:Dispose()

	arg_43_0.awakeSequenceView = nil

	arg_43_0.effectView:Dispose()

	arg_43_0.effectView = nil

	pg.redDotHelper:Dispose()

	pg.redDotHelper = nil

	arg_43_0.buffDescPage:Destroy()

	arg_43_0.buffDescPage = nil

	arg_43_0.silentChecker:Dispose()

	arg_43_0.silentChecker = nil

	arg_43_0.skinExperienceDisplayPage:Destroy()

	arg_43_0.skinExperienceDisplayPage = nil

	arg_43_0:UnloadTheme()
	arg_43_0:RevertSleepTimeout()
end

return var_0_0
