ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleAntiAirUnit", var_0_0.Battle.BattleWeaponUnit)

var_0_0.Battle.BattleAntiAirUnit = var_0_1
var_0_1.__name = "BattleAntiAirUnit"

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.TriggerBuffOnFire(arg_2_0)
	arg_2_0._host:TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_ANTIAIR_FIRE_NEAR, {})
end

function var_0_1.FilterTarget(arg_3_0)
	local var_3_0 = arg_3_0._dataProxy:GetAircraftList()
	local var_3_1 = {}
	local var_3_2 = arg_3_0._host:GetIFF()
	local var_3_3 = 1

	for iter_3_0, iter_3_1 in pairs(var_3_0) do
		if iter_3_1:GetIFF() ~= var_3_2 and iter_3_1:IsVisitable() then
			var_3_1[var_3_3] = iter_3_1
			var_3_3 = var_3_3 + 1
		end
	end

	return var_3_1
end

function var_0_1.Spawn(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = var_0_1.super.Spawn(arg_4_0, arg_4_1, arg_4_2)

	var_4_0:SetDirectHitUnit(arg_4_2)

	return var_4_0
end

function var_0_1.TriggerBuffWhenSpawn(arg_5_0, arg_5_1)
	local var_5_0 = {
		_bullet = arg_5_1,
		bulletTag = arg_5_1:GetExtraTag()
	}

	arg_5_0._host:TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_BULLET_CREATE, var_5_0)
	arg_5_0._host:TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_ANTIAIR_BULLET_CREATE, var_5_0)
end
