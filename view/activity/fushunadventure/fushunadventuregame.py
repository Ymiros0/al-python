local var_0_0 = class("FushunAdventureGame")
local var_0_1 = False
local var_0_2 = 0
local var_0_3 = 1
local var_0_4 = 2
local var_0_5 = 3
local var_0_6 = 4

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.fushunLoader = AutoLoader.New()
	arg_1_0.state = var_0_2
	arg_1_0._go = arg_1_1
	arg_1_0.gameData = arg_1_2
	arg_1_0.highestScore = (arg_1_3.GetRuntimeData("elements") or {})[1] or 0

	arg_1_0.Init()

def var_0_0.SetOnShowResult(arg_2_0, arg_2_1):
	arg_2_0.OnShowResult = arg_2_1

def var_0_0.SetOnLevelUpdate(arg_3_0, arg_3_1):
	arg_3_0.OnLevelUpdate = arg_3_1

def var_0_0.Init(arg_4_0):
	if arg_4_0.state != var_0_2:
		return

	arg_4_0.state = var_0_4

	arg_4_0.InitMainUI()

def var_0_0.InitMainUI(arg_5_0):
	local var_5_0 = arg_5_0._go

	onButton(arg_5_0, findTF(var_5_0, "btn_help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.fushun_adventure_help.tip
		}), SFX_PANEL)
	onButton(arg_5_0, findTF(var_5_0, "btn_start"), function()
		pg.BgmMgr.GetInstance().StopPlay()
		arg_5_0.StartGame(), SFX_PANEL)

	arg_5_0.levelList = UIItemList.New(findTF(var_5_0, "levels/scrollrect/content"), findTF(var_5_0, "levels/scrollrect/content/level"))
	arg_5_0.arrUp = findTF(var_5_0, "levels/arr_up")
	arg_5_0.arrDown = findTF(var_5_0, "levels/arr_bottom")

	onScroll(arg_5_0, findTF(var_5_0, "levels/scrollrect"), function(arg_8_0)
		setActive(arg_5_0.arrUp, arg_8_0.y < 1)
		setActive(arg_5_0.arrDown, arg_8_0.y > 0))
	arg_5_0.RefreshLevels()

def var_0_0.RefreshLevels(arg_9_0):
	local var_9_0

	arg_9_0.levelList.make(function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0 == UIItemList.EventUpdate:
			arg_10_2.Find("Text").GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("ui/FushunAdventureGame_atlas", "level_" .. arg_10_1 + 1)

			local var_10_0 = arg_9_0.gameData.count > 0 and 1 or 0
			local var_10_1 = arg_10_1 >= arg_9_0.gameData.usedtime + var_10_0

			setActive(arg_10_2.Find("lock"), var_10_1)

			local var_10_2 = arg_10_1 < arg_9_0.gameData.usedtime

			setActive(arg_10_2.Find("cleared"), var_10_2)
			setActive(arg_10_2.Find("Text"), not var_10_1)

			if not var_10_2 and not var_9_0:
				var_9_0 = arg_10_1

			arg_10_2.GetComponent(typeof(Image)).enabled = not var_10_1)
	arg_9_0.levelList.align(FushunAdventureGameConst.LEVEL_CNT)
	setActive(findTF(arg_9_0._go, "tip/got"), arg_9_0.gameData.ultimate != 0)

	if var_9_0:
		local var_9_1 = var_9_0 * (arg_9_0.levelList.item.rect.height + 50)
		local var_9_2 = arg_9_0.levelList.container.anchoredPosition

		setAnchoredPosition(arg_9_0.levelList.container, {
			y = var_9_2.y + var_9_1
		})

	if arg_9_0.OnLevelUpdate:
		arg_9_0.OnLevelUpdate()

