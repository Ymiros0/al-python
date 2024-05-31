local var_0_0 = class("PileGameView")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.controller = arg_1_1

def var_0_0.SetUI(arg_2_0, arg_2_1):
	pg.DelegateInfo.New(arg_2_0)

	arg_2_0._go = arg_2_1
	arg_2_0._tf = tf(arg_2_1)
	arg_2_0.bg = arg_2_0._tf.Find("AD")
	arg_2_0.curtainTF = arg_2_0._tf.Find("AD/curtain")
	arg_2_0.countDown = arg_2_0.curtainTF.Find("Text").GetComponent(typeof(Text))
	arg_2_0.itemTpl = arg_2_0._tf.Find("AD/item")
	arg_2_0.groundTpl = arg_2_0._tf.Find("AD/ground")
	arg_2_0.gameContainer = arg_2_0._tf.Find("AD/game")
	arg_2_0.itemsContainer = arg_2_0._tf.Find("AD/game/items")
	arg_2_0.scoreTxt = arg_2_0._tf.Find("AD/score_panel/Text").GetComponent(typeof(Text))
	arg_2_0.heats = {
		arg_2_0._tf.Find("AD/score_panel/heart1"),
		arg_2_0._tf.Find("AD/score_panel/heart2"),
		arg_2_0._tf.Find("AD/score_panel/heart3")
	}
	arg_2_0.manjuuAnim = arg_2_0._tf.Find("AD/npc/manjuu").GetComponent(typeof(Animator))
	arg_2_0.anikiAnim = arg_2_0._tf.Find("AD/npc/aniki").GetComponent(typeof(Animator))
	arg_2_0.manjuuPilot = arg_2_0._tf.Find("AD/npc/manjuu_pilot")
	arg_2_0.backBtn = arg_2_0._tf.Find("AD/back")
	arg_2_0.exitPanel = arg_2_0._tf.Find("AD/exit_panel")
	arg_2_0.exitPanelConfirmBtn = arg_2_0.exitPanel.Find("frame/confirm")
	arg_2_0.exitPanelCancelBtn = arg_2_0.exitPanel.Find("frame/cancel")
	arg_2_0.resultPanel = arg_2_0._tf.Find("AD/result")
	arg_2_0.endGameBtn = arg_2_0.resultPanel.Find("frame/endGame")
	arg_2_0.finalScoreTxt = arg_2_0.resultPanel.Find("frame/score/Text").GetComponent(typeof(Text))
	arg_2_0.highestScoreText = arg_2_0.resultPanel.Find("frame/highestscore/Text").GetComponent(typeof(Text))
	arg_2_0.itemIndexTF = arg_2_0._tf.Find("AD/score_panel/index/target")
	arg_2_0.overviewPanel = arg_2_0._tf.Find("overview")
	arg_2_0.startBtn = arg_2_0._tf.Find("overview/start")
	arg_2_0.helpBtn = arg_2_0._tf.Find("overview/help")
	arg_2_0.deathLine = arg_2_0._tf.Find("death_line")
	arg_2_0.safeLine = arg_2_0._tf.Find("safe_line")
	arg_2_0.itemCollider = arg_2_0._tf.Find("item_collider")
	arg_2_0.items = {}
	arg_2_0.bgMgr = PileGameBgMgr.New(arg_2_0._tf.Find("AD/bgs"))

def var_0_0.OnEnterGame(arg_3_0, arg_3_1):
	arg_3_0.viewData = arg_3_1
	arg_3_0.gameHelpTip = arg_3_0.viewData.tip and arg_3_0.viewData.tip or None

	setActive(arg_3_0.overviewPanel, True)
	setActive(arg_3_0.bg, False)
	onButton(arg_3_0, arg_3_0.startBtn, function()
		arg_3_0.controller.StartGame(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = arg_3_0.gameHelpTip or pg.gametip.pile_game_notice.tip
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.backBtn, function()
		arg_3_0.ShowExitMsg(), SFX_PANEL)

def var_0_0.ShowExitMsg(arg_7_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_7_0.exitPanel)
	setActive(arg_7_0.exitPanel, True)

	local function var_7_0()
		setActive(arg_7_0.exitPanel, False)
		pg.UIMgr.GetInstance().UnblurPanel(arg_7_0.exitPanel, arg_7_0.bg)

	onButton(arg_7_0, arg_7_0.exitPanelCancelBtn, var_7_0, SFX_PANEL)
	onButton(arg_7_0, arg_7_0.exitPanelConfirmBtn, function()
		var_7_0()
		arg_7_0.controller.OnEndGame(False), SFX_PANEL)

def var_0_0.DoCurtain(arg_10_0, arg_10_1):
	seriesAsync({
		function(arg_11_0)
			arg_10_0.bgMgr.Init(arg_11_0),
		function(arg_12_0)
			setActive(arg_10_0.overviewPanel, False)
			setActive(arg_10_0.bg, True)
			setActive(arg_10_0.curtainTF, True)
			setAnchoredPosition(arg_10_0.anikiAnim.gameObject, {
				x = -177,
				y = 158
			})

			local var_12_0 = 4

			arg_10_0.timer = Timer.New(function()
				var_12_0 = var_12_0 - 1

				if var_12_0 == 3:
					pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_STEP_PILE_COUNTDOWN)

				arg_10_0.countDown.text = var_12_0

				if var_12_0 == 0:
					setActive(arg_10_0.curtainTF, False)
					arg_12_0(), 1, 4)

			arg_10_0.timer.Start()
			arg_10_0.timer.func()
	}, arg_10_1)

