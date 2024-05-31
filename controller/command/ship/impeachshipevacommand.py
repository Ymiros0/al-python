local var_0_0 = class("ImpeachShipEvaCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.evaId
	local var_1_3 = var_1_0.reason

	pg.ConnectionMgr.GetInstance().Send(17109, {
		ship_group_id = var_1_1,
		discuss_id = var_1_2,
		reason = var_1_3
	}, 17110, function(arg_2_0)
		if arg_2_0.result == 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("report_sent_thank")))

return var_0_0
