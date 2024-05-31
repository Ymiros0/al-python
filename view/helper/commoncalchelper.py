local var_0_0 = class("CommonCalcHelper")

def var_0_0.CalcDungeonHp(arg_1_0, arg_1_1):
	local var_1_0 = 0
	local var_1_1 = {}
	local var_1_2 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(arg_1_0)

	for iter_1_0, iter_1_1 in ipairs(var_1_2.stages):
		for iter_1_2, iter_1_3 in ipairs(iter_1_1.waves):
			if iter_1_3.triggerType == ys.Battle.BattleConst.WaveTriggerType.NORMAL:
				for iter_1_4, iter_1_5 in ipairs(iter_1_3.spawn):
					local var_1_3 = iter_1_5.monsterTemplateID

					var_1_1[#var_1_1 + 1] = var_1_3

				if iter_1_3.reinforcement:
					for iter_1_6, iter_1_7 in ipairs(iter_1_3.reinforcement):
						local var_1_4 = iter_1_7.monsterTemplateID

						var_1_1[#var_1_1 + 1] = var_1_4

	for iter_1_8, iter_1_9 in ipairs(var_1_1):
		local var_1_5 = ys.Battle.BattleDataFunction.GetMonsterTmpDataFromID(iter_1_9)

		var_1_0 = var_1_0 + (var_1_5.durability + var_1_5.durability_growth * ((arg_1_1 - 1) / 1000))

	return var_1_0

return var_0_0
