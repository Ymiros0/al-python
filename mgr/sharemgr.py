pg = pg or {}

local var_0_0 = pg

var_0_0.ShareMgr = singletonClass("ShareMgr")

local var_0_1 = var_0_0.ShareMgr

var_0_1.TypeAdmira = 1
var_0_1.TypeShipProfile = 2
var_0_1.TypeNewShip = 3
var_0_1.TypeBackyard = 4
var_0_1.TypeNewSkin = 5
var_0_1.TypeSummary = 6
var_0_1.TypePhoto = 7
var_0_1.TypeReflux = 8
var_0_1.TypeCommander = 9
var_0_1.TypeColoring = 10
var_0_1.TypeChallenge = 11
var_0_1.TypeInstagram = 12
var_0_1.TypePizzahut = 13
var_0_1.TypeSecondSummary = 14
var_0_1.TypePoraisMedals = 15
var_0_1.TypeIcecream = 16
var_0_1.TypeValentineQte = 17
var_0_1.TypeBossRushEX = 18
var_0_1.TypeTWCelebrationShare = 5000
var_0_1.TypeCardTower = 17
var_0_1.PANEL_TYPE_BLACK = 1
var_0_1.PANEL_TYPE_PINK = 2
var_0_1.ANCHORS_TYPE = {
	{
		0,
		0,
		0,
		0
	},
	{
		1,
		0,
		1,
		0
	},
	{
		0,
		1,
		0,
		1
	},
	{
		1,
		1,
		1,
		1
	},
	{
		0.5,
		0.5,
		0.5,
		0.5
	}
}

def var_0_1.Init(arg_1_0):
	PoolMgr.GetInstance().GetUI("ShareUI", False, function(arg_2_0)
		arg_1_0.go = arg_2_0

		arg_1_0.go.SetActive(False)

		arg_1_0.tr = arg_2_0.transform
		arg_1_0.panelBlack = arg_1_0.tr.Find("panel")
		arg_1_0.panelPink = arg_1_0.tr.Find("panel_pink")
		arg_1_0.deckTF = arg_1_0.tr.Find("deck")

		setActive(arg_1_0.panelBlack, False)
		setActive(arg_1_0.panelPink, False)

		arg_1_0.logo = arg_1_0.tr.Find("deck/logo")

		GetComponent(arg_1_0.logo, "Image").SetNativeSize())

	arg_1_0.screenshot = Application.persistentDataPath .. "/screen_scratch/last_picture_for_share.jpg"
	arg_1_0.cacheComps = {}
	arg_1_0.cacheShowComps = {}
	arg_1_0.cacheMoveComps = {}

