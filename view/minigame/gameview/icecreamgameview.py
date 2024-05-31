local var_0_0 = class("IceCreamGameView", import("..BaseMiniGameView"))
local var_0_1 = "EVENT_ICE_FINISH"
local var_0_2 = "EVENT_UPDATE_WAIT_TIME"
local var_0_3 = 0.05
local var_0_4 = 2
local var_0_5 = {
	{
		6,
		10
	},
	{
		8,
		12
	},
	{
		10,
		14
	}
}
local var_0_6 = 60
local var_0_7 = {
	750,
	250,
	300
}
local var_0_8 = {
	200,
	100
}
local var_0_9 = {
	100,
	50,
	20
}
local var_0_10 = 20
local var_0_11 = {
	point_boost = 100,
	wait_time_boost = 2,
	bullet_time = {
		0.1,
		4,
		0.8,
		5
	}
}
local var_0_12 = {
	{
		1
	},
	{
		0,
		1
	},
	{
		1,
		0,
		2
	}
}
local var_0_13 = {
	{
		1
	},
	{
		2
	},
	{
		1,
		3
	}
}
local var_0_14 = {
	"A",
	"B",
	"C",
	"D"
}
local var_0_15 = {
	"H",
	"J",
	"K",
	"I"
}
local var_0_16

local function var_0_17(arg_1_0)
	if var_0_16:
		var_0_16.Pause(not arg_1_0)
	elif arg_1_0:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-icecream_topping", function(arg_2_0)
			assert(arg_2_0)

			var_0_16 = arg_2_0.playback)

def var_0_0.getUIName(arg_3_0):
	return "IceCreamGameUI"

def var_0_0.initTimer(arg_4_0):
	arg_4_0.timer = Timer.New(function()
		arg_4_0.onTimer(), var_0_3, -1)

def var_0_0.didEnter(arg_6_0):
	arg_6_0.initTimer()
	arg_6_0.initUI()
	arg_6_0.initGameUI()
	arg_6_0.openMainUI()

def var_0_0.initUI(arg_7_0):
	arg_7_0.clickMask = arg_7_0.findTF("ui/click_mask")
	arg_7_0.rtResource = arg_7_0._tf.Find("Resource")
	arg_7_0.mainUI = arg_7_0.findTF("ui/main_ui")
	arg_7_0.listScrollRect = GetComponent(arg_7_0.mainUI.Find("right_panel/item_list/content"), typeof(ScrollRect))

	onButton(arg_7_0, arg_7_0.mainUI.Find("btn_back"), function()
		arg_7_0.emit(var_0_0.ON_BACK_PRESSED), SFX_PANEL)
	onButton(arg_7_0, arg_7_0.mainUI.Find("bg/btn_help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.icecreamgame_tip.tip
		}), SFX_PANEL)
	onButton(arg_7_0, arg_7_0.mainUI.Find("bg/btn_start"), function()
		arg_7_0.readyStart(), SFX_PANEL)

	arg_7_0.totalTimes = arg_7_0.getGameTotalTime()

	local var_7_0 = arg_7_0.getGameUsedTimes() - 4 < 0 and 0 or arg_7_0.getGameUsedTimes() - 4

	scrollTo(arg_7_0.listScrollRect, 0, 1 - var_7_0 / (arg_7_0.totalTimes - 4))
	onButton(arg_7_0, arg_7_0.findTF("right_panel/arrows_up", arg_7_0.mainUI), function()
		local var_11_0 = arg_7_0.listScrollRect.normalizedPosition.y + 1 / (arg_7_0.totalTimes - 4)

		if var_11_0 > 1:
			var_11_0 = 1

		scrollTo(arg_7_0.listScrollRect, 0, var_11_0), SFX_PANEL)
	onButton(arg_7_0, arg_7_0.findTF("right_panel/arrows_down", arg_7_0.mainUI), function()
		local var_12_0 = arg_7_0.listScrollRect.normalizedPosition.y - 1 / (arg_7_0.totalTimes - 4)

		if var_12_0 < 0:
			var_12_0 = 0

		scrollTo(arg_7_0.listScrollRect, 0, var_12_0), SFX_PANEL)

	local var_7_1 = pg.mini_game[arg_7_0.GetMGData().id].simple_config_data.drop_ids
	local var_7_2 = arg_7_0.mainUI.Find("right_panel/item_list/content")

	arg_7_0.itemList = UIItemList.New(var_7_2, var_7_2.GetChild(0))

	arg_7_0.itemList.make(function(arg_13_0, arg_13_1, arg_13_2)
		arg_13_1 = arg_13_1 + 1

		if arg_13_0 == UIItemList.EventUpdate:
			arg_13_2.name = arg_13_1

			GetImageSpriteFromAtlasAsync("ui/minigameui/icecreamgameui_atlas", "day_" .. arg_13_1, arg_13_2.Find("text"))

			local var_13_0 = arg_13_2.Find("IconTpl")
			local var_13_1 = {}

			var_13_1.type, var_13_1.id, var_13_1.count = unpack(var_7_1[arg_13_1])

			updateDrop(var_13_0, var_13_1)
			onButton(arg_7_0, var_13_0, function()
				arg_7_0.emit(var_0_0.ON_DROP, var_13_1), SFX_PANEL))
	arg_7_0.itemList.align(#var_7_1)

	arg_7_0.countUI = arg_7_0.findTF("ui/count_ui")
	arg_7_0.countAnimator = GetComponent(arg_7_0.findTF("count", arg_7_0.countUI), typeof(Animator))
	arg_7_0.countDft = GetOrAddComponent(arg_7_0.findTF("count", arg_7_0.countUI), typeof(DftAniEvent))

	arg_7_0.countDft.SetTriggerEvent(function()
		return)
	arg_7_0.countDft.SetEndEvent(function()
		setActive(arg_7_0.countUI, False)
		arg_7_0.startGame())

	arg_7_0.pauseUI = arg_7_0.findTF("ui/pause_ui")

	onButton(arg_7_0, arg_7_0.findTF("panel/btn_confirm", arg_7_0.pauseUI), function()
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_7_0.pauseUI, arg_7_0._tf.Find("ui"))
		setActive(arg_7_0.pauseUI, False)
		arg_7_0.resumeGame(), SFX_PANEL)

	arg_7_0.returnUI = arg_7_0.findTF("ui/return_ui")

	onButton(arg_7_0, arg_7_0.findTF("panel/btn_confirm", arg_7_0.returnUI), function()
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_7_0.returnUI, arg_7_0._tf.Find("ui"))
		setActive(arg_7_0.returnUI, False)
		arg_7_0.resumeGame()
		arg_7_0.endGame(), SFX_PANEL)
	onButton(arg_7_0, arg_7_0.findTF("panel/btn_cancel", arg_7_0.returnUI), function()
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_7_0.returnUI, arg_7_0._tf.Find("ui"))
		setActive(arg_7_0.returnUI, False)
		arg_7_0.resumeGame(), SFX_PANEL)

	arg_7_0.endUI = arg_7_0.findTF("ui/end_ui")

	onButton(arg_7_0, arg_7_0.findTF("panel/btn_finish", arg_7_0.endUI), function()
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_7_0.endUI, arg_7_0._tf.Find("ui"))
		setActive(arg_7_0.endUI, False)
		arg_7_0.openMainUI(), SFX_PANEL)

	if not arg_7_0.handle:
		arg_7_0.handle = UpdateBeat.CreateListener(arg_7_0.Update, arg_7_0)

	UpdateBeat.AddListener(arg_7_0.handle)

