ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = class("BattleBuffAddForce", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffAddForce = var_0_2
var_0_2.__name = "BattleBuffAddForce"

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

def var_0_2.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._singularity = arg_2_0._tempData.arg_list.singularity or {
		x = 0,
		z = 0
	}
	arg_2_0._casterGravity = arg_2_0._tempData.arg_list.gravitationalCaster
	arg_2_0._force = arg_2_0._tempData.arg_list.force
	arg_2_0._forceScalteRate = arg_2_0._tempData.arg_list.scale_rate

	if not arg_2_0._casterGravity:
		arg_2_0._staticSingularity = Vector3.New(arg_2_0._singularity.x, 0, arg_2_0._singularity.z)
	else
		local var_2_0 = arg_2_2.GetCaster().GetIFF()

		arg_2_0._singularityOffset = Vector3.New(arg_2_0._singularity.x * var_2_0, 0, arg_2_0._singularity.z)

def var_0_2.onUpdate(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0

	if arg_3_0._casterGravity:
		var_3_0 = arg_3_2.GetCaster().GetPosition() + arg_3_0._singularityOffset
	else
		var_3_0 = arg_3_0._staticSingularity

	local var_3_1 = pg.Tool.FilterY(var_3_0 - arg_3_1.GetPosition())
	local var_3_2 = arg_3_0._force
	local var_3_3 = var_3_1.magnitude

	if var_3_3 < 2:
		var_3_2 = 1e-08
	elif arg_3_0._forceScalteRate:
		var_3_2 = math.min(var_3_3, 1 / var_3_3 * var_3_2)

	arg_3_1.SetUncontrollableSpeed(var_3_1, var_3_2, 1e-18)

	arg_3_0._lastSingularityPos = var_3_0

def var_0_2.onAttach(arg_4_0, arg_4_1, arg_4_2):
	return

def var_0_2.onRemove(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = pg.Tool.FilterY(arg_5_0._lastSingularityPos - arg_5_1.GetPosition())

	arg_5_1.SetUncontrollableSpeed(var_5_0, 0.1, 0.1)