def var_0_1.Share(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if PLATFORM_CODE == PLATFORM_CHT and not CheckPermissionGranted(ANDROID_WRITE_EXTERNAL_PERMISSION):
		var_0_0.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n1("指揮官，碧藍航線需要存儲權限才能分享是否打開？"),
			def onYes:()
				ApplyPermission({
					ANDROID_WRITE_EXTERNAL_PERMISSION
				})
		})

		return

	local var_3_0 = LuaHelper.GetCHPackageType()

	if not IsUnityEditor and PLATFORM_CODE == PLATFORM_CH and var_3_0 != PACKAGE_TYPE_BILI:
		var_0_0.TipsMgr.GetInstance().ShowTips("指挥官，当前平台不支持分享功能哦")

		return

	if IsNil(arg_3_0.go):
		arg_3_0.Init()

	arg_3_2 = arg_3_2 or var_0_1.PANEL_TYPE_BLACK

	if arg_3_2 == var_0_1.PANEL_TYPE_BLACK:
		arg_3_0.panel = arg_3_0.panelBlack
	elif arg_3_2 == var_0_1.PANEL_TYPE_PINK:
		arg_3_0.panel = arg_3_0.panelPink

	setActive(arg_3_0.panelBlack, arg_3_2 == var_0_1.PANEL_TYPE_BLACK)
	setActive(arg_3_0.panelPink, arg_3_2 == var_0_1.PANEL_TYPE_PINK)

	local var_3_1 = var_0_0.share_template[arg_3_1]

	assert(var_3_1, "share_template not exist. " .. arg_3_1)

	local var_3_2 = getProxy(PlayerProxy).getRawData()
	local var_3_3 = getProxy(UserProxy).getRawData()
	local var_3_4 = getProxy(ServerProxy).getRawData()[var_3_3 and var_3_3.server or 0]
	local var_3_5 = var_3_2 and var_3_2.name or ""
	local var_3_6 = var_3_4 and var_3_4.name or ""
	local var_3_7 = arg_3_0.deckTF
	local var_3_8 = arg_3_0.ANCHORS_TYPE[var_3_1.deck] or {
		0.5,
		0.5,
		0.5,
		0.5
	}

	var_3_7.anchorMin = Vector2(var_3_8[1], var_3_8[2])
	var_3_7.anchorMax = Vector2(var_3_8[3], var_3_8[4])

	setText(var_3_7.Find("name/value"), var_3_5)
	setText(var_3_7.Find("server/value"), var_3_6)
	setText(var_3_7.Find("lv/value"), var_3_2.level)

	if PLATFORM_CODE == PLATFORM_CHT or PLATFORM_CODE == PLATFORM_CH:
		setActive(var_3_7.Find("code_bg"), True)
	else
		setActive(var_3_7.Find("code_bg"), False)

	local var_3_9 = GameObject.Find(var_3_1.camera).GetComponent(typeof(Camera))
	local var_3_10 = var_3_9.transform.GetChild(0)

	var_3_7.anchoredPosition3D = Vector3(var_3_1.qrcode_location[1], var_3_1.qrcode_location[2], -100)
	var_3_7.anchoredPosition = Vector2(var_3_1.qrcode_location[1], var_3_1.qrcode_location[2])

	_.each(var_3_1.hidden_comps, function(arg_5_0)
		local var_5_0 = GameObject.Find(arg_5_0)

		if not IsNil(var_5_0) and var_5_0.activeSelf:
			table.insert(arg_3_0.cacheComps, var_5_0)
			var_5_0.SetActive(False))
	_.each(var_3_1.show_comps, function(arg_6_0)
		local var_6_0 = GameObject.Find(arg_6_0)

		if not IsNil(var_6_0) and not var_6_0.activeSelf:
			table.insert(arg_3_0.cacheShowComps, var_6_0)
			var_6_0.SetActive(True))
	_.each(var_3_1.move_comps, function(arg_7_0)
		local var_7_0 = GameObject.Find(arg_7_0.path)

		if not IsNil(var_7_0):
			local var_7_1 = var_7_0.transform.anchoredPosition.x
			local var_7_2 = var_7_0.transform.anchoredPosition.y
			local var_7_3 = arg_7_0.x
			local var_7_4 = arg_7_0.y

			table.insert(arg_3_0.cacheMoveComps, {
				var_7_0,
				var_7_1,
				var_7_2
			})
			setAnchoredPosition(var_7_0, {
				x = var_7_3,
				y = var_7_4
			}))
	SetParent(var_3_7, var_3_10, False)
	var_3_7.SetAsLastSibling()

	local var_3_11 = ScreenShooter.New(Screen.width, Screen.height, TextureFormat.ARGB32)

	if (PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US) and var_0_0.SdkMgr.GetInstance().GetIsPlatform():
		local var_3_12 = arg_3_0.TakeTexture(arg_3_1, var_3_11, var_3_9)

		var_0_0.SdkMgr.GetInstance().GameShare(var_3_1.description, var_3_12)
		var_0_0.UIMgr.GetInstance().LoadingOn()
		onDelayTick(function()
			var_0_0.UIMgr.GetInstance().LoadingOff(), 2)
	elif PLATFORM_CODE == PLATFORM_CHT:
		arg_3_0.TakePhoto(arg_3_1, var_3_11, var_3_9)
		var_0_0.SdkMgr.GetInstance().ShareImg(arg_3_0.screenshot, function()
			return)
	elif PLATFORM_CODE == PLATFORM_CH and var_3_0 == PACKAGE_TYPE_BILI:
		if arg_3_0.TakePhoto(arg_3_1, var_3_11, var_3_9):
			var_0_0.SdkMgr.GetInstance().GameShare(var_3_1.description, arg_3_0.screenshot)
	elif arg_3_0.TakePhoto(arg_3_1, var_3_11, var_3_9):
		print("截图位置. " .. arg_3_0.screenshot)
		arg_3_0.Show(var_3_1, arg_3_3)
	elif PLATFORM_CODE == PLATFORM_CHT:
		var_0_0.TipsMgr.GetInstance().ShowTips("截圖失敗")
	else
		var_0_0.TipsMgr.GetInstance().ShowTips("截图失败")

	SetParent(var_3_7, arg_3_0.tr, False)
	_.each(arg_3_0.cacheComps, function(arg_10_0)
		arg_10_0.SetActive(True))

	arg_3_0.cacheComps = {}

	_.each(arg_3_0.cacheShowComps, function(arg_11_0)
		arg_11_0.SetActive(False))

	arg_3_0.cacheShowComps = {}

	_.each(arg_3_0.cacheMoveComps, function(arg_12_0)
		setAnchoredPosition(arg_12_0[1], {
			x = arg_12_0[2],
			y = arg_12_0[3]
		}))

	arg_3_0.cacheMoveComps = {}

