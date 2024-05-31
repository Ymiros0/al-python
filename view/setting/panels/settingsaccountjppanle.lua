local var_0_0 = class("SettingsAccountJPPanle", import(".SettingsBasePanel"))

function var_0_0.GetUIName(arg_1_0)
	return "SettingsAccountJP"
end

function var_0_0.GetTitle(arg_2_0)
	return i18n("Settings_title_LoginJP")
end

function var_0_0.GetTitleEn(arg_3_0)
	return "  / ACCOUNT"
end

function var_0_0.OnInit(arg_4_0)
	arg_4_0.userProxy = getProxy(UserProxy)

	local var_4_0 = arg_4_0._tf

	arg_4_0.accountTwitterUI = findTF(var_4_0, "page1")

	local var_4_1 = findTF(arg_4_0.accountTwitterUI, "btn_layout/account_con")

	arg_4_0.goTranscodeUIBtn = findTF(var_4_1, "bind_account")

	local var_4_2 = findTF(arg_4_0.accountTwitterUI, "btn_layout/twitter_con")

	arg_4_0.twitterBtn = findTF(var_4_2, "bind_twitter")
	arg_4_0.twitterUnlinkBtn = findTF(var_4_2, "unlink_twitter")
	arg_4_0.twitterLinkSign = findTF(var_4_2, "twitter_status")

	local var_4_3 = findTF(arg_4_0.accountTwitterUI, "btn_layout/apple_con")

	arg_4_0.appleBtn = findTF(var_4_3, "bind_apple")
	arg_4_0.appleUnlinkBtn = findTF(var_4_3, "unlink_apple")
	arg_4_0.appleLinkSign = findTF(var_4_3, "apple_status")

	setActive(var_4_3, PLATFORM_CODE == PLATFORM_JP and pg.SdkMgr.GetInstance():GetChannelUID() == "1")

	local var_4_4 = findTF(arg_4_0.accountTwitterUI, "btn_layout/amazon_con")

	arg_4_0.amazonBtn = findTF(var_4_4, "bind_amazon")
	arg_4_0.amazonUnlinkBtn = findTF(var_4_4, "unlink_amazon")
	arg_4_0.amazonLinkSign = findTF(var_4_4, "amazon_status")

	setButtonEnabled(arg_4_0.amazonUnlinkBtn, false)
	setText(findTF(arg_4_0.amazonUnlinkBtn, "Text"), i18n("amazon_unlink_btn_text"))
	setActive(var_4_4, PLATFORM_CODE == PLATFORM_JP and pg.SdkMgr.GetInstance():GetChannelUID() == "3")

	local var_4_5 = findTF(arg_4_0.accountTwitterUI, "btn_layout/yostar_con")

	arg_4_0.yostarBtn = findTF(var_4_5, "bind_yostar")
	arg_4_0.yostarUnlinkBtn = findTF(var_4_5, "unlink_yostar")
	arg_4_0.yostarLinkSign = findTF(var_4_5, "yostar_status")

	setButtonEnabled(arg_4_0.yostarUnlinkBtn, false)
	setText(findTF(arg_4_0.yostarUnlinkBtn, "Text"), i18n("yostar_unlink_btn_text"))

	arg_4_0.pgsCon = findTF(arg_4_0.accountTwitterUI, "btn_layout/pgs_con")
	arg_4_0.pgsBtn = findTF(arg_4_0.pgsCon, "bind")
	arg_4_0.pgsUnlinkBtn = findTF(arg_4_0.pgsCon, "unlink")
	arg_4_0.pgsLinkSign = findTF(arg_4_0.pgsCon, "status")

	setText(findTF(arg_4_0.pgsUnlinkBtn, "Text"), i18n("pgs_unbind"))

	arg_4_0.transcodeUI = findTF(var_4_0, "page2")
	arg_4_0.uidTxt = findTF(arg_4_0.transcodeUI, "account_name/Text")
	arg_4_0.transcodeTxt = findTF(arg_4_0.transcodeUI, "password/Text")
	arg_4_0.getCodeBtn = findTF(arg_4_0.transcodeUI, "publish_transcode")
	arg_4_0.codeDesc = findTF(arg_4_0.transcodeUI, "title_desc")

	arg_4_0:OnRegisterEvent()
end

function var_0_0.OnRegisterEvent(arg_5_0)
	onButton(arg_5_0, arg_5_0.getCodeBtn, function()
		if arg_5_0.transcode == "" then
			local function var_6_0()
				pg.SdkMgr.GetInstance():TranscodeRequest()
			end

			local var_6_1 = pg.SecondaryPWDMgr

			var_6_1:LimitedOperation(var_6_1.CREATE_INHERIT, nil, var_6_0)
		end
	end)
	onButton(arg_5_0, arg_5_0.twitterBtn, function()
		pg.SdkMgr.GetInstance():LinkSocial(AIRI_PLATFORM_TWITTER)
	end)
	onButton(arg_5_0, arg_5_0.twitterUnlinkBtn, function()
		pg.SdkMgr.GetInstance():UnlinkSocial(AIRI_PLATFORM_TWITTER)
	end)
	onButton(arg_5_0, arg_5_0.appleBtn, function()
		pg.SdkMgr.GetInstance():LinkSocial(AIRI_PLATFORM_APPLE)
	end)
	onButton(arg_5_0, arg_5_0.appleUnlinkBtn, function()
		pg.SdkMgr.GetInstance():UnlinkSocial(AIRI_PLATFORM_APPLE)
	end)
	onButton(arg_5_0, arg_5_0.goTranscodeUIBtn, function()
		setActive(arg_5_0.accountTwitterUI, false)
		setActive(arg_5_0.transcodeUI, true)
	end)
	onButton(arg_5_0, arg_5_0.amazonBtn, function()
		pg.SdkMgr.GetInstance():LinkSocial(AIRI_PLATFORM_AMAZON)
	end)
	onButton(arg_5_0, arg_5_0.yostarBtn, function()
		pg.m02:sendNotification(NewSettingsMediator.OPEN_YOSTAR_ALERT_VIEW)
	end)
	onButton(arg_5_0, arg_5_0.pgsUnlinkBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("pgs_unbind_tip1"),
			onYes = function()
				pg.SdkMgr.GetInstance():UnlinkSocial(AIRI_PLATFORM_GPS)
			end
		})
	end)
