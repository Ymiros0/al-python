local var_0_0 = class("ChapterMissileExplodeAction")

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

def var_0_0.SetTargetLine(arg_6_0, arg_6_1):
	arg_6_0.targetLine = arg_6_1
	arg_6_0.flagStrategy = True

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
					local var_9_0 = arg_7_1.mergeChampion(arg_9_0) and ChapterConst.DirtyChampionPosition or ChapterConst.DirtyChampion

					var_7_0 = bit.bor(var_7_0, var_9_0)
				else
					arg_7_1.mergeChapterCell(arg_9_0)

					var_7_0 = bit.bor(var_7_0, ChapterConst.DirtyAttachment))

			var_7_1 = bit.bor(var_7_1, ChapterConst.DirtyAutoAction)

		if #arg_7_0.shipUpdate > 0:
			_.each(arg_7_0.shipUpdate, function(arg_10_0)
				arg_7_1.updateFleetShipHp(arg_10_0.id, arg_10_0.hpRant))

			var_7_0 = bit.bor(var_7_0, ChapterConst.DirtyFleet)

		return True, var_7_0, var_7_1

	return True

def var_0_0.PlayAIAction(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	local var_11_0

	if arg_11_0.targetLine:
		var_11_0 = {
			arg_11_0.targetLine
		}
	else
		local function var_11_1(arg_12_0)
			local var_12_0 = arg_11_1.GetRawChapterCell(arg_12_0.row, arg_12_0.column)

			return var_12_0 and table.contains(var_12_0.GetFlagList(), ChapterConst.FlagMissleAiming) and not table.contains(arg_12_0.flag_list, ChapterConst.FlagMissleAiming)

		var_11_0 = _.filter(arg_11_0.cellFlagUpdates, function(arg_13_0)
			return var_11_1(arg_13_0))

	seriesAsync({
		function(arg_14_0)
			if not arg_11_0.flagStrategy:
				return arg_14_0()

			arg_11_2.viewComponent.doPlayAnim("MissileStrikeBar", function(arg_15_0)
				setActive(arg_15_0, False)
				arg_14_0()),
		function(arg_16_0)
			table.ParallelIpairsAsync(var_11_0, function(arg_17_0, arg_17_1, arg_17_2)
				arg_11_2.viewComponent.grid.PlayMissileExplodAnim(arg_17_1, arg_17_2), arg_16_0),
		function(arg_18_0)
			table.ParallelIpairsAsync(arg_11_0.cellUpdates, function(arg_19_0, arg_19_1, arg_19_2)
				if ChapterConst.IsBossCell(arg_19_1):
					arg_11_2.viewComponent.grid.PlayShellFx(arg_19_1)
					arg_19_2()
				else
					local var_19_0 = arg_11_1.GetRawChapterCell(arg_19_1.row, arg_19_1.column)
					local var_19_1 = var_19_0 and var_19_0.data or 0
					local var_19_2 = "-" .. (arg_19_1.data - var_19_1) / 100 .. "%"

					arg_11_2.viewComponent.strikeEnemy(arg_19_1, var_19_2, arg_19_2), arg_18_0),
		function(arg_20_0)
			arg_11_2.viewComponent.levelStageView.SwitchBottomStagePanel(False)
			arg_11_2.viewComponent.grid.HideMissileAimingMark()
			arg_20_0(),
		arg_11_3
	})

return var_0_0
