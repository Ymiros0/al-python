ys = {}
pg = {}
cs = {}
pg._weak = setmetatable({}, {
	__mode = "k"
})
PLATFORM_CH = 1
PLATFORM_JP = 2
PLATFORM_KR = 3
PLATFORM_US = 4
PLATFORM_CHT = 5
PLATFORM_CODE = PLATFORM_US
IsUnityEditor = UnityEngine.Application.isEditor

require("Include")
require("tolua.reflection")
tolua.loadassembly("Assembly-CSharp")
tolua.loadassembly("UnityEngine.UI")
math.randomseed(os.time())

CSharpVersion = NetConst.GatewayState

originalPrint("C# Ver... " .. CSharpVersion)

PLATFORM = LuaHelper.GetPlatformInt()
SDK_EXIT_CODE = 99

if not IsUnityEditor:
	function assert()
		return

QualitySettings.vSyncCount = 0

ReflectionHelp.RefSetField(typeof("ResourceMgr"), "_asyncMax", ResourceMgr.Inst, 30)

tf(GameObject.Find("EventSystem")).GetComponent(typeof(EventSystem)).sendNavigationEvents = False

if IsUnityEditor:
	function luaIdeDebugFunc()
		breakInfoFun = require("LuaDebugjit")("localhost", 7003)
		time = Timer.New(breakInfoFun, 0.5, -1, 1)

		time.Start()
		print("luaIdeDebugFunc")

if PLATFORM_CODE == PLATFORM_CHT and PLATFORM == 8:
	pg.SdkMgr.GetInstance().InitSDK()

pg.TimeMgr.GetInstance().Init()
pg.TimeMgr.GetInstance()._SetServerTime_(VersionMgr.Inst.timestamp, VersionMgr.Inst.monday0oclockTimestamp, VersionMgr.Inst.realStartUpTimeWhenSetServerTime)
pg.PushNotificationMgr.GetInstance().Init()

def OnApplicationPause(arg_3_0):
	originalPrint("OnApplicationPause. " .. tostring(arg_3_0))

	if not pg.m02:
		return

	if arg_3_0:
		pg.m02.sendNotification(GAME.PAUSE_BATTLE)
		pg.PushNotificationMgr.GetInstance().PushAll()
	else
		pg.SdkMgr.GetInstance().BindCPU()

	pg.SdkMgr.GetInstance().OnAppPauseForSDK(arg_3_0)
	pg.m02.sendNotification(GAME.ON_APPLICATION_PAUSE, arg_3_0)

def OnApplicationExit():
	originalPrint("OnApplicationExit")

	if pg.FileDownloadMgr.GetInstance().IsRunning():
		return

	if pg.NewStoryMgr.GetInstance().IsRunning():
		pg.NewStoryMgr.GetInstance().ForEscPress()

		return

	if pg.NewGuideMgr.GetInstance().IsBusy():
		return

	if pg.PerformMgr.GetInstance().IsRunning():
		return

	local var_4_0 = ys.Battle.BattleState.GetInstance()

	if var_4_0 and var_4_0.GetState() == var_4_0.BATTLE_STATE_FIGHT and not var_4_0.IsPause():
		pg.m02.sendNotification(GAME.PAUSE_BATTLE)

		return

	local var_4_1 = pg.UIMgr.GetInstance()

	if not var_4_1._loadPanel or var_4_1.LoadingRetainCount() != 0:
		return

	if pg.SceneAnimMgr.GetInstance().IsPlaying():
		return

	local var_4_2 = pg.MsgboxMgr.GetInstance()
	local var_4_3 = var_4_2 and var_4_2.getMsgBoxOb()
	local var_4_4 = pg.NewStoryMgr.GetInstance()

	if var_4_4 and var_4_4.IsRunning():
		if var_4_3 and var_4_3.activeSelf:
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
			triggerButton(var_4_2._closeBtn)

		return

	local var_4_5 = pg.m02

	if not var_4_5:
		return

	local var_4_6 = var_4_5.retrieveProxy(ContextProxy.__cname)

	if not var_4_6:
		return

	local var_4_7 = var_4_6.getCurrentContext()

	if not var_4_7:
		return

	local var_4_8 = pg.ShareMgr.GetInstance()

	if var_4_8.go and isActive(var_4_8.go):
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
		triggerButton(var_4_8.panel.Find("main/top/btnBack"))

		return

	local var_4_9 = var_4_7.retriveLastChild()
	local var_4_10 = var_4_5.retrieveMediator(var_4_9.mediator.__cname)

	if not var_4_10 or not var_4_10.viewComponent:
		return

	local var_4_11 = var_4_10.viewComponent
	local var_4_12 = var_4_11._tf.parent
	local var_4_13 = var_4_11._tf.GetSiblingIndex()
	local var_4_14 = -1
	local var_4_15

	if var_4_3 and var_4_3.activeSelf:
		var_4_15 = var_4_3.transform.parent
		var_4_14 = var_4_3.transform.GetSiblingIndex()

	if pg.playerResUI.checkBackPressed():
		return

	if var_4_12 == var_4_15 and var_4_14 < var_4_13:
		var_4_11.onBackPressed()

		return

	if var_4_3 and var_4_3.activeSelf:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
		triggerButton(var_4_2._closeBtn)

		return

	local var_4_16 = nowWorld()

	if var_4_16 and var_4_16.staminaMgr.IsShowing():
		var_4_16.staminaMgr.Hide()

		return

	var_4_11.onBackPressed()

