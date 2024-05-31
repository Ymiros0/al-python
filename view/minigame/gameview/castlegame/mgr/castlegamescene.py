local var_0_0 = class("CastleGameScene")
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.sceneMask = findTF(arg_1_0._tf, "sceneMask")
	arg_1_0.tplContent = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/tpl")
	arg_1_0.floorTpl = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/tpl/floorTpl")
	arg_1_0.charTpl = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/tpl/charTpl")
	arg_1_0.carriageTpl = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/tpl/carriageTpl")
	arg_1_0.bubbleTpl = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/tpl/bubbleTpl")
	arg_1_0.scoreTpl = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/tpl/scoreTpl")
	arg_1_0.contentBack = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene_background/content")
	arg_1_0.contentMid = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/content")
	arg_1_0.contentTop = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene_front/content")
	arg_1_0.contentEF = findTF(arg_1_0._tf, "sceneMask/sceneContainer/scene/effect_front")

	local var_1_0 = CastleGameVo.GetRotationPosByWH(0, -1)

	arg_1_0.gameFloor = CastleGameFloor.New(arg_1_0.floorTpl, arg_1_0._event)
	arg_1_0.gameChar = CastleGameChar.New(arg_1_0.charTpl, arg_1_0._event)
	arg_1_0.gameItem = CastleGameItem.New(arg_1_0.tplContent, arg_1_0._event)
	arg_1_0.gameRemind = CastleGameRemind.New(arg_1_0.tplContent, arg_1_0._event)
	arg_1_0.gameScore = CastleGameScore.New(arg_1_0.scoreTpl, arg_1_0._event)

	arg_1_0.gameFloor.setContent(arg_1_0.getContent(var_0_2))
	arg_1_0.gameChar.setContent(arg_1_0.getContent(var_0_3))
	arg_1_0.gameItem.setContent(arg_1_0.getContent(var_0_3))
	arg_1_0.gameRemind.setContent(arg_1_0.getContent(var_0_4))
	arg_1_0.gameScore.setContent(arg_1_0.getContent(var_0_3))
	arg_1_0.gameFloor.setFloorFallCallback(function(arg_2_0)
		arg_1_0.addRemindItems(arg_2_0))

	local var_1_1 = arg_1_0.gameFloor.getOutLandPoint()

	arg_1_0.gameChar.setOutLandPoint(var_1_1)

	arg_1_0.floorItems = {}

	arg_1_0.insertFloorItem(arg_1_0.gameFloor.getFloors())

	arg_1_0.items = {}

	table.insert(arg_1_0.items, arg_1_0.gameChar.getChar())
	arg_1_0.gameItem.setItemRemindCallback(function(arg_3_0)
		arg_1_0.addRemindItems(arg_3_0))
	arg_1_0.gameItem.setItemChange(function(arg_4_0, arg_4_1)
		arg_1_0.itemChange(arg_4_0, arg_4_1))
	arg_1_0.gameItem.setFloorBroken(function(arg_5_0, arg_5_1)
		for iter_5_0, iter_5_1 in ipairs(arg_5_0):
			arg_1_0.gameFloor.setBroken(iter_5_1, arg_5_1))
	arg_1_0.gameScore.setItemChange(function(arg_6_0, arg_6_1)
		arg_1_0.itemChange(arg_6_0, arg_6_1))
	arg_1_0.gameItem.setBubbleBroken(function(arg_7_0)
		if arg_7_0 and arg_7_0.char:
			arg_1_0.returnPlayerBubble(arg_7_0, arg_7_0.char))
	arg_1_0.sortItems(arg_1_0.floorItems)

def var_0_0.addRemindItems(arg_8_0, arg_8_1):
	for iter_8_0 = 1, #arg_8_1:
		local var_8_0 = arg_8_1[iter_8_0]
		local var_8_1 = var_8_0.w
		local var_8_2 = var_8_0.h
		local var_8_3 = var_8_0.type and var_8_0.type or CastleGameRemind.remind_type_1

		arg_8_0.gameRemind.addRemind(var_8_1, var_8_2, var_8_3)

def var_0_0.itemChange(arg_9_0, arg_9_1, arg_9_2):
	if arg_9_2:
		if table.contains(arg_9_0.items, arg_9_1):
			return

		table.insert(arg_9_0.items, arg_9_1)
	else
		for iter_9_0 = 1, #arg_9_0.items:
			if arg_9_0.items[iter_9_0] == arg_9_1:
				table.remove(arg_9_0.items, iter_9_0)

				return

def var_0_0.start(arg_10_0):
	arg_10_0.prepareScene()
	arg_10_0.gameFloor.start()
	arg_10_0.gameChar.start()
	arg_10_0.gameItem.start()
	arg_10_0.gameRemind.start()
	arg_10_0.gameScore.start()

def var_0_0.step(arg_11_0):
	arg_11_0.gameFloor.step()
	arg_11_0.gameChar.step()
	arg_11_0.gameItem.step()
	arg_11_0.gameRemind.step()
	arg_11_0.gameScore.step()
	arg_11_0.sortItems(arg_11_0.items)
	arg_11_0.updateActiveFloor()
	arg_11_0.checkPlayerInFloor()
	arg_11_0.checkPlayerInBubble()
	arg_11_0.checkPlayerCarriage()
	arg_11_0.checkPlayerInScore()

