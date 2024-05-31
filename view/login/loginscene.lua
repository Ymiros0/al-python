﻿local var_0_0 = class("LoginScene", import("..base.BaseUI"))
local var_0_1 = 1

function var_0_0.getUIName(arg_1_0)
	return "LoginUI2"
end

function var_0_0.getBGM(arg_2_0)
	if arg_2_0.bgmName and arg_2_0.bgmName ~= "" then
		return arg_2_0.bgmName
	end

	return var_0_0.super.getBGM(arg_2_0)
end

function var_0_0.preload(arg_3_0, arg_3_1)
	arg_3_0.iconSpries = {}

	seriesAsync({
		function(arg_4_0)
			buildTempAB("ui/LoginUI2_atlas", function(arg_5_0)
				table.insert(arg_3_0.iconSpries, arg_5_0:LoadAssetSync("statu_green", typeof(Sprite), true, false))
				table.insert(arg_3_0.iconSpries, arg_5_0:LoadAssetSync("statu_gray", typeof(Sprite), true, false))
				table.insert(arg_3_0.iconSpries, arg_5_0:LoadAssetSync("statu_red", typeof(Sprite), true, false))
				table.insert(arg_3_0.iconSpries, arg_5_0:LoadAssetSync("statu_org", typeof(Sprite), true, false))
				arg_4_0()
			end)
		end,
		function(arg_6_0)
			arg_3_0.isCriBg, arg_3_0.bgPath, arg_3_0.bgmName, arg_3_0.isOpPlay, arg_3_0.opVersion = getLoginConfig()

			if arg_3_0.isCriBg then
				LoadAndInstantiateAsync("effect", arg_3_0.bgPath, function(arg_7_0)
					arg_3_0.criBgGo = arg_7_0

					arg_6_0()
				end)
			else
				LoadSpriteAsync("loadingbg/" .. arg_3_0.bgPath, function(arg_8_0)
					arg_3_0.staticBgSprite = arg_8_0

					arg_6_0()
				end)
			end
		end
	}, arg_3_1)
end

