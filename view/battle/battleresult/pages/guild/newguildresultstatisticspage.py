local var_0_0 = class("NewGuildResultStatisticsPage", import("..NewBattleResultStatisticsPage"))

def var_0_0.UpdateGrade(arg_1_0):
	local var_1_0 = "battlescore/grade_label_clear"

	LoadImageSpriteAsync(var_1_0, arg_1_0.gradeTxt, False)
	setActive(arg_1_0.gradeIcon, False)

def var_0_0.UpdatePainting(arg_2_0, arg_2_1):
	arg_2_0.UpdatePaintingPosition()
	arg_2_0.UpdateMvpPainting(arg_2_1)

return var_0_0
