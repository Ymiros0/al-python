local var_0_0 = class("MainPaintingView", import("..base.MainBaseView"))

var_0_0.STATE_PAINTING = 1
var_0_0.STATE_L2D = 2
var_0_0.STATE_SPINE_PAINTING = 3
var_0_0.STATE_EDUCATE_CHAR = 4
var_0_0.MESH_POSITION_X_OFFSET = 145

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_3)

	arg_1_0._bgTf = arg_1_2
	arg_1_0._bgGo = arg_1_2.gameObject
	arg_1_0.l2dContainer = arg_1_1.Find("live2d")
	arg_1_0.spineContainer = arg_1_1.Find("spinePainting")
	arg_1_0.bgOffset = arg_1_0._bgTf.localPosition - arg_1_0._tf.localPosition
	arg_1_0.cg = arg_1_0._tf.GetComponent(typeof(CanvasGroup))
	arg_1_0.paintings = {
		MainMeshImagePainting.New(arg_1_0._tf, arg_1_0.event),
		MainLive2dPainting.New(arg_1_0._tf, arg_1_0.event),
		MainSpinePainting.New(arg_1_0._tf, arg_1_0.event, arg_1_0._bgGo),
		MainEducateCharPainting.New(arg_1_0._tf, arg_1_0.event)
	}

	arg_1_0.Register()

def var_0_0.Register(arg_2_0):
	arg_2_0.bind(TaskProxy.TASK_ADDED, function(arg_3_0)
		arg_2_0.OnStopVoice())
	arg_2_0.bind(NewMainScene.CHAT_STATE_CHANGE, function(arg_4_0, arg_4_1)
		arg_2_0.OnChatStateChange(arg_4_1))
	arg_2_0.bind(NewMainScene.ENABLE_PAITING_MOVE, function(arg_5_0, arg_5_1)
		arg_2_0.EnableOrDisableMove(arg_5_1))
	arg_2_0.bind(NewMainScene.ON_ENTER_DONE, function(arg_6_0)
		if arg_2_0.painting:
			arg_2_0.painting.TriggerEventAtFirstTime())
	arg_2_0.bind(NewMainScene.ENTER_SILENT_VIEW, function()
		arg_2_0.cg.blocksRaycasts = False
		arg_2_0.silentFlag = True

		for iter_7_0, iter_7_1 in ipairs(arg_2_0.paintings):
			iter_7_1.PauseForSilent())
	arg_2_0.bind(NewMainScene.EXIT_SILENT_VIEW, function()
		arg_2_0.cg.blocksRaycasts = True
		arg_2_0.silentFlag = False

		for iter_8_0, iter_8_1 in ipairs(arg_2_0.paintings):
			iter_8_1.ResumeForSilent())
	arg_2_0.bind(NewMainScene.RESET_L2D, function()
		if not arg_2_0.painting:
			return

		if not isa(arg_2_0.painting, MainLive2dPainting):
			return

		arg_2_0.painting.ResetState())

	function Live2dConst.UnLoadL2dPating()
		if not arg_2_0.reloadOnResume and arg_2_0.painting and isa(arg_2_0.painting, MainLive2dPainting):
			arg_2_0.painting.SetContainerVisible(False)

			arg_2_0.reloadOnResume = True

def var_0_0.OnChatStateChange(arg_11_0, arg_11_1):
	if not arg_11_1:
		arg_11_0.painting.StopChatAnimtion()

def var_0_0.OnStopVoice(arg_12_0):
	if arg_12_0.painting:
		arg_12_0.painting.OnStopVoice()

def var_0_0.IsLive2DState(arg_13_0):
	return var_0_0.STATE_L2D == arg_13_0.state

def var_0_0.IsLoading(arg_14_0):
	if arg_14_0.painting and arg_14_0.painting.IsLoading():
		return True

	return False

