ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleUnitEvent
local var_0_3 = var_0_0.Battle.BattleTargetChoise
local var_0_4 = class("BattleAutoMissileUnit", var_0_0.Battle.BattleWeaponUnit)

var_0_0.Battle.BattleAutoMissileUnit = var_0_4
var_0_4.__name = "BattleAutoMissileUnit"

def var_0_4.Ctor(arg_1_0):
	var_0_4.super.Ctor(arg_1_0)

def var_0_4.createMajorEmitter(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	local function var_2_0(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4)
		local var_3_0 = arg_2_0._emitBulletIDList[arg_2_2]
		local var_3_1 = arg_2_0.Spawn(var_3_0, arg_3_4, var_0_4.INTERNAL)

		var_3_1.SetOffsetPriority(arg_3_3)
		var_3_1.SetShiftInfo(arg_3_0, arg_3_1)

		if arg_2_0._tmpData.aim_type == var_0_1.WeaponAimType.AIM and arg_3_4 != None:
			var_3_1.SetRotateInfo(arg_3_4.GetBeenAimedPosition(), arg_2_0.GetBaseAngle(), arg_3_2)
		else
			var_3_1.SetRotateInfo(None, arg_2_0.GetBaseAngle(), arg_3_2)

		var_3_1.setTrackingTarget(arg_3_4)

		local var_3_2 = {}

		var_3_1.SetTrackingFXData(var_3_2)
		arg_2_0.DispatchBulletEvent(var_3_1)

		return var_3_1

	local function var_2_1()
		for iter_4_0, iter_4_1 in ipairs(arg_2_0._majorEmitterList):
			if iter_4_1.GetState() != iter_4_1.STATE_STOP:
				return

		arg_2_0.EnterCoolDown()

	arg_2_3 = arg_2_3 or var_0_4.EMITTER_NORMAL

	local var_2_2 = var_0_0.Battle[arg_2_3].New(var_2_0, var_2_1, arg_2_1)

	arg_2_0._majorEmitterList[#arg_2_0._majorEmitterList + 1] = var_2_2

	return var_2_2

def var_0_4.Tracking(arg_5_0):
	return var_0_3.TargetWeightiest(arg_5_0, None, arg_5_0.GetFilteredList())[1]
