local var_0_0 = class("WorldBossPtRecoverCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = nowWorld().GetBossProxy()

	if var_1_0.isMaxPt():
		return

	local var_1_1 = var_1_0.GetNextReconveTime()
	local var_1_2 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_1_3 = var_1_0.GetRecoverPtTime()

	if var_1_1 <= var_1_2:
		local var_1_4 = var_1_2 - var_1_1

		var_1_0.increasePt()

		if not var_1_0.isMaxPt():
			while var_1_3 <= var_1_4:
				var_1_0.increasePt()

				var_1_4 = var_1_4 - var_1_3

			local var_1_5 = var_1_2 + (var_1_3 - var_1_4)

			var_1_0.updatePtTime(var_1_5)

	arg_1_0.sendNotification(GAME.WORLD_BOSS_PT_RECOVER_DONE)

return var_0_0
