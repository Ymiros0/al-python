local var_0_0 = class("ActivityPuzzlePicecOPCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id or 0
	local var_1_2 = var_1_0.cmd
	local var_1_3 = var_1_0.actId
	local var_1_4 = var_1_0.callback
	local var_1_5 = getProxy(ActivityProxy)
	local var_1_6 = getProxy(ActivityProxy).getActivityById(var_1_3)

	if not var_1_6 or var_1_6.isEnd():
		return

	local var_1_7 = pg.activity_event_picturepuzzle[var_1_3]

	if not var_1_7:
		return

	if var_1_2 == 1:
		if #var_1_6.data2_list > #var_1_7.pickup_picturepuzzle + #var_1_7.drop_picturepuzzle:
			return

		if var_1_6.data1 != 0:
			return

		arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 1,
			activity_id = var_1_3
		})

		return
	elif var_1_2 == 2:
		if not var_1_0.isPickUp and not table.contains(var_1_6.data1_list, var_1_1):
			return

		if table.contains(var_1_6.data2_list, var_1_1):
			return
	elif var_1_2 == 3:
		if table.contains(var_1_6.data3_list, var_1_1):
			return

		if pg.TimeMgr.GetInstance().GetServerTime() < var_1_6.data2:
			pg.TipsMgr.GetInstance().ShowTips(i18n("bulin_tip_other2"))

			return
	elif var_1_2 == 4:
		if var_1_6.data1 != 1:
			return

		arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 4,
			activity_id = var_1_3
		})

		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		arg2 = 0,
		activity_id = var_1_3,
		cmd = var_1_2,
		arg1 = var_1_1,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_6 = getProxy(ActivityProxy).getActivityById(var_1_3)

			if var_1_2 == 1:
				var_1_6.data1 = 1
			elif var_1_2 == 2:
				table.insert(var_1_6.data2_list, var_1_1)
			elif var_1_2 == 3:
				table.insert(var_1_6.data3_list, var_1_1)

				var_1_6.data2 = pg.TimeMgr.GetInstance().GetServerTime() + var_1_7.cd
			elif var_1_2 == 4:
				var_1_6.data1 = 2

			var_1_5.updateActivity(var_1_6)

			if var_1_4:
				var_1_4()
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
