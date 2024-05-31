ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleCubeCldComponent", var_0_0.Battle.BattleCldComponent)

var_0_0.Battle.BattleCubeCldComponent = var_0_1
var_0_1.__name = "BattleCubeCldComponent"

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5):
	var_0_0.Battle.BattleCubeCldComponent.super.Ctor(arg_1_0)

	arg_1_0._offsetX = arg_1_4
	arg_1_0._offsetZ = arg_1_5
	arg_1_0._offset = Vector3(arg_1_4, 0, arg_1_5)
	arg_1_0._boxSize = Vector3.zero
	arg_1_0._min = Vector3.zero
	arg_1_0._max = Vector3.zero

	arg_1_0.ResetSize(arg_1_1, arg_1_2, arg_1_3)

	arg_1_0._box = pg.CldNode.New()

def var_0_1.ResetSize(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	local var_2_0 = arg_2_1 * 0.5
	local var_2_1 = arg_2_2 * 0.5
	local var_2_2 = arg_2_3 * 0.5

	arg_2_0._boxSize.x = var_2_0
	arg_2_0._boxSize.y = var_2_1
	arg_2_0._boxSize.z = var_2_2
	arg_2_0._min.x = arg_2_0._offsetX - var_2_0
	arg_2_0._min.y = -var_2_1
	arg_2_0._min.z = arg_2_0._offsetZ - var_2_2
	arg_2_0._max.x = arg_2_0._offsetX + var_2_0
	arg_2_0._max.y = var_2_1
	arg_2_0._max.z = arg_2_0._offsetZ + var_2_2

def var_0_1.GetCldBox(arg_3_0, arg_3_1):
	if arg_3_1:
		arg_3_0._cldData.LeftBound = arg_3_1.x - math.abs(arg_3_0._min.x)
		arg_3_0._cldData.RightBound = arg_3_1.x + math.abs(arg_3_0._max.x)
		arg_3_0._cldData.LowerBound = arg_3_1.z - math.abs(arg_3_0._min.z)
		arg_3_0._cldData.UpperBound = arg_3_1.z + math.abs(arg_3_0._max.z)

	return arg_3_0._box.UpdateBox(arg_3_0._min, arg_3_0._max, arg_3_1)

def var_0_1.GetCldBoxSize(arg_4_0):
	return arg_4_0._boxSize
