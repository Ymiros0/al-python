local var_0_0 = class("MainSpinePainting", import(".MainBasePainting"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.bgTr = arg_1_3
	arg_1_0.spTF = findTF(arg_1_1, "spinePainting")
	arg_1_0.spBg = findTF(arg_1_3, "spinePainting")
	arg_1_0.uiCam = GameObject.Find("UICamera").GetComponent("Camera")

def var_0_0.GetCenterPos(arg_2_0):
	return arg_2_0.spTF.position

def var_0_0.OnLoad(arg_3_0, arg_3_1):
	local var_3_0 = SpinePainting.GenerateData({
		ship = arg_3_0.ship,
		position = Vector3(0, 0, 0),
		parent = arg_3_0.spTF,
		effectParent = arg_3_0.spBg
	})

	arg_3_0.spinePainting = SpinePainting.New(var_3_0, function(arg_4_0)
		arg_3_0.AdJustOrderInLayer(arg_4_0)
		arg_3_0.InitSpecialTouch()
		arg_3_1())

def var_0_0.AdJustOrderInLayer(arg_5_0, arg_5_1):
	local var_5_0 = 0
	local var_5_1 = arg_5_0.container.GetComponent(typeof(Canvas))

	if var_5_1 and var_5_1.overrideSorting and var_5_1.sortingOrder != 0:
		local var_5_2 = arg_5_0.spTF.GetComponentsInChildren(typeof(Canvas))

		for iter_5_0 = 1, var_5_2.Length:
			local var_5_3 = var_5_2[iter_5_0 - 1]

			var_5_3.overrideSorting = True
			var_5_0 = var_5_3.sortingOrder - var_5_1.sortingOrder
			var_5_3.sortingOrder = var_5_1.sortingOrder

	local var_5_4 = arg_5_0.bgTr.GetComponent(typeof(Canvas))

	if var_5_4 and var_5_4.overrideSorting and var_5_4.sortingOrder != 0:
		local var_5_5 = arg_5_0.spBg.GetComponentsInChildren(typeof(Canvas))

		for iter_5_1 = 1, var_5_5.Length:
			local var_5_6 = var_5_5[iter_5_1 - 1]

			var_5_6.overrideSorting = True
			var_5_6.sortingOrder = var_5_6.sortingOrder - var_5_0

		local var_5_7 = arg_5_0.spBg.GetComponentsInChildren(typeof("UnityEngine.ParticleSystemRenderer"))

		for iter_5_2 = 1, var_5_7.Length:
			local var_5_8 = var_5_7[iter_5_2 - 1]
			local var_5_9 = ReflectionHelp.RefGetProperty(typeof("UnityEngine.ParticleSystemRenderer"), "sortingOrder", var_5_8) - var_5_0

			ReflectionHelp.RefSetProperty(typeof("UnityEngine.ParticleSystemRenderer"), "sortingOrder", var_5_8, var_5_9)

def var_0_0.InitSpecialTouch(arg_6_0):
	arg_6_0.specialClickDic = {}

	local var_6_0 = findTF(arg_6_0.spTF.GetChild(0), "hitArea")

	if not var_6_0:
		return

	eachChild(var_6_0, function(arg_7_0)
		if arg_7_0.name == "drag":
			arg_6_0.dragEvent = GetOrAddComponent(arg_7_0, typeof(EventTriggerListener))

			arg_6_0.dragEvent.AddPointDownFunc(function(arg_8_0, arg_8_1)
				arg_6_0.dragActive = True
				arg_6_0.dragStart = arg_8_1.position)
			arg_6_0.dragEvent.AddPointUpFunc(function(arg_9_0, arg_9_1)
				if arg_6_0.dragActive:
					arg_6_0.dragActive = False
					arg_6_0.dragOffset = Vector2(arg_6_0.dragStart.x - arg_9_1.position.x, arg_6_0.dragStart.y - arg_9_1.position.y)

					if math.abs(arg_6_0.dragOffset.x) < 200 or math.abs(arg_6_0.dragOffset.y) < 200:
						arg_6_0.dragUp = arg_9_1.position

						local var_9_0 = arg_6_0.uiCam.ScreenToWorldPoint(arg_9_1.position)

						for iter_9_0 = 1, #arg_6_0.specialClickDic:
							local var_9_1 = arg_6_0.specialClickDic[iter_9_0]
							local var_9_2 = var_9_1.tf.InverseTransformPoint(var_9_0)

							if math.abs(var_9_2.x) < var_9_1.bound.x / 2 and math.abs(var_9_2.y) < var_9_1.bound.y / 2:
								arg_6_0.TriggerEvent(var_9_1.name)
								arg_6_0.TriggerPersonalTask(var_9_1.task)

								return)
			arg_6_0.dragEvent.AddDragFunc(function(arg_10_0, arg_10_1)
				if arg_6_0.dragActive:
					if arg_6_0.isDragAndZoomState:
						arg_6_0.dragActive = False

						return

					if arg_6_0.chatting:
						arg_6_0.dragActive = False

						return

					arg_6_0.dragOffset = Vector2(arg_6_0.dragStart.x - arg_10_1.position.x, arg_6_0.dragStart.y - arg_10_1.position.y)

					if math.abs(arg_6_0.dragOffset.x) > 200 or math.abs(arg_6_0.dragOffset.y) > 200:
						arg_6_0.dragActive = False

						arg_6_0.spinePainting.DoDragTouch())
		else
			local var_7_0 = arg_6_0.GetSpecialTouchEvent(arg_7_0.name)

			if var_7_0:
				table.insert(arg_6_0.specialClickDic, {
					name = var_7_0,
					task = arg_6_0.ship.groupId,
					bound = arg_7_0.sizeDelta,
					tf = arg_7_0
				})

			onButton(arg_6_0, arg_7_0, function()
				local var_11_0 = arg_6_0.GetSpecialTouchEvent(arg_7_0.name)

				if arg_7_0.name == "special":
					if arg_6_0.isDragAndZoomState:
						return

					if arg_6_0.chatting:
						return

					arg_6_0.spinePainting.DoSpecialTouch()
				else
					arg_6_0.TriggerEvent(var_11_0)
					arg_6_0.TriggerPersonalTask(arg_6_0.ship.groupId)))

def var_0_0.OnClick(arg_12_0):
	local var_12_0 = arg_12_0.CollectTouchEvents()

	arg_12_0.TriggerEvent(var_12_0[math.ceil(math.random(#var_12_0))])

def var_0_0.OnDisplayWorld(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_0.ship.getCVIntimacy()
	local var_13_1 = ShipExpressionHelper.GetExpression(arg_13_0.paintingName, arg_13_1, var_13_0, arg_13_0.ship.skinId)

	if var_13_1 != "":
		arg_13_0.spinePainting.SetAction(var_13_1, 1)

def var_0_0.OnDisplayWordEnd(arg_14_0):
	var_0_0.super.OnDisplayWordEnd(arg_14_0)
	arg_14_0.spinePainting.SetEmptyAction(1)

def var_0_0.OnLongPress(arg_15_0):
	if arg_15_0.isFoldState:
		return

	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
		shipId = arg_15_0.ship.id
	})

def var_0_0.OnUnload(arg_16_0):
	if arg_16_0.spinePainting:
		arg_16_0.spinePainting.Dispose()

		arg_16_0.spinePainting = None

	if arg_16_0.dragEvent:
		ClearEventTrigger(arg_16_0.dragEvent)

def var_0_0.GetOffset(arg_17_0):
	return arg_17_0.spTF.localPosition.x

def var_0_0.OnPuase(arg_18_0):
	if arg_18_0.spinePainting:
		arg_18_0.spinePainting.SetVisible(False)

def var_0_0.OnResume(arg_19_0):
	if arg_19_0.spinePainting:
		arg_19_0.spinePainting.SetVisible(True)
		arg_19_0.spinePainting.SetEmptyAction(1)

return var_0_0