def var_0_0.InitGameUI(arg_11_0):
	local var_11_0 = arg_11_0.gameUI

	arg_11_0.btnA = findTF(var_11_0, "UI/A")
	arg_11_0.btnB = findTF(var_11_0, "UI/B")
	arg_11_0.btnAEffect = arg_11_0.btnA.Find("effect")
	arg_11_0.btnBEffect = arg_11_0.btnB.Find("effect")
	arg_11_0.btnAExEffect = arg_11_0.btnA.Find("effect_ex")
	arg_11_0.btnBExEffect = arg_11_0.btnB.Find("effect_ex")
	arg_11_0.keys = {
		findTF(var_11_0, "UI/keys/1").GetComponent(typeof(Image)),
		findTF(var_11_0, "UI/keys/2").GetComponent(typeof(Image)),
		findTF(var_11_0, "UI/keys/3").GetComponent(typeof(Image))
	}
	arg_11_0.btnSprites = {
		arg_11_0.keys[1].sprite,
		arg_11_0.btnA.GetComponent(typeof(Image)).sprite,
		arg_11_0.btnB.GetComponent(typeof(Image)).sprite
	}
	arg_11_0.hearts = {
		findTF(var_11_0, "UI/heart_score/hearts/1/mark"),
		findTF(var_11_0, "UI/heart_score/hearts/2/mark"),
		findTF(var_11_0, "UI/heart_score/hearts/3/mark")
	}
	arg_11_0.numbers = {
		findTF(var_11_0, "UI/countdown_panel/timer/3"),
		findTF(var_11_0, "UI/countdown_panel/timer/2"),
		findTF(var_11_0, "UI/countdown_panel/timer/1")
	}
	arg_11_0.scoreTxt = findTF(var_11_0, "UI/heart_score/score/Text").GetComponent(typeof(Text))
	arg_11_0.energyBar = findTF(var_11_0, "UI/ex/bar").GetComponent(typeof(Image))
	arg_11_0.energyIcon = findTF(var_11_0, "UI/ex/icon")
	arg_11_0.energyLight = findTF(var_11_0, "UI/ex/light")
	arg_11_0.exTipPanel = findTF(var_11_0, "UI/ex_tip_panel")
	arg_11_0.comboTxt = findTF(var_11_0, "UI/combo/Text").GetComponent(typeof(Text))
	arg_11_0.countdownPanel = findTF(var_11_0, "UI/countdown_panel")
	arg_11_0.resultPanel = findTF(var_11_0, "UI/result_panel")
	arg_11_0.resultCloseBtn = findTF(arg_11_0.resultPanel, "frame/close")
	arg_11_0.resultHighestScoreTxt = findTF(arg_11_0.resultPanel, "frame/highest/Text").GetComponent(typeof(Text))
	arg_11_0.resultScoreTxt = findTF(arg_11_0.resultPanel, "frame/score/Text").GetComponent(typeof(Text))
	arg_11_0.msgboxPanel = findTF(var_11_0, "UI/msg_panel")
	arg_11_0.exitMsgboxWindow = findTF(arg_11_0.msgboxPanel, "frame/exit_mode")
	arg_11_0.pauseMsgboxWindow = findTF(arg_11_0.msgboxPanel, "frame/pause_mode")
	arg_11_0.helpWindow = findTF(var_11_0, "UI/help")
	arg_11_0.lightTF = findTF(var_11_0, "game/range")
	arg_11_0.lightMark = arg_11_0.lightTF.Find("Image")
	arg_11_0.pauseBtn = findTF(var_11_0, "UI/pause")
	arg_11_0.exitBtn = findTF(var_11_0, "UI/back")
	arg_11_0.energyBar.fillAmount = 0

def var_0_0.EnterAnimation(arg_12_0, arg_12_1):
	setActive(arg_12_0.countdownPanel, True)

	local function var_12_0(arg_13_0)
		for iter_13_0, iter_13_1 in ipairs(arg_12_0.numbers):
			setActive(iter_13_1, iter_13_0 == arg_13_0)

	local var_12_1 = 1

	arg_12_0.countdownTimer = Timer.New(function()
		var_12_1 = var_12_1 + 1

		if var_12_1 > 3:
			setActive(arg_12_0.countdownPanel, False)
			arg_12_1()
		else
			var_12_0(var_12_1), 1, 3)

	var_12_0(var_12_1)
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(FushunAdventureGameConst.COUNT_DOWN_VOICE)
	arg_12_0.countdownTimer.Start()

def var_0_0.ShowHelpWindow(arg_15_0, arg_15_1):
	setActive(arg_15_0.helpWindow, True)
	onButton(arg_15_0, arg_15_0.helpWindow, function()
		setActive(arg_15_0.helpWindow, False)
		PlayerPrefs.SetInt("FushunAdventureGame" .. getProxy(PlayerProxy).getRawData().id, 1)
		arg_15_1(), SFX_PANEL)

