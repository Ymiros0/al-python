ys = ys or {}

local var_0_0 = ys
local var_0_1 = "BattleCardPuzzleSkillAddBurnDot"
local var_0_2 = class(var_0_1, var_0_0.Battle.BattleCardPuzzleSkillAddBuff)

var_0_0.Battle[var_0_1] = var_0_2
var_0_2.__name = var_0_1

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._buffID = arg_1_0._tempData.arg_list.buff_id
	arg_1_0._stack_count = arg_1_0._tempData.arg_list.stack_count or 0
	arg_1_0._stack_ratio = arg_1_0._tempData.arg_list.stack_ratio or 0

def var_0_2.SkillEffectHandler(arg_2_0):
	local var_2_0 = arg_2_0.GetTarget()

	for iter_2_0, iter_2_1 in ipairs(var_2_0):
		if iter_2_1.IsAlive():
			local var_2_1 = arg_2_0._stack_count
			local var_2_2 = iter_2_1.GetBuff(arg_2_0._buffID)
			local var_2_3 = var_2_2 and var_2_2.GetStack() or 0
			local var_2_4 = var_2_1 + math.floor(var_2_3 * arg_2_0._stack_ratio)
			local var_2_5 = var_0_0.Battle.BattleStackableBuffUnit.New(arg_2_0._buffID, 1, arg_2_0._caster, var_2_4)
			local var_2_6 = arg_2_0.GetCardPuzzleComponent().GetAttrManager()

			var_2_5.SetStackCount(var_2_6.GetCurrent("BurnStackCount"))
			var_2_5.SetUnstackCount(var_2_6.GetCurrent("BurnUnStackCount"))
			iter_2_1.AddBuff(var_2_5)

	arg_2_0.Finale()
