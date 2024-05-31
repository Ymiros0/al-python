local var_0_0 = class("CastleGameChar")
local var_0_1 = Vector3(0, 0)
local var_0_2 = "qiye_6_SkeletonData"
local var_0_3 = 3
local var_0_4 = "activity_run"
local var_0_5 = "walk"
local var_0_6 = "activity_wait"
local var_0_7 = "tuozhuai2"
local var_0_8 = "tuozhuai2"
local var_0_9 = "dead"
local var_0_10 = Vector3(0, 0, -1)

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._charTpl = arg_1_1
	arg_1_0._event = arg_1_2

	arg_1_0.initChar()

def var_0_0.initChar(arg_2_0):
	if arg_2_0.char:
		return

	arg_2_0.charTf = tf(instantiate(arg_2_0._charTpl))
	arg_2_0.speed = Vector3(0, 0, 0)
	arg_2_0.colliderTf = findTF(arg_2_0.charTf, "zPos/collider")
	arg_2_0.collider = GetComponent(arg_2_0.colliderTf, typeof(BoxCollider2D))
	arg_2_0.zPos = findTF(arg_2_0.charTf, "zPos")
	arg_2_0.raycastPoints = {}

	for iter_2_0 = 1, var_0_3:
		table.insert(arg_2_0.raycastPoints, Vector3(0, 0, 0))

	CastleGameVo.LoadSkeletonData(var_0_2, function(arg_3_0)
		arg_3_0.transform.localScale = Vector3(1, 1, 1)
		arg_3_0.transform.localPosition = Vector3(0, 0, 0)

		arg_3_0.SetActive(True)
		SetParent(tf(arg_3_0), findTF(arg_2_0.charTf, "zPos/char"))

		arg_2_0.graphic = arg_3_0.GetComponent("SkeletonGraphic")
		arg_2_0.anim = arg_3_0.GetComponent(typeof(SpineAnimUI))
		arg_2_0.charTf.anchoredPosition = var_0_1
		arg_2_0.zPos.anchoredPosition = Vector2(0, var_0_1.z))

	arg_2_0.char = {
		tf = arg_2_0.charTf,
		bound = {}
	}

def var_0_0.setInGround(arg_4_0, arg_4_1):
	arg_4_0.inGround = arg_4_1

	if not arg_4_0.inGround:
		arg_4_0.speed = Vector3(0, 0, 0)

	if arg_4_0.char.floor:
		local var_4_0 = arg_4_0.char.floor.tf

		arg_4_0.setContent(findTF(var_4_0, "zPos/top"))

def var_0_0.setOutLandPoint(arg_5_0, arg_5_1):
	arg_5_0.outlandPoint = arg_5_1

	local var_5_0 = arg_5_0.outlandPoint.lb
	local var_5_1 = arg_5_0.outlandPoint.lt
	local var_5_2 = arg_5_0.outlandPoint.rt
	local var_5_3 = arg_5_0.outlandPoint.rb
	local var_5_4 = 2
	local var_5_5 = Vector2(var_5_0.x + var_5_4, var_5_0.y)
	local var_5_6 = Vector2(var_5_1.x, var_5_1.y - var_5_4)
	local var_5_7 = Vector2(var_5_2.x - var_5_4, var_5_2.y)
	local var_5_8 = Vector2(var_5_3.x, var_5_3.y + var_5_4)

	arg_5_0.outlandPoint.exlb = var_5_5
	arg_5_0.outlandPoint.exlt = var_5_6
	arg_5_0.outlandPoint.exrt = var_5_7
	arg_5_0.outlandPoint.exrb = var_5_8

def var_0_0.step(arg_6_0):
	if arg_6_0.timeToOver and arg_6_0.timeToOver > 0:
		arg_6_0.timeToOver = arg_6_0.timeToOver - CastleGameVo.deltaTime

		if arg_6_0.timeToOver <= 0:
			arg_6_0.timeToOver = None

			arg_6_0._event.emit(CastleGameView.GAME_OVER)

	arg_6_0.updateSpeed()
	arg_6_0.updatePosition()
	arg_6_0.updateAnim()
	arg_6_0.checkPlayerOutScreen()

def var_0_0.getPoint(arg_7_0):
	if arg_7_0.charTf:
		return None

	return arg_7_0.charTf.anchoredPosition

