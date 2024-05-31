local var_0_0 = class("SwitcherRedDotNode", import(".RedDotNode"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	local var_1_0 = arg_1_1:Find(arg_1_3 and "on" or "off")

	var_0_0.super.Ctor(arg_1_0, var_1_0, arg_1_2)

	arg_1_0.toggle = arg_1_1:GetComponent(typeof(Toggle))
	arg_1_0.isOn = arg_1_3
end

function var_0_0.SetData(arg_2_0, arg_2_1)
	if IsNil(arg_2_0.gameObject) then
		return
	end

	setActive(arg_2_0.gameObject, arg_2_1 and arg_2_0.toggle.isOn ~= arg_2_0.isOn)
end

return var_0_0
