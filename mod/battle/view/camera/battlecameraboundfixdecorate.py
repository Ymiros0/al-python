ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleCameraBoundFixDecorate = class("BattleCameraBoundFixDecorate")
var_0_0.Battle.BattleCameraBoundFixDecorate.__name = "BattleCameraBoundFixDecorate"

local var_0_3 = var_0_0.Battle.BattleCameraBoundFixDecorate

def var_0_3.Ctor(arg_1_0):
	return

def var_0_3.SetMapData(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	arg_2_0._cameraUpperBound = arg_2_1 + 30
	arg_2_0._cameraLowerBound = arg_2_2 - 5
	arg_2_0._cameraLeftBound = arg_2_3 - 3
	arg_2_0._cameraRightBound = arg_2_4 + 3
	arg_2_0._cameraHalfWidth = var_0_1.CAMERA_SIZE * pg.CameraFixMgr.GetInstance().targetRatio
	arg_2_0._cameraLeftBoundPoint = arg_2_0._cameraLeftBound + arg_2_0._cameraHalfWidth
	arg_2_0._cameraRightBoundPoint = arg_2_0._cameraRightBound - arg_2_0._cameraHalfWidth
	arg_2_0._projectionConst = var_0_1.CAMERA_SIZE / var_0_2._camera_radian_x_sin

	return arg_2_0._cameraUpperBound, arg_2_0._cameraLowerBound, arg_2_0._cameraLeftBound, arg_2_0._cameraRightBound

def var_0_3.GetCameraPos(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.y / var_0_2._camera_radian_x_tan + arg_3_0._projectionConst

	if arg_3_1.z < arg_3_0._cameraLowerBound:
		arg_3_1.z = arg_3_0._cameraLowerBound
	elif arg_3_1.z > arg_3_0._cameraUpperBound - var_3_0:
		arg_3_1.z = arg_3_0._cameraUpperBound - var_3_0

	if arg_3_1.x < arg_3_0._cameraLeftBoundPoint:
		arg_3_1.x = arg_3_0._cameraLeftBoundPoint
	elif arg_3_1.x > arg_3_0._cameraRightBoundPoint:
		arg_3_1.x = arg_3_0._cameraRightBoundPoint

	return arg_3_1

def var_0_3.Dispose(arg_4_0):
	arg_4_0._cameraUpperBound = None
	arg_4_0._cameraLowerBound = None
	arg_4_0._cameraLeftBound = None
	arg_4_0._cameraRightBound = None
	arg_4_0._cameraHalfWidth = None
	arg_4_0._cameraLeftBoundPoint = None
	arg_4_0._cameraRightBoundPoint = None
	arg_4_0._projectionConst = None