function var_0_0.init(arg_9_0)
	local var_9_0 = BundleWizard.Inst:GetGroupMgr("DEFAULT_RES")

	arg_9_0:setBg()

	arg_9_0.version = arg_9_0:findTF("version")
	arg_9_0.version:GetComponent("Text").text = "ver " .. var_9_0.CurrentVersion:ToString()
	arg_9_0.bgLay = arg_9_0:findTF("bg_lay")
	arg_9_0.accountBtn = arg_9_0:findTF("bg_lay/buttons/account_button")
	arg_9_0.repairBtn = arg_9_0:findTF("btns/repair_button")
	arg_9_0.privateBtn = arg_9_0:findTF("btns/private_btn")
	arg_9_0.licenceBtn = arg_9_0:findTF("btns/Licence_btn")
	arg_9_0.chInfo = arg_9_0:findTF("background/info")

	setActive(arg_9_0.chInfo, PLATFORM_CODE == PLATFORM_CH)

	arg_9_0.pressToLogin = GetOrAddComponent(arg_9_0:findTF("background/press_to_login"), "CanvasGroup")

	LeanTween.alphaCanvas(arg_9_0.pressToLogin, 0.25, var_0_1):setFrom(1):setEase(LeanTweenType.easeInOutSine):setLoopPingPong()

	arg_9_0.currentServer = arg_9_0:findTF("current_server")
	arg_9_0.serviceBtn = arg_9_0:findTF("bg_lay/buttons/service_button")
	arg_9_0.filingBtn = arg_9_0:findTF("filingBtn")

	setActive(arg_9_0.filingBtn, PLATFORM_CODE == PLATFORM_CH)

	arg_9_0.serversPanel = arg_9_0:findTF("servers")
	arg_9_0.servers = arg_9_0:findTF("panel/servers/content/server_list", arg_9_0.serversPanel)
	arg_9_0.serverTpl = arg_9_0:getTpl("server_tpl")
	arg_9_0.recentTF = arg_9_0:findTF("panel/servers/content/advice_panel/recent", arg_9_0.serversPanel)
	arg_9_0.adviceTF = arg_9_0:findTF("panel/servers/content/advice_panel/advice", arg_9_0.serversPanel)
	arg_9_0.userAgreenTF = arg_9_0:findTF("UserAgreement")
	arg_9_0.userAgreenMainTF = arg_9_0:findTF("UserAgreement/window")
	arg_9_0.closeUserAgreenTF = arg_9_0.userAgreenTF:Find("window/close_btn")
	arg_9_0.userAgreenConfirmTF = arg_9_0:findTF("UserAgreement/window/accept_btn")
	arg_9_0.userDisagreeConfirmTF = arg_9_0:findTF("UserAgreement/window/disagree_btn")
	arg_9_0.switchGatewayBtn = SwitchGatewayBtn.New(arg_9_0:findTF("servers/panel/switch_platform"))

	setActive(arg_9_0.userAgreenTF, false)
	pg.UIMgr.GetInstance():UnblurPanel(arg_9_0.userAgreenTF, arg_9_0._tf)

	arg_9_0.opBtn = arg_9_0:findTF("bg_lay/buttons/opBtn")

	if arg_9_0.opBtn then
		setActive(arg_9_0.opBtn, arg_9_0.isOpPlay)
	end

	arg_9_0.airiUidTxt = arg_9_0:findTF("airi_uid")
	arg_9_0.shareData = {}
	arg_9_0.searchAccount = arg_9_0:findTF("panel/searchAccount", arg_9_0.serversPanel)

	setText(findTF(arg_9_0.searchAccount, "text"), i18n("query_role_button"))

	arg_9_0.serverPanelCanvas = GetComponent(arg_9_0:findTF("servers/panel/servers"), typeof(CanvasGroup))

	onButton(arg_9_0, arg_9_0.searchAccount, function()
		if not arg_9_0.serversDic or arg_9_0.searching then
			return
		end

		arg_9_0:searchAountState(true)

		arg_9_0.serverPanelCanvas.interactable = false

		arg_9_0.event:emit(LoginMediator.ON_SEARCH_ACCOUNT, {
			callback = function()
				arg_9_0.serverPanelCanvas.interactable = true

				arg_9_0:searchAountState(false)
			end,
			update = function(arg_12_0)
				arg_9_0:setServerAccountData(arg_12_0)
			end
		})
	end, SFX_CONFIRM)

	arg_9_0.subViewList = {}
	arg_9_0.loginPanelView = LoginPanelView.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)

	arg_9_0.loginPanelView:SetShareData(arg_9_0.shareData)

	arg_9_0.registerPanelView = RegisterPanelView.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)

	arg_9_0.loginPanelView:SetShareData(arg_9_0.shareData)

	arg_9_0.tencentLoginPanelView = TencentLoginPanelView.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)

	arg_9_0.loginPanelView:SetShareData(arg_9_0.shareData)

	arg_9_0.airiLoginPanelView = AiriLoginPanelView.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)

	arg_9_0.loginPanelView:SetShareData(arg_9_0.shareData)

	arg_9_0.transcodeAlertView = TranscodeAlertView.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)

	arg_9_0.loginPanelView:SetShareData(arg_9_0.shareData)

	arg_9_0.yostarAlertView = YostarAlertView.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)

	arg_9_0.loginPanelView:SetShareData(arg_9_0.shareData)

	arg_9_0.subViewList[LoginSceneConst.DEFINE.LOGIN_PANEL_VIEW] = arg_9_0.loginPanelView
	arg_9_0.subViewList[LoginSceneConst.DEFINE.REGISTER_PANEL_VIEW] = arg_9_0.registerPanelView
	arg_9_0.subViewList[LoginSceneConst.DEFINE.TENCENT_LOGIN_VIEW] = arg_9_0.tencentLoginPanelView
	arg_9_0.subViewList[LoginSceneConst.DEFINE.AIRI_LOGIN_PANEL_VIEW] = arg_9_0.airiLoginPanelView
	arg_9_0.subViewList[LoginSceneConst.DEFINE.TRANSCODE_ALERT_VIEW] = arg_9_0.transcodeAlertView
	arg_9_0.subViewList[LoginSceneConst.DEFINE.YOSTAR_ALERT_VIEW] = arg_9_0.yostarAlertView
	arg_9_0.subViewList[LoginSceneConst.DEFINE.PRESS_TO_LOGIN] = arg_9_0.pressToLogin
	arg_9_0.subViewList[LoginSceneConst.DEFINE.BG_LAY] = arg_9_0.bgLay
	arg_9_0.subViewList[LoginSceneConst.DEFINE.SERVER_PANEL] = arg_9_0.serversPanel
	arg_9_0.subViewList[LoginSceneConst.DEFINE.ACCOUNT_BTN] = arg_9_0.accountBtn
	arg_9_0.subViewList[LoginSceneConst.DEFINE.CURRENT_SERVER] = arg_9_0.currentServer
	arg_9_0.age = arg_9_0:findTF("background/age")

	if PLATFORM_CODE == PLATFORM_CH then
		onButton(arg_9_0, arg_9_0.age, function()
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = pg.gametip.cadpa_help.tip,
				title = pg.MsgboxMgr.TITLE_CADPA
			})
		end)
		SetActive(arg_9_0.age, true)
	end

	SetActive(arg_9_0.age, PLATFORM_CODE == PLATFORM_CH)
	setText(findTF(arg_9_0.currentServer, "server_name"), "")
	arg_9_0:switchToServer()
	arg_9_0:initEvents()
