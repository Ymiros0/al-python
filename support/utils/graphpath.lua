local var_0_0 = class("GraphPath")

GraphPath = var_0_0

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.points = {}
	arg_1_0.edges = {}

	for iter_1_0, iter_1_1 in pairs(arg_1_1.Points) do
		local var_1_0 = {
			id = iter_1_0,
			nexts = {}
		}

		table.merge(var_1_0, iter_1_1)

		arg_1_0.points[iter_1_0] = setmetatable(var_1_0, Vector2)
	end

	for iter_1_2, iter_1_3 in pairs(arg_1_1.Edges) do
		local var_1_1 = arg_1_0.points[iter_1_3.p1]
		local var_1_2 = arg_1_0.points[iter_1_3.p2]

		if var_1_1 and var_1_2 and var_1_1 ~= var_1_2 then
			table.insert(var_1_1.nexts, iter_1_3.p2)
			table.insert(var_1_2.nexts, iter_1_3.p1)

			arg_1_0.edges[var_1_1] = arg_1_0.edges[var_1_1] or {}
			arg_1_0.edges[var_1_1][var_1_2] = iter_1_3
			arg_1_0.edges[var_1_2] = arg_1_0.edges[var_1_2] or {}
			arg_1_0.edges[var_1_2][var_1_1] = iter_1_3
		end
	end
end

function var_0_0.getRandomPoint(arg_2_0)
	local var_2_0 = _.values(arg_2_0.points)

	return var_2_0[math.random(1, #var_2_0)]
end

function var_0_0.getPoint(arg_3_0, arg_3_1)
	return arg_3_0.points[arg_3_1]
end

function var_0_0.getEdge(arg_4_0, arg_4_1, arg_4_2)
	return arg_4_0.edges[arg_4_1] and arg_4_0.edges[arg_4_1][arg_4_2]
end
