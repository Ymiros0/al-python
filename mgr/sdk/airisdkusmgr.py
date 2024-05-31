local var_0_0 = {}
local var_0_1 = AiriUSSdkMgr.inst
local var_0_2 = AiriUSSdkMgr.AiriSDKInst
local var_0_3 = AiriUSSdkMgr.AiriSdkDataInst

AIRI_PLATFORM_FACEBOOK = "facebook"
AIRI_PLATFORM_TWITTER = "twitter"
AIRI_PLATFORM_YOSTAR = "yostar"
AIRI_PLATFORM_APPLE = "apple"
AIRI_PLATFORM_AMAZON = "amazon"
AIRI_PLATFORM_GPS = "gps"
AIRI_SDK_INITED = False
var_0_0.OnAiriBuying = -1
var_0_0.BuyingLimit = 60

def var_0_0.CheckAudit():
	return NetConst.GATEWAY_PORT == 20001 and NetConst.GATEWAY_HOST == "audit.us.yo-star.com"

def var_0_0.CheckPreAudit():
	return NetConst.GATEWAY_PORT == 30001 and NetConst.GATEWAY_HOST == "audit.us.yo-star.com"

def var_0_0.CheckPretest():
	return IsUnityEditor or var_0_0.CheckPreAudit()

def var_0_0.CheckGoogleSimulator():
	return NetConst.GATEWAY_PORT == 50001 and NetConst.GATEWAY_HOST == "audit.us.yo-star.com"

def var_0_0.GoSDkLoginScene():
	var_0_1.GoLoginScene()
	var_0_0.AiriInit()

def var_0_0.AiriInit(arg_6_0):
	pg.UIMgr.GetInstance().LoadingOn()
	var_0_1.InitSdk()
	print("CSharpVersion." .. tostring(CSharpVersion))

def var_0_0.AiriLogin():
	pg.UIMgr.GetInstance().LoadingOn()
	var_0_1.Login()

def var_0_0.LoginWithSocial(arg_8_0, arg_8_1, arg_8_2):
	pg.UIMgr.GetInstance().LoadingOn()

	if arg_8_0 == AIRI_PLATFORM_FACEBOOK:
		var_0_1.LoginWithFB()
	elif arg_8_0 == AIRI_PLATFORM_TWITTER:
		var_0_1.LoginWithTW()
	elif arg_8_0 == AIRI_PLATFORM_YOSTAR:
		var_0_1.LoginWithSDKAccount(arg_8_1, arg_8_2)
	elif arg_8_0 == AIRI_PLATFORM_APPLE:
		var_0_1.LoginWithApple()
	elif arg_8_0 == AIRI_PLATFORM_AMAZON:
		var_0_1.LoginWithAmazon()

def var_0_0.LoginWithTranscode(arg_9_0, arg_9_1):
	pg.UIMgr.GetInstance().LoadingOn()
	var_0_1.LoginWithTranscode(arg_9_0, arg_9_1)

def var_0_0.TranscodeRequest():
	pg.UIMgr.GetInstance().LoadingOn()
	var_0_1.TranscodeRequest()

def var_0_0.AiriBuy(arg_11_0, arg_11_1, arg_11_2):
	var_0_0.OnAiriBuying = Time.realtimeSinceStartup

	if arg_11_1 == "audit":
		var_0_1.NewBuy(arg_11_0, Airisdk.BuyServerTag.audit, arg_11_2)
	elif arg_11_1 == "preAudit":
		var_0_1.NewBuy(arg_11_0, Airisdk.BuyServerTag.preAudit, arg_11_2)
	elif arg_11_1 == "production":
		var_0_1.NewBuy(arg_11_0, Airisdk.BuyServerTag.production, arg_11_2)
	elif arg_11_1 == "test":
		var_0_1.NewBuy(arg_11_0, Airisdk.BuyServerTag.test, arg_11_2)

