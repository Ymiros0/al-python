pg = pg or {}
pg.SdkMgr = singletonClass("SdkMgr")

local var_0_0 = pg.SdkMgr

def var_0_0.Ctor(arg_1_0):
	if PLATFORM_CODE == PLATFORM_CH:
		arg_1_0.instance = require("Mgr.Sdk.BiliSDKMgr")
	elif PLATFORM_CODE == PLATFORM_JP:
		arg_1_0.instance = require("Mgr.Sdk.AiriSDKJPMgr")
	elif PLATFORM_CODE == PLATFORM_KR:
		arg_1_0.instance = require("Mgr.Sdk.TxwyKrSDKMgr")
	elif PLATFORM_CODE == PLATFORM_US:
		arg_1_0.instance = require("Mgr.Sdk.AiriSDKUSMgr")
	elif PLATFORM_CODE == PLATFORM_CHT:
		arg_1_0.instance = require("Mgr.Sdk.YongshiSdkMgr")

	arg_1_0.pcode = arg_1_0.GetPlatformCode(Application.identifier)

def var_0_0.Call(arg_2_0, arg_2_1, ...):
	assert(arg_2_0.instance)

	if arg_2_0.instance[arg_2_1]:
		arg_2_0.instance[arg_2_1](...)

def var_0_0.Get(arg_3_0, arg_3_1, ...):
	assert(arg_3_0.instance)
	assert(arg_3_0.instance[arg_3_1], "func should exist " .. arg_3_1)

	return arg_3_0.instance[arg_3_1](...)

def EnterMultiWindow(arg_4_0):
	originalPrint(".......EnterMultiWindow")

def ExitMultiWindow(arg_5_0):
	originalPrint(".......ExitMultiWindow")

def var_0_0.InitSDK(arg_6_0):
	arg_6_0.Call("InitSDK")

def var_0_0.GoSDkLoginScene(arg_7_0):
	arg_7_0.Call("GoSDkLoginScene")

def var_0_0.LoginSdk(arg_8_0, arg_8_1):
	arg_8_0.Call("LoginSdk", arg_8_1)

def var_0_0.TryLoginSdk(arg_9_0):
	arg_9_0.Call("TryLoginSdk")

def var_0_0.CreateRole(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4, arg_10_5):
	arg_10_0.Call("CreateRole", arg_10_1, arg_10_2, arg_10_3, arg_10_4, arg_10_5)

def var_0_0.EnterServer(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4, arg_11_5, arg_11_6, arg_11_7):
	arg_11_0.Call("EnterServer", arg_11_1, arg_11_2, arg_11_3, arg_11_4, arg_11_5, arg_11_6, arg_11_7)

def var_0_0.ChooseServer(arg_12_0, arg_12_1, arg_12_2):
	arg_12_0.Call("ChooseServer", arg_12_1, arg_12_2)

def var_0_0.SdkGateWayLogined(arg_13_0):
	arg_13_0.Call("SdkGateWayLogined")

def var_0_0.SdkLoginGetaWayFailed(arg_14_0):
	arg_14_0.Call("SdkLoginGetaWayFailed")

def var_0_0.SdkLevelUp(arg_15_0):
	arg_15_0.Call("SdkLevelUp")

def var_0_0.SdkPay(arg_16_0, arg_16_1, arg_16_2, arg_16_3, arg_16_4, arg_16_5, arg_16_6, arg_16_7, arg_16_8, arg_16_9, arg_16_10):
	arg_16_0.Call("SdkPay", arg_16_1, arg_16_2, arg_16_3, arg_16_4, arg_16_5, arg_16_6, arg_16_7, arg_16_8, arg_16_9, arg_16_10)

def var_0_0.LogoutSDK(arg_17_0, arg_17_1):
	arg_17_0.Call("LogoutSDK", arg_17_1)

def var_0_0.BindCPU(arg_18_0):
	arg_18_0.Call("BindCPU")

def var_0_0.OnAndoridBackPress(arg_19_0):
	arg_19_0.Call("OnAndoridBackPress")

def var_0_0.DeleteAccount(arg_20_0):
	arg_20_0.Call("DeleteAccount")

def var_0_0.GetChannelUID(arg_21_0):
	return arg_21_0.Get("GetChannelUID")