def var_0_0.DisplayKey(arg_17_0):
	local function var_17_0(arg_18_0, arg_18_1)
		local var_18_0

		if not arg_18_1 or arg_18_1 == "":
			var_18_0 = arg_17_0.btnSprites[1]
		elif arg_18_1 == "A":
			var_18_0 = arg_17_0.btnSprites[2]
		elif arg_18_1 == "B":
			var_18_0 = arg_17_0.btnSprites[3]

		if arg_18_0.sprite != var_18_0:
			arg_18_0.sprite = var_18_0

	for iter_17_0, iter_17_1 in ipairs(arg_17_0.keys):
		local var_17_1 = string.sub(arg_17_0.key, iter_17_0, iter_17_0) or ""

		var_17_0(iter_17_1, var_17_1)

def var_0_0.DisplayeHearts(arg_19_0, arg_19_1):
	for iter_19_0, iter_19_1 in ipairs(arg_19_0.hearts):
		setActive(iter_19_1, iter_19_0 <= arg_19_1)

def var_0_0.DisplayScore(arg_20_0):
	arg_20_0.scoreTxt.text = arg_20_0.score

def var_0_0.DisplayeEnergy(arg_21_0, arg_21_1, arg_21_2):
	local var_21_0 = math.min(1, arg_21_1 / arg_21_2)

	arg_21_0.energyBar.fillAmount = var_21_0

	local var_21_1 = arg_21_0.energyIcon.parent.rect.width * var_21_0
	local var_21_2 = var_21_1 - arg_21_0.energyIcon.rect.width

	setAnchoredPosition(arg_21_0.energyIcon, {
		x = math.max(0, var_21_2)
	})

	local var_21_3 = 0

	if var_21_0 >= 1:
		var_21_3 = tf(arg_21_0.energyBar.gameObject).rect.width
	elif var_21_1 > 0:
		var_21_3 = var_21_1

	setActive(arg_21_0.energyLight, var_21_0 >= 0.01)

	arg_21_0.energyLight.sizeDelta = Vector2(var_21_3, arg_21_0.energyLight.sizeDelta.y)

def var_0_0.StartGame(arg_22_0):
	if arg_22_0.state != var_0_4:
		return

	arg_22_0.enemys = {}
	arg_22_0.hitList = {}
	arg_22_0.missFlags = {}
	arg_22_0.score = 0
	arg_22_0.combo = 0
	arg_22_0.pause = False
	arg_22_0.schedule = FushunSchedule.New()
	arg_22_0.specailSchedule = FushunSchedule.New()

	arg_22_0.LoadScene(function()
		arg_22_0.EnterGame()
		pg.BgmMgr.GetInstance().Push(arg_22_0.__cname, FushunAdventureGameConst.GAME_BGM_NAME))

	arg_22_0.state = var_0_5

def var_0_0.LoadScene(arg_24_0, arg_24_1):
	seriesAsync({
		function(arg_25_0)
			if arg_24_0.gameUI:
				setActive(arg_24_0.gameUI, True)
				arg_25_0()
			else
				arg_24_0.fushunLoader.LoadPrefab("ui/FushunAdventureGame", "", function(arg_26_0)
					arg_24_0.gameUI = arg_26_0

					arg_26_0.transform.SetParent(arg_24_0._go.transform, False)
					arg_24_0.InitGameUI()
					arg_25_0(), "FushunAdventureGame"),
		function(arg_27_0)
			arg_24_0.DisplayeHearts(3)
			arg_24_0.DisplayScore()
			arg_24_0.DisplayeEnergy(0, 1)

			if not (PlayerPrefs.GetInt("FushunAdventureGame" .. getProxy(PlayerProxy).getRawData().id, 0) > 0):
				arg_24_0.ShowHelpWindow(arg_27_0)
			else
				arg_27_0(),
		function(arg_28_0)
			parallelAsync({
				function(arg_29_0)
					arg_24_0.EnterAnimation(arg_29_0),
				function(arg_30_0)
					arg_24_0.fushunLoader.LoadPrefab("FushunAdventure/fushun", "", function(arg_31_0)
						arg_24_0.fushun = FushunChar.New(arg_31_0)

						arg_24_0.fushun.SetPosition(FushunAdventureGameConst.FUSHUN_INIT_POSITION)
						arg_31_0.transform.SetParent(arg_24_0.gameUI.transform.Find("game"), False)
						arg_30_0(), "fushun")
			}, arg_28_0)
	}, arg_24_1)

