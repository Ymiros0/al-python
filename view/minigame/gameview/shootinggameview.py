local var_0_0 = class("ShootingGameView", import("..BaseMiniGameView"))

var_0_0.animTime = 0.3333333333333333
var_0_0.moveModulus = 120

def var_0_0.getUIName(arg_1_0):
	return "ShootingGameUI"

def var_0_0.init(arg_2_0):
	arg_2_0.uiMGR = pg.UIMgr.GetInstance()
	arg_2_0.blurPanel = arg_2_0._tf.Find("noAdaptPanel/blur_panel")
	arg_2_0.top = arg_2_0.blurPanel.Find("top")
	arg_2_0.backBtn = arg_2_0.top.Find("back")
	arg_2_0.scoreTF = arg_2_0.top.Find("score/Text")

	setText(arg_2_0.scoreTF, 0)

	arg_2_0.bestScoreTF = arg_2_0.top.Find("score_heightest/Text")
	arg_2_0.ticketTF = arg_2_0.top.Find("ticket/Text")
	arg_2_0.helpBtn = arg_2_0.top.Find("help_btn")
	arg_2_0.sightTF = arg_2_0.blurPanel.Find("MoveArea/Sight")

	setActive(arg_2_0.sightTF, False)

	arg_2_0.corners = arg_2_0.blurPanel.Find("Corners")
	arg_2_0.shootAreaTF = arg_2_0._tf.Find("noAdaptPanel/ShootArea")
	arg_2_0.targetPanel = arg_2_0.shootAreaTF.Find("target_panel")
	arg_2_0.targetTpl = {}

	local var_2_0 = arg_2_0.shootAreaTF.Find("tpl")

	for iter_2_0 = 1, var_2_0.childCount:
		arg_2_0.targetTpl[iter_2_0] = var_2_0.GetChild(iter_2_0 - 1)

	setActive(var_2_0, False)

	arg_2_0.startMaskTF = arg_2_0.shootAreaTF.Find("start_mask")
	arg_2_0.countdownTF = arg_2_0.startMaskTF.Find("count")
	arg_2_0.lastTimeTF = arg_2_0.shootAreaTF.Find("time_word")
	arg_2_0.bottomTF = arg_2_0._tf.Find("noAdaptPanel/bottom")
	arg_2_0.joyStrickTF = arg_2_0.bottomTF.Find("Stick")
	arg_2_0.fireBtn = arg_2_0.bottomTF.Find("fire/ActCtl")
	arg_2_0.fireBtnDelegate = GetOrAddComponent(arg_2_0.fireBtn, "EventTriggerListener")

	setActive(arg_2_0.fireBtn.Find("block"), False)

	arg_2_0.resultPanel = arg_2_0._tf.Find("result_panel")

	setActive(arg_2_0.resultPanel, False)

def var_0_0.initData(arg_3_0):
	arg_3_0.tempConfig = arg_3_0.GetMGData().getConfig("simple_config_data")
	arg_3_0.tempConfig.waitCountdown = 3
	arg_3_0.tempConfig.half = 56

