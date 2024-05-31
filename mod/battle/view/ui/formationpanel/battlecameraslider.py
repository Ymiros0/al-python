ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleCameraSlider = class("BattleCameraSlider")

local var_0_2 = class("BattleCameraSlider")

var_0_0.Battle.BattleCameraSlider = var_0_2
var_0_2.__name = "BattleCameraSlider"

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1

	arg_1_0.Init()

def var_0_2.Init(arg_2_0):
	SetActive(arg_2_0._go, True)

	arg_2_0._distX, arg_2_0._distY = 0, 0
	arg_2_0._dirX, arg_2_0._dirY = 0, 0
	arg_2_0._isPress = False

	local var_2_0 = pg.CameraFixMgr.GetInstance()

	arg_2_0._screenWidth, arg_2_0._screenHeight = var_2_0.actualWidth, var_2_0.actualHeight

	arg_2_0._go.GetComponent("StickController").SetStickFunc(function(arg_3_0, arg_3_1)
		arg_2_0.updateStick(arg_3_0, arg_3_1))

def var_0_2.updateStick(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0._initX = False
	arg_4_0._initY = False

	if arg_4_2 == -1:
		arg_4_0._startX = None
		arg_4_0._startY = None
		arg_4_0._isPress = False
	else
		arg_4_0._isPress = True

		local var_4_0 = arg_4_1.x
		local var_4_1 = arg_4_1.y

		if arg_4_0._startX == None:
			arg_4_0._startX = var_4_0
			arg_4_0._startY = var_4_1
			arg_4_0._initX = True
			arg_4_0._initY = True
		else
			local var_4_2 = var_4_0 - arg_4_0._lastPosX

			if var_4_2 * arg_4_0._dirX < 0:
				arg_4_0._startX = var_4_0
				arg_4_0._initX = True

			if var_4_2 != 0:
				arg_4_0._dirX = var_4_2

			local var_4_3 = var_4_1 - arg_4_0._lastPosY

			if var_4_3 * arg_4_0._dirY < 0:
				arg_4_0._startY = var_4_1
				arg_4_0._initY = True

			if var_4_3 != 0:
				arg_4_0._dirY = var_4_3

		arg_4_0._distX = (var_4_0 - arg_4_0._startX) / arg_4_0._screenWidth
		arg_4_0._distY = (var_4_1 - arg_4_0._startY) / arg_4_0._screenHeight

	arg_4_0._lastPosX = arg_4_1.x
	arg_4_0._lastPosY = arg_4_1.y

def var_0_2.GetDistance(arg_5_0):
	return arg_5_0._distX, arg_5_0._distY

def var_0_2.IsFirstPress(arg_6_0):
	return arg_6_0._initX, arg_6_0._initY

def var_0_2.IsPress(arg_7_0):
	return arg_7_0._isPress