def var_0_0.Update(arg_21_0):
	return

def var_0_0.initGameUI(arg_22_0):
	arg_22_0.gameUI = arg_22_0.findTF("ui/game_ui")
	arg_22_0.timeTF = arg_22_0.gameUI.Find("Score/time/Text")
	arg_22_0.scoreTF = arg_22_0.gameUI.Find("Score/point/Text")
	arg_22_0.addScoreTF = arg_22_0.gameUI.Find("Score/add_score")

	onButton(arg_22_0, arg_22_0.gameUI.Find("Button/btn_pause"), function()
		arg_22_0.pauseGame()
		pg.UIMgr.GetInstance().OverlayPanel(arg_22_0.pauseUI)
		setActive(arg_22_0.pauseUI, True))
	onButton(arg_22_0, arg_22_0.gameUI.Find("Button/btn_back"), function()
		arg_22_0.pauseGame()
		pg.UIMgr.GetInstance().OverlayPanel(arg_22_0.returnUI)
		setActive(arg_22_0.returnUI, True))

	arg_22_0.rtWalk = arg_22_0.gameUI.Find("Walk")
	arg_22_0.rtMake = arg_22_0.gameUI.Find("Make")
	arg_22_0.rtTime = arg_22_0.gameUI.Find("Time")
	arg_22_0.rtButton = arg_22_0.gameUI.Find("Button")

	for iter_22_0 = 1, 4:
		onButton(arg_22_0, arg_22_0.rtButton.Find("L" .. iter_22_0), function()
			if not arg_22_0.iceBuild or arg_22_0.iceBuild.isLeftLock:
				return

			local var_25_0 = arg_22_0.targetList[arg_22_0.targetIndex]._info

			if #arg_22_0.iceBuild._info[1] == #var_25_0[1]:
				return

			arg_22_0.iceBuild.MakeBall(iter_22_0))
		onButton(arg_22_0, arg_22_0.rtButton.Find("R" .. iter_22_0), function()
			if not arg_22_0.iceBuild or arg_22_0.iceBuild.isRightLock:
				return

			local var_26_0 = arg_22_0.targetList[arg_22_0.targetIndex]._info

			if #arg_22_0.iceBuild._info[2] == #var_26_0[2]:
				return

			if not arg_22_0.iceBuild._info[1][var_0_13[#var_26_0[1]][#arg_22_0.iceBuild._info[2] + 1]]:
				arg_22_0.iceBuild.MakeMissTopping(iter_22_0)
			else
				arg_22_0.iceBuild.MakeTopping(iter_22_0))

	arg_22_0.bind(var_0_1, function(arg_27_0, ...)
		arg_22_0.ResultTarget(...))
	arg_22_0.bind(var_0_2, function(arg_28_0, arg_28_1, ...)
		eachChild(arg_22_0.rtTime, function(arg_29_0)
			setActive(arg_29_0, arg_29_0.name == arg_28_1))
		setSlider(arg_22_0.rtTime.Find(arg_28_1), ...))

def var_0_0.updateMainUI(arg_30_0):
	local var_30_0 = arg_30_0.getGameUsedTimes()
	local var_30_1 = arg_30_0.getGameTimes()
	local var_30_2 = arg_30_0.itemList.container
	local var_30_3 = var_30_2.childCount

	for iter_30_0 = 1, var_30_3:
		local var_30_4 = {
			award = True
		}

		if iter_30_0 <= var_30_0:
			var_30_4.finish = True
		elif iter_30_0 == var_30_0 + 1 and var_30_1 >= 1:
			-- block empty
		elif var_30_0 < iter_30_0 and iter_30_0 <= var_30_0 + var_30_1:
			-- block empty
		else
			var_30_4.lock = True
			var_30_4.award = False

		local var_30_5 = var_30_2.GetChild(iter_30_0 - 1)

		setActive(var_30_5.Find("finish"), var_30_4.finish)
		setActive(var_30_5.Find("lock"), var_30_4.lock)
		setActive(var_30_5.Find("IconTpl"), var_30_4.award)

	arg_30_0.totalTimes = arg_30_0.getGameTotalTime()

	local var_30_6 = 1 - (arg_30_0.getGameUsedTimes() - 3 < 0 and 0 or arg_30_0.getGameUsedTimes() - 3) / (arg_30_0.totalTimes - 4)

	if var_30_6 > 1:
		var_30_6 = 1

	scrollTo(arg_30_0.listScrollRect, 0, var_30_6)
	arg_30_0.checkGet()

def var_0_0.checkGet(arg_31_0):
	if arg_31_0.getUltimate() == 0:
		if arg_31_0.getGameTotalTime() > arg_31_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_31_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})