def var_0_0.Init(arg_15_0, arg_15_1, arg_15_2, arg_15_3):
	if arg_15_0.ShouldReLoad(arg_15_1):
		arg_15_0.Reload(arg_15_1)
	else
		arg_15_0.painting.Resume()

	arg_15_0.shift = arg_15_2 or arg_15_0.shift

	assert(arg_15_0.shift)

	if arg_15_3:
		arg_15_0.AdjustPositionWithAnim(arg_15_1)
	else
		arg_15_0.AdjustPosition(arg_15_1)

def var_0_0.Reload(arg_16_0, arg_16_1):
	arg_16_0.ship = arg_16_1

	local var_16_0, var_16_1 = var_0_0.GetAssistantStatus(arg_16_1)
	local var_16_2 = arg_16_0.paintings[var_16_0]

	if arg_16_0.painting:
		arg_16_0.painting.Unload()

	var_16_2.Load(arg_16_1)

	arg_16_0.painting = var_16_2
	arg_16_0.state = var_16_0
	arg_16_0.bgToggle = PlayerPrefs.GetInt("paint_hide_other_obj_" .. arg_16_0.painting.paintingName, 0)

def var_0_0.Refresh(arg_17_0, arg_17_1, arg_17_2):
	arg_17_0.Init(arg_17_1, arg_17_2)

def var_0_0.ShouldReLoad(arg_18_0, arg_18_1):
	if not arg_18_0.painting or not arg_18_0.ship or not arg_18_0.state or not arg_18_0.bgToggle:
		return True

	local var_18_0 = var_0_0.GetAssistantStatus(arg_18_1)
	local var_18_1 = PlayerPrefs.GetInt("paint_hide_other_obj_" .. arg_18_0.painting.paintingName, 0)

	if arg_18_1.skinId == arg_18_0.ship.skinId and arg_18_1.id == arg_18_0.ship.id and arg_18_0.state == var_18_0 and arg_18_0.bgToggle == var_18_1 and arg_18_1.GetRecordPosKey() == arg_18_0.ship.GetRecordPosKey() and not arg_18_0.reloadOnResume:
		return False
	else
		if arg_18_0.reloadOnResume:
			arg_18_0.reloadOnResume = False

		return True

def var_0_0.Disable(arg_19_0):
	if arg_19_0.painting:
		arg_19_0.painting.Puase()

def var_0_0.AdjustPositionWithAnim(arg_20_0, arg_20_1):
	LeanTween.cancel(go(arg_20_0._tf))
	LeanTween.cancel(go(arg_20_0._bgTf))

	local var_20_0 = arg_20_0.GetPositionAndScale(arg_20_1)

	LeanTween.moveLocal(go(arg_20_0._tf), var_20_0, 0.3).setEase(LeanTweenType.easeInOutExpo)
	LeanTween.moveLocal(go(arg_20_0._bgTf), var_20_0, 0.3).setEase(LeanTweenType.easeInOutExpo)

	local var_20_1, var_20_2 = arg_20_0.shift.GetL2dShift()

	LeanTween.moveLocal(go(arg_20_0.spineContainer), var_20_1, 0.3).setEase(LeanTweenType.easeInOutExpo)

	local var_20_3, var_20_4 = arg_20_0.shift.GetSpineShift()

	LeanTween.moveLocal(go(arg_20_0.l2dContainer), var_20_3, 0.3).setEase(LeanTweenType.easeInOutExpo).setOnComplete(System.Action(function()
		arg_20_0.AdjustPosition(arg_20_1)))

def var_0_0.AdjustPosition(arg_22_0, arg_22_1):
	local var_22_0, var_22_1 = arg_22_0.GetPositionAndScale(arg_22_1)

	arg_22_0._tf.anchoredPosition = var_22_0
	arg_22_0._bgTf.anchoredPosition = var_22_0

	local var_22_2, var_22_3 = arg_22_0.shift.GetL2dShift()

	arg_22_0.l2dContainer.anchoredPosition = var_22_2

	local var_22_4, var_22_5 = arg_22_0.shift.GetSpineShift()

	arg_22_0.spineContainer.anchoredPosition = var_22_4

	local var_22_6, var_22_7, var_22_8 = getProxy(SettingsProxy).getSkinPosSetting(arg_22_1)

	if var_22_8:
		arg_22_0._bgTf.localScale = Vector3(var_22_8, var_22_8, 1)
		arg_22_0._tf.localScale = Vector3(var_22_8, var_22_8, 1)
	elif arg_22_0.state == var_0_0.STATE_L2D:
		arg_22_0._bgTf.localScale = var_22_3
		arg_22_0._tf.localScale = var_22_3
	elif arg_22_0.state == var_0_0.STATE_SPINE_PAINTING:
		arg_22_0._bgTf.localScale = var_22_5
		arg_22_0._tf.localScale = var_22_5
	else
		arg_22_0._bgTf.localScale = var_22_1
		arg_22_0._tf.localScale = var_22_1

