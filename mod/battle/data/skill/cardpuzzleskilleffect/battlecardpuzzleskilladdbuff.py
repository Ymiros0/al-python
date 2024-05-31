ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleCardPuzzleSkillAddBuff", var_0_0.Battle.BattleCardPuzzleSkillEffect)

var_0_0.Battle.BattleCardPuzzleSkillAddBuff = var_0_1
var_0_1.__name = "BattleCardPuzzleSkillAddBuff"

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._buffID = arg_1_0._tempData.arg_list.buff_id

def var_0_1.SkillEffectHandler(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0.GetTarget()

	for iter_2_0, iter_2_1 in ipairs(var_2_0):
		if iter_2_1.IsAlive():
			local var_2_1 = var_0_0.Battle.BattleBuffUnit.New(arg_2_0._buffID, 1, arg_2_0._caster)

			iter_2_1.AddBuff(var_2_1)

	arg_2_0.Finale()