def var_0_0.clear(arg_12_0):
	arg_12_0.gameFloor.clear()
	arg_12_0.gameChar.clear()
	arg_12_0.gameItem.clear()
	arg_12_0.gameRemind.clear()

def var_0_0.stop(arg_13_0):
	return

def var_0_0.resume(arg_14_0):
	return

def var_0_0.dispose(arg_15_0):
	return

def var_0_0.prepareScene(arg_16_0):
	arg_16_0.showContainer(True)
	arg_16_0.sortItems(arg_16_0.floorItems)
	arg_16_0.gameChar.setContent(arg_16_0.getContent(var_0_3))
	CastleGameVo.PointFootLine(Vector2(0, 0), Vector2(0, 100), Vector2(100, 0))

def var_0_0.updateActiveFloor(arg_17_0):
	local var_17_0 = arg_17_0.gameFloor.getActiveIndexs()

	arg_17_0.gameItem.setFloorIndexs(var_17_0)

	local var_17_1 = arg_17_0.gameFloor.getFloors()

	arg_17_0.gameScore.setFloor(var_17_1)

def var_0_0.checkPlayerInScore(arg_18_0):
	if arg_18_0.gameChar.getActionAble():
		local var_18_0 = arg_18_0.gameChar.getChar()
		local var_18_1 = var_18_0.tf.anchoredPosition
		local var_18_2 = arg_18_0.gameScore.getScores()

		for iter_18_0 = 1, #var_18_2:
			local var_18_3 = var_18_2[iter_18_0]

			if var_18_3.ready == 0:
				local var_18_4 = var_18_3.tf.anchoredPosition
				local var_18_5 = var_18_3.bmin
				local var_18_6 = var_18_3.bmax
				local var_18_7 = Vector2(var_18_4.x + var_18_5.x, var_18_4.y + var_18_5.y)
				local var_18_8 = Vector2(var_18_4.x + var_18_6.x, var_18_4.y + var_18_6.y)

				if var_18_1.x >= var_18_7.x and var_18_1.y >= var_18_7.y and var_18_1.x <= var_18_8.x and var_18_1.y <= var_18_8.y:
					arg_18_0.setPlayerScore(var_18_3, var_18_0)

					return

def var_0_0.checkPlayerInBubble(arg_19_0):
	if arg_19_0.gameChar.getActionAble():
		local var_19_0 = arg_19_0.gameChar.getChar()
		local var_19_1 = var_19_0.tf.anchoredPosition
		local var_19_2 = arg_19_0.gameItem.getBubbles()

		for iter_19_0 = 1, #var_19_2:
			local var_19_3 = var_19_2[iter_19_0]

			if var_19_3.ready == 0 and not var_19_3.broken and isActive(var_19_3.tf) and var_19_3.hit:
				local var_19_4 = var_19_3.tf.anchoredPosition
				local var_19_5 = var_19_3.bmin
				local var_19_6 = var_19_3.bmax
				local var_19_7 = Vector2(var_19_4.x + var_19_5.x, var_19_4.y + var_19_5.y)
				local var_19_8 = Vector2(var_19_4.x + var_19_6.x, var_19_4.y + var_19_6.y)

				if var_19_1.x >= var_19_7.x and var_19_1.y >= var_19_7.y and var_19_1.x <= var_19_8.x and var_19_1.y <= var_19_8.y:
					arg_19_0.setPlayerBubble(var_19_3, var_19_0)

					return

def var_0_0.checkPlayerBoom(arg_20_0):
	if arg_20_0.gameChar.getActionAble():
		local var_20_0 = arg_20_0.gameChar.getChar().tf.anchoredPosition
		local var_20_1 = arg_20_0.gameItem.getBooms()
		local var_20_2 = False

		for iter_20_0 = 1, #var_20_1:
			local var_20_3 = var_20_1[iter_20_0]

			if var_20_3.ready and var_20_3.ready == 0 and not var_20_3.broken and var_20_3.brokenTime < 1:
				local var_20_4 = var_20_3.boundPoints

				if not var_20_2:
					local var_20_5 = CastleGameVo.PointInTriangle(var_20_0, var_20_4[1], var_20_4[2], var_20_4[3])
					local var_20_6 = CastleGameVo.PointInTriangle(var_20_0, var_20_4[3], var_20_4[4], var_20_4[1])

					if var_20_5:
						var_20_2 = True
					elif var_20_6:
						var_20_2 = True

				if var_20_2:
					arg_20_0.gameChar.setPlayerFail()

					return

