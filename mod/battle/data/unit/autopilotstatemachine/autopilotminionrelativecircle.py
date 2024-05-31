ys = ys or {}

local var_0_0 = ys
local var_0_1 = Vector3.up
local var_0_2 = class("AutoPilotMinionRelativeCircle", var_0_0.Battle.IPilot)

var_0_0.Battle.AutoPilotMinionRelativeCircle = var_0_2
var_0_2.__name = "AutoPilotMinionRelativeCircle"

def var_0_2.Ctor(arg_1_0, ...):
	var_0_2.super.Ctor(arg_1_0, ...)

def var_0_2.SetParameter(arg_2_0, arg_2_1, arg_2_2):
	var_0_2.super.SetParameter(arg_2_0, arg_2_1, arg_2_2)

	arg_2_0._radius = arg_2_1.radius

	if arg_2_1.antiClockWise == True:
		arg_2_0.GetDirection = var_0_2._antiClockWise
	else
		arg_2_0.GetDirection = var_0_2._clockWise

	arg_2_0._nextBuffID = arg_2_1.buffID

def var_0_2._clockWise(arg_3_0, arg_3_1):
	if arg_3_0.IsExpired():
		arg_3_0.Finish()

		return Vector3.zero

	local var_3_0 = arg_3_0._pilot.GetTarget().GetMaster()

	if not var_3_0.IsAlive():
		if arg_3_0._nextBuffID:
			local var_3_1 = var_0_0.Battle.BattleBuffUnit.New(arg_3_0._nextBuffID)

			arg_3_0._pilot.GetTarget().AddBuff(var_3_1)

		return Vector3.zero

	local var_3_2 = var_3_0.GetPosition()

	if (arg_3_1 - var_3_2).magnitude > arg_3_0._radius:
		return (var_3_2 - arg_3_1).normalized
	else
		local var_3_3 = (var_3_2 - arg_3_1).normalized
		local var_3_4 = -var_3_3.z
		local var_3_5 = var_3_3.x

		return Vector3(var_3_4, 0, var_3_5)

def var_0_2._antiClockWise(arg_4_0, arg_4_1):
	if arg_4_0._duration > 0 and pg.TimeMgr.GetInstance().GetCombatTime() - arg_4_0._startTime > arg_4_0._duration:
		arg_4_0.Finish()

		return Vector3.zero

	local var_4_0 = arg_4_0._pilot.GetTarget().GetMaster()

	if not var_4_0.IsAlive():
		if arg_4_0._nextBuffID:
			local var_4_1 = var_0_0.Battle.BattleBuffUnit.New(arg_4_0._nextBuffID)

			arg_4_0._pilot.GetTarget().AddBuff(var_4_1)

		return Vector3.zero

	local var_4_2 = var_4_0.GetPosition()

	if (arg_4_1 - var_4_2).magnitude > arg_4_0._radius:
		return (var_4_2 - arg_4_1).normalized
	else
		local var_4_3 = (var_4_2 - arg_4_1).normalized
		local var_4_4 = var_4_3.z
		local var_4_5 = -var_4_3.x

		return Vector3(var_4_4, 0, var_4_5)
