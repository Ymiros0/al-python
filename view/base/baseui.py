local var_0_0 = class("BaseUI", import("view.base.BaseEventLogic"))

var_0_0.LOADED = "BaseUI.LOADED"
var_0_0.DID_ENTER = "BaseUI.DID_ENTER"
var_0_0.AVALIBLE = "BaseUI.AVALIBLE"
var_0_0.DID_EXIT = "BaseUI.DID_EXIT"
var_0_0.ON_BACK = "BaseUI.ON_BACK"
var_0_0.ON_RETURN = "BaseUI.ON_RETURN"
var_0_0.ON_HOME = "BaseUI.ON_HOME"
var_0_0.ON_CLOSE = "BaseUI.ON_CLOSE"
var_0_0.ON_DROP = "BaseUI.ON_DROP"
var_0_0.ON_DROP_LIST = "BaseUI.ON_DROP_LIST"
var_0_0.ON_DROP_LIST_OWN = "BaseUI.ON_DROP_LIST_OWN"
var_0_0.ON_ITEM = "BaseUI.ON_ITEM"
var_0_0.ON_ITEM_EXTRA = "BaseUI.ON_ITEM_EXTRA"
var_0_0.ON_SHIP = "BaseUI.ON_SHIP"
var_0_0.ON_AWARD = "BaseUI.ON_AWARD"
var_0_0.ON_ACHIEVE = "BaseUI.ON_ACHIEVE"
var_0_0.ON_WORLD_ACHIEVE = "BaseUI.ON_WORLD_ACHIEVE"
var_0_0.ON_EQUIPMENT = "BaseUI.ON_EQUIPMENT"
var_0_0.ON_SPWEAPON = "BaseUI.ON_SPWEAPON"
var_0_0.ON_SHIP_EXP = "BaseUI.ON_SHIP_EXP"
var_0_0.ON_BACK_PRESSED = "BaseUI.ON_BACK_PRESS"

def var_0_0.Ctor(arg_1_0):
	var_0_0.super.Ctor(arg_1_0)

	arg_1_0._isLoaded = False
	arg_1_0._go = None
	arg_1_0._tf = None
	arg_1_0._isCachedView = False

def var_0_0.setContextData(arg_2_0, arg_2_1):
	arg_2_0.contextData = arg_2_1

def var_0_0.getUIName(arg_3_0):
	return None

def var_0_0.needCache(arg_4_0):
	return False

def var_0_0.forceGC(arg_5_0):
	return False

def var_0_0.tempCache(arg_6_0):
	return False

def var_0_0.getGroupName(arg_7_0):
	return None

def var_0_0.getLayerWeight(arg_8_0):
	return LayerWeightConst.BASE_LAYER

def var_0_0.preload(arg_9_0, arg_9_1):
	arg_9_1()

def var_0_0.loadUISync(arg_10_0, arg_10_1):
	local var_10_0 = LoadAndInstantiateSync("UI", arg_10_1, True, False)
	local var_10_1 = pg.UIMgr.GetInstance().UIMain

	var_10_0.transform.SetParent(var_10_1.transform, False)

	return var_10_0

def var_0_0.load(arg_11_0):
	local var_11_0
	local var_11_1 = Time.realtimeSinceStartup
	local var_11_2 = arg_11_0.getUIName()

	seriesAsync({
		function(arg_12_0)
			arg_11_0.preload(arg_12_0),
		function(arg_13_0)
			arg_11_0.LoadUIFromPool(var_11_2, function(arg_14_0)
				print("Loaded " .. var_11_2)

				var_11_0 = arg_14_0

				arg_13_0())
	}, function()
		originalPrint("load " .. var_11_0.name .. " time cost. " .. Time.realtimeSinceStartup - var_11_1)

		local var_15_0 = pg.UIMgr.GetInstance().UIMain

		var_11_0.transform.SetParent(var_15_0.transform, False)

		if arg_11_0.tempCache():
			PoolMgr.GetInstance().AddTempCache(var_11_2)

		arg_11_0.onUILoaded(var_11_0))

