local var_0_0 = class("WorldScene", import("..base.BaseUI"))

var_0_0.SceneOp = "WorldScene.SceneOp"
var_0_0.Listeners = {
	onAchievementAchieved = "OnAchievementAchieved",
	onUpdateEventTips = "OnUpdateEventTips",
	onSelectFleet = "OnSelectFleet",
	onUpdateSubmarineSupport = "OnUpdateSubmarineSupport",
	onClearMoveQueue = "ClearMoveQueue",
	onModelSelectMap = "OnModelSelectMap",
	onUpdateDaily = "OnUpdateDaily",
	onUpdateProgress = "OnUpdateProgress",
	onUpdateScale = "OnUpdateScale",
	onUpdateRound = "OnUpdateRound",
	onDisposeMap = "OnDisposeMap",
	onFleetSelected = "OnFleetSelected"
}
var_0_0.optionsPath = {
	"top/adapt/top_chapter/option",
	"top/adapt/top_stage/option"
}

def var_0_0.forceGC(arg_1_0):
	return True

def var_0_0.getUIName(arg_2_0):
	return "WorldUI"

def var_0_0.getBGM(arg_3_0):
	local var_3_0 = {}

	if arg_3_0.GetInMap() == False:
		-- block empty
	else
		table.insert(var_3_0, nowWorld().GetActiveMap().GetBGM() or "")

	for iter_3_0, iter_3_1 in ipairs(var_3_0):
		if iter_3_1 != "":
			return iter_3_1

	return var_0_0.super.getBGM(arg_3_0)

def var_0_0.init(arg_4_0):
	for iter_4_0, iter_4_1 in pairs(var_0_0.Listeners):
		arg_4_0[iter_4_0] = function(...)
			var_0_0[iter_4_1](arg_4_0, ...)

	arg_4_0.bind(var_0_0.SceneOp, function(arg_6_0, ...)
		arg_4_0.Op(...))

	local var_4_0 = pg.UIMgr.GetInstance()

	arg_4_0.camera = var_4_0.levelCamera.GetComponent(typeof(Camera))
	arg_4_0.rtUIMain = var_4_0.LevelMain

	setActive(arg_4_0.rtUIMain, False)

	arg_4_0.rtGrid = arg_4_0.rtUIMain.Find("LevelGrid")

	setActive(arg_4_0.rtGrid, True)

	arg_4_0.rtDragLayer = arg_4_0.rtGrid.Find("DragLayer")
	arg_4_0.rtEnvBG = arg_4_0._tf.Find("main/bg")
	arg_4_0.rtTop = arg_4_0._tf.Find("top")
	arg_4_0.rtTopAtlas = arg_4_0.rtTop.Find("adapt/top_chapter")

	setActive(arg_4_0.rtTopAtlas, False)

	arg_4_0.rtRightAtlas = arg_4_0.rtTop.Find("adapt/right_chapter")

	setActive(arg_4_0.rtRightAtlas, False)

	arg_4_0.rtBottomAtlas = arg_4_0.rtTop.Find("adapt/bottom_chapter")

	setActive(arg_4_0.rtBottomAtlas, False)

	arg_4_0.rtTransportAtlas = arg_4_0.rtTop.Find("transport_chapter")

	setActive(arg_4_0.rtTransportAtlas, False)

	arg_4_0.rtTopMap = arg_4_0.rtTop.Find("adapt/top_stage")

	setActive(arg_4_0.rtTopMap, False)

	arg_4_0.rtLeftMap = arg_4_0.rtTop.Find("adapt/left_stage")

	setActive(arg_4_0.rtLeftMap, False)

	arg_4_0.rtRightMap = arg_4_0.rtTop.Find("adapt/right_stage")

	setActive(arg_4_0.rtRightMap, False)

	arg_4_0.rtOutMap = arg_4_0.rtTop.Find("effect_stage")

	setActive(arg_4_0.rtOutMap, False)

	arg_4_0.rtClickStop = arg_4_0.rtTop.Find("stop_click")

	onButton(arg_4_0, arg_4_0.rtClickStop.Find("long_move"), function()
		if #arg_4_0.moveQueue > 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_fleet_stop"))
			arg_4_0.ClearMoveQueue())
	onButton(arg_4_0, arg_4_0.rtClickStop.Find("auto_fight"), function()
		local var_8_0 = nowWorld()

		if var_8_0.isAutoFight:
			pg.TipsMgr.GetInstance().ShowTips(i18n("autofight_tip_bigworld_stop"))
			var_8_0.TriggerAutoFight(False)
		else
			assert(False, "stop clicker shouldn't active"))
	setActive(arg_4_0.rtClickStop, False)

	arg_4_0.resAtlas = WorldResource.New()

	arg_4_0.resAtlas.setParent(arg_4_0.rtTopAtlas.Find("resources"), False)

	arg_4_0.resMap = WorldResource.New()

	arg_4_0.resMap.setParent(arg_4_0.rtTopMap.Find("resources"), False)

	arg_4_0.wsPool = WSPool.New()

	arg_4_0.wsPool.Setup(arg_4_0.findTF("resources"))

	arg_4_0.wsAnim = WSAnim.New()

	arg_4_0.wsAnim.Setup()

	arg_4_0.wsTimer = WSTimer.New()

	arg_4_0.wsTimer.Setup()

	arg_4_0.wsDragProxy = WSDragProxy.New()
	arg_4_0.wsDragProxy.transform = arg_4_0.rtDragLayer
	arg_4_0.wsDragProxy.wsTimer = arg_4_0.wsTimer

	arg_4_0.wsDragProxy.Setup({
		def clickCall:(arg_9_0, arg_9_1)
			if arg_4_0.svScannerPanel.isShowing():
				local var_9_0, var_9_1 = arg_4_0.CheckScannerEnable(arg_4_0.ScreenPos2MapPos(arg_9_1.position))

				if var_9_0:
					arg_4_0.svScannerPanel.ActionInvoke("DisplayWindow", var_9_0, var_9_1)
				else
					arg_4_0.svScannerPanel.ActionInvoke("HideWindow")
			else
				arg_4_0.OnClickMap(arg_4_0.ScreenPos2MapPos(arg_9_1.position)),
		def longPressCall:()
			arg_4_0.OnLongPressMap(arg_4_0.ScreenPos2MapPos(Vector3(Input.mousePosition.x, Input.mousePosition.y)))
	})

	arg_4_0.wsMapCamera = WSMapCamera.New()
	arg_4_0.wsMapCamera.camera = arg_4_0.camera

	arg_4_0.wsMapCamera.Setup()
	arg_4_0.InitSubView()
	arg_4_0.AddWorldListener()

	arg_4_0.moveQueue = {}
	arg_4_0.achievedList = {}
	arg_4_0.mapOps = {}
	arg_4_0.wsCommands = {}

	WSCommand.Bind(arg_4_0)
	arg_4_0.OpOpen()

def var_0_0.InitSubView(arg_11_0):
	arg_11_0.rtPanelList = arg_11_0.findTF("panel_list")
	arg_11_0.svOrderPanel = SVOrderPanel.New(arg_11_0.rtPanelList, arg_11_0.event, {
		wsPool = arg_11_0.wsPool
	})
	arg_11_0.svScannerPanel = SVScannerPanel.New(arg_11_0.rtPanelList, arg_11_0.event)

	arg_11_0.bind(SVScannerPanel.ShowView, function(arg_12_0)
		arg_11_0.wsMap.ShowScannerMap(True)
		setActive(arg_11_0.wsMap.rtTop, False)
		arg_11_0.HideMapUI())
	arg_11_0.bind(SVScannerPanel.HideView, function(arg_13_0)
		arg_11_0.wsMap.ShowScannerMap(False)
		setActive(arg_11_0.wsMap.rtTop, True)
		arg_11_0.DisplayMapUI())
	arg_11_0.bind(SVScannerPanel.HideGoing, function(arg_14_0, arg_14_1, arg_14_2)
		arg_11_0.wsMap.ShowScannerMap(False)
		setActive(arg_11_0.wsMap.rtTop, True)
		arg_11_0.DisplayMapUI()
		arg_11_0.OnClickCell(arg_14_1, arg_14_2))

	arg_11_0.svRealmPanel = SVRealmPanel.New(arg_11_0.rtPanelList, arg_11_0.event)
	arg_11_0.svAchievement = SVAchievement.New(arg_11_0.rtPanelList, arg_11_0.event)

	arg_11_0.bind(SVAchievement.HideView, function(arg_15_0)
		table.remove(arg_11_0.achievedList, 1)

		return (#arg_11_0.achievedList > 0 and function()
			arg_11_0.ShowSubView("Achievement", arg_11_0.achievedList[1]) or function()
			arg_11_0.Op("OpInteractive"))())

	arg_11_0.svDebugPanel = SVDebugPanel.New(arg_11_0.rtPanelList, arg_11_0.event)
	arg_11_0.svFloatPanel = SVFloatPanel.New(arg_11_0.rtTop, arg_11_0.event)

	arg_11_0.bind(SVFloatPanel.ReturnCall, function(arg_18_0, arg_18_1)
		arg_11_0.Op("OpCall", function(arg_19_0)
			arg_19_0()

			local var_19_0 = nowWorld().GetActiveEntrance()

			if arg_18_1.id == var_19_0.id:
				arg_11_0.wsAtlas.UpdateSelect()
				arg_11_0.wsAtlas.UpdateSelect(arg_18_1)
			else
				arg_11_0.ClickAtlas(var_19_0)))

	arg_11_0.svPoisonPanel = SVPoisonPanel.New(arg_11_0.rtPanelList, arg_11_0.event)
	arg_11_0.svGlobalBuff = SVGlobalBuff.New(arg_11_0.rtPanelList, arg_11_0.event)

	arg_11_0.bind(SVGlobalBuff.HideView, function(arg_20_0, arg_20_1)
		return existCall(arg_20_1))

	arg_11_0.svBossProgress = SVBossProgress.New(arg_11_0.rtPanelList, arg_11_0.event)

	arg_11_0.bind(SVBossProgress.HideView, function(arg_21_0, arg_21_1)
		return existCall(arg_21_1))

	arg_11_0.svSalvageResult = SVSalvageResult.New(arg_11_0.rtPanelList, arg_11_0.event)

def var_0_0.didEnter(arg_22_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_22_0.rtTop)

	arg_22_0.warningSairen = not arg_22_0.contextData.inSave

	if arg_22_0.contextData.inWorld:
		arg_22_0.Op("OpSetInMap", False, function()
			arg_22_0.wsAtlas.UpdateSelect(nowWorld().GetActiveEntrance()))
	else
		arg_22_0.Op("OpSetInMap", True)

def var_0_0.onBackPressed(arg_24_0):
	if arg_24_0.inCutIn:
		return
	elif arg_24_0.svDebugPanel.isShowing():
		arg_24_0.HideSubView("DebugPanel")
	elif arg_24_0.svAchievement.isShowing():
		arg_24_0.HideSubView("Achievement")
	elif arg_24_0.svGlobalBuff.isShowing():
		arg_24_0.HideSubView("GlobalBuff")
	elif arg_24_0.svBossProgress.isShowing():
		arg_24_0.HideSubView("BossProgress")
	elif arg_24_0.svOrderPanel.isShowing():
		arg_24_0.HideSubView("OrderPanel")
	elif arg_24_0.svScannerPanel.isShowing():
		arg_24_0.HideSubView("ScannerPanel")
	elif arg_24_0.svPoisonPanel.isShowing():
		arg_24_0.HideSubView("PoisonPanel")
	elif arg_24_0.svSalvageResult.isShowing():
		arg_24_0.HideSubView("SalvageResult")
	elif arg_24_0.wsMapLeft and isActive(arg_24_0.wsMapLeft.toggleMask):
		arg_24_0.wsMapLeft.HideToggleMask()
	elif arg_24_0.GetInMap():
		triggerButton(arg_24_0.wsMapTop.btnBack)
	else
		triggerButton(arg_24_0.rtTopAtlas.Find("back_button"))

