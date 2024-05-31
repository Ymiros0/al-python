local var_0_0 = class("ChangeRandomFlagShipsCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.addList
	local var_1_2 = var_1_0.deleteList
	local var_1_3 = 300
	local var_1_4 = math.max(#var_1_2, #var_1_1)
	local var_1_5 = math.ceil(var_1_4 / var_1_3)
	local var_1_6 = {}

	for iter_1_0 = 1, var_1_5:
		local var_1_7 = {}
		local var_1_8 = {}
		local var_1_9 = (iter_1_0 - 1) * var_1_3 + 1

		for iter_1_1 = var_1_9, var_1_9 + var_1_3 - 1:
			if iter_1_1 <= #var_1_1:
				table.insert(var_1_7, var_1_1[iter_1_1])

			if iter_1_1 <= #var_1_2:
				table.insert(var_1_8, var_1_2[iter_1_1])

		table.insert(var_1_6, function(arg_2_0)
			arg_1_0.Send(var_1_7, var_1_8, arg_2_0))

	seriesAsync(var_1_6, function()
		if #var_1_1 > 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("random_ship_custom_mode_add_complete"))

		if #var_1_2 > 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("random_ship_custom_mode_remove_complete"))

		arg_1_0.sendNotification(GAME.CHANGE_RANDOM_SHIPS_DONE))

def var_0_0.Send(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	pg.ConnectionMgr.GetInstance().Send(12208, {
		add_list = arg_4_1,
		del_list = arg_4_2
	}, 12209, function(arg_5_0)
		if arg_5_0.result == 0:
			local var_5_0 = getProxy(PlayerProxy).getRawData()
			local var_5_1 = var_5_0.GetCustomRandomShipList()
			local var_5_2 = {}

			for iter_5_0, iter_5_1 in ipairs(arg_4_2):
				var_5_2[iter_5_1] = True

			for iter_5_2 = #var_5_1, 1, -1:
				if var_5_2[var_5_1[iter_5_2]]:
					table.remove(var_5_1, iter_5_2)

			for iter_5_3, iter_5_4 in ipairs(arg_4_1):
				if not table.contains(var_5_1, iter_5_4):
					table.insert(var_5_1, iter_5_4)

			var_5_0.UpdateCustomRandomShipList(var_5_1)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_5_0.result] .. arg_5_0.result)

		if arg_4_3:
			arg_4_3())

return var_0_0
