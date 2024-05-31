local var_0_0 = class("ActivityWorldInPictureCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_WORLDINPICTURE)

	if not var_1_1 or var_1_1.isEnd():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		activity_id = var_1_1.id,
		cmd = var_1_0.cmd,
		arg1 = var_1_0.cmd == ActivityConst.WORLDINPICTURE_OP_DRAW and var_1_0.index or var_1_0.arg1,
		arg2 = var_1_0.arg2,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)

			if var_1_0.cmd == ActivityConst.WORLDINPICTURE_OP_TURN:
				var_1_1.data2 = var_1_1.data2 - 1

				table.insert(var_1_1.data1_list, var_1_0.index)
			elif var_1_0.cmd == ActivityConst.WORLDINPICTURE_OP_DRAW:
				var_1_1.data3 = var_1_1.data3 - 1

				table.insert(var_1_1.data2_list, var_1_0.index)

			getProxy(ActivityProxy).updateActivity(var_1_1)
			arg_1_0.sendNotification(GAME.WORLDIN_PICTURE_OP_DONE, {
				activity = var_1_1,
				cmd = var_1_0.cmd,
				arg1 = var_1_0.arg1,
				arg2 = var_1_0.arg2,
				auto = var_1_0.auto,
				awards = var_2_0
			})
		else
			if arg_2_0.result == 3 or arg_2_0.result == 4:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("activity_op_error", arg_2_0.result))

			arg_1_0.sendNotification(GAME.WORLDIN_PICTURE_OP_ERRO, {
				cmd = var_1_0.cmd,
				auto = var_1_0.auto
			}))

return var_0_0