def var_0_0.quickExitFunc(arg_25_0):
	arg_25_0.Op("OpCall", function(arg_26_0)
		arg_26_0()

		local var_26_0 = {}

		if nowWorld().CheckReset():
			table.insert(var_26_0, function(arg_27_0)
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("world_recycle_notice"),
					onYes = arg_27_0
				}))

		seriesAsync(var_26_0, function()
			var_0_0.super.quickExitFunc(arg_25_0)))

def var_0_0.ExitWorld(arg_29_0, arg_29_1, arg_29_2):
	local var_29_0 = {}

	if not arg_29_2:
		table.insert(var_29_0, function(arg_30_0)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("world_exit_tip"),
				onYes = arg_30_0,
				def onNo:()
					return existCall(arg_29_1)
			}))

	if not arg_29_2 and nowWorld().CheckReset():
		table.insert(var_29_0, function(arg_32_0)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("world_recycle_notice"),
				onYes = arg_32_0,
				def onNo:()
					return existCall(arg_29_1)
			}))

	table.insert(var_29_0, function(arg_34_0)
		if arg_29_0.GetInMap():
			arg_29_0.EaseOutMapUI(arg_34_0)
		else
			arg_29_0.EaseOutAtlasUI(arg_34_0))
	seriesAsync(var_29_0, function()
		existCall(arg_29_1)
		arg_29_0.closeView())

def var_0_0.SaveState(arg_36_0):
	arg_36_0.contextData.inSave = True
	arg_36_0.contextData.inWorld = arg_36_0.GetInMap() == False
	arg_36_0.contextData.inShop = False
	arg_36_0.contextData.inPort = False

def var_0_0.willExit(arg_37_0):
	arg_37_0.SaveState()
	arg_37_0.RemoveWorldListener()
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_37_0.rtTop, arg_37_0._tf)
	arg_37_0.svOrderPanel.Destroy()
	arg_37_0.svScannerPanel.Destroy()
	arg_37_0.svAchievement.Destroy()
	arg_37_0.svRealmPanel.Destroy()
	arg_37_0.svDebugPanel.Destroy()
	arg_37_0.svFloatPanel.Destroy()
	arg_37_0.svPoisonPanel.Destroy()
	arg_37_0.svGlobalBuff.Destroy()
	arg_37_0.svBossProgress.Destroy()
	arg_37_0.DisposeAtlas()
	arg_37_0.DisposeAtlasUI()
	arg_37_0.DisposeMap()
	arg_37_0.DisposeMapUI()
	arg_37_0.wsPool.Dispose()

	arg_37_0.wsPool = None

	arg_37_0.wsAnim.Dispose()

	arg_37_0.wsAnim = None

	arg_37_0.wsTimer.Dispose()

	arg_37_0.wsTimer = None

	arg_37_0.wsDragProxy.Dispose()

	arg_37_0.wsDragProxy = None

	arg_37_0.wsMapCamera.Dispose()

	arg_37_0.wsMapCamera = None

	arg_37_0.resAtlas.exit()

	arg_37_0.resAtlas = None

	arg_37_0.resMap.exit()

	arg_37_0.resMap = None

	arg_37_0.VerifyMapOp()
	arg_37_0.OpDispose()
	WSCommand.Unbind(arg_37_0)
	WBank.Recycle(WorldMapOp)

def var_0_0.SetPlayer(arg_38_0, arg_38_1):
	arg_38_0.player = arg_38_1

	arg_38_0.resAtlas.setPlayer(arg_38_0.player)
	arg_38_0.resMap.setPlayer(arg_38_0.player)

def var_0_0.AddWorldListener(arg_39_0):
	local var_39_0 = nowWorld()

	var_39_0.AddListener(World.EventUpdateProgress, arg_39_0.onUpdateProgress)
	var_39_0.GetTaskProxy().AddListener(WorldTaskProxy.EventUpdateDailyTaskIds, arg_39_0.onUpdateDaily)

def var_0_0.RemoveWorldListener(arg_40_0):
	local var_40_0 = nowWorld()

	var_40_0.RemoveListener(World.EventUpdateProgress, arg_40_0.onUpdateProgress)
	var_40_0.GetTaskProxy().RemoveListener(WorldTaskProxy.EventUpdateDailyTaskIds, arg_40_0.onUpdateDaily)

def var_0_0.SetInMap(arg_41_0, arg_41_1, arg_41_2):
	if arg_41_1:
		arg_41_2 = defaultValue(arg_41_2, function()
			arg_41_0.Op("OpInteractive"))

	if arg_41_0.inMap == arg_41_1:
		return existCall(arg_41_2)

	local var_41_0 = {}
	local var_41_1 = {}

	arg_41_0.StopAnim()

	if arg_41_0.inMap:
		table.insert(var_41_0, function(arg_43_0)
			arg_41_0.Op("OpSwitchOutMap", arg_43_0))
	elif arg_41_0.inMap != None:
		table.insert(var_41_0, function(arg_44_0)
			arg_41_0.Op("OpSwitchOutWorld", arg_44_0))

	table.insert(var_41_0, function(arg_45_0)
		arg_41_0.Op("OpCall", function(arg_46_0)
			parallelAsync(var_41_1, function()
				arg_46_0()

				return arg_45_0())))
	table.insert(var_41_1, function(arg_48_0)
		arg_41_0.DisplayEnv(arg_48_0))

	if arg_41_1:
		table.insert(var_41_1, function(arg_49_0)
			arg_41_0.LoadMap(nowWorld().GetActiveMap(), arg_49_0))
		table.insert(var_41_0, function(arg_50_0)
			arg_41_0.Op("OpSwitchInMap", arg_50_0))
	else
		table.insert(var_41_1, function(arg_51_0)
			arg_41_0.LoadAtlas(arg_51_0))
		table.insert(var_41_0, function(arg_52_0)
			arg_41_0.Op("OpSwitchInWorld", arg_52_0))

	table.insert(var_41_0, function(arg_53_0)
		arg_41_0.PlayBGM()
		arg_53_0())

	arg_41_0.inMap = arg_41_1

	seriesAsync(var_41_0, arg_41_2)

def var_0_0.GetInMap(arg_54_0):
	return arg_54_0.inMap

def var_0_0.ShowSubView(arg_55_0, arg_55_1, arg_55_2, arg_55_3):
	local var_55_0 = arg_55_0["sv" .. arg_55_1]

	var_55_0.Load()
	var_55_0.ActionInvoke("Setup", unpack(arg_55_2 or {}))
	var_55_0.ActionInvoke("Show", unpack(arg_55_3 or {}))

def var_0_0.HideSubView(arg_56_0, arg_56_1, ...):
	arg_56_0["sv" .. arg_56_1].ActionInvoke("Hide", ...)

def var_0_0.DisplayAtlasUI(arg_57_0):
	arg_57_0.DisplayAtlasTop()
	arg_57_0.DisplayAtlasRight()
	arg_57_0.DisplayAtlasBottom()
	arg_57_0.UpdateSystemOpen()

def var_0_0.HideAtlasUI(arg_58_0):
	arg_58_0.HideAtlasTop()
	arg_58_0.HideAtlasRight()
	arg_58_0.HideAtlasBottom()

def var_0_0.EaseInAtlasUI(arg_59_0, arg_59_1):
	arg_59_0.CancelAtlasUITween()
	parallelAsync({
		function(arg_60_0)
			setAnchoredPosition(arg_59_0.rtTopAtlas, {
				y = arg_59_0.rtTopAtlas.rect.height
			})
			arg_59_0.wsTimer.AddTween(LeanTween.moveY(arg_59_0.rtTopAtlas, 0, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeInSine).setOnComplete(System.Action(arg_60_0)).uniqueId),
		function(arg_61_0)
			setAnchoredPosition(arg_59_0.rtBottomAtlas, {
				y = -arg_59_0.rtBottomAtlas.rect.height
			})
			arg_59_0.wsTimer.AddTween(LeanTween.moveY(arg_59_0.rtBottomAtlas, 0, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeInSine).setOnComplete(System.Action(arg_61_0)).uniqueId),
		function(arg_62_0)
			setAnchoredPosition(arg_59_0.rtRightAtlas, {
				x = arg_59_0.rtRightAtlas.rect.width
			})
			arg_59_0.wsTimer.AddTween(LeanTween.moveX(arg_59_0.rtRightAtlas, 0, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeInSine).setOnComplete(System.Action(arg_62_0)).uniqueId)
	}, function()
		return existCall(arg_59_1))

def var_0_0.EaseOutAtlasUI(arg_64_0, arg_64_1):
	arg_64_0.CancelAtlasUITween()
	parallelAsync({
		function(arg_65_0)
			setAnchoredPosition(arg_64_0.rtTopAtlas, {
				y = 0
			})
			arg_64_0.wsTimer.AddTween(LeanTween.moveY(arg_64_0.rtTopAtlas, arg_64_0.rtTopAtlas.rect.height, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeOutSine).setOnComplete(System.Action(arg_65_0)).uniqueId),
		function(arg_66_0)
			setAnchoredPosition(arg_64_0.rtBottomAtlas, {
				y = 0
			})
			arg_64_0.wsTimer.AddTween(LeanTween.moveY(arg_64_0.rtBottomAtlas, -arg_64_0.rtBottomAtlas.rect.height, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeOutSine).setOnComplete(System.Action(arg_66_0)).uniqueId),
		function(arg_67_0)
			setAnchoredPosition(arg_64_0.rtRightAtlas, {
				x = 0
			})
			arg_64_0.wsTimer.AddTween(LeanTween.moveX(arg_64_0.rtRightAtlas, arg_64_0.rtRightAtlas.rect.width, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeOutSine).setOnComplete(System.Action(arg_67_0)).uniqueId)
	}, function()
		return existCall(arg_64_1))

def var_0_0.CancelAtlasUITween(arg_69_0):
	LeanTween.cancel(go(arg_69_0.rtTransportAtlas))
	LeanTween.cancel(go(arg_69_0.rtTopAtlas))
	LeanTween.cancel(go(arg_69_0.rtBottomAtlas))
	LeanTween.cancel(go(arg_69_0.rtRightAtlas))

def var_0_0.DisposeAtlasUI(arg_70_0):
	arg_70_0.HideAtlasUI()
	arg_70_0.DisposeAtlasTransport()
	arg_70_0.DisposeAtlasTop()
	arg_70_0.DisposeAtlasRight()
	arg_70_0.DisposeAtlasBottom()

def var_0_0.DisplayAtlas(arg_71_0):
	local var_71_0 = nowWorld().GetActiveEntrance()

	arg_71_0.wsAtlas.SwitchArea(var_71_0.GetAreaId())
	arg_71_0.wsAtlas.UpdateActiveMark()
	arg_71_0.wsAtlas.ShowOrHide(True)

def var_0_0.HideAtlas(arg_72_0):
	arg_72_0.wsAtlas.UpdateSelect()
	arg_72_0.wsAtlas.ShowOrHide(False)