end

function var_0_0.setServerAccountData(arg_14_0, arg_14_1)
	local var_14_0 = arg_14_1.id
	local var_14_1

	for iter_14_0 = 1, #arg_14_0.serversDic do
		if arg_14_0.serversDic[iter_14_0].id == var_14_0 then
			var_14_1 = arg_14_0.serversDic[iter_14_0]

			break
		end
	end

	if not var_14_1 then
		return
	end

	local var_14_2 = var_14_1.tf

	if arg_14_1 and arg_14_1.level then
		setActive(findTF(var_14_2, "mark/charactor"), true)
		setActive(findTF(var_14_2, "mark/level"), true)
		setActive(findTF(var_14_2, "mark/searching"), false)
		setText(findTF(var_14_2, "mark/level"), "lv." .. arg_14_1.level)
		setText(findTF(var_14_2, "mark/level"), setColorStr("lv." .. arg_14_1.level, "#ffffffff"))

		var_14_1.level = arg_14_1.level
	else
		setActive(findTF(var_14_2, "mark/level"), true)
		setActive(findTF(var_14_2, "mark/searching"), false)
		setActive(findTF(var_14_2, "mark/charactor"), false)

		var_14_1.level = 0

		setText(findTF(var_14_2, "mark/level"), setColorStr(i18n("query_role_none"), "#d0d0d0FF"))
	end
end

function var_0_0.searchAountState(arg_15_0, arg_15_1)
	arg_15_0.searching = arg_15_1

	for iter_15_0 = 1, #arg_15_0.serversDic do
		local var_15_0 = arg_15_0.serversDic[iter_15_0].tf
		local var_15_1 = arg_15_0.serversDic[iter_15_0].level

		setActive(findTF(var_15_0, "mark"), true)

		if arg_15_1 then
			setActive(findTF(var_15_0, "mark/charactor"), false)
			setActive(findTF(var_15_0, "mark/level"), true)
			setText(findTF(var_15_0, "mark/level"), setColorStr(i18n("query_role"), "#d0d0d0FF"))
			setActive(findTF(var_15_0, "mark/searching"), true)
		else
			if not var_15_1 then
				setText(findTF(var_15_0, "mark/level"), setColorStr(i18n("query_role_fail"), "#d0d0d0FF"))
			end

			setActive(findTF(var_15_0, "mark/searching"), false)
		end
	end
end

function var_0_0.initEvents(arg_16_0)
	arg_16_0:bind(LoginSceneConst.SWITCH_SUB_VIEW, function(arg_17_0, arg_17_1)
		arg_16_0:switchSubView(arg_17_1)
	end)
	arg_16_0:bind(LoginSceneConst.CLEAR_REGISTER_VIEW, function(arg_18_0)
		arg_16_0.registerPanelView:ActionInvoke("Clear")
	end)
end

function var_0_0.switchSubView(arg_19_0, arg_19_1)
	for iter_19_0, iter_19_1 in ipairs(arg_19_0.subViewList) do
		if isa(iter_19_1, BaseSubView) then
			if table.contains(arg_19_1, iter_19_0) then
				iter_19_1:CallbackInvoke(function()
					arg_19_0.repairBtn:SetAsLastSibling()
				end)
				iter_19_1:Load()
				iter_19_1:ActionInvoke("Show")
			else
				iter_19_1:ActionInvoke("Hide")
			end
		else
			setActive(iter_19_1, table.contains(arg_19_1, iter_19_0))
		end
	end

	if not table.contains(arg_19_1, LoginSceneConst.DEFINE.SERVER_PANEL) then
		pg.UIMgr.GetInstance():UnblurPanel(arg_19_0.serversPanel, arg_19_0._tf)
	end

	if table.contains(arg_19_1, LoginSceneConst.DEFINE.AIRI_LOGIN_PANEL_VIEW) then
		setActive(arg_19_0.airiUidTxt, false)
	end

	arg_19_0.userAgreenTF:SetAsLastSibling()
	arg_19_0.repairBtn:SetAsLastSibling()
