local var_0_0 = class("NewGuildResultStatisticsPage", import("..NewBattleResultStatisticsPage"))

function var_0_0.UpdateGrade(arg_1_0)
	local var_1_0 = "battlescore/grade_label_clear"

	LoadImageSpriteAsync(var_1_0, arg_1_0.gradeTxt, false)
	setActive(arg_1_0.gradeIcon, false)
end

function var_0_0.UpdatePainting(arg_2_0, arg_2_1)
	arg_2_0:UpdatePaintingPosition()
	arg_2_0:UpdateMvpPainting(arg_2_1)
end

return var_0_0