def var_0_0.ClickAtlas(arg_73_0, arg_73_1):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL)

	local var_73_0 = arg_73_1.GetAreaId()

	if not nowWorld().CheckAreaUnlock(var_73_0):
		pg.TipsMgr.GetInstance().ShowTips(i18n("area_lock"))

		return

	if arg_73_0.wsAtlas.nowArea:
		arg_73_0.wsAtlas.UpdateSelect()

		if arg_73_0.wsAtlas.selectEntrance != arg_73_1:
			arg_73_0.wsAtlas.UpdateSelect(arg_73_1)
	else
		arg_73_0.EnterToModelMap(var_73_0)

def var_0_0.LoadAtlas(arg_74_0, arg_74_1):
	local var_74_0 = {}

	if not arg_74_0.wsAtlas:
		table.insert(var_74_0, function(arg_75_0)
			arg_74_0.wsAtlas = arg_74_0.NewAtlas()

			arg_74_0.wsAtlas.LoadScene(function()
				arg_74_0.wsAtlas.AddListener(WSAtlasWorld.EventUpdateselectEntrance, arg_74_0.onModelSelectMap)
				arg_74_0.wsAtlas.UpdateAtlas(nowWorld().GetAtlas())

				return arg_75_0()))

	seriesAsync(var_74_0, arg_74_1)

def var_0_0.NewAtlas(arg_77_0):
	local var_77_0 = WSAtlasWorld.New()

	var_77_0.wsTimer = arg_77_0.wsTimer

	function var_77_0.onClickColor(arg_78_0, arg_78_1)
		if arg_77_0.wsAtlas.CheckIsTweening():
			return

		arg_77_0.Op("OpCall", function(arg_79_0)
			arg_79_0()
			arg_77_0.ClickAtlas(arg_78_0))

	var_77_0.Setup()

	return var_77_0

def var_0_0.DisposeAtlas(arg_80_0):
	if arg_80_0.wsAtlas:
		arg_80_0.HideAtlas()
		arg_80_0.wsAtlas.RemoveListener(WSAtlasWorld.EventUpdateselectEntrance, arg_80_0.onModelSelectMap)
		arg_80_0.wsAtlas.Dispose()

		arg_80_0.wsAtlas = None

