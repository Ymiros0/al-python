﻿ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleTimerView = class("BattleTimerView")
var_0_0.Battle.BattleTimerView.__name = "BattleTimerView"

function var_0_0.Battle.BattleTimerView.Ctor(arg_1_0, arg_1_1)
	arg_1_0._go = arg_1_1
	arg_1_0._timer = arg_1_0._go.transform:Find("Text")
	arg_1_0._blinker = arg_1_0._timer:GetComponent(typeof(Animator))
	arg_1_0._isBlink = false
	arg_1_0._text = arg_1_0._timer:GetComponent(typeof(Text))
	arg_1_0.timeStr = ""
end

function var_0_0.Battle.BattleTimerView.SetActive(arg_2_0, arg_2_1)
	setActive(arg_2_0._go, arg_2_1)
end

function var_0_0.Battle.BattleTimerView.SetCountDownText(arg_3_0, arg_3_1)
	if arg_3_1 <= 30 and not arg_3_0._isBlink then
		arg_3_0._blinker.enabled = true
		arg_3_0._isBlink = true
	end

	local var_3_0 = arg_3_0.formatTime(math.floor(arg_3_1))

	if var_3_0 == arg_3_0.timeStr then
		return
	end

	arg_3_0.timeStr = var_3_0
	arg_3_0._text.text = var_3_0
end

function var_0_0.Battle.BattleTimerView.formatTime(arg_4_0)
	return string.format("%02u:%02u", math.floor(arg_4_0 / 60), arg_4_0 % 60)
end

function var_0_0.Battle.BattleTimerView.Dispose(arg_5_0)
	return
end
