local var_0_0 = class("EatFoodGameView", import("..BaseMiniGameView"))
local var_0_1 = "xinnong-1"
local var_0_2 = "event./ui/ddldaoshu2"
local var_0_3 = "event./ui/zhengque"
local var_0_4 = "event./ui/shibai2"
local var_0_5 = "event./ui/deshou"
local var_0_6 = "event./ui/shibai"
local var_0_7 = 60
local var_0_8 = "ui/eatfoodgameui_atlas"
local var_0_9 = "salvage_tips"
local var_0_10 = 2.5
local var_0_11 = 3.75
local var_0_12 = {
	0,
	600
}
local var_0_13 = {
	150,
	150,
	150,
	140,
	140,
	140,
	130,
	130,
	130,
	120,
	120,
	120,
	110,
	110,
	100
}
local var_0_14 = {
	8,
	8,
	9,
	9,
	10,
	10,
	11,
	11,
	12,
	12,
	13,
	13,
	14,
	15,
	16,
	17,
	18,
	20
}
local var_0_15 = 400
local var_0_16 = 1
local var_0_17 = "event touch"
local var_0_18 = {
	15,
	25,
	40,
	75
}
local var_0_19 = {
	500,
	300,
	150,
	50
}
local var_0_20 = {
	-400,
	-300,
	-200,
	-100
}
local var_0_21 = {
	20,
	40,
	60,
	100
}
local var_0_22 = 0.8
local var_0_23 = 0.05
local var_0_24 = 1.4
local var_0_25 = {
	{
		id = 1,
		next_time = {
			3.5,
			4
		}
	},
	{
		id = 2,
		next_time = {
			3.5,
			4
		}
	},
	{
		id = 4,
		next_time = {
			3.5,
			4
		}
	}
}
local var_0_26 = 2
local var_0_27 = {
	1,
	3
}
local var_0_28 = 15
local var_0_29 = {
	3,
	6,
	9,
	11,
	13,
	15
}
local var_0_30 = 10
local var_0_31 = {
	{
		id = 3
	}
}
local var_0_32 = "event game over"

