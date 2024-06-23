from luatable import table, pairs
from Vector3 import Vector2
from alsupport import math, Mathf

from support.helpers.UnitySupport import setActive #!
from Framework.tolua.typeof import typeof #!
from Framework.tolua.tolua import Camera, GameObject #!


import BattleConfig





class BattleVariable:
	@staticmethod
	def Init():
		BattleVariable.speedRatioByIFF = table({
			0: 1,
			1: 1,
			-1: 1
		})
		BattleVariable.focusExemptList = table()
		BattleVariable.MapSpeedRatio = 1
		BattleVariable.MapSpeedFacotrList = table()
		BattleVariable.IFFFactorList = table()

		for iter_1_0, iter_1_1 in pairs(BattleVariable.speedRatioByIFF):
			BattleVariable.IFFFactorList[iter_1_0] = table()

		BattleVariable._lastCameraPos = None

		var_1_0 = UIMgr.GetInstance().GetMainCamera()

		setActive(var_1_0, True)

		BattleVariable._camera = var_1_0.GetComponent(typeof(Camera))
		BattleVariable._cameraTF = BattleVariable._camera.transform
		BattleVariable._uiCamera = GameObject.Find("UICamera").GetComponent(typeof(Camera))

		var_1_1 = math.deg2Rad * BattleVariable._cameraTF.localEulerAngles.x

		BattleVariable._camera_radian_x_sin = math.sin(var_1_1)
		BattleVariable._camera_radian_x_cos = math.cos(var_1_1)
		BattleVariable._camera_radian_x_tan = BattleVariable._camera_radian_x_sin / BattleVariable._camera_radian_x_cos
		BattleVariable.CameraNormalHeight = BattleVariable._camera_radian_x_cos * BattleConfig.CAMERA_SIZE + BattleConfig.CAMERA_BASE_HEIGH
		BattleVariable.CameraFocusHeight = BattleVariable._camera_radian_x_cos * BattleConfig.CAST_CAM_ZOOM_SIZE + BattleConfig.CAMERA_BASE_HEIGH

	@staticmethod
	def Clear():
		BattleVariable.speedRatioByIFF = None
		BattleVariable.focusExemptList = None
		BattleVariable.MapSpeedRatio = None
		BattleVariable.MapSpeedFacotrList = None
		BattleVariable.IFFFactorList = None
		BattleVariable._lastCameraPos = None
		BattleVariable._camera = None
		BattleVariable._cameraTF = None
		BattleVariable._uiCamera = None
		BattleVariable._camera_radian_x_sin = None
		BattleVariable._camera_radian_x_cos = None
		BattleVariable._camera_radian_x_tan = None
		BattleVariable.CameraNormalHeight = None
		BattleVariable.CameraFocusHeight = None

	var_0_3 = 0
	var_0_4 = 0
	var_0_5 = 0
	var_0_6 = 0
	var_0_7 = 0
	var_0_8 = 0

	@staticmethod
	def UpdateCameraPositionArgs():
		var_3_0 = BattleVariable._cameraTF.position
		var_3_1 = BattleVariable._camera.orthographicSize

		if BattleVariable._lastCameraPos == var_3_0 and BattleVariable._lastCameraSize == var_3_1:
			return
		else:
			BattleVariable._lastCameraPos = var_3_0
			BattleVariable._lastCameraSize = var_3_1

		var_3_2 = CameraFixMgr.GetInstance()
		var_3_3 = BattleVariable._camera.ScreenToWorldPoint(var_3_2.leftBottomVector)
		var_3_4 = BattleVariable._camera.ScreenToWorldPoint(var_3_2.rightTopVector)
		var_3_5 = BattleVariable._uiCamera.ScreenToWorldPoint(var_3_2.leftBottomVector)
		var_3_6 = BattleVariable._uiCamera.ScreenToWorldPoint(var_3_2.rightTopVector)

		BattleVariable.var_0_3 = var_3_3.x
		BattleVariable.var_0_4 = var_3_5.x
		BattleVariable.var_0_5 = (var_3_6.x - var_3_5.x) / (var_3_4.x - var_3_3.x)

		var_3_7 = var_3_3.y * 0.866 + var_3_3.z * 0.5
		var_3_8 = var_3_4.y * 0.866 + var_3_4.z * 0.5

		BattleVariable.var_0_6 = var_3_7
		BattleVariable.var_0_7 = var_3_5.y
		BattleVariable.var_0_8 = (var_3_6.y - var_3_5.y) / (var_3_8 - var_3_7)

	@staticmethod
	def CameraPosToUICamera(arg_4_0):
		BattleVariable.CameraPosToUICameraByRef(arg_4_0)

		return arg_4_0

	@staticmethod
	def CameraPosToUICameraByRef(arg_5_0):
		var_5_0 = (arg_5_0.x - BattleVariable.var_0_3) * BattleVariable.var_0_5 + BattleVariable.var_0_4

		arg_5_0.y, arg_5_0.x = (arg_5_0.y * 0.866 + arg_5_0.z * 0.5 - BattleVariable.var_0_6) * BattleVariable.var_0_8 + BattleVariable.var_0_7, var_5_0
		arg_5_0.z = 0

	@staticmethod
	def UIPosToScenePos(arg_6_0, arg_6_1):
		var_6_0 = CameraFixMgr.GetInstance()
		var_6_1 = var_6_0.GetCurrentWidth()
		var_6_2 = var_6_0.GetCurrentHeight()
		var_6_3 = var_6_1 / 1920
		var_6_4 = var_6_2 / 1080

		arg_6_0 = Vector2(var_6_3 * arg_6_0.x, var_6_4 * arg_6_0.y)

		var_6_5 = BattleVariable._uiCamera.ScreenToWorldPoint(arg_6_0)
		var_6_6 = (var_6_5.x - BattleVariable.var0_4) / BattleVariable.var0_5 + BattleVariable.var0_3
		var_6_7 = (var_6_5.y - BattleVariable.var0_7) / BattleVariable.var0_8 + BattleVariable.var0_6
		var_6_8 = math.tan(30 * Mathf.Deg2Rad)
		var_6_9 = var_6_7 / var_6_8 + var_6_7 * var_6_8 * 0.5

		arg_6_1.Set(var_6_6, 0, var_6_9)

	@staticmethod
	def AppendMapFactor(arg_7_0, arg_7_1):
		if BattleVariable.MapSpeedFacotrList[arg_7_0] != None:
			BattleVariable.RemoveMapFactor(arg_7_0)

		BattleVariable.MapSpeedRatio = BattleVariable.MapSpeedRatio * arg_7_1
		BattleVariable.MapSpeedFacotrList[arg_7_0] = arg_7_1

	@staticmethod
	def RemoveMapFactor(arg_8_0):
		var_8_0 = BattleVariable.MapSpeedFacotrList[arg_8_0]

		if var_8_0 != None:
			BattleVariable.MapSpeedRatio = BattleVariable.MapSpeedRatio / var_8_0
			BattleVariable.MapSpeedFacotrList[arg_8_0] = None

	@staticmethod
	def AppendIFFFactor(arg_9_0, arg_9_1, arg_9_2):
		var_9_0 = BattleVariable.IFFFactorList[arg_9_0]

		if var_9_0[arg_9_1] != None:
			BattleVariable.RemoveIFFFactor(arg_9_0, arg_9_1)

		BattleVariable.speedRatioByIFF[arg_9_0] = BattleVariable.speedRatioByIFF[arg_9_0] * arg_9_2
		var_9_0[arg_9_1] = arg_9_2
		BattleVariable.focusExemptList = table()

	@staticmethod
	def RemoveIFFFactor(arg_10_0, arg_10_1):
		var_10_0 = BattleVariable.IFFFactorList[arg_10_0]
		var_10_1 = var_10_0[arg_10_1]

		if var_10_1 != None:
			BattleVariable.speedRatioByIFF[arg_10_0] = BattleVariable.speedRatioByIFF[arg_10_0] / var_10_1
			var_10_0[arg_10_1] = None
			BattleVariable.focusExemptList = table()

	@staticmethod
	def GetSpeedRatio(arg_11_0, arg_11_1):
		return BattleVariable.focusExemptList[arg_11_0] or BattleVariable.speedRatioByIFF[arg_11_1]

	@staticmethod
	def AddExempt(arg_12_0, arg_12_1, arg_12_2):
		var_12_0 = BattleVariable.IFFFactorList[arg_12_1][arg_12_2]

		if var_12_0 != None:
			BattleVariable.focusExemptList[arg_12_0] = BattleVariable.speedRatioByIFF[arg_12_1] / var_12_0
