local var_0_0 = class("CurlingGameView", import("..BaseMiniGameView"))
local var_0_1 = "event./ui/ddldaoshu2"
local var_0_2 = "event./ui/taosheng"
local var_0_3 = "event./ui/minigame_hitcake"
local var_0_4 = "event./ui/zhengque"
local var_0_5 = "event./ui/shibai"
local var_0_6 = 1
local var_0_7 = 2
local var_0_8 = 3
local var_0_9 = {
	20,
	40,
	60
}
local var_0_10 = 4
local var_0_11 = Vector2(-720, 0)
local var_0_12 = {
	-250,
	250
}
local var_0_13 = Vector2(-250, -42)
local var_0_14 = {
	1,
	10,
	30
}
local var_0_15 = 0.2
local var_0_16 = False
local var_0_17 = {
	walker = 0.1,
	miner = 0.2,
	wall = 0,
	oil = 0.2,
	cube = 0.2
}
local var_0_18 = {
	walker = 2,
	miner = 2,
	wall = 0,
	oil = 2,
	cube = 2
}
local var_0_19 = {
	0.5,
	5,
	10
}
local var_0_20 = {
	0.5,
	5,
	10
}
local var_0_21 = Vector2(400, -600)
local var_0_22 = Vector2(400, 500)
local var_0_23 = 1
local var_0_24 = 2
local var_0_25 = 3
local var_0_26 = 4
local var_0_27 = Vector2(617, -108)
local var_0_28 = 0.7
local var_0_29 = {
	111,
	222,
	333
}
local var_0_30 = {
	3000,
	2000,
	1000
}
local var_0_31 = 1
local var_0_32 = 2
local var_0_33 = 3
local var_0_34 = 4
local var_0_35 = {
	walker = 900,
	miner = 300,
	wall = 100,
	oil = 300,
	cube = 300
}
local var_0_36 = 1
local var_0_37 = {
	oil = {
		{
			appear = 0.8,
			num = 1
		},
		{
			appear = 0.1,
			num = 1
		}
	},
	cube = {
		{
			appear = 0.8,
			num = 1
		},
		{
			appear = 0.1,
			num = 1
		}
	},
	miner = {
		{
			appear = 1,
			num = 1
		},
		{
			appear = 0.1,
			num = 1
		}
	},
	walker = {
		appear = 1,
		path = {
			var_0_23,
			var_0_24,
			var_0_25,
			var_0_26
		}
	}
}
local var_0_38 = {
	cube = 3.5,
	miner = 3.5,
	walker = 4.5,
	oil = 3.5
}
local var_0_39 = True
local var_0_40 = "event_push"
local var_0_41 = "event_speed"
local var_0_42 = "event_hit"
local var_0_43 = "event_result"
local var_0_44 = "event_next"
local var_0_45 = "event_game_pause"
local var_0_46 = "event_game_resume"
local var_0_47 = "event_add_score"

local function var_0_48(arg_1_0, arg_1_1)
	local var_1_0 = {
		def Ctor:(arg_2_0)
			arg_2_0._tf = arg_1_0
			arg_2_0._event = arg_1_1
			arg_2_0.powerTF = findTF(arg_2_0._tf, "power")
			arg_2_0.powerSlider = GetComponent(arg_2_0.powerTF, typeof(Slider))

			arg_2_0.InitPowerSlider()

			arg_2_0.animator = GetComponent(arg_2_0._tf, typeof(Animator))
			arg_2_0.aniDft = GetComponent(arg_2_0._tf, typeof(DftAniEvent))

			arg_2_0.aniDft.SetTriggerEvent(function()
				arg_2_0.Push())

			arg_2_0.dragTrigger = GetOrAddComponent(arg_2_0._tf, "EventTriggerListener")

			arg_2_0.dragTrigger.AddPointDownFunc(function(arg_4_0, arg_4_1)
				if not arg_2_0.canClick:
					return

				arg_2_0.canClick = False
				arg_2_0.charging = True
				arg_2_0.originScreenY = arg_4_1.position.y
				arg_2_0.originY = arg_2_0._tf.anchoredPosition.y

				arg_2_0.Charge())
			arg_2_0.dragTrigger.AddDragFunc(function(arg_5_0, arg_5_1)
				if not arg_2_0.charging:
					return

				local var_5_0 = arg_5_1.position.y - arg_2_0.originScreenY + arg_2_0.originY

				var_5_0 = var_5_0 >= var_0_12[1] and var_5_0 or var_0_12[1]
				var_5_0 = var_5_0 <= var_0_12[2] and var_5_0 or var_0_12[2]

				setLocalPosition(arg_2_0._tf, Vector2(arg_2_0._tf.anchoredPosition.x, var_5_0)))
			arg_2_0.dragTrigger.AddPointUpFunc(function(arg_6_0, arg_6_1)
				if not arg_2_0.charging:
					return

				arg_2_0.charging = False

				arg_2_0.animator.SetInteger("Throw", arg_2_0.phase)
				arg_2_0.animator.SetInteger("Charge", 0))
			arg_2_0._event.bind(var_0_43, function(arg_7_0, arg_7_1, arg_7_2)
				arg_2_0.animator.SetInteger("Result", arg_7_1.result))
			arg_2_0._event.bind(var_0_44, function(arg_8_0, arg_8_1, arg_8_2)
				arg_2_0.Reset()
				arg_2_0.Start())
			arg_2_0.Reset(),
		def Start:(arg_9_0)
			arg_9_0.canClick = True,
		def Reset:(arg_10_0)
			setActive(arg_10_0.powerTF, False)
			setLocalPosition(arg_10_0._tf, var_0_11)
			arg_10_0.animator.SetInteger("Charge", 0)
			arg_10_0.animator.SetInteger("Throw", 0)
			arg_10_0.animator.SetInteger("Result", 0)
			arg_10_0.animator.Play("WaitA")

			arg_10_0.power = 0
			arg_10_0.phase = 0
			arg_10_0.charging = False
			arg_10_0.canClick = False
			arg_10_0.powerSlider.value = 0,
		def InitPowerSlider:(arg_11_0)
			local var_11_0 = 24
			local var_11_1 = 162
			local var_11_2 = var_0_9[1] / var_0_9[3] * var_11_1

			findTF(arg_11_0.powerTF, "progress/green").sizeDelta = Vector2(var_11_2, var_11_0)

			local var_11_3 = (var_0_9[2] - var_0_9[1]) / var_0_9[3] * var_11_1

			findTF(arg_11_0.powerTF, "progress/green/yellow").sizeDelta = Vector2(var_11_3, var_11_0)

			local var_11_4 = (var_0_9[3] - var_0_9[2]) / var_0_9[3] * var_11_1

			findTF(arg_11_0.powerTF, "progress/green/yellow/red").sizeDelta = Vector2(var_11_4, var_11_0),
		def Charge:(arg_12_0)
			setActive(arg_12_0.powerTF, True)
			setActive(findTF(arg_12_0.powerTF, "binghu_huoyan"), False)

			arg_12_0.phase = var_0_6

			arg_12_0.animator.SetInteger("Charge", arg_12_0.phase)
			LeanTween.value(go(arg_12_0._tf), arg_12_0.power, var_0_9[3], var_0_10).setOnUpdate(System.Action_float(function(arg_13_0)
				arg_12_0.power = arg_13_0
				arg_12_0.powerSlider.value = arg_12_0.power / var_0_9[3]

				if arg_12_0.phase == var_0_6 and arg_12_0.power >= var_0_9[1]:
					arg_12_0.phase = var_0_7

					arg_12_0.animator.SetInteger("Charge", arg_12_0.phase)
				elif arg_12_0.phase == var_0_7 and arg_12_0.power >= var_0_9[2]:
					arg_12_0.phase = var_0_8

					arg_12_0.animator.SetInteger("Charge", arg_12_0.phase)
					setActive(findTF(arg_12_0.powerTF, "binghu_huoyan"), True)

				if not arg_12_0.charging:
					LeanTween.cancel(go(arg_12_0._tf)))),
		def Push:(arg_14_0)
			arg_14_0._event.emit(var_0_40, {
				power = arg_14_0.power
			})
			setActive(arg_14_0.powerTF, False)
	}

	var_1_0.Ctor()

	return var_1_0

