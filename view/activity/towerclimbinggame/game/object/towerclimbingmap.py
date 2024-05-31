local var_0_0 = class("TowerClimbingMap")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1.gameView
	arg_1_0.view = arg_1_1
	arg_1_0.map = arg_1_2

def var_0_0.Init(arg_2_0, arg_2_1):
	arg_2_0.blocks = {}
	arg_2_0.groundContainer = arg_2_0._tf.Find("game")
	arg_2_0.blockPlayCon = arg_2_0.groundContainer.Find("block_play_con")

	setAnchoredPosition(arg_2_0.blockPlayCon, {
		x = 0,
		y = 0
	})

	arg_2_0.blockContainer = arg_2_0.blockPlayCon.Find("blocks")
	arg_2_0.hearts = {
		arg_2_0._tf.Find("prints/score/hearts/1"),
		arg_2_0._tf.Find("prints/score/hearts/2"),
		arg_2_0._tf.Find("prints/score/hearts/3")
	}
	arg_2_0.score = arg_2_0._tf.Find("prints/score/Text").GetComponent(typeof(Text))
	arg_2_0.heartProgress = arg_2_0._tf.Find("prints/score/progress")
	arg_2_0.heartProgressTxt = arg_2_0._tf.Find("prints/score/progress/Text").GetComponent(typeof(Text))
	arg_2_0.bg = TowerClimbBgMgr.New(arg_2_0._tf.Find("bgs"))

	arg_2_0.bg.Init(arg_2_0.map.id, arg_2_1)

	arg_2_0.npc = arg_2_0._tf.Find("prints/npc")

	arg_2_0.LoadEffect(arg_2_0.map.id)

	arg_2_0.tip = arg_2_0._tf.Find("prints/tip")

	setActive(arg_2_0.tip, False)

	arg_2_0.timers = {}

def var_0_0.LoadEffect(arg_3_0, arg_3_1):
	local var_3_0 = TowerClimbingGameSettings.MAPID2EFFECT[arg_3_1]

	if var_3_0:
		for iter_3_0, iter_3_1 in ipairs(var_3_0):
			local var_3_1 = iter_3_1[1]
			local var_3_2 = iter_3_1[2]

			arg_3_0.LoadSingleEffect(var_3_1, var_3_2)

