local var_0_0 = class("NavalAcademyStudent")

var_0_0.ShipState = {
	Walk = "Walk",
	Idle = "Idle",
	Touch = "Touch"
}
var_0_0.normalSpeed = 15

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform

	arg_1_0.init()

def var_0_0.init(arg_2_0):
	arg_2_0.chat = arg_2_0._tf.Find("chat")
	arg_2_0.chatFace = arg_2_0.chat.Find("face")
	arg_2_0.chatTask = arg_2_0.chat.Find("task")
	arg_2_0.chatFight = arg_2_0.chat.Find("fight")
	arg_2_0.clickArea = arg_2_0._tf.Find("click")

	setActive(arg_2_0.chat, True)
	setActive(arg_2_0.clickArea, True)

def var_0_0.attach(arg_3_0):
	arg_3_0.exited = False

	setActive(arg_3_0._go, True)
	pg.DelegateInfo.New(arg_3_0)

def var_0_0.setPathFinder(arg_4_0, arg_4_1):
	arg_4_0.pathFinder = arg_4_1

def var_0_0.setCallBack(arg_5_0, arg_5_1, arg_5_2):
	arg_5_0.onStateChange = arg_5_1
	arg_5_0.onTask = arg_5_2

def var_0_0.updateStudent(arg_6_0, arg_6_1, arg_6_2):
	if arg_6_1.hide:
		setActive(arg_6_0._go, False)

		return

	setActive(arg_6_0._go, True)

	if arg_6_0.shipVO == None or arg_6_0.shipVO.configId != arg_6_1.configId:
		if not IsNil(arg_6_0.model):
			PoolMgr.GetInstance().ReturnSpineChar(arg_6_0.prefab, arg_6_0.model)

		arg_6_0.prefab = arg_6_1.getPrefab()
		arg_6_0.currentPoint = arg_6_0.pathFinder.getRandomPoint()

		local var_6_0 = arg_6_0.currentPoint.nexts
		local var_6_1 = var_6_0[math.random(1, #var_6_0)]

		arg_6_0.targetPoint = arg_6_0.pathFinder.getPoint(var_6_1)
		arg_6_0._tf.anchoredPosition = Vector2.New(arg_6_0.currentPoint.x, arg_6_0.currentPoint.y)

		local var_6_2 = arg_6_0.prefab

		PoolMgr.GetInstance().GetSpineChar(var_6_2, True, function(arg_7_0)
			if var_6_2 != arg_6_0.prefab:
				PoolMgr.GetInstance().ReturnSpineChar(var_6_2, arg_7_0)

				return

			arg_6_0.model = arg_7_0
			arg_6_0.model.transform.localScale = Vector3(0.5, 0.5, 1)
			arg_6_0.model.transform.localPosition = Vector3.zero

			arg_6_0.model.transform.SetParent(arg_6_0._tf, False)
			arg_6_0.model.transform.SetSiblingIndex(1)

			arg_6_0.anim = arg_6_0.model.GetComponent(typeof(SpineAnimUI))

			arg_6_0.updateState(var_0_0.ShipState.Idle)
			onButton(arg_6_0, arg_6_0.chat, function()
				arg_6_0.onClickShip()))

	onButton(arg_6_0, arg_6_0.clickArea, function()
		if not IsNil(arg_6_0.model):
			arg_6_0.updateState(var_0_0.ShipState.Touch))

	arg_6_0.shipVO = arg_6_1
	arg_6_0.args = arg_6_2

	setActive(arg_6_0.chatFace, False)
	setActive(arg_6_0.chatTask, False)
	setActive(arg_6_0.chatFight, False)

	if arg_6_0.shipVO.withShipFace:
		if arg_6_2.showTips:
			setActive(arg_6_0.chatTask, True)
		elif arg_6_2.currentTask and not arg_6_2.currentTask.isFinish() and arg_6_2.currentTask.getConfig("sub_type") == 29:
			setActive(arg_6_0.chatFight, True)
		else
			setActive(arg_6_0.chatFace, True)

def var_0_0.updateState(arg_10_0, arg_10_1):
	if arg_10_0.state != arg_10_1:
		arg_10_0.state = arg_10_1

		arg_10_0.updateAction()
		arg_10_0.updateLogic()

		if arg_10_0.onStateChange:
			arg_10_0.onStateChange(arg_10_0.state)

def var_0_0.updateAction(arg_11_0):
	if not IsNil(arg_11_0.anim):
		if arg_11_0.state == var_0_0.ShipState.Walk:
			arg_11_0.anim.SetAction("walk", 0)
		elif arg_11_0.state == var_0_0.ShipState.Idle:
			arg_11_0.anim.SetAction("stand2", 0)
		elif arg_11_0.state == var_0_0.ShipState.Touch:
			arg_11_0.anim.SetAction("touch", 0)
			arg_11_0.anim.SetActionCallBack(function(arg_12_0)
				arg_11_0.updateState(var_0_0.ShipState.Idle))

def var_0_0.updateLogic(arg_13_0):
	arg_13_0.clearLogic()

	if arg_13_0.state == var_0_0.ShipState.Walk:
		local var_13_0 = Vector3(arg_13_0._tf.anchoredPosition.x, arg_13_0._tf.anchoredPosition.y, 0)
		local var_13_1 = Vector3(arg_13_0.targetPoint.x, arg_13_0.targetPoint.y, 0)
		local var_13_2 = arg_13_0.normalSpeed
		local var_13_3 = Vector3.Distance(var_13_0, var_13_1) / var_13_2

		LeanTween.value(arg_13_0._go, 0, 1, var_13_3).setOnUpdate(System.Action_float(function(arg_14_0)
			arg_13_0._tf.anchoredPosition3D = Vector3.Lerp(var_13_0, var_13_1, arg_14_0)

			local var_14_0 = arg_13_0._tf.localScale
			local var_14_1 = arg_13_0.targetPoint.x > arg_13_0.currentPoint.x and 1 or -1

			var_14_0.x = var_14_1
			arg_13_0._tf.localScale = var_14_0

			local var_14_2 = arg_13_0.chat.localScale

			var_14_2.x = var_14_1
			arg_13_0.chat.localScale = var_14_2

			local var_14_3 = arg_13_0.chat.anchoredPosition

			var_14_3.x = var_14_1 * math.abs(var_14_3.x)
			arg_13_0.chat.anchoredPosition = var_14_3)).setOnComplete(System.Action(function()
			arg_13_0.currentPoint = arg_13_0.targetPoint

			local var_15_0 = arg_13_0.currentPoint.nexts
			local var_15_1 = var_15_0[math.random(1, #var_15_0)]

			arg_13_0.targetPoint = arg_13_0.pathFinder.getPoint(var_15_1)

			arg_13_0.updateState(var_0_0.ShipState.Idle)))
	elif arg_13_0.state == var_0_0.ShipState.Idle:
		arg_13_0.idleTimer = Timer.New(function()
			arg_13_0.updateState(var_0_0.ShipState.Walk), math.random(10, 20), 1)

		arg_13_0.idleTimer.Start()
	elif arg_13_0.state == var_0_0.ShipState.Touch:
		arg_13_0.onClickShip()

def var_0_0.onClickShip(arg_17_0):
	if arg_17_0.onTask:
		arg_17_0.onTask(arg_17_0.acceptTaskId, arg_17_0.currentTask)

def var_0_0.clearLogic(arg_18_0):
	LeanTween.cancel(arg_18_0._go)

	if arg_18_0.idleTimer:
		arg_18_0.idleTimer.Stop()

		arg_18_0.idleTimer = None

def var_0_0.clear(arg_19_0):
	arg_19_0.clearLogic()

	if not IsNil(arg_19_0.model):
		arg_19_0.anim.SetActionCallBack(None)

		arg_19_0.model.transform.localScale = Vector3.one

		PoolMgr.GetInstance().ReturnSpineChar(arg_19_0.prefab, arg_19_0.model)

	arg_19_0.shipVO = None
	arg_19_0.prefab = None
	arg_19_0.model = None
	arg_19_0.anim = None
	arg_19_0.position = None
	arg_19_0.currentPoint = None
	arg_19_0.targetPoint = None
	arg_19_0.state = None

def var_0_0.detach(arg_20_0):
	if not arg_20_0.exited:
		setActive(arg_20_0._go, False)
		pg.DelegateInfo.Dispose(arg_20_0)
		arg_20_0.clear()

		arg_20_0.exited = True

return var_0_0
