pg = pg or {}
pg.NewGuideMgr = singletonClass("NewGuideMgr")

local var_0_0 = pg.NewGuideMgr

var_0_0.ENABLE_GUIDE = True

require("Mgr/Guide/Include")

local var_0_1 = True
local var_0_2 = 0
local var_0_3 = 1
local var_0_4 = 2
local var_0_5 = 3
local var_0_6 = 4
local var_0_7 = 5

local function var_0_8(...)
	if not var_0_1:
		return

	print(...)

local function var_0_9(arg_2_0, arg_2_1)
	arg_2_0.players = {
		[GuideStep.TYPE_DOFUNC] = GuideDoFunctionPlayer.New(arg_2_1),
		[GuideStep.TYPE_DONOTHING] = GuideDoNothingPlayer.New(arg_2_1),
		[GuideStep.TYPE_FINDUI] = GuideFindUIPlayer.New(arg_2_1),
		[GuideStep.TYPE_HIDEUI] = GuideHideUIPlayer.New(arg_2_1),
		[GuideStep.TYPE_SENDNOTIFIES] = GuideSendNotifiesPlayer.New(arg_2_1),
		[GuideStep.TYPE_SHOWSIGN] = GuideShowSignPlayer.New(arg_2_1),
		[GuideStep.TYPE_STORY] = GuideStoryPlayer.New(arg_2_1)
	}

local function var_0_10(arg_3_0)
	local var_3_0 = require("GameCfg.guide.newguide.segments." .. arg_3_0)

	return Guide.New(var_3_0)

def var_0_0.Init(arg_4_0, arg_4_1):
	arg_4_0.sceneRecords = {}
	arg_4_0.state = var_0_2

	PoolMgr.GetInstance().GetUI("NewGuideUI", True, function(arg_5_0)
		arg_4_0._go = arg_5_0
		arg_4_0._tf = arg_4_0._go.transform

		arg_4_0._go.SetActive(False)
		arg_4_0._go.transform.SetParent(pg.UIMgr.GetInstance().OverlayToast, False)

		arg_4_0.uiFinder = GuideUIFinder.New(arg_4_0._tf)
		arg_4_0.uiDuplicator = GuideUIDuplicator.New(arg_4_0._tf.Find("target"))
		arg_4_0.uiLoader = GuideUILoader.New(arg_4_0._tf.Find("target"))
		arg_4_0.dialogueWindows = {
			[GuideStep.DIALOGUE_BLUE] = arg_4_0._tf.Find("windows/window_1")
		}
		arg_4_0.counsellors = {}
		arg_4_0.state = var_0_3
		arg_4_0.uiLongPress = GetOrAddComponent(arg_4_0._tf.Find("BG/close_btn"), typeof(UILongPressTrigger))
		arg_4_0.uiLongPress.longPressThreshold = 10

		var_0_9(arg_4_0, arg_4_0._tf)
		arg_4_1())

def var_0_0.PlayNothing(arg_6_0):
	SetActive(arg_6_0._go, True)

def var_0_0.StopNothing(arg_7_0):
	SetActive(arg_7_0._go, False)

def var_0_0.Play(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4):
	if not arg_8_0.CanPlay():
		var_0_8("can not play guide " .. arg_8_1)
		arg_8_3()

		return

	var_0_8("play guide . " .. arg_8_1)

	local var_8_0 = var_0_10(arg_8_1)

	arg_8_0.PlayScript(var_8_0, arg_8_2, arg_8_3, arg_8_4)

def var_0_0._Play(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4):
	local var_9_0 = Guide.New(arg_9_1)

	arg_9_0.PlayScript(var_9_0, arg_9_2, arg_9_3, arg_9_4)

def var_0_0.PlayScript(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4):
	if not arg_10_1:
		var_0_8("should exist guide file ")
		arg_10_3()

		return

	arg_10_0.OnFailed = arg_10_4

	arg_10_0.OnStart()

	local var_10_0 = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_1.GetStepsWithCode(arg_10_2)):
		table.insert(var_10_0, function(arg_11_0)
			if arg_10_0.IsStop():
				return

			local var_11_0 = arg_10_0.players[iter_10_1.GetType()]

			var_11_0.Execute(iter_10_1, arg_11_0)

			arg_10_0.player = var_11_0)

	seriesAsync(var_10_0, function()
		arg_10_0.OnEnd(arg_10_3))

