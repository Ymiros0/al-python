local var_0_0 = class("SettingsAccountUSPanle", import(".SettingsBasePanel"))

def var_0_0.GetUIName(arg_1_0):
	return "SettingsAccountUS"

def var_0_0.GetTitle(arg_2_0):
	return "Account"

def var_0_0.GetTitleEn(arg_3_0):
	return "  / ACCOUNT"

def var_0_0.OnInit(arg_4_0):
	local var_4_0 = arg_4_0._tf
	local var_4_1 = findTF(var_4_0, "page1")
	local var_4_2 = findTF(var_4_1, "btn_layout/twitter_con")

	arg_4_0.btnBindTwitter = findTF(var_4_2, "bind_twitter")
	arg_4_0.btnUnlinkTwitter = findTF(var_4_2, "unlink_twitter")
	arg_4_0.twitterStatus = findTF(var_4_2, "twitter_status")

	local var_4_3 = findTF(var_4_1, "btn_layout/facebook_con")

	arg_4_0.btnBindFacebook = findTF(var_4_3, "bind_facebook")
	arg_4_0.btnUnlinkFacebook = findTF(var_4_3, "unlink_facebook")
	arg_4_0.facebookStatus = findTF(var_4_3, "facebook_status")

	setActive(var_4_3, PLATFORM_CODE == PLATFORM_US and pg.SdkMgr.GetInstance().GetChannelUID() != "3")

	local var_4_4 = findTF(var_4_1, "btn_layout/yostar_con")

	arg_4_0.btnBindYostar = findTF(var_4_4, "bind_yostar")
	arg_4_0.btnUnlinkYostar = findTF(var_4_4, "unlink_yostar")
	arg_4_0.yostarStatus = findTF(var_4_4, "yostar_status")

	local var_4_5 = findTF(var_4_1, "btn_layout/apple_con")

	arg_4_0.btnBindApple = findTF(var_4_5, "bind_apple")
	arg_4_0.btnUnlinkApple = findTF(var_4_5, "unlink_apple")
	arg_4_0.appleStatus = findTF(var_4_5, "apple_status")

	setActive(var_4_5, PLATFORM_CODE == PLATFORM_US and pg.SdkMgr.GetInstance().GetChannelUID() == "1")

	local var_4_6 = findTF(var_4_1, "btn_layout/amazon_con")

	arg_4_0.btnBindAmazon = findTF(var_4_6, "bind_amazon")
	arg_4_0.btnUnlinkAmazon = findTF(var_4_6, "unlink_amazon")
	arg_4_0.amazonStatus = findTF(var_4_6, "amazon_status")

	setActive(var_4_6, PLATFORM_CODE == PLATFORM_US and pg.SdkMgr.GetInstance().GetChannelUID() == "3")

	arg_4_0.pgsCon = findTF(var_4_1, "btn_layout/pgs_con")
	arg_4_0.btnBindPGS = findTF(arg_4_0.pgsCon, "bind")
	arg_4_0.btnUnlinkPGS = findTF(arg_4_0.pgsCon, "unlink")
	arg_4_0.pgsStatus = findTF(arg_4_0.pgsCon, "status")
	arg_4_0.yostarAlert = findTF(var_4_0, "page2")
	arg_4_0.yostarEmailTxt = findTF(arg_4_0.yostarAlert, "email_input_txt")
	arg_4_0.yostarCodeTxt = findTF(arg_4_0.yostarAlert, "code_input_txt")
	arg_4_0.yostarGenCodeBtn = findTF(arg_4_0.yostarAlert, "gen_code_btn")
	arg_4_0.yostarGenTxt = findTF(arg_4_0.yostarGenCodeBtn, "Text")
	arg_4_0.yostarSureBtn = findTF(arg_4_0.yostarAlert, "login_btn")

	arg_4_0.RegisterEvent()