local function var_0_33(arg_1_0, arg_1_1)
	local var_1_0 = {
		def ctor:(arg_2_0)
			arg_2_0._tf = arg_1_0
			arg_2_0._event = arg_1_1

			setActive(arg_2_0._tf, False)

			arg_2_0.sliderTouch = findTF(arg_2_0._tf, "touch")

			setActive(arg_2_0.sliderTouch, True)

			arg_2_0.sliderRange = findTF(arg_2_0._tf, "range")
			arg_2_0.sliderRange.anchoredPosition = Vector2(var_0_15, 0),
		def start:(arg_3_0)
			arg_3_0.sliderIndex = 1
			arg_3_0.nextSliderTime = var_0_11
			arg_3_0.sliderTouchPos = Vector2(var_0_12[1], 0)

			arg_3_0.setSliderBarVisible(False),
		def step:(arg_4_0)
			if arg_4_0.nextSliderTime:
				arg_4_0.nextSliderTime = arg_4_0.nextSliderTime - Time.deltaTime

				if arg_4_0.nextSliderTime <= 0:
					arg_4_0.setSliderBarVisible(True)
					arg_4_0.startSliderBar()

					arg_4_0.nextSliderTime = arg_4_0.nextSliderTime + var_0_10

			if arg_4_0.sliderBeginning:
				arg_4_0.sliderTouchPos.x = arg_4_0.sliderTouchPos.x + arg_4_0.speed
				arg_4_0.sliderTouch.anchoredPosition = arg_4_0.sliderTouchPos

				if arg_4_0.sliderTouchPos.x > var_0_12[2]:
					arg_4_0.touch(False),
		def setSliderBarVisible:(arg_5_0, arg_5_1)
			setActive(arg_5_0._tf, arg_5_1),
		def startSliderBar:(arg_6_0)
			if arg_6_0.sliderIndex > #var_0_13:
				arg_6_0.sliderIndex = 1

			arg_6_0.sliderWidth = var_0_13[arg_6_0.sliderIndex]
			arg_6_0.speed = var_0_14[arg_6_0.sliderIndex]
			arg_6_0.sliderTouchPos.x = var_0_12[1]
			arg_6_0.sliderBeginning = True
			arg_6_0.sliderRange.sizeDelta = Vector2(arg_6_0.sliderWidth, arg_6_0.sliderRange.sizeDelta.y),
		def touch:(arg_7_0, arg_7_1)
			if not arg_7_0.sliderBeginning:
				return

			arg_7_0.sliderBeginning = False

			arg_7_0.setSliderBarVisible(False)

			local var_7_0 = False
			local var_7_1 = 0
			local var_7_2 = math.abs(arg_7_0.sliderTouchPos.x - var_0_15)
			local var_7_3

			if var_7_2 < arg_7_0.sliderWidth / 2:
				var_7_1 = arg_7_0.getScore(var_7_2)
				arg_7_0.sliderIndex = arg_7_0.sliderIndex + 1
				var_7_3 = True
			else
				if arg_7_0.sliderTouchPos.x < 100 or arg_7_0.sliderTouchPos.x > var_0_12[2] - 100:
					var_7_1 = arg_7_0.getSubScore(arg_7_0.sliderTouchPos.x)

				arg_7_0.nextSliderTime = arg_7_0.nextSliderTime + var_0_16
				var_7_3 = False

			if var_7_3:
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_5)
			else
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_6)

			if arg_7_1:
				arg_7_0._event.emit(var_0_17, {
					flag = var_7_3,
					score = var_7_1
				}, function()
					return),
		def getSubScore:(arg_9_0, arg_9_1)
			local var_9_0

			if arg_9_1 <= 100:
				var_9_0 = arg_9_1
			else
				var_9_0 = var_0_12[2] - arg_9_1

			for iter_9_0 = 1, #var_0_21:
				if var_9_0 < var_0_21[iter_9_0]:
					return var_0_20[iter_9_0]

			return 0,
		def getScore:(arg_10_0, arg_10_1)
			for iter_10_0 = 1, #var_0_18:
				if arg_10_1 < var_0_18[iter_10_0]:
					return var_0_19[iter_10_0]

			return 0,
		def destroy:(arg_11_0)
			return
	}

	var_1_0.ctor()

	return var_1_0

