local var_0_0 = class("NewAirFightResultGradePage", import("..NewBattleResultGradePage"))

def var_0_0.LoadGrade(arg_1_0, arg_1_1):
	local var_1_0 = {
		"d",
		"c",
		"b",
		"a",
		"s"
	}
	local var_1_1 = arg_1_0.contextData.score
	local var_1_2

	var_1_2 = var_1_1 > ys.Battle.BattleConst.BattleScore.C

	local var_1_3
	local var_1_4
	local var_1_5
	local var_1_6 = var_1_0[var_1_1 + 1]
	local var_1_7 = "battlescore/battle_score_" .. var_1_6 .. "/letter_" .. var_1_6
	local var_1_8 = "battlescore/battle_score_" .. var_1_6 .. "/label_" .. var_1_6

	LoadImageSpriteAsync(var_1_7, arg_1_0.gradeIcon, True)
	LoadImageSpriteAsync(var_1_8, arg_1_0.gradeTxt, True)

	if arg_1_1:
		arg_1_1()

def var_0_0.GetGetObjectives(arg_2_0):
	local var_2_0 = {}
	local var_2_1 = arg_2_0.contextData.statistics._airFightStatistics
	local var_2_2 = i18n("fighterplane_destroy_tip") .. var_2_1.kill

	table.insert(var_2_0, {
		text = setColorStr(var_2_2, "#FFFFFFFF"),
		value = setColorStr(var_2_1.score, COLOR_BLUE)
	})

	local var_2_3 = i18n("fighterplane_hit_tip") .. var_2_1.hit

	table.insert(var_2_0, {
		text = setColorStr(var_2_3, "#FFFFFFFF"),
		value = setColorStr(-var_2_1.lose, COLOR_BLUE)
	})

	local var_2_4 = i18n("fighterplane_destroy_tip")

	table.insert(var_2_0, {
		text = setColorStr(var_2_4, "#FFFFFFFF"),
		value = setColorStr(var_2_1.total, COLOR_YELLOW)
	})

	return var_2_0

return var_0_0