def var_0_0.openMainUI(arg_32_0):
	setActive(arg_32_0.gameUI, False)
	setActive(arg_32_0.mainUI, True)
	arg_32_0.updateMainUI()

def var_0_0.readyStart(arg_33_0):
	setActive(arg_33_0.mainUI, False)
	setActive(arg_33_0.countUI, True)
	arg_33_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/ddldaoshu2")
	arg_33_0.resetGame()

def var_0_0.resetGame(arg_34_0):
	arg_34_0.gameStartFlag = False
	arg_34_0.gamePause = False
	arg_34_0.gameEndFlag = False
	arg_34_0.scoreNum = 0
	arg_34_0.lastTime = var_0_6
	arg_34_0.targetNameList = {}
	arg_34_0.targetList = {}
	arg_34_0.iceBuild = None
	arg_34_0.countList = {
		0,
		0,
		0
	}
	arg_34_0.effectTrigger = {
		bullet_time = {
			waitTime = 0,
			doingTime = 0
		},
		wait_time_boost = {
			count = 0
		},
		point_boost = {}
	}

	eachChild(arg_34_0.rtResource.Find("Character"), function(arg_35_0)
		table.insert(arg_34_0.targetNameList, arg_35_0.name))
	removeAllChildren(arg_34_0.rtWalk)
	setActive(arg_34_0.gameUI.Find("BulletTimeMask"), False)
	setActive(arg_34_0.rtMake, False)
	setActive(arg_34_0.rtTime, False)
	setText(arg_34_0.scoreTF, arg_34_0.scoreNum)
	setActive(arg_34_0.addScoreTF, False)
	arg_34_0.setAnimatorSpeed(arg_34_0._tf, 1)