local function var_0_49(arg_15_0, arg_15_1, arg_15_2)
	local var_15_0 = {
		def Ctor:(arg_16_0)
			arg_16_0.tpls = arg_15_0
			arg_16_0._event = arg_15_2
			arg_16_0.player = arg_15_1
			arg_16_0.scene = arg_16_0.player.parent

			arg_16_0._event.bind(var_0_40, function(arg_17_0, arg_17_1, arg_17_2)
				if arg_16_0.isPush:
					return

				arg_16_0.Push(arg_17_1.power))
			arg_16_0._event.bind(var_0_44, function(arg_18_0, arg_18_1, arg_18_2)
				arg_16_0.Reset()
				arg_16_0.Start())
			arg_16_0._event.bind(var_0_45, function(arg_19_0, arg_19_1, arg_19_2)
				arg_16_0.Pause())
			arg_16_0._event.bind(var_0_46, function(arg_20_0, arg_20_1, arg_20_2)
				arg_16_0.Resume())
			arg_16_0.Reset(),
		def Start:(arg_21_0)
			return,
		def RandomRole:(arg_22_0)
			if arg_22_0._tf:
				arg_22_0._tf.SetParent(arg_22_0.tpls, False)
				setActive(arg_22_0._tf, False)

			local var_22_0 = math.random(1, 4)

			arg_22_0._tf = arg_22_0.tpls.GetChild(var_22_0 - 1)

			setActive(arg_22_0._tf, True)

			arg_22_0.speedTF = findTF(arg_22_0._tf, "speed")

			setActive(arg_22_0.speedTF, var_0_16)

			arg_22_0.animator = GetComponent(arg_22_0._tf, typeof(Animator))
			arg_22_0.rigbody = GetComponent(arg_22_0._tf, "Rigidbody2D")
			arg_22_0.rigbody.velocity = Vector2.zero
			arg_22_0.phyItem = GetComponent(arg_22_0._tf, "Physics2DItem")

			arg_22_0.phyItem.CollisionEnter.RemoveAllListeners()
			arg_22_0.phyItem.CollisionEnter.AddListener(function(arg_23_0)
				arg_22_0.OnCollision(arg_23_0)),
		def Reset:(arg_24_0)
			arg_24_0.RandomRole()

			arg_24_0.rigbody.velocity = Vector2.zero

			arg_24_0._tf.SetParent(findTF(arg_24_0.player, "chargePos"), False)
			setText(arg_24_0.speedTF, 0)
			setLocalPosition(arg_24_0._tf, Vector2.zero)
			setLocalScale(arg_24_0._tf, Vector2.one)
			arg_24_0.animator.Play("Neutral")
			arg_24_0.animator.SetBool("Stop", False)
			arg_24_0.animator.SetInteger("Result", 0)
			arg_24_0.animator.SetInteger("SpeedPhase", 0)

			arg_24_0.isPush = False
			arg_24_0.isStop = True
			arg_24_0.phase = 0,
		def Step:(arg_25_0)
			if var_0_16:
				setText(arg_25_0.speedTF, arg_25_0.rigbody.velocity.Magnitude())

			if not arg_25_0.isPush or arg_25_0.isStop:
				return

			local var_25_0 = arg_25_0.GetSpeed()

			arg_25_0._event.emit(var_0_41, {
				speed = var_25_0
			})

			if var_25_0 > var_0_14[1]:
				arg_25_0.animator.SetInteger("SpeedPhase", 1)
			elif var_25_0 > var_0_14[2]:
				arg_25_0.animator.SetInteger("SpeedPhase", 2)
			elif var_25_0 > var_0_14[3]:
				arg_25_0.animator.SetInteger("SpeedPhase", 3)

			if var_25_0 < var_0_15:
				arg_25_0.animator.SetBool("Stop", True)

				arg_25_0.isStop = True

				arg_25_0.Result(),
		def Push:(arg_26_0, arg_26_1)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_2)

			arg_26_0.isPush = True
			arg_26_0.isStop = False

			arg_26_0._tf.SetParent(arg_26_0.scene, True)

			local var_26_0 = Vector2(var_0_13.x - arg_26_0._tf.anchoredPosition.x, var_0_13.y - arg_26_0._tf.anchoredPosition.y)

			arg_26_0.rigbody.velocity = var_26_0.Normalize().Mul(arg_26_1)

			arg_26_0.Slip(),
		def Slip:(arg_27_0)
			arg_27_0.animator.SetBool("Stop", False)

			arg_27_0.isStop = False,
		def OnCollision:(arg_28_0, arg_28_1)
			arg_28_0.animator.SetTrigger("Hit")
			arg_28_0._event.emit(var_0_42)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_3)

			local var_28_0 = arg_28_1.collider.gameObject.name
			local var_28_1 = 0
			local var_28_2 = Vector2(1, 0)
			local var_28_3 = Vector2(arg_28_0.rigbody.velocity.x, arg_28_0.rigbody.velocity.y)

			if var_28_0 == "wall":
				var_28_3.Mul(var_0_17.wall)

				var_28_1 = var_0_35.wall

				var_28_2.Mul(var_0_18.wall)
			elif var_28_0 == "oil":
				var_28_3.Mul(var_0_17.oil)

				var_28_1 = var_0_35.oil

				var_28_2.Mul(var_0_18.oil)
			elif var_28_0 == "cube":
				var_28_3.Mul(var_0_17.cube)

				var_28_1 = var_0_35.cube

				var_28_2.Mul(var_0_18.cube)
			elif var_28_0 == "miner":
				var_28_3.Mul(var_0_17.miner)

				var_28_1 = var_0_35.miner

				var_28_2.Mul(var_0_18.miner)
			elif var_28_0 == "walker":
				var_28_3.Mul(var_0_17.walker)

				var_28_1 = var_0_35.walker

				var_28_2.Mul(var_0_18.walker)

			arg_28_0.rigbody.velocity = arg_28_0.rigbody.velocity.Sub(var_28_3)
			arg_28_0.rigbody.velocity = arg_28_0.rigbody.velocity.Add(var_28_2)

			local var_28_4 = arg_28_0._tf.anchoredPosition

			arg_28_0._event.emit(var_0_47, {
				score = var_28_1,
				pos = var_28_4
			}),
		def Result:(arg_29_0)
			local var_29_0 = Vector2(arg_29_0._tf.anchoredPosition.x, arg_29_0._tf.anchoredPosition.y / var_0_28)
			local var_29_1 = Vector2.Distance(var_0_27, var_29_0)
			local var_29_2 = 0
			local var_29_3 = var_29_1 <= var_0_29[1] and 1 or var_29_1 <= var_0_29[2] and 2 or var_29_1 <= var_0_29[3] and 3 or 4

			arg_29_0.animator.SetInteger("Result", var_29_3)
			arg_29_0._event.emit(var_0_43, {
				result = var_29_3
			})

			if var_29_3 == 0 or var_29_3 == 4:
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_5)
			else
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_4),
		def Pause:(arg_30_0)
			arg_30_0.speedRecord = arg_30_0.rigbody.velocity
			arg_30_0.rigbody.velocity = Vector2.zero
			arg_30_0.animator.speed = 0,
		def Resume:(arg_31_0)
			arg_31_0.rigbody.velocity = arg_31_0.speedRecord
			arg_31_0.animator.speed = 1,
		def GetSpeed:(arg_32_0)
			return arg_32_0.rigbody.velocity.Magnitude()
	}

	var_15_0.Ctor()

	return var_15_0

