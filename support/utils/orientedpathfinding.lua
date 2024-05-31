local var_0_0 = class("OrientedPathFinding", PathFinding)

OrientedPathFinding = var_0_0

function var_0_0.Find(arg_1_0, arg_1_1, arg_1_2)
	arg_1_1 = {
		row = arg_1_1.row,
		column = arg_1_1.column
	}
	arg_1_2 = {
		row = arg_1_2.row,
		column = arg_1_2.column
	}

	if arg_1_0.cells[arg_1_1.row][arg_1_1.column].priority < 0 or arg_1_0.cells[arg_1_2.row][arg_1_2.column].priority < 0 then
		return 0, {}
	else
		return arg_1_0:_Find(arg_1_1, arg_1_2)
	end
end

local var_0_1 = {
	{
		1,
		0
	},
	{
		-1,
		0
	},
	{
		0,
		1
	},
	{
		0,
		-1
	}
}

function var_0_0._Find(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = var_0_0.PrioForbidden
	local var_2_1 = {}
	local var_2_2 = {
		arg_2_1
	}
	local var_2_3 = {}
	local var_2_4 = {
		[arg_2_1.row] = {
			[arg_2_1.column] = {
				priority = 0,
				path = {}
			}
		}
	}

	while #var_2_2 > 0 do
		local var_2_5 = table.remove(var_2_2, 1)

		if var_2_5.row == arg_2_2.row and var_2_5.column == arg_2_2.column then
			local var_2_6 = var_2_4[var_2_5.row][var_2_5.column]

			var_2_0 = var_2_6.priority
			var_2_1 = var_2_6.path

			break
		end

		table.insert(var_2_3, var_2_5)
		_.each(var_0_1, function(arg_3_0)
			local var_3_0 = {
				row = var_2_5.row + arg_3_0[1],
				column = var_2_5.column + arg_3_0[2]
			}

			if not (_.any(var_2_2, function(arg_4_0)
				return arg_4_0.row == var_3_0.row and arg_4_0.column == var_3_0.column
			end) or _.any(var_2_3, function(arg_5_0)
				return arg_5_0.row == var_3_0.row and arg_5_0.column == var_3_0.column
			end)) and var_3_0.row >= 0 and var_3_0.row < arg_2_0.rows and var_3_0.column >= 0 and var_3_0.column < arg_2_0.columns and not var_0_0.IsDirectionForbidden(arg_2_0.cells[var_2_5.row][var_2_5.column], arg_3_0[1], arg_3_0[2]) then
				local var_3_1 = var_2_4[var_2_5.row][var_2_5.column]
				local var_3_2 = var_3_1.priority + arg_2_0.cells[var_3_0.row][var_3_0.column].priority

				if var_3_2 < var_0_0.PrioObstacle then
					local var_3_3 = Clone(var_3_1)

					table.insert(var_3_3.path, var_3_0)

					var_3_3.priority = var_3_2
					var_2_4[var_3_0.row] = var_2_4[var_3_0.row] or {}
					var_2_4[var_3_0.row][var_3_0.column] = var_3_3

					local var_3_4 = 0

					for iter_3_0 = #var_2_2, 1, -1 do
						local var_3_5 = var_2_2[iter_3_0]
						local var_3_6 = var_2_4[var_3_5.row][var_3_5.column]

						if var_3_3.priority >= var_3_6.priority then
							var_3_4 = iter_3_0

							break
						end
					end

					table.insert(var_2_2, var_3_4 + 1, var_3_0)
				else
					var_2_0 = math.min(var_2_0, var_3_2)
				end
			end
		end)
	end

	if var_2_0 >= var_0_0.PrioObstacle then
		local var_2_7 = 1000000
		local var_2_8 = var_0_0.PrioForbidden

		for iter_2_0, iter_2_1 in pairs(var_2_4) do
			for iter_2_2, iter_2_3 in pairs(iter_2_1) do
				local var_2_9 = math.abs(arg_2_2.row - iter_2_0) + math.abs(arg_2_2.column - iter_2_2)

				if var_2_9 < var_2_7 or var_2_9 == var_2_7 and var_2_8 > iter_2_3.priority then
					var_2_7 = var_2_9
					var_2_8 = iter_2_3.priority
					var_2_1 = iter_2_3.path
				end
			end
		end
	end

	return var_2_0, var_2_1
end

function var_0_0.IsDirectionForbidden(arg_6_0, arg_6_1, arg_6_2)
	if arg_6_0.forbiddens == ChapterConst.ForbiddenNone then
		return
	end

	local var_6_0

	if arg_6_1 ~= 0 then
		var_6_0 = arg_6_1 < 0 and ChapterConst.ForbiddenUp or ChapterConst.ForbiddenDown
	else
		var_6_0 = arg_6_2 < 0 and ChapterConst.ForbiddenLeft or ChapterConst.ForbiddenRight
	end

	return bit.band(var_6_0, arg_6_0.forbiddens) > 0
end

return var_0_0
