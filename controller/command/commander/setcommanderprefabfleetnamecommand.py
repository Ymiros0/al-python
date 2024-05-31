local var_0_0 = class("SetCommanderPrefabFleetNameCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.name
	local var_1_3 = var_1_0.onFailed
	local var_1_4 = getProxy(CommanderProxy).getPrefabFleetById(var_1_1)

	if var_1_4.getName() == var_1_2 or var_1_2 == "":
		if var_1_3:
			var_1_3()

		pg.TipsMgr.GetInstance().ShowTips(i18n("login_newPlayerScene_name_tooShort"))

		return

	local var_1_5, var_1_6 = var_1_4.canRename()

	if not var_1_5:
		pg.TipsMgr.GetInstance().ShowTips(var_1_6)

		if var_1_3:
			var_1_3()

		return

	if not nameValidityCheck(var_1_2, 0, 12, {
		"spece_illegal_tip",
		"login_newPlayerScene_name_tooShort",
		"login_newPlayerScene_name_tooLong",
		"playerinfo_mask_word"
	}):
		if var_1_3:
			var_1_3()

		return

	pg.ConnectionMgr.GetInstance().Send(25024, {
		id = var_1_1,
		name = var_1_2
	}, 25025, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(CommanderProxy).updatePrefabFleetName(var_1_1, var_1_2)
			arg_1_0.sendNotification(GAME.SET_COMMANDER_PREFAB_NAME_DONE)
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_prefab_rename_success"))
		else
			if var_1_3:
				var_1_3()

			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result]))

return var_0_0