def var_0_0.GetPositionAndScale(arg_23_0, arg_23_1):
	local var_23_0, var_23_1, var_23_2 = getProxy(SettingsProxy).getSkinPosSetting(arg_23_1)
	local var_23_3 = Vector3(0, 0, 0)
	local var_23_4 = Vector3(1, 1, 1)

	if var_23_0:
		var_23_3 = Vector3(var_23_0, var_23_1, 0)
		var_23_4 = Vector3(var_23_2, var_23_2, 1)
	else
		local var_23_5, var_23_6 = arg_23_0.shift.GetMeshImageShift()

		var_23_3 = var_23_5
		var_23_4 = var_23_6

	return var_23_3, var_23_4

def var_0_0.GetAssistantStatus(arg_24_0):
	local var_24_0 = arg_24_0.getPainting()
	local var_24_1 = getProxy(SettingsProxy)
	local var_24_2 = HXSet.autoHxShiftPath("spinepainting/" .. var_24_0)
	local var_24_3 = checkABExist(var_24_2)
	local var_24_4 = HXSet.autoHxShiftPath("live2d/" .. var_24_0)
	local var_24_5 = var_0_0.Live2dIsDownload(var_24_4) and checkABExist(var_24_4)
	local var_24_6 = var_24_1.getCharacterSetting(arg_24_0.id, SHIP_FLAG_BG)

	if var_24_1.getCharacterSetting(arg_24_0.id, SHIP_FLAG_SP) and var_24_3:
		return var_0_0.STATE_SPINE_PAINTING, var_24_6
	elif var_24_1.getCharacterSetting(arg_24_0.id, SHIP_FLAG_L2D) and var_24_5:
		return var_0_0.STATE_L2D, var_24_6
	elif isa(arg_24_0, VirtualEducateCharShip):
		return var_0_0.STATE_EDUCATE_CHAR, var_24_6
	else
		return var_0_0.STATE_PAINTING, var_24_6

def var_0_0.Live2dIsDownload(arg_25_0):
	local var_25_0 = GroupHelper.GetGroupMgrByName("L2D").CheckF(arg_25_0)

	return var_25_0 == DownloadState.None or var_25_0 == DownloadState.UpdateSuccess

def var_0_0.Fold(arg_26_0, arg_26_1, arg_26_2):
	LeanTween.cancel(arg_26_0._tf.gameObject)
	LeanTween.cancel(arg_26_0._bgTf.gameObject)

	if arg_26_1 and not arg_26_0.silentFlag:
		local var_26_0 = arg_26_0._tf.localPosition - arg_26_0._bgTf.localPosition
		local var_26_1 = arg_26_0.shift.GetMeshImageShift()
		local var_26_2 = Vector3(0 - arg_26_0.painting.GetOffset(), var_26_1.y, 0)

		LeanTween.moveLocal(arg_26_0._tf.gameObject, var_26_2, arg_26_2).setEase(LeanTweenType.easeInOutExpo)

		local var_26_3 = var_26_2 - var_26_0

		LeanTween.moveLocal(arg_26_0._bgTf.gameObject, var_26_3, arg_26_2).setEase(LeanTweenType.easeInOutExpo).setOnComplete(System.Action(function()
			arg_26_0.painting.Fold(arg_26_1, arg_26_2)))
	elif arg_26_0.ship:
		local var_26_4 = arg_26_0.GetPositionAndScale(arg_26_0.ship)

		LeanTween.moveLocal(arg_26_0._tf.gameObject, var_26_4, arg_26_2).setEase(LeanTweenType.easeInOutExpo)
		LeanTween.moveLocal(arg_26_0._bgTf.gameObject, var_26_4, arg_26_2).setEase(LeanTweenType.easeInOutExpo).setOnComplete(System.Action(function()
			arg_26_0.painting.Fold(arg_26_1, arg_26_2)))

