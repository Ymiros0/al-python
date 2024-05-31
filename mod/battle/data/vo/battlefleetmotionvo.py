ys = ys or {}
pg = pg or {}

local var_0_0 = ys
local var_0_1 = pg
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattleFormulas
local var_0_4 = var_0_0.Battle.BattleConfig
local var_0_5 = class("BattleFleetMotionVO")

var_0_0.Battle.BattleFleetMotionVO = var_0_5
var_0_5.__name = "BattleFleetMotionVO"

def var_0_5.Ctor(arg_1_0):
	arg_1_0._pos = Vector3.zero
	arg_1_0._speed = Vector3.zero
	arg_1_0._lastDir = var_0_2.NORMALIZE_FLEET_SPEED
	arg_1_0._rotateAngle = Quaternion.identity
	arg_1_0._isCalibrateAcc = False

def var_0_5.GetPos(arg_2_0):
	return arg_2_0._pos

def var_0_5.GetSpeed(arg_3_0):
	return arg_3_0._speed.Clone()

def var_0_5.GetDirAngle(arg_4_0):
	return arg_4_0._rotateAngle

def var_0_5.UpdatePos(arg_5_0, arg_5_1):
	arg_5_0._pos = arg_5_1.GetPosition()

def var_0_5.UpdateVelocityAndDirection(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	local var_6_0 = arg_6_1
	local var_6_1 = arg_6_2
	local var_6_2 = arg_6_3
	local var_6_3 = Vector3(var_6_1, 0, var_6_2).Mul(var_6_0)

	arg_6_0.UpdateSpeed(var_6_3)

def var_0_5.UpdateSpeed(arg_7_0, arg_7_1):
	if arg_7_0._speed != arg_7_1:
		arg_7_0._speed = arg_7_1

		if not arg_7_1.EqualZero():
			arg_7_0._lastDir = arg_7_1

		arg_7_0._rotateAngle.SetFromToRotation1(var_0_2.NORMALIZE_FLEET_SPEED, arg_7_0._lastDir)

def var_0_5.CalibrateAcc(arg_8_0, arg_8_1):
	arg_8_0._isCalibrateAcc = arg_8_1

def var_0_5.SetPos(arg_9_0, arg_9_1):
	arg_9_0._pos = arg_9_1
