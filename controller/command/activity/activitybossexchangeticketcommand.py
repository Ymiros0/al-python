local var_0_0 = class("ActivityBossExchangeTicketCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().stageId

	if not var_1_0:
		return

	local var_1_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

	if not var_1_1 or var_1_1.isEnd():
		return

	local var_1_2 = pg.activity_event_worldboss[var_1_1.getConfig("config_id")]

	if not var_1_2:
		return

	local var_1_3 = getProxy(PlayerProxy).getRawData()
	local var_1_4 = var_1_2.ticket

	if var_1_3.getResource(var_1_4) <= 0:
		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		cmd = 1,
		activity_id = var_1_1.id,
		arg1 = var_1_0,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(PlayerProxy).getRawData().consume({
				[id2res(var_1_4)] = 1
			})
			arg_1_0.sendNotification(GAME.ACT_BOSS_NORMAL_UPDATE, {
				num = 1,
				stageId = var_1_0
			})
			arg_1_0.sendNotification(GAME.ACT_BOSS_EXCHANGE_TICKET_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