local function var_0_50(arg_33_0, arg_33_1)
	local var_33_0 = {
		def Ctor:(arg_34_0)
			arg_34_0._tf = arg_33_0
			arg_34_0._event = arg_33_1
			arg_34_0.animator = GetComponent(arg_34_0._tf, typeof(Animator))

			arg_34_0._event.bind(var_0_40, function(arg_35_0, arg_35_1, arg_35_2)
				arg_34_0.TurnLeft())
			arg_34_0._event.bind(var_0_42, function(arg_36_0, arg_36_1, arg_36_2)
				arg_34_0.Hit())
			arg_34_0._event.bind(var_0_43, function(arg_37_0, arg_37_1, arg_37_2)
				arg_34_0.Result(arg_37_1.result))
			arg_34_0._event.bind(var_0_44, function(arg_38_0, arg_38_1, arg_38_2)
				arg_34_0.Reset()
				arg_34_0.Start()),
		def Start:(arg_39_0)
			return,
		def Reset:(arg_40_0)
			arg_40_0.animator.SetInteger("Result", 0)
			arg_40_0.animator.Play("WaitA"),
		def TurnLeft:(arg_41_0)
			arg_41_0.animator.SetTrigger("TurnLeft"),
		def Result:(arg_42_0, arg_42_1)
			arg_42_0.animator.SetInteger("Result", arg_42_1),
		def Hit:(arg_43_0)
			arg_43_0.animator.SetTrigger("Hit")
	}

	var_33_0.Ctor()

	return var_33_0

local function var_0_51(arg_44_0, arg_44_1)
	local var_44_0 = {
		def Ctor:(arg_45_0)
			arg_45_0._tf = arg_44_0
			arg_45_0._event = arg_44_1
			arg_45_0.animator = GetComponent(arg_45_0._tf, typeof(Animator))

			arg_45_0._event.bind(var_0_44, function(arg_46_0, arg_46_1, arg_46_2)
				arg_45_0.NextRound())
			arg_45_0.Reset(),
		def Start:(arg_47_0)
			arg_47_0.NextRound(),
		def Reset:(arg_48_0)
			arg_48_0.animator.SetInteger("Round", 0)
			arg_48_0.animator.Play("IdleA")

			arg_48_0.roundNum = 1,
		def NextRound:(arg_49_0)
			arg_49_0.animator.SetInteger("Round", arg_49_0.roundNum)

			if arg_49_0.roundNum == 3:
				arg_49_0.roundNum = 1
			else
				arg_49_0.roundNum = arg_49_0.roundNum + 1
	}

	var_44_0.Ctor()

	return var_44_0

