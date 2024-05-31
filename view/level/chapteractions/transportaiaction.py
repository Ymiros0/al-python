local var_0_0 = class("TransportAIAction")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.line = {
		row = arg_1_1.ai_pos.row,
		column = arg_1_1.ai_pos.column
	}
	arg_1_0.movePath = _.map(arg_1_1.move_path, function(arg_2_0)
		return {
			row = arg_2_0.row,
			column = arg_2_0.column
		})

	local var_1_0 = _.detect(arg_1_1.map_update, function(arg_3_0)
		return arg_3_0.item_type == ChapterConst.AttachTransport)

	arg_1_0.hp = var_1_0 and var_1_0.item_data

def var_0_0.applyTo(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_1.getFleet(FleetType.Transport, arg_4_0.line.row, arg_4_0.line.column)

	if var_4_0:
		return arg_4_0.applyToFleet(arg_4_1, var_4_0, arg_4_2)

	return False, "can not find any transport at. [" .. arg_4_0.line.row .. ", " .. arg_4_0.line.column .. "]"

def var_0_0.applyToFleet(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	local var_5_0 = 0

	if not arg_5_2.isValid():
		return False, "fleet " .. arg_5_2.id .. " is invalid."

	local var_5_1 = 0

	if #arg_5_0.movePath > 0:
		if _.any(arg_5_0.movePath, function(arg_6_0)
			local var_6_0 = arg_5_1.getChapterCell(arg_6_0.row, arg_6_0.column)

			return not var_6_0 or not var_6_0.IsWalkable()):
			return False, "invalide move path"

		if not arg_5_3:
			local var_5_2 = arg_5_0.movePath[#arg_5_0.movePath]

			arg_5_2.line = {
				row = var_5_2.row,
				column = var_5_2.column
			}
			var_5_1 = bit.bor(var_5_1, ChapterConst.DirtyFleet, ChapterConst.DirtyAttachment, ChapterConst.DirtyChampionPosition)

	if arg_5_0.hp and not arg_5_3:
		arg_5_2.setRestHp(arg_5_0.hp)

		var_5_1 = bit.bor(var_5_1, ChapterConst.DirtyFleet)

		local var_5_3 = arg_5_1.getChapterCell(arg_5_2.line.row, arg_5_2.line.column)

		if var_5_3 and var_5_3.attachment == ChapterConst.AttachBox and var_5_3.flag != ChapterConst.CellFlagDisabled and pg.box_data_template[var_5_3.attachmentId].type == ChapterConst.BoxTorpedo:
			var_5_3.flag = ChapterConst.CellFlagDisabled

			arg_5_1.clearChapterCell(var_5_3.row, var_5_3.column)

			var_5_1 = bit.bor(var_5_1, ChapterConst.DirtyAttachment)

	return True, var_5_1

def var_0_0.PlayAIAction(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	local var_7_0 = arg_7_1.getFleetIndex(FleetType.Transport, arg_7_0.line.row, arg_7_0.line.column)

	if var_7_0:
		if #arg_7_0.movePath > 0:
			arg_7_2.viewComponent.grid.moveTransport(var_7_0, arg_7_0.movePath, Clone(arg_7_0.movePath), arg_7_3)
		else
			local var_7_1 = arg_7_1.fleets[var_7_0]
			local var_7_2 = arg_7_1.getChapterCell(var_7_1.line.row, var_7_1.line.column)

			if var_7_2 and var_7_2.attachment == ChapterConst.AttachBox and var_7_2.flag != ChapterConst.CellFlagDisabled and pg.box_data_template[var_7_2.attachmentId].type == ChapterConst.BoxTorpedo:
				arg_7_2.viewComponent.doPlayTorpedo(arg_7_3)

				return

			arg_7_3()

return var_0_0
