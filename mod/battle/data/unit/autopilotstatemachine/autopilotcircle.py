ys = ys or {}

local var_0_0 = ys
local var_0_1 = Vector3.up
local var_0_2 = class("AutoPilotCircle", var_0_0.Battle.IPilot)

var_0_0.Battle.AutoPilotCircle = var_0_2
var_0_2.__name = "AutoPilotCircle"

def var_0_2.Ctor(arg_1_0, ...):
	var_0_2.super.Ctor(arg_1_0, ...)

def var_0_2.SetParameter(arg_2_0, arg_2_1, arg_2_2):
	var_0_2.super.SetParameter(arg_2_0, arg_2_1, arg_2_2)

	arg_2_0._referencePoint = Vector3(arg_2_1.x, 0, arg_2_1.z)
	arg_2_0._radius = arg_2_1.radius

	if arg_2_1.antiClockWise == True:
		arg_2_0.GetDirection = var_0_2._antiClockWise
	else
		arg_2_0.GetDirection = var_0_2._clockWise

def var_0_2._clockWise(arg_3_0, arg_3_1):
	if arg_3_0.IsExpired():
		arg_3_0.Finish()

		return Vector3.zero

	if (arg_3_1 - arg_3_0._referencePoint).magnitude > arg_3_0._radius:
		return (arg_3_0._referencePoint - arg_3_1).normalized
	else
		local var_3_0 = (arg_3_0._referencePoint - arg_3_1).normalized
		local var_3_1 = -var_3_0.z
		local var_3_2 = var_3_0.x

		return Vector3(var_3_1, 0, var_3_2)

def var_0_2._antiClockWise(arg_4_0, arg_4_1):
	if arg_4_0._duration > 0 and pg.TimeMgr.GetInstance().GetCombatTime() - arg_4_0._startTime > arg_4_0._duration:
		arg_4_0.Finish()

		return Vector3.zero

	if (arg_4_1 - arg_4_0._referencePoint).magnitude > arg_4_0._radius:
		return (arg_4_0._referencePoint - arg_4_1).normalized
	else
		local var_4_0 = (arg_4_0._referencePoint - arg_4_1).normalized
		local var_4_1 = var_4_0.z
		local var_4_2 = -var_4_0.x

		return Vector3(var_4_1, 0, var_4_2)