def var_0_0.GetLoginType(arg_22_0):
	local var_22_0 = Application.persistentDataPath .. "/server_config.txt"

	if PathMgr.FileExists(var_22_0):
		return LoginType.PLATFORM_INNER

	return arg_22_0.Get("GetLoginType")

def var_0_0.GetIsPlatform(arg_23_0):
	return arg_23_0.Get("GetIsPlatform")

def var_0_0.EnterLoginScene(arg_24_0):
	arg_24_0.inLoginScene = True

def var_0_0.ExitLoginScene(arg_25_0):
	arg_25_0.inLoginScene = False

def var_0_0.IsInLoginScene(arg_26_0):
	return arg_26_0.inLoginScene

def var_0_0.IsYunPackage(arg_27_0):
	return PLATFORM_CODE == PLATFORM_CH and arg_27_0.GetChannelUID() == "yun"

def var_0_0.Service(arg_28_0):
	arg_28_0.Call("Service")

def var_0_0.Survey(arg_29_0, arg_29_1):
	arg_29_0.Call("Survey", arg_29_1)

def var_0_0.IsHuaweiPackage(arg_30_0):
	return PLATFORM_CODE == PLATFORM_CH and arg_30_0.Get("IsHuaweiPackage")

def var_0_0.IsAUPackage(arg_31_0):
	return PLATFORM_CODE == PLATFORM_JP and arg_31_0.GetChannelUID() == "2"

def var_0_0.GetYostarUid(arg_32_0):
	return arg_32_0.Get("GetYostarUid")

def var_0_0.GetYostarTransCode(arg_33_0):
	return arg_33_0.Get("GetTransCode")

def var_0_0.CheckAudit(arg_34_0):
	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
		return arg_34_0.Get("CheckAudit")
	else
		return False

def var_0_0.CheckPreAudit(arg_35_0):
	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
		return arg_35_0.Get("CheckPreAudit")
	else
		return False

def var_0_0.CheckPretest(arg_36_0):
	return arg_36_0.Get("CheckPretest")

def var_0_0.CheckGoogleSimulator(arg_37_0):
	return arg_37_0.Get("CheckGoogleSimulator")

def var_0_0.CheckWorldTest(arg_38_0):
	if PLATFORM_CODE == PLATFORM_CH:
		return arg_38_0.Get("CheckWorldTest")
	else
		return False

def var_0_0.AiriLoginSDK(arg_39_0):
	arg_39_0.Call("AiriLogin")

def var_0_0.TranscodeRequest(arg_40_0):
	arg_40_0.Call("TranscodeRequest")

def var_0_0.LoginWithTranscode(arg_41_0, arg_41_1, arg_41_2):
	arg_41_0.Call("LoginWithTranscode", arg_41_1, arg_41_2)

def var_0_0.LoginWithSocial(arg_42_0, arg_42_1, arg_42_2, arg_42_3):
	arg_42_0.Call("LoginWithSocial", arg_42_1, arg_42_2, arg_42_3)

def var_0_0.LoginWithDevice(arg_43_0):
	arg_43_0.Call("LoginWithDevice")

def var_0_0.AiriBuy(arg_44_0, arg_44_1, arg_44_2, arg_44_3):
	arg_44_0.Call("AiriBuy", arg_44_1, arg_44_2, arg_44_3)

def var_0_0.LinkSocial(arg_45_0, arg_45_1, arg_45_2, arg_45_3):
	arg_45_0.Call("LinkSocial", arg_45_1, arg_45_2, arg_45_3)

def var_0_0.UnlinkSocial(arg_46_0, arg_46_1):
	arg_46_0.Call("UnlinkSocial", arg_46_1)

def var_0_0.IsSocialLink(arg_47_0, arg_47_1):
	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
		return arg_47_0.Get("IsSocialLink", arg_47_1)
	else
		return False

def var_0_0.GetSocialName(arg_48_0, arg_48_1):
	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
		return arg_48_0.Get("GetSocialName", arg_48_1)
	else
		return "none"

def var_0_0.GetIsBirthSet(arg_49_0):
	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
		return arg_49_0.Get("GetIsBirthSet")

	return True

def var_0_0.SetBirth(arg_50_0, arg_50_1):
	arg_50_0.Call("SetBirth", arg_50_1)

