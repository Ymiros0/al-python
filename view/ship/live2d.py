local var_0_0 = class("Live2D")

var_0_0.STATE_LOADING = 0
var_0_0.STATE_INITED = 1
var_0_0.STATE_DISPOSE = 2

local var_0_1
local var_0_2 = 5
local var_0_3 = 3
local var_0_4 = 0.3

var_0_0.DRAG_TIME_ACTION = 1
var_0_0.DRAG_CLICK_ACTION = 2
var_0_0.DRAG_DOWN_ACTION = 3
var_0_0.DRAG_RELATION_XY = 4
var_0_0.DRAG_RELATION_IDLE = 5
var_0_0.DRAG_CLICK_MANY = 6
var_0_0.EVENT_ACTION_APPLY = "event action apply"
var_0_0.EVENT_ACTION_ABLE = "event action able"
var_0_0.EVENT_ADD_PARAMETER_COM = "event add parameter com "
var_0_0.EVENT_REMOVE_PARAMETER_COM = "event remove parameter com "
var_0_0.relation_type_drag_x = 101
var_0_0.relation_type_drag_y = 102
var_0_0.relation_type_action_index = 103

local var_0_5 = {
	CubismParameterBlendMode.Override,
	CubismParameterBlendMode.Additive,
	CubismParameterBlendMode.Multiply
}

def var_0_0.GenerateData(arg_1_0):
	local var_1_0 = {
		def SetData:(arg_2_0, arg_2_1)
			arg_2_0.ship = arg_2_1.ship
			arg_2_0.parent = arg_2_1.parent
			arg_2_0.scale = arg_2_1.scale

			local var_2_0 = arg_2_0.GetShipSkinConfig().live2d_offset

			arg_2_0.gyro = arg_2_0.GetShipSkinConfig().gyro or 0
			arg_2_0.shipL2dId = arg_2_0.GetShipSkinConfig().ship_l2d_id
			arg_2_0.skinId = arg_2_0.GetShipSkinConfig().id
			arg_2_0.spineUseLive2d = False

			if arg_2_0.skinId:
				arg_2_0.spineUseLive2d = pg.ship_skin_template[arg_2_0.skinId].spine_use_live2d == 1

			arg_2_0.position = arg_2_1.position + BuildVector3(var_2_0)
			arg_2_0.l2dDragRate = arg_2_0.GetShipSkinConfig().l2d_drag_rate
			arg_2_0.loadPrefs = arg_2_1.loadPrefs,
		def GetShipName:(arg_3_0)
			return arg_3_0.ship.getPainting(),
		def GetShipSkinConfig:(arg_4_0)
			return arg_4_0.ship.GetSkinConfig(),
		def isEmpty:(arg_5_0)
			return arg_5_0.ship == None,
		def Clear:(arg_6_0)
			arg_6_0.ship = None
			arg_6_0.parent = None
			arg_6_0.scale = None
			arg_6_0.position = None
	}

	var_1_0.SetData(arg_1_0)

	return var_1_0

local function var_0_6(arg_7_0)
	local var_7_0 = arg_7_0.live2dData.GetShipSkinConfig()
	local var_7_1 = var_7_0.lip_sync_gain
	local var_7_2 = var_7_0.lip_smoothing

	if var_7_1 and var_7_1 != 0:
		arg_7_0._go.GetComponent("CubismCriSrcMouthInput").Gain = var_7_1

	if var_7_2 and var_7_2 != 0:
		arg_7_0._go.GetComponent("CubismCriSrcMouthInput").Smoothing = var_7_2

local function var_0_7(arg_8_0)
	local var_8_0 = arg_8_0.live2dData.GetShipSkinConfig().l2d_para_range

	if var_8_0 != None and type(var_8_0) == "table":
		for iter_8_0, iter_8_1 in pairs(var_8_0):
			arg_8_0.liveCom.SetParaRange(iter_8_0, iter_8_1)