end

function var_0_0.onBackPressed(arg_21_0)
	if arg_21_0.searching then
		return
	end

	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)

	if isActive(arg_21_0.serversPanel) then
		pg.UIMgr.GetInstance():UnblurPanel(arg_21_0.serversPanel, arg_21_0._tf)
		setActive(arg_21_0.serversPanel, false)

		return
	end

	if isActive(arg_21_0.userAgreenTF) then
		setActive(arg_21_0.userAgreenTF, false)
		pg.UIMgr.GetInstance():UnblurPanel(arg_21_0.userAgreenTF, arg_21_0._tf)

		return
	end

	pg.SdkMgr.GetInstance():OnAndoridBackPress()
end

function var_0_0.setUserData(arg_22_0, arg_22_1)
	setActive(arg_22_0.airiUidTxt, true)
	setText(arg_22_0.airiUidTxt, "uid: " .. arg_22_1.arg2)
end

function var_0_0.showUserAgreement(arg_23_0, arg_23_1)
	local var_23_0

	if PLATFORM_CODE == PLATFORM_CH then
		arg_23_0.userAgreenConfirmTF:GetComponent(typeof(Image)).color = Color.New(0.7843137254901961, 0.7843137254901961, 0.7843137254901961, 0.5019607843137255)
	else
		var_23_0 = true
	end

	local var_23_1 = require("ShareCfg.UserAgreement")

	setActive(arg_23_0.userAgreenTF, true)
	pg.UIMgr.GetInstance():BlurPanel(arg_23_0.userAgreenTF, false, {
		weight = LayerWeightConst.THIRD_LAYER
	})
	setText(arg_23_0.userAgreenTF:Find("window/container/scrollrect/content/Text"), var_23_1.content)
	onButton(arg_23_0, arg_23_0.userAgreenConfirmTF, function()
		if var_23_0 then
			setActive(arg_23_0.userAgreenTF, false)
			pg.UIMgr.GetInstance():UnblurPanel(arg_23_0.userAgreenTF, arg_23_0._tf)

			if arg_23_1 then
				arg_23_1()
			end
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("read_the_user_agreement"))
		end
	end)
	onScroll(arg_23_0, arg_23_0.userAgreenTF:Find("window/container/scrollrect"), function(arg_25_0)
		if arg_25_0.y <= 0.01 and not var_23_0 then
			var_23_0 = true

			if PLATFORM_CODE == PLATFORM_CH then
				arg_23_0.userAgreenConfirmTF:GetComponent(typeof(Image)).color = Color.New(1, 1, 1, 1)
			end
		end
	end)
end

function var_0_0.setBg(arg_26_0)
	arg_26_0.bgImg = arg_26_0:findTF("background/bg"):GetComponent(typeof(Image))

	if not arg_26_0.isCriBg then
		setImageSprite(arg_26_0.bgImg, arg_26_0.staticBgSprite)
	else
		arg_26_0.bgImg.enabled = false

		local var_26_0 = arg_26_0.criBgGo.transform

		var_26_0:SetParent(arg_26_0.bgImg.transform, false)
		var_26_0:SetAsFirstSibling()
	end
end

function var_0_0.setLastLogin(arg_27_0, arg_27_1)
	arg_27_0.shareData.lastLoginUser = arg_27_1
end

function var_0_0.setAutoLogin(arg_28_0)
	arg_28_0.shareData.autoLoginEnabled = true
end

function var_0_0.setLastLoginServer(arg_29_0, arg_29_1)
	if not arg_29_1 then
		setText(findTF(arg_29_0.currentServer, "server_name"), "")

		arg_29_0.shareData.lastLoginServer = nil

		arg_29_0:updateAdviceServer()

		return
	end

	setText(findTF(arg_29_0.currentServer, "server_name"), arg_29_1.name)

	arg_29_0.shareData.lastLoginServer = arg_29_1
end

