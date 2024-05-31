ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = class("BattleBuffAddFleetBuff", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffAddFleetBuff = var_0_2
var_0_2.__name = "BattleBuffAddFleetBuff"

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

def var_0_2.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._level = arg_2_2.GetLv()
	arg_2_0._fleetBuffID = arg_2_0._tempData.arg_list.fleet_buff_id

def var_0_2.onAttach(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_1.GetUnitType() != var_0_1.UnitType.PLAYER_UNIT:
		return

	local var_3_0 = var_0_0.Battle.BattleFleetBuffUnit.New(arg_3_0._fleetBuffID)

	arg_3_1.GetFleetVO().AttachFleetBuff(var_3_0)

def var_0_2.onRemove(arg_4_0, arg_4_1, arg_4_2):
	if arg_4_1.GetUnitType() != var_0_1.UnitType.PLAYER_UNIT:
		return

	arg_4_1.GetFleetVO().RemoveFleetBuff(arg_4_0._fleetBuffID)
