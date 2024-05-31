﻿local var_0_0 = class("SaveDormThemeCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(DormProxy):getRawData()
	local var_1_2 = var_1_1.level
	local var_1_3, var_1_4 = CourtYardRawDataChecker.Check(var_1_0.furnitureputList, var_1_1:GetMapSize())

	if not var_1_3 then
		pg.TipsMgr.GetInstance():ShowTips(var_1_4)

		return
	end

	local var_1_5 = {}

	for iter_1_0, iter_1_1 in pairs(var_1_0.furnitureputList) do
		local var_1_6 = {}

		for iter_1_2, iter_1_3 in pairs(iter_1_1.child) do
			table.insert(var_1_6, {
				id = tostring(iter_1_2),
				x = iter_1_3.x,
				y = iter_1_3.y
			})
		end

		table.insert(var_1_5, {
			shipId = 0,
			id = tostring(iter_1_1.configId),
			x = iter_1_1.x,
			y = iter_1_1.y,
			dir = iter_1_1.dir,
			child = var_1_6,
			parent = iter_1_1.parent
		})
	end

	local var_1_7 = {
		id = var_1_0.id,
		name = var_1_0.name,
		furniture_put_list = var_1_5
	}

	pg.ConnectionMgr.GetInstance():Send(19020, var_1_7, 19021, function(arg_2_0)
		if arg_2_0.result == 0 then
			getProxy(DormProxy):AddTheme(var_1_7)
			arg_1_0:sendNotification(GAME.SAVE_DORMTHEME_DONE)
			pg.TipsMgr:GetInstance().ShowTips("Saved")
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