local function var_0_34(arg_12_0, arg_12_1, arg_12_2, arg_12_3)
	local var_12_0 = {
		def ctor:(arg_13_0)
			arg_13_0._charTpls = arg_12_0
			arg_13_0._foodTpl = arg_12_1
			arg_13_0._container = arg_12_2
			arg_13_0._event = arg_12_3,
		def start:(arg_14_0)
			arg_14_0.clear()

			arg_14_0.player = None
			arg_14_0.chars = {}
			arg_14_0.animateSpeed = var_0_22
			arg_14_0.playerNextStepTimes = {}

			arg_14_0.create(),
		def step:(arg_15_0)
			for iter_15_0 = 1, #arg_15_0.chars:
				local var_15_0 = arg_15_0.chars[iter_15_0]

				if not var_15_0.nextTime:
					var_15_0.nextTime = math.random(var_15_0.next_time[1], var_15_0.next_time[2])
				else
					var_15_0.nextTime = var_15_0.nextTime - Time.deltaTime

					if var_15_0.nextTime <= 0:
						var_15_0.nextTime = None
						var_15_0.stepIndex = var_15_0.stepIndex + 1

						if table.contains(var_0_29, var_15_0.stepIndex):
							var_15_0.tfAnimator.SetTrigger("next")

						if var_15_0.stepIndex == var_0_30:
							var_15_0.tfAnimator.SetBool("eat", False)
							var_15_0.tfAnimator.SetBool("bite", True)

						if var_15_0.stepIndex >= var_0_28:
							arg_15_0.setWinChar(var_15_0),
		def setWinChar:(arg_16_0, arg_16_1)
			local var_16_0 = False

			if arg_16_1:
				var_16_0 = arg_16_1.isPlayer
				arg_16_1.foodState = 6

				arg_16_1.foodTfAnimator.SetInteger("state", arg_16_1.foodState)

			if arg_16_0.player == arg_16_1:
				arg_16_0.player.tfAnimator.SetTrigger("victory")
			else
				arg_16_0.player.tfAnimator.SetTrigger("defeat")

			for iter_16_0 = 1, #arg_16_0.chars:
				local var_16_1 = arg_16_0.chars[iter_16_0]

				if var_16_1 == arg_16_1:
					var_16_1.tfAnimator.SetTrigger("victory")
				else
					var_16_1.tfAnimator.SetTrigger("defeat")

			arg_16_0._event.emit(var_0_32, var_16_0, function()
				return),
		def onPlayerTouch:(arg_18_0, arg_18_1)
			if arg_18_0.player:
				if arg_18_1.flag:
					arg_18_0.player.stepIndex = arg_18_0.player.stepIndex + 1

					if table.contains(var_0_29, arg_18_0.player.stepIndex) and not table.contains(arg_18_0.playerNextStepTimes, arg_18_0.player.stepIndex):
						table.insert(arg_18_0.playerNextStepTimes, arg_18_0.player.stepIndex)
						arg_18_0.player.tfAnimator.SetTrigger("next")

					if arg_18_0.player.stepIndex == var_0_30:
						arg_18_0.player.tfAnimator.SetBool("eat", False)
						arg_18_0.player.tfAnimator.SetBool("bite", True)

					if arg_18_0.player.stepIndex >= var_0_28:
						arg_18_0.setWinChar(arg_18_0.player)

					arg_18_0.animateSpeed = arg_18_0.animateSpeed + var_0_23

					if arg_18_0.animateSpeed > var_0_24:
						arg_18_0.animateSpeed = var_0_24

					arg_18_0.player.tfAnimator.speed = arg_18_0.animateSpeed
				else
					arg_18_0.animateSpeed = arg_18_0.animateSpeed - var_0_23

					if arg_18_0.animateSpeed < var_0_22:
						arg_18_0.animateSpeed = var_0_22

					arg_18_0.player.tfAnimator.speed = arg_18_0.animateSpeed

					arg_18_0.player.tfAnimator.SetTrigger("miss"),
		def create:(arg_19_0)
			local var_19_0 = Clone(var_0_31)
			local var_19_1 = table.remove(var_19_0, math.random(1, #var_19_0))

			arg_19_0.player = arg_19_0.getCharById(var_19_1, var_0_26)

			local var_19_2 = Clone(var_0_25)

			for iter_19_0 = 1, #var_0_27:
				local var_19_3 = table.remove(var_19_2, math.random(1, #var_19_2))
				local var_19_4 = arg_19_0.getCharById(var_19_3, var_0_27[iter_19_0])

				table.insert(arg_19_0.chars, var_19_4),
		def getCharById:(arg_20_0, arg_20_1, arg_20_2)
			local var_20_0 = {}
			local var_20_1 = tf(instantiate(findTF(arg_20_0._charTpls, "char" .. arg_20_1.id)))
			local var_20_2 = tf(instantiate(arg_20_0._foodTpl))

			setParent(var_20_1, findTF(arg_20_0._container, tostring(arg_20_2)))
			setActive(var_20_1, True)
			setParent(var_20_2, findTF(arg_20_0._container, tostring(arg_20_2)))
			setActive(var_20_2, True)

			var_20_2.anchoredPosition = Vector2(0, -300)
			var_20_1.anchoredPosition = Vector2(0, 0)
			var_20_0.tf = var_20_1
			var_20_0.tfAnimator = GetComponent(findTF(var_20_1, "anim"), typeof(Animator))
			var_20_0.tfAnimator.speed = arg_20_0.animateSpeed
			var_20_0.foodTf = var_20_2
			var_20_0.foodTfAnimator = GetComponent(findTF(var_20_2, "anim"), typeof(Animator))
			var_20_0.foodTfAnimator.speed = var_0_22
			var_20_0.next_time = arg_20_1.next_time

			if not var_20_0.next_time:
				var_20_0.isPlayer = True
			else
				var_20_0.nextTime = math.random(0, arg_20_1.next_time[2] - arg_20_1.next_time[1]) + arg_20_1.next_time[1] + var_0_11

			var_20_0.foodState = 0
			var_20_0.stepIndex = 0

			local var_20_3 = GetComponent(findTF(var_20_1, "anim"), typeof(DftAniEvent))

			var_20_3.SetStartEvent(function()
				var_20_0.foodState = var_20_0.foodState + 1

				var_20_0.foodTfAnimator.SetInteger("state", var_20_0.foodState))
			var_20_3.SetTriggerEvent(function()
				return)
			var_20_3.SetEndEvent(function()
				return)

			return var_20_0,
		def stop:(arg_24_0)
			if arg_24_0.player:
				arg_24_0.player.tfAnimator.speed = 0

			if arg_24_0.chars and #arg_24_0.chars > 0:
				for iter_24_0 = 1, #arg_24_0.chars:
					arg_24_0.chars[iter_24_0].tfAnimator.speed = 0,
		def resume:(arg_25_0)
			if arg_25_0.player:
				arg_25_0.player.tfAnimator.speed = arg_25_0.animateSpeed

			if arg_25_0.chars and #arg_25_0.chars > 0:
				for iter_25_0 = 1, #arg_25_0.chars:
					arg_25_0.chars[iter_25_0].tfAnimator.speed = var_0_22,
		def onTimeOut:(arg_26_0)
			local var_26_0 = arg_26_0.player
			local var_26_1 = arg_26_0.player.stepIndex or 0

			for iter_26_0 = 1, #arg_26_0.chars:
				if var_26_1 < arg_26_0.chars[iter_26_0].stepIndex:
					var_26_0 = arg_26_0.chars[iter_26_0]
					var_26_1 = arg_26_0.chars[iter_26_0].stepIndex

			arg_26_0.setWinChar(var_26_0),
		def clear:(arg_27_0)
			if arg_27_0.player:
				destroy(arg_27_0.player.tf)
				destroy(arg_27_0.player.foodTf)

			if arg_27_0.chars:
				for iter_27_0 = 1, #arg_27_0.chars:
					destroy(arg_27_0.chars[iter_27_0].tf)
					destroy(arg_27_0.chars[iter_27_0].foodTf)
	}

	var_12_0.ctor()

	return var_12_0

def var_0_0.getUIName(arg_28_0):
	return "EatFoodGameUI"

def var_0_0.getBGM(arg_29_0):
	return var_0_1

def var_0_0.didEnter(arg_30_0):
	arg_30_0.initEvent()
	arg_30_0.initData()
	arg_30_0.initUI()
	arg_30_0.initGameUI()
	arg_30_0.readyStart()

def var_0_0.OnGetAwardDone(arg_31_0):
	arg_31_0.CheckGet()

def var_0_0.OnSendMiniGameOPDone(arg_32_0, arg_32_1):
	return

def var_0_0.initEvent(arg_33_0):
	arg_33_0.bind(var_0_32, function(arg_34_0, arg_34_1, arg_34_2)
		arg_33_0.setGameOver(arg_34_1))
	arg_33_0.bind(var_0_17, function(arg_35_0, arg_35_1, arg_35_2)
		if arg_35_1.score and arg_35_1.score != 0:
			arg_33_0.addScore(arg_35_1.score)

		if arg_33_0.charController:
			arg_33_0.charController.onPlayerTouch(arg_35_1))

def var_0_0.initData(arg_36_0):
	arg_36_0.dropData = pg.mini_game[arg_36_0.GetMGData().id].simple_config_data.drop

	local var_36_0 = Application.targetFrameRate or 60

	if var_36_0 > 60:
		var_36_0 = 60

	arg_36_0.timer = Timer.New(function()
		arg_36_0.onTimer(), 1 / var_36_0, -1)

def var_0_0.initUI(arg_38_0):
	arg_38_0.backSceneTf = findTF(arg_38_0._tf, "scene_container/scene_background")
	arg_38_0.sceneTf = findTF(arg_38_0._tf, "scene_container/scene")
	arg_38_0.bgTf = findTF(arg_38_0._tf, "bg")
	arg_38_0.clickMask = findTF(arg_38_0._tf, "clickMask")
	arg_38_0.countUI = findTF(arg_38_0._tf, "pop/CountUI")
	arg_38_0.countAnimator = GetComponent(findTF(arg_38_0.countUI, "count"), typeof(Animator))
	arg_38_0.countDft = GetOrAddComponent(findTF(arg_38_0.countUI, "count"), typeof(DftAniEvent))

	arg_38_0.countDft.SetTriggerEvent(function()
		return)
	arg_38_0.countDft.SetEndEvent(function()
		setActive(arg_38_0.countUI, False)

		arg_38_0.readyStart = False)
	SetActive(arg_38_0.countUI, False)

	arg_38_0.leaveUI = findTF(arg_38_0._tf, "pop/LeaveUI")

	onButton(arg_38_0, findTF(arg_38_0.leaveUI, "ad/btnOk"), function()
		arg_38_0.resumeGame()

		if arg_38_0.charController:
			arg_38_0.charController.stop()

		arg_38_0.onGameOver(0), SFX_CANCEL)
	onButton(arg_38_0, findTF(arg_38_0.leaveUI, "ad/btnCancel"), function()
		arg_38_0.resumeGame(), SFX_CANCEL)
	SetActive(arg_38_0.leaveUI, False)

	arg_38_0.pauseUI = findTF(arg_38_0._tf, "pop/pauseUI")

	onButton(arg_38_0, findTF(arg_38_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_38_0.pauseUI, False)
		arg_38_0.resumeGame(), SFX_CANCEL)
	SetActive(arg_38_0.pauseUI, False)

	arg_38_0.resultUI = findTF(arg_38_0._tf, "pop/resultUI")

	SetActive(arg_38_0.resultUI, False)

	arg_38_0.settlementUI = findTF(arg_38_0._tf, "pop/SettleMentUI")

	onButton(arg_38_0, findTF(arg_38_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_38_0.settlementUI, False)
		arg_38_0.closeView(), SFX_CANCEL)
	SetActive(arg_38_0.settlementUI, False)

	if not arg_38_0.handle:
		arg_38_0.handle = UpdateBeat.CreateListener(arg_38_0.Update, arg_38_0)

	UpdateBeat.AddListener(arg_38_0.handle)

def var_0_0.initGameUI(arg_45_0):
	arg_45_0.gameUI = findTF(arg_45_0._tf, "ui/gameUI")

	onButton(arg_45_0, findTF(arg_45_0.gameUI, "topRight/btnStop"), function()
		arg_45_0.stopGame()
		setActive(arg_45_0.pauseUI, True))
	onButton(arg_45_0, findTF(arg_45_0.gameUI, "btnLeave"), function()
		arg_45_0.stopGame()
		setActive(arg_45_0.leaveUI, True))

	arg_45_0.dragDelegate = GetOrAddComponent(arg_45_0.sceneTf, "EventTriggerListener")
	arg_45_0.dragDelegate.enabled = True

	arg_45_0.dragDelegate.AddPointDownFunc(function(arg_48_0, arg_48_1)
		if arg_45_0.sliderController:
			arg_45_0.sliderController.touch(True))

	arg_45_0.gameTimeS = findTF(arg_45_0.gameUI, "top/time/s")
	arg_45_0.scoreTf = findTF(arg_45_0.gameUI, "top/score")
	arg_45_0.sceneScoreTf = findTF(arg_45_0.sceneTf, "score")
	arg_45_0.sliderController = var_0_33(findTF(arg_45_0.sceneTf, "collider"), arg_45_0)
	arg_45_0.charController = var_0_34(findTF(arg_45_0.sceneTf, "tpls"), findTF(arg_45_0.sceneTf, "food"), findTF(arg_45_0.sceneTf, "container"), arg_45_0)

def var_0_0.Update(arg_49_0):
	arg_49_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_50_0):
	if arg_50_0.gameStop or arg_50_0.settlementFlag:
		return

	if IsUnityEditor:
		-- block empty

def var_0_0.updateMenuUI(arg_51_0):
	return

def var_0_0.CheckGet(arg_52_0):
	if arg_52_0.getUltimate() == 0:
		if arg_52_0.getGameTotalTime() > arg_52_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_52_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})

def var_0_0.openMenuUI(arg_53_0):
	setActive(findTF(arg_53_0._tf, "scene_container"), False)
	setActive(findTF(arg_53_0.bgTf, "on"), True)
	setActive(arg_53_0.gameUI, False)
	setActive(arg_53_0.menuUI, True)

def var_0_0.clearUI(arg_54_0):
	setActive(arg_54_0.sceneTf, False)
	setActive(arg_54_0.settlementUI, False)
	setActive(arg_54_0.countUI, False)
	setActive(arg_54_0.menuUI, False)
	setActive(arg_54_0.gameUI, False)

def var_0_0.readyStart(arg_55_0):
	setActive(arg_55_0.countUI, True)
	arg_55_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_2)

	arg_55_0.readyStart = True

	arg_55_0.gameStart()

