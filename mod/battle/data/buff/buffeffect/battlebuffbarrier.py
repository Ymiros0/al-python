ys = ys or {}

local var_0_0 = ys
local var_0_1 = pg.effect_offset

var_0_0.Battle.BattleBuffBarrier = class("BattleBuffBarrier", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffBarrier.__name = "BattleBuffBarrier"

local var_0_2 = var_0_0.Battle.BattleBuffBarrier

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

def var_0_2.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._durability = var_2_0.durability
	arg_2_0._dir = arg_2_1.GetDirection()
	arg_2_0._unit = arg_2_1
	arg_2_0._dataProxy = var_0_0.Battle.BattleDataProxy.GetInstance()
	arg_2_0._centerPos = arg_2_1.GetPosition()

	local function var_2_1(arg_3_0)
		arg_2_0._dataProxy.HandleDamage(arg_3_0, arg_2_0._unit)
		arg_3_0.Intercepted()
		arg_2_0._dataProxy.RemoveBulletUnit(arg_3_0.GetUniqueID())

	local var_2_2 = var_2_0.cld_data
	local var_2_3 = var_2_2.box
	local var_2_4 = Clone(var_2_2.offset)

	if arg_2_1.GetDirection() == var_0_0.Battle.BattleConst.UnitDir.LEFT:
		var_2_4[1] = -var_2_4[1]

	arg_2_0._wall = arg_2_0._dataProxy.SpawnWall(arg_2_0, var_2_1, var_2_3, var_2_4)

def var_0_2.onUpdate(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	local var_4_0 = arg_4_3.timeStamp

	arg_4_0._centerPos = arg_4_1.GetPosition()

def var_0_2.onTakeDamage(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	if arg_5_0.damageCheck(arg_5_3):
		local var_5_0 = arg_5_3.damage

		arg_5_0._durability = arg_5_0._durability - var_5_0

		if arg_5_0._durability > 0:
			arg_5_3.damage = 0
		else
			arg_5_3.damage = -arg_5_0._durability

			arg_5_2.SetToCancel()

def var_0_2.onAttach(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	if arg_6_0._unit.IsBoss():
		arg_6_0._unit.BarrierStateChange(arg_6_0._durability, arg_6_2.GetDuration())

def var_0_2.onRemove(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	if arg_7_0._unit.IsBoss():
		arg_7_0._unit.BarrierStateChange(0)

def var_0_2.GetIFF(arg_8_0):
	return arg_8_0._unit.GetIFF()

def var_0_2.GetPosition(arg_9_0):
	return arg_9_0._centerPos

def var_0_2.IsWallActive(arg_10_0):
	return arg_10_0._durability > 0
