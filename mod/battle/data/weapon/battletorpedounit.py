ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleTorpedoUnit = class("BattleTorpedoUnit", var_0_0.Battle.BattleWeaponUnit)
var_0_0.Battle.BattleTorpedoUnit.__name = "BattleTorpedoUnit"

local var_0_1 = var_0_0.Battle.BattleTorpedoUnit

def var_0_1.Ctor(arg_1_0):
	var_0_0.Battle.BattleTorpedoUnit.super.Ctor(arg_1_0)

def var_0_1.TriggerBuffOnFire(arg_2_0):
	arg_2_0._host.TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_TORPEDO_FIRE, {
		equipIndex = arg_2_0._equipmentIndex
	})

def var_0_1.TriggerBuffWhenSpawn(arg_3_0, arg_3_1):
	local var_3_0 = {
		_bullet = arg_3_1,
		equipIndex = arg_3_0._equipmentIndex,
		bulletTag = arg_3_1.GetExtraTag()
	}

	arg_3_0._host.TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_BULLET_CREATE, var_3_0)
	arg_3_0._host.TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_TORPEDO_BULLET_CREATE, var_3_0)
