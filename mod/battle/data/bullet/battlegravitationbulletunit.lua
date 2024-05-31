ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = class("BattleGravitationBulletUnit", var_0_0.Battle.BattleBulletUnit)

var_0_0.Battle.BattleGravitationBulletUnit = var_0_2
var_0_2.__name = "BattleGravitationBulletUnit"

function var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
end

function var_0_2.Update(arg_2_0, arg_2_1)
	if arg_2_0._pierceCount > 0 then
		var_0_2.super.Update(arg_2_0, arg_2_1)
	end
end

function var_0_2.SetTemplateData(arg_3_0, arg_3_1)
	var_0_2.super.SetTemplateData(arg_3_0, arg_3_1)

	arg_3_0._hitInterval = arg_3_1.hit_type.interval or 0.2
end

function var_0_2.GetExplodePostion(arg_4_0)
	return arg_4_0._explodePos
end

function var_0_2.SetExplodePosition(arg_5_0, arg_5_1)
	arg_5_0._explodePos = arg_5_1
end

function var_0_2.DealDamage(arg_6_0)
	arg_6_0._nextDamageTime = pg.TimeMgr.GetInstance():GetCombatTime() + arg_6_0._hitInterval
end

function var_0_2.CanDealDamage(arg_7_0)
	if not arg_7_0._nextDamageTime then
		arg_7_0._nextDamageTime = pg.TimeMgr.GetInstance():GetCombatTime() + arg_7_0._tempData.extra_param.alert_duration

		return false
	else
		return arg_7_0._nextDamageTime < pg.TimeMgr.GetInstance():GetCombatTime()
	end
end

function var_0_2.Hit(arg_8_0, arg_8_1, arg_8_2)
	var_0_2.super.Hit(arg_8_0, arg_8_1, arg_8_2)

	arg_8_0._pierceCount = arg_8_0._pierceCount - 1
	arg_8_0._position.y = 100
end
