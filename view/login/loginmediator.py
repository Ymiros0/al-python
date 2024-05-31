local var_0_0 = class("LoginMediator", import("..base.ContextMediator"))

var_0_0.ON_LOGIN = "LoginMediator.ON_LOGIN"
var_0_0.ON_REGISTER = "LoginMediator.ON_REGISTER"
var_0_0.ON_SERVER = "LoginMediator.ON_SERVER"
var_0_0.ON_LOGIN_PROCESS = "LoginMediator.ON_LOGIN_PROCESS"
var_0_0.ON_SEARCH_ACCOUNT = "LoginMediator.ON_SEARCH_ACCOUNT"
var_0_0.CHECK_RES = "LoginMediator.CHECK_RES"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_LOGIN, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.USER_LOGIN, arg_2_1))
	arg_1_0.bind(var_0_0.ON_REGISTER, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.USER_REGISTER, arg_3_1))
	arg_1_0.bind(var_0_0.ON_SERVER, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.SERVER_LOGIN, arg_4_1))
	arg_1_0.bind(var_0_0.ON_LOGIN_PROCESS, function(arg_5_0)
		if PLATFORM_CODE == PLATFORM_CHT and (CSharpVersion == 31 or CSharpVersion == 32 or CSharpVersion == 33 or CSharpVersion == 34):
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				modal = True,
				hideNo = True,
				content = "檢測到版本更新，需要手動下載更新包，是否前往下載？",
				hideClose = True,
				def onYes:()
					local var_6_0 = YongshiSdkMgr.inst.channelUID

					if var_6_0 == "0":
						Application.OpenURL("https.//play.google.com/store/apps/details?id=com.hkmanjuu.azurlane.gp")
					elif var_6_0 == "1":
						Application.OpenURL("https.//apps.apple.com/app/id1479022429")
					elif var_6_0 == "2":
						Application.OpenURL("http.//www.mygame.com.tw/MyGameAD/Accept.aspx?P=YAS3ZA2RSR&S=QUNRMMN7HY")

					Application.Quit(),
				def onClose:()
					Application.Quit()
			})
		else
			arg_1_0.loginProcessHandler())
	arg_1_0.bind(var_0_0.ON_SEARCH_ACCOUNT, function(arg_8_0, arg_8_1)
		arg_1_0.sendNotification(GAME.ACCOUNT_SEARCH, arg_8_1))
	arg_1_0.bind(var_0_0.CHECK_RES, function(arg_9_0)
		arg_1_0.checkPaintingRes())
	pg.SdkMgr.GetInstance().EnterLoginScene()

def var_0_0.remove(arg_10_0):
	pg.SdkMgr.GetInstance().ExitLoginScene()

def var_0_0.loginProcessHandler(arg_11_0):
	local var_11_0 = getProxy(SettingsProxy)
	local var_11_1 = pg.SdkMgr.GetInstance().GetLoginType()

	assert(var_11_1)

	arg_11_0.process = coroutine.wrap(function()
		arg_11_0.viewComponent.switchSubView({})

		if var_11_0.CheckNeedUserAgreement():
			arg_11_0.viewComponent.showUserAgreement(arg_11_0.process)
			coroutine.yield()
			var_11_0.SetUserAgreement()

		local var_12_0

		if var_11_1 == LoginType.PLATFORM:
			arg_11_0.viewComponent.switchToServer()
		elif var_11_1 == LoginType.PLATFORM_TENCENT:
			arg_11_0.viewComponent.switchToTencentLogin()
		elif var_11_1 == LoginType.PLATFORM_INNER:
			arg_11_0.viewComponent.switchToLogin()

			var_12_0 = getProxy(UserProxy).getLastLoginUser()

			arg_11_0.viewComponent.setLastLogin(var_12_0)
		elif var_11_1 == LoginType.PLATFORM_AIRIJP or var_11_1 == LoginType.PLATFORM_AIRIUS:
			arg_11_0.viewComponent.switchToAiriLogin()

		arg_11_0.CheckMaintain()

		if arg_11_0.contextData.code:
			if arg_11_0.contextData.code == 0 or arg_11_0.contextData.code == SDK_EXIT_CODE:
				-- block empty
			else
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					modal = True,
					hideNo = True,
					content = ({
						i18n("login_loginMediator_kickOtherLogin"),
						i18n("login_loginMediator_kickServerClose"),
						i18n("login_loginMediator_kickIntError"),
						i18n("login_loginMediator_kickTimeError"),
						i18n("login_loginMediator_kickLoginOut"),
						i18n("login_loginMediator_serverLoginErro"),
						i18n("login_loginMediator_vertifyFail"),
						[199] = i18n("login_loginMediator_dataExpired")
					})[arg_11_0.contextData.code] or i18n("login_loginMediator_kickUndefined", arg_11_0.contextData.code),
					def onYes:()
						arg_11_0.process()
				})
				coroutine.yield()

			if var_12_0:
				if var_12_0.type == 1:
					var_12_0.arg3 = ""
				elif var_12_0.type == 2:
					var_12_0.arg2 = ""

				arg_11_0.viewComponent.setLastLogin(var_12_0)
		else
			arg_11_0.viewComponent.setAutoLogin()

		if var_11_1 == LoginType.PLATFORM:
			pg.SdkMgr.GetInstance().LoginSdk()
		elif var_11_1 == LoginType.PLATFORM_TENCENT:
			pg.SdkMgr.GetInstance().TryLoginSdk()
		elif var_11_1 == LoginType.PLATFORM_INNER:
			-- block empty

		arg_11_0.viewComponent.autoLogin())

	arg_11_0.process()

