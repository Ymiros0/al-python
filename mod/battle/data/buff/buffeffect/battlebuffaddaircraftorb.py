ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffAddAircraftOrb = class("BattleBuffAddAircraftOrb", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffAddAircraftOrb.__name = "BattleBuffAddAircraftOrb"

local var_0_1 = var_0_0.Battle.BattleBuffAddAircraftOrb

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._buffID = arg_2_0._tempData.arg_list.buff_id
	arg_2_0._rant = arg_2_0._tempData.arg_list.rant or 10000
	arg_2_0._level = arg_2_0._tempData.arg_list.level or 1

def var_0_1.onAircraftCreate(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if not arg_3_0.equipIndexRequire(arg_3_3.equipIndex):
		return

	local var_3_0 = {
		buffID = arg_3_0._buffID,
		rant = arg_3_0._rant,
		level = arg_3_0._level
	}
	local var_3_1 = arg_3_3.aircraft.GetWeapon()

	for iter_3_0, iter_3_1 in ipairs(var_3_1):
		iter_3_1.SetBulletOrbData(var_3_0)
