local var_0_0 = class("EquipCodeImpeachCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.shareId
	local var_1_3 = var_1_0.type

	pg.ConnectionMgr.GetInstance().Send(17607, {
		shipgroup = var_1_1,
		shareid = var_1_2,
		report_type = var_1_3
	}, 17608, function(arg_2_0)
		if arg_2_0.result == 0:
			pg.m02.sendNotification(GAME.EQUIP_CODE_IMPEACH_DONE)
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_dislike_success"))
		elif arg_2_0.result == -1:
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_report_warning"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
