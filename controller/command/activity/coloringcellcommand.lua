local var_0_0 = class("ColoringCellCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.activityId
	local var_1_2 = var_1_0.id
	local var_1_3 = var_1_0.cells

	pg.ConnectionMgr.GetInstance():Send(26004, {
		act_id = var_1_1,
		id = var_1_2,
		cell_list = var_1_3
	}, 26005, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(ColoringProxy)
			local var_2_1 = var_2_0:getColorItems()
			local var_2_2 = var_2_0:getColorGroup(var_1_2)
			local var_2_3 = var_2_2:getConfig("color_id_list")

			_.each(var_1_3, function(arg_3_0)
				var_2_2:setFill(arg_3_0.row, arg_3_0.column, arg_3_0.color)

				if not var_2_2:canBeCustomised() and arg_3_0.color > 0 then
					local var_3_0 = var_2_3[arg_3_0.color]

					var_2_1[var_3_0] = math.max(var_2_1[var_3_0] - 1, 0)
				end
			end)

			local var_2_4 = var_2_0:checkState()

			arg_1_0:sendNotification(GAME.COLORING_CELL_DONE, {
				cells = var_1_3,
				stateChange = var_2_4
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("coloring_cell", arg_2_0.result))
		end
	end)
end

return var_0_0
