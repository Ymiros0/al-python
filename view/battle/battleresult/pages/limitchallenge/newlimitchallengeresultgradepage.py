local var_0_0 = class("NewLimitChallengeResultGradePage", import("..NewBattleResultGradePage"))

def var_0_0.GetGetObjectives(arg_1_0):
	local var_1_0 = arg_1_0.contextData
	local var_1_1 = {}

	if var_1_0.statistics._battleScore > ys.Battle.BattleConst.BattleScore.C:
		local var_1_2 = var_1_0.statistics._totalTime
		local var_1_3 = math.floor(var_1_2)
		local var_1_4 = ys.Battle.BattleTimerView.formatTime(var_1_3)
		local var_1_5 = i18n("battle_result_total_time")

		table.insert(var_1_1, {
			text = setColorStr(var_1_5, "#FFFFFFFF"),
			value = setColorStr(var_1_4, COLOR_YELLOW)
		})

	return var_1_1

return var_0_0
