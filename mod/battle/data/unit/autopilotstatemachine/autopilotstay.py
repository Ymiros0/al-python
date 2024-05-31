ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("AutoPilotStay", var_0_0.Battle.IPilot)

var_0_0.Battle.AutoPilotStay = var_0_1
var_0_1.__name = "AutoPilotStay"

def var_0_1.Ctor(arg_1_0, ...):
	var_0_1.super.Ctor(arg_1_0, ...)

def var_0_1.GetDirection(arg_2_0):
	if arg_2_0.IsExpired():
		arg_2_0.Finish()

	return Vector3.zero
