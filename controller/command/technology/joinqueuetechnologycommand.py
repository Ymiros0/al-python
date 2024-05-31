local var_0_0 = class("JoinQueueTechnologyCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.pool_id
	local var_1_3 = getProxy(TechnologyProxy)

	if #var_1_3.queue >= TechnologyConst.QUEUE_TOTAL_COUNT:
		return

	local var_1_4 = var_1_3.getTechnologyById(var_1_1)

	if not var_1_4 or not var_1_4.isActivate() or not var_1_4.finishCondition() or var_1_4.isCompleted():
		return

	pg.ConnectionMgr.GetInstance().Send(63013, {
		tech_id = var_1_1,
		refresh_id = var_1_2
	}, 63014, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_3.moveTechnologyToQueue(var_1_1)
			var_1_3.updateTechnologys(arg_2_0.refresh_list)
			arg_1_0.sendNotification(GAME.JOIN_QUEUE_TECHNOLOGY_DONE)
			pg.TipsMgr.GetInstance().ShowTips(i18n("technology_queue_in_success"))
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("blueprint_stop_erro") .. arg_2_0.result))

return var_0_0