def var_0_0.CheckMaintain(arg_14_0):
	ServerStateChecker.New().Execute(function(arg_15_0)
		if arg_15_0:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("login_loginMediator_kickServerClose"),
				def onNo:()
					arg_14_0.process(),
				def onYes:()
					arg_14_0.process()
			})
		else
			arg_14_0.process())
	coroutine.yield()

def var_0_0.listNotificationInterests(arg_18_0):
	return {
		GAME.USER_LOGIN_SUCCESS,
		GAME.USER_LOGIN_FAILED,
		GAME.USER_REGISTER_SUCCESS,
		GAME.USER_REGISTER_FAILED,
		GAME.SERVER_LOGIN_SUCCESS,
		GAME.SERVER_LOGIN_FAILED,
		GAME.LOAD_PLAYER_DATA_DONE,
		ServerProxy.SERVERS_UPDATED,
		GAME.PLATFORM_LOGIN_DONE,
		GAME.SERVER_LOGIN_WAIT,
		GAME.BEGIN_STAGE_DONE,
		GAME.SERVER_LOGIN_FAILED_USER_BANNED,
		GAME.ON_SOCIAL_LINKED
	}

def var_0_0.handleNotification(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_1.getName()
	local var_19_1 = arg_19_1.getBody()

	if var_19_0 == ServerProxy.SERVERS_UPDATED:
		arg_19_0.viewComponent.updateServerList(var_19_1)
	elif var_19_0 == GAME.USER_LOGIN_SUCCESS:
		pg.TipsMgr.GetInstance().ShowTips(i18n("login_loginMediator_loginSuccess"))

		local var_19_2 = getProxy(ServerProxy).getLastServer(var_19_1.id)

		arg_19_0.viewComponent.setLastLoginServer(var_19_2)
		arg_19_0.viewComponent.switchToServer()

		local var_19_3 = getProxy(UserProxy)

		if PLATFORM_CODE == PLATFORM_JP:
			arg_19_0.viewComponent.setUserData(var_19_3.getLastLoginUser())

		if #getProxy(GatewayNoticeProxy).getGatewayNotices(False) > 0:
			arg_19_0.addSubLayers(Context.New({
				mediator = GatewayNoticeMediator,
				viewComponent = GatewayNoticeLayer
			}))

		local var_19_4 = getProxy(UserProxy)

		if var_19_4.data.limitServerIds and #var_19_4.data.limitServerIds > 0:
			arg_19_0.viewComponent.fillterRefundServer()
			arg_19_0.viewComponent.setLastLoginServer(None)

		arg_19_0.viewComponent.switchGatewayBtn.Flush()
	elif var_19_0 == GAME.USER_REGISTER_SUCCESS:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			modal = True,
			hideNo = True,
			content = i18n("login_loginMediator_quest_RegisterSuccess"),
			def onYes:()
				arg_19_0.sendNotification(GAME.USER_LOGIN, var_19_1)
		})
	elif var_19_0 == GAME.SERVER_LOGIN_SUCCESS:
		if var_19_1.uid == 0:
			if EPILOGUE_SKIPPABLE:
				arg_19_0.sendNotification(GAME.GO_SCENE, SCENE.CREATE_PLAYER)
			else
				arg_19_0.sendNotification(GAME.BEGIN_STAGE, {
					system = SYSTEM_PROLOGUE
				})
		else
			arg_19_0.facade.sendNotification(GAME.LOAD_PLAYER_DATA, {
				id = var_19_1.uid
			})
	elif var_19_0 == GAME.USER_REGISTER_FAILED:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			modal = True,
			hideNo = True,
			content = errorTip("login_loginMediator_registerFail", var_19_1)
		})
	elif var_19_0 == GAME.USER_LOGIN_FAILED:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			modal = True,
			hideNo = True,
			content = errorTip("login_loginMediator_userLoginFail_error", var_19_1),
			def onYes:()
				local var_21_0 = pg.SdkMgr.GetInstance().GetLoginType()

				if var_19_1 == 20:
					arg_19_0.viewComponent.switchToRegister()
				elif var_19_1 == 3 or var_19_1 == 6:
					arg_19_0.viewComponent.switchToServer()
				elif var_19_1 == 1 or var_19_1 == 9 or var_19_1 == 11 or var_19_1 == 12:
					if var_21_0 == LoginType.PLATFORM_AIRIJP or var_21_0 == LoginType.PLATFORM_AIRIUS:
						arg_19_0.viewComponent.switchToAiriLogin()
					else
						arg_19_0.viewComponent.switchToLogin()
				elif var_21_0 == LoginType.PLATFORM or var_21_0 == LoginType.PLATFORM_TENCENT:
					arg_19_0.viewComponent.switchToServer()
				elif var_21_0 == LoginType.PLATFORM_AIRIJP or var_21_0 == LoginType.PLATFORM_AIRIUS:
					arg_19_0.viewComponent.switchToAiriLogin()
				else
					arg_19_0.viewComponent.switchToLogin()
		})
	elif var_19_0 == GAME.SERVER_LOGIN_FAILED:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			modal = True,
			hideNo = True,
			content = errorTip("login_loginMediator_serverLoginFail", var_19_1),
			def onYes:()
				local var_22_0 = pg.SdkMgr.GetInstance().GetLoginType()

				if var_22_0 == LoginType.PLATFORM or LoginType.PLATFORM_TENCENT:
					arg_19_0.viewComponent.switchToServer()
				elif var_22_0 == LoginType.PLATFORM_AIRIJP or var_22_0 == LoginType.PLATFORM_AIRIUS:
					arg_19_0.viewComponent.switchToAiriLogin()
				else
					arg_19_0.viewComponent.switchToLogin()
		})
	elif var_19_0 == GAME.LOAD_PLAYER_DATA_DONE:
		arg_19_0.checkPaintingRes()
	elif var_19_0 == GAME.BEGIN_STAGE_DONE:
		arg_19_0.viewComponent.unloadExtraVoice()
		arg_19_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_19_1)
	elif var_19_0 == GAME.PLATFORM_LOGIN_DONE:
		arg_19_0.sendNotification(GAME.USER_LOGIN, var_19_1.user)
	elif var_19_0 == GAME.SERVER_LOGIN_WAIT:
		arg_19_0.viewComponent.SwitchToWaitPanel(var_19_1)
	elif var_19_0 == GAME.SERVER_LOGIN_FAILED_USER_BANNED:
		if var_19_1 == 0:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = True,
				content = i18n("user_is_forever_banned")
			})
		else
			local var_19_5 = pg.TimeMgr.GetInstance().STimeDescS(var_19_1, "%Y-%m-%d %H.%M")

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = True,
				content = i18n("user_is_banned", var_19_5)
			})
	elif var_19_0 == GAME.ON_SOCIAL_LINKED:
		arg_19_0.viewComponent.closeYostarAlertView()

def var_0_0.checkPaintingRes(arg_23_0):
	local function var_23_0()
		arg_23_0.viewComponent.onLoadDataDone()

	local function var_23_1()
		arg_23_0.viewComponent.isNeedResCheck = True

	pg.FileDownloadMgr.GetInstance().SetRemind(False)

	local var_23_2 = PaintingGroupConst.GetPaintingNameListInLogin()
	local var_23_3 = {
		isShowBox = True,
		paintingNameList = var_23_2,
		finishFunc = var_23_0,
		onNo = var_23_1,
		onClose = var_23_1
	}

	PaintingGroupConst.PaintingDownload(var_23_3)

return var_0_0
