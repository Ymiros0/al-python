ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("AutoPilotMinionRelativeStay", var_0_0.Battle.IPilot)

var_0_0.Battle.AutoPilotMinionRelativeStay = var_0_1
var_0_1.__name = "AutoPilotMinionRelativeStay"

def var_0_1.Ctor(arg_1_0, ...):
	var_0_1.super.Ctor(arg_1_0, ...)

def var_0_1.SetParameter(arg_2_0, arg_2_1, arg_2_2):
	var_0_1.super.SetParameter(arg_2_0, arg_2_1, arg_2_2)

	arg_2_0._distX = arg_2_1.x
	arg_2_0._distZ = arg_2_1.z
	arg_2_0._nextBuffID = arg_2_1.buffID

def var_0_1.GetDirection(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0._pilot.GetTarget().GetMaster()

	if not var_3_0.IsAlive():
		if arg_3_0._nextBuffID:
			local var_3_1 = var_0_0.Battle.BattleBuffUnit.New(arg_3_0._nextBuffID)

			arg_3_0._pilot.GetTarget().AddBuff(var_3_1)

		return Vector3.zero

	local var_3_2 = var_3_0.GetPosition()
	local var_3_3 = Vector3(var_3_2.x + arg_3_0._distX, arg_3_1.y, var_3_2.z + arg_3_0._distZ) - arg_3_1

	if arg_3_0.IsExpired():
		arg_3_0.Finish()

	if var_3_3.magnitude < 0.4:
		return Vector3.zero
	else
		var_3_3.y = 0

		return var_3_3.SetNormalize()
