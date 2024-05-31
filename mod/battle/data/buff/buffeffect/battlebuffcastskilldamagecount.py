ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleAttr

var_0_0.Battle.BattleBuffCastSkillDamageCount = class("BattleBuffCastSkillDamageCount", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffCastSkillDamageCount.__name = "BattleBuffCastSkillDamageCount"

local var_0_2 = var_0_0.Battle.BattleBuffCastSkillDamageCount

var_0_2.FX_TYPE = var_0_0.Battle.BattleBuffEffect.FX_TYPE_CASTER

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

def var_0_2.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._level = arg_2_2.GetLv()
	arg_2_0._skillTable = arg_2_0._tempData.arg_list.damage_attr_list
	arg_2_0._attrTable = {}

def var_0_2.onTakeDamage(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	local var_3_0 = arg_3_3.damageAttr

	if var_3_0:
		local var_3_1 = (arg_3_0._attrTable[var_3_0] or 0) + arg_3_3.damage

		arg_3_0._attrTable[var_3_0] = var_3_1

def var_0_2.onRemove(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	local var_4_0 = 0
	local var_4_1

	for iter_4_0, iter_4_1 in pairs(arg_4_0._attrTable):
		if var_4_0 <= iter_4_1:
			var_4_0 = iter_4_1
			var_4_1 = iter_4_0

	if not var_4_1:
		return

	local var_4_2 = arg_4_0._skillTable[var_4_1]

	arg_4_0._skill = var_0_0.Battle.BattleSkillUnit.GenerateSpell(var_4_2, arg_4_0._level, arg_4_1, arg_4_3)

	if arg_4_3 and arg_4_3.target:
		arg_4_0._skill.SetTarget({
			arg_4_3.target
		})

	arg_4_0._skill.Cast(arg_4_1, arg_4_0._commander)

def var_0_2.Interrupt(arg_5_0):
	var_0_2.super.Interrupt(arg_5_0)

	if arg_5_0._skill:
		arg_5_0._skill.Interrupt()

def var_0_2.Clear(arg_6_0):
	var_0_2.super.Clear(arg_6_0)

	if arg_6_0._skill:
		arg_6_0._skill.Clear()

		arg_6_0._skill = None