def var_0_0.ClearAccountCache(arg_51_0):
	arg_51_0.Call("ClearAccountCache")

def var_0_0.GameShare(arg_52_0, arg_52_1, arg_52_2):
	arg_52_0.Call("GameShare", arg_52_1, arg_52_2)

def var_0_0.VerificationCodeReq(arg_53_0, arg_53_1):
	arg_53_0.Call("VerificationCodeReq", arg_53_1)

def var_0_0.OpenYostarHelp(arg_54_0):
	arg_54_0.Call("OpenYostarHelp")

def var_0_0.OnAppPauseForSDK(arg_55_0, arg_55_1):
	arg_55_0.Call("OnAppPauseForSDK", arg_55_1)

def var_0_0.UserEventUpload(arg_56_0, arg_56_1):
	arg_56_0.Call("UserEventUpload", arg_56_1)

def var_0_0.ShowSurvey(arg_57_0, arg_57_1, arg_57_2):
	return arg_57_0.Call("ShowSurvey", arg_57_1, arg_57_2)

def var_0_0.CheckAiriCanBuy(arg_58_0):
	if PLATFORM_CODE == PLATFORM_US or PLATFORM_CODE == PLATFORM_JP:
		return arg_58_0.Get("CheckAiriCanBuy")
	else
		return True

def var_0_0.CheckHadAccountCache(arg_59_0):
	if PLATFORM_CODE == PLATFORM_JP:
		return arg_59_0.Get("CheckHadAccountCache")
	else
		return True

def var_0_0.AccountDelete(arg_60_0):
	if PLATFORM_CODE == PLATFORM_US or PLATFORM_CODE == PLATFORM_JP:
		return arg_60_0.Get("AccountDelete")
	else
		return True

def var_0_0.AccountReborn(arg_61_0):
	if PLATFORM_CODE == PLATFORM_US or PLATFORM_CODE == PLATFORM_JP:
		return arg_61_0.Get("AccountReborn")
	else
		return True

def var_0_0.ConfirmLinkGooglePlayGame(arg_62_0):
	if PLATFORM_CODE == PLATFORM_US or PLATFORM_CODE == PLATFORM_JP:
		return arg_62_0.Get("ConfirmLinkGooglePlayGame")
	else
		return True

def var_0_0.ConfirmUnLinkGooglePlayGame(arg_63_0):
	if PLATFORM_CODE == PLATFORM_US or PLATFORM_CODE == PLATFORM_JP:
		return arg_63_0.Get("ConfirmUnLinkGooglePlayGame")
	else
		return True

def var_0_0.BindYostarPass(arg_64_0):
	if PLATFORM_CODE == PLATFORM_US or PLATFORM_CODE == PLATFORM_JP:
		return arg_64_0.Get("BindYostarPass")
	else
		return True

AIRI_LAST_GEN_TIME = 0
AIRI_GEN_LIMIT_TIME = 30

def GetAiriGenCodeTimeRemain():
	local var_65_0 = Time.realtimeSinceStartup - AIRI_LAST_GEN_TIME

	if var_65_0 > AIRI_GEN_LIMIT_TIME or AIRI_LAST_GEN_TIME == 0:
		return 0
	else
		return math.floor(AIRI_GEN_LIMIT_TIME - var_65_0)

def var_0_0.UserCenter(arg_66_0):
	arg_66_0.Call("UserCenter")

def var_0_0.BugReport(arg_67_0):
	arg_67_0.Call("BugReport")

def var_0_0.StoreReview(arg_68_0):
	arg_68_0.Call("StoreReview")

def var_0_0.QueryWithProduct(arg_69_0):
	arg_69_0.Call("QueryWithProduct")

def var_0_0.ShareImg(arg_70_0, arg_70_1, arg_70_2):
	arg_70_0.Call("ShareImg", arg_70_1, arg_70_2)

def var_0_0.SwitchAccount(arg_71_0):
	arg_71_0.Call("SwitchAccount")

def var_0_0.CompletedTutorial(arg_72_0):
	arg_72_0.Call("CompletedTutorial")

def var_0_0.UnlockAchievement(arg_73_0):
	arg_73_0.Call("UnlockAchievement")

