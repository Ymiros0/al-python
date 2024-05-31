local var_0_0 = class("LaunchBallGameJoyStick")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1
	arg_1_0.smoothX = 0.01
	arg_1_0.smoothY = 0.01
	arg_1_0.maxDistance = 120
	arg_1_0.minDeadNum = 0.1
	arg_1_0.maxDeadNum = 0.9
	arg_1_0.currentPos = Vector2(0, 0)
	arg_1_0.targetPos = Vector2(0, 0)
	arg_1_0.currentX = 0
	arg_1_0.currentY = 0
	arg_1_0.currentXSmooth = 0
	arg_1_0.currentYSmooth = 0
	arg_1_0.active = False
	arg_1_0.startPos = Vector2(0, 0)
	arg_1_0.dragPos = Vector2(0, 0)
	arg_1_0.uiCam = GameObject.Find("UICamera").GetComponent("Camera")
	arg_1_0._controlTf = findTF(arg_1_0._tf, "control")
	arg_1_0._joyTf = findTF(arg_1_0._tf, "control/joy")
	arg_1_0._eventTriggerListener = GetComponent(arg_1_0._controlTf, typeof(EventTriggerListener))

	arg_1_0._eventTriggerListener.AddPointDownFunc(function(arg_2_0, arg_2_1)
		arg_1_0.active = True

		local var_2_0 = arg_1_0.uiCam.ScreenToWorldPoint(arg_2_1.position)

		arg_1_0.dragPos = arg_1_0._controlTf.InverseTransformPoint(var_2_0)

		arg_1_0.setTargetPos(arg_1_0.getOffset(arg_1_0.dragPos, arg_1_0.startPos))

		if arg_1_0.activeCallback:
			arg_1_0.activeCallback(True))
	arg_1_0._eventTriggerListener.AddDragFunc(function(arg_3_0, arg_3_1)
		local var_3_0 = arg_1_0.uiCam.ScreenToWorldPoint(arg_3_1.position)

		arg_1_0.dragPos = arg_1_0._controlTf.InverseTransformPoint(var_3_0)

		arg_1_0.setTargetPos(arg_1_0.getOffset(arg_1_0.dragPos, arg_1_0.startPos)))
	arg_1_0._eventTriggerListener.AddPointUpFunc(function(arg_4_0, arg_4_1)
		arg_1_0.active = False

		if arg_1_0.activeCallback:
			arg_1_0.activeCallback(False))
	arg_1_0.setTargetPos(Vector2(0, 0))

def var_0_0.setTargetPos(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0.startPos

	if math.sqrt(math.pow(arg_5_1.x - var_5_0.x, 2) + math.pow(arg_5_1.y - var_5_0.y, 2)) > arg_5_0.maxDistance:
		local var_5_1 = math.atan(math.abs(arg_5_1.y - var_5_0.y) / math.abs(arg_5_1.x - var_5_0.x))
		local var_5_2 = arg_5_1.x > var_5_0.x and 1 or -1
		local var_5_3 = arg_5_1.y > var_5_0.y and 1 or -1
		local var_5_4 = math.cos(var_5_1) * var_5_2 * arg_5_0.maxDistance
		local var_5_5 = math.sin(var_5_1) * var_5_3 * arg_5_0.maxDistance

		arg_5_0.targetPos.x = var_5_4
		arg_5_0.targetPos.y = var_5_5
	else
		arg_5_0.targetPos = arg_5_1

def var_0_0.getOffset(arg_6_0, arg_6_1, arg_6_2):
	return Vector2(arg_6_1.x - arg_6_2.x, arg_6_1.y - arg_6_2.y)

def var_0_0.show(arg_7_0, arg_7_1):
	setActive(arg_7_0._tf, arg_7_1)

def var_0_0.step(arg_8_0):
	arg_8_0.currentPos = arg_8_0._joyTf.anchoredPosition
	arg_8_0.currentX, arg_8_0.currentXSmooth = Mathf.SmoothDamp(arg_8_0.currentPos.x, arg_8_0.targetPos.x, arg_8_0.currentXSmooth, arg_8_0.smoothX)
	arg_8_0.currentY, arg_8_0.currentYSmooth = Mathf.SmoothDamp(arg_8_0.currentPos.y, arg_8_0.targetPos.y, arg_8_0.currentYSmooth, arg_8_0.smoothY)
	arg_8_0.currentPos.x = arg_8_0.currentX
	arg_8_0.currentPos.y = arg_8_0.currentY
	arg_8_0._joyTf.anchoredPosition = arg_8_0.currentPos
	arg_8_0.distanceRate = math.sqrt(math.pow(arg_8_0.currentX - arg_8_0.startPos.x, 2) + math.pow(arg_8_0.currentY - arg_8_0.startPos.y, 2)) / arg_8_0.maxDistance

	if math.abs(arg_8_0.currentY - arg_8_0.startPos.y) <= 1 and math.abs(arg_8_0.currentX - arg_8_0.startPos.x) <= 1:
		arg_8_0.angle = None
		arg_8_0.rad = None
	else
		arg_8_0.rad = math.atan2(arg_8_0.currentY - arg_8_0.startPos.y, arg_8_0.currentX - arg_8_0.startPos.x)
		arg_8_0.angle = arg_8_0.rad * math.rad2Deg

	arg_8_0.offsetX = arg_8_0.currentPos.x / arg_8_0.maxDistance
	arg_8_0.offsetY = arg_8_0.currentPos.y / arg_8_0.maxDistance

	if arg_8_0.valueCallback:
		arg_8_0.valueCallback(arg_8_0.getValue())

def var_0_0.setDirectTarget(arg_9_0, arg_9_1):
	if not arg_9_0.active:
		arg_9_0.setTargetPos(Vector2(arg_9_1.x * 1000, arg_9_1.y * 1000))

def var_0_0.setValueCallback(arg_10_0, arg_10_1):
	arg_10_0.valueCallback = arg_10_1

def var_0_0.setActiveCallback(arg_11_0, arg_11_1):
	arg_11_0.activeCallback = arg_11_1

def var_0_0.getValue(arg_12_0):
	return {
		angle = arg_12_0.angle,
		rad = arg_12_0.rad,
		rate = arg_12_0.distanceRate,
		x = arg_12_0.offsetX,
		y = arg_12_0.offsetY,
		active = arg_12_0.active
	}

return var_0_0
