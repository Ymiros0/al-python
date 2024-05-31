ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = class("BattleLaserEffect", var_0_0.Battle.BattleEffectArea)

var_0_0.Battle.BattleLaserEffect = var_0_2
var_0_2.__name = "BattleLaserEffect"

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

def var_0_2.SetStatic(arg_2_0):
	return

def var_0_2.Init(arg_3_0):
	arg_3_0._tf = arg_3_0._go.transform
	arg_3_0._laserScript = GetComponent(arg_3_0._go, "LaserScript")
	arg_3_0._waveCount = 0

	arg_3_0.Update()

def var_0_2.Update(arg_4_0):
	arg_4_0.updateLineRenderer()
	arg_4_0.UpdatePosition()

def var_0_2.updateLineRenderer(arg_5_0):
	local var_5_0 = arg_5_0._aoeData.GetHeight()

	arg_5_0._laserScript.width = var_5_0 + math.cos(arg_5_0._waveCount * math.deg2Rad * 3)
	arg_5_0._waveCount = arg_5_0._waveCount + 1
	arg_5_0._laserScript.length = arg_5_0._aoeData.GetWidth()

	local var_5_1 = arg_5_0._aoeData.GetAngle() * math.deg2Rad

	if arg_5_0._aoeData.GetIFF() == -1:
		var_5_1 = var_5_1 + math.pi

	arg_5_0._laserScript.angle = var_5_1
