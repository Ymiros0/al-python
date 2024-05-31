local var_0_0 = class("SnowballGameView", import("..BaseMiniGameView"))
local var_0_1 = {
	-1920,
	-1080,
	1920,
	1080
}
local var_0_2 = "snowball_type_player"
local var_0_3 = "snowball_type_enemy"
local var_0_4 = "win"
local var_0_5 = "fail"
local var_0_6 = 3
local var_0_7 = 6
local var_0_8 = "charactor_type_other"
local var_0_9 = "charactor_type_enemy"
local var_0_10 = {
	charactor_type_other = {
		type = var_0_8,
		skin_names = {
			"bailu",
			"huangjia",
			"jiujiu"
		},
		score = {
			-50,
			200,
			-50
		}
	},
	charactor_type_enemy = {
		type = var_0_9,
		skin_names = {
			"enemy1",
			"enemy2",
			"enemy3",
			"enemy4",
			"enemy5",
			"enemy6"
		},
		score = {
			100,
			100,
			100,
			100,
			100,
			100
		}
	}
}
local var_0_11 = 3
local var_0_12 = 1
local var_0_13 = 18
local var_0_14 = 30
local var_0_15 = 3
local var_0_16 = 100
local var_0_17 = {
	12,
	14,
	15,
	16,
	17
}
local var_0_18 = {
	{
		3,
		5
	},
	{
		3,
		4
	},
	{
		2,
		4
	},
	{
		2,
		3
	},
	{
		2,
		2
	}
}
local var_0_19 = {
	{
		90,
		10,
		0
	},
	{
		70,
		20,
		10
	},
	{
		60,
		20,
		20
	},
	{
		50,
		30,
		20
	},
	{
		40,
		40,
		20
	}
}
local var_0_20 = {
	0,
	30,
	60,
	90,
	120
}
local var_0_21 = 1.5
local var_0_22 = {
	{
		weight = 70,
		type = var_0_9,
		indexs = {
			1,
			2,
			3,
			4,
			5,
			6
		},
		time = {
			8,
			10
		},
		attack_time = {
			4,
			6
		}
	},
	{
		weight = 30,
		type = var_0_8,
		indexs = {
			4,
			5,
			6
		},
		time = {
			5,
			7
		}
	}
}
local var_0_23 = "event./ui/ddldaoshu2"
local var_0_24 = "event./ui/sou"
local var_0_25 = "event./ui/xueqiu"

local function var_0_26(arg_1_0)
	print(arg_1_0)

local function var_0_27(arg_2_0)
	local var_2_0 = {}
	local var_2_1 = 1

	function var_2_0.Ctor(arg_3_0)
		arg_3_0._tf = arg_2_0
		arg_3_0.reloadProgress = findTF(arg_3_0._tf, "reloadProgress")
		arg_3_0.playerAnimator = GetComponent(findTF(arg_3_0._tf, "player"), typeof(Animator))
		arg_3_0.playerDft = GetComponent(findTF(arg_3_0._tf, "player"), typeof(DftAniEvent))

		arg_3_0.playerDft.SetStartEvent(function()
			arg_3_0.playerAnimator.ResetTrigger("throw")
			arg_3_0.playerAnimator.SetBool("snowball", True))
		arg_3_0.playerDft.SetTriggerEvent(function()
			arg_3_0.throwSnowball())
		arg_3_0.playerDft.SetEndEvent(function()
			return)

		arg_3_0.heartPos = findTF(arg_3_0._tf, "heartPos")
		arg_3_0.tplHeart = findTF(arg_3_0._tf, "heartPos/tplHeart")
		arg_3_0.collider = findTF(arg_3_0._tf, "collider")
		arg_3_0.throwCallback = None
		arg_3_0.damageCallback = None
		arg_3_0.gameOverCallback = None

	function var_2_0.prepare(arg_7_0)
		arg_7_0._life = var_0_11
		arg_7_0._reloadTime = None
		arg_7_0._skillTime = None
		arg_7_0.stepTime = 0

		arg_7_0.playerAnimator.ResetTrigger("skill")
		arg_7_0.playerAnimator.ResetTrigger("throw")
		arg_7_0.playerAnimator.ResetTrigger("damage")
		arg_7_0.playerAnimator.ResetTrigger("reload")
		arg_7_0.playerAnimator.ResetTrigger("fail")
		arg_7_0.playerAnimator.ResetTrigger("win")
		arg_7_0.playerAnimator.ResetTrigger("fail")
		arg_7_0.playerAnimator.SetTrigger("restart")
		arg_7_0.playerAnimator.ResetTrigger("restart")
		arg_7_0.Clear()

	function var_2_0.step(arg_8_0)
		arg_8_0.stepTime = arg_8_0.stepTime + Time.deltaTime

		if not arg_8_0._reloadTime:
			arg_8_0._reloadTime = arg_8_0.stepTime

		if not arg_8_0.playerAnimator.GetBool("snowball") and arg_8_0.stepTime - arg_8_0._reloadTime > var_0_12:
			arg_8_0.reload()

		if not arg_8_0.playerAnimator.GetBool("snowball") and not isActive(arg_8_0.reloadProgress):
			setActive(arg_8_0.reloadProgress, True)
		elif arg_8_0.playerAnimator.GetBool("snowball") and isActive(arg_8_0.reloadProgress):
			setActive(arg_8_0.reloadProgress, False)

		local var_8_0 = (arg_8_0.stepTime - arg_8_0._reloadTime) / var_0_12

		if var_8_0 > 1:
			var_8_0 = 1

		setSlider(arg_8_0.reloadProgress, 0, 1, var_8_0)

	function var_2_0.reload(arg_9_0)
		arg_9_0.playerAnimator.SetTrigger("reload")

	function var_2_0.skill(arg_10_0)
		if arg_10_0._skillTime and arg_10_0.stepTime - arg_10_0._skillTime < var_0_14:
			return

		arg_10_0._skillTime = arg_10_0.stepTime
		arg_10_0._reloadTime = arg_10_0.stepTime

		arg_10_0.playerAnimator.SetTrigger("skill")

	function var_2_0.throw(arg_11_0)
		if arg_11_0.playerAnimator.GetBool("snowball"):
			arg_11_0.playerAnimator.SetTrigger("throw")

			return True

		return False

	function var_2_0.damage(arg_12_0)
		if arg_12_0._life == 0:
			return

		arg_12_0._life = arg_12_0._life - 1

		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_25)

		if arg_12_0.damageCallback:
			arg_12_0.damageCallback()

		if arg_12_0._life > 0:
			arg_12_0.playerAnimator.SetTrigger("damage")
			arg_12_0.createHeart()
		else
			arg_12_0.playerAnimator.SetTrigger("fail")

			if arg_12_0.gameOverCallback:
				arg_12_0.gameOverCallback()

	function var_2_0.createHeart(arg_13_0)
		local var_13_0 = tf(instantiate(arg_13_0.tplHeart))

		GetComponent(var_13_0, typeof(DftAniEvent)).SetEndEvent(function()
			Destroy(var_13_0))
		setParent(var_13_0, arg_13_0.heartPos)
		setActive(var_13_0, True)

	function var_2_0.setSpeed(arg_15_0, arg_15_1)
		arg_15_0.playerAnimator.speed = arg_15_1

	function var_2_0.throwSnowball(arg_16_0)
		if arg_16_0.throwCallback:
			local var_16_0 = findTF(arg_16_0._tf, "throwPos").position

			arg_16_0.throwCallback(var_16_0)

		arg_16_0.playerAnimator.SetBool("snowball", False)

		arg_16_0._reloadTime = arg_16_0.stepTime

	function var_2_0.move(arg_17_0, arg_17_1)
		arg_17_0._tf.anchoredPosition = arg_17_1

	function var_2_0.settlement(arg_18_0, arg_18_1)
		if arg_18_1 == var_0_5:
			arg_18_0.playerAnimator.SetTrigger("fail")
		elif arg_18_1 == var_0_4:
			arg_18_0.playerAnimator.SetTrigger("win")

	function var_2_0.stop(arg_19_0)
		arg_19_0.playerAnimator.speed = 0

	function var_2_0.resume(arg_20_0)
		arg_20_0.playerAnimator.speed = 1

	function var_2_0.getTargetPosition(arg_21_0)
		return findTF(arg_21_0._tf, "targetPos").position

	function var_2_0.getColliderBound(arg_22_0)
		return arg_22_0.collider.position, arg_22_0.collider.sizeDelta

	function var_2_0.getLife(arg_23_0)
		return arg_23_0._life

	function var_2_0.Clear(arg_24_0)
		arg_24_0._life = var_0_11

	var_2_0.Ctor()

	return var_2_0

