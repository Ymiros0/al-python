local var_0_0 = class("GetCommanderCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.callback
	local var_1_3 = defaultValue(var_1_0.notify, True)
	local var_1_4 = getProxy(CommanderProxy)
	local var_1_5 = var_1_4.getBoxById(var_1_1)

	if getProxy(PlayerProxy).getRawData().commanderBagMax <= var_1_4.getCommanderCnt():
		pg.TipsMgr.GetInstance().ShowTips(i18n("commander_capcity_is_max"))

		if var_1_2:
			var_1_2()

		return

	if var_1_5.getState() != CommanderBox.STATE_FINISHED:
		return

	pg.ConnectionMgr.GetInstance().Send(25004, {
		boxid = var_1_1
	}, 25005, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = Commander.New(arg_2_0.commander)

			var_1_4.addCommander(var_2_0)
			var_1_5.finish()

			if var_1_3:
				arg_1_0.sendNotification(GAME.COMMANDER_ON_OPEN_BOX_DONE, {
					commander = var_2_0.clone(),
					boxId = var_1_1,
					callback = var_1_2
				})
			elif var_1_2:
				var_1_2(var_2_0)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_acquire_erro", arg_2_0.result))

			if var_1_2:
				var_1_2())

return var_0_0