def var_0_0.LoadSingleEffect(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	PoolMgr.GetInstance().GetUI(arg_4_1, True, function(arg_5_0)
		if not arg_4_0.groundContainer:
			PoolMgr.GetInstance().ReturnUI(arg_4_1, arg_5_0)
		else
			arg_5_0.name = arg_4_1

			SetParent(arg_5_0, arg_4_0.groundContainer)

			arg_5_0.transform.anchoredPosition3D = Vector3(arg_4_2[1], arg_4_2[2], -200)

			setActive(arg_5_0, True)

			if arg_4_3:
				arg_4_3(arg_5_0))

def var_0_0.ReturnEffect(arg_6_0, arg_6_1):
	local var_6_0 = TowerClimbingGameSettings.MAPID2EFFECT[arg_6_1]

	if var_6_0:
		for iter_6_0, iter_6_1 in ipairs(var_6_0):
			local var_6_1 = iter_6_1[1]
			local var_6_2 = arg_6_0.groundContainer.Find(var_6_1)

			if var_6_2:
				PoolMgr.GetInstance().ReturnUI(var_6_1, var_6_2.gameObject)

def var_0_0.OnReachAwardScore(arg_7_0):
	if LOCK_TOWERCLIMBING_AWARD:
		return

	if arg_7_0.tipTimer:
		arg_7_0.tipTimer.Stop()

		arg_7_0.tipTimer = None

	setActive(arg_7_0.tip, True)

	arg_7_0.tipTimer = Timer.New(function()
		setActive(arg_7_0.tip, False)
		arg_7_0.tipTimer.Stop()

		arg_7_0.tipTimer = None, 3, 1)

	arg_7_0.tipTimer.Start()

	local var_7_0 = arg_7_0.groundContainer.InverseTransformPoint(arg_7_0.npc.position)
	local var_7_1 = arg_7_0.groundContainer.InverseTransformPoint(arg_7_0.player._tf.position)

	local function var_7_2()
		local function var_9_0()
			setActive(arg_7_0.awardEffect1, True)

			arg_7_0.awardTimer = Timer.New(function()
				setActive(arg_7_0.awardEffect1, False), 2, 1)

			arg_7_0.awardTimer.Start()

		if not arg_7_0.awardEffect1:
			local var_9_1 = {
				var_7_0.x,
				var_7_0.y
			}

			arg_7_0.LoadSingleEffect(TowerClimbingGameSettings.AWARDEFFECT1, var_9_1, function(arg_12_0)
				arg_7_0.awardEffect1 = arg_12_0

				var_9_0())
		else
			var_9_0()

	local function var_7_3()
		local var_13_0 = Vector3(var_7_0.x, var_7_1.y + 200, -200)
		local var_13_1 = {}

		table.insert(var_13_1, Vector3(var_7_1.x, var_7_1.y, -200))
		table.insert(var_13_1, var_13_0)
		table.insert(var_13_1, var_13_0)
		table.insert(var_13_1, Vector3(var_7_0.x, var_7_0.y, -200))

		arg_7_0.awardEffect.transform.localPosition = Vector3(var_7_1.x, var_7_1.y, -200)

		setActive(arg_7_0.awardEffect, True)
		LeanTween.moveLocal(arg_7_0.awardEffect, var_13_1, 1).setOnComplete(System.Action(function()
			setActive(arg_7_0.awardEffect, False)
			var_7_2()))

	if not arg_7_0.awardEffect:
		local var_7_4 = {
			var_7_1.x,
			var_7_1.y
		}

		arg_7_0.LoadSingleEffect(TowerClimbingGameSettings.AWARDEFFECT, var_7_4, function(arg_15_0)
			arg_7_0.awardEffect = arg_15_0

			var_7_3())
	else
		var_7_3()

def var_0_0.GetFirstBlock(arg_16_0):
	return arg_16_0.blocks[1]

def var_0_0.GetHitBlock(arg_17_0, arg_17_1):
	local var_17_0 = _.detect(arg_17_0.blocks, function(arg_18_0)
		return arg_18_0.go == arg_17_1)

	if var_17_0:
		return var_17_0

def var_0_0.OnCreateGround(arg_19_0, arg_19_1, arg_19_2):
	arg_19_0.ground = arg_19_1

	TowerClimbingResMgr.GetGround(arg_19_1.name, function(arg_20_0)
		arg_19_0.groundGo = arg_20_0
		arg_20_0.name = "manjuu"

		SetParent(arg_20_0.transform, arg_19_0.groundContainer)

		arg_20_0.transform.anchoredPosition = arg_19_1.position

		setActive(arg_20_0, True)
		arg_20_0.GetComponent("SpineAnimUI").SetAction("normal", 0)
		setText(arg_19_0.groundGo.transform.Find("Text"), "")
		arg_19_2())

def var_0_0.TranslateBlockPosition(arg_21_0, arg_21_1):
	return arg_21_0.blockContainer.InverseTransformVector(arg_21_0.groundContainer.TransformVector(arg_21_1))

def var_0_0.OnCreateBlock(arg_22_0, arg_22_1, arg_22_2):
	TowerClimbingResMgr.GetBlock(arg_22_1.type, function(arg_23_0)
		SetParent(arg_23_0, arg_22_0.blockContainer)

		arg_23_0.transform.anchoredPosition = arg_22_0.TranslateBlockPosition(arg_22_1.position)
		arg_23_0.name = TowerClimbingGameSettings.BLOCK_NAME

		setActive(arg_23_0, True)

		local var_23_0 = arg_23_0.GetComponentsInChildren(typeof(UnityEngine.Collider2D))
		local var_23_1 = {}

		for iter_23_0 = 1, var_23_0.Length:
			table.insert(var_23_1, var_23_0[iter_23_0 - 1])

		table.insert(arg_22_0.blocks, {
			go = arg_23_0,
			block = arg_22_1,
			colliders = var_23_1
		})
		arg_22_0.OnActiveBlock(arg_22_1)

		local var_23_2 = TowerClimbingGameSettings.FIRE_TIME[1]
		local var_23_3 = TowerClimbingGameSettings.FIRE_TIME[2]
		local var_23_4 = math.random(var_23_2, var_23_3)
		local var_23_5 = arg_23_0.transform.Find("firer")

		if var_23_5:
			local var_23_6 = var_23_5.GetComponent(typeof(Animation))

			arg_22_0.timers[arg_22_1.level] = Timer.New(function()
				var_23_6.Play("action"), var_23_4, -1)

			arg_22_0.timers[arg_22_1.level].Start()

		arg_22_2())

def var_0_0.OnActiveBlock(arg_25_0, arg_25_1):
	local var_25_0 = _.detect(arg_25_0.blocks, function(arg_26_0)
		return arg_26_0.block.level == arg_25_1.level)

	for iter_25_0, iter_25_1 in ipairs(var_25_0.colliders):
		iter_25_1.enabled = arg_25_1.isActive

def var_0_0.SinkHandler(arg_27_0, arg_27_1, arg_27_2):
	local var_27_0 = arg_27_0.blockPlayCon.anchoredPosition.y
	local var_27_1 = arg_27_0.blockPlayCon.anchoredPosition.y - arg_27_1

	LeanTween.value(arg_27_0.blockPlayCon.gameObject, var_27_0, var_27_1, 0.2).setOnUpdate(System.Action_float(function(arg_28_0)
		setAnchoredPosition(arg_27_0.blockPlayCon, {
			y = arg_28_0
		}))).setEase(LeanTweenType.easeOutQuad).setOnComplete(System.Action(arg_27_2))

def var_0_0.OnBlockDestory(arg_29_0, arg_29_1):
	if arg_29_0.timers[arg_29_1]:
		arg_29_0.timers[arg_29_1].Stop()

		arg_29_0.timers[arg_29_1] = None

	local var_29_0 = _.detect(arg_29_0.blocks, function(arg_30_0)
		return arg_30_0.block.level == arg_29_1)

	TowerClimbingResMgr.ReturnBlock(var_29_0.block.type, var_29_0.go)

def var_0_0.OnSink(arg_31_0, arg_31_1, arg_31_2):
	arg_31_0.bg.DoMove(arg_31_1, arg_31_2)
	arg_31_2()

def var_0_0.OnPlayerLifeUpdate(arg_32_0, arg_32_1):
	triggerToggle(arg_32_0.hearts[3], arg_32_1 >= 3)
	triggerToggle(arg_32_0.hearts[2], arg_32_1 >= 2)
	triggerToggle(arg_32_0.hearts[1], arg_32_1 >= 1)

	arg_32_0.heartProgressTxt.text = arg_32_1 .. "/" .. 3

	setFillAmount(arg_32_0.heartProgress, arg_32_1 / 3)

def var_0_0.OnScoreUpdate(arg_33_0, arg_33_1):
	arg_33_0.score.text = arg_33_1

def var_0_0.OnCreatePlayer(arg_34_0, arg_34_1, arg_34_2):
	arg_34_0.player = TowerClimbingPlayer.New(arg_34_0, arg_34_1)

	arg_34_0.player.Init(arg_34_2)

def var_0_0.OnEnableStab(arg_35_0, arg_35_1, arg_35_2):
	local var_35_0 = _.detect(arg_35_0.blocks, function(arg_36_0)
		return arg_36_0.block.level == arg_35_1.level)

	assert(var_35_0)

	local var_35_1 = var_35_0.go.GetComponent(typeof(UnityEngine.Collider2D))

	for iter_35_0, iter_35_1 in ipairs(var_35_0.colliders):
		if iter_35_1 != var_35_1:
			iter_35_1.enabled = arg_35_2

def var_0_0.OnEnableGround(arg_37_0, arg_37_1):
	arg_37_0.groundGo.GetComponent(typeof(UnityEngine.Collider2D)).enabled = arg_37_1

def var_0_0.GetPlayer(arg_38_0):
	return arg_38_0.player

def var_0_0.SendEvent(arg_39_0, arg_39_1, ...):
	local var_39_0 = arg_39_0.view.controller

	var_39_0[arg_39_1](var_39_0, unpack({
		...
	}))

def var_0_0.OnGroundRuning(arg_40_0):
	arg_40_0.groundGo.GetComponent("SpineAnimUI").SetAction("up", 0)

def var_0_0.OnGroundPositionChange(arg_41_0, arg_41_1):
	setAnchoredPosition(arg_41_0.groundGo.transform, arg_41_1)

def var_0_0.OnGroundSleepTimeChange(arg_42_0, arg_42_1):
	local var_42_0 = math.ceil(arg_42_1)

	if var_42_0 > 0:
		setText(arg_42_0.groundGo.transform.Find("Text"), var_42_0)
	else
		setText(arg_42_0.groundGo.transform.Find("Text"), "")

def var_0_0.Dispose(arg_43_0):
	if arg_43_0.awardTimer:
		arg_43_0.awardTimer.Stop()

		arg_43_0.awardTimer = None

	arg_43_0.bg.Clear()
	arg_43_0.ReturnEffect(arg_43_0.map.id)

	if arg_43_0.awardEffect:
		PoolMgr.GetInstance().ReturnUI(arg_43_0.awardEffect.name, arg_43_0.awardEffect)

		arg_43_0.awardEffect = None

	if arg_43_0.awardEffect1:
		PoolMgr.GetInstance().ReturnUI(arg_43_0.awardEffect1.name, arg_43_0.awardEffect1)

		arg_43_0.awardEffect1 = None

	if arg_43_0.tipTimer:
		arg_43_0.tipTimer.Stop()

	arg_43_0.tipTimer = None

	for iter_43_0, iter_43_1 in pairs(arg_43_0.timers or {}):
		iter_43_1.Stop()

	arg_43_0.timers = None

	if arg_43_0.player:
		arg_43_0.player.Dispose()

		arg_43_0.player = None

	if arg_43_0.ground and not IsNil(arg_43_0.groundGo):
		TowerClimbingResMgr.ReturnGround(arg_43_0.ground.name, arg_43_0.groundGo)

	if arg_43_0.blocks:
		for iter_43_2, iter_43_3 in ipairs(arg_43_0.blocks):
			if not IsNil(iter_43_3.go):
				TowerClimbingResMgr.ReturnBlock(iter_43_3.block.type, iter_43_3.go)

		arg_43_0.blocks = None

return var_0_0