local function var_0_28(arg_25_0, arg_25_1, arg_25_2, arg_25_3, arg_25_4)
	local var_25_0 = {
		_tf = arg_25_0,
		_moveDirect = arg_25_1,
		_targetPosition = arg_25_2,
		_type = arg_25_3,
		_targetIndex = arg_25_4
	}

	var_25_0._id = None

	function var_25_0.Ctor(arg_26_0)
		arg_26_0._animator = GetComponent(findTF(arg_26_0._tf, "snowball"), typeof(Animator))
		arg_26_0.snowballDft = GetComponent(findTF(arg_26_0._tf, "snowball"), typeof(DftAniEvent))

		arg_26_0.snowballDft.SetEndEvent(function()
			arg_26_0._removeFlag = True

			arg_26_0.dispose())

	function var_25_0.setId(arg_28_0, arg_28_1)
		arg_28_0._id = arg_28_1

	function var_25_0.getId(arg_29_0, arg_29_1)
		return arg_29_0._id

	function var_25_0.setPosition(arg_30_0, arg_30_1)
		arg_30_0._tf.anchoredPosition = arg_30_1
		arg_30_0._tf.localEulerAngles = Vector3(0, 0, math.atan(arg_25_1.y / arg_25_1.x) * math.rad2Deg)

	function var_25_0.hit(arg_31_0)
		arg_31_0._hitFlag = True

		arg_31_0._animator.SetTrigger("hit")

	function var_25_0.move(arg_32_0)
		local var_32_0 = Time.deltaTime / 0.015

		if var_32_0 > 2:
			var_32_0 = 1

		local var_32_1 = arg_32_0._tf.anchoredPosition

		if arg_32_0._hitFlag:
			var_32_0 = var_32_0 / 8

		var_32_1.x = var_32_1.x + arg_32_0._moveDirect.x * var_32_0
		var_32_1.y = var_32_1.y + arg_32_0._moveDirect.y * var_32_0
		arg_32_0._tf.anchoredPosition = var_32_1

	function var_25_0.getRemoveFlag(arg_33_0)
		return arg_33_0._removeFlag

	function var_25_0.checkOutScene(arg_34_0)
		local var_34_0 = arg_34_0._tf.anchoredPosition

		if var_34_0.x < var_0_1[1] or var_34_0.x > var_0_1[3] or var_34_0.y < var_0_1[2] or var_34_0.y > var_0_1[4]:
			arg_34_0.dispose()

			return True

		return False

	function var_25_0.getAnchoredPos(arg_35_0)
		return arg_35_0._tf.anchoredPosition

	function var_25_0.getTargetPos(arg_36_0)
		return arg_36_0.tar

	function var_25_0.getType(arg_37_0)
		return arg_37_0._type

	function var_25_0.getIndex(arg_38_0)
		return arg_38_0._targetIndex

	function var_25_0.checkArrived(arg_39_0, arg_39_1, arg_39_2)
		if arg_39_0._hitFlag:
			return

		local var_39_0 = arg_39_0.getAnchoredPos()

		if var_39_0.x > arg_39_1.x and var_39_0.x < arg_39_1.x + arg_39_2.x and var_39_0.y > arg_39_1.y and var_39_0.y < arg_39_1.y + arg_39_2.y:
			return True

		return False

	function var_25_0.getArrived(arg_40_0)
		if arg_40_0._hitFlag:
			return

		local var_40_0 = arg_40_0.getAnchoredPos()

		if math.abs(arg_40_0._targetPosition.x - var_40_0.x) <= math.abs(arg_40_0._moveDirect.x * 2) and math.abs(arg_40_0._targetPosition.y - var_40_0.y) <= math.abs(arg_40_0._moveDirect.y * 2):
			return True

		return False

	function var_25_0.dispose(arg_41_0)
		if arg_41_0._tf:
			Destroy(arg_41_0._tf)

			arg_41_0._tf = None

	var_25_0.Ctor()

	return var_25_0

local function var_0_29(arg_42_0, arg_42_1)
	local var_42_0 = {
		_snowballContainer = arg_42_0,
		_tplSnowball = arg_42_1,
		snowballs = {}
	}

	var_42_0._snowBallId = 0

	function var_42_0.createSnowball(arg_43_0, arg_43_1, arg_43_2, arg_43_3, arg_43_4, arg_43_5)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_24)

		local var_43_0 = tf(Instantiate(arg_43_0._tplSnowball))

		SetParent(var_43_0, arg_43_0._snowballContainer)
		setActive(var_43_0, True)

		local var_43_1 = arg_43_3 * (arg_43_2.x > arg_43_1.x and 1 or -1)
		local var_43_2 = (arg_43_2.y - arg_43_1.y) / (arg_43_2.x - arg_43_1.x) * var_43_1

		if arg_43_2.x < arg_43_1.x:
			var_43_0.localScale = Vector3(-1, 1, 1)

		local var_43_3 = Vector3(var_43_1, var_43_2, 0)
		local var_43_4 = var_0_28(var_43_0, var_43_3, arg_43_2, arg_43_4, arg_43_5)

		var_43_4.setId(arg_43_0.getSnowBallId())
		var_43_4.setPosition(arg_43_1)
		table.insert(arg_43_0.snowballs, var_43_4)

	function var_42_0.prepare(arg_44_0)
		for iter_44_0 = #arg_44_0.snowballs, 1, -1:
			local var_44_0 = arg_44_0.snowballs[iter_44_0]

			table.remove(arg_44_0.snowballs, iter_44_0)
			var_44_0.dispose()

	function var_42_0.step(arg_45_0)
		for iter_45_0 = #arg_45_0.snowballs, 1, -1:
			local var_45_0 = arg_45_0.snowballs[iter_45_0]

			if var_45_0.getRemoveFlag() or var_45_0.checkOutScene():
				table.remove(arg_45_0.snowballs, iter_45_0)
			else
				var_45_0.move()

	function var_42_0.clearEnemySnowball(arg_46_0)
		for iter_46_0 = #arg_46_0.snowballs, 1, -1:
			if arg_46_0.snowballs[iter_46_0].getType() == var_0_3:
				arg_46_0.snowballs[iter_46_0].hit()

	function var_42_0.snowballHit(arg_47_0, arg_47_1)
		if not arg_47_1:
			return

		for iter_47_0 = #arg_47_0.snowballs, 1, -1:
			if arg_47_0.snowballs[iter_47_0].getId() == arg_47_1:
				arg_47_0.snowballs[iter_47_0].hit()

	function var_42_0.getSnowBallId(arg_48_0)
		arg_48_0._snowBallId = arg_48_0._snowBallId + 1

		return arg_48_0._snowBallId

	function var_42_0.getSnowballs(arg_49_0)
		return Clone(arg_49_0.snowballs)

	return var_42_0