def var_0_0.LoadUIFromPool(arg_16_0, arg_16_1, arg_16_2):
	PoolMgr.GetInstance().GetUI(arg_16_1, True, arg_16_2)

def var_0_0.getBGM(arg_17_0, arg_17_1):
	return getBgm(arg_17_1 or arg_17_0.__cname)

def var_0_0.PlayBGM(arg_18_0):
	local var_18_0 = arg_18_0.getBGM()

	if var_18_0:
		pg.BgmMgr.GetInstance().Push(arg_18_0.__cname, var_18_0)

def var_0_0.StopBgm(arg_19_0):
	if not arg_19_0.contextData:
		return

	if arg_19_0.contextData.isLayer:
		pg.BgmMgr.GetInstance().Pop(arg_19_0.__cname)
	else
		pg.BgmMgr.GetInstance().Clear()

def var_0_0.SwitchToDefaultBGM(arg_20_0):
	local var_20_0 = arg_20_0.getBGM()

	if not var_20_0:
		if pg.CriMgr.GetInstance().IsDefaultBGM():
			var_20_0 = pg.voice_bgm.NewMainScene.default_bgm
		else
			var_20_0 = pg.voice_bgm.NewMainScene.bgm

	pg.BgmMgr.GetInstance().Push(arg_20_0.__cname, var_20_0)

def var_0_0.isLoaded(arg_21_0):
	return arg_21_0._isLoaded

def var_0_0.getGroupNameFromData(arg_22_0):
	local var_22_0

	if arg_22_0.contextData != None and arg_22_0.contextData.LayerWeightMgr_groupName:
		var_22_0 = arg_22_0.contextData.LayerWeightMgr_groupName
	else
		var_22_0 = arg_22_0.getGroupName()

	return var_22_0

def var_0_0.getWeightFromData(arg_23_0):
	local var_23_0

	if arg_23_0.contextData != None and arg_23_0.contextData.LayerWeightMgr_weight:
		var_23_0 = arg_23_0.contextData.LayerWeightMgr_weight
	else
		var_23_0 = arg_23_0.getLayerWeight()

	return var_23_0

def var_0_0.isLayer(arg_24_0):
	return arg_24_0.contextData != None and arg_24_0.contextData.isLayer and not arg_24_0.contextData.isSubView

def var_0_0.addToLayerMgr(arg_25_0):
	local var_25_0 = arg_25_0.getGroupNameFromData()
	local var_25_1 = arg_25_0.getWeightFromData()

	pg.LayerWeightMgr.GetInstance().Add2Overlay(LayerWeightConst.UI_TYPE_SYSTEM, arg_25_0._tf, {
		globalBlur = False,
		groupName = var_25_0,
		weight = var_25_1
	})

var_0_0.optionsPath = {
	"option",
	"top/option",
	"top/left_top/option",
	"blur_container/top/title/option",
	"blur_container/top/option",
	"top/top/option",
	"common/top/option",
	"blur_panel/top/option",
	"blurPanel/top/option",
	"blur_container/top/option",
	"top/title/option",
	"blur_panel/adapt/top/option",
	"mainPanel/top/option",
	"bg/top/option",
	"blur_container/adapt/top/title/option",
	"blur_container/adapt/top/option",
	"ForNorth/top/option",
	"top/top_chapter/option",
	"Main/blur_panel/adapt/top/option"
}

def var_0_0.onUILoaded(arg_26_0, arg_26_1):
	arg_26_0._go = arg_26_1
	arg_26_0._tf = arg_26_1 and arg_26_1.transform

	if arg_26_0.isLayer():
		arg_26_0.addToLayerMgr()

	pg.SeriesGuideMgr.GetInstance().dispatch({
		view = arg_26_0.__cname
	})
	pg.NewStoryMgr.GetInstance().OnSceneEnter({
		view = arg_26_0.__cname
	})

	arg_26_0._isLoaded = True

	pg.DelegateInfo.New(arg_26_0)

	arg_26_0.optionBtns = {}

	for iter_26_0, iter_26_1 in ipairs(arg_26_0.optionsPath):
		table.insert(arg_26_0.optionBtns, arg_26_0.findTF(iter_26_1))

	setActiveViaLayer(arg_26_0._tf, True)
	arg_26_0.init()
	arg_26_0.emit(var_0_0.LOADED)

