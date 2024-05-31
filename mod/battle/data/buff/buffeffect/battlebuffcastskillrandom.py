ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleAttr

var_0_0.Battle.BattleBuffCastSkillRandom = class("BattleBuffCastSkillRandom", var_0_0.Battle.BattleBuffCastSkill)
var_0_0.Battle.BattleBuffCastSkillRandom.__name = "BattleBuffCastSkillRandom"

local var_0_2 = var_0_0.Battle.BattleBuffCastSkillRandom

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._skillList = {}

def var_0_2.spell(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0._tempData.arg_list

	if var_2_0.skill_id_list:
		local var_2_1 = {}
		local var_2_2 = var_2_0.range

		for iter_2_0, iter_2_1 in ipairs(var_2_0.skill_id_list):
			var_2_1[iter_2_1] = var_2_2[iter_2_0]

		local var_2_3 = math.random()

		for iter_2_2, iter_2_3 in pairs(var_2_1):
			local var_2_4 = iter_2_3[1]
			local var_2_5 = iter_2_3[2]

			if var_2_4 <= var_2_3 and var_2_3 < var_2_5:
				arg_2_0._skillList[iter_2_2] = arg_2_0._skillList[iter_2_2] or var_0_0.Battle.BattleSkillUnit.GenerateSpell(iter_2_2, arg_2_0._level, arg_2_1, attData)

				local var_2_6 = arg_2_0._skillList[iter_2_2]

				if arg_2_2 and arg_2_2.target:
					var_2_6.SetTarget({
						arg_2_2.target
					})

				var_2_6.Cast(arg_2_1, arg_2_0._commander)
	elif var_2_0.random_skill_tag:
		local var_2_7 = var_2_0.random_skill_tag
		local var_2_8 = arg_2_1.GetLabelTag()
		local var_2_9 = {}

		for iter_2_4, iter_2_5 in ipairs(var_2_8):
			local var_2_10, var_2_11 = string.find(iter_2_5, var_2_7)

			if var_2_10:
				local var_2_12 = tonumber(string.sub(iter_2_5, var_2_11 + 1, #iter_2_5))

				if not table.contains(var_2_9, var_2_12):
					table.insert(var_2_9, var_2_12)

		if #var_2_9 > 0:
			local var_2_13 = var_2_9[math.random(#var_2_9)]

			arg_2_0._skillList[var_2_13] = arg_2_0._skillList[var_2_13] or var_0_0.Battle.BattleSkillUnit.GenerateSpell(var_2_13, arg_2_0._level, arg_2_1, attData)

			local var_2_14 = arg_2_0._skillList[var_2_13]

			if arg_2_2 and arg_2_2.target:
				var_2_14.SetTarget({
					arg_2_2.target
				})

			var_2_14.Cast(arg_2_1, arg_2_0._commander)

def var_0_2.Clear(arg_3_0):
	var_0_2.super.Clear(arg_3_0)

	for iter_3_0, iter_3_1 in pairs(arg_3_0._skillList):
		iter_3_1.Clear()