def var_0_0.updatePosition(arg_8_0):
	local var_8_0 = arg_8_0.charTf.anchoredPosition
	local var_8_1 = arg_8_0.zPos.anchoredPosition

	var_8_0.x = var_8_0.x + arg_8_0.speed.x * CastleGameVo.deltaTime
	var_8_0.y = var_8_0.y + arg_8_0.speed.y * CastleGameVo.deltaTime

	local var_8_2, var_8_3 = arg_8_0.checkOutland(var_8_0)

	if var_8_2 and var_8_3:
		arg_8_0.charTf.anchoredPosition = var_8_3

		arg_8_0.updateDirect(var_8_3)

	var_8_1.y = var_8_1.y + arg_8_0.speed.z * CastleGameVo.deltaTime
	arg_8_0.zPos.anchoredPosition = var_8_1

def var_0_0.updateDirect(arg_9_0, arg_9_1):
	if arg_9_1.x != 0:
		local var_9_0 = arg_9_0.speed.x > 0 and 1 or -1

		if arg_9_0.charTf.localScale.x != var_9_0:
			arg_9_0.charTf.localScale = Vector3(var_9_0, 1, 1)
			arg_9_0.charDirect = var_9_0

def var_0_0.checkOutland(arg_10_0, arg_10_1, arg_10_2):
	if arg_10_0.outlandPoint:
		local var_10_0 = arg_10_0.outlandPoint.lb
		local var_10_1 = arg_10_0.outlandPoint.lt
		local var_10_2 = arg_10_0.outlandPoint.rt
		local var_10_3 = arg_10_0.outlandPoint.rb
		local var_10_4 = arg_10_0.outlandPoint.exlb
		local var_10_5 = arg_10_0.outlandPoint.exlt
		local var_10_6 = arg_10_0.outlandPoint.exrt
		local var_10_7 = arg_10_0.outlandPoint.exrb

		if CastleGameVo.PointLeftLine(arg_10_1, var_10_0, var_10_1):
			local var_10_8, var_10_9 = CastleGameVo.PointFootLine(arg_10_1, var_10_4, var_10_5)

			if var_10_9:
				return arg_10_0.checkOutland(var_10_8, var_10_9)
			else
				return False

		if CastleGameVo.PointLeftLine(arg_10_1, var_10_3, var_10_0):
			local var_10_10, var_10_11 = CastleGameVo.PointFootLine(arg_10_1, var_10_7, var_10_4)

			if var_10_11:
				return arg_10_0.checkOutland(var_10_10)
			else
				return False

		if CastleGameVo.PointLeftLine(arg_10_1, var_10_1, var_10_2):
			local var_10_12, var_10_13 = CastleGameVo.PointFootLine(arg_10_1, var_10_5, var_10_6)

			if var_10_13:
				return arg_10_0.checkOutland(var_10_12)
			else
				return False

		if CastleGameVo.PointLeftLine(arg_10_1, var_10_2, var_10_3):
			local var_10_14, var_10_15 = CastleGameVo.PointFootLine(arg_10_1, var_10_6, var_10_7)

			if var_10_15:
				return arg_10_0.checkOutland(var_10_14)
			else
				return False

	return True, arg_10_1

def var_0_0.updateSpeed(arg_11_0):
	if arg_11_0.addSpeedTime and arg_11_0.addSpeedTime > 0:
		arg_11_0.addSpeedTime = arg_11_0.addSpeedTime - CastleGameVo.deltaTime

		if arg_11_0.addSpeedTime <= 0:
			arg_11_0.addSpeedTime = None
			arg_11_0.addSpeed = 0

	if not arg_11_0.inGround:
		arg_11_0.speed.z = arg_11_0.speed.z > -1500 and arg_11_0.speed.z - 20 or -1500
	elif arg_11_0.inBubble:
		arg_11_0.speed.x = 0
		arg_11_0.speed.y = 0
		arg_11_0.speed.z = 0

		print("角色在气泡中，无法移动")
	elif arg_11_0.fail:
		arg_11_0.speed.x = 0
		arg_11_0.speed.y = 0
		arg_11_0.speed.z = 0

		print("被车撞了，无法移动")
	elif CastleGameVo.joyStickData:
		local var_11_0 = CastleGameVo.joyStickData
		local var_11_1 = var_11_0.x
		local var_11_2 = var_11_0.y

		arg_11_0.speed.x = var_11_0.x * (CastleGameVo.char_speed + arg_11_0.addSpeed)
		arg_11_0.speed.y = var_11_0.y * (CastleGameVo.char_speed + arg_11_0.addSpeed)
		arg_11_0.speed.x = math.abs(arg_11_0.speed.x) < CastleGameVo.char_speed_min and 0 or arg_11_0.speed.x
		arg_11_0.speed.y = math.abs(arg_11_0.speed.y) < CastleGameVo.char_speed_min and 0 or arg_11_0.speed.y

		arg_11_0.updateDirect(arg_11_0.speed)
	else
		arg_11_0.speed.x = 0
		arg_11_0.speed.y = 0