def var_0_0.RegisterEvent(arg_5_0):
	onButton(arg_5_0, arg_5_0.btnBindTwitter, function()
		pg.SdkMgr.GetInstance().LinkSocial(AIRI_PLATFORM_TWITTER))
	onButton(arg_5_0, arg_5_0.btnUnlinkTwitter, function()
		pg.SdkMgr.GetInstance().UnlinkSocial(AIRI_PLATFORM_TWITTER))
	onButton(arg_5_0, arg_5_0.btnBindFacebook, function()
		pg.SdkMgr.GetInstance().LinkSocial(AIRI_PLATFORM_FACEBOOK))
	onButton(arg_5_0, arg_5_0.btnUnlinkFacebook, function()
		pg.SdkMgr.GetInstance().UnlinkSocial(AIRI_PLATFORM_FACEBOOK))
	onButton(arg_5_0, arg_5_0.btnBindApple, function()
		pg.SdkMgr.GetInstance().LinkSocial(AIRI_PLATFORM_APPLE))
	onButton(arg_5_0, arg_5_0.btnUnlinkApple, function()
		pg.SdkMgr.GetInstance().UnlinkSocial(AIRI_PLATFORM_APPLE))
	onButton(arg_5_0, arg_5_0.btnBindAmazon, function()
		pg.SdkMgr.GetInstance().LinkSocial(AIRI_PLATFORM_AMAZON))
	onButton(arg_5_0, arg_5_0.btnUnlinkAmazon, function()
		pg.SdkMgr.GetInstance().UnlinkSocial(AIRI_PLATFORM_AMAZON))
	onButton(arg_5_0, arg_5_0.btnBindYostar, function()
		pg.UIMgr.GetInstance().BlurPanel(arg_5_0.yostarAlert, False)
		setActive(arg_5_0.yostarAlert, True))
	onButton(arg_5_0, arg_5_0.yostarAlert, function()
		pg.UIMgr.GetInstance().UnblurPanel(arg_5_0.yostarAlert, arg_5_0.accountUS)
		setActive(arg_5_0.yostarAlert, False))
	onButton(arg_5_0, arg_5_0.yostarGenCodeBtn, function()
		local var_16_0 = getInputText(arg_5_0.yostarEmailTxt)

		if var_16_0 != "":
			pg.SdkMgr.GetInstance().VerificationCodeReq(var_16_0)
			arg_5_0.checkAiriGenCodeCounter_US()
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("verification_code_req_tip1")))
	onButton(arg_5_0, arg_5_0.yostarSureBtn, function()
		local var_17_0 = getInputText(arg_5_0.yostarEmailTxt)
		local var_17_1 = getInputText(arg_5_0.yostarCodeTxt)

		if var_17_0 != "" and var_17_1 != "":
			pg.UIMgr.GetInstance().LoadingOn()
			pg.SdkMgr.GetInstance().LinkSocial(AIRI_PLATFORM_YOSTAR, var_17_0, var_17_1)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("verification_code_req_tip3"))

		triggerButton(arg_5_0.yostarAlert))
	onButton(arg_5_0, arg_5_0.btnUnlinkPGS, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("pgs_unbind_tip1"),
			def onYes:()
				pg.SdkMgr.GetInstance().UnlinkSocial(AIRI_PLATFORM_GPS)
		}))

def var_0_0.OnUpdate(arg_20_0):
	arg_20_0.checkAllAccountState_US()
	arg_20_0.checkAiriGenCodeCounter_US()

def var_0_0.checkAllAccountState_US(arg_21_0):
	arg_21_0.checkAccountTwitterView_US()
	arg_21_0.checkAccountFacebookView_US()
	arg_21_0.checkAccountAppleView_US()
	arg_21_0.checkAccountYostarView_US()
	arg_21_0.checkAccountAmazonView_US()
	arg_21_0.checkAccountPGSView_US()

def var_0_0.checkAccountTwitterView_US(arg_22_0):
	local var_22_0 = pg.SdkMgr.GetInstance().IsSocialLink(AIRI_PLATFORM_TWITTER)

	setActive(arg_22_0.btnUnlinkTwitter, var_22_0)
	setActive(arg_22_0.twitterStatus, var_22_0)
	setActive(arg_22_0.btnBindTwitter, not var_22_0)

	if var_22_0:
		setText(arg_22_0.twitterStatus, i18n("twitter_link_title", pg.SdkMgr.GetInstance().GetSocialName(AIRI_PLATFORM_TWITTER)))

