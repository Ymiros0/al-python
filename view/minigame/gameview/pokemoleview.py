local var_0_0 = class("PokeMoleView", import("..BaseMiniGameView"))
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = {
	1000,
	230
}
local var_0_5 = {
	300,
	100
}
local var_0_6 = "backyard"
local var_0_7 = "event./ui/jida"
local var_0_8 = "event./ui/quanji"
local var_0_9 = "event./ui/baozhaxiaoshi"
local var_0_10 = ""
local var_0_11 = ""
local var_0_12 = "event./ui/ddldaoshu2"
local var_0_13 = 0.5
local var_0_14 = 90
local var_0_15 = {
	{
		speed = 60,
		type = 1,
		enable_time = 1,
		life = 1,
		score = 100,
		damage_time = 1
	},
	{
		speed = 65,
		type = 2,
		enable_time = 1,
		life = 1,
		score = 150,
		damage_time = 1
	},
	{
		speed = 50,
		type = 3,
		enable_time = 2,
		life = 2,
		score = 200,
		damage_time = 1
	},
	{
		speed = 55,
		type = 4,
		enable_time = 1,
		life = 1,
		score = 150,
		damage_time = 1
	}
}
local var_0_16 = {
	level_up_time = {
		0,
		20,
		40,
		60,
		80
	},
	enemy_apear_time = {
		2.5,
		2,
		1.5,
		1.5,
		1
	},
	enemy_max = {
		5,
		6,
		7,
		8,
		8
	},
	enemy_amounts = {
		{
			70,
			30
		},
		{
			70,
			30
		},
		{
			70,
			40
		},
		{
			70,
			40,
			20
		},
		{
			70,
			50,
			20
		}
	}
}
local var_0_17 = 3
local var_0_18 = {
	1,
	2,
	3
}
local var_0_19 = 10
local var_0_20 = 10

local function var_0_21(arg_1_0, arg_1_1)
	local var_1_0 = {
		def ctor:(arg_2_0)
			arg_2_0._tf = arg_1_0
			arg_2_0._callback = arg_1_1
			arg_2_0._animator = GetComponent(arg_2_0._tf, typeof(Animator))
			arg_2_0._attakeCount = 0
			arg_2_0._attakeCd = 0
			arg_2_0._specialTime = 0
			arg_2_0._specialCount = 0
			arg_2_0.atkCollider = GetComponent(findTF(arg_2_0._tf, "atkCollider"), typeof(BoxCollider2D))
			arg_2_0.specialCollider = GetComponent(findTF(arg_2_0._tf, "specialCollider"), typeof(BoxCollider2D))

			local var_2_0 = GetComponent(arg_2_0._tf, typeof(DftAniEvent))

			var_2_0.SetStartEvent(function()
				return)
			var_2_0.SetTriggerEvent(function()
				if arg_2_0._callback:
					local var_4_0 = arg_2_0.getColliderData()

					arg_2_0._callback(var_4_0)

					if arg_2_0.getSpecialState():
						pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_8))
			var_2_0.SetEndEvent(function()
				return),
		def getColliderData:(arg_6_0)
			local var_6_0

			if arg_6_0.getSpecialState():
				var_6_0 = arg_6_0.specialCollider
			else
				var_6_0 = arg_6_0.atkCollider

			local var_6_1 = var_6_0.bounds.max.x - var_6_0.bounds.min.x
			local var_6_2 = var_6_0.bounds.max.y - var_6_0.bounds.min.y

			return {
				pos = var_6_0.bounds.min,
				boundsLength = {
					width = var_6_1,
					height = var_6_2
				},
				damage = arg_6_0.getDamage()
			},
		def atk:(arg_7_0)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_7)
			arg_7_0._animator.SetTrigger("atk")

			arg_7_0._attakeCd = var_0_13,
		def specialAtk:(arg_8_0)
			arg_8_0._animator.SetTrigger("special")

			arg_8_0._attakeCd = var_0_13,
		def getDamage:(arg_9_0)
			if arg_9_0._specialTime > 0:
				return 3

			return 1,
		def reset:(arg_10_0)
			arg_10_0._animator.SetTrigger("reset"),
		def setActive:(arg_11_0, arg_11_1)
			SetActive(arg_11_0._tf, arg_11_1),
		def setParent:(arg_12_0, arg_12_1, arg_12_2)
			SetParent(arg_12_0._tf, arg_12_1)
			arg_12_0.setActive(arg_12_2),
		def attakeAble:(arg_13_0)
			return arg_13_0._attakeCd == 0,
		def moveTo:(arg_14_0, arg_14_1)
			arg_14_1.y = arg_14_1.y + 100
			arg_14_0._tf.anchoredPosition = arg_14_1,
		def attakeCount:(arg_15_0, arg_15_1)
			arg_15_0._attakeCount = arg_15_0._attakeCount + arg_15_1 * 4

			if arg_15_0._attakeCount > 8:
				arg_15_0._attakeCount = 8

			if arg_15_0._attakeCount > 0:
				arg_15_0._animator.speed = 0,
		def addSpecialCount:(arg_16_0, arg_16_1)
			if arg_16_0._specialTime == 0:
				arg_16_0._specialCount = arg_16_0._specialCount + arg_16_1

				if arg_16_0._specialCount >= var_0_20:
					arg_16_0._specialCount = var_0_20,
		def useSpecial:(arg_17_0)
			if arg_17_0._specialTime and arg_17_0._specialCount >= var_0_20:
				arg_17_0._specialCount = 0
				arg_17_0._specialTime = var_0_19

				return True

			return False,
		def SetSiblingIndex:(arg_18_0, arg_18_1)
			arg_18_0._tf.SetSiblingIndex(arg_18_1),
		def getSpecialState:(arg_19_0)
			return arg_19_0._specialTime > 0,
		def step:(arg_20_0)
			if arg_20_0._attakeCount > 0:
				arg_20_0._attakeCount = arg_20_0._attakeCount - 1

				if arg_20_0._attakeCount == 0:
					arg_20_0._animator.speed = 1

			if arg_20_0._attakeCd > 0:
				arg_20_0._attakeCd = arg_20_0._attakeCd - Time.deltaTime
				arg_20_0._attakeCd = arg_20_0._attakeCd < 0 and 0 or arg_20_0._attakeCd

			if arg_20_0._specialTime > 0:
				arg_20_0._specialTime = arg_20_0._specialTime - Time.deltaTime
				arg_20_0._specialTime = arg_20_0._specialTime < 0 and 0 or arg_20_0._specialTime,
		def inSpecial:(arg_21_0)
			return arg_21_0._specialTime > 0,
		def getSpecialData:(arg_22_0)
			return arg_22_0._specialTime, arg_22_0._specialCount,
		def clear:(arg_23_0)
			arg_23_0._specialTime = 0
			arg_23_0._specialCount = 0

			arg_23_0.reset(),
		def useAtk:(arg_24_0)
			if arg_24_0.inSpecial():
				arg_24_0.specialAtk()
			else
				arg_24_0.atk()
	}

	var_1_0.ctor()

	return var_1_0