local function var_0_8(arg_9_0, arg_9_1)
	if not arg_9_1 or arg_9_1 == "":
		return False

	if arg_9_0.enablePlayActions and #arg_9_0.enablePlayActions > 0 and not table.contains(arg_9_0.enablePlayActions, arg_9_1):
		return False

	if arg_9_0.ignorePlayActions and #arg_9_0.ignorePlayActions > 0 and table.contains(arg_9_0.ignorePlayActions, arg_9_1):
		return False

	if arg_9_0._readlyToStop:
		return False

	return True

local function var_0_9(arg_10_0, arg_10_1, arg_10_2)
	if not var_0_8(arg_10_0, arg_10_1):
		return False

	if arg_10_0.updateAtom:
		arg_10_0.AtomSouceFresh()

	if arg_10_0.animationClipNames:
		local var_10_0 = arg_10_0.checkActionExist(arg_10_1)

		if (not var_10_0 or var_10_0 == False) and string.find(arg_10_1, "main_"):
			arg_10_1 = "main_3"

	if not arg_10_0.isPlaying or arg_10_2:
		local var_10_1 = var_0_1.action2Id[arg_10_1]

		if var_10_1:
			arg_10_0.playActionName = arg_10_1

			arg_10_0.liveCom.SetAction(var_10_1)
			arg_10_0.live2dActionChange(True)

			return True
		else
			print(tostring(arg_10_1) .. " action is not exist")

	return False

def var_0_0.checkActionExist(arg_11_0, arg_11_1):
	return (table.indexof(arg_11_0.animationClipNames, arg_11_1))

local function var_0_10(arg_12_0, arg_12_1)
	arg_12_0.liveCom.SetCenterPart("Drawables/TouchHead", Vector3.zero)

	arg_12_0.liveCom.DampingTime = 0.3

local function var_0_11(arg_13_0, arg_13_1, arg_13_2)
	if arg_13_1 == Live2D.EVENT_ACTION_APPLY:
		local var_13_0 = arg_13_2.id
		local var_13_1 = arg_13_2.action
		local var_13_2 = arg_13_2.callback
		local var_13_3 = arg_13_2.activeData
		local var_13_4 = arg_13_2.focus
		local var_13_5 = arg_13_2.react

		if not var_0_8(arg_13_0, var_13_1):
			return

		if var_13_5 != None:
			arg_13_0.setReactPos(tobool(var_13_5))

		if var_13_1:
			var_0_9(arg_13_0, var_13_1, var_13_4 or False)

		arg_13_0.applyActiveData(arg_13_2, var_13_3)

		if var_13_2:
			var_13_2()
	elif arg_13_1 == Live2D.EVENT_ACTION_ABLE:
		if arg_13_0.ableFlag != arg_13_2.ableFlag:
			arg_13_0.ableFlag = arg_13_2.ableFlag

			if arg_13_2.ableFlag:
				arg_13_0.tempEnable = arg_13_0.enablePlayActions
				arg_13_0.enablePlayActions = {
					"none action apply"
				}
			else
				arg_13_0.enablePlayActions = arg_13_0.tempEnable
		else
			print("able flag 相同，不执行操作")

		if arg_13_2.callback:
			arg_13_2.callback()
	elif arg_13_1 == Live2D.EVENT_ADD_PARAMETER_COM:
		arg_13_0.liveCom.AddParameterValue(arg_13_2.com, arg_13_2.start, var_0_5[arg_13_2.mode])
	elif arg_13_1 == Live2D.EVENT_REMOVE_PARAMETER_COM:
		arg_13_0.liveCom.removeParameterValue(arg_13_2.com)

