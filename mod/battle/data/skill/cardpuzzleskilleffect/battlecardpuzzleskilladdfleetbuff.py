ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleCardPuzzleSkillAddFleetBuff", var_0_0.Battle.BattleCardPuzzleSkillEffect)

var_0_0.Battle.BattleCardPuzzleSkillAddFleetBuff = var_0_1
var_0_1.__name = "BattleCardPuzzleSkillAddFleetBuff"

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._fleetBuffID = arg_1_0._tempData.arg_list.fleet_buff_id
	arg_1_0._initStack = arg_1_0._tempData.arg_list.init_stack or 1

def var_0_1.SkillEffectHandler(arg_2_0):
	local var_2_0 = arg_2_0.GetCardPuzzleComponent().GetBuffManager()
	local var_2_1 = var_0_0.Battle.BattleFleetBuffUnit.New(arg_2_0._fleetBuffID)

	var_2_0.AttachCardPuzzleBuff(var_2_1)
	arg_2_0.Finale()
