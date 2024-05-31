local var_0_0 = class("MainMeshImagePainting", import(".MainBasePainting"))

var_0_0.DEFAULT_HEIGHT = 0
var_0_0.TOUCH_HEIGHT = 20
var_0_0.TOUCH_LOOP = 1
var_0_0.TOUCH_DURATION = 0.1
var_0_0.CHAT_HEIGHT = 15
var_0_0.CHAT_DURATION = 0.3
var_0_0.BREATH_HEIGHT = -10
var_0_0.BREATH_DURATION = 2.3
var_0_0.PAINTING_VARIANT_NORMAL = 0
var_0_0.PAINTING_VARIANT_EX = 1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.uiCamera = GameObject.Find("UICamera").GetComponent(typeof(Camera))

def var_0_0.StaticGetPaintingName(arg_2_0):
	local var_2_0 = arg_2_0

	if checkABExist("painting/" .. var_2_0 .. "_n") and PlayerPrefs.GetInt("paint_hide_other_obj_" .. var_2_0, 0) != 0:
		var_2_0 = var_2_0 .. "_n"

	if HXSet.isHx():
		return var_2_0

	local var_2_1 = getProxy(SettingsProxy).GetMainPaintingVariantFlag(arg_2_0) == var_0_0.PAINTING_VARIANT_EX

	if var_2_1 and not checkABExist("painting/" .. var_2_0 .. "_ex"):
		return var_2_0

	return var_2_1 and var_2_0 .. "_ex" or var_2_0

def var_0_0.GetPaintingName(arg_3_0):
	return var_0_0.StaticGetPaintingName(arg_3_0.paintingName)

