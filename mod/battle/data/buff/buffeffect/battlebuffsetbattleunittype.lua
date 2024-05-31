ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffSetBattleUnitType = class("BattleBuffSetBattleUnitType", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffSetBattleUnitType.__name = "BattleBuffSetBattleUnitType"

local var_0_1 = var_0_0.Battle.BattleBuffSetBattleUnitType
local var_0_2 = var_0_0.Battle.BattleAttr

var_0_1.FX_TYPE = var_0_0.Battle.BattleBuffEffect.FX_TTPE_MOD_BATTLE_UNIT_TYPE
var_0_1.ATTR_KEY = "battle_unit_type"

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.GetEffectType(arg_2_0)
	return var_0_1.FX_TYPE
end

function var_0_1.SetArgs(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0._value = arg_3_0._tempData.arg_list.value
end

function var_0_1.onAttach(arg_4_0, arg_4_1, arg_4_2)
	var_0_2.SetCurrent(arg_4_1, var_0_1.ATTR_KEY, arg_4_0._value)
	arg_4_0.flash(arg_4_1)
end

function var_0_1.onRemove(arg_5_0, arg_5_1, arg_5_2)
	var_0_2.SetCurrent(arg_5_1, var_0_1.ATTR_KEY, nil)
	arg_5_0.flash(arg_5_1)
end

function var_0_1.flash(arg_6_0)
	arg_6_0:UpdateBlindInvisibleBySpectre()
	var_0_0.Battle.BattleDataProxy.GetInstance():SwitchSpectreUnit(arg_6_0)
end
