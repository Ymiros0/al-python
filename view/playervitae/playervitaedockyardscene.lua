local var_0_0 = class("PlayerVitaeDockyardScene", import("view.ship.DockyardScene"))

function var_0_0.SortShips(arg_1_0, arg_1_1)
	local var_1_0 = getProxy(PlayerProxy):getRawData().characters
	local var_1_1 = {}
	local var_1_2 = #var_1_0 + 1

	for iter_1_0, iter_1_1 in ipairs(var_1_0) do
		var_1_1[iter_1_1] = var_1_2 - iter_1_0
	end

	table.insert(arg_1_1, function(arg_2_0)
		return -(var_1_1[arg_2_0.id] or 0)
	end)
	table.sort(arg_1_0.shipVOs, CompareFuncs(arg_1_1))
end

return var_0_0
