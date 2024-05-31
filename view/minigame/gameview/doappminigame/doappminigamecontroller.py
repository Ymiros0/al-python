local var_0_0 = class("DOAPPMiniGameController")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.binder = arg_1_1

	arg_1_0.InitTimer()
	arg_1_0.InitGameUI(arg_1_2)

local function var_0_1(arg_2_0, arg_2_1)
	local var_2_0 = arg_2_0.GetComponentsInChildren(typeof(Animator), True)

	for iter_2_0 = 0, var_2_0.Length - 1:
		var_2_0[iter_2_0].speed = arg_2_1

def var_0_0.InitTimer(arg_3_0):
	arg_3_0.timer = Timer.New(function()
		arg_3_0.OnTimer(DOAPPGameConfig.TIME_INTERVAL), DOAPPGameConfig.TIME_INTERVAL, -1)

	if IsUnityEditor and not arg_3_0.handle:
		arg_3_0.handle = UpdateBeat.CreateListener(arg_3_0.AddDebugInput, arg_3_0)

		UpdateBeat.AddListener(arg_3_0.handle)

def var_0_0.AddDebugInput(arg_5_0):
	local var_5_0 = {
		"E",
		"S",
		"W",
		"N"
	}
	local var_5_1 = {
		"D",
		"S",
		"A",
		"W"
	}

	for iter_5_0, iter_5_1 in ipairs(var_5_1):
		if Input.GetKeyDown(KeyCode[iter_5_1]):
			arg_5_0.cacheInput = var_5_0[iter_5_0]

		if Input.GetKeyUp(KeyCode[iter_5_1]) and arg_5_0.cacheInput == var_5_0[iter_5_0]:
			arg_5_0.cacheInput = None

local var_0_2 = {
	"Light",
	"Heavy",
	"Dodge"
}

def var_0_0.InitGameUI(arg_6_0, arg_6_1):
	arg_6_0.rtViewport = arg_6_1.Find("Viewport")
	arg_6_0.rtBg = arg_6_0.rtViewport.Find("MainContent/bg")
	arg_6_0.rtCharacter = arg_6_0.rtViewport.Find("MainContent/character")
	arg_6_0.rtPlayContent = arg_6_0.rtViewport.Find("MainContent/playContent")
	arg_6_0.rtBtns = arg_6_1.Find("Controller/middle/btn")

	eachChild(arg_6_0.rtBtns, function(arg_7_0)
		onButton(arg_6_0.binder, arg_7_0, function()
			arg_6_0.selectAction = table.indexof(var_0_2, arg_7_0.name)

			setActive(arg_6_0.rtBtns, False)
			arg_6_0.AfterSelect(), SFX_CONFIRM))
	setActive(arg_6_0.rtBtns, False)

	arg_6_0.rtFloatUI = arg_6_1.Find("Controller/middle/targetUI")

	setActive(arg_6_0.rtFloatUI, False)
	eachChild(arg_6_0.rtPlayContent.Find("middle/EffectObject"), function(arg_9_0)
		arg_9_0.Find("Image").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
			setActive(arg_9_0, False)))
	eachChild(arg_6_0.rtPlayContent.Find("middle/EffectOtherObject"), function(arg_11_0)
		arg_11_0.Find("Image").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
			setActive(arg_11_0, False)))

	arg_6_0.rtPointShow = arg_6_1.Find("Controller/middle/point")
	arg_6_0.textTime = arg_6_1.Find("Controller/top/panel/time")
	arg_6_0.rtPoint = arg_6_1.Find("Controller/top/self")
	arg_6_0.rtPointOther = arg_6_1.Find("Controller/top/others")

local var_0_3 = {
	"Misaki",
	"Marie",
	"Tamaki",
	"Luna"
}