def var_0_0.DisplayAtlasTop(arg_81_0):
	arg_81_0.wsAtlasTop = arg_81_0.wsAtlasTop or arg_81_0.NewAtlasTop(arg_81_0.rtTopAtlas)

	setActive(arg_81_0.rtTopAtlas, True)
	setActive(arg_81_0.rtTopAtlas.Find("print/title_world"), True)
	setActive(arg_81_0.rtTopAtlas.Find("print/title_view"), False)
	setActive(arg_81_0.rtTopAtlas.Find("sairen_warning"), arg_81_0.warningSairen and #nowWorld().GetAtlas().sairenEntranceList > 0)

	arg_81_0.warningSairen = False

def var_0_0.HideAtlasTop(arg_82_0):
	setActive(arg_82_0.rtTopAtlas, False)

def var_0_0.NewAtlasTop(arg_83_0, arg_83_1):
	local var_83_0 = {
		transform = arg_83_1
	}

	onButton(arg_83_0, arg_83_1.Find("back_button"), function()
		arg_83_0.Op("OpCall", function(arg_85_0)
			arg_85_0()
			arg_83_0.BackToMap()), SFX_CANCEL)

	return var_83_0

def var_0_0.DisposeAtlasTop(arg_86_0):
	arg_86_0.wsAtlasTop = None

def var_0_0.DisplayAtlasRight(arg_87_0):
	arg_87_0.wsAtlasRight = arg_87_0.wsAtlasRight or arg_87_0.NewAtlasRight(arg_87_0.rtRightAtlas)

	arg_87_0.wsAtlasRight.SetOverSize(arg_87_0.rtTop.Find("adapt").offsetMax.x)
	setActive(arg_87_0.rtRightAtlas, True)

def var_0_0.HideAtlasRight(arg_88_0):
	setActive(arg_88_0.rtRightAtlas, False)

def var_0_0.NewAtlasRight(arg_89_0, arg_89_1, arg_89_2):
	local var_89_0 = WSAtlasRight.New()

	var_89_0.transform = arg_89_1

	var_89_0.Setup()
	onButton(arg_89_0, var_89_0.btnSettings, function()
		arg_89_0.Op("OpOpenScene", SCENE.SETTINGS, {
			scroll = "world_settings",
			page = NewSettingsScene.PAGE_OPTION
		}), SFX_PANEL)
	onButton(arg_89_0, var_89_0.btnSwitch, function()
		arg_89_0.Op("OpOpenLayer", Context.New({
			mediator = WorldSwitchPlanningMediator,
			viewComponent = WorldSwitchPlanningLayer
		})), SFX_CONFIRM)

	return var_89_0

def var_0_0.DisposeAtlasRight(arg_92_0):
	if arg_92_0.wsAtlasRight:
		arg_92_0.wsAtlasRight.Dispose()

		arg_92_0.wsAtlasRight = None

def var_0_0.DisplayAtlasBottom(arg_93_0):
	arg_93_0.wsAtlasBottom = arg_93_0.wsAtlasBottom or arg_93_0.NewAtlasBottom(arg_93_0.rtBottomAtlas)

	arg_93_0.wsAtlasBottom.SetOverSize(arg_93_0.rtTop.Find("adapt").offsetMax.x)
	arg_93_0.wsAtlasBottom.UpdateScale(1)
	setActive(arg_93_0.rtBottomAtlas, True)
	setActive(arg_93_0.wsAtlasBottom.btnDailyTask.Find("tip"), nowWorld().GetTaskProxy().canAcceptDailyTask())

def var_0_0.HideAtlasBottom(arg_94_0):
	setActive(arg_94_0.rtBottomAtlas, False)

def var_0_0.NewAtlasBottom(arg_95_0, arg_95_1):
	local var_95_0 = WSAtlasBottom.New()

	var_95_0.transform = arg_95_1
	var_95_0.wsTimer = arg_95_0.wsTimer

	var_95_0.Setup()

	if CAMERA_MOVE_OPEN:
		var_95_0.AddListener(WSAtlasBottom.EventUpdateScale, arg_95_0.onUpdateScale)

	onButton(arg_95_0, var_95_0.btnOverview, function()
		if arg_95_0.wsAtlas.CheckIsTweening():
			return

		arg_95_0.Op("OpCall", function(arg_97_0)
			arg_95_0.wsAtlas.LoadModel(function()
				arg_97_0()
				arg_95_0.ReturnToModelArea())), SFX_PANEL)
	onButton(arg_95_0, var_95_0.btnBoss, function()
		if nowWorld().GetBossProxy().IsOpen():
			arg_95_0.Op("OpOpenScene", SCENE.WORLDBOSS)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end")), SFX_PANEL)
	onButton(arg_95_0, var_95_0.btnShop, function()
		arg_95_0.Op("OpOpenLayer", Context.New({
			mediator = WorldShopMediator,
			viewComponent = WorldShopLayer
		})), SFX_PANEL)
	onButton(arg_95_0, var_95_0.btnCollection, function()
		arg_95_0.Op("OpOpenScene", SCENE.WORLD_COLLECTION, {
			page = WorldMediaCollectionScene.PAGE_RECORD
		}), SFX_PANEL)
	onButton(arg_95_0, var_95_0.btnDailyTask, function()
		local var_102_0 = nowWorld()

		if var_102_0.IsSystemOpen(WorldConst.SystemDailyTask):
			var_102_0.GetTaskProxy().checkDailyTask(function()
				arg_95_0.Op("OpOpenLayer", Context.New({
					mediator = WorldDailyTaskMediator,
					viewComponent = WorldDailyTaskLayer
				})))
		else
			pg.TipsMgr.GetInstance(i18n("world_daily_task_lock")), SFX_PANEL)

	return var_95_0

def var_0_0.DisposeAtlasBottom(arg_104_0):
	if arg_104_0.wsAtlasBottom:
		arg_104_0.wsAtlasBottom.Dispose()

		arg_104_0.wsAtlasBottom = None

def var_0_0.DisplayAtlasTransport(arg_105_0):
	arg_105_0.wsAtlasTransport = arg_105_0.wsAtlasTransport or arg_105_0.NewAtlasTransport(arg_105_0.rtTransportAtlas)

	setActive(arg_105_0.rtTransportAtlas, True)

def var_0_0.HideAtlasTransport(arg_106_0):
	setActive(arg_106_0.rtTransportAtlas, False)

def var_0_0.NewAtlasTransport(arg_107_0, arg_107_1):
	local var_107_0 = {
		transform = arg_107_1,
		btnBack = arg_107_1.Find("adapt/btn_back")
	}

	onButton(arg_107_0, var_107_0.btnBack, function()
		assert(arg_107_0.inTransportMode, "this isn't transport mode atlas")
		arg_107_0.BackToMap(), SFX_CANCEL)

	return var_107_0

def var_0_0.DisposeAtlasTransport(arg_109_0):
	arg_109_0.wsAtlasTransport = None

def var_0_0.DisplayMapUI(arg_110_0):
	arg_110_0.DisplayMapTop()
	arg_110_0.DisplayMapLeft()
	arg_110_0.DisplayMapRight()
	arg_110_0.DisplayMapOut()
	arg_110_0.UpdateSystemOpen()

def var_0_0.HideMapUI(arg_111_0):
	arg_111_0.HideMapTop()
	arg_111_0.HideMapLeft()
	arg_111_0.HideMapRight()
	arg_111_0.HideMapOut()

def var_0_0.UpdateMapUI(arg_112_0):
	local var_112_0 = nowWorld()
	local var_112_1 = var_112_0.GetActiveEntrance()
	local var_112_2 = var_112_0.GetActiveMap()

	arg_112_0.wsMapTop.Update(var_112_1, var_112_2)
	arg_112_0.wsMapLeft.UpdateMap(var_112_2)
	arg_112_0.wsMapRight.Update(var_112_1, var_112_2)
	arg_112_0.wsMapOut.UpdateMap(var_112_2)

def var_0_0.EaseInMapUI(arg_113_0, arg_113_1):
	arg_113_0.CancelMapUITween()
	parallelAsync({
		function(arg_114_0)
			setAnchoredPosition(arg_113_0.rtTopMap, {
				y = arg_113_0.rtTopMap.rect.height
			})
			arg_113_0.wsTimer.AddTween(LeanTween.moveY(arg_113_0.rtTopMap, 0, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeInSine).setOnComplete(System.Action(arg_114_0)).uniqueId),
		function(arg_115_0)
			setAnchoredPosition(arg_113_0.rtLeftMap, {
				x = -arg_113_0.rtLeftMap.rect.width
			})
			arg_113_0.wsTimer.AddTween(LeanTween.moveX(arg_113_0.rtLeftMap, 0, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeInSine).setOnComplete(System.Action(arg_115_0)).uniqueId),
		function(arg_116_0)
			setAnchoredPosition(arg_113_0.rtRightMap, {
				x = arg_113_0.rtRightMap.rect.width
			})
			arg_113_0.wsTimer.AddTween(LeanTween.moveX(arg_113_0.rtRightMap, 0, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeInSine).setOnComplete(System.Action(arg_116_0)).uniqueId)
	}, function()
		return existCall(arg_113_1))

def var_0_0.EaseOutMapUI(arg_118_0, arg_118_1):
	arg_118_0.CancelMapUITween()
	parallelAsync({
		function(arg_119_0)
			setAnchoredPosition(arg_118_0.rtTopMap, {
				y = 0
			})
			arg_118_0.wsTimer.AddTween(LeanTween.moveY(arg_118_0.rtTopMap, arg_118_0.rtTopMap.rect.height, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeOutSine).setOnComplete(System.Action(arg_119_0)).uniqueId),
		function(arg_120_0)
			setAnchoredPosition(arg_118_0.rtLeftMap, {
				x = 0
			})
			arg_118_0.wsTimer.AddTween(LeanTween.moveX(arg_118_0.rtLeftMap, -arg_118_0.rtLeftMap.rect.width, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeOutSine).setOnComplete(System.Action(arg_120_0)).uniqueId),
		function(arg_121_0)
			setAnchoredPosition(arg_118_0.rtRightMap, {
				x = 0
			})
			arg_118_0.wsTimer.AddTween(LeanTween.moveX(arg_118_0.rtRightMap, arg_118_0.rtRightMap.rect.width, WorldConst.UIEaseFasterDuration).setEase(LeanTweenType.easeOutSine).setOnComplete(System.Action(arg_121_0)).uniqueId)
	}, function()
		return existCall(arg_118_1))

def var_0_0.CancelMapUITween(arg_123_0):
	LeanTween.cancel(go(arg_123_0.rtTopMap))
	LeanTween.cancel(go(arg_123_0.rtLeftMap))
	LeanTween.cancel(go(arg_123_0.rtRightMap))

def var_0_0.DisposeMapUI(arg_124_0):
	arg_124_0.DisposeMapTop()
	arg_124_0.DisposeMapLeft()
	arg_124_0.DisposeMapRight()
	arg_124_0.DisposeMapOut()

def var_0_0.DisplayMap(arg_125_0):
	setActive(arg_125_0.rtUIMain, True)

def var_0_0.HideMap(arg_126_0):
	setActive(arg_126_0.rtUIMain, False)

def var_0_0.ShowMargin(arg_127_0, arg_127_1):
	if arg_127_0.wsMap:
		arg_127_0.wsMap.UpdateTransportDisplay(arg_127_1)

def var_0_0.LoadMap(arg_128_0, arg_128_1, arg_128_2):
	assert(arg_128_1, "target map not exist.")

	local var_128_0 = {}

	if not arg_128_1.IsValid():
		table.insert(var_128_0, function(arg_129_0)
			arg_128_0.emit(WorldMediator.OnMapReq, arg_128_1.id, arg_129_0))

	seriesAsync(var_128_0, function()
		if arg_128_0.wsMap:
			return existCall(arg_128_2)
		else
			arg_128_1.AddListener(WorldMap.EventUpdateActive, arg_128_0.onDisposeMap)
			arg_128_1.AddListener(WorldMap.EventUpdateMoveSpeed, arg_128_0.onClearMoveQueue)

			arg_128_0.wsMap = arg_128_0.NewMap(arg_128_1)

			arg_128_0.wsMap.Load(function()
				arg_128_0.wsMap.transform.SetParent(arg_128_0.rtDragLayer, False)
				setActive(arg_128_0.wsMap.transform, True)
				arg_128_0.InitMap()

				return existCall(arg_128_2)))

def var_0_0.InitMap(arg_132_0):
	for iter_132_0, iter_132_1 in ipairs(arg_132_0.wsMap.wsMapFleets):
		onButton(arg_132_0, iter_132_1.rtRetreat, function()
			arg_132_0.Op("OpReqRetreat", iter_132_1.fleet), SFX_PANEL)
		iter_132_1.AddListener(WSMapFleet.EventUpdateSelected, arg_132_0.onFleetSelected)

	arg_132_0.wsMap.AddListener(WSMap.EventUpdateEventTips, arg_132_0.onUpdateEventTips)

	local var_132_0 = nowWorld()

	var_132_0.AddListener(World.EventUpdateSubmarineSupport, arg_132_0.onUpdateSubmarineSupport)
	var_132_0.AddListener(World.EventAchieved, arg_132_0.onAchievementAchieved)

	local var_132_1 = arg_132_0.wsMap.map

	arg_132_0.wsDragProxy.UpdateMap(var_132_1)
	arg_132_0.wsDragProxy.Focus(arg_132_0.wsMap.GetFleet().transform.position)
	arg_132_0.wsMapCamera.UpdateMap(var_132_1)
	arg_132_0.OnUpdateSubmarineSupport()

def var_0_0.NewMap(arg_134_0, arg_134_1):
	local var_134_0 = WSMap.New()

	var_134_0.wsPool = arg_134_0.wsPool
	var_134_0.wsTimer = arg_134_0.wsTimer

	var_134_0.Setup(arg_134_1)

	arg_134_0.rtGrid.localEulerAngles = Vector3(arg_134_1.theme.angle, 0, 0)

	return var_134_0

def var_0_0.DisposeMap(arg_135_0):
	if arg_135_0.wsMap:
		arg_135_0.wsTimer.ClearInMapTimers()
		arg_135_0.wsTimer.ClearInMapTweens()
		arg_135_0.HideMap()

		local var_135_0 = nowWorld()

		var_135_0.RemoveListener(World.EventUpdateSubmarineSupport, arg_135_0.onUpdateSubmarineSupport)
		var_135_0.RemoveListener(World.EventAchieved, arg_135_0.onAchievementAchieved)

		local var_135_1 = arg_135_0.wsMap.map

		var_135_1.RemoveListener(WorldMap.EventUpdateActive, arg_135_0.onDisposeMap)
		var_135_1.RemoveListener(WorldMap.EventUpdateMoveSpeed, arg_135_0.onClearMoveQueue)
		arg_135_0.wsMap.Dispose()

		arg_135_0.wsMap = None

def var_0_0.OnDisposeMap(arg_136_0, arg_136_1, arg_136_2):
	local var_136_0 = False

	if arg_136_1 == WorldMap.EventUpdateActive:
		var_136_0 = not arg_136_2.active

	if var_136_0:
		arg_136_0.DisposeMap()

def var_0_0.DisplayMapTop(arg_137_0):
	arg_137_0.wsMapTop = arg_137_0.wsMapTop or arg_137_0.NewMapTop(arg_137_0.rtTopMap)

	setActive(arg_137_0.rtTopMap, True)

def var_0_0.HideMapTop(arg_138_0):
	setActive(arg_138_0.rtTopMap, False)

def var_0_0.NewMapTop(arg_139_0, arg_139_1):
	local var_139_0 = WSMapTop.New()

	var_139_0.transform = arg_139_1

	var_139_0.Setup()

	function var_139_0.cmdSkillFunc(arg_140_0)
		arg_139_0.emit(WorldMediator.OnOpenLayer, Context.New({
			mediator = CommanderSkillMediator,
			viewComponent = CommanderSkillLayer,
			data = {
				isWorld = True,
				skill = arg_140_0
			}
		}))

	function var_139_0.poisonFunc(arg_141_0)
		arg_139_0.ShowSubView("PoisonPanel", {
			arg_141_0
		})

	onButton(arg_139_0, var_139_0.btnBack, function()
		arg_139_0.Op("OpCall", function(arg_143_0)
			arg_139_0.ExitWorld(arg_143_0)), SFX_CANCEL)

	return var_139_0

def var_0_0.DisposeMapTop(arg_144_0):
	if arg_144_0.wsMapTop:
		arg_144_0.HideMapTop()
		arg_144_0.wsMapTop.Dispose()

		arg_144_0.wsMapTop = None

def var_0_0.DisplayMapLeft(arg_145_0):
	arg_145_0.wsMapLeft = arg_145_0.wsMapLeft or arg_145_0.NewMapLeft(arg_145_0.rtLeftMap)

	setActive(arg_145_0.rtLeftMap, True)

def var_0_0.HideMapLeft(arg_146_0):
	setActive(arg_146_0.rtLeftMap, False)

def var_0_0.NewMapLeft(arg_147_0, arg_147_1):
	local var_147_0 = WSMapLeft.New()

	var_147_0.transform = arg_147_1

	var_147_0.Setup()

	function var_147_0.onAgonyClick()
		arg_147_0.Op("OpOpenLayer", Context.New({
			mediator = WorldInventoryMediator,
			viewComponent = WorldInventoryLayer,
			data = {
				currentFleetIndex = nowWorld().GetActiveMap().findex
			}
		}))

	function var_147_0.onLongPress(arg_149_0)
		local var_149_0 = nowWorld().GetFleet(arg_149_0.fleetId).GetShipVOs(True)

		arg_147_0.Op("OpOpenScene", SCENE.SHIPINFO, {
			shipId = arg_149_0.id,
			shipVOs = var_149_0
		})

	function var_147_0.onClickSalvage(arg_150_0)
		arg_147_0.Op("OpCall", function(arg_151_0)
			arg_151_0()
			arg_147_0.ShowSubView("SalvageResult", {
				arg_150_0
			}))

	var_147_0.AddListener(WSMapLeft.EventSelectFleet, arg_147_0.onSelectFleet)

	return var_147_0

def var_0_0.DisposeMapLeft(arg_152_0):
	if arg_152_0.wsMapLeft:
		arg_152_0.HideMapLeft()
		arg_152_0.wsMapLeft.RemoveListener(WSMapLeft.EventSelectFleet, arg_152_0.onSelectFleet)
		arg_152_0.wsMapLeft.Dispose()

		arg_152_0.wsMapLeft = None

def var_0_0.DisplayMapRight(arg_153_0):
	arg_153_0.wsMapRight = arg_153_0.wsMapRight or arg_153_0.NewMapRight(arg_153_0.rtRightMap)

	setActive(arg_153_0.rtRightMap, True)
	arg_153_0.UpdateAutoFightDisplay()
	arg_153_0.UpdateAutoSwitchDisplay()

def var_0_0.HideMapRight(arg_154_0):
	setActive(arg_154_0.rtRightMap, False)

def var_0_0.HideMapRightCompass(arg_155_0):
	return

def var_0_0.HideMapRightMemo(arg_156_0):
	return

def var_0_0.NewMapRight(arg_157_0, arg_157_1):
	local var_157_0 = WSMapRight.New()

	var_157_0.transform = arg_157_1
	var_157_0.wsPool = arg_157_0.wsPool
	var_157_0.wsTimer = arg_157_0.wsTimer

	var_157_0.Setup()
	var_157_0.OnUpdateInfoBtnTip()
	var_157_0.OnUpdateHelpBtnTip()
	onButton(arg_157_0, var_157_0.btnOrder, function()
		arg_157_0.Op("OpShowOrderPanel"), SFX_PANEL)
	onButton(arg_157_0, var_157_0.btnScan, function()
		arg_157_0.Op("OpShowScannerPanel"), SFX_PANEL)
	onButton(arg_157_0, var_157_0.btnDefeat, function()
		var_157_0.OnUpdateHelpBtnTip(True)
		arg_157_0.Op("OpOpenLayer", Context.New({
			mediator = WorldHelpMediator,
			viewComponent = WorldHelpLayer,
			data = {
				titleId = 4,
				pageId = 5
			}
		})), SFX_PANEL)
	onButton(arg_157_0, var_157_0.btnDetail, function()
		arg_157_0.Op("OpOpenLayer", Context.New({
			mediator = WorldDetailMediator,
			viewComponent = WorldDetailLayer,
			data = {
				fleetId = nowWorld().GetActiveMap().GetFleet().id
			}
		})), SFX_PANEL)
	onButton(arg_157_0, var_157_0.btnInformation, function()
		arg_157_0.Op("OpOpenLayer", Context.New({
			mediator = WorldInformationMediator,
			viewComponent = WorldInformationLayer,
			data = {
				fleetId = nowWorld().GetActiveMap().GetFleet().id
			}
		})), SFX_PANEL)
	onButton(arg_157_0, var_157_0.btnInventory, function()
		arg_157_0.Op("OpOpenLayer", Context.New({
			mediator = WorldInventoryMediator,
			viewComponent = WorldInventoryLayer,
			data = {
				currentFleetIndex = nowWorld().GetActiveMap().findex
			}
		})), SFX_PANEL)
	onButton(arg_157_0, var_157_0.btnTransport, function()
		arg_157_0.OnClickTransport(), SFX_PANEL)
	onButton(arg_157_0, var_157_0.btnPort, function()
		local var_165_0 = nowWorld().GetActiveMap()
		local var_165_1 = var_165_0.GetFleet()

		if var_165_0.GetCell(var_165_1.row, var_165_1.column).ExistEnemy():
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_port_inbattle"))

			return

		arg_157_0.Op("OpReqEnterPort"), SFX_PANEL)
	onButton(arg_157_0, var_157_0.btnExit, function()
		local var_166_0 = nowWorld().GetActiveMap()
		local var_166_1 = {}

		if var_166_0.CheckFleetSalvage(True):
			table.insert(var_166_1, function(arg_167_0)
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("world_catsearch_leavemap"),
					onYes = arg_167_0
				}))

		seriesAsync(var_166_1, function()
			arg_157_0.Op("OpReqJumpOut", var_166_0.gid)), SFX_PANEL)
	onButton(arg_157_0, var_157_0.btnHelp, function()
		var_157_0.OnUpdateHelpBtnTip(True)
		arg_157_0.Op("OpOpenLayer", Context.New({
			mediator = WorldHelpMediator,
			viewComponent = WorldHelpLayer
		})), SFX_PANEL)
	onButton(arg_157_0, var_157_0.toggleAutoFight.Find("off"), function()
		arg_157_0.Op("OpCall", function(arg_171_0)
			arg_171_0()

			local var_171_0 = {}

			if PlayerPrefs.GetInt("first_auto_fight_mark", 0) == 0:
				table.insert(var_171_0, function(arg_172_0)
					PlayerPrefs.SetInt("first_auto_fight_mark", 1)
					arg_157_0.Op("OpOpenLayer", Context.New({
						mediator = WorldHelpMediator,
						viewComponent = WorldHelpLayer,
						data = {
							titleId = 2,
							pageId = 8
						},
						onRemoved = arg_172_0
					})))

			local var_171_1 = nowWorld()

			if var_171_1.IsSystemOpen(WorldConst.SystemOrderSubmarine) and PlayerPrefs.GetInt("world_sub_auto_call", 0) == 1 and var_171_1.GetActiveMap().GetConfig("instruction_available")[1] == 1 and var_171_1.CanCallSubmarineSupport() and not var_171_1.IsSubmarineSupporting():
				local var_171_2 = var_171_1.CalcOrderCost(WorldConst.OpReqSub)

				if var_171_2 <= PlayerPrefs.GetInt("world_sub_call_line", 0) and var_171_2 <= var_171_1.staminaMgr.GetTotalStamina():
					if var_171_2 > 0:
						table.insert(var_171_0, function(arg_173_0)
							pg.MsgboxMgr.GetInstance().ShowMsgBox({
								content = i18n("world_instruction_submarine_2", setColorStr(var_171_2, COLOR_GREEN)),
								def onYes:()
									PlayerPrefs.SetInt("autoSubIsAcitve" .. AutoSubCommand.GetAutoSubMark(SYSTEM_WORLD), 1)
									arg_157_0.Op("OpReqSub", arg_173_0),
								onNo = arg_173_0
							}))
					else
						PlayerPrefs.SetInt("autoSubIsAcitve" .. AutoSubCommand.GetAutoSubMark(SYSTEM_WORLD), 1)
						table.insert(var_171_0, function(arg_175_0)
							arg_157_0.Op("OpReqSub", arg_175_0))

			seriesAsync(var_171_0, function()
				pg.TipsMgr.GetInstance().ShowTips(i18n("autofight_tip_bigworld_begin"))
				getProxy(MetaCharacterProxy).setMetaTacticsInfoOnStart()
				PlayerPrefs.SetInt("world_skip_precombat", 1)
				PlayerPrefs.SetInt("autoBotIsAcitve" .. AutoBotCommand.GetAutoBotMark(SYSTEM_WORLD), 1)
				var_171_1.TriggerAutoFight(True)
				arg_157_0.Op("OpInteractive"))), SFX_PANEL)
	onButton(arg_157_0, var_157_0.toggleAutoFight.Find("on"), function()
		arg_157_0.Op("OpCall", function(arg_178_0)
			arg_178_0()
			nowWorld().TriggerAutoFight(False)
			arg_157_0.Op("OpInteractive")), SFX_PANEL)
	onButton(arg_157_0, var_157_0.toggleAutoSwitch.Find("off"), function()
		arg_157_0.Op("OpOpenLayer", Context.New({
			mediator = WorldSwitchPlanningMediator,
			viewComponent = WorldSwitchPlanningLayer
		})), SFX_PANEL)
	onButton(arg_157_0, var_157_0.toggleAutoSwitch.Find("on"), function()
		arg_157_0.Op("OpCall", function(arg_181_0)
			arg_181_0()
			nowWorld().TriggerAutoFight(False)
			arg_157_0.Op("OpInteractive")), SFX_PANEL)

	return var_157_0

