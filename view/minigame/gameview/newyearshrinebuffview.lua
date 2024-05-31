local var_0_0 = class("NewYearShrineBuffView", import(".ShrineBuffView"))

function var_0_0.getUIName(arg_1_0)
	return "NewYearShrineBuff"
end

function var_0_0.initUI(arg_2_0)
	var_0_0.super.initUI(arg_2_0)

	arg_2_0.dft = GetComponent(arg_2_0._tf, "DftAniEvent")

	arg_2_0.dft:SetStartEvent(function()
		setButtonEnabled(arg_2_0.backBtn, false)
	end)
	arg_2_0.dft:SetEndEvent(function()
		setButtonEnabled(arg_2_0.backBtn, true)
	end)
end

return var_0_0
