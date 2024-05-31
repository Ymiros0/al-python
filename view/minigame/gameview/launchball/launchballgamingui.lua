local var_0_0 = class("LaunchBallGamingUI")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0._gameUI = findTF(arg_1_0._tf, "ui/gamingUI")
	arg_1_0.btnBack = findTF(arg_1_0._gameUI, "back")
	arg_1_0.btnPause = findTF(arg_1_0._gameUI, "pause")
	arg_1_0.gameTime = findTF(arg_1_0._gameUI, "time")
	arg_1_0.gameScore = findTF(arg_1_0._gameUI, "score")

	onButton(arg_1_0._event, arg_1_0.btnBack, function()
		arg_1_0._event:emit(LaunchBallGameView.PAUSE_GAME, true)
		arg_1_0._event:emit(LaunchBallGameView.OPEN_LEVEL_UI)
	end, SFX_CONFIRM)
	onButton(arg_1_0._event, arg_1_0.btnPause, function()
		arg_1_0._event:emit(LaunchBallGameView.PAUSE_GAME, true)
		arg_1_0._event:emit(LaunchBallGameView.OPEN_PAUSE_UI)
	end, SFX_CONFIRM)

	arg_1_0.direct = Vector2(0, 0)
	arg_1_0.skill = findTF(arg_1_0._gameUI, "Skill")
	arg_1_0.skillAnim = GetComponent(findTF(arg_1_0.skill, "ad/anim"), typeof(Animator))

	onButton(arg_1_0._event, arg_1_0.skill, function()
		arg_1_0._event:emit(LaunchBallGameView.PRESS_SKILL)
	end)

	arg_1_0.skillCd = findTF(arg_1_0.skill, "ad/black")
end

function var_0_0.show(arg_5_0, arg_5_1)
	setActive(arg_5_0._gameUI, arg_5_1)
end

function var_0_0.update(arg_6_0)
	return
end

function var_0_0.start(arg_7_0)
	arg_7_0.direct = Vector2(0, 0)
	arg_7_0.subGameStepTime = 0
end

function var_0_0.addScore(arg_8_0, arg_8_1)
	local var_8_0 = arg_8_1.num
	local var_8_1 = arg_8_1.pos
	local var_8_2 = arg_8_1.id
end

function var_0_0.step(arg_9_0)
	if LaunchBallGameVo.enemyStopTime and LaunchBallGameVo.enemyStopTime > 0 then
		arg_9_0.subGameStepTime = arg_9_0.subGameStepTime + LaunchBallGameVo.deltaTime
	end

	setText(arg_9_0.gameTime, math.floor(LaunchBallGameVo.gameStepTime - arg_9_0.subGameStepTime))
	setText(arg_9_0.gameScore, LaunchBallGameVo.scoreNum)

	local var_9_0 = LaunchBallGameVo.pressSkill

	if var_9_0 and var_9_0.time > 0 then
		setFillAmount(arg_9_0.skillCd, var_9_0.time / var_9_0.data.cd_time)

		if not isActive(arg_9_0.skillCd) then
			arg_9_0.skillAnim:Play("empty")
			setActive(arg_9_0.skillCd, true)
		end
	elseif isActive(arg_9_0.skillCd) then
		setActive(arg_9_0.skillCd, false)
		arg_9_0.skillAnim:Play("Skill")
	end
end

function var_0_0.press(arg_10_0, arg_10_1, arg_10_2)
	if arg_10_1 == KeyCode.W then
		if arg_10_2 then
			arg_10_0.direct.y = 1
		elseif arg_10_0.direct.y == 1 then
			arg_10_0.direct.y = 0
		end
	end

	if arg_10_1 == KeyCode.S then
		if arg_10_2 then
			arg_10_0.direct.y = -1
		elseif arg_10_0.direct.y == -1 then
			arg_10_0.direct.y = 0
		end
	end

	if arg_10_1 == KeyCode.A then
		if arg_10_2 then
			arg_10_0.direct.x = -1
		elseif arg_10_0.direct.x == -1 then
			arg_10_0.direct.x = 0
		end
	end

	if arg_10_1 == KeyCode.D then
		if arg_10_2 then
			arg_10_0.direct.x = 1
		elseif arg_10_0.direct.x == 1 then
			arg_10_0.direct.x = 0
		end
	end
end

return var_0_0