local function var_0_30(arg_50_0, arg_50_1, arg_50_2, arg_50_3, arg_50_4)
	local var_50_0 = {
		_tf = arg_50_1,
		_index = arg_50_2,
		_data = arg_50_0,
		_name = arg_50_3,
		_score = arg_50_4,
		def Ctor:(arg_51_0)
			arg_51_0.leaveCallback = None
			arg_51_0.collider = findTF(arg_51_0._tf, "collider")
			arg_51_0.otherAnimator = GetComponent(findTF(arg_51_0._tf, "char"), typeof(Animator))
			arg_51_0.otherDft = GetComponent(findTF(arg_51_0._tf, "char"), typeof(DftAniEvent))

			arg_51_0.otherDft.SetEndEvent(function()
				if arg_51_0.leaveCallback:
					arg_51_0.leaveCallback()

				arg_51_0.dispose())

			arg_51_0._leaveTime = math.random(arg_51_0._data.time[1], arg_51_0._data.time[2]),
		def step:(arg_53_0)
			if arg_53_0.removeFlag:
				return

			arg_53_0._leaveTime = arg_53_0._leaveTime - Time.deltaTime,
		def getColliderBound:(arg_54_0)
			return arg_54_0.collider.position, arg_54_0.collider.sizeDelta,
		def apear:(arg_55_0)
			arg_55_0.otherAnimator.SetTrigger("apear"),
		def damage:(arg_56_0)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_25)
			arg_56_0.otherAnimator.SetTrigger("damage"),
		def leave:(arg_57_0)
			arg_57_0.otherAnimator.SetTrigger("leave"),
		def getLeaveTime:(arg_58_0)
			return arg_58_0._leaveTime,
		def getScore:(arg_59_0)
			return arg_59_0._score,
		def getType:(arg_60_0)
			return arg_60_0._data.type,
		def getName:(arg_61_0)
			return arg_61_0._name,
		def setSpeed:(arg_62_0, arg_62_1)
			arg_62_0.otherAnimator.speed = arg_62_1,
		def getPosition:(arg_63_0)
			return arg_63_0._tf.position,
		def dispose:(arg_64_0)
			arg_64_0.leaveCallback = None

			if arg_64_0._tf:
				Destroy(arg_64_0._tf)

				arg_64_0._tf = None

			arg_64_0.removeFlag = True
	}

	var_50_0.Ctor()

	return var_50_0

local function var_0_31(arg_65_0, arg_65_1, arg_65_2, arg_65_3, arg_65_4)
	local var_65_0 = {
		_tf = arg_65_1,
		_index = arg_65_2,
		_data = arg_65_0,
		_name = arg_65_3,
		_score = arg_65_4,
		def Ctor:(arg_66_0)
			arg_66_0.leaveCallback = None
			arg_66_0.enemyAnimator = GetComponent(findTF(arg_66_0._tf, "char"), typeof(Animator))
			arg_66_0.enemyDft = GetComponent(findTF(arg_66_0._tf, "char"), typeof(DftAniEvent))
			arg_66_0.collider = findTF(arg_66_0._tf, "collider")
			arg_66_0.throwPos = findTF(arg_66_0._tf, "throwPos")

			arg_66_0.enemyDft.SetEndEvent(function()
				if arg_66_0.leaveCallback:
					arg_66_0.leaveCallback()

				arg_66_0.dispose())
			arg_66_0.enemyDft.SetTriggerEvent(function()
				if arg_66_0._throwCallback:
					arg_66_0._throwCallback(arg_66_0.throwPos.position, arg_66_0._index))

			arg_66_0._leaveTime = math.random(arg_66_0._data.time[1], arg_66_0._data.time[2])
			arg_66_0._activeTime = 0
	}

	function var_65_0.setThrowCallback(arg_69_0, arg_69_1)
		var_65_0._throwCallback = arg_69_1

	function var_65_0.getColliderBound(arg_70_0)
		return arg_70_0.collider.position, arg_70_0.collider.sizeDelta

	function var_65_0.step(arg_71_0)
		if arg_71_0.removeFlag:
			return

		arg_71_0._leaveTime = arg_71_0._leaveTime - Time.deltaTime
		arg_71_0._activeTime = arg_71_0._activeTime + Time.deltaTime

		if arg_71_0._activeTime > var_0_21:
			arg_71_0._activeTime = 0

			if arg_71_0.getSnowball():
				arg_71_0.throw()
				arg_71_0.enemyAnimator.SetBool("snowball", False)
			else
				arg_71_0.enemyAnimator.SetBool("snowball", True)
				arg_71_0.reload()

	function var_65_0.apear(arg_72_0)
		arg_72_0.enemyAnimator.SetTrigger("apear")

	function var_65_0.damage(arg_73_0)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_25)
		arg_73_0.enemyAnimator.SetTrigger("damage")

	function var_65_0.leave(arg_74_0)
		arg_74_0.enemyAnimator.SetTrigger("leave")

	function var_65_0.reload(arg_75_0)
		arg_75_0.enemyAnimator.SetTrigger("reload")

	function var_65_0.throw(arg_76_0)
		arg_76_0.enemyAnimator.SetTrigger("throw")

	function var_65_0.hit(arg_77_0)
		arg_77_0.enemyAnimator.SetTrigger("hit")

	function var_65_0.getSnowball(arg_78_0)
		return arg_78_0.enemyAnimator.GetBool("snowball")

	function var_65_0.getLeaveTime(arg_79_0)
		return arg_79_0._leaveTime

	function var_65_0.getType(arg_80_0)
		return arg_80_0._data.type

	function var_65_0.getScore(arg_81_0)
		return arg_81_0._score

	function var_65_0.setSpeed(arg_82_0, arg_82_1)
		arg_82_0.enemyAnimator.speed = arg_82_1

	function var_65_0.getName(arg_83_0)
		return arg_83_0._name

	function var_65_0.getPosition(arg_84_0)
		return arg_84_0._tf.position

	function var_65_0.dispose(arg_85_0)
		arg_85_0.leaveCallback = None

		if arg_85_0._tf:
			Destroy(arg_85_0._tf)

			arg_85_0._tf = None

		arg_85_0.removeFlag = True

	var_65_0.Ctor()

	return var_65_0

