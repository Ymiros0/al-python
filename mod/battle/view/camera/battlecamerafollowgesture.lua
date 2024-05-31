ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleCameraFollowGesture = class("BattleCameraFollowGesture")
var_0_0.Battle.BattleCameraFollowGesture.__name = "BattleCameraFollowGesture"

local var_0_3 = var_0_0.Battle.BattleCameraFollowGesture

function var_0_3.Ctor(arg_1_0)
	arg_1_0._point = Vector3.zero
end

function var_0_3.SetGestureComponent(arg_2_0, arg_2_1)
	arg_2_0._slider = arg_2_1
end

function var_0_3.GetCameraPos(arg_3_0, arg_3_1)
	if arg_3_0._slider:IsPress() then
		arg_3_0._pressPoint = arg_3_0._pressPoint or arg_3_1

		local var_3_0, var_3_1 = arg_3_0._slider:IsFirstPress()
		local var_3_2 = arg_3_0._pressPoint.x
		local var_3_3 = arg_3_0._pressPoint.y

		if var_3_0 then
			arg_3_0._pressPoint.x = arg_3_1.x
		end

		if var_3_1 then
			arg_3_0._pressPoint.z = arg_3_1.z
		end

		local var_3_4, var_3_5 = arg_3_0._slider:GetDistance()

		arg_3_0._point:Set(arg_3_0._pressPoint.x, arg_3_0._pressPoint.y, arg_3_0._pressPoint.z)

		arg_3_0._point.z = arg_3_0._point.z + var_3_5 * -80
		arg_3_0._point.x = arg_3_0._point.x + var_3_4 * -80

		return arg_3_0._point
	else
		return arg_3_1
	end
end

function var_0_3.Dispose(arg_4_0)
	arg_4_0._slider = nil
end
