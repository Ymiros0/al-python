ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleCameraFocusBulet = class("BattleCameraFocusBulet")
var_0_0.Battle.BattleCameraFocusBulet.__name = "BattleCameraFocusBulet"

local var_0_3 = var_0_0.Battle.BattleCameraFocusBulet

def var_0_3.Ctor(arg_1_0):
	return

def var_0_3.SetUnit(arg_2_0, arg_2_1):
	arg_2_0._unit = arg_2_1

def var_0_3.GetCameraPos(arg_3_0):
	local var_3_0 = arg_3_0._unit.GetPosition().Clone()

	var_3_0.y = var_3_0.y + var_0_2.CameraFocusHeight
	var_3_0.z = var_3_0.z - var_3_0.y / var_0_2._camera_radian_x_tan

	return var_3_0

def var_0_3.Dispose(arg_4_0):
	arg_4_0._unit = None