def var_0_0.LinkSocial(arg_12_0, arg_12_1, arg_12_2):
	var_0_0.SetAiriTimeout()

	if arg_12_0 == AIRI_PLATFORM_FACEBOOK:
		var_0_1.LinkSocial(Airisdk.LoginPlatform.FACEBOOK)
	elif arg_12_0 == AIRI_PLATFORM_TWITTER:
		var_0_1.LinkSocial(Airisdk.LoginPlatform.TWITTER)
	elif arg_12_0 == AIRI_PLATFORM_YOSTAR:
		var_0_1.LinkSocial(Airisdk.LoginPlatform.YOSTAR, arg_12_1, arg_12_2)
	elif arg_12_0 == AIRI_PLATFORM_APPLE:
		var_0_1.LinkSocial(Airisdk.LoginPlatform.APPLE)
	elif arg_12_0 == AIRI_PLATFORM_AMAZON:
		var_0_1.LinkSocial(Airisdk.LoginPlatform.AMAZON)

def var_0_0.UnlinkSocial(arg_13_0):
	var_0_0.SetAiriTimeout()

	if arg_13_0 == AIRI_PLATFORM_FACEBOOK:
		var_0_1.UnlinkSocial(Airisdk.LoginPlatform.FACEBOOK)
	elif arg_13_0 == AIRI_PLATFORM_TWITTER:
		var_0_1.UnlinkSocial(Airisdk.LoginPlatform.TWITTER)
	elif arg_13_0 == AIRI_PLATFORM_APPLE:
		var_0_1.UnlinkSocial(Airisdk.LoginPlatform.APPLE)
	elif arg_13_0 == AIRI_PLATFORM_AMAZON:
		var_0_1.UnlinkSocial(Airisdk.LoginPlatform.AMAZON)
	elif arg_13_0 == AIRI_PLATFORM_GPS:
		var_0_1.UnlinkSocial(Airisdk.LoginPlatform.GOOGLEPLAY)

def var_0_0.IsSocialLink(arg_14_0):
	if not var_0_0.GetIsPlatform():
		return False

	if arg_14_0 == AIRI_PLATFORM_FACEBOOK:
		return var_0_1.CheckPlatformLink(Airisdk.LoginPlatform.FACEBOOK)
	elif arg_14_0 == AIRI_PLATFORM_TWITTER:
		return var_0_1.CheckPlatformLink(Airisdk.LoginPlatform.TWITTER)
	elif arg_14_0 == AIRI_PLATFORM_YOSTAR:
		return var_0_1.CheckPlatformLink(Airisdk.LoginPlatform.YOSTAR)
	elif arg_14_0 == AIRI_PLATFORM_APPLE:
		return var_0_1.CheckPlatformLink(Airisdk.LoginPlatform.APPLE)
	elif arg_14_0 == AIRI_PLATFORM_AMAZON:
		return var_0_1.CheckPlatformLink(Airisdk.LoginPlatform.AMAZON)
	elif arg_14_0 == AIRI_PLATFORM_GPS:
		return var_0_1.CheckPlatformLink(Airisdk.LoginPlatform.GOOGLEPLAY)

	return False

def var_0_0.GetSocialName(arg_15_0):
	if arg_15_0 == AIRI_PLATFORM_FACEBOOK:
		return var_0_1.loginRet.FACEBOOK_NAME
	elif arg_15_0 == AIRI_PLATFORM_TWITTER:
		return var_0_1.loginRet.TWITTER_NAME
	elif arg_15_0 == AIRI_PLATFORM_YOSTAR:
		return var_0_1.loginRet.SDK_NAME
	elif arg_15_0 == AIRI_PLATFORM_APPLE:
		return var_0_1.loginRet.APPLE_ID
	elif arg_15_0 == AIRI_PLATFORM_AMAZON:
		return var_0_1.loginRet.AMAZON_NAME
	elif arg_15_0 == AIRI_PLATFORM_GPS:
		return var_0_1.loginRet.GOOGLE_PLAY_GAME_NAME

	return ""

def var_0_0.SetBirth(arg_16_0):
	pg.UIMgr.GetInstance().LoadingOn()
	var_0_1.SetBirth(arg_16_0)

def var_0_0.GetIsBirthSet():
	return var_0_1.IsBirthSet()

def var_0_0.ClearAccountCache():
	var_0_1.ClearAccountCache()

def var_0_0.GameShare(arg_19_0, arg_19_1):
	var_0_1.SystemShare(arg_19_0, arg_19_1)

