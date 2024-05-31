local var_0_0 = class("NewSettingsScene", import("..base.BaseUI"))

var_0_0.PAGE_OTHER = 1
var_0_0.PAGE_OPTION = 2
var_0_0.PAGE_BATTLE = 3
var_0_0.PAGE_RES = 4

function var_0_0.getUIName(arg_1_0)
	return "NewSettingsUI"
end

function var_0_0.OnShowDescWindow(arg_2_0, arg_2_1)
	arg_2_0.descWindow:ExecuteAction("Show", arg_2_1.desc, arg_2_1.alignment)
end

function var_0_0.OnClearExchangeCode(arg_3_0)
	if arg_3_0.pages and arg_3_0.pages[1] and arg_3_0.pages[1]:GetLoaded() then
		arg_3_0.pages[1]:OnClearExchangeCode()
	end
end

function var_0_0.OnShowTranscode(arg_4_0, arg_4_1)
	if arg_4_0.pages and arg_4_0.pages[1] and arg_4_0.pages[1]:GetLoaded() then
		arg_4_0.pages[1]:OnShowTranscode(arg_4_1)
	end
end

function var_0_0.OnCheckAllAccountState(arg_5_0)
	if arg_5_0.pages and arg_5_0.pages[1] and arg_5_0.pages[1]:GetLoaded() then
		arg_5_0.pages[1]:OnCheckAllAccountState()
	end
end

function var_0_0.OnSecondPwdStateChange(arg_6_0)
	if arg_6_0.pages and arg_6_0.pages[1] and arg_6_0.pages[1]:GetLoaded() then
		arg_6_0.pages[1]:OnSecondPwdStateChange()
	end
end

function var_0_0.OnRandomFlagShipModeUpdate(arg_7_0)
	arg_7_0:emit(SettingsRandomFlagShipAndSkinPanel.EVT_UPDTAE)
end

function var_0_0.GetPage(arg_8_0, arg_8_1)
	for iter_8_0, iter_8_1 in ipairs(arg_8_0.pages) do
		if isa(iter_8_1, arg_8_1) then
			return iter_8_1
		end
	end
end

function var_0_0.init(arg_9_0)
	arg_9_0.backBtn = arg_9_0:findTF("blur_panel/adapt/top/back_btn")

	local var_9_0 = arg_9_0:findTF("pages")

	arg_9_0.pages = {
		SettingsOtherPage.New(var_9_0, arg_9_0.event, arg_9_0.contextData),
		SettingsOptionPage.New(var_9_0, arg_9_0.event, arg_9_0.contextData),
		SettingsBattlePage.New(var_9_0, arg_9_0.event, arg_9_0.contextData),
		SettingsResPage.New(var_9_0, arg_9_0.event, arg_9_0.contextData)
	}
	arg_9_0.toggles = {
		arg_9_0:findTF("blur_panel/adapt/left_length/other"),
		arg_9_0:findTF("blur_panel/adapt/left_length/options"),
		arg_9_0:findTF("blur_panel/adapt/left_length/battle_ui"),
		arg_9_0:findTF("blur_panel/adapt/left_length/resources")
	}
	arg_9_0.otherTip = arg_9_0.toggles[1]:Find("tip")
	arg_9_0.logoutBtn = arg_9_0:findTF("blur_panel/adapt/left_length/logout")
	arg_9_0.helpBtn = arg_9_0:findTF("blur_panel/adapt/left_length/help_us")
	arg_9_0.descWindow = SettingsMsgBosPage.New(arg_9_0._tf, arg_9_0.event)
end

function var_0_0.didEnter(arg_10_0)
	onButton(arg_10_0, arg_10_0.backBtn, function()
		arg_10_0:emit(var_0_0.ON_BACK)
	end, SFX_CANCEL)
	onButton(arg_10_0, arg_10_0.logoutBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("main_settingsScene_quest_exist"),
			onYes = function()
				arg_10_0:emit(NewSettingsMediator.ON_LOGOUT)
			end
		})
	end, SFX_PANEL)

	if PLATFORM_CODE == PLATFORM_US then
		setActive(arg_10_0.helpBtn, true)
		onButton(arg_10_0, arg_10_0.helpBtn, function()
			pg.SdkMgr.GetInstance():OpenYostarHelp()
		end, SFX_PANEL)
	elseif PLATFORM_CODE == PLATFORM_KR then
		setActive(arg_10_0.helpBtn, true)
		onButton(arg_10_0, arg_10_0.helpBtn, function()
			pg.SdkMgr.GetInstance():BugReport()
		end, SFX_CANCEL)
		arg_10_0.helpBtn:SetAsFirstSibling()
	end

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.toggles) do
		onToggle(arg_10_0, iter_10_1, function(arg_16_0)
			if arg_16_0 then
				arg_10_0:SwitchPage(iter_10_0)
			end
		end, SFX_PANEL)
	end

	setActive(arg_10_0.otherTip, PlayerPrefs.GetFloat("firstIntoOtherPanel") == 0)
	arg_10_0:EnterDefaultPage()
end

function var_0_0.EnterDefaultPage(arg_17_0)
	local var_17_0
	local var_17_1 = arg_17_0.contextData.toggle

	if var_17_1 and type(var_17_1) == "string" then
		if var_17_1 == "sound" or var_17_1 == "res" then
			var_17_0 = var_0_0.PAGE_RES
		else
			var_17_0 = table.indexof({
				"other",
				"options",
				"interface",
				"res"
			}, var_17_1)
		end
	end

	local var_17_2 = arg_17_0.contextData.page or var_17_0 or var_0_0.PAGE_RES

	triggerToggle(arg_17_0.toggles[var_17_2], true)
end

function var_0_0.SwitchPage(arg_18_0, arg_18_1)
	local var_18_0 = arg_18_0.pages[arg_18_1]

	if arg_18_0.page and arg_18_0.page ~= var_18_0 and arg_18_0.page:GetLoaded() then
		arg_18_0.page:Hide()
	end

	var_18_0:ExecuteAction("Show")

	arg_18_0.page = var_18_0

	if isa(var_18_0, SettingsOtherPage) and isActive(arg_18_0.otherTip) then
		setActive(arg_18_0.otherTip, false)
	end
end

function var_0_0.OpenYostarAlertView(arg_19_0)
	arg_19_0.yostarAlertView = YostarAlertView.New(arg_19_0._tf, arg_19_0.event, {
		isDestroyOnClose = true,
		isLinkMode = true
	})

	arg_19_0.yostarAlertView:Load()
	arg_19_0.yostarAlertView:ActionInvoke("Show")
end

function var_0_0.CloseYostarAlertView(arg_20_0)
	if arg_20_0.yostarAlertView and arg_20_0.yostarAlertView:CheckState(BaseSubView.STATES.INITED) then
		arg_20_0.yostarAlertView:Destroy()
	end
end

function var_0_0.onBackPressed(arg_21_0)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)

	local var_21_0 = GameObject.Find("OverlayCamera/Overlay/UIMain/DialogPanel")

	if isActive(var_21_0) then
		triggerButton(var_21_0.transform:Find("dialog/title/back"))

		return
	end

	arg_21_0:emit(var_0_0.ON_BACK)
end

function var_0_0.willExit(arg_22_0)
	for iter_22_0, iter_22_1 in pairs(arg_22_0.pages) do
		iter_22_1:Destroy()
	end

	if arg_22_0.descWindow then
		arg_22_0.descWindow:Destroy()

		arg_22_0.descWindow = nil
	end

	arg_22_0.page = nil
	arg_22_0.pages = nil
end

return var_0_0