def var_0_0.SetCharacter(arg_13_0, arg_13_1):
	local var_13_0 = table.indexof(var_0_3, arg_13_1)

	arg_13_0.rtTarget = cloneTplTo(arg_13_0.rtCharacter.Find(arg_13_1), arg_13_0.rtPlayContent.Find("front"), arg_13_1)

	local var_13_1 = arg_13_0.rtTarget.Find("Image").GetComponent(typeof(DftAniEvent))

	var_13_1.SetEndEvent(function()
		if math.abs(arg_13_0.deltaMove) > 2:
			arg_13_0.ReadyPoint()
		else
			arg_13_0.UpdateReady(arg_13_0.rtTarget))
	var_13_1.SetTriggerEvent(function()
		arg_13_0.countTarget = arg_13_0.countTarget + 1

		eachChild(arg_13_0.rtTarget.Find("effect"), function(arg_16_0)
			if arg_16_0.name == arg_13_0.statusTarget .. "_" .. arg_13_0.countTarget:
				setActive(arg_16_0, True)))
	eachChild(arg_13_0.rtTarget.Find("effect"), function(arg_17_0)
		arg_17_0.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
			setActive(arg_17_0, False)))
	eachChild(arg_13_0.rtPoint.Find("icon/mask"), function(arg_19_0)
		setActive(arg_19_0, arg_19_0.name == arg_13_1))

	local var_13_2 = var_0_3[(var_13_0 + math.random(3) + 3) % 4 + 1]

	arg_13_0.rtOtherTarget = cloneTplTo(arg_13_0.rtCharacter.Find(var_13_2), arg_13_0.rtPlayContent.Find("back"), var_13_2)

	eachChild(arg_13_0.rtOtherTarget, function(arg_20_0)
		setAnchoredPosition(arg_20_0, {
			x = 5
		}))
	setLocalScale(arg_13_0.rtOtherTarget, {
		x = -1
	})

	local var_13_3 = arg_13_0.rtOtherTarget.Find("Image").GetComponent(typeof(DftAniEvent))

	var_13_3.SetEndEvent(function()
		if math.abs(arg_13_0.deltaMove) > 2:
			arg_13_0.ReadyPoint()
		else
			arg_13_0.UpdateReady(arg_13_0.rtOtherTarget))
	var_13_3.SetTriggerEvent(function()
		arg_13_0.countOther = arg_13_0.countOther + 1

		eachChild(arg_13_0.rtOtherTarget.Find("effect"), function(arg_23_0)
			if arg_23_0.name == arg_13_0.statusOther .. "_" .. arg_13_0.countOther:
				setActive(arg_23_0, True)))
	eachChild(arg_13_0.rtOtherTarget.Find("effect"), function(arg_24_0)
		arg_24_0.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
			setActive(arg_24_0, False)))
	eachChild(arg_13_0.rtPointOther.Find("icon/mask"), function(arg_26_0)
		setActive(arg_26_0, arg_26_0.name == var_13_2))

	arg_13_0.rtEffectObject = arg_13_0.rtPlayContent.Find("middle/EffectObject")

local function var_0_4(arg_27_0, arg_27_1)
	local var_27_0 = arg_27_0.Find("point")

	for iter_27_0 = var_27_0.childCount, 1, -1:
		triggerToggle(var_27_0.GetChild(iter_27_0 - 1), iter_27_0 <= arg_27_1)

def var_0_0.UpdatePoint(arg_28_0):
	var_0_4(arg_28_0.rtPoint, arg_28_0.myPoint)
	var_0_4(arg_28_0.rtPointOther, arg_28_0.otherPoint)

def var_0_0.UpdateReady(arg_29_0, arg_29_1):
	onNextTick(function()
		if arg_29_1 == arg_29_0.rtTarget:
			setActive(arg_29_0.rtBtns, True)
		elif arg_29_1 == arg_29_0.rtOtherTarget:
			setAnchoredPosition(arg_29_0.rtFloatUI, {
				x = arg_29_0.deltaMove * 60
			})

			arg_29_0.otherSelectAction = math.random(3)

			eachChild(arg_29_0.rtFloatUI, function(arg_31_0)
				setActive(arg_31_0, arg_31_0.name == tostring(arg_29_0.otherSelectAction)))

			arg_29_0.selectCountdown = DOAPPGameConfig.SELECT_TIME

			setSlider(arg_29_0.rtFloatUI.Find(arg_29_0.otherSelectAction .. "/Slider"), 0, DOAPPGameConfig.SELECT_TIME, DOAPPGameConfig.SELECT_TIME - arg_29_0.selectCountdown)
			setActive(arg_29_0.rtFloatUI, True)
			arg_29_0.AfterSelect()
		else
			assert(False)

		setAnchoredPosition(arg_29_1, {
			x = arg_29_0.deltaMove * 10
		}))
	quickPlayAnimator(arg_29_1.Find("Image"), "Idle")