local function var_0_12(arg_14_0)
	if not arg_14_0._l2dCharEnable:
		return

	if arg_14_0._readlyToStop:
		return

	local var_14_0 = False
	local var_14_1 = ReflectionHelp.RefGetField(typeof(Live2dChar), "reactPos", arg_14_0.liveCom)

	for iter_14_0 = 1, #arg_14_0.drags:
		arg_14_0.drags[iter_14_0].changeReactValue(var_14_1)
		arg_14_0.drags[iter_14_0].stepParameter()

		local var_14_2 = arg_14_0.drags[iter_14_0].getParameToTargetFlag()
		local var_14_3 = arg_14_0.drags[iter_14_0].getActive()

		if (var_14_2 or var_14_3) and arg_14_0.drags[iter_14_0].getIgnoreReact():
			var_14_0 = True
		elif arg_14_0.drags[iter_14_0].getReactCondition():
			var_14_0 = True

		local var_14_4 = arg_14_0.drags[iter_14_0].getParameter()
		local var_14_5 = arg_14_0.drags[iter_14_0].getParameterUpdateFlag()

		if var_14_4 and var_14_5:
			local var_14_6 = arg_14_0.drags[iter_14_0].getParameterCom()

			if var_14_6:
				arg_14_0.liveCom.ChangeParameterData(var_14_6, var_14_4)

		local var_14_7 = arg_14_0.drags[iter_14_0].getRelationParameterList()

		for iter_14_1, iter_14_2 in ipairs(var_14_7):
			if iter_14_2.enable:
				arg_14_0.liveCom.ChangeParameterData(iter_14_2.com, iter_14_2.value)

	if var_14_0 == arg_14_0.ignoreReact or not var_14_0 and (arg_14_0.mouseInputDown or arg_14_0.isPlaying):
		-- block empty
	else
		arg_14_0.setReactPos(var_14_0)

local function var_0_13(arg_15_0)
	arg_15_0.drags = {}
	arg_15_0.dragParts = {}

	for iter_15_0 = 1, #var_0_1.assistantTouchParts:
		table.insert(arg_15_0.dragParts, var_0_1.assistantTouchParts[iter_15_0])

	arg_15_0._l2dCharEnable = True
	arg_15_0._shopPreView = arg_15_0.live2dData.shopPreView

	for iter_15_1, iter_15_2 in ipairs(arg_15_0.live2dData.shipL2dId):
		local var_15_0 = pg.ship_l2d[iter_15_2]

		if var_15_0 and arg_15_0.getDragEnable(var_15_0):
			local var_15_1 = Live2dDrag.New(var_15_0, arg_15_0.live2dData)
			local var_15_2 = arg_15_0.liveCom.GetCubismParameter(var_15_0.parameter)

			var_15_1.setParameterCom(var_15_2)
			var_15_1.setEventCallback(function(arg_16_0, arg_16_1)
				var_0_11(arg_15_0, arg_16_0, arg_16_1))
			arg_15_0.liveCom.AddParameterValue(var_15_1.parameterName, var_15_1.startValue, var_0_5[var_15_0.mode])

			if var_15_0.relation_parameter and var_15_0.relation_parameter.list:
				local var_15_3 = var_15_0.relation_parameter.list

				for iter_15_3, iter_15_4 in ipairs(var_15_3):
					local var_15_4 = arg_15_0.liveCom.GetCubismParameter(iter_15_4.name)

					if var_15_4:
						var_15_1.addRelationComData(var_15_4, iter_15_4)

						local var_15_5 = iter_15_4.mode or var_15_0.mode

						arg_15_0.liveCom.AddParameterValue(iter_15_4.name, iter_15_4.start or var_15_1.startValue or 0, var_0_5[var_15_5])

			table.insert(arg_15_0.drags, var_15_1)

			if not table.contains(arg_15_0.dragParts, var_15_1.drawAbleName):
				table.insert(arg_15_0.dragParts, var_15_1.drawAbleName)

	arg_15_0.liveCom.SetDragParts(arg_15_0.dragParts)

	arg_15_0.eventTrigger = GetOrAddComponent(arg_15_0.liveCom.transform.parent, typeof(EventTriggerListener))

	arg_15_0.eventTrigger.AddPointDownFunc(function()
		if arg_15_0.useEventTriggerFlag:
			arg_15_0.onPointDown())
	arg_15_0.eventTrigger.AddPointUpFunc(function()
		if arg_15_0.useEventTriggerFlag:
			arg_15_0.onPointUp())
	arg_15_0.liveCom.SetMouseInputActions(System.Action(function()
		if not arg_15_0.useEventTriggerFlag:
			arg_15_0.onPointDown()), System.Action(function()
		if not arg_15_0.useEventTriggerFlag:
			arg_15_0.onPointUp()))

	arg_15_0.paraRanges = ReflectionHelp.RefGetField(typeof(Live2dChar), "paraRanges", arg_15_0.liveCom)
	arg_15_0.destinations = {}

	local var_15_6 = ReflectionHelp.RefGetProperty(typeof(Live2dChar), "Destinations", arg_15_0.liveCom)

	for iter_15_5 = 0, var_15_6.Length - 1:
		local var_15_7 = var_15_6[iter_15_5]

		table.insert(arg_15_0.destinations, var_15_6[iter_15_5])

	arg_15_0.timer = Timer.New(function()
		var_0_12(arg_15_0), 0.03333333333333333, -1)

	arg_15_0.timer.Start()
	var_0_12(arg_15_0)