def var_0_0.IsBindFaceBook(arg_74_0):
	if PLATFORM_CODE == PLATFORM_CHT:
		return arg_74_0.Get("IsBindFaceBook")

def var_0_0.IsBindApple(arg_75_0):
	if PLATFORM_CODE == PLATFORM_CHT:
		return arg_75_0.Get("IsBindApple")

def var_0_0.IsBindGoogle(arg_76_0):
	if PLATFORM_CODE == PLATFORM_CHT:
		return arg_76_0.Get("IsBindGoogle")

def var_0_0.IsBindPhone(arg_77_0):
	if PLATFORM_CODE == PLATFORM_CHT:
		return arg_77_0.Get("IsBindPhone")

def var_0_0.IsBindGameCenter(arg_78_0):
	if PLATFORM_CODE == PLATFORM_CHT:
		return False

def var_0_0.CanTriggerDeepLinking(arg_79_0):
	if PLATFORM_CODE == PLATFORM_CHT:
		return arg_79_0.Get("CanTriggerDeepLinking")
	else
		return False

def var_0_0.TriggerDeepLinking(arg_80_0):
	arg_80_0.Call("TriggerDeepLinking")

def var_0_0.BindSocial(arg_81_0, arg_81_1):
	if arg_81_1 == 1:
		arg_81_0.BindFaceBook()
	elif arg_81_1 == 2:
		arg_81_0.BindGoogle()
	elif arg_81_1 == 3:
		arg_81_0.BindPhone()
	elif arg_81_1 == 4:
		-- block empty
	elif arg_81_1 == 5:
		arg_81_0.BindApple()

def var_0_0.UnbindSocial(arg_82_0, arg_82_1):
	if arg_82_1 == 1:
		arg_82_0.UnBindFaceBook()
	elif arg_82_1 == 2:
		arg_82_0.UnBindGoogle()
	elif arg_82_1 == 3:
		arg_82_0.UnBindPhone()
	elif arg_82_1 == 4:
		-- block empty

def var_0_0.BindFaceBook(arg_83_0):
	arg_83_0.Call("BindFaceBook")

def var_0_0.BindApple(arg_84_0):
	arg_84_0.Call("BindApple")

def var_0_0.BindGoogle(arg_85_0):
	arg_85_0.Call("BindGoogle")

def var_0_0.BindPhone(arg_86_0):
	arg_86_0.Call("BindPhone")

def var_0_0.UnBindFaceBook(arg_87_0):
	arg_87_0.Call("UnBindFaceBook")

def var_0_0.UnBindGoogle(arg_88_0):
	arg_88_0.Call("UnBindGoogle")

def var_0_0.UnBindPhone(arg_89_0):
	arg_89_0.Call("UnBindPhone")

def var_0_0.ShowLicence(arg_90_0):
	arg_90_0.Call("ShowLicence")

def var_0_0.ShowPrivate(arg_91_0):
	arg_91_0.Call("ShowPrivate")

def var_0_0.GetProduct(arg_92_0, arg_92_1):
	if PLATFORM_CODE == PLATFORM_CHT:
		return arg_92_0.Get("GetProduct", arg_92_1)

def var_0_0.GetDeviceId(arg_93_0):
	if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
		return arg_93_0.Get("GetDeviceId")
	elif PLATFORM_CODE == PLATFORM_KR:
		return arg_93_0.Get("GetDeviceModel")
	elif PLATFORM_CODE == PLATFORM_CHT:
		return SystemInfo.deviceUniqueIdentifier
	else
		return ""

def InLoginScene():
	local function var_94_0()
		return getProxy(UserProxy).GetLoginedFlag()

	if pg.SdkMgr.GetInstance().IsInLoginScene() and not var_94_0():
		return True

	return False

def var_0_0.GetPlatformCode(arg_96_0, arg_96_1):
	if PLATFORM_CODE == PLATFORM_CHT:
		return arg_96_0.Get("GetPackageCode", arg_96_1)
	else
		return None

def var_0_0.IgnorePlatform(arg_97_0, arg_97_1):
	local var_97_0 = arg_97_0.pcode

	if var_97_0 and arg_97_1 and #arg_97_1 > 0 and _.any(arg_97_1, function(arg_98_0)
		return tostring(arg_98_0) == var_97_0):
		return True

	return False