def var_0_0.PlayEffect(arg_32_0, arg_32_1):
	setAnchoredPosition(arg_32_0.rtEffectObject, {
		x = arg_32_0.deltaMove * 10
	})

	arg_32_0.effectCountdownDic[arg_32_1] = DOAPPGameConfig.EFFECT_COUNTDOWN[arg_32_1]

def var_0_0.AfterSelect(arg_33_0):
	if arg_33_0.selectAction and arg_33_0.otherSelectAction:
		setActive(arg_33_0.rtFloatUI, False)
		switch((arg_33_0.selectAction - arg_33_0.otherSelectAction + 3) % 3, {
			[0] = function()
				quickPlayAnimator(arg_33_0.rtTarget.Find("Image"), "Draw")
				quickPlayAnimator(arg_33_0.rtOtherTarget.Find("Image"), "Draw")

				arg_33_0.stopTarget = None

				arg_33_0.PlayEffect("Draw")

				arg_33_0.blockMoveBg = True,
			function()
				arg_33_0.deltaMove = arg_33_0.deltaMove + 1

				local var_35_0 = math.abs(arg_33_0.deltaMove) > 2 and {
					"Win_",
					"Lose_"
				} or {
					"Attack_",
					"Damage_"
				}

				setParent(arg_33_0.rtTarget, arg_33_0.rtPlayContent.Find("front"))
				quickPlayAnimator(arg_33_0.rtTarget.Find("Image"), var_35_0[1] .. var_0_2[arg_33_0.selectAction])

				arg_33_0.statusTarget = var_35_0[1] .. var_0_2[arg_33_0.selectAction]
				arg_33_0.countTarget = 0

				setParent(arg_33_0.rtOtherTarget, arg_33_0.rtPlayContent.Find("back"))
				quickPlayAnimator(arg_33_0.rtOtherTarget.Find("Image"), var_35_0[2] .. var_0_2[arg_33_0.otherSelectAction])

				arg_33_0.statusOther = var_35_0[2] .. var_0_2[arg_33_0.otherSelectAction]
				arg_33_0.countOther = 0
				arg_33_0.rtEffectObject = arg_33_0.rtPlayContent.Find("middle/EffectObject")
				arg_33_0.stopTarget = arg_33_0.rtOtherTarget

				arg_33_0.PlayEffect(var_0_2[arg_33_0.selectAction])

				arg_33_0.blockMoveBg = True

				if math.abs(arg_33_0.deltaMove) > 2:
					arg_33_0.loseDropCountdown = DOAPPGameConfig.LOSE_SOUND_COUNTDOWN[var_0_2[arg_33_0.otherSelectAction]] + defaultValue(DOAPPGameConfig.EFFECT_STOP_TIME[var_0_2[arg_33_0.selectAction]], 0),
			function()
				arg_33_0.deltaMove = arg_33_0.deltaMove - 1

				local var_36_0 = math.abs(arg_33_0.deltaMove) > 2 and {
					"Win_",
					"Lose_"
				} or {
					"Attack_",
					"Damage_"
				}

				setParent(arg_33_0.rtTarget, arg_33_0.rtPlayContent.Find("back"))
				quickPlayAnimator(arg_33_0.rtTarget.Find("Image"), var_36_0[2] .. var_0_2[arg_33_0.selectAction])

				arg_33_0.statusTarget = var_36_0[2] .. var_0_2[arg_33_0.selectAction]
				arg_33_0.countTarget = 0

				setParent(arg_33_0.rtOtherTarget, arg_33_0.rtPlayContent.Find("front"))
				quickPlayAnimator(arg_33_0.rtOtherTarget.Find("Image"), var_36_0[1] .. var_0_2[arg_33_0.otherSelectAction])

				arg_33_0.statusOther = var_36_0[1] .. var_0_2[arg_33_0.otherSelectAction]
				arg_33_0.countOther = 0
				arg_33_0.rtEffectObject = arg_33_0.rtPlayContent.Find("middle/EffectOtherObject")
				arg_33_0.stopTarget = arg_33_0.rtTarget

				arg_33_0.PlayEffect(var_0_2[arg_33_0.otherSelectAction])

				arg_33_0.blockMoveBg = True

				if math.abs(arg_33_0.deltaMove) > 2:
					arg_33_0.loseDropCountdown = DOAPPGameConfig.LOSE_SOUND_COUNTDOWN[var_0_2[arg_33_0.selectAction]] + defaultValue(DOAPPGameConfig.EFFECT_STOP_TIME[var_0_2[arg_33_0.otherSelectAction]], 0)
		})

		arg_33_0.selectAction = None
		arg_33_0.otherSelectAction = None
		arg_33_0.selectCountdown = None

