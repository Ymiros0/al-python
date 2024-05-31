local var_0_0 = class("YostarAlertView", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "YostarAlertView"

def var_0_0.OnLoaded(arg_2_0):
	return

def var_0_0.SetShareData(arg_3_0, arg_3_1):
	arg_3_0.shareData = arg_3_1

def var_0_0.OnInit(arg_4_0):
	arg_4_0.yostarAlert = arg_4_0._tf
	arg_4_0.yostarEmailTxt = arg_4_0.findTF("email_input_txt", arg_4_0.yostarAlert)
	arg_4_0.yostarCodeTxt = arg_4_0.findTF("code_input_txt", arg_4_0.yostarAlert)
	arg_4_0.yostarGenCodeBtn = arg_4_0.findTF("gen_code_btn", arg_4_0.yostarAlert)
	arg_4_0.yostarGenTxt = arg_4_0.findTF("Text", arg_4_0.yostarGenCodeBtn)
	arg_4_0.yostarSureBtn = arg_4_0.findTF("login_btn", arg_4_0.yostarAlert)
	arg_4_0.email_text = arg_4_0.findTF("title1", arg_4_0.yostarAlert)
	arg_4_0.emailhold_text = arg_4_0.findTF("Placeholder", arg_4_0.yostarEmailTxt)
	arg_4_0.code_text = arg_4_0.findTF("title2", arg_4_0.yostarAlert)
	arg_4_0.codehold_text = arg_4_0.findTF("Placeholder", arg_4_0.yostarCodeTxt)
	arg_4_0.genBtn_text = arg_4_0.findTF("Text", arg_4_0.yostarGenCodeBtn)
	arg_4_0.desc_text = arg_4_0.findTF("desc", arg_4_0.yostarAlert)
	arg_4_0.loginBtn_text = arg_4_0.findTF("Image", arg_4_0.yostarSureBtn)

	setText(arg_4_0.email_text, i18n("email_text"))
	setText(arg_4_0.emailhold_text, i18n("emailhold_text"))
	setText(arg_4_0.code_text, i18n("code_text"))
	setText(arg_4_0.codehold_text, i18n("codehold_text"))
	setText(arg_4_0.genBtn_text, i18n("genBtn_text"))
	setText(arg_4_0.desc_text, i18n("desc_text"))
	setText(arg_4_0.loginBtn_text, arg_4_0.contextData.isLinkMode == True and i18n("linkBtn_text") or i18n("loginBtn_text"))
	arg_4_0.InitEvent()

def var_0_0.InitEvent(arg_5_0):
	onButton(arg_5_0, arg_5_0.yostarAlert, function()
		setActive(arg_5_0.yostarAlert, False)

		if arg_5_0.contextData.isDestroyOnClose == True:
			arg_5_0.Destroy())
	onButton(arg_5_0, arg_5_0.yostarGenCodeBtn, function()
		local var_7_0 = getInputText(arg_5_0.yostarEmailTxt)

		if var_7_0 != "":
			pg.SdkMgr.GetInstance().VerificationCodeReq(var_7_0)
			arg_5_0.CheckAiriGenCodeCounter()
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("verification_code_req_tip1")))
	onButton(arg_5_0, arg_5_0.yostarSureBtn, function()
		local var_8_0 = getInputText(arg_5_0.yostarEmailTxt)
		local var_8_1 = getInputText(arg_5_0.yostarCodeTxt)

		if var_8_0 != "" and var_8_1 != "":
			if arg_5_0.contextData.isLinkMode == True:
				pg.SdkMgr.GetInstance().LinkSocial(AIRI_PLATFORM_YOSTAR, var_8_0, var_8_1)
			else
				pg.SdkMgr.GetInstance().LoginWithSocial(AIRI_PLATFORM_YOSTAR, var_8_0, var_8_1)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("verification_code_req_tip3")))
	arg_5_0.CheckAiriGenCodeCounter()

def var_0_0.CheckAiriGenCodeCounter(arg_9_0):
	if GetAiriGenCodeTimeRemain() > 0:
		setButtonEnabled(arg_9_0.yostarGenCodeBtn, False)

		if arg_9_0.genCodeTimer:
			arg_9_0.genCodeTimer.Stop()

		arg_9_0.genCodeTimer = Timer.New(function()
			local var_10_0 = GetAiriGenCodeTimeRemain()

			if var_10_0 > 0:
				setText(arg_9_0.yostarGenTxt, "(" .. var_10_0 .. ")")
			else
				setText(arg_9_0.yostarGenTxt, i18n("genBtn_text"))
				arg_9_0.ClearAiriGenCodeTimer(), 1, -1)

		arg_9_0.genCodeTimer.Start()

def var_0_0.ClearAiriGenCodeTimer(arg_11_0):
	setButtonEnabled(arg_11_0.yostarGenCodeBtn, True)

	if arg_11_0.genCodeTimer:
		arg_11_0.genCodeTimer.Stop()

		arg_11_0.genCodeTimer = None

def var_0_0.OnDestroy(arg_12_0):
	arg_12_0.ClearAiriGenCodeTimer()

return var_0_0