def var_0_0.checkPlayerCarriage(arg_21_0):
	if arg_21_0.gameChar.getActionAble():
		local var_21_0 = arg_21_0.gameChar.getChar().tf.anchoredPosition
		local var_21_1 = arg_21_0.gameItem.getCarriages()

		for iter_21_0 = 1, #var_21_1:
			local var_21_2 = var_21_1[iter_21_0]
			local var_21_3 = var_21_2.bmin
			local var_21_4 = var_21_2.bmax
			local var_21_5 = var_21_2.tf.anchoredPosition
			local var_21_6 = Vector2(var_21_5.x + var_21_3.x, var_21_5.y + var_21_3.y)
			local var_21_7 = Vector2(var_21_5.x + var_21_4.x, var_21_5.y + var_21_4.y)

			if var_21_0.x >= var_21_6.x and var_21_0.y >= var_21_6.y and var_21_0.x <= var_21_7.x and var_21_0.y <= var_21_7.y:
				arg_21_0.gameChar.setPlayerFail()

				return

def var_0_0.setPlayerScore(arg_22_0, arg_22_1, arg_22_2):
	local var_22_0 = arg_22_0.gameChar.getChar()

	arg_22_0.gameChar.setScore(arg_22_1)
	arg_22_0.gameScore.hitScore(arg_22_1)
	arg_22_0._event.emit(CastleGameView.ADD_SCORE, {
		num = arg_22_1.data.score,
		pos = var_22_0.tf.position,
		id = arg_22_1.id
	})

def var_0_0.returnPlayerBubble(arg_23_0, arg_23_1, arg_23_2):
	arg_23_0.gameChar.setContent(arg_23_0.contentTop)
	arg_23_0.gameChar.setInBubble(False)

	arg_23_1.char = None

def var_0_0.setPlayerBubble(arg_24_0, arg_24_1, arg_24_2):
	arg_24_0.gameChar.setInBubble(True)
	arg_24_0.gameChar.setContent(arg_24_1.pos, Vector3(0, 0, 0))

	arg_24_1.char = arg_24_2

	arg_24_0.gameItem.playerInBubble(arg_24_1, arg_24_2)

def var_0_0.checkPlayerInFloor(arg_25_0):
	if arg_25_0.gameChar.getActionAble():
		local var_25_0 = arg_25_0.gameChar.getChar()
		local var_25_1 = var_25_0.tf.anchoredPosition
		local var_25_2 = arg_25_0.gameFloor.getFloors()
		local var_25_3 = False

		for iter_25_0 = 1, #var_25_2:
			local var_25_4 = var_25_2[iter_25_0]
			local var_25_5 = var_25_4.bound

			if not var_25_3:
				local var_25_6 = CastleGameVo.PointInTriangle(var_25_1, var_25_5[1], var_25_5[2], var_25_5[3])
				local var_25_7 = CastleGameVo.PointInTriangle(var_25_1, var_25_5[3], var_25_5[4], var_25_5[1])

				if var_25_6:
					var_25_3 = True
				elif var_25_7:
					var_25_3 = True

			if var_25_3:
				var_25_0.floor = var_25_2[iter_25_0]

				if var_25_4.fall == True:
					arg_25_0.setCharFall()

				return

def var_0_0.setCharFall(arg_26_0):
	arg_26_0.gameChar.setInGround(False)

def var_0_0.insertFloorItem(arg_27_0, arg_27_1):
	for iter_27_0 = 1, #arg_27_1:
		table.insert(arg_27_0.floorItems, arg_27_1[iter_27_0])

def var_0_0.getContent(arg_28_0, arg_28_1):
	local var_28_0

	if arg_28_1 == var_0_1:
		var_28_0 = arg_28_0.contentBack
	elif arg_28_1 == var_0_2:
		var_28_0 = arg_28_0.contentMid
	elif arg_28_1 == var_0_3:
		var_28_0 = arg_28_0.contentTop
	elif arg_28_1 == var_0_4:
		var_28_0 = arg_28_0.contentEF

	return var_28_0

def var_0_0.sortItems(arg_29_0, arg_29_1):
	table.sort(arg_29_1, function(arg_30_0, arg_30_1)
		local var_30_0 = arg_30_0.tf.anchoredPosition
		local var_30_1 = arg_30_1.tf.anchoredPosition

		if var_30_0.y > var_30_1.y:
			return False
		elif var_30_0.y < var_30_1.y:
			return True

		if var_30_0.x > var_30_1.x:
			return False
		elif var_30_0.x < var_30_1.x:
			return True

		return False)

	for iter_29_0 = 1, #arg_29_1:
		arg_29_1[iter_29_0].tf.SetSiblingIndex(0)

def var_0_0.compareByPosition(arg_31_0, arg_31_1, arg_31_2):
	return

def var_0_0.compareWithPosBound(arg_32_0, arg_32_1, arg_32_2):
	local var_32_0 = arg_32_2[1]
	local var_32_1 = arg_32_2[4]

	return CastleGameVo.PointLeftLine(arg_32_1, var_32_0, var_32_1)

def var_0_0.showContainer(arg_33_0, arg_33_1):
	setActive(arg_33_0.sceneMask, arg_33_1)

def var_0_0.press(arg_34_0, arg_34_1):
	arg_34_0.gameFloor.press(arg_34_1)
	arg_34_0.sortItems(arg_34_0.floorItems)

return var_0_0
