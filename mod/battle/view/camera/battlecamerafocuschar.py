ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleCameraFocusChar = class("BattleCameraFocusChar")
var_0_0.Battle.BattleCameraFocusChar.__name = "BattleCameraFocusChar"

local var_0_3 = var_0_0.Battle.BattleCameraFocusChar

def var_0_3.Ctor(arg_1_0):
	arg_1_0._point = Vector3.zero

def var_0_3.SetUnit(arg_2_0, arg_2_1):
	arg_2_0._unit = arg_2_1

def var_0_3.GetCameraPos(arg_3_0):
	local var_3_0 = arg_3_0._unit.GetPosition()

	arg_3_0._point.Set(var_3_0.x, var_3_0.y, var_3_0.z)

	arg_3_0._point.y = arg_3_0._point.y + var_0_2.CameraFocusHeight
	arg_3_0._point.z = arg_3_0._point.z - arg_3_0._point.y / var_0_2._camera_radian_x_tan

	if arg_3_0._unit.GetIFF() == var_0_1.FOE_CODE:
		arg_3_0._point.x = arg_3_0._point.x + 7
	else
		arg_3_0._point.x = arg_3_0._point.x - 7

	return arg_3_0._point

def var_0_3.Dispose(arg_4_0):
	arg_4_0._unit = None
