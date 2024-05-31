local var_0_0 = class("ChapterAirSupportAIAction", import(".ChapterMissileExplodeAction"))

def var_0_0.PlayAIAction(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	seriesAsync({
		function(arg_2_0)
			arg_1_2.viewComponent.doPlayAnim("AirStrikeBar", function(arg_3_0)
				setActive(arg_3_0, False)
				arg_2_0()),
		function(arg_4_0)
			table.ParallelIpairsAsync(arg_1_0.cellUpdates, function(arg_5_0, arg_5_1, arg_5_2)
				local var_5_0 = arg_1_1.GetRawChapterCell(arg_5_1.row, arg_5_1.column)
				local var_5_1 = var_5_0 and var_5_0.data or 0
				local var_5_2 = "-" .. (arg_5_1.data - var_5_1) / 100 .. "%"

				arg_1_2.viewComponent.strikeEnemy(arg_5_1, var_5_2, arg_5_2), arg_4_0),
		function(arg_6_0)
			arg_1_2.viewComponent.levelStageView.SwitchBottomStagePanel(False)
			arg_1_2.viewComponent.grid.HideAirSupportAimingMark()
			arg_6_0(),
		arg_1_3
	})

return var_0_0
