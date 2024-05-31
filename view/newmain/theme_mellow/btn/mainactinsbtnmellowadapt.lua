﻿local var_0_0 = class("MainActInsBtnMellowAdapt", import(".MainDifferentStyleSpActBtnAdapt"))

function var_0_0.GetContainer(arg_1_0)
	return arg_1_0.root:Find("left")
end

function var_0_0.OnInit(arg_2_0)
	local var_2_0 = getProxy(InstagramProxy):ShouldShowTip()

	setActive(arg_2_0._tf:Find("tip"), var_2_0)

	arg_2_0.textTr = arg_2_0._tf:Find("Text"):GetComponent(typeof(Text))
	arg_2_0.systemTimeUtil = arg_2_0.systemTimeUtil or SystemTimeUtil.New()

	arg_2_0:AddTimer()

	local var_2_1 = arg_2_0._tf:GetComponent(typeof(Animation))

	if var_2_0 then
		var_2_1:Play("shake")
	else
		var_2_1:Stop()

		arg_2_0._tf.localEulerAngles = Vector3.zero
	end
end

function var_0_0.AddTimer(arg_3_0)
	arg_3_0.systemTimeUtil:SetUp(function(arg_4_0, arg_4_1, arg_4_2)
		arg_3_0.textTr.text = arg_4_0 .. ":" .. arg_4_1
	end)
end

function var_0_0.RemoveTimer(arg_5_0)
	if arg_5_0.systemTimeUtil then
		arg_5_0.systemTimeUtil:Dispose()

		arg_5_0.systemTimeUtil = nil
	end
end

function var_0_0.OnClear(arg_6_0)
	arg_6_0:RemoveTimer()
end

function var_0_0.OnDisable(arg_7_0)
	arg_7_0:RemoveTimer()
end

return var_0_0
