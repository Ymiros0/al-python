local var_0_0 = class("SubAIAction")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.line = {
		row = arg_1_1.ai_pos.row,
		column = arg_1_1.ai_pos.column
	}

	if arg_1_1.target_pos and arg_1_1.target_pos.row < 9999 and arg_1_1.target_pos.column < 9999:
		arg_1_0.target = {
			row = arg_1_1.target_pos.row,
			column = arg_1_1.target_pos.column
		}

	arg_1_0.movePath = _.map(arg_1_1.move_path, function(arg_2_0)
		return {
			row = arg_2_0.row,
			column = arg_2_0.column
		})
	arg_1_0.cellUpdates = {}

	_.each(arg_1_1.map_update, function(arg_3_0)
		if arg_3_0.item_type != ChapterConst.AttachNone and arg_3_0.item_type != ChapterConst.AttachBorn and arg_3_0.item_type != ChapterConst.AttachBorn_Sub and (arg_3_0.item_type != ChapterConst.AttachStory or arg_3_0.item_data != ChapterConst.StoryTrigger):
			local var_3_0 = arg_3_0.item_type == ChapterConst.AttachChampion and ChapterChampionPackage.New(arg_3_0) or ChapterCell.New(arg_3_0)

			table.insert(arg_1_0.cellUpdates, var_3_0))

def var_0_0.applyTo(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_1.getFleet(FleetType.Submarine, arg_4_0.line.row, arg_4_0.line.column)

	if var_4_0:
		return arg_4_0.applyToFleet(arg_4_1, var_4_0, arg_4_2)

	return False, "can not find any submarine at. [" .. arg_4_0.line.row .. ", " .. arg_4_0.line.column .. "]"

def var_0_0.applyToFleet(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	local var_5_0 = 0

	if not arg_5_2.isValid():
		return False, "fleet " .. arg_5_2.id .. " is invalid."

	if arg_5_0.target:
		if arg_5_2.restAmmo <= 0:
			return False, "lack ammo of fleet."

		local var_5_1 = _.detect(arg_5_0.cellUpdates, function(arg_6_0)
			return arg_6_0.row == arg_5_0.target.row and arg_6_0.column == arg_5_0.target.column)

		if not var_5_1:
			return False, "can not find cell update at. [" .. arg_5_0.target.row .. ", " .. arg_5_0.target.column .. "]"

		if not arg_5_3:
			if isa(var_5_1, ChapterChampionPackage):
				arg_5_1.mergeChampion(var_5_1)

				var_5_0 = bit.bor(var_5_0, ChapterConst.DirtyChampion)
			else
				arg_5_1.mergeChapterCell(var_5_1)

				var_5_0 = bit.bor(var_5_0, ChapterConst.DirtyAttachment)

			arg_5_2.restAmmo = arg_5_2.restAmmo - 1
			var_5_0 = bit.bor(var_5_0, ChapterConst.DirtyFleet)
	elif #arg_5_0.movePath > 0:
		if _.any(arg_5_0.movePath, function(arg_7_0)
			local var_7_0 = arg_5_1.getChapterCell(arg_7_0.row, arg_7_0.column)

			return not var_7_0 or not var_7_0.IsWalkable()):
			return False, "invalide move path"

		if not arg_5_3:
			local var_5_2 = arg_5_0.movePath[#arg_5_0.movePath]

			arg_5_2.line = {
				row = var_5_2.row,
				column = var_5_2.column
			}
			var_5_0 = bit.bor(var_5_0, ChapterConst.DirtyFleet)

	return True, var_5_0

def var_0_0.PlayAIAction(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	local var_8_0 = arg_8_1.getFleetIndex(FleetType.Submarine, arg_8_0.line.row, arg_8_0.line.column)

	if var_8_0:
		if arg_8_0.target:
			local var_8_1 = arg_8_1.fleets[var_8_0]
			local var_8_2 = _.detect(arg_8_0.cellUpdates, function(arg_9_0)
				return arg_9_0.row == arg_8_0.target.row and arg_9_0.column == arg_8_0.target.column)
			local var_8_3 = arg_8_1.GetRawChapterCell(var_8_2.row, var_8_2.column)
			local var_8_4 = var_8_3 and var_8_3.data or 0
			local var_8_5 = "-" .. (var_8_2.data - var_8_4) / 100 .. "%"
			local var_8_6 = var_8_1.getShips(False)[1]

			arg_8_2.viewComponent.doPlayStrikeAnim(var_8_6, var_8_6.GetMapStrikeAnim(), function()
				arg_8_2.viewComponent.strikeEnemy(arg_8_0.target, var_8_5, arg_8_3))
		elif #arg_8_0.movePath > 0:
			arg_8_2.viewComponent.grid.moveSub(var_8_0, arg_8_0.movePath, None, arg_8_3)
		else
			arg_8_3()

return var_0_0
