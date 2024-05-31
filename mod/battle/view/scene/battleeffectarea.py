ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleEffectArea")

var_0_0.Battle.BattleEffectArea = var_0_3
var_0_3.__name = "BattleEffectArea"

local var_0_4 = Vector3(0, 3.5, -5)

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._go = arg_1_1
	arg_1_0._aoeData = arg_1_2
	arg_1_0._topCover = arg_1_3

	arg_1_0.Init()

def var_0_3.Init(arg_2_0):
	arg_2_0._tf = arg_2_0._go.transform
	arg_2_0._areaType = arg_2_0._aoeData.GetAreaType()

	if arg_2_0._areaType == var_0_1.AreaType.CUBE:
		arg_2_0.UpdateScale = arg_2_0.updateCubeScale
	elif arg_2_0._areaType == var_0_1.AreaType.COLUMN:
		arg_2_0.UpdateScale = arg_2_0.updateColumnScale

	if arg_2_0._aoeData.GetIFF() == var_0_2.FOE_CODE:
		function arg_2_0.GetAngle()
			return arg_2_0._aoeData.GetAngle() * -1 + 180
	else
		function arg_2_0.GetAngle()
			return arg_2_0._aoeData.GetAngle() * -1

	arg_2_0.Update()

def var_0_3.Update(arg_5_0):
	arg_5_0.UpdateScale()
	arg_5_0.UpdatePosition()
	arg_5_0.UpdateRotation()

def var_0_3.updateCubeScale(arg_6_0):
	local var_6_0 = 1
	local var_6_1 = 1

	if not arg_6_0._aoeData.GetFXStatic():
		var_6_0 = arg_6_0._aoeData.GetWidth() * arg_6_0._aoeData.GetIFF()
		var_6_1 = arg_6_0._aoeData.GetHeight()

	if var_6_0 == arg_6_0._preWidth and var_6_1 == arg_6_0._preHeight:
		return

	arg_6_0._tf.localScale = Vector3(var_6_0, 1, var_6_1)
	arg_6_0._preWidth = var_6_0
	arg_6_0._preHeight = var_6_1

def var_0_3.updateColumnScale(arg_7_0):
	local var_7_0 = arg_7_0._aoeData.GetRange()

	if var_7_0 == arg_7_0._preRange:
		return

	arg_7_0._tf.localScale = Vector3(var_7_0, 1, var_7_0)
	arg_7_0._preRange = var_7_0

def var_0_3.UpdatePosition(arg_8_0):
	if arg_8_0._topCover:
		arg_8_0._tf.position = arg_8_0._aoeData.GetPosition() + var_0_4
	else
		arg_8_0._tf.position = arg_8_0._aoeData.GetPosition()

def var_0_3.UpdateRotation(arg_9_0):
	local var_9_0 = arg_9_0.GetAngle()

	if arg_9_0._preAngle == var_9_0:
		return

	arg_9_0._tf.localEulerAngles = Vector3(0, var_9_0, 0)
	arg_9_0._preAngle = var_9_0

def var_0_3.Dispose(arg_10_0):
	var_0_0.Battle.BattleResourceManager.GetInstance().DestroyOb(arg_10_0._go)

	arg_10_0._go = None