def var_0_0.checkAccountFacebookView_US(arg_23_0):
	if PLATFORM_CODE == PLATFORM_US and pg.SdkMgr.GetInstance().GetChannelUID() != "3":
		local var_23_0 = pg.SdkMgr.GetInstance().IsSocialLink(AIRI_PLATFORM_FACEBOOK)

		setActive(arg_23_0.btnUnlinkFacebook, var_23_0)
		setActive(arg_23_0.facebookStatus, var_23_0)
		setActive(arg_23_0.btnBindFacebook, not var_23_0)

		if var_23_0:
			setText(arg_23_0.facebookStatus, i18n("facebook_link_title", pg.SdkMgr.GetInstance().GetSocialName(AIRI_PLATFORM_FACEBOOK)))

def var_0_0.checkAccountAppleView_US(arg_24_0):
	local var_24_0 = pg.SdkMgr.GetInstance().IsSocialLink(AIRI_PLATFORM_APPLE)

	setActive(arg_24_0.btnUnlinkApple, var_24_0)
	setActive(arg_24_0.appleStatus, var_24_0)
	setActive(arg_24_0.btnBindApple, not var_24_0)

	if var_24_0:
		setText(arg_24_0.appleStatus, i18n("apple_link_title", pg.SdkMgr.GetInstance().GetSocialName(AIRI_PLATFORM_APPLE)))

def var_0_0.checkAccountAmazonView_US(arg_25_0):
	if pg.SdkMgr.GetInstance().GetChannelUID() == "3":
		local var_25_0 = pg.SdkMgr.GetInstance().IsSocialLink(AIRI_PLATFORM_AMAZON)

		setActive(arg_25_0.btnUnlinkAmazon, var_25_0)
		setActive(arg_25_0.amazonStatus, var_25_0)
		setActive(arg_25_0.btnBindAmazon, not var_25_0)

		if var_25_0:
			setText(arg_25_0.amazonStatus, i18n("amazon_link_title", pg.SdkMgr.GetInstance().GetSocialName(AIRI_PLATFORM_AMAZON)))

def var_0_0.checkAccountYostarView_US(arg_26_0):
	local var_26_0 = pg.SdkMgr.GetInstance().IsSocialLink(AIRI_PLATFORM_YOSTAR)

	setActive(arg_26_0.btnUnlinkYostar, var_26_0)
	setActive(arg_26_0.yostarStatus, var_26_0)
	setActive(arg_26_0.btnBindYostar, not var_26_0)

	if var_26_0:
		setText(arg_26_0.yostarStatus, i18n("yostar_link_title", pg.SdkMgr.GetInstance().GetSocialName(AIRI_PLATFORM_YOSTAR)))

def var_0_0.checkAccountPGSView_US(arg_27_0):
	local var_27_0 = pg.SdkMgr.GetInstance().IsSocialLink(AIRI_PLATFORM_GPS)

	setActive(arg_27_0.pgsCon, var_27_0)
	setActive(arg_27_0.btnUnlinkPGS, var_27_0)
	setActive(arg_27_0.pgsStatus, var_27_0)
	setActive(arg_27_0.btnBindPGS, False)

	if var_27_0:
		setText(arg_27_0.pgsStatus, i18n("pgs_binding_account", pg.SdkMgr.GetInstance().GetSocialName(AIRI_PLATFORM_GPS)))

def var_0_0.checkAiriGenCodeCounter_US(arg_28_0):
	if GetAiriGenCodeTimeRemain() > 0:
		setButtonEnabled(arg_28_0.yostarGenCodeBtn, False)

		arg_28_0.genCodeTimer = Timer.New(function()
			local var_29_0 = GetAiriGenCodeTimeRemain()

			if var_29_0 > 0:
				setText(arg_28_0.yostarGenTxt, "(" .. var_29_0 .. ")")
			else
				setText(arg_28_0.yostarGenTxt, "Generate")
				arg_28_0.clearAiriGenCodeTimer_US(), 1, -1)

		arg_28_0.genCodeTimer.Start()

def var_0_0.clearAiriGenCodeTimer_US(arg_30_0):
	setButtonEnabled(arg_30_0.yostarGenCodeBtn, True)

	if arg_30_0.genCodeTimer:
		arg_30_0.genCodeTimer.Stop()

		arg_30_0.genCodeTimer = None

def var_0_0.Dispose(arg_31_0):
	var_0_0.super.Dispose(arg_31_0)

	if arg_31_0.genCodeTimer:
		arg_31_0.genCodeTimer.Stop()

		arg_31_0.genCodeTimer = None

return var_0_0
