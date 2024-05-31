﻿local var_0_0 = class("GuessForkGameView", import("..BaseMiniGameView"))
local var_0_1 = {
	100,
	50
}
local var_0_2 = {
	10
}
local var_0_3 = {
	20
}
local var_0_4 = {
	3,
	3,
	3,
	4,
	4,
	4,
	5,
	5,
	5,
	6,
	6,
	6,
	7,
	7,
	7,
	8,
	8,
	8,
	8,
	9,
	9,
	9,
	9,
	9,
	10,
	10,
	10,
	10,
	10,
	10,
	11,
	11,
	11,
	11,
	11,
	12
}
local var_0_5 = {
	1000,
	200
}
local var_0_6 = 10000
local var_0_7 = 2
local var_0_8 = 2
local var_0_9 = "event:/ui/ddldaoshu2"
local var_0_10 = "event:/ui/taosheng"
local var_0_11 = "event:/ui/zhengque"
local var_0_12 = "event:/ui/shibai"
local var_0_13 = "backyard"
local var_0_14 = {
	"Cup_B",
	"Cup_G",
	"Cup_P",
	"Cup_R",
	"Cup_Y"
}
local var_0_15 = 3
local var_0_16 = 0.5
local var_0_17 = "Thinking_Loop"
local var_0_18 = {
	"Select_L",
	"Select_M",
	"Select_R"
}
local var_0_19 = {
	"Correct_L",
	"Correct_M",
	"Correct_R"
}
local var_0_20 = {
	"Incorrect_L",
	"Incorrect_M",
	"Incorrect_R"
}
local var_0_21 = "Manjuu_Correct"
local var_0_22 = {
	"Ayanami",
	"Cheshire",
	"Eldridge",
	"Formidable",
	"Javelin",
	"Laffey",
	"LeMalin",
	"Merkuria",
	"PingHai",
	"Roon",
	"Saratoga",
	"Shiratsuyu",
	"Yukikaze",
	"Z23"
}

function var_0_0.getUIName(arg_1_0)
	return "GuessForkGameUI"
end

function var_0_0.getBGM(arg_2_0)
	return var_0_13
end

