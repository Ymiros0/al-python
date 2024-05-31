local var_0_0 = class("NewSubRoutineResultGradePage", import("..NewBattleResultGradePage"))

def var_0_0.GetGetObjectives(arg_1_0):
	local var_1_0 = arg_1_0.contextData
	local var_1_1 = {}
	local var_1_2 = var_1_0.statistics.subRunResult
	local var_1_3 = i18n("battle_result_base_score")

	table.insert(var_1_1, {
		icon = "check_mark",
		text = setColorStr(var_1_3, "#FFFFFFFF"),
		value = setColorStr("+" .. var_1_2.basePoint, COLOR_BLUE)
	})

	local var_1_4 = i18n("battle_result_dead_score", var_1_2.deadCount)

	table.insert(var_1_1, {
		icon = "check_mark",
		text = setColorStr(var_1_4, "#FFFFFFFF"),
		value = setColorStr("-" .. var_1_2.losePoint, COLOR_BLUE)
	})

	local var_1_5 = i18n("battle_result_score", var_1_2.score)

	table.insert(var_1_1, {
		icon = "check_mark",
		text = setColorStr(var_1_5, "#FFFFFFFF"),
		value = setColorStr("+" .. var_1_2.point, COLOR_BLUE)
	})

	local var_1_6 = i18n("battle_result_score_total")

	table.insert(var_1_1, {
		text = setColorStr(var_1_6, "#FFFFFFFF"),
		value = setColorStr(var_1_2.total, COLOR_YELLOW)
	})

	return var_1_1

return var_0_0
