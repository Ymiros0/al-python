local var_0_0 = class("SculptureActivityOpCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.state
	local var_1_3 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SCULPTURE)

	if not var_1_3 or var_1_3.isEnd():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	local var_1_4 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

	if not var_1_4 or var_1_4.isEnd():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	if not var_1_3.CanEnterState(var_1_1, var_1_2):
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_error"))

		return

	if var_1_2 == SculptureActivity.STATE_UNLOCK:
		local var_1_5, var_1_6 = var_1_3._GetComsume(var_1_1)

		if var_1_6 > var_1_4.getVitemNumber(var_1_5):
			local var_1_7 = pg.activity_workbench_item[var_1_5].name

			pg.TipsMgr.GetInstance().ShowTips(i18n("gift_act_tips", var_1_7))

			return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		cmd = 1,
		activity_id = var_1_3.id,
		arg1 = var_1_1,
		arg2 = var_1_2,
		arg_list = {},
		arg_list2 = {},
		kvargs1 = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)

			if var_1_2 == SculptureActivity.STATE_UNLOCK:
				local var_2_1, var_2_2 = var_1_3._GetComsume(var_1_1)
				local var_2_3 = var_1_4.getVitemNumber(var_2_1)

				var_1_4.addVitemNumber(var_2_1, 0 - var_2_2)
				getProxy(ActivityProxy).updateActivity(var_1_4)

			var_1_3.UpdateState(var_1_1, var_1_2)
			getProxy(ActivityProxy).updateActivity(var_1_3)
			arg_1_0.sendNotification(GAME.SCULPTURE_ACT_OP_DONE, {
				state = var_1_2,
				activity = var_1_3,
				id = var_1_1,
				awards = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
