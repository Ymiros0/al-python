local var_0_0 = {}
local var_0_1 = BilibiliSdkMgr.inst
local var_0_2 = "BLHX24V20210713"
local var_0_3 = "FTBLHX20190524WW"

PACKAGE_TYPE_BILI = 1
PACKAGE_TYPE_SHAJOY = 2
PACKAGE_TYPE_UNION = 3
PACKAGE_TYPE_YYX = 4

def var_0_0.CheckPretest():
	return NetConst.GATEWAY_HOST == "line1-test-login-ios-blhx.bilibiligame.net" and (NetConst.GATEWAY_PORT == 80 or NetConst.GATEWAY_PORT == 10080) or NetConst.GATEWAY_HOST == "line1-test-login-bili-blhx.bilibiligame.net" and (NetConst.GATEWAY_PORT == 80 or NetConst.GATEWAY_PORT == 10080) or IsUnityEditor

def var_0_0.CheckWorldTest():
	return NetConst.GATEWAY_PORT == 10080 and NetConst.GATEWAY_HOST == "blhx-test-world-ios-game.bilibiligame.net"

def var_0_0.InitSDK():
	if PLATFORM_CHT == PLATFORM_CODE:
		var_0_1.sandboxKey = var_0_3

	var_0_1.Init()

def var_0_0.GoSDkLoginScene():
	var_0_1.GoLoginScene()

def var_0_0.LoginQQ():
	var_0_1.Login(1)

def var_0_0.LoginWX():
	var_0_1.Login(2)

def var_0_0.LoginSdk(arg_7_0):
	if arg_7_0 == 1:
		var_0_0.LoginQQ()
	elif arg_7_0 == 2:
		var_0_0.LoginWX()
	else
		var_0_1.Login(0)

def var_0_0.TryLoginSdk():
	var_0_1.TryLogin()

def var_0_0.CreateRole(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4):
	var_0_1.CreateRole(arg_9_0, arg_9_1, arg_9_2, 1000 * arg_9_3, "vip0", arg_9_4)

def var_0_0.EnterServer(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4, arg_10_5, arg_10_6):
	var_0_1.EnterServer(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4 * 1000, arg_10_5, "vip0", arg_10_6)

def var_0_0.ChooseServer(arg_11_0, arg_11_1):
	var_0_1.ChooseServer(arg_11_0, arg_11_1)

def var_0_0.SdkGateWayLogined():
	var_0_1.OnGatewayLogined()

def var_0_0.SdkLoginGetaWayFailed():
	var_0_1.OnLoginGatewayFailed()

def var_0_0.SdkLevelUp():
	var_0_1.LevelUp()

def var_0_0.SdkPay(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4, arg_15_5, arg_15_6, arg_15_7, arg_15_8, arg_15_9):
	var_0_1.Pay(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4, arg_15_5, arg_15_6, arg_15_7, arg_15_8, arg_15_9)

def var_0_0.LogoutSDK(arg_16_0):
	if arg_16_0 != 0 and CSharpVersion >= 44:
		var_0_1.ClearLoginData()
	else
		var_0_1.LocalLogout()

def var_0_0.BindCPU():
	return

def var_0_0.DeleteAccount():
	if LuaHelper.GetCHPackageType() == PACKAGE_TYPE_UNION:
		local var_18_0 = getProxy(UserProxy).getRawData()
		local var_18_1 = getProxy(ServerProxy).getRawData()[var_18_0 and var_18_0.server or 0]
		local var_18_2 = var_18_1 and var_18_1.name or ""
		local var_18_3 = getProxy(PlayerProxy).getRawData()
		local var_18_4 = var_18_3 and var_18_3.GetName() or ""
		local var_18_5 = var_18_3 and tostring(var_18_3.level) or "0"
		local var_18_6 = var_18_3 and var_18_3.GetRegisterTime() or 0
		local var_18_7 = pg.TimeMgr.GetInstance().STimeDescS(var_18_6, "%Y/%m/%d")

		var_0_1.DeleteAccountForUO(var_18_4, var_18_2, var_18_5, var_18_7)
	else
		var_0_1.DeleteAccount()