def var_0_0.addTimer(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	arg_4_0.timerList = arg_4_0.timerList or {}

	assert(arg_4_0.timerList[arg_4_1] == None, "error Timers")
	assert(arg_4_2 > 0, "duration must >0")

	arg_4_0.timerList[arg_4_1] = {
		timeMark = Time.realtimeSinceStartup + arg_4_2,
		func = arg_4_3
	}

def var_0_0.updateTimers(arg_5_0):
	local var_5_0 = Time.realtimeSinceStartup

	for iter_5_0, iter_5_1 in pairs(arg_5_0.timerList):
		if var_5_0 > iter_5_1.timeMark:
			local var_5_1 = iter_5_1.func

			arg_5_0.timerList[iter_5_0] = None

			var_5_1()

def var_0_0.stopTimers(arg_6_0):
	arg_6_0.isStopped = True

	local var_6_0 = Time.realtimeSinceStartup

	for iter_6_0, iter_6_1 in pairs(arg_6_0.timerList):
		iter_6_1.timeMark = iter_6_1.timeMark - var_6_0

def var_0_0.restartTimers(arg_7_0):
	arg_7_0.isStopped = False

	local var_7_0 = Time.realtimeSinceStartup

	for iter_7_0, iter_7_1 in pairs(arg_7_0.timerList):
		iter_7_1.timeMark = iter_7_1.timeMark + var_7_0

def var_0_0.clearTimers(arg_8_0):
	arg_8_0.timerList = {}

def var_0_0.didEnter(arg_9_0):
	onButton(arg_9_0, arg_9_0.backBtn, function()
		if arg_9_0.isPlaying:
			arg_9_0.stopTimers()
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("tips_summergame_exit"),
				def onYes:()
					arg_9_0.gameFinish(True)
					arg_9_0.closeView(),
				def onNo:()
					arg_9_0.restartTimers()
			})
		else
			arg_9_0.closeView())
	onButton(arg_9_0, arg_9_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_summer_shooting.tip
		}), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.startMaskTF, function()
		if not arg_9_0.isPlaying:
			arg_9_0.gameStart())
	arg_9_0.initData()
	arg_9_0.updateCount()
	arg_9_0.resetTime()
	arg_9_0.initFireFunc()
	arg_9_0.setFireLink(False)
	setActive(arg_9_0.startMaskTF, True)

def var_0_0.onBackPressed(arg_15_0):
	triggerButton(arg_15_0.backBtn)

local function var_0_1(arg_16_0, arg_16_1)
	return Vector2(math.clamp(arg_16_0.x, -arg_16_1.x, arg_16_1.x), math.clamp(arg_16_0.y, -arg_16_1.y, arg_16_1.y))

def var_0_0.update(arg_17_0):
	local var_17_0 = Time.GetTimestamp()

	if not arg_17_0.isStopped:
		if arg_17_0.isAfterCount and arg_17_0.sightTimeMark:
			if not arg_17_0.moveRect:
				local var_17_1 = tf(arg_17_0.sightTF.parent)

				arg_17_0.moveRect = Vector2(var_17_1.rect.width - arg_17_0.sightTF.rect.width, var_17_1.rect.height - arg_17_0.sightTF.rect.height) / 2

			local var_17_2 = Vector2(arg_17_0.uiMGR.hrz, arg_17_0.uiMGR.vtc) * arg_17_0.tempConfig.moveSpeed * (var_17_0 - arg_17_0.sightTimeMark) * var_0_0.moveModulus

			arg_17_0.sightTF.anchoredPosition = var_0_1(arg_17_0.sightTF.anchoredPosition + var_17_2 * (arg_17_0.isDown and 0.5 or 1), arg_17_0.moveRect)

		arg_17_0.updateTimers()

	arg_17_0.sightTimeMark = var_17_0

def var_0_0.resetTime(arg_18_0):
	arg_18_0.countdown = arg_18_0.tempConfig.waitCountdown

	setText(arg_18_0.countdownTF, arg_18_0.countdown)

	arg_18_0.lastTime = arg_18_0.tempConfig.baseTime

	setText(arg_18_0.lastTimeTF, arg_18_0.lastTime)

def var_0_0.gameStart(arg_19_0):
	arg_19_0.isPlaying = True

	UpdateBeat.Add(arg_19_0.update, arg_19_0)
	setActive(arg_19_0.countdownTF, True)
	setActive(arg_19_0.startMaskTF.Find("word"), False)

	local function var_19_0(arg_20_0)
		arg_19_0.addTimer("start countdown", 1, function()
			arg_19_0.countdown = arg_19_0.countdown - 1

			setText(arg_19_0.countdownTF, arg_19_0.countdown)

			if arg_19_0.countdown > 0:
				arg_20_0(arg_20_0)
			else
				arg_19_0.afterCountDown())

	var_19_0(var_19_0)

def var_0_0.afterCountDown(arg_22_0):
	arg_22_0.isAfterCount = True

	arg_22_0.uiMGR.AttachStickOb(arg_22_0.joyStrickTF)
	setActive(arg_22_0.sightTF, True)
	setAnchoredPosition(arg_22_0.sightTF, Vector2.zero)
	arg_22_0.setFireLink(True)
	setActive(arg_22_0.startMaskTF, False)

	arg_22_0.score = 0

	arg_22_0.flushTarget(True)

	local function var_22_0(arg_23_0)
		arg_22_0.addTimer("gamefinish", 1, function()
			arg_22_0.lastTime = arg_22_0.lastTime - 1

			setText(arg_22_0.lastTimeTF, arg_22_0.lastTime)

			if arg_22_0.lastTime > 0:
				arg_23_0(arg_23_0)
			else
				arg_22_0.gameFinish())

	var_22_0(var_22_0)

