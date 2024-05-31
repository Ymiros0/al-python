﻿local var_0_0 = class("BossSingleContinuousOperationPanel", import("view.base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "BossSingleContinuousOperationUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.btnOn = arg_2_0._tf:Find("Panel/On")
	arg_2_0.btnOff = arg_2_0._tf:Find("Panel/Off")
	arg_2_0.slider = arg_2_0._tf:Find("Panel/Slider")
	arg_2_0._ratioFitter = GetComponent(arg_2_0._tf, typeof(AspectRatioFitter))

	setText(arg_2_0.btnOff:Find("common/Text"), i18n("multiple_sorties_stopped"))
end

function var_0_0.UpdateAutoFightMark(arg_3_0)
	local var_3_0 = arg_3_0.contextData.autoFlag

	setActive(arg_3_0.btnOn, var_3_0)
	setActive(arg_3_0.btnOff, not var_3_0)
end

function var_0_0.didEnter(arg_4_0)
	arg_4_0.contextData.autoFlag = defaultValue(arg_4_0.contextData.autoFlag, true)

	onButton(arg_4_0, arg_4_0.btnOn, function()
		arg_4_0.contextData.autoFlag = false

		arg_4_0:UpdateAutoFightMark()
		pg.TipsMgr.GetInstance():ShowTips(i18n("multiple_sorties_stop_tip"))
		arg_4_0:emit(BattleMediator.HIDE_ALL_BUTTONS, true)
	end, SFX_PANEL)
	onButton(arg_4_0, arg_4_0.btnOff, function()
		arg_4_0.contextData.autoFlag = true

		arg_4_0:UpdateAutoFightMark()
		pg.TipsMgr.GetInstance():ShowTips(i18n("multiple_sorties_resume_tip"))
		arg_4_0:emit(BattleMediator.HIDE_ALL_BUTTONS, false)
	end, SFX_PANEL)

	arg_4_0._ratioFitter.aspectRatio = pg.CameraFixMgr.GetInstance():GetBattleUIRatio()

	arg_4_0:UpdateAutoFightMark()
	arg_4_0:UpdateBattleTimes()
	pg.LayerWeightMgr.GetInstance():Add2Overlay(LayerWeightConst.UI_TYPE_OVERLAY_FOREVER, arg_4_0._tf, {
		weight = LayerWeightConst.THIRD_LAYER,
		groupName = LayerWeightConst.GROUP_COMBAT
	})
end

function var_0_0.UpdateBattleTimes(arg_7_0)
	local var_7_0 = arg_7_0.contextData.continuousBattleTimes
	local var_7_1 = arg_7_0.contextData.totalBattleTimes

	setText(arg_7_0.btnOn:Find("Text"), var_7_1 - var_7_0 + 1 .. "/" .. var_7_1)
	setActive(arg_7_0.slider, false)
	setActive(arg_7_0.btnOff:Find("small"), true)
	setActive(arg_7_0.btnOff:Find("common"), false)
end

function var_0_0.OnEnterBattleResult(arg_8_0)
	setActive(arg_8_0.btnOff:Find("small"), false)
	setActive(arg_8_0.btnOff:Find("common"), true)
end

function var_0_0.AnimatingSlider(arg_9_0)
	setActive(arg_9_0.slider, true)
	arg_9_0:managedTween(LeanTween.value, function()
		arg_9_0:emit(BossSingleContinuousOperationMediator.ON_REENTER)
	end, go(arg_9_0.slider), 1, 0, 5):setOnUpdate(System.Action_float(function(arg_11_0)
		setSlider(arg_9_0.slider, 0, 1, arg_11_0)
	end))
end

function var_0_0.willExit(arg_12_0)
	pg.UIMgr.GetInstance():UnOverlayPanel(arg_12_0._tf)
end

function var_0_0.onBackPressed(arg_13_0)
	arg_13_0:emit(GAME.PAUSE_BATTLE)
end

return var_0_0