def var_0_0.OnAndoridBackPress():
	local var_19_0 = LuaHelper.GetCHPackageType()

	if var_19_0 == PACKAGE_TYPE_BILI or var_19_0 == PACKAGE_TYPE_SHAJOY:
		if not IsNil(pg.MsgboxMgr.GetInstance()._go):
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("confirm_app_exit"),
				def onYes:()
					var_0_1.onBackPressed()
			})
		else
			var_0_1.onBackPressed()
	else
		var_0_1.onBackPressed()

def var_0_0.ShowPrivate():
	local var_21_0 = LuaHelper.GetCHPackageType()

	if var_21_0 == PACKAGE_TYPE_UNION or IsUnityEditor:
		pg.UserAgreementMgr.GetInstance().ShowForBiliPrivate()
	elif var_21_0 == PACKAGE_TYPE_SHAJOY:
		Application.OpenURL("https.//game.bilibili.com/uosdk_privacy/h5?game_id=209&privacyProtocol=1")
	elif var_21_0 == PACKAGE_TYPE_YYX:
		-- block empty
	else
		var_0_1.ShowPrivate()

def var_0_0.ShowLicence():
	local var_22_0 = LuaHelper.GetCHPackageType()

	if var_22_0 == PACKAGE_TYPE_UNION or IsUnityEditor:
		pg.UserAgreementMgr.GetInstance().ShowForBiliLicence()
	elif var_22_0 == PACKAGE_TYPE_SHAJOY:
		Application.OpenURL("https.//game.bilibili.com/uosdk_privacy/h5?game_id=209&userProtocol=1")
	elif var_22_0 == PACKAGE_TYPE_YYX:
		-- block empty
	else
		var_0_1.ShowLicence()

def var_0_0.GetBiliServerId():
	local var_23_0 = var_0_1.serverId

	originalPrint("serverId . " .. var_23_0)

	return var_23_0

def var_0_0.GetChannelUID():
	local var_24_0 = var_0_1.channelUID

	originalPrint("channelUID . " .. var_24_0)

	return var_24_0

def var_0_0.GetLoginType():
	return var_0_1.loginType

def var_0_0.GetIsPlatform():
	return var_0_1.isPlatform

def var_0_0.GameShare(arg_27_0, arg_27_1):
	var_0_1.ShareWithImage("Azur Lane", arg_27_0, arg_27_1)

def var_0_0.Service():
	local var_28_0 = getProxy(PlayerProxy)

	if not var_28_0:
		return

	local var_28_1 = var_28_0.getRawData()
	local var_28_2 = var_28_1.id
	local var_28_3 = var_28_1.GetName()
	local var_28_4 = ""
	local var_28_5 = ""
	local var_28_6 = PLATFORM == PLATFORM_IPHONEPLAYER and "portrai" or "portrait"

	var_0_1.Service(var_28_2, var_28_3, var_28_4, var_28_6)

def var_0_0.Survey(arg_29_0):
	var_0_1.OpenWeb(arg_29_0)

def var_0_0.IsHuaweiPackage():
	return var_0_1.isHuawei()

def StartSdkLogin():
	Timer.New(function()
		var_0_1.OnLoginTimeOut(), 30, 1).Start()

def GoLoginScene():
	if not pg.m02:
		originalPrint("game is not start")

		return

	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LOGIN)
	gcAll()

def SDKLogined(arg_34_0, arg_34_1, arg_34_2, arg_34_3):
	if not pg.m02:
		originalPrint("game is not start")

		return

	local var_34_0 = User.New({
		type = 1,
		arg1 = arg_34_0,
		arg2 = arg_34_1,
		arg3 = arg_34_2,
		arg4 = arg_34_3
	})

	if LuaHelper.GetCHPackageType() == PACKAGE_TYPE_UNION:
		pg.m02.sendNotification(GAME.PLATFORM_LOGIN_DONE, {
			user = var_34_0
		})
	else
		pg.m02.sendNotification(GAME.SERVER_INTERCOMMECTION, {
			user = var_34_0
		})

