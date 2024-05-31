﻿local var_0_0 = class("ChapterCell", import(".LevelCellData"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.walkable = true
	arg_1_0.forbiddenDirections = ChapterConst.ForbiddenNone
	arg_1_0.row = arg_1_1.pos.row
	arg_1_0.column = arg_1_1.pos.column
	arg_1_0.attachment = arg_1_1.item_type
	arg_1_0.attachmentId = arg_1_1.item_id
	arg_1_0.flag = arg_1_1.item_flag
	arg_1_0.data = arg_1_1.item_data
	arg_1_0.trait = ChapterConst.TraitNone
	arg_1_0.item = nil
	arg_1_0.itemOffset = nil
	arg_1_0.flagList = {}

	if arg_1_1.flag_list then
		for iter_1_0, iter_1_1 in ipairs(arg_1_1.flag_list) do
			table.insert(arg_1_0.flagList, iter_1_1)
		end
	end
end

function var_0_0.updateFlagList(arg_2_0, arg_2_1)
	arg_2_0.flagList = arg_2_0.flagList or {}

	table.clear(arg_2_0.flagList)

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.flag_list) do
		table.insert(arg_2_0.flagList, iter_2_1)
	end
end

function var_0_0.GetFlagList(arg_3_0)
	return arg_3_0.flagList
end

function var_0_0.GetWeatherFlagList(arg_4_0)
	return _.filter(arg_4_0:GetFlagList(), function(arg_5_0)
		return tobool(pg.weather_data_template[arg_5_0])
	end)
end

function var_0_0.checkHadFlag(arg_6_0, arg_6_1)
	return table.contains(arg_6_0.flagList, arg_6_1)
end

function var_0_0.Line2Name(arg_7_0, arg_7_1)
	return "chapter_cell_" .. arg_7_0 .. "_" .. arg_7_1
end

function var_0_0.Line2QuadName(arg_8_0, arg_8_1)
	return "chapter_cell_quad_" .. arg_8_0 .. "_" .. arg_8_1
end

function var_0_0.Line2MarkName(arg_9_0, arg_9_1, arg_9_2)
	return "chapter_cell_mark_" .. arg_9_0 .. "_" .. arg_9_1 .. "#" .. arg_9_2
end

function var_0_0.MinMaxLine2QuadName(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	return "chapter_cell_quad_" .. arg_10_0 .. "_" .. arg_10_1 .. "_" .. arg_10_2 .. "_" .. arg_10_3
end

function var_0_0.Line2RivalName(arg_11_0, arg_11_1, arg_11_2)
	return "rival_" .. arg_11_1 .. "_" .. arg_11_2
end

function var_0_0.LineAround(arg_12_0, arg_12_1, arg_12_2)
	local var_12_0 = {}

	for iter_12_0 = -arg_12_2, arg_12_2 do
		for iter_12_1 = -arg_12_2, arg_12_2 do
			if arg_12_2 >= math.abs(iter_12_0) + math.abs(iter_12_1) then
				table.insert(var_12_0, {
					row = arg_12_0 + iter_12_0,
					column = arg_12_1 + iter_12_1
				})
			end
		end
	end

	return var_12_0
end

function var_0_0.SetWalkable(arg_13_0, arg_13_1)
	arg_13_0.walkable = tobool(arg_13_1)

	if type(arg_13_1) == "boolean" then
		arg_13_0.forbiddenDirections = arg_13_1 and ChapterConst.ForbiddenNone or ChapterConst.ForbiddenAll
	elseif type(arg_13_1) == "number" then
		arg_13_0.forbiddenDirections = bit.band(arg_13_1, ChapterConst.ForbiddenAll)
	end
end

function var_0_0.IsWalkable(arg_14_0)
	return arg_14_0.walkable
end

return var_0_0
