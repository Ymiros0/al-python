local var_0_0 = class("WorldSubmitTaskCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().taskId
	local var_1_1 = nowWorld()
	local var_1_2 = var_1_1.GetInventoryProxy()
	local var_1_3 = var_1_1.GetTaskProxy()
	local var_1_4 = var_1_3.getTaskById(var_1_0)

	if not var_1_4:
		return

	local var_1_5 = {}

	table.insert(var_1_5, function(arg_2_0)
		local var_2_0, var_2_1 = var_1_4.canSubmit()

		if var_2_0:
			arg_2_0()
		else
			pg.TipsMgr.GetInstance().ShowTips(var_2_1))

	local var_1_6 = var_1_4.config.complete_condition == WorldConst.TaskTypeSubmitItem and var_1_4.config.item_retrieve == 1

	if not var_1_4.IsAutoSubmit() and var_1_6:
		table.insert(var_1_5, function(arg_3_0)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_ITEM_BOX,
				content = i18n("sub_item_warning"),
				items = {
					{
						type = DROP_TYPE_WORLD_ITEM,
						id = var_1_4.config.complete_parameter[1],
						count = var_1_4.getMaxProgress()
					}
				},
				onYes = arg_3_0
			}))

	seriesAsync(var_1_5, function()
		pg.ConnectionMgr.GetInstance().Send(33207, {
			taskId = var_1_0
		}, 33208, function(arg_5_0)
			if arg_5_0.result == 0:
				local function var_5_0(arg_6_0, arg_6_1, arg_6_2)
					local var_6_0 = getProxy(BayProxy)
					local var_6_1 = {}
					local var_6_2 = {}
					local var_6_3 = arg_6_0.GetShipVOs()

					for iter_6_0, iter_6_1 in ipairs(var_6_3):
						table.insert(var_6_1, iter_6_1)

						local var_6_4 = var_6_0.getShipById(iter_6_1.id)

						var_6_4.setIntimacy(var_6_4.getIntimacy() + arg_6_2)
						var_6_4.addExp(arg_6_1)
						var_6_0.updateShip(var_6_4)

						local var_6_5 = WorldConst.FetchShipVO(iter_6_1.id)

						table.insert(var_6_2, var_6_5)

					return {
						oldships = var_6_1,
						newships = var_6_2
					}

				local var_5_1 = {}
				local var_5_2 = arg_5_0.exp
				local var_5_3 = arg_5_0.intimacy
				local var_5_4 = var_1_1.GetFleets()

				for iter_5_0, iter_5_1 in pairs(var_5_4):
					local var_5_5 = var_5_0(iter_5_1, var_5_2, var_5_3)

					if var_5_2 > 0:
						table.insert(var_5_1, var_5_5)

				local var_5_6 = PlayerConst.addTranDrop(arg_5_0.drops)

				var_1_4.commited()
				var_1_3.updateTask(var_1_4)
				var_1_3.riseTaskFinishCount()
				var_1_1.UpdateProgress(var_1_4.config.complete_stage)

				if var_1_6:
					var_1_2.RemoveItem(var_1_4.config.complete_parameter[1], var_1_4.getMaxProgress())

				arg_1_0.sendNotification(GAME.WORLD_SUMBMIT_TASK_DONE, {
					task = var_1_4,
					drops = var_5_6,
					expfleets = var_5_1
				})
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("task_submitTask", arg_5_0.result))))

return var_0_0