function var_0_0.didEnter(arg_30_0)
	onButton(arg_30_0, arg_30_0.closeUserAgreenTF, function()
		if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US then
			setActive(arg_30_0.userAgreenTF, false)
			pg.UIMgr.GetInstance():UnblurPanel(arg_30_0.userAgreenTF, arg_30_0._tf)
		else
			setActive(arg_30_0.userAgreenMainTF, false)
			onNextTick(function()
				setActive(arg_30_0.userAgreenMainTF, true)
			end)
		end
	end, SFX_CANCEL)
	onButton(arg_30_0, arg_30_0.privateBtn, function()
		pg.SdkMgr.GetInstance():ShowPrivate()
	end, SFX_PANEL)
	onButton(arg_30_0, arg_30_0.licenceBtn, function()
		pg.SdkMgr.GetInstance():ShowLicence()
	end, SFX_PANEL)
	setActive(arg_30_0.privateBtn, PLATFORM_CODE == PLATFORM_CH)
	setActive(arg_30_0.licenceBtn, PLATFORM_CODE == PLATFORM_CH)

	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US then
		onButton(arg_30_0, arg_30_0.userDisagreeConfirmTF, function()
			setActive(arg_30_0.userAgreenTF, false)
			pg.UIMgr.GetInstance():UnblurPanel(arg_30_0.userAgreenTF, arg_30_0._tf)
		end)
	end

	setActive(arg_30_0.serviceBtn, PLATFORM_CODE == PLATFORM_KR)
	onButton(arg_30_0, arg_30_0.serviceBtn, function()
		if PLATFORM_CODE == PLATFORM_KR then
			pg.SdkMgr.GetInstance():UserCenter()
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("word_systemClose"))
		end
	end, SFX_MAIN)
	onButton(arg_30_0, arg_30_0.accountBtn, function()
		local var_37_0 = pg.SdkMgr.GetInstance():GetLoginType() ~= LoginType.PLATFORM_INNER

		if not var_37_0 then
			arg_30_0:switchToLogin()
		elseif var_37_0 and PLATFORM_KR == PLATFORM_CODE then
			pg.SdkMgr.GetInstance():SwitchAccount()
		end
	end, SFX_MAIN)
	onButton(arg_30_0, arg_30_0.repairBtn, function()
		pg.RepairResMgr.GetInstance():Repair()
	end)

	local function var_30_0()
		local var_39_0 = pg.SdkMgr.GetInstance():GetLoginType()

		if var_39_0 == LoginType.PLATFORM then
			pg.SdkMgr.GetInstance():LoginSdk()
		elseif var_39_0 == LoginType.PLATFORM_TENCENT then
			arg_30_0:switchToTencentLogin()
		elseif var_39_0 == LoginType.PLATFORM_INNER then
			arg_30_0:switchToLogin()
		end
	end

	onButton(arg_30_0, arg_30_0.filingBtn, function()
		Application.OpenURL("http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/gameNetTag/4028c08b58bd467b0158bd8bd80d062a")
	end, SFX_PANEL)
	onButton(arg_30_0, arg_30_0.currentServer, function()
		if table.getCount(arg_30_0.serverList or {}) == 0 then
			var_30_0()
		else
			pg.UIMgr.GetInstance():BlurPanel(arg_30_0.serversPanel)
			setActive(arg_30_0.serversPanel, true)
		end
	end, SFX_PANEL)
	onButton(arg_30_0, arg_30_0.serversPanel, function()
		pg.UIMgr.GetInstance():UnblurPanel(arg_30_0.serversPanel, arg_30_0._tf)
		setActive(arg_30_0.serversPanel, false)
	end, SFX_CANCEL)
	onButton(arg_30_0, arg_30_0:findTF("background"), function()
		if pg.CpkPlayMgr.GetInstance():OnPlaying() then
			return
		end

		if not arg_30_0.initFinished then
			return
		end

		if arg_30_0.isNeedResCheck then
			arg_30_0.event:emit(LoginMediator.CHECK_RES)

			return
		end

		if getProxy(SettingsProxy):CheckNeedUserAgreement() then
			arg_30_0.event:emit(LoginMediator.ON_LOGIN_PROCESS)

			return
		end

		if go(arg_30_0.pressToLogin).activeSelf then
			if table.getCount(arg_30_0.serverList or {}) == 0 then
				var_30_0()

				return
			end

			if not arg_30_0.shareData.lastLoginServer then
				pg.TipsMgr.GetInstance():ShowTips(i18n("login_loginScene_choiseServer"))

				return
			end

			if arg_30_0.shareData.lastLoginServer.status == Server.STATUS.VINDICATE or arg_30_0.shareData.lastLoginServer.status == Server.STATUS.FULL then
				ServerStateChecker.New():Execute(function(arg_44_0)
					if arg_44_0 then
						pg.TipsMgr.GetInstance():ShowTips(i18n("login_loginScene_server_disabled"))
					else
						arg_30_0.event:emit(LoginMediator.ON_SERVER, arg_30_0.shareData.lastLoginServer)
						pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CONFIRM)
					end
				end)

				return
			end

			arg_30_0.event:emit(LoginMediator.ON_SERVER, arg_30_0.shareData.lastLoginServer)
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CONFIRM)
		end
	end)

	if arg_30_0.isOpPlay then
		onButton(arg_30_0, arg_30_0.opBtn, function()
			if arg_30_0.initFinished and not pg.CpkPlayMgr.GetInstance():OnPlaying() then
				arg_30_0:playOpening()
			end
		end)

		if PLATFORM_CODE ~= PLATFORM_JP and PlayerPrefs.GetString("op_ver", "") ~= arg_30_0.opVersion then
			arg_30_0:playOpening(function()
				PlayerPrefs.SetString("op_ver", arg_30_0.opVersion)
				arg_30_0:playExtraVoice()

				arg_30_0.initFinished = true

				arg_30_0.event:emit(LoginMediator.ON_LOGIN_PROCESS)
			end)

			return
		end

		arg_30_0.event:emit(LoginMediator.ON_LOGIN_PROCESS)
	else
		arg_30_0.event:emit(LoginMediator.ON_LOGIN_PROCESS)
	end

	arg_30_0:playExtraVoice()

	arg_30_0.initFinished = true

	arg_30_0:InitPrivateAndLicence()