def OnReceiveMemoryWarning():
	return

def PressBack():
	if not IsNil(pg.MsgboxMgr.GetInstance()._go):
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("confirm_app_exit"),
			def onYes:()
				Application.Quit()
		})

local function var_0_0(arg_8_0)
	parallelAsync({
		function(arg_9_0)
			pg.LayerWeightMgr.GetInstance().Init(arg_9_0),
		function(arg_10_0)
			pg.UIMgr.GetInstance().Init(arg_10_0),
		function(arg_11_0)
			pg.CriMgr.GetInstance().Init(arg_11_0)
	}, arg_8_0)

local function var_0_1(arg_12_0)
	parallelAsync({
		function(arg_13_0)
			pg.FontMgr.GetInstance().Init(arg_13_0),
		function(arg_14_0)
			pg.ShaderMgr.GetInstance().Init(arg_14_0),
		function(arg_15_0)
			pg.PoolMgr.GetInstance().Init(arg_15_0),
		function(arg_16_0)
			pg.TipsMgr.GetInstance().Init(arg_16_0),
		function(arg_17_0)
			pg.MsgboxMgr.GetInstance().Init(arg_17_0),
		function(arg_18_0)
			pg.SystemOpenMgr.GetInstance().Init(arg_18_0),
		function(arg_19_0)
			pg.SystemGuideMgr.GetInstance().Init(arg_19_0),
		function(arg_20_0)
			pg.NewGuideMgr.GetInstance().Init(arg_20_0),
		function(arg_21_0)
			pg.SeriesGuideMgr.GetInstance().Init(arg_21_0),
		function(arg_22_0)
			pg.ToastMgr.GetInstance().Init(arg_22_0),
		function(arg_23_0)
			pg.WorldToastMgr.GetInstance().Init(arg_23_0),
		function(arg_24_0)
			pg.SecondaryPWDMgr.GetInstance().Init(arg_24_0),
		function(arg_25_0)
			pg.ShipFlagMgr.GetInstance().Init(arg_25_0),
		function(arg_26_0)
			pg.NewStoryMgr.GetInstance().Init(arg_26_0),
		function(arg_27_0)
			pg.RedDotMgr.GetInstance().Init(arg_27_0),
		function(arg_28_0)
			pg.UserAgreementMgr.GetInstance().Init(arg_28_0),
		function(arg_29_0)
			pg.BrightnessMgr.GetInstance().Init(arg_29_0),
		function(arg_30_0)
			pg.ConfigTablePreloadMgr.GetInstance().Init(arg_30_0),
		function(arg_31_0)
			pg.CameraFixMgr.GetInstance().Init(arg_31_0),
		function(arg_32_0)
			pg.BgmMgr.GetInstance().Init(arg_32_0),
		function(arg_33_0)
			pg.FileDownloadMgr.GetInstance().Init(arg_33_0),
		function(arg_34_0)
			pg.RepairResMgr.GetInstance().Init(arg_34_0),
		function(arg_35_0)
			pg.NodeCanvasMgr.GetInstance().Init(arg_35_0),
		function(arg_36_0)
			pg.SceneAnimMgr.GetInstance().Init(arg_36_0),
		function(arg_37_0)
			pg.PerformMgr.GetInstance().Init(arg_37_0)
	}, arg_12_0)

local var_0_2 = os.clock()

seriesAsync({
	var_0_0,
	var_0_1
}, function(arg_38_0)
	pg.SdkMgr.GetInstance().QueryWithProduct()
	print("loading cost. " .. os.clock() - var_0_2)
	VersionMgr.Inst.DestroyUI()

	local var_38_0 = GameObject.Find("OverlayCamera/Overlay/UIMain/ServerChoosePanel")

	if not IsNil(var_38_0):
		Object.Destroy(var_38_0)

	Screen.sleepTimeout = SleepTimeout.SystemSetting

	pg.UIMgr.GetInstance().displayLoadingBG(True)
	pg.UIMgr.GetInstance().LoadingOn()

	if arg_38_0:
		pg.UIMgr.GetInstance().Loading(arg_38_0)
		error(arg_38_0)

		return

	pg.SdkMgr.GetInstance().BindCPU()

	pg.m02 = pm.Facade.getInstance("m02")

	pg.m02.registerCommand(GAME.STARTUP, StartupCommand)
	pg.m02.sendNotification(GAME.STARTUP)

	pg.playerResUI = PlayerResUI.New()

	pg.SdkMgr.GetInstance().GoSDkLoginScene())
