local var_0_0 = class("ActivityLinerOPCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.callback
	local var_1_2 = getProxy(ActivityProxy)
	local var_1_3 = var_1_2.getActivityById(var_1_0.activity_id)

	if not var_1_3 or var_1_3.isEnd():
		return

	local var_1_4 = var_1_0.drop

	if var_1_4:
		local var_1_5 = getProxy(PlayerProxy).getData()

		if var_1_4.type == DROP_TYPE_RESOURCE and var_1_4.id == 1 and var_1_5.GoldMax(var_1_4.count):
			pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title"))

			return

		if var_1_4.type == DROP_TYPE_RESOURCE and var_1_4.id == 2 and var_1_5.OilMax(var_1_4.count):
			pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title"))

			return

		if var_1_4.type == DROP_TYPE_ITEM:
			local var_1_6 = Item.getConfigData(var_1_4.id)

			if var_1_6.type == Item.EXP_BOOK_TYPE and getProxy(BagProxy).getItemCountById(var_1_4.id) + var_1_4.count > var_1_6.max_num:
				pg.TipsMgr.GetInstance().ShowTips(i18n("expbook_max_tip_title"))

				return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		activity_id = var_1_0.activity_id,
		cmd = var_1_0.cmd or 0,
		arg1 = var_1_0.arg1 or 0,
		arg2 = var_1_0.arg2 or 0,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = {}
			local var_2_1 = PlayerConst.addTranDrop(arg_2_0.award_list)

			if var_1_0.cmd == 1:
				local var_2_2 = var_1_3.GetCurTime()

				switch(var_2_2.GetType(), {
					[LinerTime.TYPE.TARGET] = function()
						return,
					[LinerTime.TYPE.EXPLORE] = function()
						var_1_3.AddExploredRoom(var_1_0.arg1),
					[LinerTime.TYPE.EVENT] = function()
						var_1_3.AddEvent(var_1_0.arg1, var_1_0.arg2),
					[LinerTime.TYPE.STORY] = function()
						return
				})

				if var_1_3.CheckTimeFinish():
					var_1_3.UpdateTimeIdx()
					var_1_3.UpdateRoomIdx(True)

				if var_1_3.CheckRoomFinish():
					var_1_3.UpdateRoomIdx(False)
			elif var_1_0.cmd == 2:
				var_1_3.AddTimeAwardFlag(var_1_0.arg1)
			elif var_1_0.cmd == 3:
				var_1_3.AddRoomAwardFlag(var_1_0.arg1)
			elif var_1_0.cmd == 4:
				var_1_3.AddEventAwardFlag(var_1_0.arg1, var_1_0.arg2)

			var_1_2.updateActivity(var_1_3)

			if var_1_1:
				var_1_1()

			arg_1_0.sendNotification(GAME.ACTIVITY_LINER_OP_DONE, {
				awards = var_2_1
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
