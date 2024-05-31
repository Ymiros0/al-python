local var_0_0 = {}
local var_0_1 = YongshiSdkMgr.inst
local var_0_2 = "com.hkmanjuu.azurlane.gp.mc"
local var_0_3 = "com.hkmanjuu.azurlane.gp"
local var_0_4 = "com.hkmanjuu.azurlane.ios1"

def var_0_0.CheckPretest():
	return NetConst.GATEWAY_HOST == "ts-all-login.azurlane.tw" and (NetConst.GATEWAY_PORT == 11001 or NetConst.GATEWAY_PORT == 11101) or IsUnityEditor

def var_0_0.InitSDK():
	var_0_1.Init()

def var_0_0.GoSDkLoginScene():
	var_0_1.GoLoginScene()

def var_0_0.LoginSdk(arg_4_0):
	var_0_1.Login(0)

def var_0_0.TryLoginSdk():
	var_0_1.TryLogin()

def var_0_0.SdkGateWayLogined():
	var_0_1.OnGatewayLogined()

def var_0_0.SdkLoginGetaWayFailed():
	var_0_1.OnLoginGatewayFailed()

def var_0_0.IsBindApple():
	return var_0_1.bindInfo.IsBindApple()

def var_0_0.IsBindFaceBook():
	return var_0_1.bindInfo.IsBindFaceBook()

def var_0_0.IsBindGoogle():
	return var_0_1.bindInfo.IsBindGoogle()

def var_0_0.IsBindPhone():
	return var_0_1.bindInfo.IsBindPhone()

def var_0_0.BindApple():
	var_0_1.BindApple()

def var_0_0.BindFaceBook():
	var_0_1.BindFaceBook()

def var_0_0.BindGoogle():
	var_0_1.BindGoogle()

def var_0_0.BindPhone():
	var_0_1.BindPhone()

def var_0_0.UnBindPhone():
	var_0_1.UnBindPhone()

def var_0_0.UnBindApple():
	var_0_1.UnBindApple()

def var_0_0.UnBindFaceBook():
	var_0_1.UnBindFaceBook()

def var_0_0.UnBindGoogle():
	var_0_1.UnBindGoogle()

def var_0_0.CanTriggerDeepLinking():
	return var_0_1.CanTriggerDeepLinking()

def var_0_0.TriggerDeepLinking():
	var_0_1.TriggerDeepLinking()

def var_0_0.SdkPay(arg_22_0, arg_22_1, arg_22_2, arg_22_3, arg_22_4, arg_22_5, arg_22_6, arg_22_7, arg_22_8, arg_22_9):
	local var_22_0 = getProxy(UserProxy).getData().uid
	local var_22_1 = getProxy(ServerProxy).getLastServer(var_22_0)
	local var_22_2 = var_22_1.id
	local var_22_3 = var_22_1.name
	local var_22_4 = getProxy(PlayerProxy).getRawData()
	local var_22_5 = var_22_4.id
	local var_22_6 = var_22_4.name
	local var_22_7 = var_22_4.level

	var_0_1.Pay(arg_22_0, arg_22_2, arg_22_5, arg_22_1, "1", arg_22_3, "1", var_22_2, var_22_3, var_22_2, var_22_5, var_22_6, var_22_7, arg_22_8, "1", arg_22_4, arg_22_6, arg_22_9)

def var_0_0.UserEventUpload(arg_23_0):
	var_0_1.UserEventUpload(arg_23_0)

def var_0_0.LogoutSDK():
	var_0_1.LocalLogout()

def var_0_0.BindCPU():
	var_0_1.callSdkApi("bindCpu", None)

def var_0_0.DeleteAccount():
	var_0_1.Delete()

def var_0_0.OnAndoridBackPress():
	PressBack()

def var_0_0.ShareImg(arg_28_0, arg_28_1):
	var_0_1.Share(arg_28_0)

def var_0_0.GetBiliServerId():
	local var_29_0 = var_0_1.serverId

	originalPrint("serverId . " .. var_29_0)

	return var_29_0

def var_0_0.GetChannelUID():
	local var_30_0 = var_0_1.channelUID

	originalPrint("channelUID . " .. var_30_0)

	return var_30_0

def var_0_0.GetLoginType():
	return var_0_1.loginType

def var_0_0.GetIsPlatform():
	return var_0_1.isPlatform

def var_0_0.GetPackageCode(arg_33_0):
	if arg_33_0 == var_0_2:
		return "2"
	elif arg_33_0 == var_0_3:
		return "1"
	elif arg_33_0 == var_0_4:
		return "3"

	return "0"