local function var_0_32(arg_86_0, arg_86_1)
	local var_86_0 = {
		_tplCharactorDic = arg_86_1,
		_charactorContainer = arg_86_0,
		charators = {}
	}

	var_86_0.apearStepTime = None
	var_86_0.gameStepTime = 0

	function var_86_0.Ctor(arg_87_0)
		for iter_87_0 = 1, var_0_7:
			arg_87_0.charators[iter_87_0] = 0

		arg_87_0.throwCallback = None
		arg_87_0.charactorDamageCallback = None

	function var_86_0.prepare(arg_88_0)
		for iter_88_0, iter_88_1 in pairs(arg_88_0.charators):
			if iter_88_1 != 0:
				iter_88_1.dispose()

				arg_88_0.charators[iter_88_0] = 0

		arg_88_0.gameStepTime = 0
		arg_88_0.apearStepTime = None

	function var_86_0.step(arg_89_0)
		arg_89_0.gameStepTime = arg_89_0.gameStepTime + Time.deltaTime

		if arg_89_0.gameStepTime > arg_89_0.getNextApearTime():
			local var_89_0 = arg_89_0.getApearAmount()

			for iter_89_0 = 1, var_89_0:
				arg_89_0.apearCharactor()

			arg_89_0.setNextApearTime()

		for iter_89_1 = 1, #arg_89_0.charators:
			if arg_89_0.charators[iter_89_1] != 0:
				local var_89_1 = arg_89_0.charators[iter_89_1].getLeaveTime()

				if arg_89_0.charators[iter_89_1].getLeaveTime() < 0:
					arg_89_0.leaveCharactor(iter_89_1)
				else
					arg_89_0.charators[iter_89_1].step()

	function var_86_0.leaveCharactor(arg_90_0, arg_90_1)
		if arg_90_0.charators[arg_90_1] != 0:
			arg_90_0.charators[arg_90_1].leave()

			arg_90_0.charators[arg_90_1] = 0

	function var_86_0.removeCharactor(arg_91_0, arg_91_1)
		if arg_91_0.charators[arg_91_1] != 0:
			arg_91_0.charators[arg_91_1] = 0

	function var_86_0.damageEnemy(arg_92_0)
		for iter_92_0 = 1, #arg_92_0.charators:
			if arg_92_0.charators[iter_92_0] and arg_92_0.charators[iter_92_0] != 0 and arg_92_0.charators[iter_92_0].getScore() > 0:
				if arg_92_0.charactorDamageCallback:
					arg_92_0.charactorDamageCallback(arg_92_0.charators[iter_92_0].getPosition(), arg_92_0.charators[iter_92_0].getScore())

				arg_92_0.charators[iter_92_0].damage()
				arg_92_0.removeCharactor(iter_92_0)

	function var_86_0.getCharactorByIndex(arg_93_0, arg_93_1)
		return arg_93_0.charators[arg_93_1]

	function var_86_0.apearCharactor(arg_94_0)
		local var_94_0 = arg_94_0.getAbleRandomDatas()

		if not var_94_0:
			return

		local var_94_1 = arg_94_0.getDataByWeight(var_94_0)

		if not var_94_1:
			return

		local var_94_2, var_94_3 = arg_94_0.getCharactorName(var_0_10[var_94_1.type])
		local var_94_4 = arg_94_0.getCharactorRandomIndex(var_94_1)
		local var_94_5 = arg_94_0.createCharactor(var_94_1, var_94_4, var_94_2, var_94_3)

		if var_94_5:
			arg_94_0.addCharactor(var_94_5, var_94_4)

	function var_86_0.setSpeed(arg_95_0, arg_95_1)
		arg_95_0.speedValue = arg_95_1

		for iter_95_0 = 1, #arg_95_0.charators:
			if arg_95_0.charators[iter_95_0] and arg_95_0.charators[iter_95_0] != 0:
				arg_95_0.charators[iter_95_0].setSpeed(arg_95_1)

	function var_86_0.createCharactor(arg_96_0, arg_96_1, arg_96_2, arg_96_3, arg_96_4)
		local var_96_0 = tf(Instantiate(arg_96_0._tplCharactorDic[arg_96_3]))
		local var_96_1 = findTF(arg_96_0._charactorContainer, arg_96_2)

		SetParent(var_96_0, var_96_1)
		setActive(var_96_0, True)

		local var_96_2

		if arg_96_1.type == var_0_8:
			var_96_2 = var_0_30(arg_96_1, var_96_0, arg_96_2, arg_96_3, arg_96_4)
		elif arg_96_1.type == var_0_9:
			var_96_2 = var_0_31(arg_96_1, var_96_0, arg_96_2, arg_96_3, arg_96_4)

			var_96_2.setThrowCallback(arg_96_0.throwCallback)

		return var_96_2

	function var_86_0.addCharactor(arg_97_0, arg_97_1, arg_97_2)
		arg_97_0.charators[arg_97_2] = arg_97_1

		arg_97_1.apear()

	function var_86_0.getCharactorRandomIndex(arg_98_0, arg_98_1)
		local var_98_0 = arg_98_0.getEmptyIndex()
		local var_98_1 = {}

		for iter_98_0 = 1, #var_98_0:
			if table.contains(arg_98_1.indexs, var_98_0[iter_98_0]):
				table.insert(var_98_1, var_98_0[iter_98_0])

		if #var_98_1:
			return var_98_1[math.random(1, #var_98_1)]

		return None

	function var_86_0.getCharactorName(arg_99_0, arg_99_1)
		local var_99_0 = arg_99_1.skin_names
		local var_99_1 = math.random(1, #arg_99_1.skin_names)

		return arg_99_1.skin_names[var_99_1], arg_99_1.score[var_99_1]

	function var_86_0.getDataByWeight(arg_100_0, arg_100_1)
		if #arg_100_1 == 1:
			return arg_100_1[1]
		else
			if not arg_100_0.charactorWeight:
				arg_100_0.charactorWeight = {}
				arg_100_0.charactorSubWeight = 0

				for iter_100_0 = 1, #arg_100_1:
					arg_100_0.charactorSubWeight = arg_100_0.charactorSubWeight + arg_100_1[iter_100_0].weight

					table.insert(arg_100_0.charactorWeight, arg_100_0.charactorSubWeight)

			local var_100_0 = math.random(0, arg_100_0.charactorSubWeight)

			for iter_100_1 = #arg_100_0.charactorWeight - 1, 1, -1:
				if var_100_0 > arg_100_0.charactorWeight[iter_100_1]:
					return arg_100_1[iter_100_1 + 1]

			return arg_100_1[1]

		return None

	function var_86_0.getAbleRandomDatas(arg_101_0)
		local var_101_0 = {}
		local var_101_1 = arg_101_0.getEmptyIndex()

		if #var_101_1 == 0:
			return var_101_0

		for iter_101_0 = 1, #var_0_22:
			local var_101_2 = var_0_22[iter_101_0].indexs
			local var_101_3

			for iter_101_1, iter_101_2 in ipairs(var_101_2):
				if table.contains(var_101_1, iter_101_2) and not var_101_3:
					table.insert(var_101_0, var_0_22[iter_101_0])

					var_101_3 = True

		return var_101_0

	function var_86_0.getEmptyIndex(arg_102_0)
		local var_102_0 = {}

		for iter_102_0, iter_102_1 in pairs(arg_102_0.charators):
			if iter_102_1 == 0:
				table.insert(var_102_0, iter_102_0)

		return var_102_0

	function var_86_0.getNextApearTime(arg_103_0)
		if not arg_103_0.apearStepTime:
			arg_103_0.setNextApearTime()

		return arg_103_0.apearStepTime

	function var_86_0.setNextApearTime(arg_104_0)
		if not arg_104_0.apearStepTime:
			arg_104_0.apearStepTime = 0

		arg_104_0.apearStepTime = arg_104_0.apearStepTime + arg_104_0.getApearTime()

	function var_86_0.getApearTime(arg_105_0)
		local var_105_0 = 1

		for iter_105_0 = #var_0_20, 1, -1:
			if arg_105_0.gameStepTime > var_0_20[iter_105_0]:
				var_105_0 = iter_105_0

				break

		local var_105_1 = var_0_18[var_105_0][2] - var_0_18[var_105_0][1]
		local var_105_2 = var_0_18[var_105_0][1]

		return math.random() * var_105_1 + var_105_2

	function var_86_0.getApearAmount(arg_106_0)
		local var_106_0 = 1

		for iter_106_0 = #var_0_20, 1, -1:
			if arg_106_0.gameStepTime > var_0_20[iter_106_0]:
				var_106_0 = iter_106_0

				break

		local var_106_1 = var_0_19[var_106_0]
		local var_106_2 = 0
		local var_106_3 = {}

		for iter_106_1 = 1, #var_106_1:
			var_106_2 = var_106_2 + var_106_1[iter_106_1]

			table.insert(var_106_3, var_106_2)

		local var_106_4 = math.random(0, var_106_2)

		for iter_106_2 = #var_106_3 - 1, 1, -1:
			if var_106_4 > var_106_3[iter_106_2]:
				return iter_106_2 + 1

		return 1

	var_86_0.Ctor()

	return var_86_0

local function var_0_33(arg_107_0, arg_107_1, arg_107_2, arg_107_3)
	local var_107_0 = {
		_player = arg_107_1,
		_charactorCtrl = arg_107_3,
		_snowballCtrl = arg_107_2,
		_sceneTf = arg_107_0
	}

	var_107_0.hitEnemyCallback = None

	function var_107_0.Ctor(arg_108_0)
		return

	function var_107_0.prepare(arg_109_0)
		return

	function var_107_0.step(arg_110_0)
		local var_110_0 = arg_110_0._snowballCtrl.getSnowballs()

		for iter_110_0 = 1, #var_110_0:
			local var_110_1 = var_110_0[iter_110_0].getType()
			local var_110_2 = var_110_0[iter_110_0].getIndex()
			local var_110_3 = arg_107_3.getCharactorByIndex(var_110_2)

			if var_110_1 == var_0_2:
				if var_110_3 and var_110_3 != 0:
					local var_110_4, var_110_5 = var_110_3.getColliderBound()
					local var_110_6 = arg_110_0._sceneTf.InverseTransformPoint(var_110_4)

					if var_110_0[iter_110_0].checkArrived(var_110_6, var_110_5):
						var_110_3.damage()
						arg_110_0._snowballCtrl.snowballHit(var_110_0[iter_110_0].getId())
						arg_107_3.removeCharactor(var_110_2)

						if arg_110_0.hitEnemyCallback:
							arg_110_0.hitEnemyCallback(var_110_3.getType(), var_110_3.getName(), var_110_3.getScore(), var_110_3.getPosition())
			elif var_110_1 == var_0_3:
				local var_110_7, var_110_8 = arg_110_0._player.getColliderBound()
				local var_110_9 = arg_110_0._sceneTf.InverseTransformPoint(var_110_7)

				if var_110_0[iter_110_0].checkArrived(var_110_9, var_110_8):
					if var_110_3 and var_110_3 != 0 and var_110_3.getType() == var_0_9:
						var_110_3.hit()

					arg_110_0._player.damage()
					arg_110_0._snowballCtrl.snowballHit(var_110_0[iter_110_0].getId())

	var_107_0.Ctor()

	return var_107_0

def var_0_0.getUIName(arg_111_0):
	return "SnowballGameUI"

def var_0_0.getBGM(arg_112_0):
	return "backyard"

def var_0_0.didEnter(arg_113_0):
	arg_113_0.initData()
	arg_113_0.initUI()

def var_0_0.initData(arg_114_0):
	arg_114_0.timer = Timer.New(function()
		arg_114_0.onTimer(), 0.016666666666666666, -1)

def var_0_0.initUI(arg_116_0):
	arg_116_0.sceneTf = findTF(arg_116_0._tf, "scene")
	arg_116_0.clickMask = findTF(arg_116_0._tf, "clickMask")
	arg_116_0.player = var_0_27(findTF(arg_116_0._tf, "scene/luao"))

	function arg_116_0.player.throwCallback(arg_117_0)
		arg_116_0.onPlayerThrowSnowball(arg_117_0)

	function arg_116_0.player.damageCallback()
		arg_116_0.onPlayerDamage()

	function arg_116_0.player.gameOverCallback()
		arg_116_0.onGameOver()

	arg_116_0.snowballContainer = findTF(arg_116_0._tf, "scene_front/snowballContainer")
	arg_116_0.tplSnowball = findTF(arg_116_0._tf, "tplSnowball")
	arg_116_0.snowballController = var_0_29(arg_116_0.snowballContainer, arg_116_0.tplSnowball)
	arg_116_0.tplScore = findTF(arg_116_0._tf, "tplScore")
	arg_116_0.specialTf = findTF(arg_116_0._tf, "scene_front/special")
	arg_116_0.specialAniamtor = GetComponent(arg_116_0.specialTf, typeof(Animator))

	GetComponent(arg_116_0.specialTf, typeof(DftAniEvent)).SetTriggerEvent(function()
		arg_116_0.specialComplete())

	arg_116_0.charactorContainer = findTF(arg_116_0._tf, "scene/charactorContainer")

	local var_116_0 = {}

	for iter_116_0, iter_116_1 in pairs(var_0_10):
		local var_116_1 = iter_116_1.skin_names

		for iter_116_2, iter_116_3 in ipairs(var_116_1):
			var_116_0[iter_116_3] = findTF(arg_116_0._tf, "charactor/" .. iter_116_3)

	arg_116_0.charactorController = var_0_32(arg_116_0.charactorContainer, var_116_0)

	function arg_116_0.charactorController.throwCallback(arg_121_0, arg_121_1)
		function arg_116_0.charactorController.charactorDamageCallback(arg_122_0, arg_122_1)
			arg_116_0.onHitEnemy(arg_122_1, arg_122_0)

		local var_121_0 = var_0_17[arg_116_0.getCurrentDiff()]

		arg_116_0.onEnemyThrowSnowball(arg_121_0, arg_121_1, var_121_0)

	arg_116_0.colliderController = var_0_33(arg_116_0.sceneTf, arg_116_0.player, arg_116_0.snowballController, arg_116_0.charactorController)

	function arg_116_0.colliderController.hitEnemyCallback(arg_123_0, arg_123_1, arg_123_2, arg_123_3)
		arg_116_0.onHitEnemy(arg_123_2, arg_123_3)

	local var_116_2 = findTF(arg_116_0._tf, "scene/moveCollider")

	arg_116_0.playerMoveVecs = {}

	for iter_116_4 = 1, var_0_6:
		local var_116_3 = findTF(var_116_2, iter_116_4)

		table.insert(arg_116_0.playerMoveVecs, var_116_3.anchoredPosition)

	arg_116_0.lockTf = findTF(arg_116_0._tf, "scene_front/lock")

	local var_116_4 = findTF(arg_116_0._tf, "scene/throwCollider")

	for iter_116_5 = 1, var_0_7:
		local var_116_5 = findTF(var_116_4, iter_116_5)
		local var_116_6 = iter_116_5

		onButton(arg_116_0, var_116_5, function()
			local var_124_0 = arg_116_0.charactorController.getCharactorByIndex(var_116_6)

			if var_124_0 and var_124_0 != 0:
				local var_124_1 = findTF(var_116_5, "target").position
				local var_124_2 = arg_116_0.sceneTf.InverseTransformPoint(var_124_1.x, var_124_1.y, 0)

				arg_116_0.throwSnowballTo(var_124_2, var_116_6, var_124_0))

	arg_116_0.countUI = findTF(arg_116_0._tf, "pop/CountUI")
	arg_116_0.countAnimator = GetComponent(findTF(arg_116_0.countUI, "count"), typeof(Animator))
	arg_116_0.countDft = GetComponent(findTF(arg_116_0.countUI, "count"), typeof(DftAniEvent))

	arg_116_0.countDft.SetTriggerEvent(function()
		return)
	arg_116_0.countDft.SetEndEvent(function()
		setActive(arg_116_0.countUI, False)
		arg_116_0.gameStart())

	arg_116_0.leaveUI = findTF(arg_116_0._tf, "pop/LeaveUI")

	onButton(arg_116_0, findTF(arg_116_0.leaveUI, "ad/btnOk"), function()
		arg_116_0.resumeGame()
		arg_116_0.player.settlement(var_0_4)
		arg_116_0.onGameOver(), SFX_CANCEL)
	onButton(arg_116_0, findTF(arg_116_0.leaveUI, "ad/btnCancel"), function()
		arg_116_0.resumeGame(), SFX_CANCEL)

	arg_116_0.pauseUI = findTF(arg_116_0._tf, "pop/pauseUI")

	onButton(arg_116_0, findTF(arg_116_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_116_0.pauseUI, False)
		arg_116_0.resumeGame(), SFX_CANCEL)

	arg_116_0.settlementUI = findTF(arg_116_0._tf, "pop/SettleMentUI")

	onButton(arg_116_0, findTF(arg_116_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_116_0.settlementUI, False)
		arg_116_0.openMenuUI(), SFX_CANCEL)

	arg_116_0.menuUI = findTF(arg_116_0._tf, "pop/menuUI")
	arg_116_0.battleScrollRect = GetComponent(findTF(arg_116_0.menuUI, "battList"), typeof(ScrollRect))
	arg_116_0.totalTimes = arg_116_0.getGameTotalTime()

	local var_116_7 = arg_116_0.getGameUsedTimes() - 4 < 0 and 0 or arg_116_0.getGameUsedTimes() - 4

	scrollTo(arg_116_0.battleScrollRect, 0, 1 - var_116_7 / (arg_116_0.totalTimes - 4))
	onButton(arg_116_0, findTF(arg_116_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_131_0 = arg_116_0.battleScrollRect.normalizedPosition.y + 1 / (arg_116_0.totalTimes - 4)

		if var_131_0 > 1:
			var_131_0 = 1

		scrollTo(arg_116_0.battleScrollRect, 0, var_131_0), SFX_CANCEL)
	onButton(arg_116_0, findTF(arg_116_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_132_0 = arg_116_0.battleScrollRect.normalizedPosition.y - 1 / (arg_116_0.totalTimes - 4)

		if var_132_0 < 0:
			var_132_0 = 0

		scrollTo(arg_116_0.battleScrollRect, 0, var_132_0), SFX_CANCEL)
	onButton(arg_116_0, findTF(arg_116_0.menuUI, "btnBack"), function()
		arg_116_0.closeView(), SFX_CANCEL)
	onButton(arg_116_0, findTF(arg_116_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.snowball_help.tip
		}), SFX_CANCEL)
	onButton(arg_116_0, findTF(arg_116_0.menuUI, "btnStart"), function()
		setActive(arg_116_0.menuUI, False)
		arg_116_0.readyStart(), SFX_CANCEL)

	local var_116_8 = findTF(arg_116_0.menuUI, "tplBattleItem")

	arg_116_0.battleItems = {}

	for iter_116_6 = 1, arg_116_0.totalTimes:
		local var_116_9 = tf(instantiate(var_116_8))

		var_116_9.name = "battleItem_" .. iter_116_6

		setParent(var_116_9, findTF(arg_116_0.menuUI, "battList/Viewport/Content"))

		local var_116_10 = iter_116_6

		GetSpriteFromAtlasAsync("ui/minigameui/snowballgameui_atlas", "tx_" .. var_116_10, function(arg_136_0)
			setImageSprite(findTF(var_116_9, "state_open/icon"), arg_136_0, True)
			setImageSprite(findTF(var_116_9, "state_clear/icon"), arg_136_0, True)
			setImageSprite(findTF(var_116_9, "state_current/icon"), arg_136_0, True))
		GetSpriteFromAtlasAsync("ui/minigameui/snowballgameui_atlas", "battleDesc" .. var_116_10, function(arg_137_0)
			setImageSprite(findTF(var_116_9, "state_open/buttomDesc"), arg_137_0, True)
			setImageSprite(findTF(var_116_9, "state_clear/buttomDesc"), arg_137_0, True)
			setImageSprite(findTF(var_116_9, "state_current/buttomDesc"), arg_137_0, True)
			setImageSprite(findTF(var_116_9, "state_closed/buttomDesc"), arg_137_0, True))
		setActive(var_116_9, True)
		table.insert(arg_116_0.battleItems, var_116_9)

	arg_116_0.gameUI = findTF(arg_116_0._tf, "ui/gameUI")
	arg_116_0.lifeProgress = findTF(arg_116_0.gameUI, "lifeProgress")
	arg_116_0.textLife = findTF(arg_116_0.gameUI, "life")
	arg_116_0.textScore = findTF(arg_116_0.gameUI, "score")

	onButton(arg_116_0, findTF(arg_116_0.gameUI, "btnStop"), function()
		arg_116_0.stopGame()
		setActive(arg_116_0.pauseUI, True))
	onButton(arg_116_0, findTF(arg_116_0.gameUI, "btnLeave"), function()
		arg_116_0.stopGame()
		setActive(arg_116_0.leaveUI, True))
	onButton(arg_116_0, findTF(arg_116_0.gameUI, "btnMoveUp"), function()
		if arg_116_0.playerPosIndex > 1:
			arg_116_0.playerPosIndex = arg_116_0.playerPosIndex - 1

			arg_116_0.movePlayerTo(arg_116_0.playerPosIndex))
	onButton(arg_116_0, findTF(arg_116_0.gameUI, "btnMoveDown"), function()
		if arg_116_0.playerPosIndex < #arg_116_0.playerMoveVecs:
			arg_116_0.playerPosIndex = arg_116_0.playerPosIndex + 1

			arg_116_0.movePlayerTo(arg_116_0.playerPosIndex))

	arg_116_0.btnSkill = findTF(arg_116_0.gameUI, "btnSkill")

	onButton(arg_116_0, arg_116_0.btnSkill, function()
		if arg_116_0.skilTime == var_0_14:
			arg_116_0.skilTime = 0

			arg_116_0.usePlayerSkill())
	arg_116_0.updateMenuUI()
	arg_116_0.openMenuUI()

	if not arg_116_0.handle:
		arg_116_0.handle = UpdateBeat.CreateListener(arg_116_0.Update, arg_116_0)

	UpdateBeat.AddListener(arg_116_0.handle)

def var_0_0.Update(arg_143_0):
	arg_143_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_144_0):
	if arg_144_0.gameStop or arg_144_0.settlementFlag:
		return

	if IsUnityEditor:
		if Input.GetKeyDown(KeyCode.W) and arg_144_0.playerPosIndex and arg_144_0.playerPosIndex > 1:
			arg_144_0.playerPosIndex = arg_144_0.playerPosIndex - 1

			arg_144_0.movePlayerTo(arg_144_0.playerPosIndex)

		if Input.GetKeyDown(KeyCode.S) and arg_144_0.playerPosIndex and arg_144_0.playerPosIndex < #arg_144_0.playerMoveVecs:
			arg_144_0.playerPosIndex = arg_144_0.playerPosIndex + 1

			arg_144_0.movePlayerTo(arg_144_0.playerPosIndex)

def var_0_0.getCurrentDiff(arg_145_0):
	for iter_145_0 = #var_0_20, 1, -1:
		if arg_145_0.gameStepTime > var_0_20[iter_145_0]:
			return iter_145_0

def var_0_0.updateMenuUI(arg_146_0):
	local var_146_0 = arg_146_0.getGameUsedTimes()
	local var_146_1 = arg_146_0.getGameTimes()

	for iter_146_0 = 1, #arg_146_0.battleItems:
		setActive(findTF(arg_146_0.battleItems[iter_146_0], "state_open"), False)
		setActive(findTF(arg_146_0.battleItems[iter_146_0], "state_closed"), False)
		setActive(findTF(arg_146_0.battleItems[iter_146_0], "state_clear"), False)
		setActive(findTF(arg_146_0.battleItems[iter_146_0], "state_current"), False)

		if iter_146_0 <= var_146_0:
			setActive(findTF(arg_146_0.battleItems[iter_146_0], "state_clear"), True)
		elif iter_146_0 == var_146_0 + 1 and var_146_1 >= 1:
			setActive(findTF(arg_146_0.battleItems[iter_146_0], "state_current"), True)
		elif var_146_0 < iter_146_0 and iter_146_0 <= var_146_0 + var_146_1:
			setActive(findTF(arg_146_0.battleItems[iter_146_0], "state_open"), True)
		else
			setActive(findTF(arg_146_0.battleItems[iter_146_0], "state_closed"), True)

	arg_146_0.totalTimes = arg_146_0.getGameTotalTime()

	local var_146_2 = 1 - (arg_146_0.getGameUsedTimes() - 3 < 0 and 0 or arg_146_0.getGameUsedTimes() - 3) / (arg_146_0.totalTimes - 4)

	if var_146_2 > 1:
		var_146_2 = 1

	scrollTo(arg_146_0.battleScrollRect, 0, var_146_2)
	setActive(findTF(arg_146_0.menuUI, "btnStart/tip"), var_146_1 > 0)
	arg_146_0.CheckGet()

def var_0_0.CheckGet(arg_147_0):
	setActive(findTF(arg_147_0.menuUI, "got"), False)

	if arg_147_0.getUltimate() and arg_147_0.getUltimate() != 0:
		setActive(findTF(arg_147_0.menuUI, "got"), True)

	if arg_147_0.getUltimate() == 0:
		if arg_147_0.getGameTotalTime() > arg_147_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_147_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_147_0.menuUI, "got"), True)

def var_0_0.openMenuUI(arg_148_0):
	setActive(findTF(arg_148_0._tf, "scene_front"), False)
	setActive(findTF(arg_148_0._tf, "scene_background"), False)
	setActive(findTF(arg_148_0._tf, "scene"), False)
	setActive(arg_148_0.gameUI, False)
	setActive(arg_148_0.menuUI, True)
	arg_148_0.updateMenuUI()

def var_0_0.clearUI(arg_149_0):
	setActive(arg_149_0.sceneTf, False)
	setActive(arg_149_0.settlementUI, False)
	setActive(arg_149_0.countUI, False)
	setActive(arg_149_0.menuUI, False)
	setActive(arg_149_0.gameUI, False)

def var_0_0.OnSendMiniGameOPDone(arg_150_0, arg_150_1):
	if arg_150_0.sendSuccessFlag:
		local var_150_0 = (getProxy(MiniGameProxy).GetMiniGameData(MiniGameDataCreator.NewYearShrineGameID).GetRuntimeData("count") or 0) + 2

		pg.m02.sendNotification(GAME.MODIFY_MINI_GAME_DATA, {
			id = MiniGameDataCreator.NewYearShrineGameID,
			map = {
				count = var_150_0
			}
		})

		arg_150_0.sendSuccessFlag = False

def var_0_0.readyStart(arg_151_0):
	setActive(arg_151_0.countUI, True)
	arg_151_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_23)