def var_0_0.getGameTimes(arg_56_0):
	return arg_56_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_57_0):
	return arg_57_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_58_0):
	return arg_58_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_59_0):
	return (arg_59_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.gameStart(arg_60_0):
	setActive(findTF(arg_60_0._tf, "scene_container"), True)
	setActive(findTF(arg_60_0.bgTf, "on"), False)
	setActive(arg_60_0.gameUI, True)

	arg_60_0.gameStartFlag = True
	arg_60_0.scoreNum = 0
	arg_60_0.playerPosIndex = 2
	arg_60_0.gameStepTime = 0
	arg_60_0.gameTime = var_0_7

	if arg_60_0.sliderController:
		arg_60_0.sliderController.start()

	if arg_60_0.charController:
		arg_60_0.charController.start()

	arg_60_0.updateGameUI()
	arg_60_0.timerStart()

def var_0_0.transformColor(arg_61_0, arg_61_1):
	local var_61_0 = tonumber(string.sub(arg_61_1, 1, 2), 16)
	local var_61_1 = tonumber(string.sub(arg_61_1, 3, 4), 16)
	local var_61_2 = tonumber(string.sub(arg_61_1, 5, 6), 16)

	return Color.New(var_61_0 / 255, var_61_1 / 255, var_61_2 / 255)

def var_0_0.addScore(arg_62_0, arg_62_1, arg_62_2):
	setActive(arg_62_0.sceneScoreTf, False)

	if arg_62_1:
		arg_62_0.scoreNum = arg_62_0.scoreNum + arg_62_1

		local var_62_0 = arg_62_1 >= 0 and "+" .. arg_62_1 or tostring(arg_62_1)

		setText(findTF(arg_62_0.sceneScoreTf, "img"), var_62_0)
		setActive(arg_62_0.sceneScoreTf, True)

	arg_62_0.updateGameUI()

def var_0_0.onTimer(arg_63_0):
	arg_63_0.gameStep()

def var_0_0.gameStep(arg_64_0):
	if not arg_64_0.readyStart:
		arg_64_0.gameTime = arg_64_0.gameTime - Time.deltaTime
		arg_64_0.gameStepTime = arg_64_0.gameStepTime + Time.deltaTime

	if arg_64_0.gameTime < 0:
		arg_64_0.gameTime = 0

	arg_64_0.updateGameUI()

	if arg_64_0.sliderController:
		arg_64_0.sliderController.step()

	if arg_64_0.charController:
		arg_64_0.charController.step()

	if arg_64_0.gameTime <= 0:
		if arg_64_0.charController:
			arg_64_0.charController.onTimeOut()

		return

def var_0_0.timerStart(arg_65_0):
	if not arg_65_0.timer.running:
		arg_65_0.timer.Start()

def var_0_0.timerStop(arg_66_0):
	if arg_66_0.timer.running:
		arg_66_0.timer.Stop()

def var_0_0.updateGameUI(arg_67_0):
	setText(arg_67_0.scoreTf, arg_67_0.scoreNum)
	setText(arg_67_0.gameTimeS, math.ceil(arg_67_0.gameTime))

def var_0_0.setGameOver(arg_68_0, arg_68_1):
	arg_68_0.onGameOver(3.5)

	local var_68_0
	local var_68_1 = Application.targetFrameRate or 60

	seriesAsync({
		function(arg_69_0)
			local var_69_0 = 0

			var_68_0 = Timer.New(function()
				var_69_0 = var_69_0 + 15

				if var_69_0 > 1400:
					arg_69_0(), 1 / var_68_1, -1)

			var_68_0.Start(),
		function(arg_71_0)
			if var_68_0:
				var_68_0.Stop()

				var_68_0 = None

			if arg_68_1:
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_3)
			else
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_4)

			setActive(findTF(arg_68_0.resultUI, "ad/victory"), arg_68_1)
			setActive(findTF(arg_68_0.resultUI, "ad/defeat"), not arg_68_1)
			setActive(arg_68_0.resultUI, True)
			GetComponent(findTF(arg_68_0.resultUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

			local var_71_0 = 0

			var_68_0 = Timer.New(function()
				var_71_0 = var_71_0 + 15

				if var_71_0 > 1400:
					setActive(arg_68_0.resultUI, False)
					arg_71_0(), 1 / var_68_1, -1)

			var_68_0.Start()
	}, function()
		if var_68_0:
			var_68_0.Stop()

			var_68_0 = None)

def var_0_0.onGameOver(arg_74_0, arg_74_1):
	if arg_74_0.settlementFlag:
		return

	arg_74_0.timerStop()

	arg_74_0.settlementFlag = True

	setActive(arg_74_0.clickMask, True)
	LeanTween.delayedCall(go(arg_74_0._tf), arg_74_1, System.Action(function()
		arg_74_0.settlementFlag = False
		arg_74_0.gameStartFlag = False

		setActive(arg_74_0.clickMask, False)
		arg_74_0.showSettlement()))

def var_0_0.showSettlement(arg_76_0):
	setActive(arg_76_0.settlementUI, True)
	GetComponent(findTF(arg_76_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_76_0 = arg_76_0.GetMGData().GetRuntimeData("elements")
	local var_76_1 = arg_76_0.scoreNum
	local var_76_2 = var_76_0 and #var_76_0 > 0 and var_76_0[1] or 0

	setActive(findTF(arg_76_0.settlementUI, "ad/new"), var_76_2 < var_76_1)

	if var_76_2 <= var_76_1:
		var_76_2 = var_76_1

		arg_76_0.StoreDataToServer({
			var_76_2
		})

	local var_76_3 = findTF(arg_76_0.settlementUI, "ad/highText")
	local var_76_4 = findTF(arg_76_0.settlementUI, "ad/currentText")

	setText(var_76_3, var_76_2)
	setText(var_76_4, var_76_1)

	if arg_76_0.getGameTimes() and arg_76_0.getGameTimes() > 0:
		arg_76_0.sendSuccessFlag = True

		arg_76_0.SendSuccess(0)

		local var_76_5 = arg_76_0.getGameTotalTime()
		local var_76_6 = arg_76_0.getGameUsedTimes()

def var_0_0.resumeGame(arg_77_0):
	arg_77_0.gameStop = False

	setActive(arg_77_0.leaveUI, False)

	if arg_77_0.charController:
		arg_77_0.charController.resume()

	arg_77_0.timerStart()

def var_0_0.stopGame(arg_78_0):
	arg_78_0.gameStop = True

	if arg_78_0.charController:
		arg_78_0.charController.stop()

	arg_78_0.timerStop()

def var_0_0.onBackPressed(arg_79_0):
	if not arg_79_0.gameStartFlag:
		arg_79_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_79_0.settlementFlag:
			return

		if isActive(arg_79_0.pauseUI):
			setActive(arg_79_0.pauseUI, False)

		arg_79_0.stopGame()
		setActive(arg_79_0.leaveUI, True)

def var_0_0.willExit(arg_80_0):
	if arg_80_0.handle:
		UpdateBeat.RemoveListener(arg_80_0.handle)

	if arg_80_0._tf and LeanTween.isTweening(go(arg_80_0._tf)):
		LeanTween.cancel(go(arg_80_0._tf))

	if arg_80_0.timer and arg_80_0.timer.running:
		arg_80_0.timer.Stop()

	Time.timeScale = 1
	arg_80_0.timer = None

return var_0_0