def var_0_0.EnableOrDisableMove(arg_29_0, arg_29_1):
	arg_29_0.painting.EnableOrDisableMove(arg_29_1)

	if arg_29_1:
		arg_29_0.EnableDragAndZoom()
	else
		arg_29_0.DisableDragAndZoom()

def var_0_0.EnableDragAndZoom(arg_30_0):
	arg_30_0.isEnableDrag = True

	local var_30_0 = arg_30_0._tf.parent.gameObject
	local var_30_1 = GetOrAddComponent(var_30_0, typeof(PinchZoom))
	local var_30_2 = GetOrAddComponent(var_30_0, typeof(EventTriggerListener))
	local var_30_3 = Vector3(0, 0, 0)

	var_30_2.AddBeginDragFunc(function(arg_31_0, arg_31_1)
		if Application.isEditor and Input.GetMouseButton(2):
			return

		if var_30_1.processing:
			return

		setButtonEnabled(var_30_0, False)

		if Input.touchCount > 1:
			return

		local var_31_0 = var_0_0.Screen2Local(var_30_0.transform.parent, arg_31_1.position)

		var_30_3 = arg_30_0._tf.localPosition - var_31_0)
	var_30_2.AddDragFunc(function(arg_32_0, arg_32_1)
		if Application.isEditor and Input.GetMouseButton(2):
			return

		if var_30_1.processing:
			return

		if Input.touchCount > 1:
			return

		local var_32_0 = var_0_0.Screen2Local(var_30_0.transform.parent, arg_32_1.position)

		arg_30_0._tf.localPosition = arg_30_0.painting.IslimitYPos() and Vector3(var_32_0.x, var_30_0.transform.localPosition.y, 0) + Vector3(var_30_3.x, 0, 0) or Vector3(var_32_0.x, var_32_0.y, 0) + var_30_3
		arg_30_0._bgTf.localPosition = arg_30_0.bgOffset + arg_30_0._tf.localPosition)
	var_30_2.AddDragEndFunc(function()
		setButtonEnabled(var_30_0, True))

	if not arg_30_0.painting.IslimitYPos():
		var_30_1.enabled = True

	var_30_2.enabled = True
	Input.multiTouchEnabled = True
	arg_30_0.cg.blocksRaycasts = False

	arg_30_0.AdjustPosition(arg_30_0.ship)

def var_0_0.DisableDragAndZoom(arg_34_0):
	if arg_34_0.isEnableDrag:
		local var_34_0 = arg_34_0._tf.parent.GetComponent(typeof(EventTriggerListener))

		ClearEventTrigger(var_34_0)

		var_34_0.enabled = False
		arg_34_0._tf.parent.GetComponent(typeof(PinchZoom)).enabled = False
		arg_34_0.cg.blocksRaycasts = True
		arg_34_0.isEnableDrag = False

def var_0_0.Dispose(arg_35_0):
	var_0_0.super.Dispose(arg_35_0)
	arg_35_0.DisableDragAndZoom()

	if arg_35_0.painting:
		arg_35_0.painting.Unload()

	arg_35_0.painting = None

	for iter_35_0, iter_35_1 in ipairs(arg_35_0.paintings):
		iter_35_1.Dispose()

	arg_35_0.paintings = None

def var_0_0.Screen2Local(arg_36_0, arg_36_1):
	local var_36_0 = GameObject.Find("UICamera").GetComponent("Camera")
	local var_36_1 = arg_36_0.GetComponent("RectTransform")
	local var_36_2 = LuaHelper.ScreenToLocal(var_36_1, arg_36_1, var_36_0)

	return Vector3(var_36_2.x, var_36_2.y, 0)

return var_0_0
