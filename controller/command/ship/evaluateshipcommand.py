local var_0_0 = class("EvaluateShipCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.content

	pg.ConnectionMgr.GetInstance().Send(17103, {
		ship_group_id = var_1_1,
		context = var_1_2
	}, 17104, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(CollectionProxy)
			local var_2_1 = var_2_0.getShipGroup(var_1_1)

			if var_2_1:
				var_2_1.evaluation = ShipEvaluation.New(arg_2_0.ship_discuss)

				var_2_0.updateShipGroup(var_2_1)
				arg_1_0.sendNotification(CollectionProxy.GROUP_EVALUATION_UPDATE, var_1_1)

			pg.TipsMgr.GetInstance().ShowTips(i18n("eva_ship_success"))
		elif arg_2_0.result == 1:
			pg.TipsMgr.GetInstance().ShowTips(i18n("report_ship_cannot_comment"))
		elif arg_2_0.result == 2011:
			pg.TipsMgr.GetInstance().ShowTips(i18n("evaluate_too_loog"))
		elif arg_2_0.result == 2013:
			pg.TipsMgr.GetInstance().ShowTips(i18n("evaluate_ban_word"))
		elif arg_2_0.result == 40:
			pg.TipsMgr.GetInstance().ShowTips(i18n("report_cannot_comment"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("eva_ship", arg_2_0.result)))

return var_0_0