def var_0_1.TakeTexture(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	if arg_13_1 == var_0_1.TypeValentineQte:
		local var_13_0 = System.Collections.Generic.List_UnityEngine_Camera()
		local var_13_1 = GameObject.Find("UICamera").GetComponent(typeof(Camera))
		local var_13_2 = GameObject.Find("OverlayCamera").GetComponent(typeof(Camera))

		var_13_0.Add(var_13_1)
		var_13_0.Add(var_13_2)

		local var_13_3 = arg_13_2.TakePhotoMultiCam(var_13_0)

		return (arg_13_2.EncodeToJPG(var_13_3))
	else
		local var_13_4 = arg_13_2.TakePhoto(arg_13_3)

		return (arg_13_2.EncodeToJPG(var_13_4))

def var_0_1.TakePhoto(arg_14_0, arg_14_1, arg_14_2, arg_14_3):
	if arg_14_1 == var_0_1.TypeValentineQte:
		local var_14_0 = System.Collections.Generic.List_UnityEngine_Camera()
		local var_14_1 = GameObject.Find("UICamera").GetComponent(typeof(Camera))
		local var_14_2 = GameObject.Find("OverlayCamera").GetComponent(typeof(Camera))

		var_14_0.Add(var_14_1)
		var_14_0.Add(var_14_2)

		return arg_14_2.TakeMultiCam(var_14_0, arg_14_0.screenshot)
	else
		return arg_14_2.Take(arg_14_3, arg_14_0.screenshot)

def var_0_1.Show(arg_15_0, arg_15_1, arg_15_2):
	arg_15_0.go.SetActive(True)
	var_0_0.UIMgr.GetInstance().BlurPanel(arg_15_0.panel, True, arg_15_2)
	var_0_0.DelegateInfo.New(arg_15_0)

	local function var_15_0()
		arg_15_0.go.SetActive(False)
		var_0_0.UIMgr.GetInstance().UnblurPanel(arg_15_0.panel, arg_15_0.tr)
		PoolMgr.GetInstance().ReturnUI("ShareUI", arg_15_0.go)
		var_0_0.DelegateInfo.Dispose(arg_15_0)

		arg_15_0.go = None
		arg_15_0.tr = None
		arg_15_0.panel = None

	onButton(arg_15_0, arg_15_0.panel.Find("main/top/btnBack"), var_15_0)
	onButton(arg_15_0, arg_15_0.panel.Find("main/buttons/weibo"), function()
		var_15_0())
	onButton(arg_15_0, arg_15_0.panel.Find("main/buttons/weixin"), function()
		var_15_0())

	if PLATFORM_CODE == PLATFORM_KR:
		onButton(arg_15_0, arg_15_0.panel.Find("main/buttons/facebook"), function()
			var_0_0.SdkMgr.GetInstance().ShareImg(arg_15_0.screenshot, function(arg_20_0, arg_20_1)
				if arg_20_0 and arg_20_1 == 0:
					var_0_0.TipsMgr.GetInstance().ShowTips(i18n("share_success")))
			var_15_0())