local function var_0_52(arg_50_0, arg_50_1)
	local var_50_0 = {
		def Ctor:(arg_51_0)
			arg_51_0._tf = arg_50_0
			arg_51_0._event = arg_50_1
			arg_51_0.config = var_0_37.miner
			arg_51_0.animator = GetComponent(arg_51_0._tf, typeof(Animator))
			arg_51_0.phyItem = GetComponent(arg_51_0._tf, "Physics2DItem")

			arg_51_0.phyItem.CollisionEnter.AddListener(function(arg_52_0)
				arg_51_0.OnCollision())

			arg_51_0.phyGrazeItem = GetComponent(findTF(arg_51_0._tf, "GrazeCollider"), "Physics2DItem")

			arg_51_0.phyGrazeItem.TriggerEnter.AddListener(function(arg_53_0)
				arg_51_0.OnGrazeTrigger(arg_53_0))
			arg_51_0._event.bind(var_0_41, function(arg_54_0, arg_54_1, arg_54_2)
				arg_51_0.hitSpeed = arg_54_1.speed)
			arg_51_0.Reset(),
		def Start:(arg_55_0)
			return,
		def Reset:(arg_56_0)
			arg_56_0.isClash = False
			arg_56_0.hitSpeed = 0,
		def OnCollision:(arg_57_0)
			arg_57_0.isClash = True

			local var_57_0 = 0

			if arg_57_0.hitSpeed > var_0_19[3]:
				var_57_0 = 3
			elif arg_57_0.hitSpeed > var_0_19[2]:
				var_57_0 = 2
			elif arg_57_0.hitSpeed > var_0_19[1]:
				var_57_0 = 1

			arg_57_0.animator.SetInteger("Speed", var_57_0)
			arg_57_0.animator.SetTrigger("Clash"),
		def OnGrazeTrigger:(arg_58_0, arg_58_1)
			if arg_58_1.gameObject.name != "Ayanami":
				return

			onDelayTick(function()
				if arg_58_0.isClash:
					return

				arg_58_0.animator.SetTrigger("Graze"), 0.3)
	}

	var_50_0.Ctor()

	return var_50_0

local function var_0_53(arg_60_0, arg_60_1)
	local var_60_0 = {}
	local var_60_1 = 1000

	function var_60_0.Ctor(arg_61_0)
		arg_61_0._tf = arg_60_0
		arg_61_0._event = arg_60_1
		arg_61_0.config = var_0_37.walker
		arg_61_0.obstacleTF = arg_61_0._tf.parent
		arg_61_0.bgFrontTF = findTF(arg_61_0.obstacleTF.parent.parent, "bg_front")
		arg_61_0.animator = GetComponent(arg_61_0._tf, typeof(Animator))
		arg_61_0.rigbody = GetComponent(arg_61_0._tf, "Rigidbody2D")
		arg_61_0.phyItem = GetComponent(arg_61_0._tf, "Physics2DItem")

		arg_61_0.phyItem.CollisionEnter.AddListener(function(arg_62_0)
			arg_61_0.OnCollision(arg_62_0))
		arg_61_0._event.bind(var_0_41, function(arg_63_0, arg_63_1, arg_63_2)
			arg_61_0.hitSpeed = arg_63_1.speed)
		arg_61_0._event.bind(var_0_45, function(arg_64_0, arg_64_1, arg_64_2)
			arg_61_0.Pause())
		arg_61_0._event.bind(var_0_46, function(arg_65_0, arg_65_1, arg_65_2)
			arg_61_0.Resume())

	function var_60_0.SetPath(arg_66_0, arg_66_1)
		arg_66_0.pathType = arg_66_1

	function var_60_0.Start(arg_67_0)
		arg_67_0.WalkPath()

	function var_60_0.Reset(arg_68_0)
		setActive(arg_68_0._tf, False)
		setLocalPosition(arg_68_0._tf, Vector2(-1400, 0))

		arg_68_0.rigbody.velocity = Vector2.zero
		arg_68_0.isJumpDown = False
		arg_68_0.isJumpUp = False
		arg_68_0.isForwardNorth = False
		arg_68_0.isForwardSouth = False
		arg_68_0.hitSpeed = 0
		arg_68_0.pathType = 0

	function var_60_0.OnCollision(arg_69_0, arg_69_1)
		arg_69_0.animator.SetTrigger("Clash")

		local var_69_0 = 0

		if arg_69_0.hitSpeed > var_0_20[3]:
			var_69_0 = 3
		elif arg_69_0.hitSpeed > var_0_20[2]:
			var_69_0 = 2
		elif arg_69_0.hitSpeed > var_0_20[1]:
			var_69_0 = 1

		arg_69_0.animator.SetInteger("Speed", var_69_0)

		arg_69_0.rigbody.velocity = Vector2.zero

	function var_60_0.WalkPath(arg_70_0)
		if arg_70_0.pathType == var_0_25 or arg_70_0.pathType == var_0_26:
			setLocalPosition(arg_70_0._tf, var_0_21)
			arg_70_0._tf.SetParent(arg_70_0.bgFrontTF, False)

			arg_70_0.isForwardNorth = True

			arg_70_0.animator.SetBool("IsNorth", True)
			arg_70_0.WalkNorth()
		elif arg_70_0.pathType == var_0_23 or arg_70_0.pathType == var_0_24:
			setLocalPosition(arg_70_0._tf, var_0_22)
			arg_70_0._tf.SetParent(arg_70_0.obstacleTF, False)

			arg_70_0.isForwardSouth = True

			arg_70_0.animator.SetBool("IsSouth", True)
			arg_70_0.WalkSouth()

	function var_60_0.WalkNorth(arg_71_0)
		arg_71_0.animator.SetTrigger("WalkN")

		arg_71_0.rigbody.velocity = Vector2(0, 1.5)

	function var_60_0.JumpNorth(arg_72_0)
		arg_72_0.animator.SetTrigger("JumpN")

		if arg_72_0.isJumpUp:
			arg_72_0.WalkNorth()
		elif arg_72_0.pathType == var_0_26:
			arg_72_0.WalkNorthwest()
		else
			arg_72_0.WalkNorth()

	function var_60_0.WalkNorthwest(arg_73_0)
		arg_73_0.animator.SetTrigger("WalkNW")

		arg_73_0.rigbody.velocity = Vector2(-1.5, 1.5)

	function var_60_0.WalkSouth(arg_74_0)
		arg_74_0.animator.SetTrigger("WalkS")

		arg_74_0.rigbody.velocity = Vector2(0, -1.5)

	function var_60_0.JumpSouth(arg_75_0)
		arg_75_0.animator.SetTrigger("JumpS")

		if arg_75_0.isJumpDown:
			arg_75_0.WalkSouth()
		elif arg_75_0.pathType == var_0_24:
			arg_75_0.WalkSouthwest()
		else
			arg_75_0.WalkSouth()

	function var_60_0.WalkSouthwest(arg_76_0)
		arg_76_0.animator.SetTrigger("WalkSW")

		arg_76_0.rigbody.velocity = Vector2(-1.5, -1.5)

	function var_60_0.Step(arg_77_0)
		local var_77_0 = arg_77_0._tf.anchoredPosition.y

		if var_77_0 > var_60_1 or var_77_0 < -var_60_1:
			arg_77_0.rigbody.velocity = Vector2.zero

			return

		if arg_77_0.isForwardNorth:
			if not arg_77_0.isJumpDown and var_77_0 >= -470:
				arg_77_0.isJumpDown = True

				arg_77_0.JumpNorth()
				onDelayTick(function()
					arg_77_0._tf.SetParent(arg_77_0.obstacleTF, False), 0.3)

			if not arg_77_0.isJumpUp and var_77_0 >= 310:
				arg_77_0.isJumpUp = True

				arg_77_0.JumpNorth()

		if arg_77_0.isForwardSouth:
			if not arg_77_0.isJumpUp and var_77_0 <= 370:
				arg_77_0.isJumpUp = True

				arg_77_0.JumpSouth()

			if not arg_77_0.isJumpDown and var_77_0 <= -420:
				arg_77_0.isJumpDown = True

				arg_77_0.JumpSouth()
				onDelayTick(function()
					arg_77_0._tf.SetParent(arg_77_0.bgFrontTF, False), 0.3)

	function var_60_0.Pause(arg_80_0)
		arg_80_0.speedRecord = arg_80_0.rigbody.velocity
		arg_80_0.rigbody.velocity = Vector2.zero
		arg_80_0.animator.speed = 0

	function var_60_0.Resume(arg_81_0)
		arg_81_0.rigbody.velocity = arg_81_0.speedRecord
		arg_81_0.animator.speed = 1

	var_60_0.Ctor()

	return var_60_0