local function var_0_22(arg_25_0, arg_25_1)
	local var_25_0 = {
		def ctor:(arg_26_0)
			arg_26_0.playerTpl = arg_25_0
			arg_26_0.sceneTf = arg_25_1
			arg_26_0._playerPos = findTF(arg_26_0.sceneTf, "playerPos")
			arg_26_0.uiCam = GameObject.Find("UICamera").GetComponent("Camera")
			arg_26_0.dragDelegate = GetOrAddComponent(findTF(arg_26_0.sceneTf, "clickBounds"), "EventTriggerListener")
			arg_26_0.dragDelegate.enabled = True

			arg_26_0.dragDelegate.AddPointDownFunc(function(arg_27_0, arg_27_1)
				if arg_26_0.player and arg_26_0.player.attakeAble():
					local var_27_0 = arg_26_0.uiCam.ScreenToWorldPoint(arg_27_1.pressPosition)
					local var_27_1 = arg_26_0._playerPos.InverseTransformPoint(var_27_0)

					arg_26_0.player.moveTo(var_27_1)
					arg_26_0.player.reset()
					arg_26_0.player.useAtk()),
		def createPlayer:(arg_28_0)
			if arg_28_0.player == None:
				arg_28_0.player = var_0_21(tf(Instantiate(arg_28_0.playerTpl)), function(arg_29_0)
					arg_28_0.playerActHand(arg_29_0))

				arg_28_0.player.setParent(arg_28_0._playerPos, True),
		def playerActHand:(arg_30_0, arg_30_1)
			if arg_30_0.playerHandle:
				arg_30_0.playerHandle(arg_30_1),
		def setPlayerHandle:(arg_31_0, arg_31_1)
			arg_31_0.playerHandle = arg_31_1,
		def step:(arg_32_0)
			if arg_32_0.player:
				arg_32_0.player.step(),
		def getSpecialData:(arg_33_0)
			if arg_33_0.player:
				return arg_33_0.player.getSpecialData()

			return None, None,
		def useSpecial:(arg_34_0)
			if arg_34_0.player:
				return arg_34_0.player.useSpecial(),
		def attakeCount:(arg_35_0, arg_35_1)
			if arg_35_0.player:
				arg_35_0.player.attakeCount(arg_35_1),
		def addSpecialCount:(arg_36_0, arg_36_1)
			if arg_36_0.player:
				arg_36_0.player.addSpecialCount(arg_36_1),
		def clear:(arg_37_0)
			if arg_37_0.player:
				arg_37_0.player.clear()
	}

	var_25_0.ctor()

	return var_25_0

