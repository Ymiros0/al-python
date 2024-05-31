﻿local var_0_0 = class("BattleRewardRerformResultLayer", import(".BattleResultLayer"))

function var_0_0.didEnter(arg_1_0)
	local var_1_0 = arg_1_0.contextData.stageId
	local var_1_1 = pg.expedition_data_template[var_1_0]

	setText(arg_1_0._levelText, var_1_1.name)

	local var_1_2 = rtf(arg_1_0._grade)

	arg_1_0._gradeUpperLeftPos = var_1_2.localPosition
	var_1_2.localPosition = Vector3(0, 25, 0)

	pg.UIMgr.GetInstance():BlurPanel(arg_1_0._tf)

	arg_1_0._grade.transform.localScale = Vector3(1.5, 1.5, 0)

	LeanTween.scale(arg_1_0._grade, Vector3(0.88, 0.88, 1), var_0_0.DURATION_WIN_SCALE):setOnComplete(System.Action(function()
		SetActive(arg_1_0._levelText, true)
		arg_1_0:rankAnimaFinish()
	end))

	arg_1_0._tf:GetComponent(typeof(Image)).color = Color.New(0, 0, 0, 0.5)
	arg_1_0._stateFlag = BattleResultLayer.STATE_RANK_ANIMA

	onButton(arg_1_0, arg_1_0._skipBtn, function()
		arg_1_0:skip()
	end, SFX_CONFIRM)
end

function var_0_0.skip(arg_4_0)
	if arg_4_0._stateFlag == BattleResultLayer.STATE_REPORTED then
		arg_4_0:emit(BattleResultMediator.ON_BACK_TO_LEVEL_SCENE)
	end
end

function var_0_0.onBackPressed(arg_5_0)
	triggerButton(arg_5_0._skipBtn)
end

function var_0_0.willExit(arg_6_0)
	LeanTween.cancel(go(arg_6_0._tf))
	pg.UIMgr.GetInstance():UnblurPanel(arg_6_0._tf)
end

return var_0_0
