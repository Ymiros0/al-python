local var_0_0 = class("UseTecSpeedUpItemCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.blueprintid
	local var_1_2 = var_1_0.itemid
	local var_1_3 = var_1_0.number
	local var_1_4 = var_1_0.taskID

	pg.ConnectionMgr.GetInstance().Send(63210, {
		blueprintid = var_1_1,
		itemid = var_1_2,
		number = var_1_3,
		task_id = var_1_4
	}, 63211, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(BagProxy).removeItemById(var_1_2, var_1_3)
			arg_1_0.sendNotification(GAME.USE_TEC_SPEEDUP_ITEM_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips("Error Code" .. arg_2_0.result))

return var_0_0
