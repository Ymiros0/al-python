local var_0_0 = class("RopingCowGameView", import("..BaseMiniGameView"))
local var_0_1 = "SailAwayJustice-inst"
local var_0_2 = "event./ui/ddldaoshu2"
local var_0_3 = "event./ui/niujiao"
local var_0_4 = "event./ui/taosheng"
local var_0_5 = 60
local var_0_6 = {
	{
		20,
		{
			0,
			0.25
		}
	},
	{
		40,
		{
			0.5,
			0.5
		}
	},
	{
		50,
		{
			0.5,
			1
		}
	},
	{
		60,
		{
			1,
			1.5
		}
	}
}
local var_0_7 = {
	{
		speed = 800,
		score = 300
	},
	{
		speed = 700,
		score = 200
	},
	{
		speed = 600,
		score = 100
	},
	{
		speed = 500,
		score = 50
	}
}
local var_0_8 = {
	{
		20,
		{
			300,
			300,
			200,
			200
		}
	},
	{
		40,
		{
			200,
			300,
			300,
			200
		}
	},
	{
		50,
		{
			150,
			250,
			300,
			300
		}
	},
	{
		60,
		{
			100,
			100,
			400,
			400
		}
	}
}
local var_0_9 = {
	-50,
	50
}
local var_0_10 = 0.75
local var_0_11 = 1700
local var_0_12 = 4
local var_0_13 = 0
local var_0_14 = 1
local var_0_15 = 2
local var_0_16 = "cow_event_capture"
local var_0_17 = "player_event_capture"
local var_0_18 = "player_event_get"
local var_0_19 = "player_event_miss"
local var_0_20 = "player_event_cd"
local var_0_21 = "idol"
local var_0_22 = "miss"
local var_0_23 = "get"
local var_0_24 = "throw"
local var_0_25 = "event_capture"
local var_0_26 = "scene_item_type_time"
local var_0_27 = "scene_item_type_event"
local var_0_28 = {
	{
		name = "backGround/2/jiujiuA",
		type = var_0_26,
		params = {
			15,
			20
		},
		states = {
			1,
			2,
			3
		}
	},
	{
		name = "backGround/2/jiujiuB",
		type = var_0_26,
		params = {
			15,
			20
		},
		states = {
			1,
			2
		}
	},
	{
		trigger = True,
		name = "backGround/2/jiujiuC",
		type = var_0_26,
		params = {
			15,
			20
		}
	},
	{
		trigger = True,
		name = "backGround/3/jiujiuD",
		type = var_0_26,
		params = {
			20,
			22
		}
	},
	{
		trigger = True,
		name = "backGround/3/train",
		type = var_0_26,
		params = {
			20,
			23
		}
	},
	{
		name = "backGround/2/saloon",
		type = var_0_26,
		params = {
			15,
			20
		},
		states = {
			1,
			2,
			3
		}
	},
	{
		name = "backGround/1/meow",
		type = var_0_26,
		params = {
			15,
			20
		},
		states = {
			1,
			2
		}
	},
	{
		name = "backGround/1/sheriff",
		type = var_0_27,
		events = {
			var_0_19,
			var_0_18,
			var_0_20
		},
		states = {
			1,
			2,
			3
		}
	}
}
local var_0_29 = "state"
local var_0_30 = "trigger"

