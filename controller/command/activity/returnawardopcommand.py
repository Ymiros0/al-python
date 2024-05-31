local var_0_0 = class("ReturnAwardOPCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(ActivityProxy)
	local var_1_2 = var_1_1.getActivityById(var_1_0.activity_id)

	if not var_1_2 or var_1_2.isEnd():
		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		activity_id = var_1_0.activity_id,
		cmd = var_1_0.cmd or 0,
		arg1 = var_1_0.arg1 or 0,
		arg2 = var_1_0.arg2 or 0,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)

			if var_1_0.cmd == ActivityConst.RETURN_AWARD_OP_ACTIVTION:
				var_1_2.data1 = 1
			elif var_1_0.cmd == ActivityConst.RETURN_AWARD_OP_GET_RETRUNERS:
				local var_2_1 = {}

				for iter_2_0, iter_2_1 in ipairs(arg_2_0.return_user_list):
					table.insert(var_2_1, Returner.New(iter_2_1))

				var_1_2.setClientList(var_2_1)
			elif var_1_0.cmd == ActivityConst.RETURN_AWARD_OP_GET_AWARD:
				table.insert(var_1_2.data1_list, var_1_0.arg1)
			elif var_1_0.cmd == ActivityConst.RETURN_AWARD_OP_PUSH_UID:
				var_1_2.data2_list[1] = 1

				pg.TipsMgr.GetInstance().ShowTips(i18n("returner_push_success"))
			elif var_1_0.cmd == ActivityConst.RETURN_AWARD_OP_ACCEPT_TASK:
				-- block empty
			elif var_1_0.cmd == ActivityConst.RETURN_AWARD_OP_SET_RETRUNER:
				var_1_2.data2 = var_1_0.arg1

				pg.TipsMgr.GetInstance().ShowTips(i18n("return_award_bind_success"))
			elif var_1_0.cmd == ActivityConst.RETURN_AWARD_OP_RETURNER_GET_AWARD:
				local var_2_2 = pg.activity_template_returnner[var_1_2.id].task_list

				var_1_2.data4 = math.min(var_1_2.data4 + 1, #var_2_2)
			elif var_1_0.cmd == ActivityConst.RETURN_AWARD_OP_MATCH:
				var_1_2.data2 = arg_2_0.number[1]

				pg.TipsMgr.GetInstance().ShowTips(i18n("return_award_bind_success"))

			var_1_1.updateActivity(var_1_2)
			arg_1_0.sendNotification(GAME.RETURN_AWARD_OP_DONE, {
				awards = var_2_0,
				id = var_1_2.id,
				cmd = var_1_0.cmd
			})
		elif ERROR_MESSAGE[arg_2_0.result]:
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result])
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[9999] .. arg_2_0.result))

return var_0_0
