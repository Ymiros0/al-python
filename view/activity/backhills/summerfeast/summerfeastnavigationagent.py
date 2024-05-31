local var_0_0 = class("SummerFeastNavigationAgent", require("view.main.NavalAcademyStudent"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.onTransEdge = None

	var_0_0.super.Ctor(arg_1_0, arg_1_1)

def var_0_0.init(arg_2_0):
	return

var_0_0.normalSpeed = 150
var_0_0.normalScale = 0.5

def var_0_0.SetOnTransEdge(arg_3_0, arg_3_1):
	arg_3_0.onTransEdge = arg_3_1

def var_0_0.setCurrentIndex(arg_4_0, arg_4_1):
	if not arg_4_1:
		return

	arg_4_0.currentPoint = arg_4_0.pathFinder.getPoint(arg_4_1)

def var_0_0.SetPositionTable(arg_5_0, arg_5_1):
	arg_5_0.posTable = arg_5_1

def var_0_0.updateStudent(arg_6_0, arg_6_1):
	if arg_6_1 == None or arg_6_1 == "":
		setActive(arg_6_0._go, False)

		return

	setActive(arg_6_0._go, True)

	if arg_6_0.prefabName != arg_6_1:
		if not IsNil(arg_6_0.model):
			PoolMgr.GetInstance().ReturnSpineChar(arg_6_0.prefab, arg_6_0.model)

		arg_6_0.prefab = arg_6_1
		arg_6_0.currentPoint = arg_6_0.currentPoint or arg_6_0.pathFinder.getRandomPoint()
		arg_6_0.targetPoint = arg_6_0.currentPoint

		local var_6_0 = arg_6_0.currentPoint.id

		arg_6_0._tf.anchoredPosition = arg_6_0.currentPoint

		if arg_6_0.onTransEdge:
			arg_6_0.onTransEdge(arg_6_0, var_6_0, var_6_0)

		local var_6_1 = arg_6_0.prefab

		PoolMgr.GetInstance().GetSpineChar(var_6_1, True, function(arg_7_0)
			if var_6_1 != arg_6_0.prefab:
				PoolMgr.GetInstance().ReturnSpineChar(var_6_1, arg_7_0)

				return

			arg_6_0.model = arg_7_0
			arg_6_0.model.transform.localScale = Vector3.one
			arg_6_0.model.transform.localPosition = Vector3.zero

			arg_6_0.model.transform.SetParent(arg_6_0._tf, False)

			arg_6_0.anim = arg_6_0.model.GetComponent(typeof(SpineAnimUI))

			arg_6_0.updateState(var_0_0.ShipState.Walk))

	arg_6_0.prefabName = arg_6_1

def var_0_0.updateLogic(arg_8_0):
	arg_8_0.clearLogic()

	if arg_8_0.state == var_0_0.ShipState.Walk:
		local var_8_0 = arg_8_0.currentPoint
		local var_8_1 = arg_8_0.targetPoint
		local var_8_2 = 15
		local var_8_3 = Vector2.Distance(var_8_0, var_8_1) / var_8_2

		if arg_8_0.posTable[arg_8_0.currentPoint.id] == arg_8_0:
			arg_8_0.posTable[arg_8_0.currentPoint.id] = None

		arg_8_0._tf.localScale = (var_8_0.scale or var_0_0.normalScale) * Vector2.one

		local var_8_4 = arg_8_0.pathFinder.getEdge(var_8_0, var_8_1)

		LeanTween.value(arg_8_0._go, 0, 1, var_8_3).setOnUpdate(System.Action_float(function(arg_9_0)
			local var_9_0

			if var_8_4 and var_8_4.bezier_control_point:
				local var_9_1 = arg_8_0.pathFinder.getPoint(var_8_4.bezier_control_point)

				var_9_0 = var_0_0.GetBeziersPoints(var_8_0, var_8_1, var_9_1, arg_9_0)
			else
				var_9_0 = Vector2.Lerp(var_8_0, var_8_1, arg_9_0)

			arg_8_0._tf.anchoredPosition = var_9_0

			local var_9_2 = math.lerp(var_8_0.scale or var_0_0.normalScale, var_8_1.scale or var_0_0.normalScale, arg_9_0) * Vector2.one
			local var_9_3 = var_8_1.x > var_8_0.x and 1 or -1

			if var_8_0.id == var_8_1.id:
				var_9_3 = math.random(0, 1) == 1 and 1 or -1

			if var_8_0.fixedDirection:
				var_9_3 = math.sign(var_8_0.fixedDirection)

			var_9_2.x = math.abs(var_9_2.x) * var_9_3
			arg_8_0._tf.localScale = var_9_2)).setOnComplete(System.Action(function()
			arg_8_0.currentPoint = arg_8_0.targetPoint

			local var_10_0 = arg_8_0.currentPoint.id
			local var_10_1 = arg_8_0.currentPoint.nexts
			local var_10_2 = var_10_1[math.random(1, #var_10_1)]

			if arg_8_0.onTransEdge and var_10_2:
				arg_8_0.targetPoint = arg_8_0.pathFinder.getPoint(var_10_2)

				arg_8_0.onTransEdge(arg_8_0, var_10_0, var_10_2)

			arg_8_0.updateState(var_0_0.ShipState.Idle)))
	elif arg_8_0.state == var_0_0.ShipState.Idle:
		if arg_8_0.posTable[arg_8_0.currentPoint.id] == None:
			arg_8_0.posTable[arg_8_0.currentPoint.id] = arg_8_0
		else
			arg_8_0.updateState(var_0_0.ShipState.Walk)

			return

		if arg_8_0.currentPoint.isBan:
			arg_8_0.updateState(var_0_0.ShipState.Walk)

			return

		local var_8_5 = math.random(10, 20)

		arg_8_0.idleTimer = Timer.New(function()
			arg_8_0.updateState(var_0_0.ShipState.Walk), var_8_5, 1)

		arg_8_0.idleTimer.Start()
	elif arg_8_0.state == var_0_0.ShipState.Touch:
		arg_8_0.onClickShip()

def var_0_0.GetBeziersPoints(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	local var_12_0 = arg_12_0.Clone().Mul((1 - arg_12_3) * (1 - arg_12_3))
	local var_12_1 = arg_12_2.Clone().Mul(2 * arg_12_3 * (1 - arg_12_3))
	local var_12_2 = arg_12_1.Clone().Mul(arg_12_3 * arg_12_3)

	return var_12_0.Add(var_12_1).Add(var_12_2)

return var_0_0