def var_0_0.UpdateScore(arg_14_0, arg_14_1, arg_14_2):
	arg_14_0.scoreTxt.text = arg_14_1

	local var_14_0 = False

	if arg_14_1 > 0 and arg_14_1 % PileGameConst.LEVEL_TO_HAPPY_ANIM == 0:
		arg_14_0.manjuuAnim.SetTrigger("happy")
		arg_14_0.anikiAnim.SetTrigger("nice")

		var_14_0 = True

	local var_14_1 = arg_14_0.items[arg_14_2]

	if var_14_1 and var_14_0:
		var_14_1.Find("anim").GetComponent(typeof(Animator)).SetTrigger("win")
	elif var_14_1:
		var_14_1.Find("anim").GetComponent(typeof(Animator)).SetTrigger("idle")

	if arg_14_2:
		local var_14_2 = arg_14_2.position.x

		arg_14_0.itemIndexTF.localPosition = Vector3(var_14_2 / PileGameConst.RATIO, 0, 0)

		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_STEP_PILE_SUCCESS)

def var_0_0.UpdateFailedCnt(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4):
	for iter_15_0, iter_15_1 in ipairs(arg_15_0.heats):
		setActive(iter_15_1, arg_15_2 < iter_15_0)

	if arg_15_3:
		arg_15_0.anikiAnim.SetTrigger("miss")
		arg_15_0.items[arg_15_4].Find("anim").GetComponent(typeof(Animator)).SetTrigger("miss")

