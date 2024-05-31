local var_0_0 = class("OrientedWeightPathFinding", OrientedPathFinding)

OrientedWeightPathFinding = var_0_0

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

local function var_0_2(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)
	local var_1_0 = var_0_0.PrioForbidden
	local var_1_1 = {}
	local var_1_2 = {
		arg_1_3
	}
	local var_1_3 = {}
	local var_1_4 = {
		[arg_1_3.row] = {
			[arg_1_3.column] = {
				enemyCount = 0,
				priority = 0,
				path = {}
			}
		}
	}

	while #var_1_2 > 0:
		local var_1_5 = table.remove(var_1_2, 1)

		if var_1_5.row == arg_1_4.row and var_1_5.column == arg_1_4.column:
			local var_1_6 = var_1_4[var_1_5.row][var_1_5.column]

			var_1_0 = var_1_6.priority
			var_1_1 = var_1_6.path

			break

		table.insert(var_1_3, var_1_5)
		_.each(var_0_1, function(arg_2_0)
			local var_2_0 = {
				row = var_1_5.row + arg_2_0[1],
				column = var_1_5.column + arg_2_0[2]
			}

			if not _.any(var_1_3, function(arg_3_0)
				return arg_3_0.row == var_2_0.row and arg_3_0.column == var_2_0.column) and var_2_0.row >= 0 and var_2_0.row < arg_1_1 and var_2_0.column >= 0 and var_2_0.column < arg_1_2 and not var_0_0.IsDirectionForbidden(arg_1_0[var_1_5.row][var_1_5.column], arg_2_0[1], arg_2_0[2]):
				local var_2_1 = var_1_4[var_1_5.row][var_1_5.column]
				local var_2_2 = arg_1_0[var_2_0.row][var_2_0.column]
				local var_2_3 = var_2_1.priority + var_2_2.priority
				local var_2_4 = var_2_1.enemyCount + (var_2_2.isEnemy and 1 or 0)

				if var_2_3 < var_0_0.PrioObstacle:
					local var_2_5 = Clone(var_2_1)

					table.insert(var_2_5.path, var_2_0)

					var_2_5.priority = var_2_3
					var_2_5.enemyCount = var_2_1.enemyCount + var_2_4

					local var_2_6 = _.detect(var_1_2, function(arg_4_0)
						return arg_4_0.row == var_2_0.row and arg_4_0.column == var_2_0.column)
					local var_2_7 = not var_2_6

					if var_2_6:
						local var_2_8 = var_1_4[var_2_0.row][var_2_0.column]

						var_2_7 = var_2_8.enemyCount > var_2_5.enemyCount or var_2_8.enemyCount == var_2_5.enemyCount and var_2_8.priority > var_2_5.priority

						if var_2_7:
							table.removebyvalue(var_1_2, var_2_6)

					if var_2_7:
						var_1_4[var_2_0.row] = var_1_4[var_2_0.row] or {}
						var_1_4[var_2_0.row][var_2_0.column] = var_2_5

						local var_2_9 = 0

						for iter_2_0 = #var_1_2, 1, -1:
							local var_2_10 = var_1_2[iter_2_0]
							local var_2_11 = var_1_4[var_2_10.row][var_2_10.column]

							if var_2_5.enemyCount > var_2_11.enemyCount or var_2_5.enemyCount == var_2_11.enemyCount and var_2_5.priority >= var_2_11.priority:
								var_2_9 = iter_2_0

								break

						table.insert(var_1_2, var_2_9 + 1, var_2_0)
				else
					var_1_0 = math.min(var_1_0, var_2_3))

	if var_1_0 >= var_0_0.PrioObstacle:
		local var_1_7 = 1000000
		local var_1_8 = var_0_0.PrioForbidden

		for iter_1_0, iter_1_1 in pairs(var_1_4):
			for iter_1_2, iter_1_3 in pairs(iter_1_1):
				local var_1_9 = math.abs(arg_1_4.row - iter_1_0) + math.abs(arg_1_4.column - iter_1_2)

				if var_1_9 < var_1_7 or var_1_9 == var_1_7 and var_1_8 > iter_1_3.priority:
					var_1_7 = var_1_9
					var_1_8 = iter_1_3.priority
					var_1_1 = iter_1_3.path

	return var_1_0, var_1_1

def var_0_0.StaticFind(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
	arg_5_3 = {
		row = arg_5_3.row,
		column = arg_5_3.column
	}
	arg_5_4 = {
		row = arg_5_4.row,
		column = arg_5_4.column
	}

	if arg_5_0[arg_5_3.row][arg_5_3.column].priority < 0 or arg_5_0[arg_5_4.row][arg_5_4.column].priority < 0:
		return 0, {}
	else
		return var_0_2(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4)

return var_0_0