function var_0_0.init(arg_3_0)
	arg_3_0.countUI = arg_3_0:findTF("count_ui")
	arg_3_0.countAnimator = arg_3_0:findTF("count_bg/count", arg_3_0.countUI):GetComponent(typeof(Animator))
	arg_3_0.countDft = arg_3_0:findTF("count_bg/count", arg_3_0.countUI):GetComponent(typeof(DftAniEvent))

	arg_3_0.countDft:SetEndEvent(function()
		setActive(arg_3_0.countUI, false)
		arg_3_0:startGame()
	end)

	arg_3_0.pauseUI = arg_3_0:findTF("pause_ui")
	arg_3_0.resuemBtn = arg_3_0:findTF("box/sure_btn", arg_3_0.pauseUI)

	setText(arg_3_0:findTF("box/content", arg_3_0.pauseUI), i18n("idolmaster_game_tip1"))

	arg_3_0.exitUI = arg_3_0:findTF("exit_ui")
	arg_3_0.exitSureBtn = arg_3_0:findTF("box/sure_btn", arg_3_0.exitUI)
	arg_3_0.exitCancelBtn = arg_3_0:findTF("box/cancel_btn", arg_3_0.exitUI)

	setText(arg_3_0:findTF("box/content", arg_3_0.exitUI), i18n("idolmaster_game_tip2"))

	arg_3_0.endUI = arg_3_0:findTF("end_ui")
	arg_3_0.endSureBtn = arg_3_0:findTF("box/sure_btn", arg_3_0.endUI)

	setText(arg_3_0:findTF("box/cur_score", arg_3_0.endUI), i18n("idolmaster_game_tip3"))

	arg_3_0.endScoreTxt = arg_3_0:findTF("box/cur_score/score", arg_3_0.endUI)
	arg_3_0.newTag = arg_3_0:findTF("new", arg_3_0.endScoreTxt)

	setText(arg_3_0:findTF("box/highest_score", arg_3_0.endUI), i18n("idolmaster_game_tip4"))

	arg_3_0.highestScoreTxt = arg_3_0:findTF("box/highest_score/score", arg_3_0.endUI)
	arg_3_0.gameUI = arg_3_0:findTF("game_ui")
	arg_3_0.returnBtn = arg_3_0:findTF("top/return_btn", arg_3_0.gameUI)
	arg_3_0.pauseBtn = arg_3_0:findTF("top/pause_btn", arg_3_0.gameUI)
	arg_3_0.roundTxt = arg_3_0:findTF("top/title/round/num", arg_3_0.gameUI)
	arg_3_0.roundNum = 0
	arg_3_0.curScoreTxt = arg_3_0:findTF("top/title/score_title/score", arg_3_0.gameUI)
	arg_3_0.curScore = 0

	setText(arg_3_0.curScoreTxt, arg_3_0.curScore)

	arg_3_0.curTimeTxt = arg_3_0:findTF("top/time_bg/time", arg_3_0.gameUI)
	arg_3_0.curTime = 0

	setText(arg_3_0:findTF("top/title/score_title", arg_3_0.gameUI), i18n("idolmaster_game_tip5"))

	arg_3_0.correctBar = arg_3_0:findTF("correct_bar", arg_3_0.gameUI)
	arg_3_0.failBar = arg_3_0:findTF("fail_bar", arg_3_0.gameUI)
	arg_3_0.manjuu = arg_3_0:findTF("play/manjuu", arg_3_0.gameUI)
	arg_3_0.manjuuAnimator = arg_3_0.manjuu:GetComponent(typeof(Animator))
	arg_3_0.manjuuDft = arg_3_0.manjuu:GetComponent(typeof(DftAniEvent))
	arg_3_0.result = arg_3_0:findTF("result", arg_3_0.gameUI)
	arg_3_0.resultAnimator = arg_3_0.result:GetComponent(typeof(Animator))
	arg_3_0.resultDft = arg_3_0.result:GetComponent(typeof(DftAniEvent))
	arg_3_0.scoreAni = arg_3_0:findTF("score", arg_3_0.gameUI)
	arg_3_0.cupContainer = arg_3_0:findTF("cup_container", arg_3_0.gameUI)
	arg_3_0.fork = arg_3_0:findTF("fork", arg_3_0.gameUI)
	arg_3_0.isGuessTime = false
end

function var_0_0.didEnter(arg_5_0)
	onButton(arg_5_0, arg_5_0.pauseBtn, function()
		setActive(arg_5_0.pauseUI, true)
		arg_5_0:pauseGame()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.resuemBtn, function()
		setActive(arg_5_0.pauseUI, false)
		arg_5_0:resumeGame()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.returnBtn, function()
		setActive(arg_5_0.exitUI, true)
		arg_5_0:pauseGame()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.exitSureBtn, function()
		setActive(arg_5_0.exitUI, false)
		arg_5_0:enterResultUI()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.exitCancelBtn, function()
		setActive(arg_5_0.exitUI, false)
		arg_5_0:resumeGame()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.endSureBtn, function()
		arg_5_0:emit(var_0_0.ON_BACK)
	end, SFX_PANEL)
	eachChild(arg_5_0.cupContainer, function(arg_12_0)
		onButton(arg_5_0, arg_12_0, function()
			if not arg_5_0.isGuessTime then
				return
			end

			setActive(arg_5_0:findTF("select", arg_12_0), true)

			arg_5_0.isGuessTime = false

			local var_13_0 = string.gsub(arg_12_0.name, "cup_", "")

			arg_5_0.selectIndex = tonumber(var_13_0)

			arg_5_0:endRound(arg_5_0.selectIndex == arg_5_0.forkIndex)
		end, SFX_PANEL)
	end)
	arg_5_0:initGameData()
	setActive(arg_5_0.countUI, true)
	arg_5_0.countAnimator:Play("countDown")
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_9)
end