def var_0_0.ResUISettings(arg_27_0):
	return None

def var_0_0.ShowOrHideResUI(arg_28_0, arg_28_1):
	local var_28_0 = arg_28_0.ResUISettings()

	if not var_28_0:
		return

	if var_28_0 == True:
		var_28_0 = {
			anim = True,
			showType = PlayerResUI.TYPE_ALL
		}

	pg.playerResUI.SetActive(setmetatable({
		active = arg_28_1,
		clear = not arg_28_1 and not arg_28_0.isLayer(),
		weight = var_28_0.weight or arg_28_0.getWeightFromData(),
		groupName = var_28_0.groupName or arg_28_0.getGroupNameFromData(),
		canvasOrder = var_28_0.order or False
	}, {
		__index = var_28_0
	}))

def var_0_0.onUIAnimEnd(arg_29_0, arg_29_1):
	arg_29_1()

def var_0_0.init(arg_30_0):
	return

def var_0_0.quickExitFunc(arg_31_0):
	arg_31_0.emit(var_0_0.ON_HOME)

def var_0_0.quickExit(arg_32_0):
	for iter_32_0, iter_32_1 in ipairs(arg_32_0.optionBtns):
		onButton(arg_32_0, iter_32_1, function()
			arg_32_0.quickExitFunc(), SFX_PANEL)

def var_0_0.enter(arg_34_0):
	arg_34_0.quickExit()
	arg_34_0.PlayBGM()

	local function var_34_0()
		arg_34_0.emit(var_0_0.DID_ENTER)

		if not arg_34_0._isCachedView:
			arg_34_0.didEnter()
			arg_34_0.ShowOrHideResUI(True)

		arg_34_0.emit(var_0_0.AVALIBLE)
		arg_34_0.onUIAnimEnd(function()
			pg.SeriesGuideMgr.GetInstance().start({
				view = arg_34_0.__cname,
				code = {
					pg.SeriesGuideMgr.CODES.MAINUI
				}
			})
			pg.NewGuideMgr.GetInstance().OnSceneEnter({
				view = arg_34_0.__cname
			}))

	local var_34_1 = False

	if not IsNil(arg_34_0._tf.GetComponent(typeof(Animation))):
		arg_34_0.animTF = arg_34_0._tf
	else
		arg_34_0.animTF = arg_34_0.findTF("blur_panel")

	if arg_34_0.animTF != None:
		local var_34_2 = arg_34_0.animTF.GetComponent(typeof(Animation))
		local var_34_3 = arg_34_0.animTF.GetComponent(typeof(UIEventTrigger))

		if var_34_2 != None and var_34_3 != None:
			if var_34_2.get_Item("enter") == None:
				originalPrint("cound not found enter animation")
			else
				var_34_2.Play("enter")
		elif var_34_2 != None:
			originalPrint("cound not found [UIEventTrigger] component")
		elif var_34_3 != None:
			originalPrint("cound not found [Animation] component")

	if not var_34_1:
		var_34_0()

def var_0_0.closeView(arg_37_0):
	if arg_37_0.contextData.isLayer:
		arg_37_0.emit(var_0_0.ON_CLOSE)
	else
		arg_37_0.emit(var_0_0.ON_BACK)

def var_0_0.didEnter(arg_38_0):
	return

def var_0_0.willExit(arg_39_0):
	return

