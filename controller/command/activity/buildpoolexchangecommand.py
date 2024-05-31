local var_0_0 = class("BuildPoolExchangeCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().activity_id
	local var_1_1 = getProxy(ActivityProxy).getActivityById(var_1_0)

	if not var_1_1 or var_1_1.isEnd():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		arg1 = 0,
		arg2 = 0,
		cmd = 2,
		activity_id = var_1_0,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_1.data2 = var_1_1.data2 + 1

			getProxy(ActivityProxy).updateActivity(var_1_1)

			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)

			arg_1_0.sendNotification(GAME.ACTIVITY_BUILD_POOL_EXCHANGE_DONE, {
				awards = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
