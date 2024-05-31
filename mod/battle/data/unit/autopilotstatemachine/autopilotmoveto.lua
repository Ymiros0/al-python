ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("AutoPilotMoveTo", var_0_0.Battle.IPilot)

var_0_0.Battle.AutoPilotMoveTo = var_0_1
var_0_1.__name = "AutoPilotMoveTo"

function var_0_1.Ctor(arg_1_0, ...)
	var_0_1.super.Ctor(arg_1_0, ...)
end

function var_0_1.SetParameter(arg_2_0, arg_2_1, arg_2_2)
	var_0_1.super.SetParameter(arg_2_0, arg_2_1, arg_2_2)

	arg_2_0._targetPos = Vector3(arg_2_1.x, 0, arg_2_1.z)
end

function var_0_1.GetDirection(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_0._targetPos - arg_3_1

	var_3_0.y = 0

	if var_3_0.magnitude < arg_3_0._valve then
		var_3_0 = Vector3.zero

		if arg_3_0._duration == -1 or arg_3_0:IsExpired() then
			arg_3_0:Finish()
		end
	end

	return var_3_0.normalized
end