def var_0_0.ReadyPoint(arg_37_0):
	if arg_37_0.readyPointCount > 0:
		arg_37_0.readyPointCount = 0

		if arg_37_0.deltaMove > 0:
			arg_37_0.myPoint = arg_37_0.myPoint + 1
		else
			arg_37_0.otherPoint = arg_37_0.otherPoint + 1

		arg_37_0.UpdatePoint()

		if arg_37_0.myPoint > 2 or arg_37_0.otherPoint > 2:
			arg_37_0.EndGame(arg_37_0.myPoint - arg_37_0.otherPoint)
		else
			arg_37_0.nextCountdown = DOAPPGameConfig.NEXT_ROUND_COUNTDOWN

			eachChild(arg_37_0.rtPointShow.Find("left"), function(arg_38_0)
				setActive(arg_38_0, arg_38_0.name == tostring(arg_37_0.myPoint)))
			eachChild(arg_37_0.rtPointShow.Find("right"), function(arg_39_0)
				setActive(arg_39_0, arg_39_0.name == tostring(arg_37_0.otherPoint)))
			setActive(arg_37_0.rtPointShow, True)
	else
		arg_37_0.readyPointCount = arg_37_0.readyPointCount + 1

def var_0_0.GetResultInfo(arg_40_0, arg_40_1):
	if arg_40_1:
		return arg_40_0.rtOtherTarget.name, arg_40_0.otherPoint, arg_40_0.result * -1
	else
		return arg_40_0.rtTarget.name, arg_40_0.myPoint, arg_40_0.result

def var_0_0.ResetGame(arg_41_0):
	arg_41_0.timeCount = DOAPPGameConfig.ALL_TIME

	setText(arg_41_0.textTime, string.format("%02ds", arg_41_0.timeCount))

	arg_41_0.deltaMove = 0

	if not IsNil(arg_41_0.rtTarget):
		Destroy(arg_41_0.rtTarget)

		arg_41_0.rtTarget = None

	if not IsNil(arg_41_0.rtOtherTarget):
		Destroy(arg_41_0.rtOtherTarget)

		arg_41_0.rtOtherTarget = None

	setAnchoredPosition(arg_41_0.rtViewport.Find("MainContent"), {
		x = 0
	})
	eachChild(arg_41_0.rtViewport.Find("MainContent/bg"), function(arg_42_0)
		setAnchoredPosition(arg_42_0, {
			x = 0
		}))

	arg_41_0.myPoint = 0
	arg_41_0.otherPoint = 0
	arg_41_0.readyPointCount = 0

	setActive(arg_41_0.rtPointShow, False)

	arg_41_0.effectCountdownDic = {}

def var_0_0.ReadyGame(arg_43_0, arg_43_1):
	arg_43_0.SetCharacter(arg_43_1.name)
	arg_43_0.UpdatePoint()
	arg_43_0.PauseGame()

def var_0_0.StartGame(arg_44_0):
	arg_44_0.isStart = True

	arg_44_0.UpdateReady(arg_44_0.rtTarget)
	arg_44_0.UpdateReady(arg_44_0.rtOtherTarget)
	arg_44_0.ResumeGame()

def var_0_0.EndGame(arg_45_0, arg_45_1):
	arg_45_0.isStart = False

	arg_45_0.PauseGame()

	arg_45_0.result = arg_45_1 or 0

	arg_45_0.binder.openUI("result")

def var_0_0.ResumeGame(arg_46_0):
	arg_46_0.isPause = False

	arg_46_0.timer.Start()
	var_0_1(arg_46_0.rtViewport, 1)

def var_0_0.PauseGame(arg_47_0):
	arg_47_0.isPause = True

	arg_47_0.timer.Stop()
	var_0_1(arg_47_0.rtViewport, 0)

