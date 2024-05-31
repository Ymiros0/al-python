ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = class("BattleScoreBarView")

var_0_0.Battle.BattleScoreBarView = var_0_2
var_0_2.__name = "BattleScoreBarView"

function var_0_2.Ctor(arg_1_0, arg_1_1)
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform

	arg_1_0:init()
end

function var_0_2.init(arg_2_0)
	arg_2_0._scoreTF = arg_2_0._tf:Find("bg/Text")
	arg_2_0._comboTF = arg_2_0._tf:Find("comboMark")
	arg_2_0._comboText = arg_2_0._tf:Find("comboMark/value")
end

function var_0_2.SetActive(arg_3_0, arg_3_1)
	SetActive(arg_3_0._tf, arg_3_1)
end

function var_0_2.UpdateScore(arg_4_0, arg_4_1)
	setText(arg_4_0._scoreTF, arg_4_1)
end

function var_0_2.UpdateCombo(arg_5_0, arg_5_1)
	if arg_5_1 > 1 then
		SetActive(arg_5_0._comboTF, true)
	else
		SetActive(arg_5_0._comboTF, false)
	end

	setText(arg_5_0._comboText, arg_5_1)
end
