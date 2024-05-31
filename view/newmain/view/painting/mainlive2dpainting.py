local var_0_0 = class("MainLive2dPainting", import(".MainBasePainting"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.live2dContainer = arg_1_1.Find("live2d")
	arg_1_0.cg = arg_1_0.live2dContainer.GetComponent(typeof(CanvasGroup))
	arg_1_0.currentWidth = Screen.width
	arg_1_0.currentHeight = Screen.height
	arg_1_0.isModifyOrder = False
	arg_1_0.actionWaiting = False
	arg_1_0.eventTrigger = GetOrAddComponent(arg_1_0.live2dContainer, typeof(EventTriggerListener))

	arg_1_0.eventTrigger.AddPointClickFunc(function()
		arg_1_0.OnClick()
		arg_1_0.TriggerPersonalTask(arg_1_0.ship.groupId))

def var_0_0.GetHalfBodyOffsetY(arg_3_0):
	local var_3_0 = arg_3_0.container.parent
	local var_3_1 = var_3_0.rect.height * -0.5
	local var_3_2 = var_3_0.InverseTransformPoint(arg_3_0.live2dContainer.position)
	local var_3_3 = arg_3_0.live2dContainer.localScale

	return var_3_1 - (arg_3_0.live2dContainer.rect.height * -0.5 * var_3_3.y + var_3_2.y)

def var_0_0.OnLoad(arg_4_0, arg_4_1):
	local var_4_0 = Live2D.GenerateData({
		loadPrefs = True,
		ship = arg_4_0.ship,
		scale = Vector3(52, 52, 52),
		position = Vector3(0, 0, 100),
		parent = arg_4_0.live2dContainer
	})

	arg_4_0.SetContainerVisible(True)

	arg_4_0.cg.blocksRaycasts = True
	arg_4_0.live2dChar = Live2D.New(var_4_0, function(arg_5_0)
		arg_4_0.AdJustOrderInLayer(arg_5_0)
		arg_4_1())
	arg_4_0.shipGroup = getProxy(CollectionProxy).getShipGroup(arg_4_0.ship.groupId)

	arg_4_0.UpdateContainerPosition()
	arg_4_0.AddScreenChangeTimer()

def var_0_0.ResetState(arg_6_0):
	if not arg_6_0.live2dChar:
		return

	arg_6_0.live2dChar.resetL2dData()

def var_0_0.AdJustOrderInLayer(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.container.GetComponent(typeof(Canvas))

	if var_7_0 and var_7_0.overrideSorting and var_7_0.sortingOrder != 0:
		local var_7_1 = arg_7_1._go.GetComponent("Live2D.Cubism.Rendering.CubismRenderController")
		local var_7_2 = var_7_0.sortingOrder
		local var_7_3 = typeof("Live2D.Cubism.Rendering.CubismRenderController")

		ReflectionHelp.RefSetProperty(var_7_3, "SortingOrder", var_7_1, var_7_2)

		arg_7_0.isModifyOrder = True

def var_0_0.ResetOrderInLayer(arg_8_0):
	if not arg_8_0.live2dChar:
		return

	local var_8_0 = arg_8_0.live2dChar._go.GetComponent("Live2D.Cubism.Rendering.CubismRenderController")
	local var_8_1 = typeof("Live2D.Cubism.Rendering.CubismRenderController")

	ReflectionHelp.RefSetProperty(var_8_1, "SortingOrder", var_8_0, 0)

def var_0_0.AddScreenChangeTimer(arg_9_0):
	arg_9_0.RemoveScreenChangeTimer()

	if not arg_9_0.IslimitYPos():
		return

	arg_9_0.screenTimer = Timer.New(function()
		if arg_9_0.currentWidth != Screen.width or arg_9_0.currentHeight != Screen.height:
			arg_9_0.currentWidth = Screen.width
			arg_9_0.currentHeight = Screen.height

			arg_9_0.ResetContainerPosition()
			arg_9_0.UpdateContainerPosition(), 0.5, -1)

	arg_9_0.screenTimer.Start()

def var_0_0.RemoveScreenChangeTimer(arg_11_0):
	if arg_11_0.screenTimer:
		arg_11_0.screenTimer.Stop()

		arg_11_0.screenTimer = None

def var_0_0.UpdateContainerPosition(arg_12_0):
	local var_12_0 = arg_12_0.IslimitYPos() and arg_12_0.GetHalfBodyOffsetY() or 0
	local var_12_1 = arg_12_0.live2dContainer.localPosition

	arg_12_0.live2dContainer.localPosition = Vector3(var_12_1.x, var_12_0, var_12_1.z)

def var_0_0.ResetContainerPosition(arg_13_0):
	local var_13_0 = arg_13_0.live2dContainer.localPosition

	arg_13_0.live2dContainer.localPosition = Vector3(var_13_0.x, 0, 0)

def var_0_0.OnUnload(arg_14_0):
	if arg_14_0.live2dChar:
		arg_14_0.RemoveScreenChangeTimer()
		arg_14_0.ResetContainerPosition()

		if arg_14_0.isModifyOrder:
			arg_14_0.isModifyOrder = False

			arg_14_0.ResetOrderInLayer()

		arg_14_0.cg.blocksRaycasts = False

		arg_14_0.live2dChar.Dispose()

		arg_14_0.live2dChar = None

def var_0_0.OnClick(arg_15_0):
	local var_15_0

	if arg_15_0.live2dChar and arg_15_0.live2dChar.state == Live2D.STATE_INITED and not arg_15_0.live2dChar.ignoreReact:
		if not Input.mousePosition:
			return

		local var_15_1 = arg_15_0.live2dChar.GetTouchPart()

		if var_15_1 > 0:
			local var_15_2 = arg_15_0.GetTouchEvent(var_15_1)

			var_15_0 = var_15_2[math.ceil(math.random(#var_15_2))]
		else
			local var_15_3 = arg_15_0.GetIdleEvents()

			var_15_0 = var_15_3[math.floor(math.Random(0, #var_15_3)) + 1]

	if var_15_0:
		arg_15_0.TriggerEvent(var_15_0)

def var_0_0._TriggerEvent(arg_16_0, arg_16_1):
	if not arg_16_1:
		return

	if arg_16_0.actionWaiting:
		return

	local var_16_0 = arg_16_0.GetEventConfig(arg_16_1)

	local function var_16_1(arg_17_0)
		if arg_17_0:
			if var_16_0.dialog != "":
				arg_16_0.DisplayWord(var_16_0.dialog)
			else
				arg_16_0.TriggerNextEventAuto()

		arg_16_0.actionWaiting = False

	local var_16_2, var_16_3, var_16_4, var_16_5, var_16_6, var_16_7 = ShipWordHelper.GetCvDataForShip(arg_16_0.ship, var_16_0.dialog)
	local var_16_8 = var_16_0.action
	local var_16_9 = var_16_0.dialog
	local var_16_10 = string.gsub(var_16_9, "main_", "main")

	if arg_16_0.ship.propose and pg.character_voice[var_16_10] and arg_16_0.shipGroup and arg_16_0.shipGroup.VoiceReplayCodition(pg.character_voice[var_16_10]) and arg_16_0.live2dChar.checkActionExist(var_16_8 .. "_ex"):
		var_16_8 = var_16_8 .. "_ex"

	if not var_16_7:
		arg_16_0.actionWaiting = True

		arg_16_0.live2dChar.TriggerAction(var_16_8)
		var_16_1(True)
	else
		arg_16_0.actionWaiting = True

		if not var_16_4 or var_16_4 == None or var_16_4 == "" or var_16_4 == "None":
			arg_16_0.actionWaiting = False

			var_16_1(True)

		arg_16_0.live2dChar.TriggerAction(var_16_8, None, None, var_16_1)

def var_0_0.PlayCV(arg_18_0, arg_18_1, arg_18_2, arg_18_3, arg_18_4):
	arg_18_0.RemoveSeTimer()

	if arg_18_1:
		arg_18_0.seTimer = Timer.New(function()
			pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/" .. arg_18_1[1]), arg_18_1[2], 1)

		arg_18_0.seTimer.Start()

	local var_18_0 = ShipWordHelper.RawGetCVKey(arg_18_0.ship.skinId)
	local var_18_1 = pg.CriMgr.GetCVBankName(var_18_0)

	arg_18_0.cvLoader.Load(var_18_1, arg_18_3, arg_18_2, arg_18_4)

def var_0_0.RemoveSeTimer(arg_20_0):
	if arg_20_0.seTimer:
		arg_20_0.seTimer.Stop()

		arg_20_0.seTimer = None

def var_0_0.OnDisplayWorld(arg_21_0):
	return

def var_0_0.OnPuase(arg_22_0):
	arg_22_0.RemoveScreenChangeTimer()
	arg_22_0.ResetContainerPosition()

	arg_22_0.actionWaiting = False

	arg_22_0.live2dChar.SetVisible(False)

def var_0_0.OnUpdateShip(arg_23_0, arg_23_1):
	if arg_23_1:
		arg_23_0.live2dChar.updateShip(arg_23_1)

def var_0_0.SetContainerVisible(arg_24_0, arg_24_1):
	setActive(arg_24_0.live2dContainer, arg_24_1)

def var_0_0.OnResume(arg_25_0):
	arg_25_0.SetContainerVisible(True)
	arg_25_0.AddScreenChangeTimer()
	arg_25_0.UpdateContainerPosition()
	arg_25_0.live2dChar.SetVisible(True)
	arg_25_0.live2dChar.UpdateAtomSource()

def var_0_0.Dispose(arg_26_0):
	var_0_0.super.Dispose(arg_26_0)
	arg_26_0.RemoveSeTimer()
	arg_26_0.RemoveScreenChangeTimer()

	if arg_26_0.eventTrigger:
		ClearEventTrigger(arg_26_0.eventTrigger)

def var_0_0.GetOffset(arg_27_0):
	return arg_27_0.live2dContainer.localPosition.x

def var_0_0.GetCenterPos(arg_28_0):
	return arg_28_0.live2dContainer.position

def var_0_0.IslimitYPos(arg_29_0):
	local var_29_0 = arg_29_0.ship.getPainting()

	return var_29_0 == "biaoqiang" or var_29_0 == "z23" or var_29_0 == "lafei" or var_29_0 == "lingbo" or var_29_0 == "mingshi" or var_29_0 == "xuefeng"

return var_0_0