def var_0_0.DisposeMapRight(arg_182_0):
	if arg_182_0.wsMapRight:
		arg_182_0.HideMapRight()
		arg_182_0.wsMapRight.Dispose()

		arg_182_0.wsMapRight = None

def var_0_0.DisplayMapOut(arg_183_0):
	arg_183_0.wsMapOut = arg_183_0.wsMapOut or arg_183_0.NewMapOut(arg_183_0.rtOutMap)

	setActive(arg_183_0.rtOutMap, True)

def var_0_0.HideMapOut(arg_184_0):
	setActive(arg_184_0.rtOutMap, False)

def var_0_0.NewMapOut(arg_185_0, arg_185_1):
	local var_185_0 = WSMapOut.New()

	var_185_0.transform = arg_185_1

	var_185_0.Setup()

	return var_185_0

def var_0_0.DisposeMapOut(arg_186_0):
	if arg_186_0.wsMapOut:
		arg_186_0.HideMapOut()
		arg_186_0.wsMapOut.Dispose()

		arg_186_0.wsMapOut = None

def var_0_0.OnUpdateProgress(arg_187_0, arg_187_1, arg_187_2, arg_187_3, arg_187_4):
	arg_187_0.UpdateSystemOpen()

	if arg_187_0.wsMapRight:
		arg_187_0.wsMapRight.OnUpdateHelpBtnTip()

def var_0_0.OnUpdateScale(arg_188_0, arg_188_1, arg_188_2, arg_188_3):
	if arg_188_0.wsAtlas and not arg_188_0.wsAtlasBottom.CheckIsTweening():
		arg_188_0.wsAtlas.UpdateScale(arg_188_3)

def var_0_0.OnModelSelectMap(arg_189_0, arg_189_1, arg_189_2, arg_189_3, arg_189_4, arg_189_5):
	if arg_189_3:
		arg_189_0.ShowSubView("FloatPanel", {
			arg_189_3,
			arg_189_4,
			arg_189_5,
			arg_189_2
		})
	else
		arg_189_0.HideSubView("FloatPanel")

def var_0_0.OnUpdateSubmarineSupport(arg_190_0, arg_190_1):
	arg_190_0.wsMap.UpdateSubmarineSupport()

	if arg_190_0.wsMapLeft:
		arg_190_0.wsMapLeft.OnUpdateSubmarineSupport()

def var_0_0.OnUpdateDaily(arg_191_0):
	if arg_191_0.wsAtlasBottom:
		setActive(arg_191_0.wsAtlasBottom.btnDailyTask.Find("tip"), nowWorld().GetTaskProxy().canAcceptDailyTask())

def var_0_0.OnFleetSelected(arg_192_0, arg_192_1, arg_192_2):
	if arg_192_2.selected:
		arg_192_0.wsDragProxy.Focus(arg_192_2.transform.position, None, LeanTweenType.easeInOutSine)

def var_0_0.OnSelectFleet(arg_193_0, arg_193_1, arg_193_2, arg_193_3):
	if arg_193_3 == nowWorld().GetActiveMap().GetFleet():
		arg_193_0.Op("OpMoveCamera", 0, 0.1)
	else
		arg_193_0.Op("OpReqSwitchFleet", arg_193_3)

def var_0_0.OnClickCell(arg_194_0, arg_194_1, arg_194_2):
	local var_194_0 = nowWorld().GetActiveMap()
	local var_194_1 = var_194_0.GetFleet()
	local var_194_2 = var_194_0.GetCell(arg_194_1, arg_194_2)
	local var_194_3 = var_194_0.FindFleet(var_194_2.row, var_194_2.column)

	if var_194_3 and var_194_3 != var_194_1:
		arg_194_0.Op("OpReqSwitchFleet", var_194_3)
	elif var_194_0.CheckInteractive():
		arg_194_0.Op("OpInteractive", True)
	elif var_194_0.IsSign(arg_194_1, arg_194_2) and ManhattonDist({
		row = var_194_1.row,
		column = var_194_1.column
	}, {
		row = var_194_2.row,
		column = var_194_2.column
	}) <= 1:
		arg_194_0.Op("OpTriggerSign", var_194_1, var_194_2.GetEventAttachment(), function()
			arg_194_0.Op("OpInteractive"))
	elif var_194_0.CanLongMove(var_194_1):
		arg_194_0.Op("OpLongMoveFleet", var_194_1, var_194_2.row, var_194_2.column)
	else
		arg_194_0.Op("OpReqMoveFleet", var_194_1, var_194_2.row, var_194_2.column)

def var_0_0.OnClickTransport(arg_196_0):
	if arg_196_0.svScannerPanel.isShowing():
		return

	arg_196_0.Op("OpCall", function(arg_197_0)
		arg_197_0()
		arg_196_0.QueryTransport(function()
			arg_196_0.EnterTransportWorld()))

def var_0_0.QueryTransport(arg_199_0, arg_199_1):
	local var_199_0 = nowWorld()
	local var_199_1 = var_199_0.GetActiveMap()
	local var_199_2 = {}

	if not var_199_0.IsSystemOpen(WorldConst.SystemOutMap):
		pg.TipsMgr.GetInstance().ShowTips(i18n("word_systemClose"))

		return

	if var_199_1.CheckAttachmentTransport() == "story":
		local var_199_3 = pg.gameset.world_transfer_eventstory.description[1]

		table.insert(var_199_2, function(arg_200_0)
			arg_199_0.OpRaw("OpStory", var_199_3, True, True, False, function(arg_201_0)
				if arg_201_0 == 1:
					arg_200_0()))

	if var_199_0.IsSubmarineSupporting() and var_199_1.GetSubmarineFleet().GetAmmo() > 0:
		table.insert(var_199_2, function(arg_202_0)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("world_instruction_submarine_6"),
				onYes = arg_202_0
			}))

	if var_199_1.CheckFleetSalvage(True):
		table.insert(var_199_2, function(arg_203_0)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("world_catsearch_leavemap"),
				onYes = arg_203_0
			}))

	local var_199_4

	for iter_199_0, iter_199_1 in ipairs(var_199_1.GetNormalFleets()):
		for iter_199_2, iter_199_3 in ipairs(iter_199_1.GetCarries()):
			if iter_199_3.config.out_story != "":
				var_199_4 = iter_199_3.config.out_story

	if var_199_4:
		table.insert(var_199_2, function(arg_204_0)
			arg_199_0.OpRaw("OpStory", var_199_4, True, True, False, function(arg_205_0)
				if arg_205_0 == 1:
					arg_204_0()))

	local var_199_5, var_199_6 = var_199_1.CkeckTransport()

	if not var_199_5:
		table.insert(var_199_2, function(arg_206_0)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = var_199_6,
				onYes = arg_206_0
			}))

	seriesAsync(var_199_2, function()
		return arg_199_1(var_199_5))