def var_0_0.gameFinish(arg_25_0, arg_25_1):
	if arg_25_0.isAfterCount:
		arg_25_0.setFireLink(False)
		arg_25_0.uiMGR.ClearStick()

		arg_25_0.isAfterCount = False

	arg_25_0.clearTimers()
	UpdateBeat.Remove(arg_25_0.update, arg_25_0)
	setActive(arg_25_0.sightTF, False)
	setActive(arg_25_0.countdownTF, False)
	arg_25_0.resetTime()

	arg_25_0.isPlaying = False

	if not arg_25_1:
		for iter_25_0 = 1, 3:
			for iter_25_1 = 1, 6:
				if arg_25_0.cell[iter_25_0][iter_25_1]:
					arg_25_0.targetPanel.Find("line_" .. iter_25_0).GetChild(iter_25_1 - 1).GetChild(0).GetComponent(typeof(Animator)).Play("targetDown")

		Timer.New(function()
			setActive(arg_25_0.startMaskTF, True)
			setActive(arg_25_0.startMaskTF.Find("word"), True), var_0_0.animTime).Start()
		arg_25_0.resultFinish()

def var_0_0.resultFinish(arg_27_0):
	local var_27_0 = arg_27_0.tempConfig.score_level
	local var_27_1

	for iter_27_0 = 1, #var_27_0:
		if arg_27_0.score >= var_27_0[#var_27_0 - iter_27_0 + 1]:
			var_27_1 = iter_27_0

			break

	arg_27_0.awardLevel = var_27_1

	if arg_27_0.GetMGHubData().count > 0:
		arg_27_0.SendSuccess(var_27_1)
	else
		arg_27_0.showResultPanel({})

def var_0_0.showResultPanel(arg_28_0, arg_28_1, arg_28_2):
	local function var_28_0()
		setActive(arg_28_0.resultPanel, False)

		if arg_28_2:
			arg_28_2()
		else
			arg_28_0.updateCount()

	onButton(arg_28_0, arg_28_0.resultPanel.Find("bg"), var_28_0)
	onButton(arg_28_0, arg_28_0.resultPanel.Find("main/btn_confirm"), var_28_0)

	local var_28_1 = arg_28_0.resultPanel.Find("main")

	if arg_28_0.score > arg_28_0.bestScore:
		arg_28_0.StoreDataToServer({
			arg_28_0.score
		})
		GetImageSpriteFromAtlasAsync("ui/minigameui/shootinggameui_atlas", "new_recode", var_28_1.Find("success"), True)
	else
		GetImageSpriteFromAtlasAsync("ui/minigameui/shootinggameui_atlas", "success", var_28_1.Find("success"), True)

	GetImageSpriteFromAtlasAsync("ui/minigameui/shootinggameui_atlas", "level_" .. #arg_28_0.tempConfig.score_level - arg_28_0.awardLevel + 1, var_28_1.Find("success/level"), True)
	setText(var_28_1.Find("right/score/number"), arg_28_0.score)
	setActive(var_28_1.Find("right/awards/list"), #arg_28_1 > 0)
	setActive(var_28_1.Find("right/awards/nothing"), #arg_28_1 == 0)

	arg_28_0.itemList = arg_28_0.itemList or UIItemList.New(var_28_1.Find("right/awards/list"), var_28_1.Find("right/awards/list/item"))

	arg_28_0.itemList.make(function(arg_30_0, arg_30_1, arg_30_2)
		if arg_30_0 == UIItemList.EventUpdate:
			updateDrop(arg_30_2, arg_28_1[arg_30_1 + 1])
			setText(arg_30_2.Find("number"), "x" .. arg_28_1[arg_30_1 + 1].count))
	arg_28_0.itemList.align(#arg_28_1)
	setActive(arg_28_0.resultPanel, True)

def var_0_0.updateAfterFinish(arg_31_0):
	local var_31_0 = (getProxy(MiniGameProxy).GetMiniGameData(MiniGameDataCreator.ShrineGameID).GetRuntimeData("count") or 0) + 1

	pg.m02.sendNotification(GAME.MODIFY_MINI_GAME_DATA, {
		id = MiniGameDataCreator.ShrineGameID,
		map = {
			count = var_31_0
		}
	})

def var_0_0.OnGetAwardDone(arg_32_0, arg_32_1):
	if arg_32_1.cmd == MiniGameOPCommand.CMD_COMPLETE:
		local var_32_0 = arg_32_0.GetMGHubData()

		if var_32_0.ultimate == 0 and var_32_0.usedtime >= var_32_0.getConfig("reward_need"):
			pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
				hubid = var_32_0.id,
				cmd = MiniGameOPCommand.CMD_ULTIMATE,
				args1 = {}
			})
	elif arg_32_1.cmd == MiniGameOPCommand.CMD_ULTIMATE:
		pg.NewStoryMgr.GetInstance().Play("TIANHOUYUYI2")

def var_0_0.OnSendMiniGameOPDone(arg_33_0, arg_33_1):
	arg_33_0.updateCount()

def var_0_0.updateCount(arg_34_0):
	setText(arg_34_0.ticketTF, arg_34_0.GetMGHubData().count)

	arg_34_0.bestScore = checkExist(arg_34_0.GetMGData().GetRuntimeData("elements"), {
		1
	}) or 0

	setText(arg_34_0.bestScoreTF, arg_34_0.bestScore)

def var_0_0.initFireFunc(arg_35_0):
	local var_35_0 = pg.TipsMgr.GetInstance()
	local var_35_1 = pg.TimeMgr.GetInstance()
	local var_35_2 = arg_35_0.sightTF.Find("sight_base")
	local var_35_3 = arg_35_0.sightTF.Find("sight_ready")

	setImageAlpha(var_35_2, 1)
	setImageAlpha(var_35_3, 0)

	local function var_35_4()
		setActive(arg_35_0.corners, True)
		LeanTween.scale(var_35_2, Vector3(1.95, 1.95, 1), 0.1).setOnComplete(System.Action(function()
			LeanTween.alpha(var_35_2, 0, 0.1)
			LeanTween.alpha(var_35_3, 1, 0.1)))

	local function var_35_5()
		setActive(arg_35_0.corners, False)
		LeanTween.alpha(var_35_2, 1, 0.1)
		LeanTween.alpha(var_35_3, 0, 0.1).setOnComplete(System.Action(function()
			LeanTween.scale(var_35_2, Vector3.one, 0.1)))

	function arg_35_0._downFunc()
		var_35_4()

	function arg_35_0._upFunc()
		LeanTween.scale(var_35_3, Vector3(2, 2, 2), 0.03).setOnComplete(System.Action(function()
			LeanTween.scale(var_35_3, Vector3.one, 0.07).setOnComplete(System.Action(function()
				var_35_5()))))

		local var_41_0, var_41_1, var_41_2 = arg_35_0.checkHit()

		if var_41_0:
			local var_41_3 = arg_35_0.cell[var_41_1][var_41_2]

			arg_35_0.cell[var_41_1][var_41_2] = None
			arg_35_0.score = arg_35_0.score + arg_35_0.tempConfig.targetScore[var_41_3]
			arg_35_0.targetCount[var_41_3] = arg_35_0.targetCount[var_41_3] - 1
			arg_35_0.lastTime = arg_35_0.lastTime + arg_35_0.tempConfig.bonusTime

			setText(arg_35_0.lastTimeTF, arg_35_0.lastTime)
			arg_35_0.targetPanel.Find("line_" .. var_41_1).GetChild(var_41_2 - 1).GetChild(0).GetComponent(typeof(Animator)).Play("targetDown")
			arg_35_0.addTimer("flush call", 0.2 + var_0_0.animTime, function()
				arg_35_0.flushTarget())

			if not _.any(arg_35_0.targetCount, function(arg_45_0)
				return arg_45_0 > 0):
				arg_35_0.gameFinish()

		arg_35_0.setFireLink(False)
		arg_35_0.addTimer("fire cd", arg_35_0.tempConfig.fireCD, function()
			arg_35_0.setFireLink(True))

	function arg_35_0._cancelFunc()
		var_35_5()

	arg_35_0._emptyFunc = None

def var_0_0.setFireLink(arg_48_0, arg_48_1):
	if arg_48_1:
		setButtonEnabled(arg_48_0.fireBtn, True)

		if arg_48_0._downFunc != None:
			arg_48_0.fireBtnDelegate.AddPointDownFunc(function()
				arg_48_0.isDown = True

				if arg_48_0._main_cannon_sound:
					arg_48_0._main_cannon_sound.Stop(True)

				arg_48_0._main_cannon_sound = pg.CriMgr.GetInstance().PlaySE_V3("battle-cannon-main-prepared")

				arg_48_0._downFunc())

		if arg_48_0._upFunc != None:
			arg_48_0.fireBtnDelegate.AddPointUpFunc(function()
				if arg_48_0.isDown:
					if arg_48_0._main_cannon_sound:
						arg_48_0._main_cannon_sound.Stop(True)

					pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./battle/boom2")

					arg_48_0.isDown = False

					arg_48_0._upFunc())

		if arg_48_0._cancelFunc != None:
			arg_48_0.fireBtnDelegate.AddPointExitFunc(function()
				if arg_48_0.isDown:
					if arg_48_0._main_cannon_sound:
						arg_48_0._main_cannon_sound.Stop(True)

					arg_48_0.isDown = False

					arg_48_0._cancelFunc())
	else
		if arg_48_0.isDown:
			arg_48_0.isDown = False

			arg_48_0._cancelFunc()

		setButtonEnabled(arg_48_0.fireBtn, False)
		arg_48_0.fireBtnDelegate.RemovePointDownFunc()
		arg_48_0.fireBtnDelegate.RemovePointUpFunc()
		arg_48_0.fireBtnDelegate.RemovePointExitFunc()

def var_0_0.flushTarget(arg_52_0, arg_52_1):
	if arg_52_1:
		arg_52_0.targetCount = {
			2,
			4,
			6
		}

	for iter_52_0 = 1, 3:
		for iter_52_1 = 1, 6:
			removeAllChildren(arg_52_0.targetPanel.Find("line_" .. iter_52_0).GetChild(iter_52_1 - 1))

	local var_52_0 = {
		0,
		0,
		0
	}

	arg_52_0.cell = {
		{},
		{},
		{}
	}

	for iter_52_2, iter_52_3 in ipairs(arg_52_0.targetCount):
		for iter_52_4 = 1, iter_52_3:
			local var_52_1 = math.random(3)
			local var_52_2 = math.random(6)

			while arg_52_0.cell[var_52_1][var_52_2] or arg_52_1 and var_52_0[var_52_1] >= 4:
				var_52_1, var_52_2 = math.random(3), math.random(6)

			var_52_0[var_52_1] = var_52_0[var_52_1] + 1
			arg_52_0.cell[var_52_1][var_52_2] = iter_52_2

			cloneTplTo(arg_52_0.targetTpl[iter_52_2], arg_52_0.targetPanel.Find("line_" .. var_52_1).GetChild(var_52_2 - 1))

	setText(arg_52_0.scoreTF, arg_52_0.score)

def var_0_0.checkHit(arg_53_0):
	for iter_53_0 = 1, 3:
		for iter_53_1 = 1, 6:
			if arg_53_0.cell[iter_53_0][iter_53_1]:
				local var_53_0 = arg_53_0.targetPanel.Find("line_" .. iter_53_0).GetChild(iter_53_1 - 1).GetChild(0).Find("icon/face")
				local var_53_1 = arg_53_0.sightTF.InverseTransformPoint(var_53_0.TransformPoint(var_53_0.position))

				if var_53_1.x * var_53_1.x + var_53_1.y * var_53_1.y < arg_53_0.tempConfig.half * arg_53_0.tempConfig.half:
					return True, iter_53_0, iter_53_1

def var_0_0.willExit(arg_54_0):
	return

return var_0_0