def var_0_0.EnterGame(arg_32_0):
	if not arg_32_0.handle:
		arg_32_0.handle = UpdateBeat.CreateListener(arg_32_0.UpdateGame, arg_32_0)

	UpdateBeat.AddListener(arg_32_0.handle)

	arg_32_0.lightTF.sizeDelta = Vector2(FushunAdventureGameConst.FUSHUN_ATTACK_RANGE, arg_32_0.lightTF.sizeDelta.y)
	arg_32_0.lightTF.localPosition = Vector2(FushunAdventureGameConst.FUSHUN_ATTACK_DISTANCE + arg_32_0.fushun.GetPosition().x, arg_32_0.lightTF.localPosition.y)

	arg_32_0.SpawnEnemys()
	arg_32_0.RegisterEventListener()

	arg_32_0.key = ""

	arg_32_0.fushun.SetOnAnimEnd(function()
		arg_32_0.key = ""

		arg_32_0.DisplayKey())

def var_0_0.UpdateGame(arg_34_0):
	if arg_34_0.state == var_0_6:
		arg_34_0.ExitGame(True)

		return

	if not arg_34_0.pause:
		arg_34_0.spawner.Update()
		arg_34_0.AddDebugInput()

		if arg_34_0.fushun.IsDeath():
			arg_34_0.fushun.Die()

			arg_34_0.state = var_0_6

			return
		elif arg_34_0.fushun.ShouldInvincible():
			arg_34_0.EnterInvincibleMode()
		elif arg_34_0.fushun.ShouldVincible():
			arg_34_0.ExitInvincibleMode()

		local var_34_0 = False

		for iter_34_0 = #arg_34_0.enemys, 1, -1:
			local var_34_1 = arg_34_0.enemys[iter_34_0]

			if var_34_1.IsFreeze():
				-- block empty
			elif arg_34_0.CheckEnemyDeath(iter_34_0):
				-- block empty
			else
				var_34_1.Move()
				arg_34_0.CheckCollision(arg_34_0.fushun, var_34_1)

				if arg_34_0.CheckAttackRange(var_34_1):
					var_34_0 = True

		arg_34_0.RangeLightDisplay(var_34_0)
		arg_34_0.DisplayeEnergy(arg_34_0.fushun.GetEnergy(), arg_34_0.fushun.GetEnergyTarget())
		arg_34_0.specailSchedule.Update()
	else
		for iter_34_1 = #arg_34_0.enemys, 1, -1:
			arg_34_0.CheckEnemyDeath(iter_34_1)

	arg_34_0.schedule.Update()

def var_0_0.RangeLightDisplay(arg_35_0, arg_35_1):
	setActive(arg_35_0.lightMark, arg_35_1)

def var_0_0.CheckAttackRange(arg_36_0, arg_36_1):
	local var_36_0 = arg_36_0.fushun

	return arg_36_1.GetPosition().x <= var_36_0.GetAttackPosition().x

def var_0_0.CheckEnemyDeath(arg_37_0, arg_37_1):
	local var_37_0 = False
	local var_37_1 = arg_37_0.enemys[arg_37_1]

	if var_37_1.IsDeath():
		if arg_37_0.hitList[var_37_1.index] and not var_37_1.IsEscape():
			arg_37_0.AddScore(var_37_1.GetScore())
			arg_37_0.AddEnergy(var_37_1.GetEnergyScore())

		var_37_1.Vanish()
		table.remove(arg_37_0.enemys, arg_37_1)

		var_37_0 = True

	return var_37_0

