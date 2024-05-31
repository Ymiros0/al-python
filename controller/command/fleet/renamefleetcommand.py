local var_0_0 = class("FleetRenameCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.name
	local var_1_3 = getProxy(FleetProxy)

	if not var_1_3.getFleetById(var_1_1):
		pg.TipsMgr.GetInstance().ShowTips(i18n("fleet_error_no_fleet"))

		return

	if not nameValidityCheck(var_1_2, 2, 24, {
		"spece_illegal_tip",
		"login_newPlayerScene_name_tooShort",
		"login_newPlayerScene_name_tooLong",
		"playerinfo_mask_word"
	}):
		return

	pg.ConnectionMgr.GetInstance().Send(12104, {
		id = var_1_1,
		name = var_1_2
	}, 12105, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_3.renameFleet(var_1_1, var_1_2)
			arg_1_0.sendNotification(GAME.RENAME_FLEET_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result]))

return var_0_0