def var_0_0.OnUpdateEventTips(arg_208_0, arg_208_1, arg_208_2):
	if arg_208_0.wsMapRight:
		arg_208_0.wsMapRight.OnUpdateEventTips()

	if arg_208_0.wsMapTop:
		arg_208_0.wsMapTop.OnUpdatePoison()

def var_0_0.OnClickMap(arg_209_0, arg_209_1, arg_209_2):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL)

	local var_209_0 = arg_209_0.wsMap.map
	local var_209_1 = var_209_0.top
	local var_209_2 = var_209_0.bottom
	local var_209_3 = var_209_0.left
	local var_209_4 = var_209_0.right

	if arg_209_1 < var_209_1 or var_209_2 < arg_209_1 or arg_209_2 < var_209_3 or var_209_4 < arg_209_2:
		arg_209_0.OnClickTransport()
	else
		arg_209_0.OnClickCell(arg_209_1, arg_209_2)

def var_0_0.CheckScannerEnable(arg_210_0, arg_210_1, arg_210_2):
	if nowWorld().IsSystemOpen(WorldConst.SystemScanner):
		local var_210_0 = arg_210_0.wsMap.map.GetCell(arg_210_1, arg_210_2)

		if var_210_0 and var_210_0.GetInFOV() and not var_210_0.InFog():
			local var_210_1 = var_210_0.GetScannerAttachment()

			if var_210_1:
				local var_210_2 = arg_210_0.wsMap.GetCell(arg_210_1, arg_210_2).rtAttachments.position

				return var_210_1, arg_210_0.camera.WorldToScreenPoint(var_210_2)

def var_0_0.OnLongPressMap(arg_211_0, arg_211_1, arg_211_2):
	if not arg_211_0.svScannerPanel.isShowing():
		local var_211_0, var_211_1 = arg_211_0.CheckScannerEnable(arg_211_1, arg_211_2)

		if var_211_0:
			arg_211_0.Op("OpShowScannerPanel", var_211_0, var_211_1)

def var_0_0.OnAchievementAchieved(arg_212_0, arg_212_1, arg_212_2, arg_212_3, arg_212_4):
	if arg_212_3:
		for iter_212_0, iter_212_1 in ipairs(arg_212_3):
			pg.TipsMgr.GetInstance().ShowTips(iter_212_1)

	if arg_212_4:
		local var_212_0 = nowWorld()

		if var_212_0.isAutoFight:
			var_212_0.AddAutoInfo("message", i18n("autofight_discovery", arg_212_4.config.target_desc))
		else
			table.insert(arg_212_0.achievedList, {
				arg_212_4,
				arg_212_0.wsMapRight.btnInformation.position
			})

def var_0_0.DoAnim(arg_213_0, arg_213_1, arg_213_2):
	local var_213_0 = arg_213_0.wsAnim

	if not var_213_0.GetAnim(arg_213_1):
		var_213_0.SetAnim(arg_213_1, arg_213_0.NewUIAnim(arg_213_1))

	var_213_0.GetAnim(arg_213_1).Play(arg_213_2)

def var_0_0.NewUIAnim(arg_214_0, arg_214_1):
	local var_214_0 = UIAnim.New()

	var_214_0.Setup(arg_214_1)
	var_214_0.AddListener(UIAnim.EventLoaded, function()
		var_214_0.transform.SetParent(arg_214_0.rtTop, False))
	var_214_0.Load()

	return var_214_0

def var_0_0.DoStrikeAnim(arg_216_0, arg_216_1, arg_216_2, arg_216_3):
	local var_216_0 = arg_216_0.wsAnim

	if not var_216_0.GetAnim(arg_216_1):
		var_216_0.SetAnim(arg_216_1, arg_216_0.NewStrikeAnim(arg_216_1, arg_216_2))
	else
		var_216_0.GetAnim(arg_216_1).ReloadShip(arg_216_2)

	var_216_0.GetAnim(arg_216_1).Play(arg_216_3)

def var_0_0.NewStrikeAnim(arg_217_0, arg_217_1, arg_217_2):
	local var_217_0 = UIStrikeAnim.New()

	var_217_0.Setup(arg_217_1, arg_217_2)
	var_217_0.AddListener(UIStrikeAnim.EventLoaded, function()
		var_217_0.transform.SetParent(arg_217_0.rtTop, False))
	var_217_0.Load()

	return var_217_0

def var_0_0.StopAnim(arg_219_0):
	arg_219_0.wsAnim.Stop()

def var_0_0.UpdateSystemOpen(arg_220_0):
	local var_220_0 = nowWorld()

	if arg_220_0.GetInMap():
		local var_220_1 = var_220_0.GetActiveMap()

		arg_220_0.wsMapLeft.onAgonyClickEnabled = var_220_0.IsSystemOpen(WorldConst.SystemInventory)

		setActive(arg_220_0.wsMapRight.btnInventory, var_220_0.IsSystemOpen(WorldConst.SystemInventory))
		setActive(arg_220_0.wsMapRight.btnTransport, var_220_0.IsSystemOpen(WorldConst.SystemOutMap))
		setActive(arg_220_0.wsMapRight.btnDetail, var_220_0.IsSystemOpen(WorldConst.SystemFleetDetail))
		setActive(arg_220_0.wsMapRight.rtCompassPanel, var_220_0.IsSystemOpen(WorldConst.SystemCompass))
		setActive(arg_220_0.wsMapRight.toggleAutoFight, var_220_1.CanAutoFight())
		setActive(arg_220_0.wsMapRight.toggleAutoSwitch, var_220_0.IsSystemOpen(WorldConst.SystemAutoSwitch))
	else
		setActive(arg_220_0.wsAtlasBottom.btnBoss, var_220_0.IsSystemOpen(WorldConst.SystemWorldBoss))

		local var_220_2 = var_220_0.GetBossProxy().NeedTip()
		local var_220_3 = var_220_0.GetBossProxy().ExistSelfBoss()
		local var_220_4 = WorldBossConst.CanUnlockCurrBoss()
		local var_220_5 = not var_220_3 and not var_220_4

		setActive(arg_220_0.wsAtlasBottom.btnBoss.Find("tip"), var_220_2 or var_220_4 or WorldBossConst.AnyArchivesBossCanGetAward())
		setActive(arg_220_0.wsAtlasBottom.btnBoss.Find("sel"), not var_220_5)

		local var_220_6 = arg_220_0.rtTopAtlas.Find("reset_coutdown")

		onButton(arg_220_0, var_220_6, function()
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = i18n("world_reset_tip")
			}), SFX_PANEL)

		local var_220_7 = var_220_0.IsSystemOpen(WorldConst.SystemResetCountDown) and var_220_0.CheckResetProgress()

		setActive(var_220_6, var_220_7)

		if var_220_7:
			local var_220_8 = var_220_0.GetResetWaitingTime()
			local var_220_9 = math.floor(var_220_8 / 86400)

			if var_220_9 > 0:
				setText(var_220_6.Find("Text"), i18n("world_reset_1", string.format("  %d  ", var_220_9)))
			elif var_220_9 == 0:
				setText(var_220_6.Find("Text"), i18n("world_reset_2", string.format("  %d  ", 0)))
			elif var_220_9 < 0:
				setText(var_220_6.Find("Text"), i18n("world_reset_3"))

		setActive(arg_220_0.wsAtlasBottom.btnShop, var_220_0.IsSystemOpen(WorldConst.SystemResetShop))
		setActive(arg_220_0.wsAtlasBottom.btnDailyTask.Find("mask"), not var_220_0.IsSystemOpen(WorldConst.SystemDailyTask))
		setActive(arg_220_0.wsAtlasRight.btnSwitch, var_220_0.IsSystemOpen(WorldConst.SystemAutoSwitch))

	setActive(arg_220_0.resAtlas._tf, var_220_0.IsSystemOpen(WorldConst.SystemResource))
	setActive(arg_220_0.resMap._tf, var_220_0.IsSystemOpen(WorldConst.SystemResource))

def var_0_0.EnterToModelMap(arg_222_0, arg_222_1):
	local var_222_0 = {}

	table.insert(var_222_0, function(arg_223_0)
		setActive(arg_222_0.rtTopAtlas.Find("print/title_world"), True)
		setActive(arg_222_0.rtTopAtlas.Find("print/title_view"), False)
		arg_222_0.wsAtlasBottom.UpdateScale(1, True, arg_223_0))
	table.insert(var_222_0, function(arg_224_0)
		arg_222_0.wsAtlas.SwitchArea(arg_222_1, True, arg_224_0))
	parallelAsync(var_222_0, function()
		local var_225_0 = nowWorld().GetAtlas().GetActiveEntrance()

		if arg_222_1 == var_225_0.GetAreaId():
			arg_222_0.wsAtlas.UpdateSelect(var_225_0))

def var_0_0.ReturnToModelArea(arg_226_0):
	arg_226_0.wsAtlas.UpdateSelect()

	local var_226_0 = {}

	table.insert(var_226_0, function(arg_227_0)
		setActive(arg_226_0.rtTopAtlas.Find("print/title_world"), False)
		setActive(arg_226_0.rtTopAtlas.Find("print/title_view"), True)
		arg_226_0.wsAtlasBottom.UpdateScale(0, True, arg_227_0))
	table.insert(var_226_0, function(arg_228_0)
		arg_226_0.wsAtlas.SwitchArea(None, True, arg_228_0))
	parallelAsync(var_226_0, function()
		return)

def var_0_0.EnterTransportWorld(arg_230_0, arg_230_1):
	local var_230_0 = nowWorld()

	arg_230_1 = arg_230_1 or {
		entrance = var_230_0.GetActiveEntrance()
	}

	local var_230_1 = {}

	if arg_230_0.GetInMap():
		table.insert(var_230_1, function(arg_231_0)
			arg_230_0.Op("OpSetInMap", False, arg_231_0))
	elif not arg_230_0.wsAtlas.nowArea:
		table.insert(var_230_1, function(arg_232_0)
			arg_230_0.wsAtlas.SwitchArea(arg_230_1.entrance.GetAreaId(), False, arg_232_0))

	seriesAsync(var_230_1, function()
		arg_230_0.wsAtlas.UpdateSelect()
		arg_230_0.wsAtlas.UpdateSelect(arg_230_1.entrance, arg_230_1.mapId, arg_230_1.mapTypes)
		arg_230_0.wsAtlas.DisplayTransport(arg_230_0.contextData.displayTransDic or {}, function()
			arg_230_0.contextData.displayTransDic = Clone(var_230_0.GetAtlas().transportDic)))

def var_0_0.BackToMap(arg_235_0):
	if arg_235_0.wsAtlas.CheckIsTweening():
		return

	arg_235_0.Op("OpSetInMap", True)

def var_0_0.DisplayEnv(arg_236_0, arg_236_1):
	local var_236_0 = checkExist(nowWorld().GetActiveMap(), {
		"config"
	}, {
		"map_bg"
	}, {
		1
	}) or "model_bg"
	local var_236_1 = {}

	if arg_236_0.rtEnvBG.GetComponent(typeof(Image)).sprite.name != var_236_0:
		table.insert(var_236_1, function(arg_237_0)
			GetSpriteFromAtlasAsync("world/map/" .. var_236_0, var_236_0, function(arg_238_0)
				setImageSprite(arg_236_0.rtEnvBG, arg_238_0)

				return arg_237_0()))

	seriesAsync(var_236_1, arg_236_1)

