﻿local var_0_0 = class("CourtYardWallGridAgent", import(".CourtYardGridAgent"))

function var_0_0.Reset(arg_1_0, arg_1_1)
	table.clear(arg_1_0.grids)

	for iter_1_0 = 1, #arg_1_1 do
		if iter_1_0 % 2 == 0 then
			local var_1_0 = arg_1_0:GetPool():Dequeue()

			var_1_0.transform:SetParent(arg_1_0.gridsTF)

			var_1_0.transform.localScale = Vector3.one

			table.insert(arg_1_0.grids, var_1_0)
			arg_1_0:UpdatePositionAndColor(var_1_0, {
				arg_1_1[iter_1_0 - 1],
				arg_1_1[iter_1_0]
			})
		end
	end
end

function var_0_0.Flush(arg_2_0, arg_2_1)
	for iter_2_0 = 1, #arg_2_1 do
		if iter_2_0 % 2 == 0 then
			local var_2_0 = arg_2_0.grids[iter_2_0 * 0.5]

			assert(var_2_0)
			arg_2_0:UpdatePositionAndColor(var_2_0, {
				arg_2_1[iter_2_0 - 1],
				arg_2_1[iter_2_0]
			})
		end
	end
end

function var_0_0.UpdatePositionAndColor(arg_3_0, arg_3_1, arg_3_2)
	table.sort(arg_3_2, function(arg_4_0, arg_4_1)
		return arg_4_0.position.x + arg_4_0.position.y < arg_4_1.position.x + arg_4_1.position.y
	end)

	local var_3_0 = arg_3_2[1]
	local var_3_1 = CourtYardCalcUtil.Map2Local(var_3_0.position)

	arg_3_1.transform.localPosition = var_3_1

	local var_3_2 = _.all(arg_3_2, function(arg_5_0)
		return arg_5_0.flag == 1
	end)
	local var_3_3 = arg_3_0:GetColor(var_3_2 and 1 or 2)

	arg_3_1:GetComponent(typeof(Image)).color = var_3_3

	local var_3_4 = var_3_0.position.y - var_3_0.position.x >= 1

	arg_3_1.transform.localScale = var_3_4 and Vector3(-1, 1, 1) or Vector3(1, 1, 1)
end

function var_0_0.GetPool(arg_6_0)
	return arg_6_0:GetView().poolMgr:GetWallGridPool()
end

return var_0_0