local function var_0_31(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = {
		def ctor:(arg_2_0)
			arg_2_0._tplCows = arg_1_0
			arg_2_0._container = arg_1_1
			arg_2_0._event = arg_1_2
			arg_2_0.cows = {}
			arg_2_0.cowWeights = {}

			for iter_2_0 = 1, #var_0_8:
				arg_2_0.cowWeights[iter_2_0] = {}

				local var_2_0 = var_0_8[iter_2_0][2]
				local var_2_1 = 0

				for iter_2_1, iter_2_2 in ipairs(var_2_0):
					var_2_1 = var_2_1 + iter_2_2

					table.insert(arg_2_0.cowWeights[iter_2_0], var_2_1),
		def start:(arg_3_0)
			arg_3_0.nextCreateTime = 0
			arg_3_0.lastTime = var_0_5

			arg_3_0.clear(),
		def step:(arg_4_0, arg_4_1)
			arg_4_0.lastTime = arg_4_0.lastTime - Time.deltaTime

			if arg_4_1 > arg_4_0.nextCreateTime:
				arg_4_0.nextCreateTime = arg_4_1 + arg_4_0.getNextCreateCowTime()

				arg_4_0.createCow()

			for iter_4_0 = 1, #arg_4_0.cows:
				local var_4_0 = arg_4_0.cows[iter_4_0].tf
				local var_4_1 = var_4_0.anchoredPosition.x
				local var_4_2 = var_4_0.anchoredPosition

				var_4_2.x = var_4_2.x - arg_4_0.cows[iter_4_0].data.speed * Time.deltaTime

				local var_4_3 = var_4_2.x

				if var_4_1 >= 0 and var_4_3 <= 0:
					arg_4_0.setCowAniamtion(var_4_0, var_0_15)

				var_4_0.anchoredPosition = var_4_2

			for iter_4_1 = #arg_4_0.cows, 1, -1:
				local var_4_4 = arg_4_0.cows[iter_4_1].tf
				local var_4_5 = var_4_4.anchoredPosition

				if var_4_4.anchoredPosition.x <= -var_0_11:
					local var_4_6 = table.remove(arg_4_0.cows, iter_4_1)

					arg_4_0.cowLeave(var_4_6.tf),
		def captureCow:(arg_5_0, arg_5_1)
			local var_5_0

			for iter_5_0 = #arg_5_0.cows, 1, -1:
				local var_5_1 = arg_5_0.cows[iter_5_0].tf
				local var_5_2 = var_5_1.anchoredPosition

				if var_5_1.anchoredPosition.x >= var_0_9[1] and var_5_1.anchoredPosition.x <= var_0_9[2]:
					if not var_5_0:
						var_5_0 = iter_5_0
					elif arg_5_0.cows[var_5_0].tf.anchoredPosition.x - var_5_1.anchoredPosition.x >= 0:
						var_5_0 = iter_5_0

			if var_5_0:
				local var_5_3 = table.remove(arg_5_0.cows, var_5_0)

				arg_5_0.setCowAniamtion(var_5_3.tf, var_0_14)

				if arg_5_1:
					arg_5_1(True)

				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_3)
				arg_5_0._event.emit(var_0_16, var_5_3.data.score)
			elif arg_5_1:
				arg_5_1(False),
		def clear:(arg_6_0)
			for iter_6_0 = 1, #arg_6_0.cows:
				Destroy(arg_6_0.cows[iter_6_0].tf)

			arg_6_0.cows = {},
		def destroy:(arg_7_0)
			arg_7_0.clear(),
		def createCow:(arg_8_0)
			local var_8_0 = arg_8_0.getCowWeightIndex()
			local var_8_1 = arg_8_0.cowWeights[var_8_0]
			local var_8_2 = math.random(0, var_8_1[#var_8_1])
			local var_8_3

			for iter_8_0 = 1, #var_8_1:
				if var_8_2 < var_8_1[iter_8_0]:
					var_8_3 = iter_8_0

					break

			var_8_3 = var_8_3 or math.random(1, #var_0_7)

			local var_8_4 = tf(Instantiate(arg_8_0._tplCows[var_8_3]))

			SetActive(var_8_4, True)
			SetParent(var_8_4, arg_8_0._container)

			var_8_4.anchoredPosition = Vector3(var_0_11, 0, 0)

			arg_8_0.setCowAniamtion(var_8_4, var_0_13)

			local var_8_5 = Clone(var_0_7[var_8_3])

			GetOrAddComponent(findTF(var_8_4, "anim"), typeof(DftAniEvent)).SetEndEvent(function()
				arg_8_0.cowLeave(var_8_4))
			table.insert(arg_8_0.cows, {
				tf = var_8_4,
				data = var_8_5
			}),
		def getCowWeightIndex:(arg_10_0)
			for iter_10_0 = 1, #var_0_8:
				if arg_10_0.lastTime and arg_10_0.lastTime < var_0_8[iter_10_0][1]:
					return iter_10_0

			return #var_0_8,
		def getNextCreateCowTime:(arg_11_0)
			local var_11_0

			for iter_11_0 = 1, #var_0_6:
				if arg_11_0.lastTime < var_0_6[iter_11_0][1]:
					local var_11_1 = var_0_6[iter_11_0][2]

					return 0.3 + var_11_1[1] + math.random() * (var_11_1[2] - var_11_1[1])

			local var_11_2 = var_0_6[#var_0_6][2]

			return math.random(var_11_2[1], var_11_2[2]),
		def setCowAniamtion:(arg_12_0, arg_12_1, arg_12_2)
			GetComponent(findTF(arg_12_1, "anim"), typeof(Animator)).SetInteger("state", arg_12_2),
		def cowLeave:(arg_13_0, arg_13_1)
			Destroy(arg_13_1)
	}

	var_1_0.ctor()

	return var_1_0

local function var_0_32(arg_14_0, arg_14_1)
	local var_14_0 = {
		def ctor:(arg_15_0)
			arg_15_0._playerTf = arg_14_0
			arg_15_0._initPosition = arg_15_0._playerTf.anchoredPosition
			arg_15_0._animator = GetComponent(findTF(arg_15_0._playerTf, "img"), typeof(Animator))

			arg_15_0.setPlayerAnim(var_0_21)

			arg_15_0._event = arg_14_1
			arg_15_0.playerDft = GetOrAddComponent(findTF(arg_15_0._playerTf, "img"), typeof(DftAniEvent))

			arg_15_0.playerDft.SetTriggerEvent(function()
				arg_15_0._event.emit(var_0_25, None, function(arg_17_0)
					if arg_17_0:
						arg_15_0.setPlayerAnim(var_0_23)
						arg_15_0._event.emit(var_0_18)
					else
						arg_15_0.setPlayerAnim(var_0_22)))
			arg_15_0.playerDft.SetEndEvent(function()
				arg_15_0._event.emit(var_0_19)),
		def throw:(arg_19_0)
			if arg_19_0.captureCdTime:
				return

			arg_19_0.captureCdTime = var_0_10

			arg_19_0.setPlayerAnim(var_0_24)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_4),
		def setPlayerAnim:(arg_20_0, arg_20_1)
			arg_20_0._animator.SetTrigger(arg_20_1),
		def start:(arg_21_0)
			arg_21_0.captureCdTime = 0,
		def getThrowTime:(arg_22_0)
			return arg_22_0.captureCdTime,
		def step:(arg_23_0, arg_23_1)
			if arg_23_0.captureCdTime:
				if arg_23_0.captureCdTime < 0:
					arg_23_0.captureCdTime = None

					arg_23_0.setPlayerAnim(var_0_21)
					arg_23_0._event.emit(var_0_20)
				else
					arg_23_0.captureCdTime = arg_23_0.captureCdTime - Time.deltaTime,
		def destory:(arg_24_0)
			return
	}

	var_14_0.ctor()

	return var_14_0

local function var_0_33(arg_25_0)
	local var_25_0 = {
		def ctor:(arg_26_0)
			arg_26_0._backSceneTf = arg_25_0

			if not arg_26_0.sceneItems:
				arg_26_0.sceneItems = {}

				for iter_26_0 = 1, #var_0_28:
					local var_26_0 = findTF(arg_26_0._backSceneTf, var_0_28[iter_26_0].name)

					table.insert(arg_26_0.sceneItems, {
						tf = var_26_0,
						data = var_0_28[iter_26_0]
					}),
		def onEventHandle:(arg_27_0, arg_27_1)
			for iter_27_0 = 1, #arg_27_0.sceneItems:
				local var_27_0 = arg_27_0.sceneItems[iter_27_0].data
				local var_27_1 = arg_27_0.sceneItems[iter_27_0].tf

				if var_27_0.type == var_0_27:
					local var_27_2 = var_27_0.events

					for iter_27_1, iter_27_2 in ipairs(var_27_2):
						if iter_27_2 == arg_27_1 and var_27_0.states:
							arg_27_0.changeSceneItemAnim(var_0_29, var_27_0.states[iter_27_1], var_27_1),
		def step:(arg_28_0, arg_28_1)
			for iter_28_0 = 1, #arg_28_0.sceneItems:
				local var_28_0 = arg_28_0.sceneItems[iter_28_0]
				local var_28_1 = var_28_0.data
				local var_28_2 = var_28_0.tf

				if var_28_1.type == var_0_26:
					if not var_28_0.time:
						var_28_0.time = math.random(var_28_1.params[1], var_28_1.params[2])
					elif var_28_0.time > 0:
						var_28_0.time = var_28_0.time - Time.deltaTime
					else
						var_28_0.time = math.random(var_28_1.params[1], var_28_1.params[2])

						if var_28_1.states:
							arg_28_0.changeSceneItemAnim(var_0_29, var_28_1.states[math.random(1, #var_28_1.states)], var_28_2)
						elif var_28_1.trigger:
							arg_28_0.changeSceneItemAnim(var_0_30, None, var_28_2),
		def changeSceneItemAnim:(arg_29_0, arg_29_1, arg_29_2, arg_29_3)
			local var_29_0 = GetComponent(arg_29_3, typeof(Animator))

			if arg_29_1 == var_0_29:
				var_29_0.SetInteger("state", arg_29_2)
			elif arg_29_1 == var_0_30:
				var_29_0.SetTrigger("trigger")
	}

	var_25_0.ctor()

	return var_25_0

def var_0_0.getUIName(arg_30_0):
	return "RopingCowGameUI"

def var_0_0.getBGM(arg_31_0):
	return var_0_1

def var_0_0.didEnter(arg_32_0):
	arg_32_0.initEvent()
	arg_32_0.initData()
	arg_32_0.initUI()
	arg_32_0.initGameUI()
	arg_32_0.updateMenuUI()
	arg_32_0.openMenuUI()

def var_0_0.initEvent(arg_33_0):
	arg_33_0.bind(var_0_16, function(arg_34_0, arg_34_1, arg_34_2)
		arg_33_0.addScore(arg_34_1)
		arg_33_0.onEventHandle(var_0_16))
	arg_33_0.bind(var_0_25, function(arg_35_0, arg_35_1, arg_35_2)
		if arg_33_0._cowController:
			arg_33_0._cowController.captureCow(arg_35_2)

		arg_33_0.onEventHandle(var_0_25))
	arg_33_0.bind(var_0_18, function(arg_36_0, arg_36_1, arg_36_2)
		arg_33_0.onEventHandle(var_0_18))
	arg_33_0.bind(var_0_19, function(arg_37_0, arg_37_1, arg_37_2)
		arg_33_0.onEventHandle(var_0_19))
	arg_33_0.bind(var_0_20, function(arg_38_0, arg_38_1, arg_38_2)
		arg_33_0.onEventHandle(var_0_20))

def var_0_0.onEventHandle(arg_39_0, arg_39_1):
	if arg_39_0._sceneItemController:
		arg_39_0._sceneItemController.onEventHandle(arg_39_1)

def var_0_0.initData(arg_40_0):
	local var_40_0 = Application.targetFrameRate or 60

	if var_40_0 > 60:
		var_40_0 = 60

	arg_40_0.timer = Timer.New(function()
		arg_40_0.onTimer(), 1 / var_40_0, -1)

def var_0_0.initUI(arg_42_0):
	arg_42_0.backSceneTf = findTF(arg_42_0._tf, "scene_background")
	arg_42_0.sceneTf = findTF(arg_42_0._tf, "scene")
	arg_42_0.clickMask = findTF(arg_42_0._tf, "clickMask")
	arg_42_0.countUI = findTF(arg_42_0._tf, "pop/CountUI")
	arg_42_0.countAnimator = GetComponent(findTF(arg_42_0.countUI, "count"), typeof(Animator))
	arg_42_0.countDft = GetOrAddComponent(findTF(arg_42_0.countUI, "count"), typeof(DftAniEvent))

	arg_42_0.countDft.SetTriggerEvent(function()
		return)
	arg_42_0.countDft.SetEndEvent(function()
		setActive(arg_42_0.countUI, False)
		arg_42_0.gameStart())

	arg_42_0.leaveUI = findTF(arg_42_0._tf, "pop/LeaveUI")

	onButton(arg_42_0, findTF(arg_42_0.leaveUI, "ad/btnOk"), function()
		arg_42_0.resumeGame()
		arg_42_0.onGameOver(), SFX_CANCEL)
	onButton(arg_42_0, findTF(arg_42_0.leaveUI, "ad/btnCancel"), function()
		arg_42_0.resumeGame(), SFX_CANCEL)

	arg_42_0.pauseUI = findTF(arg_42_0._tf, "pop/pauseUI")

	onButton(arg_42_0, findTF(arg_42_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_42_0.pauseUI, False)
		arg_42_0.resumeGame(), SFX_CANCEL)

	arg_42_0.settlementUI = findTF(arg_42_0._tf, "pop/SettleMentUI")

	onButton(arg_42_0, findTF(arg_42_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_42_0.settlementUI, False)
		arg_42_0.openMenuUI(), SFX_CANCEL)

	arg_42_0.menuUI = findTF(arg_42_0._tf, "pop/menuUI")
	arg_42_0.battleScrollRect = GetComponent(findTF(arg_42_0.menuUI, "battList"), typeof(ScrollRect))
	arg_42_0.totalTimes = arg_42_0.getGameTotalTime()

	local var_42_0 = arg_42_0.getGameUsedTimes() - 4 < 0 and 0 or arg_42_0.getGameUsedTimes() - 4

	scrollTo(arg_42_0.battleScrollRect, 0, 1 - var_42_0 / (arg_42_0.totalTimes - 4))
	onButton(arg_42_0, findTF(arg_42_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_49_0 = arg_42_0.battleScrollRect.normalizedPosition.y + 1 / (arg_42_0.totalTimes - 4)

		if var_49_0 > 1:
			var_49_0 = 1

		scrollTo(arg_42_0.battleScrollRect, 0, var_49_0), SFX_CANCEL)
	onButton(arg_42_0, findTF(arg_42_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_50_0 = arg_42_0.battleScrollRect.normalizedPosition.y - 1 / (arg_42_0.totalTimes - 4)

		if var_50_0 < 0:
			var_50_0 = 0

		scrollTo(arg_42_0.battleScrollRect, 0, var_50_0), SFX_CANCEL)
	onButton(arg_42_0, findTF(arg_42_0.menuUI, "btnBack"), function()
		arg_42_0.closeView(), SFX_CANCEL)
	onButton(arg_42_0, findTF(arg_42_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.cowboy_tips.tip
		}), SFX_CANCEL)
	onButton(arg_42_0, findTF(arg_42_0.menuUI, "btnStart"), function()
		setActive(arg_42_0.menuUI, False)
		arg_42_0.readyStart(), SFX_CANCEL)

	local var_42_1 = findTF(arg_42_0.menuUI, "tplBattleItem")

	arg_42_0.battleItems = {}
	arg_42_0.dropItems = {}

	local var_42_2 = pg.mini_game[arg_42_0.GetMGData().id].simple_config_data.drop

	for iter_42_0 = 1, #var_42_2:
		local var_42_3 = tf(instantiate(var_42_1))

		var_42_3.name = "battleItem_" .. iter_42_0

		setParent(var_42_3, findTF(arg_42_0.menuUI, "battList/Viewport/Content"))

		local var_42_4 = iter_42_0

		GetSpriteFromAtlasAsync("ui/minigameui/ropingcowgameui_atlas", "battleDesc" .. var_42_4, function(arg_54_0)
			setImageSprite(findTF(var_42_3, "state_open/buttomDesc"), arg_54_0, True)
			setImageSprite(findTF(var_42_3, "state_clear/buttomDesc"), arg_54_0, True)
			setImageSprite(findTF(var_42_3, "state_current/buttomDesc"), arg_54_0, True)
			setImageSprite(findTF(var_42_3, "state_closed/buttomDesc"), arg_54_0, True))

		local var_42_5 = findTF(var_42_3, "icon")
		local var_42_6 = {
			type = var_42_2[iter_42_0][1],
			id = var_42_2[iter_42_0][2],
			amount = var_42_2[iter_42_0][3]
		}

		updateDrop(var_42_5, var_42_6)
		onButton(arg_42_0, var_42_5, function()
			arg_42_0.emit(BaseUI.ON_DROP, var_42_6), SFX_PANEL)
		table.insert(arg_42_0.dropItems, var_42_5)
		setActive(var_42_3, True)
		table.insert(arg_42_0.battleItems, var_42_3)

	if not arg_42_0.handle:
		arg_42_0.handle = UpdateBeat.CreateListener(arg_42_0.Update, arg_42_0)

	UpdateBeat.AddListener(arg_42_0.handle)

def var_0_0.initGameUI(arg_56_0):
	arg_56_0.gameUI = findTF(arg_56_0._tf, "ui/gameUI")

	onButton(arg_56_0, findTF(arg_56_0.gameUI, "topRight/btnStop"), function()
		arg_56_0.stopGame()
		setActive(arg_56_0.pauseUI, True))
	onButton(arg_56_0, findTF(arg_56_0.gameUI, "btnLeave"), function()
		arg_56_0.stopGame()
		setActive(arg_56_0.leaveUI, True))

	arg_56_0.gameTimeS = findTF(arg_56_0.gameUI, "top/time/s")
	arg_56_0.scoreTf = findTF(arg_56_0.gameUI, "top/score")
	arg_56_0.btnCapture = findTF(arg_56_0.gameUI, "btnCapture")
	arg_56_0.captureButton = GetOrAddComponent(arg_56_0.btnCapture, "EventTriggerListener")

	arg_56_0.captureButton.AddPointDownFunc(function(arg_59_0, arg_59_1)
		if arg_56_0._playerController:
			arg_56_0._playerController.throw())

	local var_56_0 = findTF(arg_56_0.sceneTf, "cowContainer")
	local var_56_1 = {}

	for iter_56_0 = 1, var_0_12:
		local var_56_2 = findTF(arg_56_0.sceneTf, "cow" .. iter_56_0)

		table.insert(var_56_1, var_56_2)

	arg_56_0.sceneScoreTf = findTF(arg_56_0.sceneTf, "score")
	arg_56_0._playerController = var_0_32(findTF(arg_56_0.sceneTf, "player"), arg_56_0)
	arg_56_0._cowController = var_0_31(var_56_1, var_56_0, arg_56_0)
	arg_56_0._sceneItemController = var_0_33(arg_56_0.backSceneTf)

def var_0_0.Update(arg_60_0):
	arg_60_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_61_0):
	if arg_61_0.gameStop or arg_61_0.settlementFlag:
		return

	if IsUnityEditor and Input.GetKeyDown(KeyCode.S) and arg_61_0._playerController:
		arg_61_0._playerController.throw()

def var_0_0.updateMenuUI(arg_62_0):
	local var_62_0 = arg_62_0.getGameUsedTimes()
	local var_62_1 = arg_62_0.getGameTimes()

	for iter_62_0 = 1, #arg_62_0.battleItems:
		setActive(findTF(arg_62_0.battleItems[iter_62_0], "state_open"), False)
		setActive(findTF(arg_62_0.battleItems[iter_62_0], "state_closed"), False)
		setActive(findTF(arg_62_0.battleItems[iter_62_0], "state_clear"), False)
		setActive(findTF(arg_62_0.battleItems[iter_62_0], "state_current"), False)

		if iter_62_0 <= var_62_0:
			SetParent(arg_62_0.dropItems[iter_62_0], findTF(arg_62_0.battleItems[iter_62_0], "state_clear/icon"))
			setActive(arg_62_0.dropItems[iter_62_0], True)
			setActive(findTF(arg_62_0.battleItems[iter_62_0], "state_clear"), True)
		elif iter_62_0 == var_62_0 + 1 and var_62_1 >= 1:
			setActive(findTF(arg_62_0.battleItems[iter_62_0], "state_current"), True)
			SetParent(arg_62_0.dropItems[iter_62_0], findTF(arg_62_0.battleItems[iter_62_0], "state_current/icon"))
			setActive(arg_62_0.dropItems[iter_62_0], True)
		elif var_62_0 < iter_62_0 and iter_62_0 <= var_62_0 + var_62_1:
			setActive(findTF(arg_62_0.battleItems[iter_62_0], "state_open"), True)
			SetParent(arg_62_0.dropItems[iter_62_0], findTF(arg_62_0.battleItems[iter_62_0], "state_open/icon"))
			setActive(arg_62_0.dropItems[iter_62_0], True)
		else
			setActive(findTF(arg_62_0.battleItems[iter_62_0], "state_closed"), True)
			setActive(arg_62_0.dropItems[iter_62_0], False)

	arg_62_0.totalTimes = arg_62_0.getGameTotalTime()

	local var_62_2 = 1 - (arg_62_0.getGameUsedTimes() - 3 < 0 and 0 or arg_62_0.getGameUsedTimes() - 3) / (arg_62_0.totalTimes - 4)

	if var_62_2 > 1:
		var_62_2 = 1

	scrollTo(arg_62_0.battleScrollRect, 0, var_62_2)
	setActive(findTF(arg_62_0.menuUI, "btnStart/tip"), var_62_1 > 0)
	arg_62_0.CheckGet()

def var_0_0.CheckGet(arg_63_0):
	setActive(findTF(arg_63_0.menuUI, "got"), False)

	if arg_63_0.getUltimate() and arg_63_0.getUltimate() != 0:
		setActive(findTF(arg_63_0.menuUI, "got"), True)

	if arg_63_0.getUltimate() == 0:
		if arg_63_0.getGameTotalTime() > arg_63_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_63_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_63_0.menuUI, "got"), True)

def var_0_0.openMenuUI(arg_64_0):
	setActive(findTF(arg_64_0._tf, "scene_front"), False)
	setActive(findTF(arg_64_0._tf, "scene_background"), False)
	setActive(findTF(arg_64_0._tf, "scene"), False)
	setActive(arg_64_0.gameUI, False)
	setActive(arg_64_0.menuUI, True)
	arg_64_0.updateMenuUI()

def var_0_0.clearUI(arg_65_0):
	setActive(arg_65_0.sceneTf, False)
	setActive(arg_65_0.settlementUI, False)
	setActive(arg_65_0.countUI, False)
	setActive(arg_65_0.menuUI, False)
	setActive(arg_65_0.gameUI, False)

def var_0_0.readyStart(arg_66_0):
	setActive(arg_66_0.countUI, True)
	arg_66_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_2)

def var_0_0.gameStart(arg_67_0):
	setActive(findTF(arg_67_0._tf, "scene_front"), True)
	setActive(findTF(arg_67_0._tf, "scene_background"), True)
	setActive(findTF(arg_67_0._tf, "scene"), True)
	setActive(arg_67_0.gameUI, True)

	arg_67_0.gameStartFlag = True
	arg_67_0.scoreNum = 0
	arg_67_0.playerPosIndex = 2
	arg_67_0.gameStepTime = 0
	arg_67_0.heart = 3
	arg_67_0.gameTime = var_0_5

	if arg_67_0._cowController:
		arg_67_0._cowController.start()

	if arg_67_0._playerController:
		arg_67_0._playerController.start()

	arg_67_0.updateGameUI()
	arg_67_0.timerStart()

def var_0_0.getGameTimes(arg_68_0):
	return arg_68_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_69_0):
	return arg_69_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_70_0):
	return arg_70_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_71_0):
	return (arg_71_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.changeSpeed(arg_72_0, arg_72_1):
	return

def var_0_0.onTimer(arg_73_0):
	arg_73_0.gameStep()

def var_0_0.gameStep(arg_74_0):
	arg_74_0.gameTime = arg_74_0.gameTime - Time.deltaTime

	if arg_74_0.gameTime < 0:
		arg_74_0.gameTime = 0

	arg_74_0.gameStepTime = arg_74_0.gameStepTime + Time.deltaTime

	if arg_74_0._cowController:
		arg_74_0._cowController.step(arg_74_0.gameStepTime)

	if arg_74_0._playerController:
		arg_74_0._playerController.step(arg_74_0.gameStepTime)

	if arg_74_0._sceneItemController:
		arg_74_0._sceneItemController.step(arg_74_0.gameStepTime)

	arg_74_0.updateGameUI()

	if arg_74_0.gameTime <= 0:
		arg_74_0.onGameOver()

		return

def var_0_0.timerStart(arg_75_0):
	if not arg_75_0.timer.running:
		arg_75_0.timer.Start()

def var_0_0.timerStop(arg_76_0):
	if arg_76_0.timer.running:
		arg_76_0.timer.Stop()

def var_0_0.updateGameUI(arg_77_0):
	setText(arg_77_0.scoreTf, arg_77_0.scoreNum)
	setText(arg_77_0.gameTimeS, math.ceil(arg_77_0.gameTime))

	if not arg_77_0.captureCdMaskImg:
		arg_77_0.captureCdMaskImg = GetComponent(findTF(arg_77_0.btnCapture, "cd"), typeof(Image))

	if arg_77_0._playerController:
		local var_77_0 = arg_77_0._playerController.getThrowTime()

		if var_77_0 and var_77_0 > 0:
			local var_77_1 = var_77_0 / var_0_10

			arg_77_0.captureCdMaskImg.fillAmount = var_77_1
		else
			arg_77_0.captureCdMaskImg.fillAmount = 0

def var_0_0.addScore(arg_78_0, arg_78_1):
	arg_78_0.scoreNum = arg_78_0.scoreNum + arg_78_1

	if arg_78_0.scoreNum < 0:
		arg_78_0.scoreNum = 0

	setActive(arg_78_0.sceneScoreTf, False)

	for iter_78_0 = 0, arg_78_0.sceneScoreTf.childCount - 1:
		local var_78_0 = arg_78_0.sceneScoreTf.GetChild(iter_78_0)

		if var_78_0.name == tostring(arg_78_1):
			setActive(var_78_0, True)
		else
			setActive(var_78_0, False)

	setActive(arg_78_0.sceneScoreTf, True)

def var_0_0.onGameOver(arg_79_0):
	if arg_79_0.settlementFlag:
		return

	arg_79_0.timerStop()

	arg_79_0.settlementFlag = True

	setActive(arg_79_0.sceneScoreTf, False)
	setActive(arg_79_0.clickMask, True)

	if arg_79_0._cowController:
		arg_79_0._cowController.clear()

	LeanTween.delayedCall(go(arg_79_0._tf), 0.1, System.Action(function()
		arg_79_0.settlementFlag = False
		arg_79_0.gameStartFlag = False

		setActive(arg_79_0.clickMask, False)
		arg_79_0.showSettlement()))

def var_0_0.showSettlement(arg_81_0):
	setActive(arg_81_0.settlementUI, True)
	GetComponent(findTF(arg_81_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_81_0 = arg_81_0.GetMGData().GetRuntimeData("elements")
	local var_81_1 = arg_81_0.scoreNum
	local var_81_2 = var_81_0 and #var_81_0 > 0 and var_81_0[1] or 0

	setActive(findTF(arg_81_0.settlementUI, "ad/new"), var_81_2 < var_81_1)

	if var_81_2 <= var_81_1:
		var_81_2 = var_81_1

		arg_81_0.StoreDataToServer({
			var_81_2
		})

	local var_81_3 = findTF(arg_81_0.settlementUI, "ad/highText")
	local var_81_4 = findTF(arg_81_0.settlementUI, "ad/currentText")

	setText(var_81_3, var_81_2)
	setText(var_81_4, var_81_1)

	if arg_81_0.getGameTimes() and arg_81_0.getGameTimes() > 0:
		arg_81_0.sendSuccessFlag = True

		arg_81_0.SendSuccess(0)

def var_0_0.resumeGame(arg_82_0):
	arg_82_0.gameStop = False

	setActive(arg_82_0.leaveUI, False)
	arg_82_0.changeSpeed(1)
	arg_82_0.timerStart()

def var_0_0.stopGame(arg_83_0):
	arg_83_0.gameStop = True

	arg_83_0.timerStop()
	arg_83_0.changeSpeed(0)

def var_0_0.onBackPressed(arg_84_0):
	if not arg_84_0.gameStartFlag:
		arg_84_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_84_0.settlementFlag:
			return

		if isActive(arg_84_0.pauseUI):
			setActive(arg_84_0.pauseUI, False)

		arg_84_0.stopGame()
		setActive(arg_84_0.leaveUI, True)

def var_0_0.willExit(arg_85_0):
	if arg_85_0.handle:
		UpdateBeat.RemoveListener(arg_85_0.handle)

	if arg_85_0._tf and LeanTween.isTweening(go(arg_85_0._tf)):
		LeanTween.cancel(go(arg_85_0._tf))

	if arg_85_0.timer and arg_85_0.timer.running:
		arg_85_0.timer.Stop()

	Time.timeScale = 1
	arg_85_0.timer = None

return var_0_0