def var_0_0.ScreenPos2MapPos(arg_239_0, arg_239_1):
	local var_239_0 = arg_239_0.wsMap
	local var_239_1 = var_239_0.map
	local var_239_2 = arg_239_0.camera.ScreenPointToRay(arg_239_1)
	local var_239_3, var_239_4 = Plane.New(var_239_0.rtQuads.forward, -Vector3.Dot(var_239_0.rtQuads.position, var_239_0.rtQuads.forward)).Raycast(var_239_2)

	if var_239_3:
		local var_239_5 = var_239_2.GetPoint(var_239_4)
		local var_239_6 = var_239_0.rtQuads.InverseTransformPoint(var_239_5)
		local var_239_7 = var_239_1.theme.X2Column(var_239_6.x)

		return var_239_1.theme.Y2Row(var_239_6.y), var_239_7

def var_0_0.BuildCutInAnim(arg_240_0, arg_240_1, arg_240_2):
	arg_240_0.tfAnim = arg_240_0.rtPanelList.Find(arg_240_1 .. "(Clone)")

	local var_240_0 = {}

	if not arg_240_0.tfAnim:
		table.insert(var_240_0, function(arg_241_0)
			PoolMgr.GetInstance().GetUI(arg_240_1, True, function(arg_242_0)
				arg_242_0.SetActive(False)

				arg_240_0.tfAnim = tf(arg_242_0)

				arg_240_0.tfAnim.SetParent(arg_240_0.rtPanelList, False)

				return arg_241_0()))

	table.insert(var_240_0, function(arg_243_0)
		arg_240_0.inCutIn = True

		arg_240_0.tfAnim.GetComponent("DftAniEvent").SetEndEvent(function(arg_244_0)
			if not IsNil(arg_240_0.tfAnim):
				arg_240_0.inCutIn = False

				pg.UIMgr.GetInstance().UnOverlayPanel(arg_240_0.tfAnim, arg_240_0.rtPanelList)
				setActive(arg_240_0.tfAnim, False)

				return arg_243_0())
		pg.UIMgr.GetInstance().OverlayPanel(arg_240_0.tfAnim)
		setActive(arg_240_0.tfAnim, True))
	seriesAsync(var_240_0, function()
		return existCall(arg_240_2))

def var_0_0.PlaySound(arg_246_0, arg_246_1, arg_246_2):
	if arg_246_0.cueName:
		pg.CriMgr.GetInstance().StopSE_V3()

		arg_246_0.cueName = None

	pg.CriMgr.GetInstance().PlaySE_V3(arg_246_1, function()
		arg_246_0.cueName = None)

	return existCall(arg_246_2)

def var_0_0.ChangeTopRaycasts(arg_248_0, arg_248_1):
	GetComponent(arg_248_0.rtTop, typeof(CanvasGroup)).blocksRaycasts = tobool(arg_248_1)

def var_0_0.DoTopBlock(arg_249_0, arg_249_1):
	arg_249_0.ChangeTopRaycasts(False)

	return function(...)
		arg_249_0.ChangeTopRaycasts(True)

		return existCall(arg_249_1, ...)

def var_0_0.SetMoveQueue(arg_251_0, arg_251_1):
	arg_251_0.ReContinueMoveQueue()

	arg_251_0.moveQueue = arg_251_1

def var_0_0.ClearMoveQueue(arg_252_0):
	arg_252_0.DisplayMoveStopClick(False)

	arg_252_0.moveQueueInteractive = True

	if #arg_252_0.moveQueue > 0:
		arg_252_0.moveQueue = {}

	arg_252_0.ShowFleetMoveTurn(False)