def var_0_0.VerificationCodeReq(arg_20_0):
	var_0_1.VerificationCodeReq(arg_20_0)

	AIRI_LAST_GEN_TIME = Time.realtimeSinceStartup

def var_0_0.OpenYostarHelp():
	local var_21_0 = getProxy(PlayerProxy).getData()
	local var_21_1 = getProxy(UserProxy).getData()
	local var_21_2 = getProxy(ServerProxy).getLastServer(var_21_1.uid)
	local var_21_3 = pg.TimeMgr.GetInstance().STimeDescS(var_21_0.registerTime, "%Y-%m-%d %H.%M.%S")
	local var_21_4 = math.modf(var_21_0.rmb / 100)

	originalPrint("uid." .. var_21_0.id .. ",name." .. var_21_0.name .. ",level" .. var_21_0.level .. ",serverId." .. var_21_2.id .. " - " .. var_21_2.name .. ",rmb." .. var_21_4 .. ",createTime." .. var_21_3)
	var_0_1.OpenHelp(tostring(var_21_0.id), var_21_0.name, tostring(var_21_2.id .. " - " .. var_21_2.name), var_21_4, var_21_3)

def var_0_0.GetYostarUid():
	return var_0_1.loginRet.UID

def var_0_0.GetDeviceId():
	return var_0_2.GetDeviceID()

def var_0_0.GetLoginType():
	return var_0_1.loginType

def var_0_0.GetIsPlatform():
	return var_0_1.isPlatform

def var_0_0.GetChannelUID():
	local var_26_0 = var_0_1.channelUID

	originalPrint("channelUID . " .. var_26_0)

	return var_26_0

def var_0_0.UserEventUpload(arg_27_0):
	if var_0_0.GetIsPlatform():
		var_0_1.UserEventUpload(arg_27_0)

def var_0_0.ShowSurvey(arg_28_0, arg_28_1):
	if var_0_0.GetIsPlatform():
		local var_28_0 = getProxy(PlayerProxy).getData()

		var_0_2.UserEventUpload(arg_28_0, tostring(var_28_0.id), arg_28_1)

def var_0_0.Survey(arg_29_0):
	Application.OpenURL(arg_29_0)

def var_0_0.OnAndoridBackPress():
	PressBack()

def var_0_0.BindCPU():
	return

def var_0_0.CheckAiriCanBuy():
	if var_0_0.OnAiriBuying == -1 or Time.realtimeSinceStartup - var_0_0.OnAiriBuying > var_0_0.BuyingLimit:
		return True
	else
		return False

def var_0_0.AccountDelete():
	pg.UIMgr.GetInstance().LoadingOn()
	var_0_1.AccountDeleteReq()

def var_0_0.AccountReborn():
	pg.UIMgr.GetInstance().LoadingOn()
	var_0_1.AccountRebornReq()

def var_0_0.ConfirmLinkGooglePlayGame():
	var_0_1.ConfirmLinkGooglePlayGame()

def var_0_0.ConfirmUnLinkGooglePlayGame():
	var_0_1.ConfirmUnLinkGooglePlayGame()

def var_0_0.BindYostarPass():
	var_0_1.BindYostarPassReq()

def GoLoginScene():
	print("US: nothing")

def AiriInitResult(arg_39_0):
	pg.UIMgr.GetInstance().LoadingOff()

	if var_0_0.AiriResultCodeHandler(arg_39_0.R_CODE):
		AIRI_SDK_INITED = True

		OnAppPauseForSDK(False)
		AiriGoLogin()

def AiriGoLogin(arg_40_0):
	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LOGIN, {
		loginPlatform = arg_40_0
	})
	gcAll()

