local var_0_0 = class("SailBoatGamingUI")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	var_0_1 = SailBoatGameVo
	arg_1_0._gameUI = findTF(arg_1_0._tf, "ui/gamingUI")
	arg_1_0.btnBack = findTF(arg_1_0._gameUI, "back")
	arg_1_0.btnPause = findTF(arg_1_0._gameUI, "pause")
	arg_1_0.gameTime = findTF(arg_1_0._gameUI, "time")
	arg_1_0.gameScore = findTF(arg_1_0._gameUI, "score")
	arg_1_0.btnSkill = findTF(arg_1_0._gameUI, "skill")
	arg_1_0.skillCount = findTF(arg_1_0._gameUI, "skill/amount")
	arg_1_0.progress = GetComponent(findTF(arg_1_0._gameUI, "progress"), typeof(Slider))
	arg_1_0.powerTf = findTF(arg_1_0._gameUI, "power")

	onButton(arg_1_0._event, arg_1_0.btnSkill, function()
		if arg_1_0.skillTime > 0:
			return

		if var_0_1.UseSkill():
			arg_1_0._event.emit(SailBoatGameView.USE_SKILL)

			arg_1_0.skillTime = var_0_1.skillTime

			setActive(arg_1_0.powerTf, False)
			setActive(arg_1_0.powerTf, True), SFX_CONFIRM)
	onButton(arg_1_0._event, arg_1_0.btnBack, function()
		arg_1_0._event.emit(SailBoatGameView.PAUSE_GAME, True)
		arg_1_0._event.emit(SailBoatGameView.OPEN_LEVEL_UI), SFX_CONFIRM)
	onButton(arg_1_0._event, arg_1_0.btnPause, function()
		arg_1_0._event.emit(SailBoatGameView.PAUSE_GAME, True)
		arg_1_0._event.emit(SailBoatGameView.OPEN_PAUSE_UI), SFX_CONFIRM)

	arg_1_0.direct = Vector2(0, 0)
	arg_1_0.joyStick = MiniGameJoyStick.New(findTF(arg_1_0._gameUI, "joyStick"))

	arg_1_0.joyStick.setActiveCallback(function(arg_5_0)
		return)

	arg_1_0._hpTf = findTF(arg_1_0._gameUI, "hp")
	arg_1_0._hpSlider = GetComponent(arg_1_0._hpTf, typeof(Slider))
	arg_1_0._powerEnemy = findTF(arg_1_0._gameUI, "powerEnemy")

def var_0_0.show(arg_6_0, arg_6_1):
	setActive(arg_6_0._gameUI, arg_6_1)

def var_0_0.update(arg_7_0):
	return

def var_0_0.start(arg_8_0):
	arg_8_0.direct = Vector2(0, 0)
	arg_8_0.subGameStepTime = 0
	arg_8_0.maxProgress = var_0_1.GetRoundData().progress
	arg_8_0.powers = Clone(var_0_1.GetRoundData().powers)

	setText(arg_8_0.skillCount, var_0_1.GetSkill())

	arg_8_0.skillTime = 0
	arg_8_0._char = None

	setActive(arg_8_0._powerEnemy, False)
	setActive(arg_8_0.powerTf, False)

def var_0_0.addScore(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.num
	local var_9_1 = arg_9_1.pos
	local var_9_2 = arg_9_1.id

def var_0_0.step(arg_10_0, arg_10_1):
	if not arg_10_0._char:
		arg_10_0._char = var_0_1.GetGameChar()
		arg_10_0._hpSlider.minValue = 0
		arg_10_0._hpSlider.maxValue = arg_10_0._char.getMaxHp()

	local var_10_0 = var_0_1.gameTime
	local var_10_1 = var_0_1.gameStepTime

	setText(arg_10_0.gameScore, var_0_1.scoreNum)
	setText(arg_10_0.gameTime, math.floor(var_10_0))

	arg_10_0.progress.value = var_10_1 / arg_10_0.maxProgress

	arg_10_0.joyStick.step()
	arg_10_0.joyStick.setDirectTarget(arg_10_0.direct)

	if arg_10_0.skillTime > 0:
		arg_10_0.skillTime = arg_10_0.skillTime - arg_10_1

	SailBoatGameVo.joyStickData = arg_10_0.joyStick.getValue()

	setText(arg_10_0.skillCount, var_0_1.GetSkill())

	local var_10_2 = arg_10_0._char.getHpPos()

	arg_10_0._hpTf.position = var_10_2
	arg_10_0.powerTf.position = var_10_2
	arg_10_0._hpSlider.value = arg_10_0._char.getHp()

	for iter_10_0 = #arg_10_0.powers, 1, -1:
		if var_0_1.gameStepTime > arg_10_0.powers[iter_10_0]:
			table.remove(arg_10_0.powers, iter_10_0)
			setActive(arg_10_0._powerEnemy, False)
			setActive(arg_10_0._powerEnemy, True)

def var_0_0.press(arg_11_0, arg_11_1, arg_11_2):
	if arg_11_1 == KeyCode.W:
		if arg_11_2:
			arg_11_0.direct.y = 1
		elif arg_11_0.direct.y == 1:
			arg_11_0.direct.y = 0
	elif arg_11_1 == KeyCode.S:
		if arg_11_2:
			arg_11_0.direct.y = -1
		elif arg_11_0.direct.y == -1:
			arg_11_0.direct.y = 0
	elif arg_11_1 == KeyCode.A:
		if arg_11_2:
			arg_11_0.direct.x = -1
		elif arg_11_0.direct.x == -1:
			arg_11_0.direct.x = 0
	elif arg_11_1 == KeyCode.D:
		if arg_11_2:
			arg_11_0.direct.x = 1
		elif arg_11_0.direct.x == 1:
			arg_11_0.direct.x = 0

return var_0_0
