local var_0_0 = class("SailBoatGameScene")
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5

var_0_0.random_scene_imgs = {
	{
		content = "scene_background/content/bg_6",
		icon = {
			"06_Deep_Multiply_1",
			"06_Deep_Multiply_2",
			"06_Deep_Multiply_3",
			"06_Deep_Multiply_4",
			"06_Deep_Multiply_5",
			"06_Deep_Multiply_6",
			"06_Deep_Multiply_7"
		}
	}
}

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_5 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.sceneMask = findTF(arg_1_0._tf, "sceneMask")
	arg_1_0.sceneContent = findTF(arg_1_0._tf, "sceneMask/sceneContainer")

	local function var_1_0(arg_2_0, arg_2_1)
		if arg_2_0 == SailBoatGameEvent.DESTROY_ENEMY:
			arg_1_0.destroyEnemy(arg_2_1)
		elif arg_2_0 == SailBoatGameEvent.USE_ITEM:
			arg_1_0._event.emit(SailBoatGameView.ADD_SCORE, {
				num = arg_2_1.score
			})

			if arg_2_1.skill:
				var_0_5.AddSkill()
		elif arg_2_0 == SailBoatGameEvent.PLAYER_DEAD:
			arg_1_0._event.emit(SailBoatGameView.GAME_OVER)

		arg_1_0.onSceneEventCall(arg_2_0, arg_2_1)

	arg_1_0.charControl = SailBoatCharControl.New(arg_1_0.sceneContent, var_1_0)
	arg_1_0.bgControl = SailBoatBgControl.New(arg_1_0.sceneContent, var_1_0)
	arg_1_0.itemControl = SailBoatItemControl.New(arg_1_0.sceneContent, var_1_0)
	arg_1_0.colliderControl = SailBoatColliderControl.New(arg_1_0.sceneContent, var_1_0)
	arg_1_0.enemyControl = SailBoatEnemyControl.New(arg_1_0.sceneContent, var_1_0)
	arg_1_0.bulletControl = SailBoatBulletsControl.New(arg_1_0.sceneContent, var_1_0)
	arg_1_0.effectControl = SailBoatEffectControl.New(arg_1_0.sceneContent, var_1_0)
	arg_1_0.bgRules = {}
	arg_1_0.bgTfs = {}
	arg_1_0.bgTfPool = {}

	for iter_1_0 = 1, #var_0_0.random_scene_imgs:
		local var_1_1 = var_0_0.random_scene_imgs[iter_1_0]

		table.insert(arg_1_0.bgRules, {
			time = 0,
			ruleData = var_1_1
		})

def var_0_0.start(arg_3_0):
	arg_3_0.showContainer(True)
	arg_3_0.charControl.start()
	arg_3_0.bgControl.start()
	arg_3_0.itemControl.start()
	arg_3_0.colliderControl.start()
	arg_3_0.enemyControl.start()
	arg_3_0.bulletControl.start()
	arg_3_0.effectControl.start()

	arg_3_0.sortIndex = 10
	arg_3_0.bgImgTpl = var_0_5.GetGameBgTf("bgs/bg_other")

	for iter_3_0 = #arg_3_0.bgTfs, 1, -1:
		local var_3_0 = table.remove(arg_3_0.bgTfs, iter_3_0)

		setActive(var_3_0, False)
		table.insert(arg_3_0.bgTfPool, var_3_0)

	for iter_3_1 = 1, #arg_3_0.bgRules:
		arg_3_0.bgRules[iter_3_1].time = 0

