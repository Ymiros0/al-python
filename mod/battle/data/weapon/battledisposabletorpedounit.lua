ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = class("BattleDisposableTorpedoUnit", var_0_0.Battle.BattleManualTorpedoUnit)

var_0_0.Battle.BattleDisposableTorpedoUnit = var_0_2
var_0_2.__name = "BattleDisposableTorpedoUnit"

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0)
end

function var_0_2.EnterCoolDown(arg_2_0)
	return
end

function var_0_2.Fire(arg_3_0)
	var_0_2.super.Fire(arg_3_0)
	arg_3_0._playerTorpedoVO:Deduct(arg_3_0)
	arg_3_0._playerTorpedoVO:DispatchOverLoadChange()

	return true
end

function var_0_2.OverHeat(arg_4_0)
	arg_4_0._currentState = arg_4_0.STATE_OVER_HEAT
end

function var_0_2.GetType(arg_5_0)
	return var_0_0.Battle.BattleConst.EquipmentType.DISPOSABLE_TORPEDO
end

function var_0_2.createMajorEmitter(arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4, arg_6_5)
	return var_0_2.super.createMajorEmitter(arg_6_0, 1, arg_6_2, arg_6_3, arg_6_4, arg_6_5)
end
