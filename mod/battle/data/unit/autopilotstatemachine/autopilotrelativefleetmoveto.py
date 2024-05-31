ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("AutoPilotRelativeFleetMoveTo", var_0_0.Battle.IPilot)

var_0_0.Battle.AutoPilotRelativeFleetMoveTo = var_0_1
var_0_1.__name = "AutoPilotRelativeFleetMoveTo"

def var_0_1.Ctor(arg_1_0, ...):
	var_0_1.super.Ctor(arg_1_0, ...)

def var_0_1.SetParameter(arg_2_0, arg_2_1, arg_2_2):
	var_0_1.super.SetParameter(arg_2_0, arg_2_1, arg_2_2)

	arg_2_0._offsetX = arg_2_1.offsetX
	arg_2_0._offsetZ = arg_2_1.offsetZ
	arg_2_0._fixX = arg_2_1.X
	arg_2_0._fixZ = arg_2_1.Z
	arg_2_0._targetFleetVO = var_0_0.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(var_0_0.Battle.BattleConfig.FRIENDLY_CODE)

def var_0_1.GetDirection(arg_3_0, arg_3_1):
	if arg_3_0.IsExpired():
		arg_3_0.Finish()

		return Vector3.zero

	local var_3_0
	local var_3_1
	local var_3_2 = arg_3_0._targetFleetVO.GetMotion().GetPos()

	if arg_3_0._offsetX:
		var_3_0 = var_3_2.x + arg_3_0._offsetX
	elif arg_3_0._fixX:
		var_3_0 = arg_3_0._fixX
	else
		var_3_0 = arg_3_1.x

	if arg_3_0._offsetZ:
		var_3_1 = var_3_2.z + arg_3_0._offsetZ
	elif arg_3_0._fixZ:
		var_3_1 = arg_3_0._fixZ
	else
		var_3_1 = arg_3_1.z

	local var_3_3 = Vector3.New(var_3_0, 0, var_3_1) - arg_3_1

	var_3_3.y = 0

	if var_3_3.magnitude < arg_3_0._valve:
		var_3_3 = Vector3.zero

	return var_3_3.normalized