def var_0_0.updateAnim(arg_12_0):
	local var_12_0

	if not arg_12_0.inGround:
		var_12_0 = var_0_7
	elif arg_12_0.inBubble:
		var_12_0 = var_0_8
	elif arg_12_0.fail:
		var_12_0 = var_0_9
	else
		local var_12_1 = math.max(math.abs(arg_12_0.speed.x), math.abs(arg_12_0.speed.y))

		if var_12_1 > 120:
			var_12_0 = var_0_4
		elif var_12_1 > 0:
			var_12_0 = var_0_5
		else
			var_12_0 = var_0_6

	if arg_12_0.action != var_12_0:
		arg_12_0.changeAnimAction(arg_12_0.anim, var_12_0, 0)

def var_0_0.setScore(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_1.data.speed
	local var_13_1 = arg_13_1.data.time

	if var_13_0 >= arg_13_0.addSpeed:
		arg_13_0.addSpeed = var_13_0

	arg_13_0.addSpeedTime = var_13_1

def var_0_0.setPlayerFail(arg_14_0):
	arg_14_0.fail = True
	arg_14_0.timeToOver = 1

	arg_14_0.playerDead()

def var_0_0.setContent(arg_15_0, arg_15_1, arg_15_2):
	arg_15_0._content = arg_15_1

	setParent(arg_15_0.charTf, arg_15_0._content, True)

	arg_15_0.charTf.localScale = Vector3(1, 1, 1)

	if arg_15_2:
		arg_15_0.charTf.anchoredPosition = arg_15_2

def var_0_0.getPoint(arg_16_0):
	return arg_16_0.charTf.anchoredPosition

def var_0_0.start(arg_17_0):
	arg_17_0.charTf.anchoredPosition = var_0_1
	arg_17_0.zPos.anchoredPosition = Vector2(0, var_0_1.y)

	setActive(arg_17_0.charTf, True)

	arg_17_0.inGround = True
	arg_17_0.inBubble = False
	arg_17_0.fail = False
	arg_17_0.timeToOver = None
	arg_17_0.speed = Vector3(0, 0, 0)
	arg_17_0.addSpeed = 0
	arg_17_0.addSpeedTime = 0

	arg_17_0.changeAnimAction(arg_17_0.anim, var_0_6, 0)

def var_0_0.clear(arg_18_0):
	return

def var_0_0.checkPlayerOutScreen(arg_19_0):
	if math.abs(arg_19_0.zPos.anchoredPosition.y) > 2000:
		arg_19_0._event.emit(CastleGameView.GAME_OVER)

def var_0_0.setInBubble(arg_20_0, arg_20_1):
	arg_20_0.inBubble = arg_20_1

	if arg_20_1:
		arg_20_0.lastBubblePos = arg_20_0.char.tf.anchoredPosition
	else
		arg_20_0.char.tf.anchoredPosition = arg_20_0.lastBubblePos

def var_0_0.getActionAble(arg_21_0):
	if not arg_21_0.inGround:
		return False

	if arg_21_0.inBubble:
		return False

	if arg_21_0.fail:
		return False

	return True

def var_0_0.press(arg_22_0, arg_22_1):
	return

def var_0_0.playerDead(arg_23_0):
	arg_23_0.action = var_0_9

	arg_23_0.anim.GetAnimationState().SetAnimation(0, var_0_9, False)

def var_0_0.changeAnimAction(arg_24_0, arg_24_1, arg_24_2, arg_24_3, arg_24_4, arg_24_5):
	arg_24_0.action = arg_24_2

	arg_24_1.SetActionCallBack(None)
	arg_24_1.SetAction(arg_24_2, 0)
	arg_24_1.SetActionCallBack(function(arg_25_0)
		if arg_25_0 == "finish":
			if arg_24_3 == 1:
				arg_24_1.SetActionCallBack(None)

			if arg_24_5:
				arg_24_5())

	if arg_24_3 != 1 and arg_24_5:
		arg_24_5()

def var_0_0.getChar(arg_26_0):
	return arg_26_0.char

def var_0_0.getTfs(arg_27_0):
	return {
		arg_27_0.charTf
	}

return var_0_0