def AiriLogin(arg_41_0):
	pg.UIMgr.GetInstance().LoadingOff()

	local function var_41_0()
		local var_42_0 = User.New({
			type = 1,
			arg1 = PLATFORM_AIRIUS,
			arg2 = arg_41_0.UID,
			arg3 = arg_41_0.ACCESS_TOKEN
		})

		pg.m02.sendNotification(GAME.PLATFORM_LOGIN_DONE, {
			user = var_42_0
		})

	if var_0_0.AiriYoStarPassMigrateHandler(arg_41_0):
		return

	if var_0_0.AiriResultCodeHandler(arg_41_0.R_CODE):
		var_41_0()
	else
		if var_0_0.AiriPGSResultCodeHandler(arg_41_0.R_CODE, function()
			var_41_0()):
			return

		if arg_41_0.R_CODE.ToInt() == 100233:
			local var_41_1 = pg.TimeMgr.GetInstance().GetServerTime()
			local var_41_2 = tonumber(string.sub(arg_41_0.R_DELETETIME, 1, string.len(arg_41_0.R_DELETETIME) - 3))

			if var_41_1 < var_41_2:
				local var_41_3 = pg.TimeMgr.GetInstance().CTimeDescC(var_41_2, "%Y-%m-%d %H.%M.%S")

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					modal = True,
					content = i18n("box_account_reborn_content", var_41_3),
					weight = LayerWeightConst.TOP_LAYER,
					def onYes:()
						var_0_0.AccountReborn()
				})
		else
			originalPrint("AiriLogin failed")

def AiriTranscodeResult(arg_45_0):
	pg.UIMgr.GetInstance().LoadingOff()

	if var_0_0.AiriResultCodeHandler(arg_45_0.R_CODE):
		pg.m02.sendNotification(GAME.ON_GET_TRANSCODE, {
			transcode = arg_45_0.MIGRATIONCODE
		})

def AiriBuyResult(arg_46_0):
	var_0_0.OnAiriBuying = -1

	pg.UIMgr.GetInstance().LoadingOff()

	if var_0_0.AiriResultCodeHandler(arg_46_0.R_CODE):
		getProxy(ShopsProxy).removeWaitTimer()
		pg.m02.sendNotification(GAME.CHARGE_CONFIRM, {
			payId = arg_46_0.EXTRADATA,
			bsId = arg_46_0.ORDERID
		})
	else
		getProxy(ShopsProxy).removeWaitTimer()
		pg.m02.sendNotification(GAME.CHARGE_FAILED, {
			payId = arg_46_0.EXTRADATA
		})

def SetBirthResult(arg_47_0):
	pg.UIMgr.GetInstance().LoadingOff()

	if var_0_0.AiriResultCodeHandler(arg_47_0.R_CODE):
		pg.TipsMgr.GetInstance().ShowTips(i18n("set_birth_success"))

def LinkSocialResult(arg_48_0):
	var_0_0.EndAiriTimeout()

	if var_0_0.AiriResultCodeHandler(arg_48_0.R_CODE):
		pg.m02.sendNotification(GAME.ON_SOCIAL_LINKED)

def UnlinkSocialResult(arg_49_0):
	var_0_0.EndAiriTimeout()

	if var_0_0.AiriResultCodeHandler(arg_49_0.R_CODE):
		pg.m02.sendNotification(GAME.ON_SOCIAL_UNLINKED)
	elif var_0_0.AiriPGSResultCodeHandler(arg_49_0.R_CODE):
		return

def VerificationCodeResult(arg_50_0):
	pg.UIMgr.GetInstance().LoadingOff()

	if var_0_0.AiriResultCodeHandler(arg_50_0.R_CODE):
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			content = i18n("verification_code_req_tip2")
		})

def OnAppPauseForSDK(arg_51_0):
	if not AIRI_SDK_INITED:
		return

	if arg_51_0:
		var_0_2.OnPause()
	else
		var_0_2.OnResume()

def AccountDeleteResult(arg_52_0, arg_52_1, arg_52_2, arg_52_3, arg_52_4):
	pg.UIMgr.GetInstance().LoadingOff()

	local var_52_0 = {
		def ToInt:()
			return arg_52_0
	}

	if var_0_0.AiriResultCodeHandler(var_52_0):
		local var_52_1 = tonumber(string.sub(arg_52_3, 1, string.len(arg_52_3) - 3))
		local var_52_2 = pg.TimeMgr.GetInstance().CTimeDescC(var_52_1, "%Y-%m-%d %H.%M.%S")

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			modal = True,
			hideNo = True,
			content = i18n("box_account_del_success_content", var_52_2),
			weight = LayerWeightConst.TOP_LAYER,
			def onYes:()
				pg.m02.sendNotification(GAME.LOGOUT, {
					code = 0
				}),
			def onClose:()
				pg.m02.sendNotification(GAME.LOGOUT, {
					code = 0
				})
		})