def var_0_0.getUIName(arg_82_0):
	return "CurlingGameUI"

def var_0_0.didEnter(arg_83_0):
	arg_83_0.initEvent()
	arg_83_0.initData()
	arg_83_0.initUI()
	arg_83_0.initGameUI()
	arg_83_0.initController()
	arg_83_0.updateMainUI()
	arg_83_0.openMainUI()
	arg_83_0.AutoFitScreen()

def var_0_0.AutoFitScreen(arg_84_0):
	local var_84_0 = Screen.width / Screen.height
	local var_84_1 = 1.7777777777777777
	local var_84_2 = arg_84_0.findTF("bg_back")
	local var_84_3 = 2331
	local var_84_4 = var_84_2.rect.height
	local var_84_5

	if var_84_1 <= var_84_0:
		local var_84_6 = 1080 * var_84_0

		var_84_5 = math.clamp(var_84_6 / var_84_3, 1, 2)
	else
		local var_84_7 = 1920 / var_84_0

		var_84_5 = math.clamp(var_84_7 / var_84_4, 1, 2)

	setLocalScale(arg_84_0._tf, {
		x = var_84_5,
		y = var_84_5,
		z = var_84_5
	})

def var_0_0.initEvent(arg_85_0):
	arg_85_0.bind(var_0_43, function(arg_86_0, arg_86_1, arg_86_2)
		if arg_86_1.result != var_0_34:
			arg_85_0.addScore(var_0_30[arg_86_1.result])

		arg_85_0.obsFadeOut()
		onDelayTick(function()
			arg_85_0.nextRoundGame(), var_0_36))
	arg_85_0.bind(var_0_47, function(arg_88_0, arg_88_1, arg_88_2)
		if arg_88_1.score and arg_88_1.score != 0:
			arg_85_0.addScore(arg_88_1.score, arg_88_1.pos))

def var_0_0.initData(arg_89_0):
	local var_89_0 = Application.targetFrameRate or 60

	if var_89_0 > 60:
		var_89_0 = 60

	if not Physics2D.autoSimulation:
		arg_89_0.needManualSimulate = True

	arg_89_0.timer = Timer.New(function()
		arg_89_0.onTimer()

		if arg_89_0.needManualSimulate:
			Physics2D.Simulate(1 / var_89_0), 1 / var_89_0, -1)

