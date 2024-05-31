ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("AutoPilotBrownian", var_0_0.Battle.IPilot)

var_0_0.Battle.AutoPilotBrownian = var_0_1
var_0_1.__name = "AutoPilotBrownian"

def var_0_1.Ctor(arg_1_0, ...):
	var_0_1.super.Ctor(arg_1_0, ...)

def var_0_1.SetParameter(arg_2_0, arg_2_1, arg_2_2):
	var_0_1.super.SetParameter(arg_2_0, arg_2_1, arg_2_2)

	arg_2_0._randomPoint = {
		X1 = arg_2_1.X1,
		X2 = arg_2_1.X2,
		Z1 = arg_2_1.Z1,
		Z2 = arg_2_1.Z2
	}
	arg_2_0._stop = arg_2_1.stopCount
	arg_2_0._move = arg_2_1.moveCount
	arg_2_0._random = arg_2_1.randomCount or 30

def var_0_1.Active(arg_3_0, arg_3_1):
	arg_3_0._stopCount = arg_3_0._stop
	arg_3_0._moveCount = 0
	arg_3_0._randomCount = 0
	arg_3_0._referencePoint = var_0_0.Battle.BattleFormulas.RandomPos(arg_3_0._randomPoint)

	var_0_1.super.Active(arg_3_0, arg_3_1)

def var_0_1.GetDirection(arg_4_0, arg_4_1):
	if arg_4_0.IsExpired():
		arg_4_0.Finish()

		return Vector3.zero

	arg_4_0._moveCount = arg_4_0._moveCount or 0

	if arg_4_0._stop > arg_4_0._stopCount:
		arg_4_0._stopCount = arg_4_0._stopCount + 1

		return Vector3.zero

	local var_4_0 = arg_4_0._referencePoint - arg_4_1

	if var_4_0.magnitude < 0.4 or arg_4_0._randomCount > arg_4_0._random:
		if arg_4_0._move < arg_4_0._moveCount:
			arg_4_0._stopCount = 0
			arg_4_0._moveCount = 0
		else
			arg_4_0._randomCount = 0

			local var_4_1 = var_0_0.Battle.BattleFormulas.RandomPos(arg_4_0._randomPoint)
			local var_4_2 = 0

			while Vector3.SqrDistance(var_4_1, arg_4_1) < 5:
				var_4_1 = var_0_0.Battle.BattleFormulas.RandomPos(arg_4_0._randomPoint)
				var_4_2 = var_4_2 + 1

			arg_4_0._referencePoint = var_4_1

		return Vector3.zero
	else
		arg_4_0._randomCount = arg_4_0._randomCount + 1
		arg_4_0._moveCount = arg_4_0._moveCount + 1

		return var_4_0.SetNormalize()