def var_0_0.gameStart(arg_152_0):
	setActive(findTF(arg_152_0._tf, "scene_front"), True)
	setActive(findTF(arg_152_0._tf, "scene_background"), True)
	setActive(findTF(arg_152_0._tf, "scene"), True)
	setActive(arg_152_0.gameUI, True)
	setActive(arg_152_0.lockTf, False)

	arg_152_0.gameStartFlag = True
	arg_152_0.scoreNum = 0
	arg_152_0.skilTime = 0
	arg_152_0.playerPosIndex = 2

	arg_152_0.movePlayerTo(arg_152_0.playerPosIndex)

	arg_152_0.specialTime = 0
	arg_152_0.gameStepTime = 0

	arg_152_0.player.prepare()
	arg_152_0.snowballController.prepare()
	arg_152_0.charactorController.prepare()
	arg_152_0.colliderController.prepare()
	arg_152_0.updateGameUI()
	arg_152_0.timerStart()

def var_0_0.onPlayerDamage(arg_153_0):
	arg_153_0.updateGameUI()

def var_0_0.getGameTimes(arg_154_0):
	return arg_154_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_155_0):
	return arg_155_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_156_0):
	return arg_156_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_157_0):
	return (arg_157_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.changeSpeed(arg_158_0, arg_158_1):
	arg_158_0.player.setSpeed(arg_158_1)

	arg_158_0.specialAniamtor.speed = arg_158_1

	arg_158_0.charactorController.setSpeed(arg_158_1)

def var_0_0.onTimer(arg_159_0):
	arg_159_0.player.step()
	arg_159_0.snowballController.step()
	arg_159_0.charactorController.step()
	arg_159_0.colliderController.step()
	arg_159_0.gameStep()

def var_0_0.gameStep(arg_160_0):
	arg_160_0.gameStepTime = arg_160_0.gameStepTime + Time.deltaTime
	arg_160_0.skilTime = arg_160_0.skilTime + Time.deltaTime

	if arg_160_0.skilTime > var_0_14:
		arg_160_0.skilTime = var_0_14

	if not arg_160_0.skillProgress:
		arg_160_0.skillProgress = GetComponent(findTF(arg_160_0.btnSkill, "progress"), typeof(Image))

	arg_160_0.skillProgress.fillAmount = arg_160_0.skilTime / var_0_14

	if arg_160_0.skilTime == var_0_14:
		if not isActive(findTF(arg_160_0.gameUI, "xuehezhan_zhiyuantiao")):
			setActive(findTF(arg_160_0.gameUI, "xuehezhan_zhiyuantiao"), True)
	elif isActive(findTF(arg_160_0.gameUI, "xuehezhan_zhiyuantiao")):
		setActive(findTF(arg_160_0.gameUI, "xuehezhan_zhiyuantiao"), False)

	if arg_160_0.gameStepTime < arg_160_0.specialTime:
		if not arg_160_0.specialIndex:
			arg_160_0.specialIndex = 0

		if arg_160_0.specialIndex > 20:
			arg_160_0.specialIndex = 0

			arg_160_0.charactorController.damageEnemy()

		arg_160_0.specialIndex = arg_160_0.specialIndex + 1

def var_0_0.timerStart(arg_161_0):
	if not arg_161_0.timer.running:
		arg_161_0.timer.Start()

def var_0_0.timerStop(arg_162_0):
	if arg_162_0.timer.running:
		arg_162_0.timer.Stop()

def var_0_0.movePlayerTo(arg_163_0, arg_163_1):
	arg_163_0.player.move(arg_163_0.playerMoveVecs[arg_163_1])

def var_0_0.updateGameUI(arg_164_0):
	setSlider(arg_164_0.lifeProgress, 0, 1, arg_164_0.player.getLife() / var_0_11)
	setText(arg_164_0.textLife, arg_164_0.player.getLife() .. "/" .. var_0_11)
	setText(arg_164_0.textScore, arg_164_0.scoreNum)

def var_0_0.throwSnowballTo(arg_165_0, arg_165_1, arg_165_2, arg_165_3):
	arg_165_0.throwTarget = arg_165_1
	arg_165_0.targetIndex = arg_165_2

	if arg_165_0.player.throw() and arg_165_0.targetCharactor != arg_165_3:
		setActive(arg_165_0.lockTf, False)

		arg_165_0.lockTf.anchoredPosition = arg_165_1

		setActive(arg_165_0.lockTf, True)

		arg_165_0.targetCharactor = arg_165_3

def var_0_0.onPlayerThrowSnowball(arg_166_0, arg_166_1):
	if arg_166_0.throwTarget:
		local var_166_0 = arg_166_0.sceneTf.InverseTransformPoint(arg_166_1.x, arg_166_1.y, 0)
		local var_166_1 = arg_166_0.throwTarget

		arg_166_0.snowballController.createSnowball(var_166_0, var_166_1, var_0_13, var_0_2, arg_166_0.targetIndex)

		arg_166_0.throwTarget = None
		arg_166_0.targetIndex = None

def var_0_0.onEnemyThrowSnowball(arg_167_0, arg_167_1, arg_167_2, arg_167_3):
	local var_167_0 = arg_167_0.sceneTf.InverseTransformPoint(arg_167_1.x, arg_167_1.y, 0)
	local var_167_1 = arg_167_0.player.getTargetPosition()
	local var_167_2 = arg_167_0.sceneTf.InverseTransformPoint(var_167_1.x, var_167_1.y, 0)

	arg_167_0.snowballController.createSnowball(var_167_0, var_167_2, arg_167_3, var_0_3, arg_167_2)

def var_0_0.usePlayerSkill(arg_168_0):
	Time.timeScale = 0.05

	LeanTween.delayedCall(go(arg_168_0.specialTf), 3, System.Action(function()
		if Time.timeScale != 1:
			Time.timeScale = 1))
	arg_168_0.player.skill()
	arg_168_0.snowballController.clearEnemySnowball()
	setActive(arg_168_0.specialTf, True)

	if not arg_168_0.specialEffect:
		arg_168_0.specialEffect = findTF(arg_168_0._tf, "xuehezhan_xueqiuhongzha")

	setActive(arg_168_0.specialEffect, False)
	setActive(arg_168_0.specialEffect, True)

def var_0_0.specialComplete(arg_170_0):
	Time.timeScale = 1

	setActive(arg_170_0.specialTf, False)

	arg_170_0.specialTime = arg_170_0.gameStepTime + var_0_15
	arg_170_0.specialIndex = 0

def var_0_0.dropSpeedUp(arg_171_0):
	return

def var_0_0.onHitEnemy(arg_172_0, arg_172_1, arg_172_2):
	arg_172_0.addScore(arg_172_1, arg_172_2)
	arg_172_0.updateGameUI()

def var_0_0.addScore(arg_173_0, arg_173_1, arg_173_2):
	arg_173_0.scoreNum = arg_173_0.scoreNum + arg_173_1

	if arg_173_0.scoreNum < 0:
		arg_173_0.scoreNum = 0

	local var_173_0 = tf(instantiate(arg_173_0.tplScore))
	local var_173_1 = findTF(var_173_0, "ad")
	local var_173_2 = GetComponent(var_173_1, typeof(DftAniEvent))

	var_173_0.anchoredPosition = arg_173_0.snowballContainer.InverseTransformPoint(arg_173_2)

	if arg_173_1 > 0:
		setActive(findTF(var_173_1, "add"), True)
		setText(findTF(var_173_1, "add"), "+" .. arg_173_1)
	else
		setActive(findTF(var_173_1, "sub"), True)
		setText(findTF(var_173_1, "sub"), arg_173_1)

	setParent(var_173_0, arg_173_0.snowballContainer)
	var_173_2.SetEndEvent(function()
		setActive(var_173_0, False)
		Destroy(var_173_0))
	setActive(var_173_0, True)

def var_0_0.onGameOver(arg_175_0):
	arg_175_0.timerStop()

	arg_175_0.settlementFlag = True

	setActive(arg_175_0.clickMask, True)
	LeanTween.delayedCall(go(arg_175_0._tf), 2, System.Action(function()
		arg_175_0.settlementFlag = False
		arg_175_0.gameStartFlag = False

		setActive(arg_175_0.clickMask, False)
		setActive(findTF(arg_175_0.gameUI, "xuehezhan_zhiyuantiao"), False)
		setActive(arg_175_0.specialTf, False)
		arg_175_0.showSettlement()))

def var_0_0.showSettlement(arg_177_0):
	setActive(arg_177_0.settlementUI, True)
	GetComponent(findTF(arg_177_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_177_0 = arg_177_0.GetMGData().GetRuntimeData("elements")
	local var_177_1 = arg_177_0.scoreNum
	local var_177_2 = var_177_0 and #var_177_0 > 0 and var_177_0[1] or 0

	if var_177_2 <= var_177_1:
		var_177_2 = var_177_1

		arg_177_0.StoreDataToServer({
			var_177_2
		})

	local var_177_3 = findTF(arg_177_0.settlementUI, "ad/highText")
	local var_177_4 = findTF(arg_177_0.settlementUI, "ad/currentText")

	setText(var_177_3, var_177_2)
	setText(var_177_4, var_177_1)

	if arg_177_0.getGameTimes() and arg_177_0.getGameTimes() > 0:
		arg_177_0.sendSuccessFlag = True

		arg_177_0.SendSuccess(0)

def var_0_0.resumeGame(arg_178_0):
	arg_178_0.gameStop = False

	setActive(arg_178_0.leaveUI, False)
	arg_178_0.changeSpeed(1)
	arg_178_0.timerStart()

def var_0_0.stopGame(arg_179_0):
	arg_179_0.gameStop = True

	arg_179_0.timerStop()
	arg_179_0.changeSpeed(0)

def var_0_0.onBackPressed(arg_180_0):
	if not arg_180_0.gameStartFlag:
		arg_180_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_180_0.settlementFlag:
			return

		if isActive(arg_180_0.pauseUI):
			setActive(arg_180_0.pauseUI, False)

		arg_180_0.stopGame()
		setActive(arg_180_0.leaveUI, True)

def var_0_0.willExit(arg_181_0):
	if arg_181_0.handle:
		UpdateBeat.RemoveListener(arg_181_0.handle)

	if not arg_181_0._tf:
		print()

	if arg_181_0._tf and LeanTween.isTweening(go(arg_181_0._tf)):
		LeanTween.cancel(go(arg_181_0._tf))

	if arg_181_0.specialTf and LeanTween.isTweening(go(arg_181_0.specialTf)):
		LeanTween.cancel(go(arg_181_0.specialTf))

	if arg_181_0.specialEffect and LeanTween.isTweening(go(arg_181_0.specialEffect)):
		LeanTween.cancel(go(arg_181_0.specialEffect))

	if arg_181_0.timer and arg_181_0.timer.running:
		arg_181_0.timer.Stop()

	Time.timeScale = 1
	arg_181_0.timer = None

return var_0_0