def var_0_0.initUI(arg_91_0):
	arg_91_0.clickMask = arg_91_0.findTF("ui/click_mask")
	arg_91_0.mainUI = arg_91_0.findTF("ui/main_ui")
	arg_91_0.listScrollRect = GetComponent(findTF(arg_91_0.mainUI, "item_list"), typeof(ScrollRect))

	onButton(arg_91_0, arg_91_0.findTF("skin_btn", arg_91_0.mainUI), function()
		local var_92_0 = pg.mini_game[arg_91_0.GetMGData().id].simple_config_data.skin_shop_id

		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SKINSHOP, {
			skinId = var_92_0
		}), SFX_PANEL)
	onButton(arg_91_0, arg_91_0.findTF("return_btn", arg_91_0.mainUI), function()
		arg_91_0.emit(var_0_0.ON_BACK_PRESSED), SFX_PANEL)
	onButton(arg_91_0, arg_91_0.findTF("help_btn", arg_91_0.mainUI), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.CurlingGame_tips1.tip
		}), SFX_PANEL)
	onButton(arg_91_0, arg_91_0.findTF("start_btn", arg_91_0.mainUI), function()
		arg_91_0.readyStart(), SFX_PANEL)

	arg_91_0.totalTimes = arg_91_0.getGameTotalTime()

	local var_91_0 = arg_91_0.getGameUsedTimes() - 4 < 0 and 0 or arg_91_0.getGameUsedTimes() - 4

	scrollTo(arg_91_0.listScrollRect, 0, 1 - var_91_0 / (arg_91_0.totalTimes - 4))
	onButton(arg_91_0, arg_91_0.findTF("right_panel/arrows_up", arg_91_0.mainUI), function()
		local var_96_0 = arg_91_0.listScrollRect.normalizedPosition.y + 1 / (arg_91_0.totalTimes - 4)

		if var_96_0 > 1:
			var_96_0 = 1

		scrollTo(arg_91_0.listScrollRect, 0, var_96_0), SFX_PANEL)
	onButton(arg_91_0, arg_91_0.findTF("right_panel/arrows_down", arg_91_0.mainUI), function()
		local var_97_0 = arg_91_0.listScrollRect.normalizedPosition.y - 1 / (arg_91_0.totalTimes - 4)

		if var_97_0 < 0:
			var_97_0 = 0

		scrollTo(arg_91_0.listScrollRect, 0, var_97_0), SFX_PANEL)

	local var_91_1 = arg_91_0.findTF("item_tpl", arg_91_0.mainUI)

	arg_91_0.itemList = {}

	local var_91_2 = pg.mini_game[arg_91_0.GetMGData().id].simple_config_data.drop

	for iter_91_0 = 1, #var_91_2:
		local var_91_3 = tf(instantiate(var_91_1))

		var_91_3.name = "item_" .. iter_91_0

		setParent(var_91_3, arg_91_0.findTF("item_list/Viewport/Content", arg_91_0.mainUI))

		local var_91_4 = iter_91_0

		GetSpriteFromAtlasAsync("ui/minigameui/curlinggameui_atlas", "text_" .. var_91_4, function(arg_98_0)
			setImageSprite(arg_91_0.findTF("bg/text", var_91_3), arg_98_0, True))
		setActive(var_91_3, True)
		table.insert(arg_91_0.itemList, var_91_3)

		local var_91_5 = arg_91_0.findTF("award", var_91_3)
		local var_91_6 = {
			type = var_91_2[iter_91_0][1],
			id = var_91_2[iter_91_0][2],
			count = var_91_2[iter_91_0][3]
		}

		updateDrop(var_91_5, var_91_6)
		onButton(arg_91_0, var_91_5, function()
			arg_91_0.emit(BaseUI.ON_DROP, var_91_6), SFX_PANEL)

	arg_91_0.countUI = arg_91_0.findTF("ui/count_ui")
	arg_91_0.countAnimator = GetComponent(arg_91_0.findTF("count", arg_91_0.countUI), typeof(Animator))
	arg_91_0.countDft = GetOrAddComponent(arg_91_0.findTF("count", arg_91_0.countUI), typeof(DftAniEvent))

	arg_91_0.countDft.SetTriggerEvent(function()
		return)
	arg_91_0.countDft.SetEndEvent(function()
		setActive(arg_91_0.countUI, False)
		arg_91_0.startGame())

	arg_91_0.pauseUI = arg_91_0.findTF("ui/pause_ui")

	onButton(arg_91_0, arg_91_0.findTF("ad/panel/sure_btn", arg_91_0.pauseUI), function()
		setActive(arg_91_0.pauseUI, False)
		arg_91_0.resumeGame(), SFX_PANEL)

	arg_91_0.returnUI = arg_91_0.findTF("ui/return_ui")

	onButton(arg_91_0, arg_91_0.findTF("ad/panel/sure_btn", arg_91_0.returnUI), function()
		setActive(arg_91_0.returnUI, False)
		arg_91_0.resumeGame()
		arg_91_0.endGame(), SFX_PANEL)
	onButton(arg_91_0, arg_91_0.findTF("ad/panel/cancel_btn", arg_91_0.returnUI), function()
		setActive(arg_91_0.returnUI, False)
		arg_91_0.resumeGame(), SFX_PANEL)

	arg_91_0.endUI = arg_91_0.findTF("ui/end_ui")

	onButton(arg_91_0, arg_91_0.findTF("ad/panel/end_btn", arg_91_0.endUI), function()
		setActive(arg_91_0.endUI, False)
		arg_91_0.openMainUI(), SFX_PANEL)

	if not arg_91_0.handle:
		arg_91_0.handle = UpdateBeat.CreateListener(arg_91_0.Update, arg_91_0)

	UpdateBeat.AddListener(arg_91_0.handle)

def var_0_0.initGameUI(arg_106_0):
	arg_106_0.gameUI = arg_106_0.findTF("ui/game_ui")
	arg_106_0.roundTF = arg_106_0.findTF("score_panel/round_text", arg_106_0.gameUI)
	arg_106_0.scoreTF = arg_106_0.findTF("score_panel/score_text", arg_106_0.gameUI)

	onButton(arg_106_0, arg_106_0.findTF("pause_btn", arg_106_0.gameUI), function()
		arg_106_0.pauseGame()
		setActive(arg_106_0.pauseUI, True))
	onButton(arg_106_0, arg_106_0.findTF("return_btn", arg_106_0.gameUI), function()
		arg_106_0.pauseGame()
		setActive(arg_106_0.returnUI, True))

	arg_106_0.scoreGroup = arg_106_0.findTF("score_group", arg_106_0.gameUI)

	setActive(arg_106_0.findTF("bg_front/wall"), var_0_39)

def var_0_0.initController(arg_109_0):
	arg_109_0.scene = arg_109_0.findTF("scene")
	arg_109_0.gridTF = arg_109_0.findTF("ui/grid")
	arg_109_0.player = var_0_48(arg_109_0.findTF("player", arg_109_0.scene), arg_109_0)
	arg_109_0.phy = arg_109_0.findTF("Ayanami_phy", arg_109_0.scene)
	arg_109_0.drawDot = arg_109_0.findTF("draw_dot", arg_109_0.scene)
	arg_109_0.curlingTpls = arg_109_0.findTF("curling_Tpl", arg_109_0.scene)
	arg_109_0.curling = var_0_49(arg_109_0.curlingTpls, arg_109_0.player._tf, arg_109_0)
	arg_109_0.ofunya = var_0_50(arg_109_0.findTF("bg_back/07_Ofunya"), arg_109_0)
	arg_109_0.manjuu = var_0_51(arg_109_0.findTF("bg_back/08_Manjuu"), arg_109_0)
	arg_109_0.walker = var_0_53(arg_109_0.findTF("obstacle/walker", arg_109_0.scene), arg_109_0)
	arg_109_0.obsTF = arg_109_0.findTF("scene/obstacle")
	arg_109_0.obsCanvas = GetComponent(arg_109_0.obsTF, typeof(CanvasGroup))
	arg_109_0.obsTpl = arg_109_0.findTF("scene/obstacle_Tpl")
	arg_109_0.minerGroups = arg_109_0.findTF("miner_groups", arg_109_0.obsTF)
	arg_109_0.oilGroups = arg_109_0.findTF("oil_groups", arg_109_0.obsTF)
	arg_109_0.cubeGroups = arg_109_0.findTF("cube_groups", arg_109_0.obsTF)