end

function var_0_0.OnUpdate(arg_17_0)
	arg_17_0:checkAllAccountState()
end

function var_0_0.checkAllAccountState(arg_18_0)
	arg_18_0:checkTranscodeView()
	arg_18_0:checkAccountTwitterView()
	arg_18_0:checkAccountAppleView()
	arg_18_0:checkAccountAmazonView()
	arg_18_0:checkAccountYostarView()
	arg_18_0:checkAccountGPSView()
end

function var_0_0.showTranscode(arg_19_0, arg_19_1)
	arg_19_0.userProxy:saveTranscode(arg_19_1)
	arg_19_0:checkTranscodeView()
end

function var_0_0.checkTranscodeView(arg_20_0)
	arg_20_0.transcode = pg.SdkMgr.GetInstance():GetYostarTransCode() or ""

	if not arg_20_0.transcode or arg_20_0.transcode == "" or arg_20_0.transcode == "NULL" then
		arg_20_0.transcode = arg_20_0.userProxy:getTranscode()
	end

	setActive(arg_20_0.codeDesc, arg_20_0.transcode ~= "")
	setActive(arg_20_0.getCodeBtn, arg_20_0.transcode == "")

	if arg_20_0.transcode ~= "" then
		setText(arg_20_0.uidTxt, pg.SdkMgr.GetInstance():GetYostarUid())
		setText(arg_20_0.transcodeTxt, arg_20_0.transcode)
	end
end

function var_0_0.checkAccountTwitterView(arg_21_0)
	local var_21_0 = pg.SdkMgr.GetInstance():IsSocialLink(AIRI_PLATFORM_TWITTER)

	setActive(arg_21_0.twitterUnlinkBtn, var_21_0)
	setActive(arg_21_0.twitterLinkSign, var_21_0)
	setActive(arg_21_0.twitterBtn, not var_21_0)

	if var_21_0 then
		setText(arg_21_0.twitterLinkSign, i18n("twitter_link_title", pg.SdkMgr.GetInstance():GetSocialName(AIRI_PLATFORM_TWITTER)))
	end
end

function var_0_0.checkAccountAppleView(arg_22_0)
	local var_22_0 = pg.SdkMgr.GetInstance():IsSocialLink(AIRI_PLATFORM_APPLE)

	setActive(arg_22_0.appleUnlinkBtn, var_22_0)
	setActive(arg_22_0.appleLinkSign, var_22_0)
	setActive(arg_22_0.appleBtn, not var_22_0)

	if var_22_0 then
		setText(arg_22_0.appleLinkSign, i18n("apple_link_title", pg.SdkMgr.GetInstance():GetSocialName(AIRI_PLATFORM_APPLE)))
	end
end

function var_0_0.checkAccountAmazonView(arg_23_0)
	if pg.SdkMgr.GetInstance():GetChannelUID() == "3" then
		local var_23_0 = pg.SdkMgr.GetInstance():IsSocialLink(AIRI_PLATFORM_AMAZON)

		setActive(arg_23_0.amazonUnlinkBtn, var_23_0)
		setActive(arg_23_0.amazonLinkSign, var_23_0)
		setActive(arg_23_0.amazonBtn, not var_23_0)

		if var_23_0 then
			setText(arg_23_0.amazonLinkSign, i18n("amazon_link_title", pg.SdkMgr.GetInstance():GetSocialName(AIRI_PLATFORM_AMAZON)))
		end
	end
end

function var_0_0.checkAccountYostarView(arg_24_0)
	local var_24_0 = pg.SdkMgr.GetInstance():IsSocialLink(AIRI_PLATFORM_YOSTAR)

	setActive(arg_24_0.yostarUnlinkBtn, var_24_0)
	setActive(arg_24_0.yostarLinkSign, var_24_0)
	setActive(arg_24_0.yostarBtn, not var_24_0)

	if var_24_0 then
		setText(arg_24_0.yostarLinkSign, i18n("yostar_link_title"))
	end
end

function var_0_0.checkAccountGPSView(arg_25_0)
	local var_25_0 = pg.SdkMgr.GetInstance():IsSocialLink(AIRI_PLATFORM_GPS)

	setActive(arg_25_0.pgsCon, var_25_0)
	setActive(arg_25_0.pgsUnlinkBtn, var_25_0)
	setActive(arg_25_0.pgsLinkSign, var_25_0)
	setActive(arg_25_0.pgsBtn, false)

	if var_25_0 then
		setText(arg_25_0.pgsLinkSign, i18n("pgs_binding_account", pg.SdkMgr.GetInstance():GetSocialName(AIRI_PLATFORM_GPS)))
	end
end

return var_0_0