def var_0_0.EnterInvincibleMode(arg_38_0):
	local var_38_0 = FushunAdventureGameConst.EX_TIP_TIME
	local var_38_1 = FushunAdventureGameConst.EX_TIME

	arg_38_0.fushun.Invincible()
	setActive(arg_38_0.exTipPanel, True)

	arg_38_0.pause = True

	blinkAni(arg_38_0.energyBar.gameObject, 0.5, -1)
	arg_38_0.schedule.AddSchedule(var_38_0, 1, function()
		setActive(arg_38_0.exTipPanel, False)
		arg_38_0.spawner.CarzyMode()

		arg_38_0.pause = False

		arg_38_0.fushun.StartAction("EX")
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(FushunAdventureGameConst.ENTER_EX_VOICE)

		local var_39_0 = arg_38_0.fushun.GetEnergyTarget() / var_38_1

		arg_38_0.specailSchedule.AddSchedule(1, var_38_1, function()
			arg_38_0.fushun.ReduceEnergy(var_39_0)))
	setActive(arg_38_0.btnAExEffect, True)
	setActive(arg_38_0.btnBExEffect, True)

	arg_38_0.key = ""

	arg_38_0.DisplayKey()

def var_0_0.ExitInvincibleMode(arg_41_0):
	arg_41_0.fushun.Vincible()

	arg_41_0.energyBar.color = Color.New(1, 1, 1, 1)

	LeanTween.cancel(arg_41_0.energyBar.gameObject)

	for iter_41_0, iter_41_1 in ipairs(arg_41_0.enemys):
		arg_41_0.hitList[iter_41_1.index] = None

		iter_41_1.Die()

	arg_41_0.spawner.NormalMode()
	setActive(arg_41_0.btnAExEffect, False)
	setActive(arg_41_0.btnBExEffect, False)

def var_0_0.CheckCollision(arg_42_0, arg_42_1, arg_42_2):
	if var_0_0.IsCollision(arg_42_2.effectCollider2D, arg_42_1.collider2D):
		arg_42_1.Hurt()
		arg_42_2.OnHit()
		arg_42_0.DisplayeHearts(arg_42_0.fushun.GetHp())
		arg_42_0.AddCombo(-arg_42_0.combo)
	elif arg_42_0.fushun.InvincibleState() and not arg_42_2.IsDeath() and arg_42_2.GetPosition().x <= arg_42_1.GetAttackPosition().x:
		arg_42_2.Hurt(1)

		arg_42_0.hitList[arg_42_2.index] = True

		arg_42_0.AddHitEffect(arg_42_2)
	elif var_0_0.IsNearby(arg_42_1.GetPosition(), arg_42_2.GetAttackPosition()):
		arg_42_2.Attack()

def var_0_0.AddHitEffect(arg_43_0, arg_43_1):
	local var_43_0 = arg_43_0.fushun.effectCollider2D.bounds.center
	local var_43_1 = arg_43_0.gameUI.transform.InverseTransformPoint(var_43_0)
	local var_43_2 = arg_43_1.collider2D.bounds.GetMin()
	local var_43_3 = arg_43_0.gameUI.transform.InverseTransformPoint(var_43_2)
	local var_43_4 = Vector3(var_43_3.x, var_43_1.y, 0)

	arg_43_0.fushunLoader.GetPrefab("FushunAdventure/attack_effect", "", function(arg_44_0)
		arg_44_0.transform.SetParent(arg_43_0.gameUI.transform, False)

		arg_44_0.transform.localPosition = var_43_4

		local var_44_0 = arg_44_0.GetComponent(typeof(DftAniEvent))

		var_44_0.SetEndEvent(function()
			var_44_0.SetEndEvent(None)
			arg_43_0.fushunLoader.ReturnPrefab(arg_44_0)))
	arg_43_0.ShakeScreen(arg_43_0.gameUI)

def var_0_0.ShakeScreen(arg_46_0, arg_46_1):
	if LeanTween.isTweening(arg_46_1):
		LeanTween.cancel(arg_46_1)

	LeanTween.rotateAroundLocal(arg_46_1, Vector3(0, 0, 1), FushunAdventureGameConst.SHAKE_RANGE, FushunAdventureGameConst.SHAKE_TIME).setLoopPingPong(FushunAdventureGameConst.SHAKE_LOOP_CNT).setFrom(-1 * FushunAdventureGameConst.SHAKE_RANGE).setOnComplete(System.Action(function()
		arg_46_1.transform.localEulerAngles = Vector3(0, 0, 0)))