end

function var_0_0.InitPrivateAndLicence(arg_47_0)
	local var_47_0 = PLATFORM_CODE == PLATFORM_CH or IsUnityEditor

	setActive(arg_47_0.privateBtn, var_47_0)
	setActive(arg_47_0.licenceBtn, var_47_0)

	if var_47_0 then
		onButton(arg_47_0, arg_47_0.privateBtn, function()
			pg.SdkMgr.GetInstance():ShowPrivate()
		end, SFX_PANEL)
		onButton(arg_47_0, arg_47_0.licenceBtn, function()
			pg.SdkMgr.GetInstance():ShowLicence()
		end, SFX_PANEL)
	end
end

function var_0_0.playExtraVoice(arg_50_0)
	local var_50_0 = pg.gameset.login_extra_voice.description

	if var_50_0 and #var_50_0 > 0 then
		local var_50_1 = var_50_0[math.clamp(math.floor(math.random() * #var_50_0) + 1, 1, #var_50_0)]
		local var_50_2 = "cv-" .. var_50_1
		local var_50_3 = pg.CriMgr.GetInstance()

		arg_50_0.loginCueSheet = var_50_2

		var_50_3:PlayCV_V3(var_50_2, "extra")
	end
end

function var_0_0.unloadExtraVoice(arg_51_0)
	if arg_51_0.loginCueSheet then
		pg.CriMgr.GetInstance():UnloadCueSheet(arg_51_0.loginCueSheet)

		arg_51_0.loginCueSheet = nil
	end
end

function var_0_0.autoLogin(arg_52_0)
	if arg_52_0.shareData.lastLoginUser then
		if arg_52_0.shareData.autoLoginEnabled then
			arg_52_0.event:emit(LoginMediator.ON_LOGIN, arg_52_0.shareData.lastLoginUser)
		end

		if arg_52_0.loginPanelView:GetLoaded() then
			if arg_52_0.shareData.lastLoginUser.type == 1 then
				arg_52_0.loginPanelView:SetContent(arg_52_0.shareData.lastLoginUser.arg2, arg_52_0.shareData.lastLoginUser.arg3)
			elseif arg_52_0.shareData.lastLoginUser.type == 2 then
				arg_52_0.loginPanelView:SetContent(arg_52_0.shareData.lastLoginUser.arg1, arg_52_0.shareData.lastLoginUser.arg2)
			end
		end
	end
end

local var_0_2 = {
	{
		0.403921568627451,
		1,
		0.2196078431372549,
		0.6274509803921569
	},
	{
		0.6078431372549019,
		0.6078431372549019,
		0.6078431372549019,
		0.6274509803921569
	},
	{
		1,
		0.3607843137254902,
		0.2196078431372549,
		0.6274509803921569
	},
	{
		1,
		0.6588235294117647,
		0.2196078431372549,
		0.6274509803921569
	}
}

function var_0_0.updateServerTF(arg_53_0, arg_53_1, arg_53_2)
	setText(findTF(arg_53_1, "name"), "-  " .. arg_53_2.name .. "  -")
	setImageSprite(findTF(arg_53_1, "statu"), arg_53_0.iconSpries[arg_53_2.status + 1], true)

	findTF(arg_53_1, "statu_1"):GetComponent("Image").color = Color.New(var_0_2[arg_53_2.status + 1][1], var_0_2[arg_53_2.status + 1][2], var_0_2[arg_53_2.status + 1][3], var_0_2[arg_53_2.status + 1][4])

	setActive(findTF(arg_53_1, "mark"), arg_53_2.isLogined)
	setActive(arg_53_0:findTF("tag_new", arg_53_1), arg_53_2.isNew)
	setActive(arg_53_0:findTF("tag_hot", arg_53_1), arg_53_2.isHot)
	onButton(arg_53_0, arg_53_1, function()
		if arg_53_2.status == Server.STATUS.VINDICATE then
			pg.TipsMgr.GetInstance():ShowTips(i18n("login_loginScene_server_vindicate"))

			return
		end

		if arg_53_2.status == Server.STATUS.FULL then
			pg.TipsMgr.GetInstance():ShowTips(i18n("login_loginScene_server_full"))

			return
		end

		arg_53_0:setLastLoginServer(arg_53_2)
		pg.UIMgr.GetInstance():UnblurPanel(arg_53_0.serversPanel, arg_53_0._tf)
		setActive(arg_53_0.serversPanel, false)
	end, SFX_CONFIRM)
end

function var_0_0.updateAdviceServer(arg_55_0)
	if not arg_55_0.recentTF or not arg_55_0.adviceTF then
		return
	end

	setActive(arg_55_0.recentTF, arg_55_0.shareData.lastLoginServer)

	if arg_55_0.shareData.lastLoginServer then
		local var_55_0 = findTF(arg_55_0.recentTF, "server")

		arg_55_0:updateServerTF(var_55_0, arg_55_0.shareData.lastLoginServer)
	end

	local var_55_1 = getProxy(ServerProxy).firstServer

	setActive(arg_55_0.adviceTF, var_55_1)

	if var_55_1 then
		local var_55_2 = findTF(arg_55_0.adviceTF, "server")

		arg_55_0:updateServerTF(var_55_2, var_55_1)
	end
end

function var_0_0.updateServerList(arg_56_0, arg_56_1)
	arg_56_0.serverList = arg_56_1

	local var_56_0 = _.sort(_.values(arg_56_1), function(arg_57_0, arg_57_1)
		return arg_57_0.sortIndex < arg_57_1.sortIndex
	end)

	removeAllChildren(arg_56_0.servers)

	if IsUnityEditor then
		table.sort(var_56_0, function(arg_58_0, arg_58_1)
			local var_58_0 = string.lower(arg_58_0.name)
			local var_58_1 = string.lower(arg_58_1.name)

			return string.byte(var_58_0, 1) > string.byte(var_58_1, 1)
		end)
	end

	arg_56_0.serversDic = {}

	for iter_56_0, iter_56_1 in pairs(var_56_0) do
		local var_56_1 = cloneTplTo(arg_56_0.serverTpl, arg_56_0.servers)

		arg_56_0:updateServerTF(var_56_1, iter_56_1)
		table.insert(arg_56_0.serversDic, {
			server = iter_56_1,
			tf = var_56_1,
			id = iter_56_1.id
		})
	end
end

function var_0_0.fillterRefundServer(arg_59_0)
	local var_59_0 = getProxy(UserProxy)
	local var_59_1 = {}

	if var_59_0.data.limitServerIds and #var_59_0.data.limitServerIds > 0 and arg_59_0.serverList and #arg_59_0.serverList > 0 then
		local var_59_2 = var_59_0.data.limitServerIds
		local var_59_3

		for iter_59_0, iter_59_1 in pairs(arg_59_0.serverList) do
			local var_59_4 = iter_59_1.id
			local var_59_5 = false

			for iter_59_2, iter_59_3 in pairs(var_59_2) do
				if var_59_2[iter_59_2] == var_59_4 and not var_59_5 then
					if not var_59_3 then
						var_59_3 = "\n" .. iter_59_1.name
					else
						var_59_3 = var_59_3 .. "," .. iter_59_1.name
					end

					table.insert(var_59_1, iter_59_1)

					var_59_5 = true
				end
			end
		end

		arg_59_0:updateServerList(var_59_1)
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			modal = true,
			hideNo = true,
			hideClose = true,
			content = i18n("login_arrears_tips", var_59_3),
			onYes = function()
				return
			end
		})
	end
end

function var_0_0.switchToTencentLogin(arg_61_0)
	arg_61_0:switchSubView({
		LoginSceneConst.DEFINE.TENCENT_LOGIN_VIEW
	})
end

function var_0_0.switchToAiriLogin(arg_62_0)
	arg_62_0:switchSubView({
		LoginSceneConst.DEFINE.AIRI_LOGIN_PANEL_VIEW,
		LoginSceneConst.DEFINE.PRESS_TO_LOGIN
	})
end

function var_0_0.switchToLogin(arg_63_0)
	arg_63_0:switchSubView({
		LoginSceneConst.DEFINE.LOGIN_PANEL_VIEW
	})
end

function var_0_0.switchToRegister(arg_64_0)
	arg_64_0:switchSubView({
		LoginSceneConst.DEFINE.REGISTER_PANEL_VIEW
	})
end

function var_0_0.switchToServer(arg_65_0)
	arg_65_0:updateAdviceServer()

	if pg.SdkMgr.GetInstance():GetLoginType() ~= LoginType.PLATFORM_INNER and PLATFORM_CODE ~= PLATFORM_KR then
		arg_65_0:switchSubView({
			LoginSceneConst.DEFINE.PRESS_TO_LOGIN,
			LoginSceneConst.DEFINE.CURRENT_SERVER,
			LoginSceneConst.DEFINE.BG_LAY
		})
	else
		arg_65_0:switchSubView({
			LoginSceneConst.DEFINE.ACCOUNT_BTN,
			LoginSceneConst.DEFINE.PRESS_TO_LOGIN,
			LoginSceneConst.DEFINE.CURRENT_SERVER,
			LoginSceneConst.DEFINE.BG_LAY
		})
	end
end

function var_0_0.SwitchToWaitPanel(arg_66_0, arg_66_1)
	local var_66_0 = arg_66_0:findTF("Msgbox")
	local var_66_1 = arg_66_0:findTF("window/content", var_66_0)

	arg_66_0.waitTimer = nil

	local var_66_2 = 0
	local var_66_3 = arg_66_1

	arg_66_0.waitTimer = Timer.New(function()
		setText(var_66_1, i18n("login_wait_tip", var_66_3))

		arg_66_1 = arg_66_1 - 1

		if math.random(0, 1) == 1 then
			var_66_3 = arg_66_1
		end

		if arg_66_1 <= 0 then
			triggerButton(arg_66_0:findTF("background"))
			arg_66_0.waitTimer:Stop()

			arg_66_0.waitTimer = nil
		end
	end, 1, -1)

	arg_66_0.waitTimer:Start()
	arg_66_0.waitTimer.func()
	setActive(var_66_0, true)
end

function var_0_0.willExit(arg_68_0)
	if arg_68_0.waitTimer then
		arg_68_0.waitTimer:Stop()

		arg_68_0.waitTimer = nil
	end

	pg.CpkPlayMgr.GetInstance():DisposeCpkMovie()
	arg_68_0.loginPanelView:Destroy()
	arg_68_0.registerPanelView:Destroy()
	arg_68_0.tencentLoginPanelView:Destroy()
	arg_68_0.airiLoginPanelView:Destroy()
	arg_68_0.transcodeAlertView:Destroy()
	arg_68_0.yostarAlertView:Destroy()
	arg_68_0.switchGatewayBtn:Dispose()
end

function var_0_0.playOpening(arg_69_0, arg_69_1)
	pg.CpkPlayMgr.GetInstance():PlayCpkMovie(function()
		if not arg_69_0.cg then
			arg_69_0.cg = GetOrAddComponent(arg_69_0._tf, "CanvasGroup")
		end

		arg_69_0.cg.alpha = 0
	end, function()
		arg_69_0.cg.alpha = 1

		if arg_69_1 then
			arg_69_1()
		end
	end, "ui", "opening", true, false, nil)

	arg_69_0.onPlayingOP = true
end

function var_0_0.closeYostarAlertView(arg_72_0)
	if arg_72_0.yostarAlertView and arg_72_0.yostarAlertView:CheckState(BaseSubView.STATES.INITED) then
		arg_72_0.yostarAlertView:Destroy()
	end
end

function var_0_0.onLoadDataDone(arg_73_0)
	arg_73_0:unloadExtraVoice()

	if getProxy(PlayerProxy) then
		getProxy(PlayerProxy):setFlag("login", true)
		pg.m02:sendNotification(GAME.GO_SCENE, SCENE.MAINUI, {
			isFromLogin = true
		})
	end
end

return var_0_0
