ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleEnvironmentBehaviourMovement", var_0_0.Battle.BattleEnvironmentBehaviour)

var_0_0.Battle.BattleEnvironmentBehaviourMovement = var_0_3
var_0_3.__name = "BattleEnvironmentBehaviourMovement"

def var_0_3.Ctor(arg_1_0):
	arg_1_0._movebeginTime = None
	arg_1_0._moveEndTime = None
	arg_1_0._lastPosition = None
	arg_1_0._destPosition = None
	arg_1_0._targetIndex = 1

	var_0_3.super.Ctor(arg_1_0)

def var_0_3.SetTemplate(arg_2_0, arg_2_1):
	var_0_3.super.SetTemplate(arg_2_0, arg_2_1)

	arg_2_0._route = arg_2_1.route or {}
	arg_2_0._random_duration = arg_2_1.random_duration or {
		1,
		5
	}
	arg_2_0._random_speed = arg_2_1.random_speed or 1

	local var_2_0 = arg_2_0._unit.GetTemplate()
	local var_2_1
	local var_2_2

	if #var_2_0.cld_data == 1:
		var_2_1 = var_2_0.cld_data[1]
		var_2_2 = var_2_1
	elif #var_2_0.cld_data == 2:
		var_2_1, var_2_2 = unpack(var_2_0.cld_data)

	local var_2_3 = {
		var_0_0.Battle.BattleDataProxy.GetInstance().GetFleetBoundByIFF(var_0_2.FRIENDLY_CODE)
	}

	var_2_3[3] = var_2_3[3] + var_2_1
	var_2_3[4] = var_2_3[4] - var_2_1
	var_2_3[2] = var_2_3[2] + var_2_2
	var_2_3[1] = var_2_3[1] - var_2_2
	arg_2_0._bounds = var_2_3
	arg_2_0._lastPosition = Vector3(unpack(var_2_0.coordinate))

	if arg_2_1.random_range:
		arg_2_0._randomRangeX = arg_2_1.random_range[1]
		arg_2_0._randomRangeZ = arg_2_1.random_range[2]
		arg_2_0._resetRandomRange = True

def var_0_3.doBehaviour(arg_3_0):
	local var_3_0 = pg.TimeMgr.GetInstance().GetCombatTime()

	if not arg_3_0._moveEndTime:
		local var_3_1 = arg_3_0._route[arg_3_0._targetIndex]

		arg_3_0._movebeginTime = var_3_0

		if var_3_1:
			arg_3_0._destPosition = Vector3(unpack(var_3_1))
			arg_3_0._moveEndTime = var_3_0 + var_3_1[4]
			arg_3_0._targetIndex = arg_3_0._targetIndex + 1
		else
			local var_3_2 = arg_3_0.GenerateRandomPlayerAreaPoint()
			local var_3_3 = math.random(unpack(arg_3_0._random_duration))
			local var_3_4 = var_3_3 * arg_3_0._random_speed
			local var_3_5 = (var_3_2 - arg_3_0._lastPosition).Magnitude()

			if var_3_5 < var_3_4:
				var_3_3 = var_3_5 / arg_3_0._random_speed
			else
				var_3_2 = Vector3.Lerp(arg_3_0._lastPosition, var_3_2, var_3_4 / var_3_5)

			arg_3_0._moveEndTime = var_3_0 + var_3_3
			arg_3_0._destPosition = var_3_2

	if var_3_0 < arg_3_0._moveEndTime:
		local var_3_6 = Vector3.Lerp(arg_3_0._lastPosition, arg_3_0._destPosition, (var_3_0 - arg_3_0._movebeginTime) / (arg_3_0._moveEndTime - arg_3_0._movebeginTime))

		arg_3_0._unit._aoeData.SetPosition(var_3_6)
	else
		arg_3_0._unit._aoeData.SetPosition(arg_3_0._destPosition)

		arg_3_0._lastPosition = arg_3_0._destPosition
		arg_3_0._moveEndTime = None

	var_0_3.super.doBehaviour(arg_3_0)

def var_0_3.GenerateRandomPlayerAreaPoint(arg_4_0):
	local var_4_0 = arg_4_0._bounds
	local var_4_1 = math.random(var_4_0[3], var_4_0[4])
	local var_4_2 = math.random(var_4_0[2], var_4_0[1])

	if arg_4_0._resetRandomRange:
		arg_4_0.resetRandomBound(var_4_1, var_4_2)

	return Vector3(var_4_1, 0, var_4_2)

def var_0_3.resetRandomBound(arg_5_0, arg_5_1, arg_5_2):
	arg_5_0._bounds[3] = arg_5_1 - arg_5_0._randomRangeX
	arg_5_0._bounds[4] = arg_5_1 + arg_5_0._randomRangeX
	arg_5_0._bounds[2] = arg_5_2 - arg_5_0._randomRangeZ
	arg_5_0._bounds[1] = arg_5_2 + arg_5_0._randomRangeZ
	arg_5_0._resetRandomRange = False

def var_0_3.Dispose(arg_6_0):
	var_0_3.super.Dispose(arg_6_0)
	table.clear(arg_6_0)
