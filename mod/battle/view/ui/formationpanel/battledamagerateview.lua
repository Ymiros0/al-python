ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleDamageRateView = class("BattleDamageRateView")
var_0_0.Battle.BattleDamageRateView.__name = "BattleDamageRateView"

function var_0_0.Battle.BattleDamageRateView.Ctor(arg_1_0, arg_1_1)
	arg_1_0._go = arg_1_1
	arg_1_0.tick_bar = arg_1_1.transform:Find("tick_bar"):GetComponent(typeof(Image))
	arg_1_0.tickBarOb = arg_1_0.tick_bar.gameObject
	arg_1_0.tick_bar.fillAmount = 0
end

function var_0_0.Battle.BattleDamageRateView.UpdateScore(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_0:CalScore(arg_2_1, arg_2_2)

	LeanTween.cancel(arg_2_0.tickBarOb)
	LeanTween.value(arg_2_0.tickBarOb, arg_2_0.tick_bar.fillAmount, var_2_0, 0.5):setOnUpdate(System.Action_float(function(arg_3_0)
		arg_2_0.tick_bar.fillAmount = arg_3_0
	end))
end

function var_0_0.Battle.BattleDamageRateView.CalScore(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = pg.expedition_data_template[arg_4_2]
	local var_4_1 = {
		"c_score_point",
		"b_score_point",
		"a_score_point",
		"s_score_point",
		"score_max"
	}
	local var_4_2 = {
		0,
		0.445,
		0.7,
		0.88,
		1
	}
	local var_4_3 = 0

	for iter_4_0, iter_4_1 in ipairs(var_4_1) do
		if arg_4_1 < var_4_0[iter_4_1] then
			break
		end

		var_4_3 = iter_4_0
	end

	local var_4_4 = 0

	if var_4_3 < #var_4_1 then
		local var_4_5 = var_4_0[var_4_1[var_4_3]]

		if var_4_5 < 0 then
			var_4_5 = 0
		end

		local var_4_6 = (arg_4_1 - var_4_5) / (var_4_0[var_4_1[var_4_3 + 1]] - var_4_5)

		var_4_4 = (var_4_2[var_4_3 + 1] - var_4_2[var_4_3]) * var_4_6 + var_4_2[var_4_3]
	else
		var_4_4 = 1
	end

	return var_4_4
end

function var_0_0.Battle.BattleDamageRateView.Dispose(arg_5_0)
	LeanTween.cancel(arg_5_0.tickBarOb)
end
