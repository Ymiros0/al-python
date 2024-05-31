ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = var_0_0.Battle.BattleFormulas
local var_0_4 = var_0_0.Battle.BattleDataFunction
local var_0_5 = class("BattleSpaceLaserWeaponUnit", var_0_0.Battle.BattleWeaponUnit)

var_0_0.Battle.BattleSpaceLaserWeaponUnit = var_0_5
var_0_5.__name = "BattleSpaceLaserWeaponUnit"

def var_0_5.createMajorEmitter(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5):
	local var_1_0 = arg_1_0.CreateEmitter(arg_1_3, arg_1_1, arg_1_2)

	arg_1_0._majorEmitterList[#arg_1_0._majorEmitterList + 1] = var_1_0

	return var_1_0

def var_0_5.CreateEmitter(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_1 = arg_2_1 or var_0_5.EMITTER_NORMAL

	local var_2_0
	local var_2_1
	local var_2_2
	local var_2_3 = 0

	local function var_2_4(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4)
		if arg_2_0._currentState == arg_2_0.STATE_DISABLE:
			return

		local var_3_0 = arg_2_0._emitBulletIDList[arg_2_3]
		local var_3_1 = arg_2_0.Spawn(var_3_0, arg_3_4, var_0_5.INTERNAL)

		var_2_3 = var_2_3 + 1
		arg_3_4 = arg_2_0._tmpData.aim_type == var_0_1.WeaponAimType.AIM and arg_3_4 or None

		var_3_1.SetOffsetPriority(arg_3_3)
		var_3_1.SetShiftInfo(arg_3_0, arg_3_1)
		var_3_1.setTrackingTarget(arg_3_4)
		var_3_1.SetYAngle(var_2_1)
		var_3_1.SetLifeTime(var_3_1.GetTemplate().extra_param.attack_time)
		var_3_1.RegisterLifeEndCB(function()
			var_2_3 = var_2_3 - 1

			if var_2_3 > 0:
				return

			if arg_2_0._currentState == arg_2_0.STATE_DISABLE:
				return

			for iter_4_0, iter_4_1 in ipairs(arg_2_0._majorEmitterList):
				if iter_4_1.GetState() != iter_4_1.STATE_STOP:
					return

			arg_2_0.EnterCoolDown())

		local var_3_2 = var_2_2 or arg_3_4 and pg.Tool.FilterY(arg_3_4.GetCLDZCenterPosition())

		var_3_1.SetRotateInfo(var_3_2, arg_2_0.GetBaseAngle(), arg_3_2)
		arg_2_0.DispatchBulletEvent(var_3_1, var_2_0 or var_3_2)

		return var_3_1

	local function var_2_5(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4)
		if arg_2_0._currentState == arg_2_0.STATE_DISABLE:
			return

		local var_5_0 = arg_2_0._emitBulletIDList[arg_2_3]
		local var_5_1 = var_0_4.GetBulletTmpDataFromID(var_5_0).extra_param.aim_time

		if not var_5_1 or not (var_5_1 > 0):
			var_2_4(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4)

			return

		local var_5_2 = arg_2_0.Spawn(var_5_0, arg_5_4, var_0_5.INTERNAL)

		var_2_3 = var_2_3 + 1
		arg_5_4 = arg_2_0._tmpData.aim_type == var_0_1.WeaponAimType.AIM and arg_5_4 or None

		var_5_2.setTrackingTarget(arg_5_4)
		var_5_2.SetOffsetPriority(arg_5_3)
		var_5_2.SetShiftInfo(arg_5_0, arg_5_1)
		var_5_2.SetLifeTime(var_5_2.GetTemplate().extra_param.aim_time)
		var_5_2.SetAlert(True)
		var_5_2.RegisterLifeEndCB(function()
			var_2_3 = var_2_3 - 1
			var_2_0 = pg.Tool.FilterY(var_5_2.GetPosition() - Vector3(arg_5_0, 0, arg_5_1))
			var_2_1 = var_5_2.GetYAngle()
			var_2_2 = var_5_2.GetRotateInfo()

			var_2_4(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4))

		local var_5_3 = var_5_2.GetTemplate().alert_fx

		if var_5_3 and #var_5_3 > 0:
			var_5_2.SetModleID(var_5_3)

		local var_5_4 = arg_5_4 and pg.Tool.FilterY(arg_5_4.GetCLDZCenterPosition())

		var_5_2.SetRotateInfo(var_5_4, arg_2_0.GetBaseAngle(), arg_5_2)
		arg_2_0.DispatchBulletEvent(var_5_2, var_5_4)

		return var_5_2

	local function var_2_6()
		return

	return (var_0_0.Battle[arg_2_1].New(var_2_5, var_2_6, arg_2_2))

def var_0_5.SingleFire(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4):
	assert(False, "Not Support only fire for BattleSpaceLaserWeapon")
