ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffOverrideBullet = class("BattleBuffOverrideBullet", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffOverrideBullet.__name = "BattleBuffOverrideBullet"

local var_0_1 = var_0_0.Battle.BattleBuffOverrideBullet

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._bulletType = arg_2_0._tempData.arg_list.bullet_type
	arg_2_0._override = arg_2_0._tempData.arg_list.override

def var_0_1.onBulletCreate(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if not arg_3_0.equipIndexRequire(arg_3_3.equipIndex):
		return

	local var_3_0 = arg_3_3._bullet

	if var_3_0.GetType() == arg_3_0._bulletType:
		arg_3_0.overrideBullet(var_3_0)

def var_0_1.overrideBullet(arg_4_0, arg_4_1):
	for iter_4_0, iter_4_1 in pairs(arg_4_0._override):
		if iter_4_0 == "diverFilter":
			arg_4_1.SetDiverFilter(iter_4_1)
			arg_4_1.ResetCldSurface()
		elif iter_4_0 == "ignoreShield":
			arg_4_1.SetIgnoreShield(iter_4_1)