def var_0_0.OnTimer(arg_48_0, arg_48_1):
	arg_48_0.timeCount = arg_48_0.timeCount - arg_48_1

	setText(arg_48_0.textTime, string.format("%02ds", arg_48_0.timeCount))

	if arg_48_0.timeCount <= 0:
		arg_48_0.EndGame(arg_48_0.myPoint - arg_48_0.otherPoint)

		return

	if arg_48_0.selectCountdown:
		arg_48_0.selectCountdown = arg_48_0.selectCountdown - arg_48_1

		setSlider(arg_48_0.rtFloatUI.Find(arg_48_0.otherSelectAction .. "/Slider"), 0, DOAPPGameConfig.SELECT_TIME, DOAPPGameConfig.SELECT_TIME - arg_48_0.selectCountdown)
		setText(arg_48_0.rtFloatUI.Find(arg_48_0.otherSelectAction .. "/Text"), string.format("%2d%%", (DOAPPGameConfig.SELECT_TIME - arg_48_0.selectCountdown) * 100 / DOAPPGameConfig.SELECT_TIME))

		if arg_48_0.selectCountdown <= 0:
			arg_48_0.selectAction = (arg_48_0.otherSelectAction + 1) % 3 + 1

			setActive(arg_48_0.rtBtns, False)
			arg_48_0.AfterSelect()

	if arg_48_0.nextCountdown:
		arg_48_0.nextCountdown = arg_48_0.nextCountdown - arg_48_1

		if arg_48_0.nextCountdown <= 0:
			arg_48_0.nextCountdown = None

			setActive(arg_48_0.rtPointShow, False)

			arg_48_0.deltaMove = 0

			arg_48_0.UpdateReady(arg_48_0.rtTarget)
			arg_48_0.UpdateReady(arg_48_0.rtOtherTarget)

	for iter_48_0, iter_48_1 in pairs(arg_48_0.effectCountdownDic):
		arg_48_0.effectCountdownDic[iter_48_0] = arg_48_0.effectCountdownDic[iter_48_0] - arg_48_1

		if arg_48_0.effectCountdownDic[iter_48_0] <= 0:
			arg_48_0.effectCountdownDic[iter_48_0] = None

			setActive(arg_48_0.rtEffectObject.Find(iter_48_0), True)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(DOAPPGameConfig.SOUND_EFFECT_PP)

			arg_48_0.blockMoveBg = False

			if arg_48_0.stopTarget:
				arg_48_0.stopCount = DOAPPGameConfig.EFFECT_STOP_TIME[iter_48_0]

				if arg_48_0.stopCount:
					onNextTick(function()
						var_0_1(arg_48_0.stopTarget, 0))

	if arg_48_0.stopCount:
		arg_48_0.stopCount = arg_48_0.stopCount - arg_48_1

		if arg_48_0.stopCount <= 0:
			arg_48_0.stopCount = None

			var_0_1(arg_48_0.stopTarget, 1)

	if arg_48_0.loseDropCountdown:
		arg_48_0.loseDropCountdown = arg_48_0.loseDropCountdown - arg_48_1

		if arg_48_0.loseDropCountdown <= 0:
			arg_48_0.loseDropCountdown = None

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(DOAPPGameConfig.SOUND_EFFECT_DROP)

	if not arg_48_0.blockMoveBg:
		local function var_48_0(arg_50_0, arg_50_1)
			local var_50_0 = arg_50_0.anchoredPosition.x / arg_50_1
			local var_50_1 = var_50_0 + (arg_48_0.deltaMove - var_50_0 > 0 and 1 or -1) * (arg_48_1 / DOAPPGameConfig.BG_MOVE_TIME)
			local var_50_2 = var_50_0 < arg_48_0.deltaMove and {
				var_50_0,
				arg_48_0.deltaMove
			} or {
				arg_48_0.deltaMove,
				var_50_0
			}
			local var_50_3 = math.clamp(var_50_1, unpack(var_50_2))

			setAnchoredPosition(arg_50_0, {
				x = var_50_3 * arg_50_1
			})

		local var_48_1 = arg_48_0.rtViewport.Find("MainContent")

		if var_48_1.anchoredPosition.x != arg_48_0.deltaMove * DOAPPGameConfig.BG_DISTANCE:
			var_48_0(var_48_1, -1 * DOAPPGameConfig.BG_DISTANCE)

			local var_48_2 = var_48_1.Find("bg")
			local var_48_3 = var_48_2.childCount

			for iter_48_2 = 1, var_48_3 - 1:
				var_48_0(var_48_2.GetChild(iter_48_2 - 1), (iter_48_2 - var_48_3) * DOAPPGameConfig.BG_DISTANCE)

def var_0_0.willExit(arg_51_0):
	if arg_51_0.handle:
		UpdateBeat.RemoveListener(arg_51_0.handle)

return var_0_0
