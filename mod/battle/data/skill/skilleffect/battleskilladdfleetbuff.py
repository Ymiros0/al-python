ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst

var_0_0.Battle.BattleSkillAddFleetBuff = class("BattleSkillAddFleetBuff", var_0_0.Battle.BattleSkillEffect)
var_0_0.Battle.BattleSkillAddFleetBuff.__name = "BattleSkillAddFleetBuff"

local var_0_2 = var_0_0.Battle.BattleSkillAddFleetBuff

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._fleetBuffID = arg_1_0._tempData.arg_list.fleet_buff_id

def var_0_2.DoDataEffect(arg_2_0, arg_2_1, arg_2_2):
	if arg_2_2.IsAlive() and arg_2_2.GetUnitType() == var_0_1.UnitType.PLAYER_UNIT:
		local var_2_0 = var_0_0.Battle.BattleFleetBuffUnit.New(arg_2_0._fleetBuffID)

		arg_2_2.GetFleetVO().AttachFleetBuff(var_2_0)
