﻿local var_0_0 = class("BattleSubmarineRunResultLayer", import("..base.BaseUI"))

var_0_0.DURATION_WIN_FADE_IN = 0.5
var_0_0.DURATION_LOSE_FADE_IN = 1.5
var_0_0.DURATION_GRADE_LAST = 1.5
var_0_0.DURATION_MOVE = 0.7
var_0_0.DURATION_WIN_SCALE = 0.7

function var_0_0.getUIName(arg_1_0)
	return "BattleResultUI"
end

function var_0_0.setPlayer(arg_2_0)
	return
end

function var_0_0.setShips(arg_3_0)
	return
end

function var_0_0.init(arg_4_0)
	arg_4_0._grade = arg_4_0:findTF("grade")
	arg_4_0._levelText = arg_4_0:findTF("chapterName/Text22", arg_4_0._grade)
	arg_4_0.clearFX = arg_4_0:findTF("clear")
	arg_4_0._main = arg_4_0:findTF("main")
	arg_4_0._blurConatiner = arg_4_0:findTF("blur_container")
	arg_4_0._bg = arg_4_0:findTF("main/jiesuanbeijing")
	arg_4_0._painting = arg_4_0:findTF("painting", arg_4_0._blurConatiner)
	arg_4_0._failPainting = arg_4_0:findTF("fail", arg_4_0._painting)
	arg_4_0._chat = arg_4_0:findTF("chat", arg_4_0._painting)
	arg_4_0._rightBottomPanel = arg_4_0:findTF("dodgem_confirm", arg_4_0._main)
	arg_4_0._exitBtn = arg_4_0:findTF("confirm_btn", arg_4_0._rightBottomPanel)
	arg_4_0._skipBtn = arg_4_0:findTF("skipLayer", arg_4_0._tf)
	arg_4_0.UIMain = pg.UIMgr.GetInstance().UIMain
	arg_4_0.overlay = pg.UIMgr.GetInstance().OverlayMain

	local var_4_0 = {
		"d",
		"c",
		"b",
		"a",
		"s"
	}
	local var_4_1 = arg_4_0:findTF("grade/Xyz/bg13")
	local var_4_2 = arg_4_0:findTF("grade/Xyz/bg14")
	local var_4_3
	local var_4_4
	local var_4_5
	local var_4_6 = arg_4_0.contextData.score
	local var_4_7 = var_4_6 > 0

	setActive(arg_4_0:findTF("jieuan01/BG/bg_victory", arg_4_0._bg), var_4_7)
	setActive(arg_4_0:findTF("jieuan01/BG/bg_fail", arg_4_0._bg), not var_4_7)

	if var_4_7 then
		local var_4_8 = var_4_0[var_4_6 + 1]

		var_4_3 = "battlescore/battle_score_" .. var_4_8 .. "/letter_" .. var_4_8
		var_4_4 = "battlescore/battle_score_" .. var_4_8 .. "/label_" .. var_4_8
	else
		local var_4_9 = var_4_0[1]

		var_4_3 = "battlescore/battle_score_" .. var_4_9 .. "/letter_" .. var_4_9
		var_4_4 = "battlescore/battle_score_" .. var_4_9 .. "/label_" .. var_4_9
	end

	LoadImageSpriteAsync(var_4_3, var_4_1, false)
	LoadImageSpriteAsync(var_4_4, var_4_2, false)
	SetActive(arg_4_0._levelText, false)
	SetActive(arg_4_0:findTF("main/conditions"), false)

	arg_4_0._ratioFitter = GetComponent(arg_4_0._tf, typeof(AspectRatioFitter))
	arg_4_0._ratioFitter.enabled = true
	arg_4_0._ratioFitter.aspectRatio = pg.CameraFixMgr.GetInstance().targetRatio
	arg_4_0.camEventId = pg.CameraFixMgr.GetInstance():bind(pg.CameraFixMgr.ASPECT_RATIO_UPDATE, function(arg_5_0, arg_5_1)
		arg_4_0._ratioFitter.aspectRatio = arg_5_1
	end)