function var_0_0.initGameData(arg_14_0)
	local var_14_0 = math.random(#var_0_14)
	local var_14_1 = var_0_14[var_14_0]

	eachChild(arg_14_0.cupContainer, function(arg_15_0)
		GetSpriteFromAtlasAsync("ui/minigameui/guessforkgameui", var_14_1, function(arg_16_0)
			setImageSprite(arg_14_0:findTF("front", arg_15_0), arg_16_0, true)
		end)
	end)

	arg_14_0.forkIndex = math.random(var_0_15)
	arg_14_0.selectIndex = nil
	arg_14_0.roundNum = arg_14_0.roundNum + 1

	setText(arg_14_0.roundTxt, arg_14_0.roundNum)

	arg_14_0.curTime = var_0_3[arg_14_0.roundNum] or var_0_3[#var_0_3]

	setText(arg_14_0.curTimeTxt, arg_14_0.curTime)
	setActive(arg_14_0.result, false)
end

function var_0_0.startGame(arg_17_0)
	arg_17_0.manjuuAnimator:Play(var_0_17)

	local var_17_0 = var_0_4[arg_17_0.roundNum] or var_0_4[#var_0_4]

	arg_17_0:playForkAni(function()
		arg_17_0:startSwap(var_17_0)
	end)

	arg_17_0.gameStartFlag = true
end

function var_0_0.playForkAni(arg_19_0, arg_19_1)
	local var_19_0 = arg_19_0:findTF("cup_" .. arg_19_0.forkIndex, arg_19_0.cupContainer)

	setParent(arg_19_0.fork, arg_19_0:findTF("fork_node", var_19_0), false)
	setLocalScale(arg_19_0.fork, Vector3.one)
	setLocalPosition(arg_19_0.fork, Vector3(0, 50, 0))
	setActive(arg_19_0.fork, true)
	arg_19_0:managedTween(LeanTween.delayedCall, function()
		arg_19_0:managedTween(LeanTween.moveY, function()
			setActive(arg_19_0.fork, false)

			if arg_19_1 then
				arg_19_1()
			end
		end, arg_19_0.fork, -20, var_0_16):setEase(LeanTweenType.linear)
	end, 0.5, nil)
end

function var_0_0.startSwap(arg_22_0, arg_22_1)
	if arg_22_1 < 1 then
		arg_22_0.isGuessTime = true

		arg_22_0:startTimer()

		return
	end

	local var_22_0 = {
		1,
		2,
		3
	}
	local var_22_1 = math.random(#var_22_0)

	table.remove(var_22_0, var_22_1)

	local var_22_2 = arg_22_0:findTF("cup_" .. var_22_0[1], arg_22_0.cupContainer)
	local var_22_3 = arg_22_0:findTF("cup_" .. var_22_0[2], arg_22_0.cupContainer)

	arg_22_0:swapCup(var_22_2, var_22_3, function()
		arg_22_0:startSwap(arg_22_1 - 1)
	end)
end

function var_0_0.swapCup(arg_24_0, arg_24_1, arg_24_2, arg_24_3)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_10)

	local var_24_0 = var_0_5[1] + (arg_24_0.roundNum - 1) * var_0_5[2]
	local var_24_1 = var_24_0 < var_0_6 and var_24_0 or var_0_6
	local var_24_2 = arg_24_2.anchoredPosition
	local var_24_3 = arg_24_1.anchoredPosition
	local var_24_4 = math.abs(var_24_2.x - var_24_3.x) / var_24_1

	arg_24_0:managedTween(LeanTween.moveX, nil, arg_24_1, var_24_2.x, var_24_4):setEase(LeanTweenType.linear)
	arg_24_0:managedTween(LeanTween.moveX, function()
		if arg_24_3 then
			arg_24_3()
		end
	end, arg_24_2, var_24_3.x, var_24_4):setEase(LeanTweenType.linear)
end

function var_0_0.startTimer(arg_26_0)
	local var_26_0 = arg_26_0.curTime

	arg_26_0.timer = Timer.New(function()
		arg_26_0.curTime = arg_26_0.curTime - 1

		if arg_26_0.curTime <= 0 then
			arg_26_0:endRound(false)
		end

		setText(arg_26_0.curTimeTxt, arg_26_0.curTime)
	end, 1, -1)

	arg_26_0.timer:Start()
end

function var_0_0.stopTimer(arg_28_0)
	if arg_28_0.timer then
		arg_28_0.timer:Stop()

		arg_28_0.timer = nil
	end
end

function var_0_0.pauseGame(arg_29_0)
	arg_29_0:pauseManagedTween()

	if arg_29_0.timer then
		arg_29_0.timer:Pause()
	end

	arg_29_0.manjuuAnimator.speed = 0
	arg_29_0.resultAnimator.speed = 0
end

function var_0_0.resumeGame(arg_30_0)
	arg_30_0:resumeManagedTween()

	if arg_30_0.timer then
		arg_30_0.timer:Resume()
	end

	arg_30_0.manjuuAnimator.speed = 1
	arg_30_0.resultAnimator.speed = 1
end

function var_0_0.endRound(arg_31_0, arg_31_1)
	arg_31_0:stopTimer()

	if arg_31_0.selectIndex then
		arg_31_0:playManjuuAni(arg_31_1)
	else
		arg_31_0:playTimeOutAni()
		arg_31_0:endGame()
	end
end

function var_0_0.playManjuuAni(arg_32_0, arg_32_1)
	local var_32_0 = arg_32_0:findTF("cup_" .. arg_32_0.selectIndex, arg_32_0.cupContainer)
	local var_32_1 = (var_32_0.anchoredPosition.x + 480) / 480 + 1

	arg_32_0.manjuuAnimator:Play(var_0_18[var_32_1])
	arg_32_0.manjuuDft:SetEndEvent(function()
		arg_32_0.manjuuDft:SetEndEvent(nil)

		local var_33_0 = arg_32_1 and var_0_19[var_32_1] or var_0_20[var_32_1]

		setActive(arg_32_0:findTF("select", var_32_0), false)
		arg_32_0.manjuuAnimator:Play(var_33_0)
		arg_32_0:playResultAni(arg_32_1)
	end)
end

function var_0_0.playResultAni(arg_34_0, arg_34_1)
	local var_34_0 = arg_34_0:findTF("cup_" .. arg_34_0.selectIndex, arg_34_0.cupContainer)

	setParent(arg_34_0.result, arg_34_0:findTF("result_node", var_34_0), false)
	setLocalScale(arg_34_0.result, Vector3.one)
	setLocalPosition(arg_34_0.result, Vector3.zero)
	setActive(arg_34_0.result, true)

	if arg_34_1 then
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_11)
		arg_34_0.resultAnimator:Play(var_0_21)
		arg_34_0.resultDft:SetEndEvent(function()
			arg_34_0.resultDft:SetEndEvent(nil)
			arg_34_0:showCorrectBar()
		end)
	else
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_12)

		local var_34_1 = var_0_22[math.random(#var_0_22)]

		arg_34_0.resultAnimator:Play(var_34_1)
		arg_34_0.resultDft:SetEndEvent(function()
			arg_34_0.resultDft:SetEndEvent(nil)
			arg_34_0:endGame()
		end)
	end
end

function var_0_0.showCorrectBar(arg_37_0)
	setActive(arg_37_0.correctBar, true)

	local var_37_0 = var_0_1[1] + (arg_37_0.roundNum - 1) * var_0_1[2]

	arg_37_0.curScore = arg_37_0.curScore + var_37_0

	setText(arg_37_0.curScoreTxt, arg_37_0.curScore)
	setLocalPosition(arg_37_0.scoreAni, Vector3(0, 250, 0))
	setText(arg_37_0.scoreAni, "+" .. var_37_0)
	setActive(arg_37_0.scoreAni, true)
	LeanTween.moveY(arg_37_0.scoreAni, 300, 1):setOnComplete(System.Action(function()
		setActive(arg_37_0.scoreAni, false)
	end))

	local var_37_1 = 0.5
	local var_37_2 = var_0_2[arg_37_0.roundNum] or var_0_2[#var_0_2]
	local var_37_3 = arg_37_0.curScore + var_37_2 * arg_37_0.curTime

	LeanTween.value(go(arg_37_0.curScoreTxt), arg_37_0.curScore, var_37_3, var_37_1):setOnUpdate(System.Action_float(function(arg_39_0)
		setText(arg_37_0.curScoreTxt, math.ceil(arg_39_0))
	end)):setOnComplete(System.Action(function()
		arg_37_0.curScore = var_37_3

		setText(arg_37_0.curScoreTxt, arg_37_0.curScore)
	end))
	LeanTween.value(go(arg_37_0.curTimeTxt), arg_37_0.curTime, 0, var_37_1):setOnUpdate(System.Action_float(function(arg_41_0)
		setText(arg_37_0.curTimeTxt, math.ceil(arg_41_0))
	end)):setOnComplete(System.Action(function()
		arg_37_0.curScore = var_37_3

		setText(arg_37_0.curTimeTxt, 0)
	end))
	onButton(arg_37_0, arg_37_0.correctBar, function()
		setActive(arg_37_0.correctBar, false)
		setActive(arg_37_0.scoreAni, false)
		arg_37_0:initGameData()
		arg_37_0:startGame()
	end, SFX_PANEL)
	arg_37_0:managedTween(LeanTween.delayedCall, function()
		if isActive(arg_37_0.correctBar) then
			triggerButton(arg_37_0.correctBar)
		end
	end, var_0_7, nil)
end

function var_0_0.playTimeOutAni(arg_45_0)
	local var_45_0 = arg_45_0:findTF("cup_" .. arg_45_0.forkIndex, arg_45_0.cupContainer)

	setParent(arg_45_0.result, arg_45_0:findTF("result_node", var_45_0), false)
	setLocalScale(arg_45_0.result, Vector3.one)
	setLocalPosition(arg_45_0.result, Vector3.zero)
	setActive(arg_45_0.result, true)
	arg_45_0.resultAnimator:Play(var_0_21)
	arg_45_0.resultDft:SetEndEvent(function()
		arg_45_0.resultDft:SetEndEvent(nil)
	end)
end

function var_0_0.endGame(arg_47_0)
	setActive(arg_47_0.failBar, true)
	onButton(arg_47_0, arg_47_0.failBar, function()
		setActive(arg_47_0.failBar, false)
		arg_47_0:enterResultUI()
	end, SFX_PANEL)
	arg_47_0:managedTween(LeanTween.delayedCall, function()
		if isActive(arg_47_0.failBar) then
			triggerButton(arg_47_0.failBar)
		end
	end, var_0_7, nil)
end

function var_0_0.enterResultUI(arg_50_0)
	arg_50_0.gameStartFlag = false

	setActive(arg_50_0.endUI, true)
	setText(arg_50_0.endScoreTxt, arg_50_0.curScore)

	local var_50_0 = arg_50_0:GetMGData():GetRuntimeData("elements")
	local var_50_1 = var_50_0 and #var_50_0 > 0 and var_50_0[1] or 0

	setActive(arg_50_0.newTag, var_50_1 < arg_50_0.curScore)

	if var_50_1 <= arg_50_0.curScore then
		var_50_1 = arg_50_0.curScore

		arg_50_0:StoreDataToServer({
			var_50_1
		})
	end

	setText(arg_50_0.highestScoreTxt, var_50_1)

	if arg_50_0:GetMGHubData().count > 0 then
		arg_50_0:SendSuccess(0)
	end
end

function var_0_0.OnGetAwardDone(arg_51_0, arg_51_1)
	if arg_51_1.cmd == MiniGameOPCommand.CMD_COMPLETE then
		local var_51_0 = arg_51_0:GetMGHubData()

		if var_51_0.ultimate == 0 and var_51_0.usedtime >= var_51_0:getConfig("reward_need") then
			pg.m02:sendNotification(GAME.SEND_MINI_GAME_OP, {
				hubid = var_51_0.id,
				cmd = MiniGameOPCommand.CMD_ULTIMATE,
				args1 = {}
			})
		end
	end
end

function var_0_0.onBackPressed(arg_52_0)
	if not arg_52_0.gameStartFlag then
		arg_52_0:emit(var_0_0.ON_BACK_PRESSED)
	else
		setActive(arg_52_0.exitUI, true)
		arg_52_0:pauseGame()
	end
end

return var_0_0