def var_0_0.exit(arg_40_0):
	arg_40_0.exited = True

	arg_40_0.StopBgm()
	pg.DelegateInfo.Dispose(arg_40_0)

	local function var_40_0()
		arg_40_0.willExit()
		arg_40_0.ShowOrHideResUI(False)
		arg_40_0.detach()
		pg.NewGuideMgr.GetInstance().OnSceneExit({
			view = arg_40_0.__cname
		})
		pg.NewStoryMgr.GetInstance().OnSceneExit({
			view = arg_40_0.__cname
		})
		arg_40_0.emit(var_0_0.DID_EXIT)

	local var_40_1 = False

	if not var_40_1:
		var_40_0()

def var_0_0.PlayExitAnimation(arg_42_0, arg_42_1):
	local var_42_0 = arg_42_0._tf.GetComponent(typeof(Animation))
	local var_42_1 = arg_42_0._tf.GetComponent(typeof(UIEventTrigger))

	var_42_1.didExit.RemoveAllListeners()
	var_42_1.didExit.AddListener(function()
		var_42_1.didExit.RemoveAllListeners()
		arg_42_1())
	var_42_0.Play("exit")

def var_0_0.attach(arg_44_0, arg_44_1):
	return

def var_0_0.ClearTweens(arg_45_0, arg_45_1):
	arg_45_0.cleanManagedTween(arg_45_1)

def var_0_0.RemoveTempCache(arg_46_0):
	local var_46_0 = arg_46_0.getUIName()

	PoolMgr.GetInstance().DelTempCache(var_46_0)

def var_0_0.detach(arg_47_0, arg_47_1):
	arg_47_0._isLoaded = False

	pg.LayerWeightMgr.GetInstance().DelFromOverlay(arg_47_0._tf)
	pg.DynamicBgMgr.GetInstance().ClearBg(arg_47_0.getUIName())
	arg_47_0.disposeEvent()
	arg_47_0.ClearTweens(False)

	arg_47_0._tf = None

	local var_47_0 = PoolMgr.GetInstance()
	local var_47_1 = arg_47_0.getUIName()

	if arg_47_0._go != None and var_47_1:
		var_47_0.ReturnUI(var_47_1, arg_47_0._go)

		arg_47_0._go = None

def var_0_0.findGO(arg_48_0, arg_48_1, arg_48_2):
	assert(arg_48_0._go, "game object should exist")

	return findGO(arg_48_2 or arg_48_0._go, arg_48_1)

def var_0_0.findTF(arg_49_0, arg_49_1, arg_49_2):
	assert(arg_49_0._tf, "transform should exist")

	return findTF(arg_49_2 or arg_49_0._tf, arg_49_1)

def var_0_0.getTpl(arg_50_0, arg_50_1, arg_50_2):
	local var_50_0 = arg_50_0.findTF(arg_50_1, arg_50_2)

	var_50_0.SetParent(arg_50_0._tf, False)
	SetActive(var_50_0, False)

	return var_50_0

def var_0_0.setSpriteTo(arg_51_0, arg_51_1, arg_51_2, arg_51_3):
	local var_51_0 = arg_51_2.GetComponent(typeof(Image))

	var_51_0.sprite = arg_51_0.findTF(arg_51_1).GetComponent(typeof(Image)).sprite

	if arg_51_3:
		var_51_0.SetNativeSize()

def var_0_0.setImageAmount(arg_52_0, arg_52_1, arg_52_2):
	arg_52_1.GetComponent(typeof(Image)).fillAmount = arg_52_2

def var_0_0.setVisible(arg_53_0, arg_53_1):
	arg_53_0.ShowOrHideResUI(arg_53_1)

	if arg_53_1:
		arg_53_0.OnVisible()
	else
		arg_53_0.OnDisVisible()

	setActiveViaLayer(arg_53_0._tf, arg_53_1)

def var_0_0.OnVisible(arg_54_0):
	return

def var_0_0.OnDisVisible(arg_55_0):
	return

def var_0_0.onBackPressed(arg_56_0):
	arg_56_0.emit(var_0_0.ON_BACK_PRESSED)

return var_0_0