local function var_0_23(arg_38_0, arg_38_1)
	local var_38_0 = {
		def ctor:(arg_39_0)
			arg_39_0._tf = arg_38_0
			arg_39_0._data = arg_38_1
			arg_39_0._life = 0
			arg_39_0._enable = False
			arg_39_0._attakeAble = False
			arg_39_0._animator = GetComponent(arg_39_0._tf, typeof(Animator))
			arg_39_0._boxCollider = GetComponent(arg_39_0._tf, "BoxCollider2D")

			local var_39_0 = GetComponent(arg_39_0._tf, typeof(DftAniEvent))

			var_39_0.SetStartEvent(function()
				if arg_39_0._callback:
					arg_39_0._callback(var_0_3))
			var_39_0.SetTriggerEvent(function()
				if arg_39_0._callback:
					arg_39_0._callback(var_0_2))
			var_39_0.SetEndEvent(function()
				arg_39_0._enable = False

				if arg_39_0._callback:
					arg_39_0._callback(var_0_1)),
		def setHandle:(arg_43_0, arg_43_1)
			arg_43_0._callback = arg_43_1,
		def getSpeed:(arg_44_0)
			return arg_44_0._data.speed,
		def step:(arg_45_0)
			if arg_45_0._enableTime > 0:
				arg_45_0._enableTime = arg_45_0._enableTime - Time.deltaTime

				if arg_45_0._enableTime < 0:
					arg_45_0._enable = True
					arg_45_0._enableTime = 0,
		def apear:(arg_46_0)
			arg_46_0._animator.SetTrigger("pop")

			arg_46_0._enableTime = math.random() * arg_46_0._data.enable_time + 0.5
			arg_46_0._life = arg_46_0._data.life
			arg_46_0._attakeAble = True,
		def stop:(arg_47_0)
			arg_47_0._animator.SetBool("stop", True),
		def damage:(arg_48_0, arg_48_1)
			arg_48_0._life = arg_48_0._life - arg_48_1

			if arg_48_0._life <= 0:
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_9)
				arg_48_0.dead()
			else
				arg_48_0._animator.SetTrigger("damage")

				arg_48_0._enable = False
				arg_48_0._enableTime = arg_48_0._data.damage_time,
		def dead:(arg_49_0)
			arg_49_0._animator.SetTrigger("dead")

			arg_49_0._enable = False
			arg_49_0._enableTime = 0
			arg_49_0._attakeAble = False,
		def steal:(arg_50_0)
			arg_50_0._animator.SetTrigger("steal")

			arg_50_0._enable = False
			arg_50_0._attakeAble = False,
		def move:(arg_51_0, arg_51_1, arg_51_2)
			local var_51_0 = arg_51_0._tf.anchoredPosition

			var_51_0.x = var_51_0.x + arg_51_1
			var_51_0.y = var_51_0.y + arg_51_2
			arg_51_0._tf.anchoredPosition = var_51_0

			local var_51_1 = arg_51_0._tf.localScale

			var_51_1.x = Mathf.Abs(arg_51_0._tf.localScale.x) * -1 * Mathf.Sign(arg_51_1)
			arg_51_0._tf.localScale = var_51_1,
		def moveTo:(arg_52_0, arg_52_1)
			arg_52_0._tf.anchoredPosition = arg_52_1

			local var_52_0 = arg_52_0._tf.localScale

			var_52_0.x = Mathf.Abs(arg_52_0._tf.localScale.x) * Mathf.Sign(arg_52_0._tf.localPosition.x)
			arg_52_0._tf.localScale = var_52_0,
		def setParent:(arg_53_0, arg_53_1, arg_53_2)
			SetParent(arg_53_0._tf, arg_53_1)
			arg_53_0.setActive(arg_53_2),
		def setActive:(arg_54_0, arg_54_1)
			SetActive(arg_54_0._tf, arg_54_1),
		def SetSiblingIndex:(arg_55_0, arg_55_1)
			arg_55_0._tf.SetSiblingIndex(arg_55_1),
		def getPosition:(arg_56_0)
			return arg_56_0._tf.anchoredPosition,
		def getType:(arg_57_0)
			return arg_57_0._data.type,
		def getMoveAble:(arg_58_0)
			return isActive(arg_58_0._tf) and arg_58_0._enable,
		def getAttakeAble:(arg_59_0)
			return isActive(arg_59_0._tf) and arg_59_0._attakeAble,
		def getBounds:(arg_60_0)
			return arg_60_0._boxCollider.bounds,
		def getLife:(arg_61_0)
			return arg_61_0._life,
		def getScore:(arg_62_0)
			return arg_62_0._data.score,
		def getBoundLength:(arg_63_0)
			if arg_63_0.boundsData == None:
				local var_63_0 = arg_63_0._boxCollider.bounds.max.x - arg_63_0._boxCollider.bounds.min.x
				local var_63_1 = arg_63_0._boxCollider.bounds.max.y - arg_63_0._boxCollider.bounds.min.y

				arg_63_0.boundsData = {
					width = var_63_0,
					height = var_63_1
				}

			return arg_63_0.boundsData
	}

	var_38_0.ctor()

	return var_38_0