def var_0_0.onPointDown(arg_22_0):
	if not arg_22_0._l2dCharEnable:
		return

	arg_22_0.mouseInputDown = True

	if #arg_22_0.drags > 0 and arg_22_0.liveCom.GetDragPart() > 0:
		local var_22_0 = arg_22_0.liveCom.GetDragPart()
		local var_22_1 = arg_22_0.dragParts[var_22_0]

		if var_22_0 > 0 and var_22_1:
			for iter_22_0, iter_22_1 in ipairs(arg_22_0.drags):
				if iter_22_1.drawAbleName == var_22_1:
					iter_22_1.startDrag()

def var_0_0.onPointUp(arg_23_0):
	if not arg_23_0._l2dCharEnable:
		return

	arg_23_0.mouseInputDown = False

	if arg_23_0.drags and #arg_23_0.drags > 0:
		local var_23_0 = arg_23_0.liveCom.GetDragPart()

		if var_23_0 > 0:
			local var_23_1 = arg_23_0.dragParts[var_23_0]

		for iter_23_0 = 1, #arg_23_0.drags:
			arg_23_0.drags[iter_23_0].stopDrag()

def var_0_0.changeTriggerFlag(arg_24_0, arg_24_1):
	arg_24_0.useEventTriggerFlag = arg_24_1

