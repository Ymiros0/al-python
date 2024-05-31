local var_0_0 = class("CommanderSkill", import("..BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.exp = arg_1_1.exp

def var_0_0.getExp(arg_2_0):
	return arg_2_0.exp

def var_0_0.bindConfigTable(arg_3_0):
	return pg.commander_skill_template

def var_0_0.getLevel(arg_4_0):
	return arg_4_0.getConfig("lv")

def var_0_0.isMaxLevel(arg_5_0):
	return arg_5_0.getConfig("next_id") == 0

def var_0_0.getNextLevelExp(arg_6_0):
	return arg_6_0.getConfig("exp")

def var_0_0.addExp(arg_7_0, arg_7_1):
	arg_7_0.exp = arg_7_0.exp + arg_7_1

	while arg_7_0.canLevelUp():
		arg_7_0.exp = arg_7_0.exp - arg_7_0.getNextLevelExp()
		arg_7_0.id = arg_7_0.getConfig("next_id")
		arg_7_0.configId = arg_7_0.id

def var_0_0.canLevelUp(arg_8_0):
	return arg_8_0.getNextLevelExp() <= arg_8_0.exp and not arg_8_0.isMaxLevel()

def var_0_0.getTacticSkill(arg_9_0):
	return arg_9_0.getConfig("effect_tactic")

def var_0_0.GetTacticSkillForWorld(arg_10_0):
	return arg_10_0.getConfig("effect_tactic_world")

def var_0_0.GetSkillGroup(arg_11_0):
	local var_11_0 = {}
	local var_11_1 = arg_11_0.getConfig("prev_id")

	while var_11_1 and var_11_1 != 0:
		local var_11_2 = pg.commander_skill_template[var_11_1]

		table.insert(var_11_0, var_11_2)

		var_11_1 = var_11_2.prev_id

	table.insert(var_11_0, pg.commander_skill_template[arg_11_0.configId])

	local var_11_3 = arg_11_0.getConfig("next_id")

	while var_11_3 and var_11_3 != 0:
		local var_11_4 = pg.commander_skill_template[var_11_3]

		table.insert(var_11_0, var_11_4)

		var_11_3 = var_11_4.next_id

	table.sort(var_11_0, function(arg_12_0, arg_12_1)
		return arg_12_0.lv < arg_12_1.lv)

	return var_11_0

return var_0_0