def var_0_0.OnLoad(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.GetPaintingName()

	LoadPaintingPrefabAsync(arg_4_0.container, arg_4_0.paintingName, var_4_0, "mainNormal", function()
		if arg_4_0.IsExited():
			arg_4_0.UnLoad()

			return

		arg_4_0.loadPaintingName = var_4_0

		local var_5_0 = arg_4_0.InitSpecialTouch()

		arg_4_0.InitSpecialDrag(var_5_0)

		if arg_4_0.expression:
			ShipExpressionHelper.UpdateExpression(findTF(arg_4_0.container, "fitter").GetChild(0), arg_4_0.paintingName, arg_4_0.expression)

		arg_4_0.Breath()
		arg_4_1())

def var_0_0.GetCenterPos(arg_6_0):
	if arg_6_0.IsLoaded():
		local var_6_0 = arg_6_0.container.Find("fitter").GetChild(0)
		local var_6_1 = (0.5 - var_6_0.pivot.x) * var_6_0.sizeDelta.x
		local var_6_2 = var_6_0.localPosition + Vector3(var_6_1, 0, 0)

		return (var_6_0.TransformPoint(var_6_2))
	else
		return var_0_0.super.GetCenterPos(arg_6_0)

def var_0_0.InitSpecialTouch(arg_7_0):
	local var_7_0 = findTF(findTF(arg_7_0.container, "fitter").GetChild(0), "Touch")

	if not var_7_0:
		return

	setActive(var_7_0, True)

	local var_7_1 = {}

	eachChild(var_7_0, function(arg_8_0)
		onButton(arg_7_0, arg_8_0, function()
			local var_9_0 = arg_7_0.GetSpecialTouchEvent(arg_8_0.name)

			arg_7_0.TriggerEvent(var_9_0)
			arg_7_0.TriggerPersonalTask(arg_7_0.ship.groupId))

		var_7_1[arg_8_0] = arg_8_0.rect)

	return var_7_1

def var_0_0.InitSpecialDrag(arg_10_0, arg_10_1):
	local var_10_0 = findTF(findTF(arg_10_0.container, "fitter").GetChild(0), "Drag")

	if not var_10_0:
		return

	if PLATFORM_CODE == PLATFORM_CH and HXSet.isHx():
		setActive(var_10_0, False)

		return

	setActive(var_10_0, True)

	local var_10_1 = GetOrAddComponent(var_10_0, typeof(EventTriggerListener))
	local var_10_2 = Vector2(0, 0)

	arg_10_0.isDrag = False

	var_10_1.AddBeginDragFunc(function(arg_11_0, arg_11_1)
		arg_10_0.isDrag = True
		var_10_2 = arg_11_1.position)
	var_10_1.AddDragEndFunc(function(arg_12_0, arg_12_1)
		arg_10_0.isDrag = False

		local var_12_0 = arg_12_1.position - var_10_2

		if math.abs(var_12_0.x) > 50 or math.abs(var_12_0.y) > 50:
			arg_10_0.SwitchToVariant(var_10_0))

	if arg_10_1 and table.getCount(arg_10_1) > 0:
		var_10_1.AddPointUpFunc(function(arg_13_0, arg_13_1)
			if arg_10_0.isDrag:
				return

			local var_13_0

			for iter_13_0, iter_13_1 in pairs(arg_10_1):
				local var_13_1 = LuaHelper.ScreenToLocal(iter_13_0, arg_13_1.position, arg_10_0.uiCamera)

				if iter_13_1.Contains(var_13_1):
					var_13_0 = iter_13_0

					break

			if var_13_0:
				triggerButton(var_13_0)
			else
				triggerButton(arg_10_0.container))

	local var_10_3 = GetOrAddComponent(var_10_0, "UILongPressTrigger").onLongPressed

	var_10_3.RemoveAllListeners()
	var_10_3.AddListener(function()
		arg_10_0.OnLongPress())

def var_0_0.SwitchToVariant(arg_15_0, arg_15_1):
	pg.UIMgr.GetInstance().LoadingOn(False)
	getProxy(SettingsProxy).SwitchMainPaintingVariantFlag(arg_15_0.paintingName)
	seriesAsync({
		function(arg_16_0)
			local var_16_0 = arg_15_0.GetPaintingName()

			PoolMgr.GetInstance().PreloadPainting(var_16_0, arg_16_0),
		function(arg_17_0)
			arg_15_0.PlayVariantEffect(arg_15_1, arg_17_0),
		function(arg_18_0)
			onDelayTick(arg_18_0, 0.5),
		function(arg_19_0)
			arg_15_0.UnloadOnlyPainting()
			arg_15_0.Load(arg_15_0.ship, True)
			onDelayTick(arg_19_0, 1)
	}, function()
		arg_15_0.ClearEffect()
		pg.UIMgr.GetInstance().LoadingOff())

def var_0_0.PlayVariantEffect(arg_21_0, arg_21_1, arg_21_2):
	local var_21_0 = getProxy(SettingsProxy).GetMainPaintingVariantFlag(arg_21_0.paintingName) == var_0_0.PAINTING_VARIANT_EX
	local var_21_1 = var_21_0 and "lihui_qiehuan01" or "lihui_qiehuan02"

	pg.PoolMgr.GetInstance().GetPrefab("ui/" .. var_21_1, "", True, function(arg_22_0)
		pg.ViewUtils.SetLayer(arg_22_0.transform, Layer.UI)

		arg_21_0.effectGo = arg_22_0
		arg_21_0.effectGo.name = var_21_1

		if arg_21_0.IsExited():
			arg_21_0.ClearEffect()

			return

		setParent(arg_22_0, arg_21_0.container)

		arg_21_0.effectGo.transform.position = arg_21_1.position

		if var_21_0:
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_EXPLOSIVE_SKIN)
		else
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_ANTI_EXPLOSIVE_SKIN)

		arg_21_2())

def var_0_0.ClearEffect(arg_23_0):
	if arg_23_0.effectTimer:
		arg_23_0.effectTimer.Stop()

		arg_23_0.effectTimer = None

	if arg_23_0.effectGo:
		pg.PoolMgr.GetInstance().ReturnPrefab("ui/" .. arg_23_0.effectGo.name, "", arg_23_0.effectGo)

		arg_23_0.effectGo = None

def var_0_0.ClearSpecialDrag(arg_24_0):
	if PLATFORM_CODE == PLATFORM_CH and HXSet.isHx():
		return

	local var_24_0 = findTF(findTF(arg_24_0.container, "fitter").GetChild(0), "Drag")

	if not var_24_0:
		return

	local var_24_1 = GetOrAddComponent(var_24_0, typeof(EventTriggerListener))

	var_24_1.AddBeginDragFunc(None)
	var_24_1.AddDragEndFunc(None)
	var_24_1.AddPointUpFunc(None)
	GetOrAddComponent(var_24_0, "UILongPressTrigger").onLongPressed.RemoveAllListeners()