def var_0_0.step(arg_4_0, arg_4_1):
	local var_4_0
	local var_4_1
	local var_4_2
	local var_4_3
	local var_4_4
	local var_4_5
	local var_4_6
	local var_4_7 = os.clock()

	arg_4_0.charControl.step(arg_4_1)

	local var_4_8 = (os.clock() - var_4_7) * 1000
	local var_4_9 = os.clock()

	arg_4_0.bgControl.step(arg_4_1)

	local var_4_10 = (os.clock() - var_4_9) * 1000
	local var_4_11 = os.clock()

	arg_4_0.itemControl.step(arg_4_1)

	local var_4_12 = (os.clock() - var_4_11) * 1000
	local var_4_13 = os.clock()

	arg_4_0.colliderControl.step(arg_4_1)

	local var_4_14 = (os.clock() - var_4_13) * 1000
	local var_4_15 = os.clock()

	arg_4_0.enemyControl.step(arg_4_1)

	local var_4_16 = (os.clock() - var_4_15) * 1000
	local var_4_17 = os.clock()

	arg_4_0.bulletControl.step(arg_4_1)

	local var_4_18 = tostring((os.clock() - var_4_17) * 1000, 2)
	local var_4_19 = os.clock()

	arg_4_0.effectControl.step(arg_4_1)

	local var_4_20 = (os.clock() - var_4_19) * 1000
	local var_4_21 = os.clock()
	local var_4_22 = var_0_5.GetGameEnemys()
	local var_4_23 = var_0_5.GetGameChar()
	local var_4_24 = var_0_5.GetGameItems()

	if not arg_4_0.sortTfs or #arg_4_0.sortTfs != #var_4_22 + 1 + #var_4_24:
		arg_4_0.sortTfs = {}

		for iter_4_0 = 1, #var_4_22:
			table.insert(arg_4_0.sortTfs, var_4_22[iter_4_0].getTf())

		for iter_4_1 = 1, #var_4_24:
			table.insert(arg_4_0.sortTfs, var_4_24[iter_4_1].getTf())

		table.insert(arg_4_0.sortTfs, var_4_23.getTf())

	if arg_4_0.sortIndex and arg_4_0.sortIndex == 0:
		arg_4_0.sortItems(arg_4_0.sortTfs)

		arg_4_0.sortIndex = 10
	else
		arg_4_0.sortIndex = arg_4_0.sortIndex - 1

	for iter_4_2 = 1, #arg_4_0.bgRules:
		if arg_4_0.bgRules[iter_4_2].time <= 0:
			arg_4_0.bgRules[iter_4_2].time = math.random(30, 45)

			local var_4_25 = arg_4_0.bgRules[iter_4_2].ruleData.icon
			local var_4_26 = var_4_25[math.random(1, #var_4_25)]
			local var_4_27

			if #arg_4_0.bgTfPool > 0:
				var_4_27 = table.remove(arg_4_0.bgTfPool, 1)
			else
				var_4_27 = tf(instantiate(arg_4_0.bgImgTpl))

				SetParent(var_4_27, findTF(arg_4_0.sceneContent, arg_4_0.bgRules[iter_4_2].ruleData.content))

			setImageSprite(findTF(var_4_27, "img"), var_0_5.GetBgIcon(var_4_26), True)
			setActive(var_4_27, True)
			table.insert(arg_4_0.bgTfs, var_4_27)

			var_4_27.anchoredPosition = Vector2(math.random(-300, 300), 2000)
			var_4_27.localEulerAngles = Vector3(0, 0, math.random(1, 360))

		arg_4_0.bgRules[iter_4_2].time = arg_4_0.bgRules[iter_4_2].time - arg_4_1

	local var_4_28 = var_0_5.GetSceneSpeed()

	for iter_4_3 = #arg_4_0.bgTfs, 1, -1:
		local var_4_29 = arg_4_0.bgTfs[iter_4_3]

		if var_4_29.anchoredPosition.y < -2000:
			setActive(var_4_29, False)
			table.insert(arg_4_0.bgTfPool, var_4_29)
			table.remove(arg_4_0.bgTfs, iter_4_3)
		else
			local var_4_30 = var_4_29.anchoredPosition

			var_4_30.y = var_4_30.y + var_4_28.y
			var_4_29.anchoredPosition = var_4_30

def var_0_0.destroyEnemy(arg_5_0, arg_5_1):
	arg_5_0._event.emit(SailBoatGameView.ADD_SCORE, {
		num = arg_5_1.score
	})

	if arg_5_1.boom:
		arg_5_0.checkBoomDamage(arg_5_1)

def var_0_0.checkBoomDamage(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.boom
	local var_6_1 = arg_6_1.position
	local var_6_2 = arg_6_1.range
	local var_6_3 = var_0_5.GetGameChar()
	local var_6_4 = var_0_5.GetGameEnemys()
	local var_6_5 = var_6_3.getPosition()
	local var_6_6 = var_6_3.getConfig("range")

	if math.abs(var_6_1.x - var_6_5.x) < var_6_2.x + var_6_6.x / 2 and math.abs(var_6_1.y - var_6_5.y) < var_6_2.y + var_6_6.y / 2:
		var_6_3.damage({
			num = var_6_0,
			position = var_6_1
		})

	for iter_6_0 = 1, #var_6_4:
		local var_6_7 = var_6_4[iter_6_0]
		local var_6_8 = var_6_7.getPosition()
		local var_6_9 = var_6_7.getConfig("range")

		if math.abs(var_6_1.x - var_6_8.x) < var_6_2.x + var_6_8.x / 2 and math.abs(var_6_1.y - var_6_8.y) < var_6_2.y + var_6_8.y / 2 and var_6_7.damage({
			num = var_6_0,
			position = var_6_1
		}):
			arg_6_0.destroyEnemy(var_6_7.getDestroyData())

def var_0_0.sortItems(arg_7_0, arg_7_1):
	table.sort(arg_7_1, function(arg_8_0, arg_8_1)
		local var_8_0 = arg_8_0.anchoredPosition
		local var_8_1 = arg_8_1.anchoredPosition

		if var_8_0.y > var_8_1.y:
			return False
		elif var_8_0.y < var_8_1.y:
			return True

		if var_8_0.x > var_8_1.x:
			return False
		elif var_8_0.x < var_8_1.x:
			return True

		return False)

	for iter_7_0 = 1, #arg_7_1:
		arg_7_1[iter_7_0].SetSiblingIndex(0)

def var_0_0.useSkill(arg_9_0):
	arg_9_0.charControl.useSkill()

def var_0_0.clear(arg_10_0):
	return

def var_0_0.stop(arg_11_0):
	return

def var_0_0.resume(arg_12_0):
	return

def var_0_0.onSceneEventCall(arg_13_0, arg_13_1, arg_13_2):
	arg_13_0.charControl.onEventCall(arg_13_1, arg_13_2)
	arg_13_0.bulletControl.onEventCall(arg_13_1, arg_13_2)
	arg_13_0.effectControl.onEventCall(arg_13_1, arg_13_2)

def var_0_0.dispose(arg_14_0):
	arg_14_0.charControl.dispose()
	arg_14_0.bgControl.dispose()
	arg_14_0.itemControl.dispose()
	arg_14_0.enemyControl.dispose()

def var_0_0.showContainer(arg_15_0, arg_15_1):
	setActive(arg_15_0.sceneMask, arg_15_1)

def var_0_0.press(arg_16_0, arg_16_1, arg_16_2):
	if arg_16_1 == KeyCode.J and arg_16_2:
		arg_16_0.charControl.ableFire()

def var_0_0.joystickActive(arg_17_0, arg_17_1):
	return

return var_0_0