def var_0_0.updateMainUI(arg_110_0):
	local var_110_0 = arg_110_0.getGameUsedTimes()
	local var_110_1 = arg_110_0.getGameTimes()

	for iter_110_0 = 1, #arg_110_0.itemList:
		setActive(arg_110_0.findTF("lock", arg_110_0.itemList[iter_110_0]), False)
		setActive(arg_110_0.findTF("finish", arg_110_0.itemList[iter_110_0]), False)

		if iter_110_0 <= var_110_0:
			setActive(arg_110_0.findTF("finish", arg_110_0.itemList[iter_110_0]), True)
		elif iter_110_0 == var_110_0 + 1 and var_110_1 >= 1:
			-- block empty
		elif var_110_0 < iter_110_0 and iter_110_0 <= var_110_0 + var_110_1:
			-- block empty
		else
			setActive(arg_110_0.findTF("award", arg_110_0.itemList[iter_110_0]), False)
			setActive(arg_110_0.findTF("lock", arg_110_0.itemList[iter_110_0]), True)

	arg_110_0.totalTimes = arg_110_0.getGameTotalTime()

	local var_110_2 = 1 - (arg_110_0.getGameUsedTimes() - 3 < 0 and 0 or arg_110_0.getGameUsedTimes() - 3) / (arg_110_0.totalTimes - 4)

	if var_110_2 > 1:
		var_110_2 = 1

	scrollTo(arg_110_0.listScrollRect, 0, var_110_2)
	arg_110_0.checkGet()

def var_0_0.checkGet(arg_111_0):
	if arg_111_0.getUltimate() == 0:
		if arg_111_0.getGameTotalTime() > arg_111_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_111_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})

def var_0_0.openMainUI(arg_112_0):
	setActive(arg_112_0.gameUI, False)
	setActive(arg_112_0.mainUI, True)
	arg_112_0.updateMainUI()

def var_0_0.readyStart(arg_113_0):
	setActive(arg_113_0.mainUI, False)
	setActive(arg_113_0.countUI, True)
	arg_113_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_1)
	arg_113_0.resetGame()

def var_0_0.resetGame(arg_114_0):
	arg_114_0.gameStartFlag = False
	arg_114_0.gamePause = False
	arg_114_0.gameEndFlag = False
	arg_114_0.scoreNum = 0
	arg_114_0.roundNum = 1

	arg_114_0.player.Reset()
	arg_114_0.curling.Reset()
	arg_114_0.ofunya.Reset()
	arg_114_0.manjuu.Reset()
	arg_114_0.walker.Reset()

def var_0_0.startGame(arg_115_0):
	setActive(arg_115_0.gameUI, True)
	arg_115_0.CoordinateGrid(arg_115_0.gridTF)

	arg_115_0.gameStartFlag = True

	arg_115_0.player.Start()
	arg_115_0.curling.Start()
	arg_115_0.ofunya.Start()
	arg_115_0.manjuu.Start()
	arg_115_0.staticObsStart()
	arg_115_0.updateGameUI()
	arg_115_0.timerStart()

