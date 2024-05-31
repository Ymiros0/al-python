local var_0_0 = class("PathFinding")

PathFinding = var_0_0
var_0_0.PrioNormal = 1
var_0_0.PrioObstacle = 1000
var_0_0.PrioForbidden = 1000000

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.cells = arg_1_1
	arg_1_0.rows = arg_1_2
	arg_1_0.columns = arg_1_3

def var_0_0.Find(arg_2_0, arg_2_1, arg_2_2):
	arg_2_1 = {
		row = arg_2_1.row,
		column = arg_2_1.column
	}
	arg_2_2 = {
		row = arg_2_2.row,
		column = arg_2_2.column
	}

	if arg_2_0.cells[arg_2_1.row][arg_2_1.column] < 0 or arg_2_0.cells[arg_2_2.row][arg_2_2.column] < 0:
		return 0, {}
	else
		return arg_2_0._Find(arg_2_1, arg_2_2)

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

def var_0_0._Find(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = var_0_0.PrioForbidden
	local var_3_1 = {}
	local var_3_2 = {
		arg_3_1
	}
	local var_3_3 = {}
	local var_3_4 = {
		[arg_3_1.row] = {
			[arg_3_1.column] = {
				priority = 0,
				path = {}
			}
		}
	}

	while #var_3_2 > 0:
		local var_3_5 = table.remove(var_3_2, 1)

		if var_3_5.row == arg_3_2.row and var_3_5.column == arg_3_2.column:
			local var_3_6 = var_3_4[var_3_5.row][var_3_5.column]

			var_3_0 = var_3_6.priority
			var_3_1 = var_3_6.path

			break

		table.insert(var_3_3, var_3_5)
		_.each(var_0_1, function(arg_4_0)
			local var_4_0 = {
				row = var_3_5.row + arg_4_0[1],
				column = var_3_5.column + arg_4_0[2]
			}

			if not (_.any(var_3_2, function(arg_5_0)
				return arg_5_0.row == var_4_0.row and arg_5_0.column == var_4_0.column) or _.any(var_3_3, function(arg_6_0)
				return arg_6_0.row == var_4_0.row and arg_6_0.column == var_4_0.column)) and var_4_0.row >= 0 and var_4_0.row < arg_3_0.rows and var_4_0.column >= 0 and var_4_0.column < arg_3_0.columns:
				local var_4_1 = var_3_4[var_3_5.row][var_3_5.column]
				local var_4_2 = var_4_1.priority + arg_3_0.cells[var_4_0.row][var_4_0.column]

				if var_4_2 < var_0_0.PrioObstacle:
					local var_4_3 = Clone(var_4_1)

					table.insert(var_4_3.path, var_4_0)

					var_4_3.priority = var_4_2
					var_3_4[var_4_0.row] = var_3_4[var_4_0.row] or {}
					var_3_4[var_4_0.row][var_4_0.column] = var_4_3

					local var_4_4 = 0

					for iter_4_0 = #var_3_2, 1, -1:
						local var_4_5 = var_3_2[iter_4_0]
						local var_4_6 = var_3_4[var_4_5.row][var_4_5.column]

						if var_4_3.priority >= var_4_6.priority:
							var_4_4 = iter_4_0

							break

					table.insert(var_3_2, var_4_4 + 1, var_4_0)
				else
					var_3_0 = math.min(var_3_0, var_4_2))

	if var_3_0 >= var_0_0.PrioObstacle:
		local var_3_7 = 1000000
		local var_3_8 = var_0_0.PrioForbidden

		for iter_3_0, iter_3_1 in pairs(var_3_4):
			for iter_3_2, iter_3_3 in pairs(iter_3_1):
				local var_3_9 = math.abs(arg_3_2.row - iter_3_0) + math.abs(arg_3_2.column - iter_3_2)

				if var_3_9 < var_3_7 or var_3_9 == var_3_7 and var_3_8 > iter_3_3.priority:
					var_3_7 = var_3_9
					var_3_8 = iter_3_3.priority
					var_3_1 = iter_3_3.path

	return var_3_0, var_3_1

return var_0_0
