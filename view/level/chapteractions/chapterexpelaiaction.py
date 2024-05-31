local var_0_0 = class("ChapterExpelAIAction")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.actType = arg_1_1.act_type
	arg_1_0.line = {
		row = arg_1_1.ai_pos.row,
		column = arg_1_1.ai_pos.column
	}
	arg_1_0.shipUpdate = _.map(arg_1_1.ship_update, function(arg_2_0)
		return {
			id = arg_2_0.id,
			hpRant = arg_2_0.hp_rant
		})
	arg_1_0.cellFlagUpdates = _.map(arg_1_1.cell_flag_list, function(arg_3_0)
		return {
			row = arg_3_0.pos.row,
			column = arg_3_0.pos.column,
			flag_list = _.map(arg_3_0.flag_list, function(arg_4_0)
				return arg_4_0)
		})
	arg_1_0.cellUpdates = _.map(arg_1_1.map_update, function(arg_5_0)
		if arg_5_0.item_type != ChapterConst.AttachNone and arg_5_0.item_type != ChapterConst.AttachBorn and arg_5_0.item_type != ChapterConst.AttachBorn_Sub and (arg_5_0.item_type != ChapterConst.AttachStory or arg_5_0.item_data != ChapterConst.StoryTrigger):
			return arg_5_0.item_type == ChapterConst.AttachChampion and ChapterChampionPackage.New(arg_5_0) or ChapterCell.New(arg_5_0))

def var_0_0.SetTargetLine(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.sourceLine = arg_6_1
	arg_6_0.targetLine = arg_6_2

def var_0_0.applyTo(arg_7_0, arg_7_1, arg_7_2):
	if not arg_7_2:
		local var_7_0 = 0
		local var_7_1 = 0

		if #arg_7_0.cellFlagUpdates > 0:
			_.each(arg_7_0.cellFlagUpdates, function(arg_8_0)
				local var_8_0 = arg_7_1.getChapterCell(arg_8_0.row, arg_8_0.column)

				if var_8_0:
					var_8_0.updateFlagList(arg_8_0)
				else
					var_8_0 = ChapterCell.New(arg_8_0)

				arg_7_1.updateChapterCell(var_8_0))

			var_7_0 = bit.bor(var_7_0, ChapterConst.DirtyCellFlag)

		if #arg_7_0.cellUpdates > 0:
			_.each(arg_7_0.cellUpdates, function(arg_9_0)
				if isa(arg_9_0, ChapterChampionPackage):
					local var_9_0 = arg_7_1.mergeChampion(arg_9_0, True) and ChapterConst.DirtyChampionPosition or ChapterConst.DirtyChampion

					var_7_0 = bit.bor(var_7_0, var_9_0)
				else
					arg_7_1.mergeChapterCell(arg_9_0, True)

					var_7_0 = bit.bor(var_7_0, ChapterConst.DirtyAttachment))
			arg_7_1.clearChapterCell(arg_7_0.sourceLine.row, arg_7_0.sourceLine.column)

			local var_7_2 = arg_7_1.getChampion(arg_7_0.sourceLine.row, arg_7_0.sourceLine.column)

			if var_7_2:
				arg_7_1.RemoveChampion(var_7_2)

			var_7_0 = bit.bor(var_7_0, ChapterConst.DirtyAttachment)
			var_7_1 = bit.bor(var_7_1, ChapterConst.DirtyAutoAction)

		if #arg_7_0.shipUpdate > 0:
			_.each(arg_7_0.shipUpdate, function(arg_10_0)
				arg_7_1.updateFleetShipHp(arg_10_0.id, arg_10_0.hpRant))

			var_7_0 = bit.bor(var_7_0, ChapterConst.DirtyFleet)

		return True, var_7_0, var_7_1

	return True

def var_0_0.PlayAIAction(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	seriesAsync({
		function(arg_12_0)
			arg_11_2.viewComponent.levelStageView.SwitchBottomStagePanel(False)
			arg_11_2.viewComponent.grid.HideAirExpelAimingMark()
			arg_12_0(),
		arg_11_3
	})

return var_0_0