local function var_0_18(arg_36_0, arg_36_1, arg_36_2, arg_36_3)
	local var_36_0 = {}

	local function var_36_1(arg_37_0, arg_37_1)
		for iter_37_0 = math.max(#arg_37_1[1], 2), 1, -1:
			setActive(arg_37_0.Find(iter_37_0), arg_37_1[1][iter_37_0])

			if arg_37_1[1][iter_37_0]:
				local var_37_0 = arg_37_0.Find(iter_37_0)

				GetImageSpriteFromAtlasAsync("ui/minigameui/icecreamgameui_atlas", "Assets/ArtResource/UI/MiniGameUI/IceCreamGameUI/ICE_S/" .. var_0_14[arg_37_1[1][iter_37_0]] .. ".png", var_37_0.Find("Scoop"), True)

				local var_37_1 = arg_37_1[2][var_0_12[#arg_37_1[1]][iter_37_0]]

				setActive(var_37_0.Find("Topping"), var_37_1)

				if var_37_1:
					GetImageSpriteFromAtlasAsync("ui/minigameui/icecreamgameui_atlas", "Assets/ArtResource/UI/MiniGameUI/IceCreamGameUI/ICE_S/" .. var_0_15[var_37_1] .. ".png", var_37_0.Find("Topping"), True)

	function var_36_0.Ctor(arg_38_0)
		arg_38_0._tf = arg_36_0
		arg_38_0._event = arg_36_1
		arg_38_0._info = arg_36_2
		arg_38_0.time = arg_36_3
		arg_38_0.pointBoost = 100
		arg_38_0.result = None

		local var_38_0 = #arg_36_2[1] < 3 and "Cone" or "Bowl"

		for iter_38_0, iter_38_1 in ipairs({
			"IceCream",
			"Bubble",
			"BadCream"
		}):
			eachChild(arg_36_0.Find(iter_38_1), function(arg_39_0)
				setActive(arg_39_0, arg_39_0.name == var_38_0))

		var_36_1(arg_36_0.Find("Bubble/" .. var_38_0), arg_36_2)
		GetImageSpriteFromAtlasAsync("ui/minigameui/icecreamgameui_atlas", "Assets/ArtResource/UI/MiniGameUI/IceCreamGameUI/ICE_S/bubble_" .. #arg_36_2[1] .. ".png", arg_36_0.Find("Bubble"), True)
		setActive(arg_36_0.Find("Bubble/Boost"), False)

		arg_38_0.animator = GetComponent(arg_38_0._tf, typeof(Animator))

		arg_38_0._tf.GetComponent(typeof(DftAniEvent)).SetTriggerEvent(function()
			arg_38_0.isLeave = True)

	function var_36_0.Result(arg_41_0, arg_41_1, arg_41_2)
		arg_41_0.result = arg_41_1

		local var_41_0 = #arg_41_2[1] < 3 and "Cone" or "Bowl"

		if arg_41_1 == 0:
			arg_41_0.animator.Play("Bad")
		elif arg_41_1 == 1:
			var_36_1(arg_41_0._tf.Find("IceCream/" .. var_41_0), arg_41_2)
			arg_41_0.animator.Play("Hmm")
		elif arg_41_1 >= 2:
			var_36_1(arg_41_0._tf.Find("IceCream/" .. var_41_0), arg_41_2)
			arg_41_0.animator.Play("Great")
		else
			assert(False)

	var_36_0.Ctor()

	return var_36_0

def var_0_0.CreateTarget(arg_42_0, arg_42_1):
	local var_42_0 = table.remove(arg_42_0.targetNameList, math.random(#arg_42_0.targetNameList))
	local var_42_1 = cloneTplTo(arg_42_0.rtResource.Find("Character/" .. var_42_0), arg_42_0.rtWalk, var_42_0)

	setAnchoredPosition(var_42_1, {
		x = arg_42_1 or -var_0_7[1]
	})

	local var_42_2 = {
		{},
		{}
	}
	local var_42_3 = var_42_0 == "Agir" and {
		1,
		2
	} or {
		1,
		2,
		3
	}

	if #arg_42_0.targetList > 0:
		table.removebyvalue(var_42_3, #arg_42_0.targetList[#arg_42_0.targetList]._info[1])

	for iter_42_0 = var_42_3[math.random(#var_42_3)], 1, -1:
		table.insert(var_42_2[1], math.random(4))

	local var_42_4 = {
		1,
		2,
		3,
		4
	}

	for iter_42_1 = math.max(1, #var_42_2[1] - 1), 1, -1:
		table.insert(var_42_2[2], table.remove(var_42_4, math.random(#var_42_4)))

	local var_42_5 = math.clamp(var_0_5[#var_42_2[1]][2] - arg_42_0.countList[#var_42_2[1]], unpack(var_0_5[#var_42_2[1]]))

	arg_42_0.countList[#var_42_2[1]] = arg_42_0.countList[#var_42_2[1]] + 1

	table.insert(arg_42_0.targetList, var_0_18(var_42_1, arg_42_0, var_42_2, var_42_5))

def var_0_0.RemoveTarget(arg_43_0):
	assert(#arg_43_0.targetList > 0)

	local var_43_0 = table.remove(arg_43_0.targetList, 1)

	arg_43_0.targetIndex = arg_43_0.targetIndex - 1

	table.insert(arg_43_0.targetNameList, var_43_0._tf.name)
	Destroy(var_43_0._tf)

def var_0_0.ResultTarget(arg_44_0, arg_44_1, arg_44_2, ...):
	assert(#arg_44_0.targetList > 0)

	arg_44_1 = math.ceil(arg_44_1 * arg_44_0.targetList[arg_44_0.targetIndex].pointBoost / 100)

	arg_44_0.addScore(arg_44_1, arg_44_2)
	arg_44_0.targetList[arg_44_0.targetIndex].Result(arg_44_2, ...)
	arg_44_0.TriggerSpecialEffect(arg_44_2, ...)

	arg_44_0.targetIndex = arg_44_0.targetIndex + 1
	arg_44_0.iceBuild = None

	onNextTick(function()
		setActive(arg_44_0.rtMake, False)
		setActive(arg_44_0.rtTime, False))

	local var_44_0 = arg_44_0.effectTrigger.bullet_time

	if var_44_0.doingTime > 0:
		var_44_0.doingTime = 0

		arg_44_0.setAnimatorSpeed(arg_44_0._tf, 1)
		setActive(arg_44_0.gameUI.Find("BulletTimeMask"), False)

def var_0_0.TriggerSpecialEffect(arg_46_0, arg_46_1, arg_46_2):
	if arg_46_1 == 3:
		local var_46_0 = arg_46_0.targetList[arg_46_0.targetIndex + 1]
		local var_46_1 = arg_46_0.effectTrigger.bullet_time

		if #arg_46_0.targetList[arg_46_0.targetIndex]._info[1] == 3 and var_46_1.waitTime <= 0 and math.random() < var_0_11.bullet_time[3]:
			var_46_0.timeBoost = True

		local var_46_2 = arg_46_0.effectTrigger.wait_time_boost

		var_46_2.count = var_46_2.count + 1

		if var_46_2.count == 2:
			var_46_2.count = 0
			var_46_0.time = var_46_0.time + var_0_11.wait_time_boost
			var_46_0.isWaitTimeBoost = True

		local var_46_3 = arg_46_0.effectTrigger.point_boost
		local var_46_4 = arg_46_0.targetList[arg_46_0.targetIndex]._tf.name

		if var_46_3[var_46_4] == "finish":
			-- block empty
		elif var_46_3[var_46_4] == "count":
			var_46_0.pointBoost = var_46_0.pointBoost + var_0_11.point_boost

			setActive(var_46_0._tf.Find("Bubble/Boost"), True)

			var_46_3[var_46_4] = "finish"
		else
			var_46_3[var_46_4] = "count"
	else
		local var_46_5 = arg_46_0.effectTrigger.point_boost
		local var_46_6 = arg_46_0.targetList[arg_46_0.targetIndex]._tf.name

		if var_46_5[var_46_6] == "finish":
			-- block empty
		else
			var_46_5[var_46_6] = None

local function var_0_19(arg_47_0, arg_47_1, arg_47_2, arg_47_3, arg_47_4)
	local var_47_0 = {
		def Ctor:(arg_48_0)
			arg_48_0._tf = arg_47_0
			arg_48_0._event = arg_47_1
			arg_48_0._info = {
				{},
				{}
			}
			arg_48_0.isLeftLock = False
			arg_48_0.isRightLock = False
			arg_48_0.missToppingMark = {}
			arg_48_0.waitTime = arg_47_3
			arg_48_0.isWaitTimeBoost = arg_47_4

			arg_48_0.Reset()
			arg_48_0.NextDeal(),
		def NextDeal:(arg_49_0)
			if arg_49_0.isLeftLock or arg_49_0.isRightLock:
				return

			if #arg_49_0._info[1] < #arg_47_2[1]:
				arg_49_0.ReadyBall()
			elif #arg_49_0._info[2] < #arg_47_2[2]:
				arg_49_0.ReadyTopping()
			else
				arg_49_0.Result(),
		def Result:(arg_50_0, arg_50_1)
			arg_50_0.isResulted = True

			var_0_17(False)

			local var_50_0 = 0
			local var_50_1 = {
				{
					0,
					0,
					0,
					0
				},
				{
					0,
					0,
					0,
					0
				}
			}

			local function var_50_2(arg_51_0, arg_51_1, arg_51_2)
				local var_51_0 = arg_51_0[arg_51_1]

				arg_51_0[arg_51_1] = arg_51_0[arg_51_1] + arg_51_2

				return math.abs(arg_51_0[arg_51_1]) - math.abs(var_51_0)

			for iter_50_0, iter_50_1 in ipairs(arg_50_0._info):
				for iter_50_2, iter_50_3 in ipairs(iter_50_1):
					if var_50_2(var_50_1[iter_50_0], arg_47_2[iter_50_0][iter_50_2], -1) < 0:
						var_50_0 = var_50_0 + var_0_9[iter_50_0]

					if var_50_2(var_50_1[iter_50_0], iter_50_3, 1) < 0:
						var_50_0 = var_50_0 + var_0_9[iter_50_0]

					if arg_47_2[iter_50_0][iter_50_2] == iter_50_3 and (iter_50_0 == 1 or not arg_50_0.missToppingMark[iter_50_2]):
						var_50_0 = var_50_0 + var_0_9[3]

			if arg_50_1:
				arg_50_0.result = arg_50_1
			else
				local var_50_3 = #arg_50_0._info[1] * var_0_9[1] + #arg_50_0._info[2] * var_0_9[2] + (#arg_50_0._info[1] + #arg_50_0._info[2]) * var_0_9[3]

				if var_50_0 == var_50_3:
					arg_50_0.result = 3
				elif table.equal(arg_50_0._info, arg_47_2):
					arg_50_0.result = 2
				elif var_50_0 >= var_50_3 / 2:
					arg_50_0.result = 1
				else
					arg_50_0.result = 0

			local var_50_4 = arg_50_0._tf.GetComponent(typeof(Animator))

			if arg_50_0.result == 3:
				arg_50_0.point = var_50_0 * (1 + var_0_10 / 100 + arg_50_0.waitTime / arg_47_3)

				var_50_4.Play("Perfect")
				pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-icecream_great")
			elif arg_50_0.result == 2:
				arg_50_0.point = var_50_0 * (1 + arg_50_0.waitTime / arg_47_3)

				var_50_4.Play("Pass")
			elif arg_50_0.result == 1:
				arg_50_0.point = var_50_0 * (1 + arg_50_0.waitTime / arg_47_3)

				var_50_4.Play("Pass")
			elif arg_50_0.result == 0:
				arg_50_0.point = 0

				var_50_4.Play("Fail")
				pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-icecream_fail")
			else
				assert(False),
		def CountDown:(arg_52_0, arg_52_1, arg_52_2)
			if arg_52_0.isResulted:
				return

			if arg_52_0.waitTime > 0:
				arg_52_0.waitTime = arg_52_0.waitTime - arg_52_1

				arg_52_0._event.emit(var_0_2, arg_52_2, 0, arg_47_3, arg_52_0.waitTime)
			else
				arg_52_0.waitTime = 0

				arg_52_0.Result(0)

			if not arg_52_0.missTime:
				return

			if arg_52_0.missTime > 0:
				arg_52_0.missTime = arg_52_0.missTime - var_0_3
			else
				arg_52_0.missTime = None

				arg_52_0.FailMissTopping(),
		def Reset:(arg_53_0)
			arg_53_0._tf.GetComponent("DftAniEvent").SetEndEvent(function()
				onNextTick(function()
					setActive(arg_53_0._tf, False))
				arg_53_0._event.emit(var_0_1, arg_53_0.point, arg_53_0.result, arg_53_0._info))
			arg_53_0._tf.GetComponent("DftAniEvent").SetTriggerEvent(function()
				for iter_56_0 = arg_53_0._tf.name == "Cone" and 2 or 3, 1, -1:
					setActive(arg_53_0._tf.Find(iter_56_0), False)

				setActive(arg_53_0._tf.Find("Back"), False)

				if arg_53_0._tf.name == "Bowl":
					setActive(arg_53_0._tf.Find("Front"), False))
			setActive(arg_53_0._tf.Find("Back"), True)

			if arg_53_0._tf.name == "Bowl":
				setActive(arg_53_0._tf.Find("Front"), True)

			for iter_53_0 = arg_53_0._tf.name == "Cone" and 2 or 3, 1, -1:
				local var_53_0 = arg_53_0._tf.Find(iter_53_0)

				setActive(var_53_0, iter_53_0 <= #arg_47_2[1])

				if iter_53_0 <= #arg_47_2[1]:
					eachChild(var_53_0, function(arg_57_0)
						setActive(arg_57_0, False))
					var_53_0.Find("Scoop").GetComponent("DftAniEvent").SetEndEvent(function()
						arg_53_0.isLeftLock = False

						if arg_53_0.successLeftLight:
							arg_53_0.successLeftLight = False

							setAnchoredPosition(var_53_0.Find("Good"), {
								x = 0,
								y = -10
							})
							setActive(var_53_0.Find("Good"), False)
							setActive(var_53_0.Find("Good"), True)

						arg_53_0.NextDeal())
					var_53_0.Find("Topping").GetComponent("DftAniEvent").SetEndEvent(function()
						arg_53_0.isRightLock = False

						if arg_53_0.successRightLight:
							arg_53_0.successRightLight = False

							setAnchoredPosition(var_53_0.Find("Good"), {
								x = 10,
								y = 6
							})
							setActive(var_53_0.Find("Good"), False)
							setActive(var_53_0.Find("Good"), True)

						arg_53_0.NextDeal()),
		def ReadyBall:(arg_60_0)
			local var_60_0 = arg_60_0._tf.Find(#arg_60_0._info[1] + 1)

			setActive(var_60_0.Find("Scoop_Next"), True),
		def MakeBall:(arg_61_0, arg_61_1)
			arg_61_0.isLeftLock = True

			local var_61_0 = arg_61_0._tf.Find(#arg_61_0._info[1] + 1)

			setActive(var_61_0.Find("Scoop_Next"), False)
			setActive(var_61_0.Find("Scoop"), True)
			var_61_0.Find("Scoop").GetComponent(typeof(Animator)).Play("Scoop_" .. var_0_14[arg_61_1])
			table.insert(arg_61_0._info[1], arg_61_1)

			arg_61_0.successLeftLight = arg_61_0._info[1][#arg_61_0._info[1]] == arg_47_2[1][#arg_61_0._info[1]]

			if arg_61_0.temporaryKey and var_0_13[#arg_47_2[1]][#arg_61_0._info[2] + 1] == #arg_61_0._info[1]:
				arg_61_0.SafeMissTopping()

			pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-icecream_flavour"),
		def ReadyTopping:(arg_62_0)
			local var_62_0 = arg_62_0._tf.Find(var_0_13[#arg_47_2[1]][#arg_62_0._info[2] + 1])

			setActive(var_62_0.Find("Topping_Next"), True),
		def MakeTopping:(arg_63_0, arg_63_1)
			arg_63_0.isRightLock = True

			local var_63_0 = arg_63_0._tf.Find(var_0_13[#arg_47_2[1]][#arg_63_0._info[2] + 1])

			setActive(var_63_0.Find("Topping_Next"), False)
			setActive(var_63_0.Find("Topping"), True)
			var_63_0.Find("Topping").GetComponent(typeof(Animator)).Play("Topping_" .. var_0_15[arg_63_1])
			table.insert(arg_63_0._info[2], arg_63_1)

			arg_63_0.successRightLight = arg_63_0._info[2][#arg_63_0._info[2]] == arg_47_2[2][#arg_63_0._info[2]]

			pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-icecream_mixer"),
		def MakeMissTopping:(arg_64_0, arg_64_1)
			arg_64_0.isRightLock = True
			arg_64_0.temporaryKey = arg_64_1
			arg_64_0.missTime = var_0_4 * (var_0_13[#arg_47_2[1]][#arg_64_0._info[2] + 1] - #arg_64_0._info[1])

			var_0_17(True)

			local var_64_0 = arg_64_0._tf.Find(var_0_13[#arg_47_2[1]][#arg_64_0._info[2] + 1])

			setActive(var_64_0.Find("Topping_Next"), False)
			setActive(var_64_0.Find("Topping"), True)
			var_64_0.Find("Topping").GetComponent(typeof(Animator)).Play("Topping_pre_" .. var_0_15[arg_64_1]),
		def FailMissTopping:(arg_65_0)
			arg_65_0.isRightLock = True

			local var_65_0 = arg_65_0.temporaryKey

			arg_65_0.temporaryKey = None
			arg_65_0.missTime = None

			var_0_17(False)

			local var_65_1 = arg_65_0._tf.Find(var_0_13[#arg_47_2[1]][#arg_65_0._info[2] + 1])

			setActive(var_65_1.Find("Topping_Next"), False)
			setActive(var_65_1.Find("Topping"), True)
			var_65_1.Find("Topping").GetComponent(typeof(Animator)).Play("Topping_Err_" .. var_0_15[var_65_0]),
		def SafeMissTopping:(arg_66_0)
			arg_66_0.isRightLock = True

			local var_66_0 = arg_66_0.temporaryKey

			arg_66_0.temporaryKey = None
			arg_66_0.missTime = None

			var_0_17(False)

			local var_66_1 = arg_66_0._tf.Find(var_0_13[#arg_47_2[1]][#arg_66_0._info[2] + 1])

			setActive(var_66_1.Find("Topping_Next"), False)
			setActive(var_66_1.Find("Topping"), True)
			var_66_1.Find("Topping").GetComponent(typeof(Animator)).Play("Topping_safe_" .. var_0_15[var_66_0])
			table.insert(arg_66_0._info[2], var_66_0)

			arg_66_0.successRightLight = arg_66_0._info[2][#arg_66_0._info[2]] == arg_47_2[2][#arg_66_0._info[2]]
			arg_66_0.missToppingMark[#arg_66_0._info[2]] = True

			pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-icecream_mixer")
	}

	var_47_0.Ctor()

	return var_47_0

def var_0_0.DoIceCream(arg_67_0):
	setActive(arg_67_0.rtTime, True)
	setActive(arg_67_0.rtMake, True)

	local var_67_0 = arg_67_0.targetList[arg_67_0.targetIndex]
	local var_67_1 = #var_67_0._info[1] < 3 and "Cone" or "Bowl"

	eachChild(arg_67_0.rtMake, function(arg_68_0)
		setActive(arg_68_0, arg_68_0.name == var_67_1))

	local var_67_2 = arg_67_0.rtMake.Find(var_67_1)

	for iter_67_0 = var_67_1 == "Cone" and 2 or 3, 1, -1:
		setActive(var_67_2.Find(iter_67_0), False)

	arg_67_0.iceBuild = var_0_19(var_67_2, arg_67_0, var_67_0._info, var_67_0.time, var_67_0.isWaitTimeBoost)

	if var_67_0.timeBoost:
		local var_67_3 = arg_67_0.effectTrigger.bullet_time

		var_67_3.doingTime = var_0_11.bullet_time[2]
		var_67_3.waitTime = var_0_11.bullet_time[4]

		arg_67_0.setAnimatorSpeed(arg_67_0._tf, 0.5)
		arg_67_0.setAnimatorSpeed(arg_67_0.rtMake, 1)
		setActive(arg_67_0.gameUI.Find("BulletTimeMask"), True)

def var_0_0.startGame(arg_69_0):
	setActive(arg_69_0.gameUI, True)

	arg_69_0.gameStartFlag = True

	arg_69_0.CreateTarget(-var_0_7[1] / 3)

	arg_69_0.targetIndex = 1

	arg_69_0.RandomBG()
	arg_69_0.timerStart()

def var_0_0.RandomBG(arg_70_0):
	arg_70_0.poolBG = arg_70_0.poolBG or {
		GroupD = {
			1
		}
	}

	if not arg_70_0.poolBG.GroupAB or #arg_70_0.poolBG.GroupAB == 0:
		arg_70_0.poolBG.GroupAB = {
			1,
			2,
			3,
			4,
			5,
			6
		}

	if not arg_70_0.poolBG["GroupC/Other"] or #arg_70_0.poolBG["GroupC/Other"] == 0:
		arg_70_0.poolBG["GroupC/Other"] = {
			1,
			2,
			3,
			4
		}

	arg_70_0.poolBG["GroupC/Manjuu"] = {
		1,
		2,
		3
	}

	for iter_70_0, iter_70_1 in pairs(arg_70_0.poolBG):
		local var_70_0 = {}

		for iter_70_2 = iter_70_0 == "GroupC/Manjuu" and 2 or 1, 1, -1:
			if iter_70_0 == "GroupD":
				var_70_0[iter_70_1[1]] = True
				iter_70_1[1] = 3 - iter_70_1[1]
			else
				var_70_0[table.remove(iter_70_1, math.random(#iter_70_1))] = True

		local var_70_1 = arg_70_0.gameUI.Find("BG/" .. iter_70_0)

		for iter_70_3 = var_70_1.childCount, 1, -1:
			setActive(var_70_1.GetChild(iter_70_3 - 1), var_70_0[iter_70_3])

def var_0_0.getIntervalTime(arg_71_0):
	if arg_71_0.effectTrigger.bullet_time.doingTime > 0:
		return var_0_3 * var_0_11.bullet_time[1]
	else
		return var_0_3

def var_0_0.onTimer(arg_72_0):
	local var_72_0 = arg_72_0.effectTrigger.bullet_time

	if var_72_0.doingTime > 0:
		var_72_0.doingTime = var_72_0.doingTime - var_0_3

		if var_72_0.doingTime <= 0:
			arg_72_0.setAnimatorSpeed(arg_72_0._tf, 1)
			setActive(arg_72_0.gameUI.Find("BulletTimeMask"), False)
	elif var_72_0.waitTime > 0:
		var_72_0.waitTime = var_72_0.waitTime - var_0_3

	arg_72_0.lastTime = arg_72_0.lastTime - arg_72_0.getIntervalTime()

	arg_72_0.updateWalker()

	if arg_72_0.lastTime <= 0:
		arg_72_0.endGame()
	else
		setText(arg_72_0.timeTF, math.floor(arg_72_0.lastTime))

		if not arg_72_0.iceBuild and arg_72_0.targetList[arg_72_0.targetIndex]._tf.anchoredPosition.x > 0:
			arg_72_0.DoIceCream()

		if #arg_72_0.targetList == arg_72_0.targetIndex:
			arg_72_0.CreateTarget()

	if arg_72_0.iceBuild:
		local var_72_1
		local var_72_2 = var_72_0.doingTime > 0 and "frozen" or arg_72_0.iceBuild.isWaitTimeBoost and "extend" or "base"

		arg_72_0.iceBuild.CountDown(arg_72_0.getIntervalTime(), var_72_2)

def var_0_0.updateWalker(arg_73_0):
	for iter_73_0 = #arg_73_0.targetList, 1, -1:
		local var_73_0 = arg_73_0.targetList[iter_73_0]
		local var_73_1 = var_73_0._tf.GetComponent(typeof(Animator))
		local var_73_2 = var_73_1.GetCurrentAnimatorStateInfo(0)

		if var_73_0.result:
			if var_73_0.isLeave:
				setAnchoredPosition(var_73_0._tf, {
					x = var_73_0._tf.anchoredPosition.x + arg_73_0.getIntervalTime() * var_0_8[1]
				})

				if var_73_0._tf.anchoredPosition.x > var_0_7[1]:
					arg_73_0.RemoveTarget()
		else
			local var_73_3 = var_0_7[3]

			if iter_73_0 > 1:
				var_73_3 = math.min(var_73_3, arg_73_0.targetList[iter_73_0 - 1]._tf.anchoredPosition.x)

			local var_73_4 = var_73_3 - var_73_0._tf.anchoredPosition.x

			if var_73_4 < var_0_7[3]:
				if not var_73_0.state or var_73_0.state != "Stand":
					var_73_0.state = "Stand"

					var_73_1.Play("Stand")
			elif var_73_4 < var_0_7[2]:
				setAnchoredPosition(var_73_0._tf, {
					x = var_73_0._tf.anchoredPosition.x + arg_73_0.getIntervalTime() * var_0_8[2]
				})

				if not var_73_0.state or var_73_0.state != "Walk":
					var_73_0.state = "Walk"

					var_73_1.Play("Walk")
			else
				setAnchoredPosition(var_73_0._tf, {
					x = var_73_0._tf.anchoredPosition.x + arg_73_0.getIntervalTime() * var_0_8[1]
				})

				if not var_73_0.state or var_73_0.state != "Run":
					var_73_0.state = "Run"

					var_73_1.Play("Run")

def var_0_0.setAnimatorSpeed(arg_74_0, arg_74_1, arg_74_2):
	local var_74_0 = arg_74_1.GetComponentsInChildren(typeof(Animator), True)

	for iter_74_0 = 0, var_74_0.Length - 1:
		var_74_0[iter_74_0].speed = arg_74_2

def var_0_0.timerStart(arg_75_0):
	if not arg_75_0.timer.running:
		arg_75_0.timer.Start()

	if arg_75_0.effectTrigger.bullet_time.doingTime > 0:
		arg_75_0.setAnimatorSpeed(arg_75_0._tf, 0.5)
		arg_75_0.setAnimatorSpeed(arg_75_0.rtMake, 1)
	else
		arg_75_0.setAnimatorSpeed(arg_75_0._tf, 1)

	if arg_75_0.iceBuild and arg_75_0.iceBuild.missTime:
		var_0_17(True)

def var_0_0.timerStop(arg_76_0):
	if arg_76_0.timer.running:
		arg_76_0.timer.Stop()

	arg_76_0.setAnimatorSpeed(arg_76_0._tf, 0)

	if arg_76_0.iceBuild and arg_76_0.iceBuild.missTime:
		var_0_17(False)

def var_0_0.addScore(arg_77_0, arg_77_1, arg_77_2):
	arg_77_0.scoreNum = arg_77_0.scoreNum + arg_77_1

	setText(arg_77_0.scoreTF, arg_77_0.scoreNum)
	setActive(arg_77_0.addScoreTF, False)
	setActive(arg_77_0.addScoreTF, True)

	local var_77_0 = arg_77_0.addScoreTF.Find("score_tf")

	setText(var_77_0, "+" .. arg_77_1)

	if arg_77_2 == 0:
		setTextColor(var_77_0, Color.NewHex("ED666DFF"))
	elif arg_77_2 == 1:
		setTextColor(var_77_0, Color.NewHex("FAB149FF"))
	elif arg_77_2 == 2:
		setTextColor(var_77_0, Color.NewHex("C6CC15FF"))
	elif arg_77_2 == 3:
		setTextColor(var_77_0, Color.NewHex("80BF1CFF"))
	else
		assert(False)

def var_0_0.pauseGame(arg_78_0):
	arg_78_0.gamePause = True

	arg_78_0.timerStop()
	arg_78_0.pauseManagedTween()

def var_0_0.resumeGame(arg_79_0):
	arg_79_0.gamePause = False

	arg_79_0.timerStart()
	arg_79_0.resumeManagedTween()

def var_0_0.endGame(arg_80_0):
	if arg_80_0.gameEndFlag:
		return

	arg_80_0.timerStop()

	arg_80_0.gameEndFlag = True

	setActive(arg_80_0.clickMask, True)
	arg_80_0.managedTween(LeanTween.delayedCall, function()
		arg_80_0.gameEndFlag = False
		arg_80_0.gameStartFlag = False

		setActive(arg_80_0.clickMask, False)
		arg_80_0.showEndUI(), 0.1, None)

def var_0_0.showEndUI(arg_82_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_82_0.endUI)
	setActive(arg_82_0.endUI, True)

	local var_82_0 = arg_82_0.GetMGData().GetRuntimeData("elements")
	local var_82_1 = arg_82_0.scoreNum
	local var_82_2 = var_82_0 and #var_82_0 > 0 and var_82_0[1] or 0

	setActive(arg_82_0.findTF("panel/now/Text/new", arg_82_0.endUI), var_82_2 < var_82_1)

	if var_82_2 <= var_82_1:
		var_82_2 = var_82_1

		arg_82_0.StoreDataToServer({
			var_82_2
		})

	local var_82_3 = arg_82_0.findTF("panel/max/Text", arg_82_0.endUI)
	local var_82_4 = arg_82_0.findTF("panel/now/Text", arg_82_0.endUI)

	setText(var_82_3, var_82_2)
	setText(var_82_4, var_82_1)

	if arg_82_0.getGameTimes() and arg_82_0.getGameTimes() > 0:
		arg_82_0.SendSuccess(0)

def var_0_0.getGameTimes(arg_83_0):
	return arg_83_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_84_0):
	return arg_84_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_85_0):
	return arg_85_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_86_0):
	return (arg_86_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.OnApplicationPaused(arg_87_0, arg_87_1):
	if arg_87_1 and not arg_87_0.gameEndFlag and arg_87_0.gameStartFlag and not arg_87_0.gamePause:
		arg_87_0.pauseGame()
		pg.UIMgr.GetInstance().OverlayPanel(arg_87_0.pauseUI)
		setActive(arg_87_0.pauseUI, True)

def var_0_0.onBackPressed(arg_88_0):
	if arg_88_0.gameEndFlag:
		return

	if isActive(arg_88_0.pauseUI):
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_88_0.pauseUI, arg_88_0._tf.Find("ui"))
		setActive(arg_88_0.pauseUI, False)
		arg_88_0.resumeGame()

		return

	if isActive(arg_88_0.returnUI):
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_88_0.returnUI, arg_88_0._tf.Find("ui"))
		setActive(arg_88_0.returnUI, False)
		arg_88_0.resumeGame()

		return

	if isActive(arg_88_0.endUI):
		return

	if arg_88_0.gameStartFlag:
		arg_88_0.pauseGame()
		pg.UIMgr.GetInstance().OverlayPanel(arg_88_0.pauseUI)
		setActive(arg_88_0.pauseUI, True)

		return

	arg_88_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.willExit(arg_89_0):
	if arg_89_0.handle:
		UpdateBeat.RemoveListener(arg_89_0.handle)

	arg_89_0.cleanManagedTween()

	if arg_89_0.timer and arg_89_0.timer.running:
		arg_89_0.timer.Stop()

	Time.timeScale = 1
	arg_89_0.timer = None

return var_0_0