def var_0_0.DoQueueMove(arg_253_0, arg_253_1):
	assert(#arg_253_0.moveQueue > 0, "without move queue")
	arg_253_0.DisplayMoveStopClick(True)

	local var_253_0 = nowWorld().GetActiveMap()
	local var_253_1 = _.detect(arg_253_0.moveQueue, function(arg_254_0)
		return arg_254_0.stay)

	if #arg_253_0.moveQueue == 1 and var_253_0.IsSign(var_253_1.row, var_253_1.column):
		arg_253_0.ClearMoveQueue()

		local var_253_2 = var_253_0.GetCell(var_253_1.row, var_253_1.column)

		arg_253_0.Op("OpTriggerSign", arg_253_1, var_253_2.GetEventAttachment(), function()
			arg_253_0.Op("OpInteractive"))
	else
		arg_253_0.ReContinueMoveQueue()
		arg_253_0.ShowFleetMoveTurn(True)
		arg_253_0.Op("OpReqMoveFleet", arg_253_1, var_253_1.row, var_253_1.column)

def var_0_0.CheckMoveQueue(arg_256_0, arg_256_1):
	if #arg_256_0.moveQueue < #arg_256_1 or #arg_256_1 == 0:
		arg_256_0.ClearMoveQueue()
	else
		local var_256_0 = arg_256_1[#arg_256_1]

		if arg_256_0.moveQueue[#arg_256_1].row != var_256_0.row or arg_256_0.moveQueue[#arg_256_1].column != var_256_0.column:
			arg_256_0.ClearMoveQueue()
		else
			for iter_256_0 = 1, #arg_256_1:
				table.remove(arg_256_0.moveQueue, 1)

			if #arg_256_0.moveQueue == 0:
				arg_256_0.ResetLostMoveQueueCount()

				arg_256_0.moveQueueInteractive = True

def var_0_0.InteractiveMoveQueue(arg_257_0):
	if arg_257_0.moveQueueInteractive:
		arg_257_0.ClearMoveQueue()
	else
		arg_257_0.DisplayMoveStopClick(False)

		arg_257_0.moveQueueInteractive = True

def var_0_0.ReContinueMoveQueue(arg_258_0):
	arg_258_0.moveQueueInteractive = False

def var_0_0.CheckLostMoveQueueCount(arg_259_0):
	arg_259_0.lostMoveQueueCount = defaultValue(arg_259_0.lostMoveQueueCount, 0) + 1

	return arg_259_0.lostMoveQueueCount > WorldConst.AutoFightLoopCountLimit

def var_0_0.ResetLostMoveQueueCount(arg_260_0, arg_260_1):
	if arg_260_1:
		arg_260_0.inLoopAutoFight = True

	arg_260_0.lostMoveQueueCount = 0

def var_0_0.DisplayMoveStopClick(arg_261_0, arg_261_1):
	setActive(arg_261_0.rtClickStop, arg_261_1)

	if arg_261_1:
		local var_261_0 = nowWorld().isAutoFight

		setActive(arg_261_0.rtClickStop.Find("long_move"), not var_261_0)
		setActive(arg_261_0.rtClickStop.Find("auto_fight"), var_261_0)

def var_0_0.ShowFleetMoveTurn(arg_262_0, arg_262_1):
	if arg_262_0.wsMap:
		if arg_262_1:
			arg_262_0.wsMap.GetFleet().PlusMoveTurn()
		else
			arg_262_0.wsMap.GetFleet().ClearMoveTurn()

def var_0_0.GetAllPessingAward(arg_263_0, arg_263_1):
	local var_263_0 = nowWorld()
	local var_263_1 = var_263_0.GetAtlas()
	local var_263_2 = {}

	for iter_263_0, iter_263_1 in pairs(var_263_0.pressingAwardDic):
		if iter_263_1.flag:
			var_263_0.FlagMapPressingAward(iter_263_0)
			var_263_1.MarkMapTransport(iter_263_0)

			local var_263_3 = pg.world_event_complete[iter_263_1.id].event_reward_slgbuff

			if #var_263_3 > 0:
				var_263_2[var_263_3[1]] = defaultValue(var_263_2[var_263_3[1]], 0) + var_263_3[2]

	local var_263_4 = var_263_0.GetActiveMap()

	if not var_263_4.visionFlag and var_263_0.IsMapVisioned(var_263_4.id):
		var_263_4.UpdateVisionFlag(True)

	if arg_263_0.wsAtlas:
		arg_263_0.wsAtlas.OnUpdatePressingAward()

	local var_263_5 = {}

	for iter_263_2, iter_263_3 in pairs(var_263_2):
		table.insert(var_263_5, function(arg_264_0)
			local var_264_0 = {
				id = iter_263_2,
				floor = iter_263_3,
				before = var_263_0.GetGlobalBuff(iter_263_2).GetFloor()
			}

			arg_263_0.ShowSubView("GlobalBuff", {
				var_264_0,
				arg_264_0
			}))
		table.insert(var_263_5, function(arg_265_0)
			var_263_0.AddGlobalBuff(iter_263_2, iter_263_3)
			arg_265_0())

	seriesAsync(var_263_5, function()
		return existCall(arg_263_1))

def var_0_0.CheckGuideSLG(arg_267_0, arg_267_1, arg_267_2):
	local var_267_0 = nowWorld()
	local var_267_1 = {}

	table.insert(var_267_1, {
		"WorldG007",
		function()
			local var_268_0 = arg_267_1.GetPort()

			if var_268_0 and not var_268_0.IsTempPort():
				local var_268_1 = arg_267_1.GetFleet()

				return not arg_267_1.GetCell(var_268_1.row, var_268_1.column).ExistEnemy()
	})
	table.insert(var_267_1, {
		"WorldG111",
		function()
			return arg_267_1.canExit()
	})
	table.insert(var_267_1, {
		"WorldG112",
		function()
			local var_270_0 = var_267_0.GetActiveEntrance()

			return var_270_0.becomeSairen and var_270_0.GetSairenMapId() == arg_267_1.id
	})
	table.insert(var_267_1, {
		"WorldG124",
		function()
			return var_267_0.IsSystemOpen(WorldConst.SystemOrderSubmarine) and arg_267_1.GetConfig("instruction_available")[1] != 0 and var_267_0.CanCallSubmarineSupport()
	})
	table.insert(var_267_1, {
		"WorldG162",
		function()
			return _.any(arg_267_1.GetNormalFleets(), function(arg_273_0)
				return _.any(arg_273_0.GetShips(True), function(arg_274_0)
					return arg_274_0.IsBroken()))
	})
	table.insert(var_267_1, {
		"WorldG163",
		function()
			local var_275_0 = var_267_0.GetTaskProxy().getDoingTaskVOs()

			return underscore.any(var_275_0, function(arg_276_0)
				return not arg_276_0.IsAutoSubmit() and arg_276_0.isFinished())
	})
	table.insert(var_267_1, {
		"WorldG164",
		function()
			return arg_267_1.CheckFleetSalvage(True)
	})
	table.insert(var_267_1, {
		"WorldG181",
		function()
			return var_267_0.GetInventoryProxy().GetItemCount(102) > 0
	})
	table.insert(var_267_1, {
		"WorldG191",
		function()
			return WorldBossConst.CanUnlockCurrBoss() and nowWorld().IsSystemOpen(WorldConst.SystemWorldBoss)
	})

	local var_267_2 = _.filter(arg_267_1.FindAttachments(WorldMapAttachment.TypeEvent), function(arg_280_0)
		return arg_280_0.IsAlive())

	for iter_267_0, iter_267_1 in ipairs(pg.gameset.world_guide_event.description):
		table.insert(var_267_1, {
			iter_267_1[2],
			function()
				return _.any(var_267_2, function(arg_282_0)
					return arg_282_0.id == iter_267_1[1])
		})

	local var_267_3 = pg.NewStoryMgr.GetInstance()

	for iter_267_2, iter_267_3 in ipairs(var_267_1):
		if not var_267_3.IsPlayed(iter_267_3[1]) and iter_267_3[2]():
			WorldGuider.GetInstance().PlayGuide(iter_267_3[1])

			return True

	return False

def var_0_0.CheckEventForMsg(arg_283_0, arg_283_1):
	return pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_283_0.player.level, "EventMediator") and getProxy(EventProxy).eventForMsg

def var_0_0.OpenPortLayer(arg_284_0, arg_284_1):
	arg_284_0.Op("OpOpenLayer", Context.New({
		mediator = WorldPortMediator,
		viewComponent = WorldPortLayer,
		data = arg_284_1
	}))

def var_0_0.ShowTransportMarkOverview(arg_285_0, arg_285_1, arg_285_2):
	if nowWorld().GetActiveMap().CheckFleetSalvage(True):
		arg_285_0.Op("OpShowMarkOverview", arg_285_1, function()
			pg.NewStoryMgr.GetInstance().Play(pg.gameset.world_catsearch_special.description[1], arg_285_2, True))
	else
		arg_285_0.Op("OpShowMarkOverview", arg_285_1, arg_285_2)

def var_0_0.UpdateAutoFightDisplay(arg_287_0):
	arg_287_0.ClearMoveQueue()

	local var_287_0 = nowWorld().isAutoFight

	if arg_287_0.wsMapRight:
		setActive(arg_287_0.wsMapRight.toggleAutoFight.Find("off"), not var_287_0)
		setActive(arg_287_0.wsMapRight.toggleAutoFight.Find("on"), var_287_0)
		setActive(arg_287_0.wsMapRight.toggleSkipPrecombat, not var_287_0)
		triggerToggle(arg_287_0.wsMapRight.toggleSkipPrecombat, PlayerPrefs.GetInt("world_skip_precombat", 0) == 1)

def var_0_0.UpdateAutoSwitchDisplay(arg_288_0):
	local var_288_0 = nowWorld().isAutoSwitch

	if arg_288_0.wsMapRight:
		setActive(arg_288_0.wsMapRight.toggleAutoSwitch.Find("off"), not var_288_0)
		setActive(arg_288_0.wsMapRight.toggleAutoSwitch.Find("on"), var_288_0)

def var_0_0.GuideShowScannerEvent(arg_289_0, arg_289_1):
	assert(arg_289_0.svScannerPanel.isShowing(), "scanner mode is closed")

	local var_289_0 = arg_289_0.wsMap.map.FindAttachments(WorldMapAttachment.TypeEvent, arg_289_1)

	assert(#var_289_0 == 1, "event number error. " .. #var_289_0)

	local var_289_1, var_289_2 = arg_289_0.CheckScannerEnable(var_289_0[1].row, var_289_0[1].column)

	assert(var_289_1, "without scanner attachment")
	arg_289_0.svScannerPanel.ActionInvoke("DisplayWindow", var_289_1, var_289_2)

def var_0_0.DisplayAwards(arg_290_0, arg_290_1, arg_290_2, arg_290_3):
	local var_290_0 = {}
	local var_290_1 = {}

	for iter_290_0, iter_290_1 in ipairs(arg_290_1):
		if iter_290_1.type == DROP_TYPE_WORLD_COLLECTION:
			table.insert(var_290_1, iter_290_1)
		else
			table.insert(var_290_0, iter_290_1)

	seriesAsync({
		function(arg_291_0)
			if #var_290_0 == 0:
				return arg_291_0()

			arg_290_2.items = var_290_0
			arg_290_2.removeFunc = arg_291_0

			arg_290_0.emit(BaseUI.ON_WORLD_ACHIEVE, arg_290_2),
		function(arg_292_0)
			local var_292_0 = var_290_1[1]

			if not var_292_0:
				arg_292_0()

				return

			assert(WorldCollectionProxy.GetCollectionType(var_292_0.id) == WorldCollectionProxy.WorldCollectionType.FILE, string.format("collection drop type error#%d", var_292_0.id))
			arg_290_0.emit(WorldMediator.OnOpenLayer, Context.New({
				mediator = WorldMediaCollectionFilePreviewMediator,
				viewComponent = WorldMediaCollectionFilePreviewLayer,
				data = {
					collectionId = var_292_0.id
				},
				onRemoved = arg_292_0
			}))
	}, arg_290_3)

def var_0_0.DisplayPhaseAction(arg_293_0, arg_293_1):
	local var_293_0 = {}

	while #arg_293_1 > 0:
		local var_293_1 = nowWorld()
		local var_293_2 = table.remove(arg_293_1, 1)

		table.insert(var_293_0, function(arg_294_0)
			if var_293_2.anim:
				arg_293_0.BuildCutInAnim(var_293_2.anim, arg_294_0)
			elif var_293_2.story:
				if var_293_1.isAutoFight:
					arg_294_0()
				else
					pg.NewStoryMgr.GetInstance().Play(var_293_2.story, arg_294_0, True)
			elif var_293_2.drops:
				if var_293_1.isAutoFight:
					var_293_1.AddAutoInfo("drops", var_293_2.drops)
					arg_294_0()
				else
					arg_293_0.DisplayAwards(var_293_2.drops, {}, arg_294_0))

	seriesAsync(var_293_0, function()
		arg_293_0.Op("OpInteractive"))

def var_0_0.StartAutoSwitch(arg_296_0):
	local var_296_0 = nowWorld()
	local var_296_1 = var_296_0.GetActiveEntrance()
	local var_296_2 = var_296_0.GetActiveMap()

	if PlayerPrefs.GetInt("auto_switch_mode", 0) == WorldSwitchPlanningLayer.MODE_SAFE and PlayerPrefs.GetString("auto_switch_difficult_safe", "only") == "only" and World.ReplacementMapType(var_296_1, var_296_2) != "complete_chapter":
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_automode_start_tip3"))

		return
	elif PlayerPrefs.GetInt("auto_switch_mode", 0) == WorldSwitchPlanningLayer.MODE_TREASURE and not var_296_0.GetGobalFlag("treasure_flag"):
		pg.TipsMgr.GetInstance().ShowTips("without auto switch flag")

		return

	arg_296_0.QueryTransport(function(arg_297_0)
		if not arg_297_0:
			if PlayerPrefs.GetInt("auto_switch_mode", 0) == WorldSwitchPlanningLayer.MODE_TREASURE and World.ReplacementMapType(var_296_1, var_296_2) == "teasure_chapter":
				pg.TipsMgr.GetInstance().ShowTips(i18n("world_automode_start_tip5"))
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("world_automode_start_tip4"))
		else
			getProxy(MetaCharacterProxy).setMetaTacticsInfoOnStart()
			PlayerPrefs.SetInt("world_skip_precombat", 1)
			PlayerPrefs.SetInt("autoBotIsAcitve" .. AutoBotCommand.GetAutoBotMark(SYSTEM_WORLD), 1)
			arg_296_0.Op("OpAutoSwitchMap"))

def var_0_0.MoveAndOpenLayer(arg_298_0, arg_298_1):
	local var_298_0 = {}

	table.insert(var_298_0, function(arg_299_0)
		arg_298_0.Op("OpSetInMap", arg_298_1.inMap, arg_299_0))
	seriesAsync(var_298_0, function()
		arg_298_0.Op("OpOpenLayer", arg_298_1.context))

def var_0_0.GetDepth(arg_301_0):
	return #arg_301_0.wsCommands

def var_0_0.GetCommand(arg_302_0, arg_302_1):
	return arg_302_0.wsCommands[arg_302_1 or arg_302_0.GetDepth()]

def var_0_0.Op(arg_303_0, arg_303_1, ...):
	arg_303_0.GetCommand().Op(arg_303_1, ...)

def var_0_0.OpRaw(arg_304_0, arg_304_1, ...):
	arg_304_0.GetCommand().OpRaw(arg_304_1, ...)

def var_0_0.OpOpen(arg_305_0):
	local var_305_0 = arg_305_0.GetDepth()

	WorldConst.Print("open operation stack. " .. var_305_0 + 1)
	table.insert(arg_305_0.wsCommands, WSCommand.New(var_305_0 + 1))

def var_0_0.OpClose(arg_306_0):
	local var_306_0 = arg_306_0.GetDepth()

	assert(var_306_0 > 0)
	WorldConst.Print("close operation stack. " .. var_306_0)
	arg_306_0.wsCommands[var_306_0].Dispose()
	table.remove(arg_306_0.wsCommands, var_306_0)

def var_0_0.OpClear(arg_307_0):
	for iter_307_0, iter_307_1 in ipairs(arg_307_0.wsCommands):
		iter_307_1.OpClear()

def var_0_0.OpDispose(arg_308_0):
	for iter_308_0, iter_308_1 in ipairs(arg_308_0.wsCommands):
		iter_308_1.Dispose()

	arg_308_0.wsCommands = None

def var_0_0.NewMapOp(arg_309_0, arg_309_1):
	local var_309_0 = WBank.Fetch(WorldMapOp)

	var_309_0.depth = arg_309_0.GetDepth()

	for iter_309_0, iter_309_1 in pairs(arg_309_1):
		var_309_0[iter_309_0] = iter_309_1

	return var_309_0

def var_0_0.RegistMapOp(arg_310_0, arg_310_1):
	assert(arg_310_1, "mapOp can not be None.")
	assert(not table.contains(arg_310_0.mapOps, arg_310_1), "repeated registered mapOp.")
	table.insert(arg_310_0.mapOps, arg_310_1)
	arg_310_1.AddCallbackWhenApplied(function()
		for iter_311_0 = #arg_310_0.mapOps, 1, -1:
			if arg_310_0.mapOps[iter_311_0] == arg_310_1:
				table.remove(arg_310_0.mapOps, iter_311_0))

def var_0_0.VerifyMapOp(arg_312_0):
	for iter_312_0 = #arg_312_0.mapOps, 1, -1:
		local var_312_0 = table.remove(arg_312_0.mapOps, iter_312_0)

		if not var_312_0.applied:
			var_312_0.Apply()

	arg_312_0.OpClear()

def var_0_0.GetCompassGridPos(arg_313_0, arg_313_1, arg_313_2, arg_313_3):
	WorldGuider.GetInstance().SetTempGridPos(arg_313_0.wsMapRight.wsCompass.GetMarkPosition(arg_313_1, arg_313_2), arg_313_3)

def var_0_0.GetEntranceTrackMark(arg_314_0, arg_314_1, arg_314_2):
	WorldGuider.GetInstance().SetTempGridPos(arg_314_0.wsMapRight.wsCompass.GetEntranceTrackMark(arg_314_1), arg_314_2)

def var_0_0.GetSlgTilePos(arg_315_0, arg_315_1, arg_315_2, arg_315_3):
	WorldGuider.GetInstance().SetTempGridPos2(arg_315_0.wsMap.GetCell(arg_315_1, arg_315_2).GetWorldPos(), arg_315_3)

def var_0_0.GetScannerPos(arg_316_0, arg_316_1):
	local var_316_0 = arg_316_0.svScannerPanel.rtPanel.transform
	local var_316_1 = arg_316_0.svScannerPanel.rtWindow.transform
	local var_316_2 = Vector3.New(var_316_1.localPosition.x + var_316_1.rect.width * (0.5 - var_316_1.pivot.x), var_316_1.localPosition.y + var_316_1.rect.height * (0.5 - var_316_1.pivot.y), 0)
	local var_316_3 = var_316_0.TransformPoint(var_316_2)

	WorldGuider.GetInstance().SetTempGridPos(var_316_3, arg_316_1)

def var_0_0.GuideSelectModelMap(arg_317_0, arg_317_1):
	local var_317_0 = nowWorld().GetEntrance(arg_317_1)

	assert(arg_317_0.wsAtlas, "didn't enter the world map mode")
	arg_317_0.ClickAtlas(var_317_0)

return var_0_0