local function var_0_14(arg_25_0, arg_25_1)
	arg_25_0._go = arg_25_1
	arg_25_0._tf = tf(arg_25_1)

	UIUtil.SetLayerRecursively(arg_25_0._go, LayerMask.NameToLayer("UI"))
	arg_25_0._tf.SetParent(arg_25_0.live2dData.parent, True)

	arg_25_0._tf.localScale = arg_25_0.live2dData.scale
	arg_25_0._tf.localPosition = arg_25_0.live2dData.position
	arg_25_0.liveCom = arg_25_1.GetComponent(typeof(Live2dChar))
	arg_25_0._animator = arg_25_1.GetComponent(typeof(Animator))
	arg_25_0.animationClipNames = {}

	if arg_25_0._animator and arg_25_0._animator.runtimeAnimatorController:
		local var_25_0 = arg_25_0._animator.runtimeAnimatorController.animationClips
		local var_25_1 = var_25_0.Length

		for iter_25_0 = 0, var_25_1 - 1:
			table.insert(arg_25_0.animationClipNames, var_25_0[iter_25_0].name)

	local var_25_2 = var_0_1.action2Id.idle

	arg_25_0.liveCom.SetReactMotions(var_0_1.idleActions)
	arg_25_0.liveCom.SetAction(var_25_2)

	function arg_25_0.liveCom.FinishAction(arg_26_0)
		arg_25_0.live2dActionChange(False)

		if arg_25_0.finishActionCB:
			arg_25_0.finishActionCB()

			arg_25_0.finishActionCB = None

		arg_25_0.liveCom.SetAction(var_0_1.idleActions[math.ceil(math.random(#var_0_1.idleActions))])

	function arg_25_0.liveCom.EventAction(arg_27_0)
		if arg_25_0.animEventCB:
			arg_25_0.animEventCB(arg_27_0)

			arg_25_0.animEventCB = None

	arg_25_0.liveCom.SetTouchParts(var_0_1.assistantTouchParts)

	if arg_25_0.live2dData and arg_25_0.live2dData.ship and arg_25_0.live2dData.ship.propose:
		arg_25_0.changeParamaterValue("Paramring", 1)
	else
		arg_25_0.changeParamaterValue("Paramring", 0)

	if not arg_25_0._physics:
		arg_25_0._physics = GetComponent(arg_25_0._tf, "CubismPhysicsController")

	if arg_25_0._physics:
		arg_25_0._physics.enabled = False
		arg_25_0._physics.enabled = True

	if arg_25_0.live2dData.l2dDragRate and #arg_25_0.live2dData.l2dDragRate > 0:
		arg_25_0.liveCom.DragRateX = arg_25_0.live2dData.l2dDragRate[1] * var_0_2
		arg_25_0.liveCom.DragRateY = arg_25_0.live2dData.l2dDragRate[2] * var_0_3
		arg_25_0.liveCom.DampingTime = arg_25_0.live2dData.l2dDragRate[3] * var_0_4

	var_0_6(arg_25_0)
	var_0_7(arg_25_0)
	var_0_10(arg_25_0)

	if arg_25_0.live2dData.shipL2dId and #arg_25_0.live2dData.shipL2dId > 0:
		var_0_13(arg_25_0)

	arg_25_0.addKeyBoard()

	arg_25_0.state = var_0_0.STATE_INITED

	if arg_25_0.delayChangeParamater and #arg_25_0.delayChangeParamater > 0:
		for iter_25_1 = 1, #arg_25_0.delayChangeParamater:
			local var_25_3 = arg_25_0.delayChangeParamater[iter_25_1]

			arg_25_0.changeParamaterValue(var_25_3[1], var_25_3[2])

		arg_25_0.delayChangeParamater = None

	arg_25_0.enablePlayActions = {}
	arg_25_0.ignorePlayActions = {}

	arg_25_0.changeIdleIndex(0)
	arg_25_0.loadLive2dData()

def var_0_0.Ctor(arg_28_0, arg_28_1, arg_28_2):
	arg_28_0.state = var_0_0.STATE_LOADING
	arg_28_0.live2dData = arg_28_1
	var_0_1 = pg.AssistantInfo

	assert(not arg_28_0.live2dData.isEmpty())

	local var_28_0 = arg_28_0.live2dData.GetShipName()

	local function var_28_1(arg_29_0)
		var_0_14(arg_28_0, arg_29_0)

		if arg_28_2:
			arg_28_2(arg_28_0)

	arg_28_0.live2dRequestId = pg.Live2DMgr.GetInstance().GetLive2DModelAsync(var_28_0, var_28_1)
	Input.gyro.enabled = arg_28_0.live2dData.gyro == 1 and PlayerPrefs.GetInt(GYRO_ENABLE, 1) == 1
	arg_28_0.useEventTriggerFlag = True

def var_0_0.setStopCallback(arg_30_0, arg_30_1):
	arg_30_0._stopCallback = arg_30_1

def var_0_0.SetVisible(arg_31_0, arg_31_1):
	if not arg_31_0.IsLoaded():
		return

	Input.gyro.enabled = PlayerPrefs.GetInt(GYRO_ENABLE, 1) == 1

	arg_31_0.setReactPos(True)
	arg_31_0.Reset()

	if arg_31_1:
		arg_31_0._readlyToStop = False

		onDelayTick(function()
			if not arg_31_0._readlyToStop:
				if arg_31_0._physics:
					arg_31_0._physics.enabled = False
					arg_31_0._physics.enabled = True

				arg_31_0.setReactPos(False), 1)
	else
		var_0_9(arg_31_0, "idle", True)

		arg_31_0._readlyToStop = True

		onDelayTick(function()
			if arg_31_0._readlyToStop:
				arg_31_0._animator.speed = 0

				if arg_31_0._stopCallback:
					arg_31_0._stopCallback(), 3)

	if arg_31_1:
		arg_31_0.loadLive2dData()
	else
		arg_31_0.saveLive2dData()

	arg_31_0._animator.speed = 1

def var_0_0.loadLive2dData(arg_34_0):
	if not arg_34_0.live2dData.loadPrefs:
		return

	if PlayerPrefs.GetInt(LIVE2D_STATUS_SAVE, 1) != 1 and not arg_34_0.live2dData.spineUseLive2d:
		if arg_34_0.drags:
			for iter_34_0 = 1, #arg_34_0.drags:
				arg_34_0.drags[iter_34_0].clearData()

		arg_34_0.changeIdleIndex(0)
		arg_34_0._animator.Play("idle")

		arg_34_0.saveActionAbleId = None

		var_0_12(arg_34_0)

		return

	local var_34_0, var_34_1 = Live2dConst.GetL2dSaveData(arg_34_0.live2dData.GetShipSkinConfig().id, arg_34_0.live2dData.ship.id)

	if var_34_0:
		arg_34_0.changeIdleIndex(var_34_0)

		if var_34_0 == 0:
			arg_34_0._animator.Play("idle")
		else
			arg_34_0._animator.Play("idle" .. var_34_0)

	arg_34_0.saveActionAbleId = var_34_1

	if var_34_1 and var_34_1 > 0:
		if pg.ship_l2d[var_34_1]:
			local var_34_2 = pg.ship_l2d[var_34_1].action_trigger_active

			arg_34_0.enablePlayActions = var_34_2.enable
			arg_34_0.ignorePlayActions = var_34_2.ignore
	else
		arg_34_0.enablePlayActions = {}
		arg_34_0.ignorePlayActions = {}

	if arg_34_0.drags:
		for iter_34_1 = 1, #arg_34_0.drags:
			arg_34_0.drags[iter_34_1].loadData()

	var_0_12(arg_34_0)

def var_0_0.saveLive2dData(arg_35_0):
	if not arg_35_0.live2dData.loadPrefs:
		return

	if PlayerPrefs.GetInt(LIVE2D_STATUS_SAVE, 1) != 1 and not arg_35_0.live2dData.spineUseLive2d:
		return

	if arg_35_0.idleIndex:
		Live2dConst.SaveL2dIdle(arg_35_0.live2dData.GetShipSkinConfig().id, arg_35_0.live2dData.ship.id, arg_35_0.idleIndex)

	if arg_35_0.saveActionAbleId:
		if arg_35_0.idleIndex == 0:
			Live2dConst.SaveL2dAction(arg_35_0.live2dData.GetShipSkinConfig().id, arg_35_0.live2dData.ship.id, 0)
		else
			Live2dConst.SaveL2dAction(arg_35_0.live2dData.GetShipSkinConfig().id, arg_35_0.live2dData.ship.id, arg_35_0.saveActionAbleId)

	if arg_35_0.drags:
		for iter_35_0 = 1, #arg_35_0.drags:
			arg_35_0.drags[iter_35_0].saveData()

def var_0_0.enablePlayAction(arg_36_0, arg_36_1):
	return var_0_8(arg_36_0, arg_36_1)

def var_0_0.IgonreReactPos(arg_37_0, arg_37_1):
	arg_37_0.setReactPos(arg_37_1)

def var_0_0.setReactPos(arg_38_0, arg_38_1):
	if arg_38_0.liveCom:
		arg_38_0.ignoreReact = arg_38_1

		arg_38_0.liveCom.IgonreReactPos(arg_38_1)

		if arg_38_1:
			ReflectionHelp.RefSetField(typeof(Live2dChar), "inDrag", arg_38_0.liveCom, False)

		ReflectionHelp.RefSetField(typeof(Live2dChar), "reactPos", arg_38_0.liveCom, Vector3(0, 0, 0))
		arg_38_0.updateDragsSateData()

def var_0_0.l2dCharEnable(arg_39_0, arg_39_1):
	arg_39_0._l2dCharEnable = arg_39_1

def var_0_0.inShopPreView(arg_40_0, arg_40_1):
	arg_40_0._shopPreView = arg_40_1

def var_0_0.getDragEnable(arg_41_0, arg_41_1):
	if arg_41_0._shopPreView and arg_41_1.shop_action == 0:
		return False

	return True

def var_0_0.updateShip(arg_42_0, arg_42_1):
	if arg_42_1 and arg_42_0.live2dData and arg_42_0.live2dData.ship:
		arg_42_0.live2dData.ship = arg_42_1

		if arg_42_0.live2dData and arg_42_0.live2dData.ship and arg_42_0.live2dData.ship.propose:
			arg_42_0.changeParamaterValue("Paramring", 1)
		else
			arg_42_0.changeParamaterValue("Paramring", 0)

def var_0_0.IsLoaded(arg_43_0):
	return arg_43_0.state == var_0_0.STATE_INITED

def var_0_0.GetTouchPart(arg_44_0):
	return arg_44_0.liveCom.GetTouchPart()

def var_0_0.TriggerAction(arg_45_0, arg_45_1, arg_45_2, arg_45_3, arg_45_4):
	arg_45_0.CheckStopDrag()

	arg_45_0.finishActionCB = arg_45_2
	arg_45_0.animEventCB = arg_45_4

	if not var_0_9(arg_45_0, arg_45_1, arg_45_3) and arg_45_0.animEventCB:
		arg_45_0.animEventCB(False)

		arg_45_0.animEventCB = None

def var_0_0.Reset(arg_46_0):
	arg_46_0.live2dActionChange(False)

	arg_46_0.enablePlayActions = {}
	arg_46_0.ignorePlayActions = {}
	arg_46_0.ableFlag = None

def var_0_0.resetL2dData(arg_47_0):
	if not arg_47_0._tf:
		return

	if arg_47_0._tf and LeanTween.isTweening(go(arg_47_0._tf)):
		return

	arg_47_0._l2dPosition = arg_47_0._tf.position
	arg_47_0._tf.position = Vector3(arg_47_0._l2dPosition.x + 100, 0, 0)

	LeanTween.delayedCall(go(arg_47_0._tf), 0.2, System.Action(function()
		if arg_47_0._tf:
			arg_47_0._tf.position = arg_47_0._l2dPosition))
	Live2dConst.ClearLive2dSave(arg_47_0.live2dData.ship.skinId, arg_47_0.live2dData.ship.id)
	arg_47_0.Reset()
	arg_47_0.changeIdleIndex(0)
	arg_47_0.loadLive2dData()

def var_0_0.applyActiveData(arg_49_0, arg_49_1, arg_49_2):
	local var_49_0 = arg_49_2.enable
	local var_49_1 = arg_49_2.ignore
	local var_49_2 = arg_49_2.idle
	local var_49_3 = arg_49_2.repeatFlag

	if var_49_0 and #var_49_0 >= 0:
		arg_49_0.enablePlayActions = var_49_0

	if var_49_1 and #var_49_1 >= 0:
		arg_49_0.ignorePlayActions = var_49_1

	if var_49_2 != arg_49_0.indexIndex:
		arg_49_0.saveActionAbleId = arg_49_1.id

	if var_49_2:
		local var_49_4

		if type(var_49_2) == "number" and var_49_2 >= 0:
			var_49_4 = var_49_2
		elif type(var_49_2) == "table":
			local var_49_5 = {}

			for iter_49_0, iter_49_1 in ipairs(var_49_2):
				if iter_49_1 == arg_49_0.idleIndex:
					if var_49_3:
						table.insert(var_49_5, iter_49_1)
				else
					table.insert(var_49_5, iter_49_1)

			var_49_4 = var_49_5[math.random(1, #var_49_5)]

		if var_49_4:
			arg_49_0.changeIdleIndex(var_49_4)

		arg_49_0.saveLive2dData()

def var_0_0.changeIdleIndex(arg_50_0, arg_50_1):
	if arg_50_0.idleIndex != arg_50_1:
		arg_50_0._animator.SetInteger("idle", arg_50_1)

	arg_50_0.idleIndex = arg_50_1

	arg_50_0.updateDragsSateData()

def var_0_0.live2dActionChange(arg_51_0, arg_51_1):
	arg_51_0.isPlaying = arg_51_1

	arg_51_0.updateDragsSateData()

def var_0_0.updateDragsSateData(arg_52_0):
	local var_52_0 = {
		idleIndex = arg_52_0.idleIndex,
		isPlaying = arg_52_0.isPlaying,
		ignoreReact = arg_52_0.ignoreReact,
		actionName = arg_52_0.playActionName
	}

	if arg_52_0.drags:
		for iter_52_0 = 1, #arg_52_0.drags:
			arg_52_0.drags[iter_52_0].updateStateData(var_52_0)

def var_0_0.CheckStopDrag(arg_53_0):
	local var_53_0 = arg_53_0.live2dData.GetShipSkinConfig()

	if var_53_0.l2d_ignore_drag and var_53_0.l2d_ignore_drag == 1:
		arg_53_0.liveCom.ResponseClick = False

		ReflectionHelp.RefSetField(typeof(Live2dChar), "inDrag", arg_53_0.liveCom, False)

def var_0_0.changeParamaterValue(arg_54_0, arg_54_1, arg_54_2):
	if arg_54_0.IsLoaded():
		if not arg_54_1 or string.len(arg_54_1) == 0:
			return

		local var_54_0 = arg_54_0.liveCom.GetCubismParameter(arg_54_1)

		if not var_54_0:
			return

		arg_54_0.liveCom.AddParameterValue(var_54_0, arg_54_2, var_0_5[1])
	else
		if not arg_54_0.delayChangeParamater:
			arg_54_0.delayChangeParamater = {}

		table.insert(arg_54_0.delayChangeParamater, {
			arg_54_1,
			arg_54_2
		})

def var_0_0.Dispose(arg_55_0):
	if arg_55_0.state == var_0_0.STATE_INITED:
		if arg_55_0._go:
			Destroy(arg_55_0._go)

		arg_55_0.liveCom.FinishAction = None
		arg_55_0.liveCom.EventAction = None

	arg_55_0.saveLive2dData()
	arg_55_0.liveCom.SetMouseInputActions(None, None)

	arg_55_0._readlyToStop = False
	arg_55_0.state = var_0_0.STATE_DISPOSE

	pg.Live2DMgr.GetInstance().StopLoadingLive2d(arg_55_0.live2dRequestId)

	arg_55_0.live2dRequestId = None

	if arg_55_0.drags:
		for iter_55_0 = 1, #arg_55_0.drags:
			arg_55_0.drags[iter_55_0].dispose()

		arg_55_0.drags = {}

	if arg_55_0.live2dData.gyro == 1:
		Input.gyro.enabled = False

	if arg_55_0.live2dData:
		arg_55_0.live2dData.Clear()

		arg_55_0.live2dData = None

	arg_55_0.live2dActionChange(False)

	if arg_55_0.timer:
		arg_55_0.timer.Stop()

		arg_55_0.timer = None

def var_0_0.UpdateAtomSource(arg_56_0):
	arg_56_0.updateAtom = True

def var_0_0.AtomSouceFresh(arg_57_0):
	local var_57_0 = pg.CriMgr.GetInstance().getAtomSource(pg.CriMgr.C_VOICE)
	local var_57_1 = arg_57_0._go.GetComponent("CubismCriSrcMouthInput")
	local var_57_2 = ReflectionHelp.RefGetField(typeof("Live2D.Cubism.Framework.MouthMovement.CubismCriSrcMouthInput"), "Analyzer", var_57_1)

	var_57_0.AttachToAnalyzer(var_57_2)

	if arg_57_0.updateAtom:
		arg_57_0.updateAtom = False

def var_0_0.addKeyBoard(arg_58_0):
	return

return var_0_0