def SDKLogouted(arg_35_0):
	if not pg.m02:
		originalPrint("game is not start")

		return

	pg.m02.sendNotification(GAME.LOGOUT, {
		code = arg_35_0
	})

def PaySuccess(arg_36_0, arg_36_1):
	if not pg.m02:
		originalPrint("game is not start")

		return

	getProxy(ShopsProxy).removeWaitTimer()
	pg.m02.sendNotification(GAME.CHARGE_CONFIRM, {
		payId = arg_36_0,
		bsId = arg_36_1
	})

def PayFailed(arg_37_0, arg_37_1):
	if not pg.m02:
		originalPrint("game is not start")

		return

	getProxy(ShopsProxy).removeWaitTimer()

	arg_37_1 = tonumber(arg_37_1)

	if not arg_37_1:
		return

	pg.m02.sendNotification(GAME.CHARGE_FAILED, {
		payId = arg_37_0,
		code = arg_37_1
	})

	if PLATFORM == PLATFORM_IPHONEPLAYER:
		pg.TipsMgr.GetInstance().ShowTips(i18n1("支付失败" .. arg_37_1))
	elif arg_37_1 == -5:
		pg.TipsMgr.GetInstance().ShowTips(i18n1("订单签名异常" .. arg_37_1))
	elif arg_37_1 > 0:
		if arg_37_1 > 1000 and arg_37_1 < 2000:
			pg.TipsMgr.GetInstance().ShowTips(i18n1("数据格式验证错误" .. arg_37_1))
		elif arg_37_1 >= 2000 and arg_37_1 < 3000:
			pg.TipsMgr.GetInstance().ShowTips(i18n1("服务器返回异常" .. arg_37_1))
		elif arg_37_1 >= 3000 and arg_37_1 < 4000:
			pg.TipsMgr.GetInstance().ShowTips(i18n1("未登录或者会话已超时" .. arg_37_1))
		elif arg_37_1 == 4000:
			pg.TipsMgr.GetInstance().ShowTips(i18n1("系统错误" .. arg_37_1))
		elif arg_37_1 == 6001:
			pg.TipsMgr.GetInstance().ShowTips(i18n1("用户中途取消" .. arg_37_1))
		elif arg_37_1 == 7005:
			pg.TipsMgr.GetInstance().ShowTips(i18n1("支付失败" .. arg_37_1))
		elif arg_37_1 == 7004:
			pg.TipsMgr.GetInstance().ShowTips(i18n1("支付失败" .. arg_37_1))
	elif arg_37_1 == -201:
		pg.TipsMgr.GetInstance().ShowTips(i18n1("生成订单失败" .. arg_37_1))
	elif arg_37_1 == -202:
		pg.TipsMgr.GetInstance().ShowTips(i18n1("支付取消" .. arg_37_1))
	elif arg_37_1 == -203:
		pg.TipsMgr.GetInstance().ShowTips(i18n1("支付失败" .. arg_37_1))

def OnSDKInitFailed(arg_38_0):
	if not pg.m02:
		originalPrint("game is not start")

		return

	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		hideNo = True,
		content = arg_38_0,
		onYes = var_0_0.InitSDK
	})

def ShowMsgBox(arg_39_0):
	if not pg.m02:
		originalPrint("game is not start")

		return

	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		hideNo = True,
		content = arg_39_0
	})

def OnShowLicenceFailed():
	return

def OnShowPrivateFailed():
	return

def OnShareSuccess():
	return

def OnShareFailed():
	return

def CloseAgreementView():
	return

def OnDeleteAccountSuccess():
	pg.m02.sendNotification(GAME.LOGOUT, {
		code = 0
	})

def OnDeleteAccountDisable():
	pg.TipsMgr.GetInstance().ShowTips("功能未开启")

def OnDeleteAccountFailed():
	pg.TipsMgr.GetInstance().ShowTips("注销失败")

return var_0_0