def var_0_0.SpawnEnemys(arg_48_0):
	local var_48_0 = {
		FushunBeastChar,
		FushunEliteBeastChar,
		FushunEliteBeastChar
	}

	local function var_48_1(arg_49_0)
		local var_49_0 = FushunAdventureGameConst.SPEED_ADDITION
		local var_49_1

		for iter_49_0, iter_49_1 in ipairs(var_49_0):
			local var_49_2 = iter_49_1[1][1]
			local var_49_3 = iter_49_1[1][2]

			if var_49_2 <= arg_49_0 and arg_49_0 <= var_49_3:
				var_49_1 = iter_49_1

				break

		var_49_1 = var_49_1 or var_49_0[#var_49_0]

		return var_49_1[2]

	local function var_48_2(arg_50_0)
		local var_50_0 = arg_50_0.config
		local var_50_1 = arg_50_0.speed
		local var_50_2 = arg_50_0.index
		local var_50_3 = var_48_0[var_50_0.id].New(arg_50_0.go, var_50_2, var_50_0, arg_48_0.fushunLoader)
		local var_50_4 = var_50_1 + var_48_1(arg_48_0.score)

		var_0_0.LOG("  顺序 .", var_50_2, " id .", var_50_0.id, " speed .", var_50_4)
		var_50_3.SetSpeed(var_50_4)
		var_50_3.SetPosition(FushunAdventureGameConst.ENEMY_SPAWN_POSITION)
		table.insert(arg_48_0.enemys, var_50_3)

	arg_48_0.spawner = FuShunEnemySpawner.New(arg_48_0.gameUI.transform.Find("game").transform, var_48_2, arg_48_0.fushunLoader)

	arg_48_0.spawner.NormalMode()

def var_0_0.AddScore(arg_51_0, arg_51_1):
	arg_51_0.AddCombo(1)

	local var_51_0 = arg_51_0.combo >= FushunAdventureGameConst.COMBO_SCORE_TARGET and FushunAdventureGameConst.COMBO_EXTRA_SCORE or 0

	arg_51_0.score = arg_51_0.score + arg_51_1 + var_51_0

	arg_51_0.DisplayScore()
	arg_51_0.spawner.UpdateScore(arg_51_0.score)

def var_0_0.AddEnergy(arg_52_0, arg_52_1):
	arg_52_0.fushun.AddEnergy(arg_52_1)

def var_0_0.AddCombo(arg_53_0, arg_53_1):
	if arg_53_1 > 0:
		arg_53_0.fushunLoader.GetPrefab("UI/fushun_combo", "", function(arg_54_0)
			if not arg_53_0.fushunLoader:
				Destroy(arg_54_0)

				return

			arg_54_0.transform.SetParent(arg_53_0.gameUI.transform.Find("UI"), False)
			Timer.New(function()
				if not arg_53_0.fushunLoader:
					return

				arg_53_0.fushunLoader.ReturnPrefab(arg_54_0), 2, 1).Start())

	arg_53_0.combo = arg_53_0.combo + arg_53_1
	arg_53_0.comboTxt.text = arg_53_0.combo

	setActive(arg_53_0.comboTxt.gameObject.transform.parent, arg_53_0.combo > 0)

def var_0_0.Action(arg_56_0, arg_56_1):
	if arg_56_0.fushun.InvincibleState():
		arg_56_0.AddScore(FushunAdventureGameConst.EX_CLICK_SCORE)
	else
		arg_56_0.OnFushunAttack(arg_56_1)

def var_0_0.OnFushunAttack(arg_57_0, arg_57_1):
	if #arg_57_0.key == 3 or arg_57_0.fushun.IsMissState() or arg_57_0.fushun.IsDamageState():
		return

	arg_57_0.key = arg_57_0.key .. arg_57_1

	arg_57_0.DisplayKey()

	local var_57_0 = {}
	local var_57_1 = arg_57_0.fushun

	for iter_57_0, iter_57_1 in ipairs(arg_57_0.enemys):
		if not iter_57_1.WillDeath() and iter_57_1.GetPosition().x <= var_57_1.GetAttackPosition().x:
			table.insert(var_57_0, iter_57_0)

	arg_57_0.fushun.TriggerAction(arg_57_0.key, function()
		if #var_57_0 == 0:
			arg_57_0.fushun.Miss()

		arg_57_0.key = ""

		arg_57_0.DisplayKey())

	if #var_57_0 > 0:
		for iter_57_2, iter_57_3 in ipairs(var_57_0):
			local var_57_2 = arg_57_0.enemys[iter_57_3]

			var_57_2.Hurt(1)

			arg_57_0.hitList[var_57_2.index] = True

			arg_57_0.AddHitEffect(var_57_2)

def var_0_0.PauseGame(arg_59_0):
	arg_59_0.pause = True

def var_0_0.ResumeGame(arg_60_0):
	arg_60_0.pause = False

def var_0_0.ExitGame(arg_61_0, arg_61_1):
	local function var_61_0()
		arg_61_0.ClearGameScene()

	if arg_61_0.btnA:
		ClearEventTrigger(arg_61_0.btnA.GetComponent("EventTriggerListener"))

	if arg_61_0.btnB:
		ClearEventTrigger(arg_61_0.btnB.GetComponent("EventTriggerListener"))

	if arg_61_0.handle:
		UpdateBeat.RemoveListener(arg_61_0.handle)

		arg_61_0.handle = None

	if arg_61_0.schedule:
		arg_61_0.schedule.Dispose()

		arg_61_0.schedule = None

	if arg_61_0.specailSchedule:
		arg_61_0.specailSchedule.Dispose()

		arg_61_0.specailSchedule = None

	if arg_61_1:
		if arg_61_0.OnShowResult:
			arg_61_0.OnShowResult(arg_61_0.score)

		arg_61_0.ShowResultWindow(function()
			var_61_0())
	else
		var_61_0()

def var_0_0.ClearGameScene(arg_64_0):
	if arg_64_0.fushun:
		arg_64_0.fushun.Destory()

		arg_64_0.fushun = None

	if arg_64_0.spawner:
		arg_64_0.spawner.Dispose()

		arg_64_0.spawner = None

	if arg_64_0.enemys:
		for iter_64_0, iter_64_1 in ipairs(arg_64_0.enemys):
			iter_64_1.Dispose()

		arg_64_0.enemys = None

	arg_64_0.state = var_0_4

	if arg_64_0.gameUI:
		arg_64_0.HideExitMsgbox()
		arg_64_0.HideResultWindow()
		arg_64_0.HidePauseMsgbox()
		setActive(arg_64_0.gameUI, False)
		pg.BgmMgr.GetInstance().Push(arg_64_0.__cname, FushunAdventureGameConst.BGM_NAME)

def var_0_0.IsStarting(arg_65_0):
	return arg_65_0.state == var_0_5

def var_0_0.Dispose(arg_66_0):
	if arg_66_0.countdownTimer:
		arg_66_0.countdownTimer.Stop()

		arg_66_0.countdownTimer = None

	arg_66_0.ExitGame()
	pg.DelegateInfo.Dispose(arg_66_0)

	if arg_66_0.gameUI:
		Destroy(arg_66_0.gameUI)

		arg_66_0.gameUI = None

	arg_66_0._go = None
	arg_66_0.btnSprites = None
	arg_66_0.state = var_0_2

	arg_66_0.fushunLoader.Clear()

	arg_66_0.fushunLoader = None
	arg_66_0.OnShowResult = None
	arg_66_0.OnLevelUpdate = None

def var_0_0.AddDebugInput(arg_67_0):
	if IsUnityEditor:
		if Input.GetKeyDown(KeyCode.A):
			arg_67_0.OnShowBtnEffect("A", True)

		if Input.GetKeyUp(KeyCode.A):
			arg_67_0.Action("A")
			arg_67_0.OnShowBtnEffect("A", False)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(FushunAdventureGameConst.A_BTN_VOICE)

		if Input.GetKeyDown(KeyCode.S):
			arg_67_0.OnShowBtnEffect("B", True)

		if Input.GetKeyUp(KeyCode.S):
			arg_67_0.Action("B")
			arg_67_0.OnShowBtnEffect("B", False)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(FushunAdventureGameConst.B_BTN_VOICE)

def var_0_0.RegisterEventListener(arg_68_0):
	local var_68_0 = arg_68_0.btnA.GetComponent("EventTriggerListener")

	var_68_0.AddPointDownFunc(function()
		arg_68_0.OnShowBtnEffect("A", True))
	var_68_0.AddPointExitFunc(function()
		arg_68_0.OnShowBtnEffect("A", False))
	var_68_0.AddPointUpFunc(function()
		if arg_68_0.pause:
			return

		arg_68_0.Action("A")
		arg_68_0.OnShowBtnEffect("A", False)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(FushunAdventureGameConst.A_BTN_VOICE))

	local var_68_1 = arg_68_0.btnB.GetComponent("EventTriggerListener")

	var_68_1.AddPointDownFunc(function()
		arg_68_0.OnShowBtnEffect("B", True))
	var_68_1.AddPointExitFunc(function()
		arg_68_0.OnShowBtnEffect("B", False))
	var_68_1.AddPointUpFunc(function()
		if arg_68_0.pause:
			return

		arg_68_0.Action("B")
		arg_68_0.OnShowBtnEffect("B", False)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(FushunAdventureGameConst.B_BTN_VOICE))
	onButton(arg_68_0, arg_68_0.pauseBtn, function()
		arg_68_0.ShowPauseMsgbox(), SFX_PANEL)
	onButton(arg_68_0, arg_68_0.exitBtn, function()
		arg_68_0.ShowExitMsgbox(), SFX_PANEL)

def var_0_0.OnShowBtnEffect(arg_77_0, arg_77_1, arg_77_2):
	setActive(arg_77_0["btn" .. arg_77_1 .. "Effect"], arg_77_2)

def var_0_0.ShowResultWindow(arg_78_0, arg_78_1):
	setActive(arg_78_0.resultPanel, True)
	onButton(arg_78_0, arg_78_0.resultCloseBtn, function()
		arg_78_0.HideResultWindow()

		if arg_78_1:
			arg_78_1(), SFX_PANEL)

	arg_78_0.resultHighestScoreTxt.text = arg_78_0.highestScore
	arg_78_0.resultScoreTxt.text = arg_78_0.score

	if arg_78_0.score > arg_78_0.highestScore:
		arg_78_0.highestScore = arg_78_0.score

def var_0_0.HideResultWindow(arg_80_0):
	setActive(arg_80_0.resultPanel, False)

def var_0_0.ShowPauseMsgbox(arg_81_0):
	arg_81_0.PauseGame()
	setActive(arg_81_0.msgboxPanel, True)
	setActive(arg_81_0.pauseMsgboxWindow, True)
	setActive(arg_81_0.exitMsgboxWindow, False)
	onButton(arg_81_0, arg_81_0.pauseMsgboxWindow.Find("continue_btn"), function()
		arg_81_0.ResumeGame()
		arg_81_0.HidePauseMsgbox(), SFX_PANEL)

def var_0_0.HidePauseMsgbox(arg_83_0):
	setActive(arg_83_0.msgboxPanel, False)
	setActive(arg_83_0.pauseMsgboxWindow, False)

def var_0_0.ShowExitMsgbox(arg_84_0):
	arg_84_0.PauseGame()
	setActive(arg_84_0.msgboxPanel, True)
	setActive(arg_84_0.pauseMsgboxWindow, False)
	setActive(arg_84_0.exitMsgboxWindow, True)
	onButton(arg_84_0, arg_84_0.exitMsgboxWindow.Find("cancel_btn"), function()
		arg_84_0.ResumeGame()
		arg_84_0.HideExitMsgbox(), SFX_PANEL)
	onButton(arg_84_0, arg_84_0.exitMsgboxWindow.Find("confirm_btn"), function()
		arg_84_0.HideExitMsgbox()

		if arg_84_0.OnShowResult:
			arg_84_0.OnShowResult(arg_84_0.score)

		arg_84_0.ExitGame(), SFX_PANEL)

def var_0_0.HideExitMsgbox(arg_87_0):
	setActive(arg_87_0.msgboxPanel, False)
	setActive(arg_87_0.exitMsgboxWindow, False)

def var_0_0.IsCollision(arg_88_0, arg_88_1):
	return arg_88_0.enabled and arg_88_1.enabled and arg_88_0.gameObject.activeSelf and arg_88_0.bounds.Intersects(arg_88_1.bounds)

def var_0_0.IsNearby(arg_89_0, arg_89_1):
	return arg_89_1.x - arg_89_0.x <= 0

def var_0_0.LOG(...):
	if var_0_1:
		print(...)

return var_0_0
