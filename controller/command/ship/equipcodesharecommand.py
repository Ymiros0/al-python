local var_0_0 = class("EquipCodeShareCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.code

	pg.ConnectionMgr.GetInstance().Send(17603, {
		shipgroup = var_1_1,
		eqcode = var_1_2
	}, 17604, function(arg_2_0)
		if arg_2_0.result == 0:
			pg.m02.sendNotification(GAME.EQUIP_CODE_SHARE_DONE)
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_share_success"))
		elif arg_2_0.result == 7:
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_share_errorcode7"))
		elif arg_2_0.result == 44:
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_share_errorcode44"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