def var_0_0.QueryWithProduct():
	if var_0_2 == Application.identifier:
		return

	local var_34_0 = {}
	local var_34_1 = pg.pay_data_display

	for iter_34_0, iter_34_1 in pairs(var_34_1.all):
		local var_34_2 = var_34_1[iter_34_1]

		table.insert(var_34_0, var_34_2.id_str)

	var_0_1.Query(var_34_0)

def var_0_0.GetProduct(arg_35_0):
	return var_0_1.GetProduct(arg_35_0)

def StartSdkLogin():
	Timer.New(function()
		var_0_1.OnLoginTimeOut(), 30, 1).Start()

def GoLoginScene():
	if not pg.m02:
		originalPrint("game is not start")

		return

	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LOGIN)
	gcAll()

def SDKLogined(arg_39_0, arg_39_1, arg_39_2, arg_39_3):
	if not pg.m02:
		originalPrint("game is not start")

		return

	local var_39_0 = User.New({
		type = 1,
		arg1 = arg_39_0,
		arg2 = arg_39_1,
		arg3 = arg_39_2,
		arg4 = arg_39_3
	})

	pg.SdkMgr.GetInstance().airi_uid = arg_39_1 or "test"

	pg.m02.sendNotification(GAME.PLATFORM_LOGIN_DONE, {
		user = var_39_0
	})

def SDKLogouted(arg_40_0):
	if not pg.m02:
		originalPrint("game is not start")

		return

	pg.m02.sendNotification(GAME.LOGOUT, {
		code = arg_40_0
	})

def PaySuccess(arg_41_0, arg_41_1):
	if not pg.m02:
		originalPrint("game is not start")

		return

	getProxy(ShopsProxy).removeWaitTimer()
	originalPrint(arg_41_0 + " - " + arg_41_1)
	pg.m02.sendNotification(GAME.CHARGE_CONFIRM, {
		payId = arg_41_0,
		bsId = arg_41_1
	})

def PayFailed(arg_42_0, arg_42_1):
	if not pg.m02:
		originalPrint("game is not start")

		return

	getProxy(ShopsProxy).removeWaitTimer()

	arg_42_1 = tonumber(arg_42_1)

	if not arg_42_1:
		return

	pg.m02.sendNotification(GAME.CHARGE_FAILED, {
		payId = arg_42_0,
		code = arg_42_1
	})

def GetUserInfoSuccess():
	return

def GetUserInfoFailed():
	return

local function var_0_5(arg_45_0, arg_45_1, arg_45_2)
	if arg_45_0 == YongshiSdkUserBindInfo.FACEBOOK:
		pg.TipsMgr.GetInstance().ShowTips(arg_45_1 .. "facebook" .. arg_45_2)
	elif arg_45_0 == YongshiSdkUserBindInfo.APPLE:
		pg.TipsMgr.GetInstance().ShowTips(arg_45_1 .. "Apple Id" .. arg_45_2)
	elif arg_45_0 == YongshiSdkUserBindInfo.GOOGLE:
		pg.TipsMgr.GetInstance().ShowTips(arg_45_1 .. "google" .. arg_45_2)
	elif arg_45_0 == YongshiSdkUserBindInfo.PHONE:
		if arg_45_1 == "解綁":
			arg_45_1 = "换绑"

		pg.TipsMgr.GetInstance().ShowTips(arg_45_1 .. "手機" .. arg_45_2)
	else
		print("this platform is not supported")

def BindSuccess(arg_46_0):
	var_0_5(arg_46_0, "綁定", "成功")
	pg.m02.sendNotification(GAME.CHT_SOCIAL_LINK_STATE_CHANGE, arg_46_0)

def BindFailed(arg_47_0, arg_47_1):
	if arg_47_1 and arg_47_1 != "":
		pg.TipsMgr.GetInstance().ShowTips(arg_47_1)
	else
		var_0_5(arg_47_0, "綁定", "失敗")

def UnBindSuccess(arg_48_0):
	var_0_5(arg_48_0, "解綁", "成功")
	pg.m02.sendNotification(GAME.CHT_SOCIAL_LINK_STATE_CHANGE)

def UnBindFailed(arg_49_0, arg_49_1):
	if arg_49_1 and arg_49_1 != "":
		pg.TipsMgr.GetInstance().ShowTips(arg_49_1)
	else
		var_0_5(arg_49_0, "解綁", "失敗")

def OnDeepLinking(arg_50_0):
	pg.YongshiDeepLinkingMgr.GetInstance().SetData(arg_50_0)

return var_0_0