end

function var_0_0.didEnter(arg_6_0)
	local var_6_0 = arg_6_0.contextData.stageId
	local var_6_1 = pg.expedition_data_template[var_6_0]

	setText(arg_6_0._levelText, var_6_1.name)

	local var_6_2 = rtf(arg_6_0._grade)

	arg_6_0._gradeUpperLeftPos = var_6_2.localPosition
	var_6_2.localPosition = Vector3(0, 25, 0)

	pg.UIMgr.GetInstance():BlurPanel(arg_6_0._tf)

	arg_6_0._grade.transform.localScale = Vector3(1.5, 1.5, 0)

	LeanTween.scale(arg_6_0._grade, Vector3(0.88, 0.88, 1), var_0_0.DURATION_WIN_SCALE):setOnComplete(System.Action(function()
		SetActive(arg_6_0._levelText, true)
		arg_6_0:rankAnimaFinish()
	end))

	arg_6_0._tf:GetComponent(typeof(Image)).color = Color.New(0, 0, 0, 0.5)
	arg_6_0._stateFlag = BattleResultLayer.STATE_RANK_ANIMA

	onButton(arg_6_0, arg_6_0._skipBtn, function()
		arg_6_0:skip()
	end, SFX_CONFIRM)
	arg_6_0:showPainting()
end

function var_0_0.rankAnimaFinish(arg_9_0)
	arg_9_0._stateFlag = BattleResultLayer.STATE_REPORTED
end

function var_0_0.showPainting(arg_10_0)
	local var_10_0
	local var_10_1

	SetActive(arg_10_0._painting, true)

	arg_10_0.paintingName = "u556"

	setPaintingPrefabAsync(arg_10_0._painting, arg_10_0.paintingName, "jiesuan", function()
		if findTF(arg_10_0._painting, "fitter").childCount > 0 then
			ShipExpressionHelper.SetExpression(findTF(arg_10_0._painting, "fitter"):GetChild(0), arg_10_0.paintingName, "win_mvp")
		end
	end)
	SetActive(arg_10_0._failPainting, false)

	if arg_10_0.contextData.score > 1 then
		local var_10_2

		var_10_0, var_10_2 = Ship.getWords(900180, "win_mvp")
	else
		local var_10_3

		var_10_0, var_10_3 = Ship.getWords(900180, "lose")
	end

	setText(arg_10_0._chat:Find("Text"), var_10_0)

	local var_10_4 = arg_10_0._chat:Find("Text"):GetComponent(typeof(Text))

	if #var_10_4.text > CHAT_POP_STR_LEN then
		var_10_4.alignment = TextAnchor.MiddleLeft
	else
		var_10_4.alignment = TextAnchor.MiddleCenter
	end

	SetActive(arg_10_0._chat, true)

	arg_10_0._chat.transform.localScale = Vector3.New(0, 0, 0)

	LeanTween.moveX(rtf(arg_10_0._painting), 50, 0.1):setOnComplete(System.Action(function()
		LeanTween.scale(rtf(arg_10_0._chat.gameObject), Vector3.New(1, 1, 1), 0.1):setEase(LeanTweenType.easeOutBack)
	end))
end

function var_0_0.skip(arg_13_0)
	if arg_13_0._stateFlag == BattleResultLayer.STATE_RANK_ANIMA then
		-- block empty
	elseif arg_13_0._stateFlag == BattleResultLayer.STATE_REPORTED then
		arg_13_0:emit(BattleResultMediator.ON_BACK_TO_LEVEL_SCENE)
	end
end

function var_0_0.onBackPressed(arg_14_0)
	triggerButton(arg_14_0._skipBtn)
end

function var_0_0.willExit(arg_15_0)
	LeanTween.cancel(go(arg_15_0._tf))
	pg.UIMgr.GetInstance():UnblurPanel(arg_15_0._tf)
	pg.CameraFixMgr.GetInstance():disconnect(arg_15_0.camEventId)
end

return var_0_0
