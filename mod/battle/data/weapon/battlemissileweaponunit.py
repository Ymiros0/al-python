ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleDataFunction
local var_0_3 = class("BattleMissileWeaponUnit", var_0_0.Battle.BattleWeaponUnit)

var_0_0.Battle.BattleMissileWeaponUnit = var_0_3
var_0_3.__name = "BattleMissileWeaponUnit"

def var_0_3.CalculateFixedExplodePosition(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1._range
	local var_1_1 = (arg_1_0._host.GetDirection() == var_0_1.UnitDir.RIGHT and 1 or -1) * var_1_0
	local var_1_2 = arg_1_0._host.GetPosition()

	return Vector3(var_1_2.x + var_1_1, 0, 0)

def var_0_3.CalculateRandTargetPosition(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_2.GetCLDZCenterPosition()
	local var_2_1 = arg_2_1.GetTemplate().extra_param
	local var_2_2 = var_2_1.accuracy
	local var_2_3 = 0

	if var_2_2:
		var_2_3 = arg_2_1.GetAttrByName(var_2_2)

	local var_2_4 = var_2_1.randomOffsetX or 0
	local var_2_5 = var_2_1.randomOffsetZ or 0
	local var_2_6 = math.max(0, var_2_4 - var_2_3)
	local var_2_7 = math.max(0, var_2_5 - var_2_3)
	local var_2_8 = var_2_1.offsetX or 0
	local var_2_9 = var_2_1.offsetZ or 0

	if var_2_6 != 0:
		var_2_6 = var_2_6 * (math.random() - 0.5) + var_2_8

	if var_2_7 != 0:
		var_2_7 = var_2_7 * (math.random() - 0.5) + var_2_9

	local var_2_10 = var_2_1.targetOffsetX or 0
	local var_2_11 = var_2_1.targetOffsetZ or 0

	return Vector3(var_2_0.x + var_2_6 + var_2_10, 0, var_2_0.z + var_2_7 + var_2_11)

def var_0_3.createMajorEmitter(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5):
	local function var_3_0(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4)
		local var_4_0 = arg_3_0._emitBulletIDList[arg_3_2]
		local var_4_1 = arg_3_0.Spawn(var_4_0, arg_4_4, var_0_3.INTERNAL)

		var_4_1.SetOffsetPriority(arg_4_3)
		var_4_1.SetShiftInfo(arg_4_0, arg_4_1)
		var_4_1.SetRotateInfo(None, arg_3_0.GetBaseAngle(), arg_4_2)
		var_4_1.RegisterOnTheAir(arg_3_0.ChoiceOntheAir(var_4_1))
		arg_3_0.DispatchBulletEvent(var_4_1)

	return var_0_3.super.createMajorEmitter(arg_3_0, arg_3_1, arg_3_2, arg_3_3, var_3_0, None)

def var_0_3.ChoiceOntheAir(arg_5_0, arg_5_1):
	return function()
		local var_6_0 = arg_5_1.GetMissileTargetPosition()
		local var_6_1, var_6_2, var_6_3 = arg_5_1.GetRotateInfo()
		local var_6_4, var_6_5 = arg_5_1.GetOffset()

		var_6_0.Add(Vector3(var_6_4, 0, var_6_5))

		local var_6_6 = Quaternion.Euler(0, var_6_3, 0)
		local var_6_7 = pg.Tool.FilterY(var_6_0 - arg_5_1.GetSpawnPosition())
		local var_6_8 = arg_5_1.GetSpawnPosition() + var_6_6 * var_6_7

		arg_5_1.SetExplodePosition(var_6_8)
		var_0_0.Battle.BattleMissileFactory.CreateBulletAlert(arg_5_1)