def var_0_0.AddPile(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	local function var_16_0(arg_17_0)
		local var_17_0 = tf(arg_17_0)

		SetParent(var_17_0, arg_16_0.itemsContainer)

		var_17_0.sizeDelta = arg_16_1.sizeDelta
		var_17_0.pivot = arg_16_1.pivot
		go(var_17_0).name = arg_16_1.name .. "_" .. arg_16_1.gname
		arg_16_0.items[arg_16_1] = var_17_0
		var_17_0.eulerAngles = Vector3(0, 0, 0)

		arg_16_0.OnItemPositionChange(arg_16_1)
		setActive(var_17_0, not arg_16_2)

		if not arg_16_2:
			var_17_0.Find("anim").GetComponent(typeof(Animator)).SetTrigger("exit")

		if PileGameConst.DEBUG:
			arg_16_0.AddPileCollider(arg_16_1)

		arg_16_3()

	PoolMgr.GetInstance().GetPrefab("Stacks/" .. arg_16_1.gname, arg_16_1.gname, True, var_16_0)

def var_0_0.OnStartDrop(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	if arg_18_3:
		arg_18_0.manjuuAnim.SetBool("despair", PileGameController.DROP_AREA_WARN == arg_18_2)
	else
		arg_18_0.manjuuAnim.SetTrigger("shock")

	arg_18_0.items[arg_18_1].Find("anim").GetComponent(typeof(Animator)).SetTrigger("drop")

def var_0_0.OnItemPositionChange(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_0.items[arg_19_1]

	if var_19_0:
		var_19_0.localPosition = arg_19_1.position

def var_0_0.OnItemPositionChangeWithAnim(arg_20_0, arg_20_1, arg_20_2):
	local var_20_0 = arg_20_0.items[arg_20_1]

	if var_20_0:
		LeanTween.moveLocalY(go(var_20_0), arg_20_1.position.y, PileGameConst.SINK_TIME).setOnComplete(System.Action(arg_20_2))

def var_0_0.OnItemIndexPositionChange(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_1.position.x
	local var_21_1 = arg_21_1.position.y

	arg_21_0.prevPosition = arg_21_0.prevPosition or arg_21_0.manjuuPilot.localPosition.x

	local var_21_2 = 0
	local var_21_3 = 1

	if var_21_0 - arg_21_0.prevPosition <= 0:
		var_21_2 = var_21_0 + 140
		var_21_3 = -1
	else
		var_21_2 = var_21_0 - 140

	local var_21_4 = var_21_1 + arg_21_1.sizeDelta.y + arg_21_0.manjuuPilot.rect.height / 2

	arg_21_0.manjuuPilot.localPosition = Vector3(var_21_2, var_21_4, 0)
	arg_21_0.manjuuPilot.localScale = Vector3(var_21_3, 1, 1)
	arg_21_0.prevPosition = var_21_0

def var_0_0.OnExceedingTheHighestScore(arg_22_0):
	arg_22_0.manjuuAnim.SetTrigger("satisfied")

def var_0_0.DoSink(arg_23_0, arg_23_1, arg_23_2):
	local var_23_0 = getAnchoredPosition(arg_23_0.anikiAnim.gameObject)

	LeanTween.value(arg_23_0.anikiAnim.gameObject, var_23_0.y, var_23_0.y - arg_23_1, PileGameConst.SINK_TIME).setOnUpdate(System.Action_float(function(arg_24_0)
		setAnchoredPosition(arg_23_0.anikiAnim.gameObject, {
			y = arg_24_0
		}))).setOnComplete(System.Action(arg_23_2))
	arg_23_0.bgMgr.DoMove(arg_23_1)

def var_0_0.OnRemovePile(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_0.items[arg_25_1]

	if var_25_0:
		if PileGameConst.DEBUG:
			Destroy(var_25_0.Find("collider").gameObject)

		var_25_0.Find("anim").GetComponent(typeof(Animator)).SetTrigger("exit")

		var_25_0.eulerAngles = Vector3(0, 0, 0)

		PoolMgr.GetInstance().ReturnPrefab("Stacks/" .. arg_25_1.gname, arg_25_1.gname, var_25_0.gameObject)

		arg_25_0.items[arg_25_1] = None

def var_0_0.PlaySpeAction(arg_26_0, arg_26_1):
	local var_26_0 = arg_26_0.items[arg_26_1]

	if var_26_0:
		local var_26_1 = arg_26_1.speActionCount

		if var_26_1 == 0:
			return

		local var_26_2 = math.random(1, var_26_1) - 1
		local var_26_3 = var_26_2 == 0 and "spe" or "spe" .. var_26_2

		var_26_0.Find("anim").GetComponent(typeof(Animator)).SetTrigger(var_26_3)

def var_0_0.OnGameStart(arg_27_0):
	onButton(arg_27_0, arg_27_0.bg, function()
		arg_27_0.controller.Drop(), SFX_PANEL)

def var_0_0.OnGameExited(arg_29_0):
	setActive(arg_29_0.overviewPanel, True)
	setActive(arg_29_0.bg, False)

	arg_29_0.itemsContainer.eulerAngles = Vector3(0, 0, 0)
	arg_29_0.itemsContainer.pivot = Vector2(0.5, 0.5)

	arg_29_0.bgMgr.Clear()

	if PileGameConst.DEBUG:
		Destroy(arg_29_0.gameContainer.Find("ground").gameObject)
		Destroy(arg_29_0.gameContainer.Find("deathLineR").gameObject)
		Destroy(arg_29_0.gameContainer.Find("deathLineL").gameObject)
		Destroy(arg_29_0.gameContainer.Find("safeLineL").gameObject)
		Destroy(arg_29_0.gameContainer.Find("safeLineR").gameObject)

def var_0_0.OnGameEnd(arg_30_0, arg_30_1, arg_30_2):
	(function()
		pg.UIMgr.GetInstance().BlurPanel(arg_30_0.resultPanel)
		setActive(arg_30_0.resultPanel, True)
		onButton(arg_30_0, arg_30_0.endGameBtn, function()
			setActive(arg_30_0.resultPanel, False)
			pg.UIMgr.GetInstance().UnblurPanel(arg_30_0.resultPanel, arg_30_0.bg)
			arg_30_0.controller.ExitGame())

		arg_30_0.finalScoreTxt.text = arg_30_1
		arg_30_0.highestScoreText.text = arg_30_2)()

def var_0_0.OnShake(arg_33_0, arg_33_1):
	local var_33_0 = getAnchoredPosition(arg_33_0.anikiAnim)

	setAnchoredPosition(arg_33_0.anikiAnim, {
		x = var_33_0.x + arg_33_1
	})

def var_0_0.OnCollapse(arg_34_0, arg_34_1, arg_34_2, arg_34_3):
	local function var_34_0(arg_35_0, arg_35_1, arg_35_2, arg_35_3)
		LeanTween.value(go(arg_34_0.itemsContainer), arg_35_0, arg_35_1, arg_35_2).setOnUpdate(System.Action_float(function(arg_36_0)
			arg_34_0.itemsContainer.eulerAngles = Vector3(0, 0, arg_36_0))).setOnComplete(System.Action(arg_35_3))

	seriesAsync({
		function(arg_37_0)
			arg_34_0.manjuuAnim.SetTrigger("shock")

			local var_37_0 = 0.5 + arg_34_1 / arg_34_0.itemsContainer.rect.width

			arg_34_0.itemsContainer.pivot = Vector2(var_37_0, 0)

			local var_37_1 = arg_34_2 == 1 and -35 or 35

			var_34_0(0, var_37_1, 0.5, function()
				arg_37_0(var_37_1)),
		function(arg_39_0, arg_39_1)
			local var_39_0 = {}
			local var_39_1 = _.values(arg_34_0.items)

			table.sort(var_39_1, function(arg_40_0, arg_40_1)
				return arg_40_0.localPosition.y < arg_40_1.localPosition.y)

			for iter_39_0, iter_39_1 in ipairs(var_39_1):
				table.insert(var_39_0, function(arg_41_0)
					local var_41_0 = arg_34_2 == 1 and -90 or 90

					parallelAsync({
						function(arg_42_0)
							var_34_0(arg_39_1, var_41_0, 1, arg_42_0),
						function(arg_43_0)
							local var_43_0 = arg_34_2 == 1 and -356 or 356

							LeanTween.value(go(iter_39_1), 0, var_43_0, 1).setOnUpdate(System.Action_float(function(arg_44_0)
								iter_39_1.eulerAngles = Vector3(0, 0, arg_44_0))).setOnComplete(System.Action(arg_43_0)),
						function(arg_45_0)
							LeanTween.moveLocalY(go(iter_39_1), iter_39_1.localPosition.y + 50 * iter_39_0, 1).setOnComplete(System.Action(arg_45_0))
					}, arg_41_0))

			parallelAsync(var_39_0, arg_39_0)
	}, arg_34_3)

def var_0_0.InitSup(arg_46_0, arg_46_1):
	if PileGameConst.DEBUG:
		local var_46_0 = arg_46_1.ground
		local var_46_1 = cloneTplTo(arg_46_0.groundTpl, arg_46_0.gameContainer, "ground")

		var_46_1.sizeDelta = var_46_0.sizeDelta
		var_46_1.pivot = var_46_0.pivot
		var_46_1.localPosition = var_46_0.position
		cloneTplTo(arg_46_0.deathLine, arg_46_0.gameContainer, "deathLineR").localPosition = Vector3(arg_46_1.deathLine.y, 0, 0)
		cloneTplTo(arg_46_0.deathLine, arg_46_0.gameContainer, "deathLineL").localPosition = Vector3(arg_46_1.deathLine.x, 0, 0)
		cloneTplTo(arg_46_0.safeLine, arg_46_0.gameContainer, "safeLineL").localPosition = Vector3(arg_46_1.safeLine.x, 0, 0)
		cloneTplTo(arg_46_0.safeLine, arg_46_0.gameContainer, "safeLineR").localPosition = Vector3(arg_46_1.safeLine.y, 0, 0)

def var_0_0.AddPileCollider(arg_47_0, arg_47_1):
	local var_47_0 = arg_47_0.items[arg_47_1]
	local var_47_1 = cloneTplTo(arg_47_0.itemCollider, var_47_0, "collider")
	local var_47_2 = arg_47_1.collider
	local var_47_3 = (0.5 - arg_47_1.pivot.x) * arg_47_1.sizeDelta.x + var_47_2.offset.x
	local var_47_4 = (0.5 - arg_47_1.pivot.y) * arg_47_1.sizeDelta.y + var_47_2.offset.y

	var_47_1.localPosition = Vector3(var_47_3, var_47_4, 0)
	var_47_1.sizeDelta = var_47_2.sizeDelta

def var_0_0.onBackPressed(arg_48_0):
	if isActive(arg_48_0.resultPanel):
		setActive(arg_48_0.resultPanel, False)
		pg.UIMgr.GetInstance().UnblurPanel(arg_48_0.resultPanel, arg_48_0.bg)
		arg_48_0.controller.ExitGame()

		return True
	elif isActive(arg_48_0.exitPanel):
		setActive(arg_48_0.exitPanel, False)
		pg.UIMgr.GetInstance().UnblurPanel(arg_48_0.exitPanel, arg_48_0.bg)

		return True
	elif isActive(arg_48_0.bg):
		arg_48_0.controller.ExitGame()

		if arg_48_0.timer:
			arg_48_0.timer.Stop()

			arg_48_0.timer = None

		return True

	return False

def var_0_0.Dispose(arg_49_0):
	pg.DelegateInfo.Dispose(arg_49_0)

	if arg_49_0.timer:
		arg_49_0.timer.Stop()

		arg_49_0.timer = None

	arg_49_0.bgMgr.Clear()

return var_0_0