def AccountRebornResult(arg_56_0, arg_56_1):
	pg.UIMgr.GetInstance().LoadingOff()

	local var_56_0 = {
		def ToInt:()
			return arg_56_0
	}

	if var_0_0.AiriResultCodeHandler(var_56_0):
		pg.TipsMgr.GetInstance().ShowTips(i18n("tip_account_del_reborn"))

def BindYostarPassResult(arg_58_0, arg_58_1):
	local var_58_0 = {
		def ToInt:()
			return arg_58_0
	}

	if var_0_0.AiriResultCodeHandler(var_58_0):
		pg.TipsMgr.GetInstance().ShowTips("Bind Success.")

def OnYoStarMessageReceivedRespone(arg_60_0, arg_60_1, arg_60_2, arg_60_3):
	warning("OnYoStarMessageReceivedRespone")

def var_0_0.AiriResultCodeHandler(arg_61_0):
	local var_61_0 = arg_61_0.ToInt()
	local var_61_1 = "." .. var_61_0

	if var_61_0 == 0:
		return True
	else
		local var_61_2 = {
			100233,
			100201,
			100202,
			100203,
			100204,
			100205,
			100206,
			100214
		}

		if table.contains(var_61_2, var_61_0):
			return False

		if var_61_0 == 100110:
			var_0_0.ClearAccountCache()

		originalPrint("SDK Error Code." .. var_61_0)

		local var_61_3 = i18n("new_airi_error_code_" .. var_61_0)

		if string.find(var_61_3, "UndefinedLanguage"):
			pg.TipsMgr.GetInstance().ShowTips(i18n("new_airi_error_code_other") .. var_61_1)
		else
			pg.TipsMgr.GetInstance().ShowTips(var_61_3 .. var_61_1)

	return False

def var_0_0.AiriPGSResultCodeHandler(arg_62_0, arg_62_1):
	local var_62_0 = arg_62_0.ToInt()

	originalPrint("AiriPGSResultCodeHandler", tostring(var_62_0))

	if var_62_0 == 100201:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("pgs_login_binding_exist2"),
			def onYes:()
				var_0_0.ConfirmLinkGooglePlayGame()
		})

		return True
	elif var_62_0 == 100202:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("pgs_login_binding_exist1"),
			def onYes:()
				var_0_0.ConfirmLinkGooglePlayGame()
		})

		return True
	elif var_62_0 == 100203:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("pgs_login_binding_exist3"),
			def onYes:()
				var_0_0.ConfirmLinkGooglePlayGame()
		})

		return True
	elif var_62_0 == 100204:
		arg_62_1()

		return True
	elif var_62_0 == 100205:
		return True
	elif var_62_0 == 100206:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			content = i18n("pgs_login_tip"),
			def onYes:()
				pg.m02.sendNotification(GAME.ON_SOCIAL_LINKED),
			def onClose:()
				pg.m02.sendNotification(GAME.ON_SOCIAL_LINKED)
		})

		return True
	elif var_62_0 == 100214:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("pgs_unbind_tip2"),
			def onYes:()
				var_0_0.ConfirmUnLinkGooglePlayGame()
		})

		return True
	else
		return False

def var_0_0.AiriYoStarPassMigrateHandler(arg_69_0):
	local var_69_0 = {
		0,
		100204,
		100206
	}

	if table.contains(var_69_0, arg_69_0.R_CODE.ToInt()) and arg_69_0.SHOW_MIGRATE_PAGE == 1:
		var_0_0.BindYostarPass()

		return True
	else
		return False

var_0_0.ON_AIRI_LOADING = False

def var_0_0.SetAiriTimeout():
	pg.UIMgr.GetInstance().LoadingOn()

	var_0_0.ON_AIRI_LOADING = True

	onDelayTick(function()
		if var_0_0.ON_AIRI_LOADING:
			pg.UIMgr.GetInstance().LoadingOff()

			var_0_0.ON_AIRI_LOADING = False, 15)

def var_0_0.EndAiriTimeout():
	var_0_0.ON_AIRI_LOADING = False

	pg.UIMgr.GetInstance().LoadingOff()

return var_0_0