local function var_0_24(arg_64_0, arg_64_1, arg_64_2, arg_64_3)
	local var_64_0 = {
		def ctor:(arg_65_0)
			arg_65_0.enemysTpl = arg_64_0
			arg_65_0.sceneTf = arg_64_1
			arg_65_0.enemyPos = findTF(arg_65_0.sceneTf, "enemyPos")
			arg_65_0.createPos = findTF(arg_65_0.sceneTf, "createPos")
			arg_65_0.countsWeight = {}

			for iter_65_0 = 1, #var_0_16.enemy_amounts:
				local var_65_0 = {}
				local var_65_1 = 0
				local var_65_2 = var_0_16.enemy_amounts[iter_65_0]

				for iter_65_1 = 1, #var_65_2:
					var_65_1 = var_65_1 + var_65_2[iter_65_1]

					table.insert(var_65_0, var_65_1)

				table.insert(arg_65_0.countsWeight, var_65_0)

			arg_65_0.callback = arg_64_2
			arg_65_0.callback2 = arg_64_3
			arg_65_0.enemys = {}
			arg_65_0.enemysPool = {}
			arg_65_0.apearTime = 0
			arg_65_0.stepTime = 0
			arg_65_0.level = 1
			arg_65_0.cakeLife = var_0_17
			arg_65_0.cakeTf = findTF(arg_65_0.sceneTf, "enemyPos/cake")
			arg_65_0.cakeAniamtor = GetComponent(findTF(arg_65_0.cakeTf, "image"), typeof(Animator))

			arg_65_0.cakeAniamtor.SetInteger("life", arg_65_0.getCakeLifeIndex())

			arg_65_0.cakeBox = GetComponent(arg_65_0.cakeTf, "BoxCollider2D")
			arg_65_0.cakeBoundsLength = {
				width = arg_65_0.cakeBox.bounds.max.x - arg_65_0.cakeBox.bounds.min.x,
				height = arg_65_0.cakeBox.bounds.max.y - arg_65_0.cakeBox.bounds.min.y
			}
			arg_65_0.gameScore = 0
			arg_65_0.createBounds = {}

			for iter_65_2 = 0, arg_65_0.createPos.childCount - 1:
				table.insert(arg_65_0.createBounds, arg_65_0.createPos.GetChild(iter_65_2)),
		def step:(arg_66_0)
			for iter_66_0 = #var_0_16.level_up_time, 1, -1:
				if iter_66_0 > arg_66_0.level and arg_66_0.stepTime > var_0_16.level_up_time[iter_66_0] and arg_66_0.level != iter_66_0:
					arg_66_0.level = iter_66_0

					print("level up ." .. arg_66_0.level)

					break

			if arg_66_0.apearTime == 0:
				local var_66_0 = arg_66_0.getCreateCounts()

				for iter_66_1 = 1, var_66_0:
					if #arg_66_0.enemys < var_0_16.enemy_max[arg_66_0.level]:
						local var_66_1 = var_0_15[math.random(1, #var_0_15)]
						local var_66_2 = arg_66_0.getEnemyFromPool(var_66_1.type) or arg_66_0.createEnemy(var_66_1)

						table.insert(arg_66_0.enemys, var_66_2)
						var_66_2.setActive(True)
						var_66_2.moveTo(arg_66_0.getRandApearPosition())
						var_66_2.apear()

				arg_66_0.apearTime = var_0_16.enemy_apear_time[arg_66_0.level]

			table.sort(arg_66_0.enemys, function(arg_67_0, arg_67_1)
				return arg_67_0.getPosition().y > arg_67_1.getPosition().y)

			local var_66_3 = 0

			for iter_66_2 = #arg_66_0.enemys, 1, -1:
				local var_66_4 = arg_66_0.enemys[iter_66_2]

				if arg_66_0.cakeTf.localPosition.y <= var_66_4.getPosition().y:
					var_66_3 = var_66_3 + 1

				var_66_4.SetSiblingIndex(iter_66_2)
				var_66_4.step()

				if var_66_4.getMoveAble():
					local var_66_5 = var_66_4.getPosition()

					if arg_66_0.checkEnemySteal(var_66_4):
						var_66_4.steal()
					else
						local var_66_6 = Mathf.Atan2(Mathf.Abs(var_66_5.y), Mathf.Abs(var_66_5.x))
						local var_66_7 = var_66_4.getSpeed() * Mathf.Cos(var_66_6) * -Mathf.Sign(var_66_5.x)
						local var_66_8 = var_66_4.getSpeed() * Mathf.Sin(var_66_6) * -Mathf.Sign(var_66_5.y)

						var_66_4.move(var_66_7 * Time.deltaTime, var_66_8 * Time.deltaTime)

			arg_66_0.cakeTf.SetSiblingIndex(var_66_3)

			arg_66_0.apearTime = arg_66_0.apearTime - Time.deltaTime

			if arg_66_0.apearTime < 0:
				arg_66_0.apearTime = 0

			arg_66_0.stepTime = arg_66_0.stepTime + Time.deltaTime

			arg_66_0.cakeAniamtor.SetInteger("life", arg_66_0.getCakeLifeIndex()),
		def getCreateCounts:(arg_68_0)
			local var_68_0 = arg_68_0.countsWeight[arg_68_0.level]
			local var_68_1 = math.random(1, var_68_0[#var_68_0])

			for iter_68_0 = 1, #var_68_0:
				if var_68_1 <= var_68_0[iter_68_0]:
					return iter_68_0

			return 1,
		def checkEnemySteal:(arg_69_0, arg_69_1)
			local var_69_0 = arg_69_1.getBounds().min
			local var_69_1 = arg_69_1.getBoundLength()
			local var_69_2 = arg_69_0.cakeBox.bounds.min
			local var_69_3 = arg_69_0.cakeBoundsLength

			return arg_69_0.checkRectCollider(var_69_0, var_69_2, var_69_1, var_69_3),
		def checkRectCollider:(arg_70_0, arg_70_1, arg_70_2, arg_70_3, arg_70_4)
			local var_70_0 = arg_70_1.x
			local var_70_1 = arg_70_1.y
			local var_70_2 = arg_70_3.width
			local var_70_3 = arg_70_3.height
			local var_70_4 = arg_70_2.x
			local var_70_5 = arg_70_2.y
			local var_70_6 = arg_70_4.width
			local var_70_7 = arg_70_4.height

			if var_70_4 <= var_70_0 and var_70_0 >= var_70_4 + var_70_6:
				return False
			elif var_70_0 <= var_70_4 and var_70_4 >= var_70_0 + var_70_2:
				return False
			elif var_70_5 <= var_70_1 and var_70_1 >= var_70_5 + var_70_7:
				return False
			elif var_70_1 <= var_70_5 and var_70_5 >= var_70_1 + var_70_3:
				return False
			else
				return True,
		def createEnemy:(arg_71_0, arg_71_1)
			local var_71_0 = tf(Instantiate(arg_71_0.enemysTpl[arg_71_1.type]))
			local var_71_1 = var_0_23(var_71_0, arg_71_1)

			var_71_1.setHandle(function(arg_72_0)
				arg_71_0.enemyEventHandle(arg_72_0, var_71_1))
			var_71_1.setParent(arg_71_0.enemyPos, True)

			return var_71_1,
		def getEnemyFromPool:(arg_73_0, arg_73_1)
			for iter_73_0 = 1, #arg_73_0.enemysPool:
				local var_73_0 = arg_73_0.enemysPool[iter_73_0]

				if var_73_0.getType() == arg_73_1:
					table.remove(arg_73_0.enemysPool, iter_73_0)

					return var_73_0

			return None,
		def removeEnemy:(arg_74_0, arg_74_1)
			for iter_74_0 = #arg_74_0.enemys, 1, -1:
				if arg_74_0.enemys[iter_74_0] == arg_74_1:
					table.remove(arg_74_0.enemys, iter_74_0)

			arg_74_1.setActive(False)
			table.insert(arg_74_0.enemysPool, arg_74_1),
		def getRandApearPosition:(arg_75_0)
			local var_75_0 = math.random(1, #arg_75_0.createBounds)
			local var_75_1 = arg_75_0.createBounds[var_75_0]
			local var_75_2 = math.random() * (var_75_1.sizeDelta.x / 2) * (math.random() < 0.5 and 1 or -1)
			local var_75_3 = math.random() * (var_75_1.sizeDelta.y / 2) * (math.random() < 0.5 and 1 or -1)
			local var_75_4 = var_75_1.TransformPoint(var_75_2, var_75_3, 0)

			return (arg_75_0.enemyPos.InverseTransformPoint(var_75_4.x, var_75_4.y, var_75_4.z)),
		def enemyEventHandle:(arg_76_0, arg_76_1, arg_76_2)
			if arg_76_1 == var_0_2:
				arg_76_0.cakeLife = arg_76_0.cakeLife - 1

				if arg_76_0.callback2:
					arg_76_0.callback2()

				if arg_76_0.cakeLife <= 0 and arg_76_0.callback:
					arg_76_0.callback()

				arg_76_0.cakeAniamtor.SetInteger("life", arg_76_0.getCakeLifeIndex())
			elif arg_76_1 == var_0_1:
				arg_76_0.gameScore = arg_76_0.gameScore + arg_76_2.getScore()

				arg_76_0.removeEnemy(arg_76_2)
			else
				arg_76_0.removeEnemy(arg_76_2),
		def playerActAttake:(arg_77_0, arg_77_1)
			local var_77_0 = arg_77_1.pos
			local var_77_1 = arg_77_1.boundsLength
			local var_77_2 = arg_77_1.damage
			local var_77_3 = 0
			local var_77_4 = 0

			for iter_77_0 = 1, #arg_77_0.enemys:
				local var_77_5 = arg_77_0.enemys[iter_77_0]

				if var_77_5.getAttakeAble():
					local var_77_6 = var_77_5.getBounds().min
					local var_77_7 = var_77_5.getBoundLength()

					if arg_77_0.checkRectCollider(var_77_6, var_77_0, var_77_7, var_77_1):
						var_77_5.damage(var_77_2)

						var_77_3 = var_77_3 + 1

						if var_77_5.getLife() == 0:
							var_77_4 = var_77_4 + 1

			return var_77_3, var_77_4,
		def clear:(arg_78_0)
			arg_78_0.stepTime = 0

			for iter_78_0 = #arg_78_0.enemys, 1, -1:
				local var_78_0 = table.remove(arg_78_0.enemys, iter_78_0)

				var_78_0.setActive(False)
				table.insert(arg_78_0.enemysPool, var_78_0)

			arg_78_0.cakeLife = var_0_17
			arg_78_0.gameScore = 0
			arg_78_0.level = 1,
		def getCakeLife:(arg_79_0)
			return arg_79_0.cakeLife,
		def getCakeLifeIndex:(arg_80_0)
			for iter_80_0 = #var_0_18, 1, -1:
				if arg_80_0.cakeLife >= var_0_18[iter_80_0]:
					return iter_80_0

			return 0,
		def getScore:(arg_81_0)
			return arg_81_0.gameScore
	}

	var_64_0.ctor()

	return var_64_0

local function var_0_25(arg_82_0, arg_82_1, arg_82_2)
	local var_82_0 = {
		def ctor:(arg_83_0)
			arg_83_0.playerController = arg_82_0
			arg_83_0.enemyController = arg_82_1
			arg_83_0.callback = arg_82_2

			arg_83_0.playerController.setPlayerHandle(function(arg_84_0)
				local var_84_0, var_84_1 = arg_83_0.enemyController.playerActAttake(arg_84_0)

				if var_84_0 > 0:
					arg_83_0.playerController.attakeCount(var_84_0)

				if var_84_1 > 0:
					arg_83_0.playerController.addSpecialCount(var_84_1)

					if arg_83_0.callback:
						arg_83_0.callback())
	}

	var_82_0.ctor()

	return var_82_0

local var_0_26 = "role type loop"
local var_0_27 = "role type normal"

local function var_0_28(arg_85_0, arg_85_1)
	local var_85_0 = {
		def ctor:(arg_86_0)
			arg_86_0.playerController = arg_85_1
			arg_86_0.roleTfs = arg_85_0
			arg_86_0.roleDatas = {}

			for iter_86_0 = 1, #arg_86_0.roleTfs:
				local var_86_0 = {
					animator = GetComponent(arg_86_0.roleTfs[iter_86_0], typeof(Animator))
				}

				if iter_86_0 == 2 or iter_86_0 == 3:
					var_86_0.type = var_0_26
					var_86_0.loop_time = {
						3,
						3
					}
					var_86_0.time = 0
				else
					var_86_0.type = var_0_27

				table.insert(arg_86_0.roleDatas, var_86_0),
		def step:(arg_87_0)
			local var_87_0 = arg_87_0.playerController.getSpecialData()

			for iter_87_0 = 1, #arg_87_0.roleDatas:
				local var_87_1 = arg_87_0.roleDatas[iter_87_0]

				if var_87_1.type == var_0_26:
					if var_87_1.time == 0:
						var_87_1.animator.SetTrigger("loop")

						var_87_1.time = math.random() * var_87_1.loop_time[1] + var_87_1.loop_time[2]
					else
						var_87_1.time = var_87_1.time - Time.deltaTime

						if var_87_1.time < 0:
							var_87_1.time = 0

				if var_87_1.special and var_87_0 == 0:
					var_87_1.animator.SetTrigger("reset")

					var_87_1.special = False,
		def special:(arg_88_0)
			for iter_88_0 = 1, #arg_88_0.roleDatas:
				local var_88_0 = arg_88_0.roleDatas[iter_88_0]

				var_88_0.animator.SetTrigger("special")

				var_88_0.special = True,
		def fail:(arg_89_0)
			for iter_89_0 = 1, #arg_89_0.roleDatas:
				arg_89_0.roleDatas[iter_89_0].animator.SetTrigger("fail"),
		def reset:(arg_90_0)
			for iter_90_0 = 1, #arg_90_0.roleDatas:
				arg_90_0.roleDatas[iter_90_0].animator.SetTrigger("reset")
	}

	var_85_0.ctor()

	return var_85_0

def var_0_0.getUIName(arg_91_0):
	return "PokeMoleGameUI"

def var_0_0.getBGM(arg_92_0):
	return var_0_6

def var_0_0.didEnter(arg_93_0):
	arg_93_0.initData()
	arg_93_0.initUI()

def var_0_0.initData(arg_94_0):
	arg_94_0.settlementFlag = False
	arg_94_0.gameStartFlag = False

	local var_94_0 = Application.targetFrameRate or 60

	arg_94_0.timer = Timer.New(function()
		arg_94_0.onTimer(), 1 / var_94_0, -1, True)

def var_0_0.initUI(arg_96_0):
	arg_96_0.clickMask = findTF(arg_96_0._tf, "clickMask")
	arg_96_0.countUI = findTF(arg_96_0._tf, "pop/CountUI")
	arg_96_0.countAnimator = GetComponent(findTF(arg_96_0.countUI, "count"), typeof(Animator))
	arg_96_0.countDft = GetComponent(findTF(arg_96_0.countUI, "count"), typeof(DftAniEvent))

	arg_96_0.countDft.SetTriggerEvent(function()
		return)
	arg_96_0.countDft.SetEndEvent(function()
		setActive(arg_96_0.countUI, False)
		arg_96_0.gameStart())

	arg_96_0.leaveUI = findTF(arg_96_0._tf, "pop/LeaveUI")

	onButton(arg_96_0, findTF(arg_96_0.leaveUI, "ad/btnOk"), function()
		arg_96_0.resumeGame()
		arg_96_0.onGameOver(), SFX_CANCEL)
	onButton(arg_96_0, findTF(arg_96_0.leaveUI, "ad/btnCancel"), function()
		arg_96_0.resumeGame(), SFX_CANCEL)

	arg_96_0.pauseUI = findTF(arg_96_0._tf, "pop/pauseUI")

	onButton(arg_96_0, findTF(arg_96_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_96_0.pauseUI, False)
		arg_96_0.resumeGame(), SFX_CANCEL)

	arg_96_0.settlementUI = findTF(arg_96_0._tf, "pop/SettleMentUI")

	onButton(arg_96_0, findTF(arg_96_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_96_0.settlementUI, False)
		arg_96_0.openMenuUI(), SFX_CANCEL)

	arg_96_0.menuUI = findTF(arg_96_0._tf, "pop/menuUI")

	onButton(arg_96_0, findTF(arg_96_0.menuUI, "btnBack"), function()
		arg_96_0.closeView(), SFX_CANCEL)
	onButton(arg_96_0, findTF(arg_96_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.securitycake_help.tip
		}), SFX_CANCEL)
	onButton(arg_96_0, findTF(arg_96_0.menuUI, "btnStart"), function()
		setActive(arg_96_0.menuUI, False)
		arg_96_0.readyStart(), SFX_CANCEL)

	arg_96_0.gameUI = findTF(arg_96_0._tf, "ui/gameUI")
	arg_96_0.textTime = findTF(arg_96_0.gameUI, "time")
	arg_96_0.textScore = findTF(arg_96_0.gameUI, "score")
	arg_96_0.hearts = {}

	local var_96_0 = 3

	for iter_96_0 = 1, var_96_0:
		local var_96_1 = findTF(arg_96_0.gameUI, "heart" .. iter_96_0 .. "/img")

		table.insert(arg_96_0.hearts, var_96_1)

	onButton(arg_96_0, findTF(arg_96_0.gameUI, "btnStop"), function()
		arg_96_0.stopGame()
		setActive(arg_96_0.pauseUI, True))
	onButton(arg_96_0, findTF(arg_96_0.gameUI, "btnLeave"), function()
		arg_96_0.stopGame()
		setActive(arg_96_0.leaveUI, True))

	arg_96_0.specialSlider = GetComponent(findTF(arg_96_0.gameUI, "btnSpecial/Slider"), typeof(Slider))
	arg_96_0.touchSlider = findTF(arg_96_0.specialSlider, "touch")
	arg_96_0.specialEffect = findTF(arg_96_0.gameUI, "btnSpecial/baoweidangao_extiao")
	arg_96_0.arrowTf = findTF(arg_96_0.gameUI, "btnSpecial/arrow")

	onButton(arg_96_0, findTF(arg_96_0.gameUI, "btnSpecial"), function()
		if arg_96_0.playerController and arg_96_0.playerController.useSpecial():
			arg_96_0.bgRoleController.special())

	arg_96_0.sceneTf = findTF(arg_96_0._tf, "scene")
	arg_96_0.playerTpl = findTF(arg_96_0._tf, "playerTpl")
	arg_96_0.playerController = var_0_22(arg_96_0.playerTpl, arg_96_0.sceneTf)
	arg_96_0.enemyTpls = {}

	for iter_96_1 = 1, 4:
		table.insert(arg_96_0.enemyTpls, findTF(arg_96_0._tf, "enemy" .. iter_96_1 .. "Tpl"))

	arg_96_0.enemyController = var_0_24(arg_96_0.enemyTpls, arg_96_0.sceneTf, function()
		arg_96_0.bgRoleController.fail()
		arg_96_0.onGameOver(), function()
		arg_96_0.gameUIUpdate())
	arg_96_0.attakeController = var_0_25(arg_96_0.playerController, arg_96_0.enemyController, function()
		arg_96_0.gameUIUpdate())

	local var_96_2 = {}
	local var_96_3 = 4

	for iter_96_2 = 1, var_96_3:
		table.insert(var_96_2, findTF(arg_96_0._tf, "bg_background/role/role" .. iter_96_2))

	arg_96_0.bgRoleController = var_0_28(var_96_2, arg_96_0.playerController)

	arg_96_0.updateMenuUI()
	arg_96_0.openMenuUI()

	if not arg_96_0.handle:
		arg_96_0.handle = UpdateBeat.CreateListener(arg_96_0.Update, arg_96_0)

	UpdateBeat.AddListener(arg_96_0.handle)

def var_0_0.updateMenuUI(arg_112_0):
	local var_112_0 = arg_112_0.getGameUsedTimes()
	local var_112_1 = arg_112_0.getGameTimes()

	setActive(findTF(arg_112_0.menuUI, "btnStart/tip"), var_112_1 > 0)
	arg_112_0.CheckGet()

def var_0_0.openMenuUI(arg_113_0):
	setActive(findTF(arg_113_0._tf, "scene_front"), False)
	setActive(findTF(arg_113_0._tf, "scene_background"), False)
	setActive(findTF(arg_113_0._tf, "scene"), False)
	setActive(arg_113_0.gameUI, False)
	setActive(arg_113_0.menuUI, True)
	arg_113_0.updateMenuUI()

def var_0_0.showSettlement(arg_114_0):
	setActive(arg_114_0.settlementUI, True)
	GetComponent(findTF(arg_114_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_114_0 = arg_114_0.GetMGData().GetRuntimeData("elements")
	local var_114_1 = arg_114_0.enemyController.getScore()
	local var_114_2 = var_114_0 and #var_114_0 > 0 and var_114_0[1] or 0

	if var_114_2 <= var_114_1:
		var_114_2 = var_114_1

		arg_114_0.StoreDataToServer({
			var_114_2
		})

	local var_114_3 = findTF(arg_114_0.settlementUI, "ad/highText")
	local var_114_4 = findTF(arg_114_0.settlementUI, "ad/currentText")

	setText(var_114_3, var_114_2)
	setText(var_114_4, var_114_1)

	if arg_114_0.getGameTimes() and arg_114_0.getGameTimes() > 0:
		arg_114_0.SendSuccess(0)

def var_0_0.Update(arg_115_0):
	arg_115_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_116_0):
	if arg_116_0.gameStop or arg_116_0.settlementFlag:
		return

	if IsUnityEditor and Input.GetKeyDown(KeyCode.Space) and arg_116_0.playerController:
		local var_116_0 = arg_116_0.playerController.useSpecial()

def var_0_0.CheckGet(arg_117_0):
	setActive(findTF(arg_117_0.menuUI, "got"), False)

	if arg_117_0.getUltimate() and arg_117_0.getUltimate() != 0:
		setActive(findTF(arg_117_0.menuUI, "got"), True)

	if arg_117_0.getUltimate() == 0:
		if arg_117_0.getGameTotalTime() > arg_117_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_117_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_117_0.menuUI, "got"), True)

def var_0_0.clearUI(arg_118_0):
	return

def var_0_0.readyStart(arg_119_0):
	setActive(arg_119_0.countUI, True)
	arg_119_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_12)
	arg_119_0.bgRoleController.reset()

def var_0_0.gameStart(arg_120_0):
	arg_120_0.gameStartFlag = True
	arg_120_0.gameStepTime = 0
	arg_120_0.gameLastTime = var_0_14

	setActive(findTF(arg_120_0._tf, "scene_front"), True)
	setActive(findTF(arg_120_0._tf, "scene_background"), True)
	setActive(findTF(arg_120_0._tf, "scene"), True)
	setActive(arg_120_0.gameUI, True)
	arg_120_0.playerController.createPlayer()
	arg_120_0.timerStart()
	arg_120_0.gameUIUpdate()

def var_0_0.onTimer(arg_121_0):
	arg_121_0.gameStep()

def var_0_0.gameStep(arg_122_0):
	arg_122_0.playerController.step()
	arg_122_0.enemyController.step()
	arg_122_0.bgRoleController.step()

	arg_122_0.gameLastTime = arg_122_0.gameLastTime - Time.deltaTime

	setText(arg_122_0.textScore, arg_122_0.enemyController.getScore())

	if arg_122_0.gameLastTime <= 0:
		arg_122_0.gameLastTime = 0

		arg_122_0.onGameOver()

	setText(arg_122_0.textTime, math.ceil(arg_122_0.gameLastTime) .. "")

	local var_122_0, var_122_1 = arg_122_0.playerController.getSpecialData()

	var_122_1 = var_122_1 or 0

	if var_122_0 > 0:
		setSlider(arg_122_0.specialSlider, 0, 1, var_122_0 / var_0_19)
	else
		setSlider(arg_122_0.specialSlider, 0, 1, var_122_1 / var_0_20)

	if var_122_1 == var_0_20 or var_122_0 > 0:
		SetActive(arg_122_0.touchSlider, False)
		SetActive(arg_122_0.specialEffect, True)
	else
		SetActive(arg_122_0.touchSlider, True)
		SetActive(arg_122_0.specialEffect, False)

	if arg_122_0.settlementFlag:
		SetActive(arg_122_0.specialEffect, False)

	SetActive(arg_122_0.arrowTf, var_122_1 == var_0_20 and var_122_0 == 0)

def var_0_0.gameUIUpdate(arg_123_0):
	for iter_123_0 = 1, #arg_123_0.hearts:
		if iter_123_0 <= arg_123_0.enemyController.getCakeLifeIndex():
			SetActive(arg_123_0.hearts[iter_123_0], True)
		else
			SetActive(arg_123_0.hearts[iter_123_0], False)

	setText(arg_123_0.textScore, arg_123_0.enemyController.getScore())

def var_0_0.resumeGame(arg_124_0):
	arg_124_0.gameStop = False

	setActive(arg_124_0.leaveUI, False)
	arg_124_0.timerStart()

def var_0_0.stopGame(arg_125_0):
	arg_125_0.gameStop = True

	arg_125_0.timerStop()

def var_0_0.onGameOver(arg_126_0):
	if arg_126_0.settlementFlag:
		return

	arg_126_0.timerStop()

	arg_126_0.settlementFlag = True

	SetActive(arg_126_0.specialEffect, False)
	setActive(arg_126_0.clickMask, True)
	LeanTween.delayedCall(go(arg_126_0._tf), 1, System.Action(function()
		arg_126_0.showSettlement()
		arg_126_0.enemyController.clear()
		arg_126_0.playerController.clear()
		arg_126_0.bgRoleController.reset()

		arg_126_0.settlementFlag = False
		arg_126_0.gameStartFlag = False

		setActive(arg_126_0.clickMask, False)))

def var_0_0.timerStop(arg_128_0):
	if arg_128_0.timer.running:
		arg_128_0.timer.Stop()

def var_0_0.timerStart(arg_129_0):
	if not arg_129_0.timer.running:
		arg_129_0.timer.Start()

def var_0_0.getGameTimes(arg_130_0):
	return arg_130_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_131_0):
	return arg_131_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_132_0):
	return arg_132_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_133_0):
	return (arg_133_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.onBackPressed(arg_134_0):
	return

def var_0_0.willExit(arg_135_0):
	if arg_135_0.handle:
		UpdateBeat.RemoveListener(arg_135_0.handle)

	if arg_135_0.timer and arg_135_0.timer.running:
		arg_135_0.timer.Stop()

	arg_135_0.timer = None

return var_0_0