def var_0_0.OnClick(arg_25_0):
	local var_25_0 = arg_25_0.CollectTouchEvents()
	local var_25_1 = var_25_0[math.ceil(math.random(#var_25_0))]

	arg_25_0.TriggerEvent(var_25_1)

def var_0_0.OnLongPress(arg_26_0):
	if arg_26_0.isFoldState:
		return

	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
		shipId = arg_26_0.ship.id
	})

def var_0_0.OnDisplayWorld(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_0.ship.getCVIntimacy()
	local var_27_1, var_27_2 = ShipExpressionHelper.SetExpression(findTF(arg_27_0.container, "fitter").GetChild(0), arg_27_0.paintingName, arg_27_1, var_27_0, arg_27_0.ship.skinId)

	arg_27_0.expression = var_27_2

def var_0_0.OnTriggerEvent(arg_28_0):
	arg_28_0.Shake(var_0_0.TOUCH_HEIGHT, var_0_0.TOUCH_DURATION, var_0_0.TOUCH_LOOP)

def var_0_0.OnTriggerEventAuto(arg_29_0):
	arg_29_0.Shake(var_0_0.CHAT_HEIGHT, var_0_0.CHAT_DURATION)

def var_0_0.GetMeshPainting(arg_30_0):
	local var_30_0 = findTF(arg_30_0.container, "fitter")

	if var_30_0.childCount <= 0:
		return None

	return (var_30_0.GetChild(0))

def var_0_0.Shake(arg_31_0, arg_31_1, arg_31_2, arg_31_3):
	local var_31_0
	local var_31_1 = arg_31_1

	if var_31_0:
		var_31_1 = arg_31_1 - var_0_0.DEFAULT_HEIGHT + var_31_0

	arg_31_3 = arg_31_3 or math.random(3) - 1

	if arg_31_3 == 0:
		return

	local var_31_2 = arg_31_0.GetMeshPainting()

	if not var_31_2:
		return

	LeanTween.cancel(go(var_31_2))
	LeanTween.moveY(rtf(var_31_2), var_31_1, 0.1).setLoopPingPong(arg_31_3).setOnComplete(System.Action(function()
		arg_31_0.Breath()))

def var_0_0.Breath(arg_33_0):
	local var_33_0 = arg_33_0.GetMeshPainting()

	if not var_33_0:
		return

	local var_33_1
	local var_33_2 = var_33_1 or var_0_0.BREATH_HEIGHT
	local var_33_3 = var_33_1 and var_33_1 - 10 or var_0_0.DEFAULT_HEIGHT

	LeanTween.cancel(go(var_33_0))
	LeanTween.moveY(rtf(var_33_0), var_33_3, var_0_0.BREATH_DURATION).setLoopPingPong().setEase(LeanTweenType.easeInOutCubic).setFrom(var_33_2)

def var_0_0.StopBreath(arg_34_0):
	local var_34_0 = arg_34_0.GetMeshPainting()

	if not var_34_0:
		return

	LeanTween.cancel(go(var_34_0))

def var_0_0.OnEnableOrDisableDragAndZoom(arg_35_0, arg_35_1):
	if arg_35_1:
		arg_35_0.StopBreath()
	else
		arg_35_0.Breath()

def var_0_0.OnFold(arg_36_0, arg_36_1):
	if not arg_36_1:
		arg_36_0.Breath()

def var_0_0.GetOffset(arg_37_0):
	return MainPaintingView.MESH_POSITION_X_OFFSET

def var_0_0.OnPuase(arg_38_0):
	arg_38_0.StopBreath()

def var_0_0.OnResume(arg_39_0):
	checkCullResume(arg_39_0.container.Find("fitter").GetChild(0))
	arg_39_0.Breath()

def var_0_0.Unload(arg_40_0):
	var_0_0.super.Unload(arg_40_0)

	arg_40_0.expression = None

def var_0_0.OnUnload(arg_41_0):
	arg_41_0.StopBreath()
	arg_41_0.ClearSpecialDrag()

	if arg_41_0.loadPaintingName:
		retPaintingPrefab(arg_41_0.container, arg_41_0.loadPaintingName)

		arg_41_0.loadPaintingName = None

def var_0_0.OnPuase(arg_42_0):
	arg_42_0.ClearEffect()

def var_0_0.Dispose(arg_43_0):
	var_0_0.super.Dispose(arg_43_0)
	arg_43_0.ClearEffect()

return var_0_0
