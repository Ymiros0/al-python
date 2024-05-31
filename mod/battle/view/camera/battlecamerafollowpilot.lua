ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleCameraFollowPilot = class("BattleCameraFollowPilot")
var_0_0.Battle.BattleCameraFollowPilot.__name = "BattleCameraFollowPilot"

local var_0_3 = var_0_0.Battle.BattleCameraFollowPilot

function var_0_3.Ctor(arg_1_0)
	arg_1_0.point = Vector3.zero
end

function var_0_3.SetFleetVO(arg_2_0, arg_2_1)
	arg_2_0._fleetMotion = arg_2_1:GetMotion()
end

function var_0_3.SetGoldenRation(arg_3_0, arg_3_1)
	arg_3_0._cameraGoldenOffset = arg_3_1
end

function var_0_3.GetCameraPos(arg_4_0)
	local var_4_0 = arg_4_0.point:Copy(arg_4_0._fleetMotion:GetPos())

	var_4_0.x = var_4_0.x + arg_4_0._cameraGoldenOffset
	var_4_0.y = var_4_0.y + var_0_2.CameraNormalHeight
	var_4_0.z = var_4_0.z - var_4_0.y / var_0_2._camera_radian_x_tan

	return var_4_0
end

function var_0_3.Dispose(arg_5_0)
	arg_5_0._fleetMotion = nil
end