def var_0_0.CanPlay(arg_13_0):
	if pg.MsgboxMgr.GetInstance()._go.activeSelf or pg.NewStoryMgr.GetInstance().IsRunning() or not var_0_0.ENABLE_GUIDE or not arg_13_0.IsLoaded() or arg_13_0.IsPause() or arg_13_0.IsBusy():
		return False

	return True

def var_0_0.OnStart(arg_14_0):
	pg.DelegateInfo.New(arg_14_0)

	arg_14_0.state = var_0_4

	pg.m02.sendNotification(GAME.START_GUIDE)
	arg_14_0._go.transform.SetAsLastSibling()
	arg_14_0._go.SetActive(True)
	arg_14_0.uiLongPress.onLongPressed.AddListener(function()
		arg_14_0.Stop())

def var_0_0.OnEnd(arg_16_0, arg_16_1):
	arg_16_0.uiLongPress.onLongPressed.RemoveAllListeners()
	pg.DelegateInfo.Dispose(arg_16_0)

	arg_16_0.state = var_0_3

	arg_16_0.Clear()

	if arg_16_1:
		arg_16_1()

def var_0_0.Pause(arg_17_0):
	if arg_17_0.IsBusy():
		arg_17_0.state = var_0_6

		SetActive(arg_17_0._go, False)

def var_0_0.Resume(arg_18_0):
	if arg_18_0.IsPause():
		arg_18_0.state = var_0_4

		SetActive(arg_18_0._go, True)

def var_0_0.Stop(arg_19_0):
	if arg_19_0.state != var_0_5:
		if arg_19_0.OnFailed:
			arg_19_0.OnFailed()

		arg_19_0.state = var_0_5

		arg_19_0.uiFinder.Clear()
		arg_19_0.uiDuplicator.Clear()
		arg_19_0.uiLoader.Clear()
		arg_19_0.Clear()

def var_0_0.NextStep(arg_20_0):
	if not IsUnityEditor:
		return

	if arg_20_0.state == var_0_4 and arg_20_0.player:
		arg_20_0.player.NextOne()

def var_0_0.Clear(arg_21_0):
	arg_21_0.OnFailed = None
	arg_21_0.sceneRecords = {}

	arg_21_0._go.SetActive(False)

	for iter_21_0, iter_21_1 in ipairs(arg_21_0.players):
		iter_21_1.Clear()

	if arg_21_0.player:
		arg_21_0.player = None

	pg.m02.sendNotification(GAME.END_GUIDE)

def var_0_0.IsPause(arg_22_0):
	return arg_22_0.state and arg_22_0.state == var_0_6

def var_0_0.IsBusy(arg_23_0):
	return arg_23_0.state and arg_23_0.state == var_0_4

def var_0_0.IsLoaded(arg_24_0):
	return arg_24_0.state and arg_24_0.state > var_0_2

def var_0_0.IsStop(arg_25_0):
	return arg_25_0.state and arg_25_0.state == var_0_5

def var_0_0.OnSceneEnter(arg_26_0, arg_26_1):
	if not arg_26_0.IsLoaded():
		return

	if not table.contains(arg_26_0.sceneRecords, arg_26_1.view):
		table.insert(arg_26_0.sceneRecords, arg_26_1.view)

	if arg_26_0.player:
		arg_26_0.player.OnSceneEnter()

def var_0_0.OnSceneExit(arg_27_0, arg_27_1):
	if not arg_27_0.IsLoaded():
		return

	if table.contains(arg_27_0.sceneRecords, arg_27_1.view):
		table.removebyvalue(arg_27_0.sceneRecords, arg_27_1.view)

def var_0_0.ExistScene(arg_28_0, arg_28_1):
	return table.contains(arg_28_0.sceneRecords, arg_28_1)

def var_0_0.Exit(arg_29_0):
	arg_29_0.Clear()
	arg_29_0.uiFinder.Clear()
	arg_29_0.uiDuplicator.Clear()
	arg_29_0.uiLoader.Clear()

	arg_29_0.state = var_0_7