def var_0_0.staticObsStart(arg_116_0):
	setActive(arg_116_0.obsTF, True)

	arg_116_0.obsCanvas.alpha = 1

	arg_116_0.walker.Reset()

	local var_116_0 = math.random()
	local var_116_1 = var_0_37.walker

	if var_116_0 <= var_116_1.appear:
		setActive(arg_116_0.walker._tf, True)
		setLocalScale(arg_116_0.walker._tf, Vector2(var_0_38.walker, var_0_38.walker))

		local var_116_2 = var_116_1.path[math.random(1, #var_116_1.path)]

		arg_116_0.walker.SetPath(var_116_2)

		local var_116_3 = {}

		if var_116_2 == var_0_26:
			var_116_3 = {
				8,
				11,
				12,
				14,
				15,
				18,
				17,
				21
			}
		elif var_116_2 == var_0_24:
			var_116_3 = {
				5,
				9,
				10,
				14,
				15,
				19,
				20,
				24
			}

		local function var_116_4(arg_117_0)
			for iter_117_0, iter_117_1 in ipairs(var_116_3):
				if arg_117_0 == iter_117_1:
					return True

			return False

		local var_116_5 = {}

		for iter_116_0, iter_116_1 in ipairs(arg_116_0.grids):
			if not var_116_4(iter_116_0):
				table.insert(var_116_5, iter_116_1)

		arg_116_0.grids = var_116_5

		arg_116_0.walker.Start()

	removeAllChildren(arg_116_0.oilGroups)

	for iter_116_2, iter_116_3 in ipairs(var_0_37.oil):
		if math.random() <= iter_116_3.appear:
			for iter_116_4 = 1, iter_116_3.num:
				local var_116_6 = cloneTplTo(arg_116_0.findTF("oil_Tpl", arg_116_0.obsTpl), arg_116_0.oilGroups, "oil")

				setActive(var_116_6, True)

				local var_116_7 = math.random(1, #arg_116_0.grids)

				setLocalPosition(var_116_6, Vector2(arg_116_0.grids[var_116_7].x, arg_116_0.grids[var_116_7].y))
				setLocalScale(var_116_6, Vector2(var_0_38.oil, var_0_38.oil))
				table.remove(arg_116_0.grids, var_116_7)

	removeAllChildren(arg_116_0.cubeGroups)

	for iter_116_5, iter_116_6 in ipairs(var_0_37.cube):
		if math.random() <= iter_116_6.appear:
			for iter_116_7 = 1, iter_116_6.num:
				local var_116_8 = cloneTplTo(arg_116_0.findTF("cube_Tpl", arg_116_0.obsTpl), arg_116_0.cubeGroups, "cube")

				setActive(var_116_8, True)

				local var_116_9 = math.random(1, #arg_116_0.grids)

				setLocalPosition(var_116_8, Vector2(arg_116_0.grids[var_116_9].x, arg_116_0.grids[var_116_9].y))
				setLocalScale(var_116_8, Vector2(var_0_38.cube, var_0_38.cube))
				table.remove(arg_116_0.grids, var_116_9)

	removeAllChildren(arg_116_0.minerGroups)

	arg_116_0.minerControls = {}

	for iter_116_8, iter_116_9 in ipairs(var_0_37.miner):
		if math.random() <= iter_116_9.appear:
			for iter_116_10 = 1, iter_116_9.num:
				local var_116_10 = cloneTplTo(arg_116_0.findTF("miner_Tpl", arg_116_0.obsTpl), arg_116_0.minerGroups, "miner")

				setActive(var_116_10, True)

				local var_116_11 = var_0_52(var_116_10, arg_116_0)

				table.insert(arg_116_0.minerControls, var_116_11)

				local var_116_12 = math.random(1, #arg_116_0.grids)

				setLocalPosition(var_116_10, Vector2(arg_116_0.grids[var_116_12].x, arg_116_0.grids[var_116_12].y))
				setLocalScale(var_116_10, Vector2(var_0_38.miner, var_0_38.miner))
				table.remove(arg_116_0.grids, var_116_12)

def var_0_0.obsFadeOut(arg_118_0):
	arg_118_0.managedTween(LeanTween.value, function()
		setActive(arg_118_0.obsTF, False), go(arg_118_0.obsTF), 1, 0, 0.5).setOnUpdate(System.Action_float(function(arg_120_0)
		arg_118_0.obsCanvas.alpha = arg_120_0))

def var_0_0.Update(arg_121_0):
	arg_121_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_122_0):
	if arg_122_0.gamePause or arg_122_0.gameEndFlag:
		return

	if IsUnityEditor:
		-- block empty

def var_0_0.changeSpeed(arg_123_0, arg_123_1):
	return

def var_0_0.onTimer(arg_124_0):
	arg_124_0.curling.Step()
	arg_124_0.walker.Step()
	arg_124_0.updateGameUI()

def var_0_0.timerStart(arg_125_0):
	if not arg_125_0.timer.running:
		arg_125_0.timer.Start()

def var_0_0.timerStop(arg_126_0):
	if arg_126_0.timer.running:
		arg_126_0.timer.Stop()

def var_0_0.updateGameUI(arg_127_0):
	setText(arg_127_0.scoreTF, arg_127_0.scoreNum)
	setText(arg_127_0.roundTF, "Round " .. arg_127_0.roundNum)

def var_0_0.addScore(arg_128_0, arg_128_1, arg_128_2):
	local var_128_0 = cloneTplTo(arg_128_0.findTF("score_tf", arg_128_0.gameUI), arg_128_0.scoreGroup)

	if arg_128_2:
		setLocalPosition(var_128_0, arg_128_2)
	else
		setLocalPosition(var_128_0, Vector2(432, 144))

	setActive(var_128_0, False)
	setActive(var_128_0, True)
	setText(var_128_0, "+" .. arg_128_1)

	arg_128_0.scoreNum = arg_128_0.scoreNum + arg_128_1

def var_0_0.pauseGame(arg_129_0):
	arg_129_0.gamePause = True

	arg_129_0.timerStop()
	arg_129_0.changeSpeed(0)
	arg_129_0.pauseManagedTween()
	arg_129_0.emit(var_0_45)

def var_0_0.resumeGame(arg_130_0):
	arg_130_0.gamePause = False

	arg_130_0.changeSpeed(1)
	arg_130_0.timerStart()
	arg_130_0.resumeManagedTween()
	arg_130_0.emit(var_0_46)

def var_0_0.nextRoundGame(arg_131_0):
	removeAllChildren(arg_131_0.scoreGroup)

	if arg_131_0.roundNum == 3:
		arg_131_0.endGame()
	else
		arg_131_0.roundNum = arg_131_0.roundNum + 1

		arg_131_0.CoordinateGrid(arg_131_0.gridTF)
		arg_131_0.staticObsStart()
		arg_131_0.emit(var_0_44)

def var_0_0.endGame(arg_132_0):
	if arg_132_0.gameEndFlag:
		return

	arg_132_0.timerStop()

	arg_132_0.gameEndFlag = True

	setActive(arg_132_0.clickMask, True)
	arg_132_0.managedTween(LeanTween.delayedCall, function()
		arg_132_0.gameEndFlag = False
		arg_132_0.gameStartFlag = False

		setActive(arg_132_0.clickMask, False)
		arg_132_0.showEndUI(), 0.1, None)

def var_0_0.showEndUI(arg_134_0):
	setActive(arg_134_0.endUI, True)

	local var_134_0 = arg_134_0.GetMGData().GetRuntimeData("elements")
	local var_134_1 = arg_134_0.scoreNum
	local var_134_2 = var_134_0 and #var_134_0 > 0 and var_134_0[1] or 0

	setActive(arg_134_0.findTF("ad/panel/cur_score/new", arg_134_0.endUI), var_134_2 < var_134_1)

	if var_134_2 <= var_134_1:
		var_134_2 = var_134_1

		arg_134_0.StoreDataToServer({
			var_134_2
		})

	local var_134_3 = arg_134_0.findTF("ad/panel/highest_score", arg_134_0.endUI)
	local var_134_4 = arg_134_0.findTF("ad/panel/cur_score", arg_134_0.endUI)

	setText(var_134_3, var_134_2)
	setText(var_134_4, var_134_1)

	if arg_134_0.getGameTimes() and arg_134_0.getGameTimes() > 0:
		arg_134_0.SendSuccess(0)

def var_0_0.CoordinateGrid(arg_135_0, arg_135_1):
	local var_135_0 = Vector2(150, 150)
	local var_135_1 = arg_135_1.rect.width
	local var_135_2 = arg_135_1.rect.height
	local var_135_3 = Vector2(arg_135_1.anchoredPosition.x - var_135_1 / 2, arg_135_1.anchoredPosition.y - var_135_2 / 2)
	local var_135_4 = math.modf(var_135_2 / var_135_0.y)
	local var_135_5 = var_135_2 % var_135_0.y / (var_135_4 + 1)
	local var_135_6 = math.modf(var_135_1 / var_135_0.x)
	local var_135_7 = var_135_1 % var_135_0.x / (var_135_6 + 1)

	arg_135_0.grids = {}

	for iter_135_0 = 1, var_135_6:
		for iter_135_1 = 1, var_135_4:
			local var_135_8 = var_135_3.x + iter_135_0 * (var_135_7 + var_135_0.x) - var_135_0.x / 2
			local var_135_9 = var_135_3.y + iter_135_1 * (var_135_5 + var_135_0.y) - var_135_0.y / 2

			table.insert(arg_135_0.grids, Vector2(var_135_8, var_135_9))

def var_0_0.getGameTimes(arg_136_0):
	return arg_136_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_137_0):
	return arg_137_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_138_0):
	return arg_138_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_139_0):
	return (arg_139_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.onBackPressed(arg_140_0):
	if not arg_140_0.gameStartFlag:
		arg_140_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_140_0.gameEndFlag:
			return

		if isActive(arg_140_0.pauseUI):
			setActive(arg_140_0.pauseUI, False)

		arg_140_0.pauseGame()
		setActive(arg_140_0.returnUI, True)

def var_0_0.willExit(arg_141_0):
	if arg_141_0.handle:
		UpdateBeat.RemoveListener(arg_141_0.handle)

	arg_141_0.cleanManagedTween()

	if arg_141_0.timer and arg_141_0.timer.running:
		arg_141_0.timer.Stop()

	Time.timeScale = 1
	arg_141_0.timer = None

return var_0_0
