local var_0_0 = class("ReserveCommanderBoxCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().count
	local var_1_1 = getProxy(CommanderProxy)
	local var_1_2 = var_1_1.getBoxUseCnt()

	if var_1_2 == CommanderConst.MAX_GETBOX_CNT:
		pg.TipsMgr.GetInstance().ShowTips(i18n("commander_reserve_count_is_max"))

		return

	local var_1_3 = getProxy(PlayerProxy)
	local var_1_4 = var_1_3.getData()
	local var_1_5 = 0

	for iter_1_0 = var_1_2, var_1_2 + var_1_0 - 1:
		var_1_5 = var_1_5 + CommanderConst.getBoxComsume(iter_1_0)

	if var_1_5 > var_1_4.gold:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

		return

	pg.ConnectionMgr.GetInstance().Send(25018, {
		type = var_1_0
	}, 25019, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_4.consume({
				gold = var_1_5
			})
			var_1_3.updatePlayer(var_1_4)

			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.awards)

			var_1_1.updateBoxUseCnt(var_1_0)
			arg_1_0.sendNotification(GAME.COMMANDER_RESERVE_BOX_DONE, {
				awards = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_lock_erro", arg_2_0.result)))

return var_0_0
